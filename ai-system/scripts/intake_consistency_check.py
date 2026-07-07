#!/usr/bin/env python3
"""Report intake consistency gaps for public essays and raw source files.

This script separates reporting from hard intake failures. Existing citation and
Christological-resolution gaps are reported for editor attention; newly added raw
PDFs are treated as errors when they are missing source-note wiring.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "archive.qmd"
MARKDOWN_DIR = ROOT / "markdown"
RAW_DIR = ROOT / "raw"
RAW_SOURCE_NOTE_INDEXES = [
    RAW_DIR / "source-roadmap.md",
    RAW_DIR / "website-update.md",
]

CITATION_PATTERNS = [
    re.compile(r"https?://"),
    re.compile(r"\[[^\]]+\]\([^)]+\)"),
    re.compile(r"\[\^[^\]]+\]"),
    re.compile(r"\b(?:Source|Sources|References|Bibliography|Works Cited)\b", re.IGNORECASE),
    re.compile(
        r"\b(?:Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|Samuel|Kings|Chronicles|Ezra|Nehemiah|Esther|Job|Psalm|Proverbs|Ecclesiastes|Song|Isaiah|Jeremiah|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|Ephesians|Philippians|Colossians|Thessalonians|Timothy|Titus|Philemon|Hebrews|James|Peter|Jude|Revelation)\s+\d+:\d+",
        re.IGNORECASE,
    ),
]

CHRISTOLOGICAL_MARKERS = [
    "Christological resolution",
    "Christ exposes",
    "Christ judges",
    "Christ disarms",
    "Christ restores",
    "Restoration",
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_git(args: list[str]) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def added_paths(base_ref: str) -> set[Path]:
    paths: set[Path] = set()
    for line in run_git(["diff", "--name-only", "--diff-filter=A", f"{base_ref}...HEAD"]):
        paths.add(ROOT / line)
    for line in run_git(["ls-files", "--others", "--exclude-standard"]):
        paths.add(ROOT / line)
    return paths


def public_essay_paths() -> list[Path]:
    return sorted(path for path in MARKDOWN_DIR.glob("*.md") if path.is_file())


def archive_status_by_path() -> dict[str, str]:
    statuses: dict[str, str] = {}
    row_pattern = re.compile(r"\| \[[^\]]+\]\((markdown/[^)]+\.md)\) \| [^|]+ \| ([^|]+) \|")
    for match in row_pattern.finditer(read_text(ARCHIVE)):
        statuses[match.group(1)] = match.group(2).strip()
    return statuses


def has_visible_citation(text: str) -> bool:
    return any(pattern.search(text) for pattern in CITATION_PATTERNS)


def citation_report() -> list[str]:
    missing: list[str] = []
    for path in public_essay_paths():
        if path.name == "gallery.md":
            continue
        if not has_visible_citation(read_text(path)):
            missing.append(rel(path))
    return missing


def christological_resolution_report(statuses: dict[str, str]) -> list[str]:
    missing: list[str] = []
    for archive_path, status in statuses.items():
        if "Canonical" not in status:
            continue
        path = ROOT / archive_path
        if path.exists() and not any(marker in read_text(path) for marker in CHRISTOLOGICAL_MARKERS):
            missing.append(archive_path)
    return missing


def source_note_candidates(pdf_path: Path) -> list[Path]:
    return [
        pdf_path.with_suffix(".md"),
        pdf_path.with_suffix(".txt"),
        RAW_DIR / f"{pdf_path.stem}.source.md",
        RAW_DIR / f"{pdf_path.stem}.source.txt",
    ]


def has_source_note(pdf_path: Path) -> bool:
    if any(path.exists() for path in source_note_candidates(pdf_path)):
        return True
    haystacks = [read_text(path) for path in RAW_SOURCE_NOTE_INDEXES if path.exists()]
    filename = pdf_path.name
    stem = pdf_path.stem
    return any(filename in text or stem in text for text in haystacks)


def new_raw_pdf_source_note_errors(new_paths: set[Path]) -> list[str]:
    errors: list[str] = []
    for path in sorted(new_paths):
        if path.suffix.lower() != ".pdf" or not path.is_file():
            continue
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            continue
        if not relative.parts or relative.parts[0] != "raw":
            continue
        if not has_source_note(path):
            errors.append(f"{rel(path)} is a new raw PDF without a corresponding source note")
    return errors


def print_report(label: str, items: list[str]) -> None:
    print(f"{label}: {len(items)}")
    for item in items:
        print(f"- {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-ref",
        default="origin/master",
        help="Base ref for detecting newly added intake files.",
    )
    args = parser.parse_args()

    new_paths = added_paths(args.base_ref)
    statuses = archive_status_by_path()

    missing_citations = citation_report()
    missing_resolution = christological_resolution_report(statuses)
    errors = new_raw_pdf_source_note_errors(new_paths)

    print("Intake consistency report:")
    print_report("Essays lacking visible citations", missing_citations)
    print_report("Canonical-marked essays missing Christological resolution markers", missing_resolution)
    print_report("New intake errors", errors)

    if errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
