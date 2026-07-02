#!/usr/bin/env python3
"""Lightweight consistency checks for The Grammar of Apostasy.

This script intentionally checks mechanical consistency only. It does not replace
human theological judgment.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "architecture-of-apostasy"
GRAMMAR = PROJECT / "grammar-of-apostasy"
AI_SYSTEM = ROOT / "ai-system"

REQUIRED_FILES = [
    PROJECT / "README.md",
    PROJECT / "aspects" / "README.md",
    PROJECT / "aspects" / "visual-theology" / "README.md",
    PROJECT / "aspects" / "visual-theology" / "gallery-canon.md",
    GRAMMAR / "README.md",
    GRAMMAR / "constitution.md",
    GRAMMAR / "canonical-ontology.md",
    GRAMMAR / "editorial-style-guide.md",
    GRAMMAR / "agent-contracts.md",
    GRAMMAR / "checklists" / "theological-validation.md",
    AI_SYSTEM / "README.md",
    AI_SYSTEM / "schemas" / "agent-output.schema.json",
    AI_SYSTEM / "schemas" / "chapter.schema.json",
    AI_SYSTEM / "schemas" / "knowledge-graph.schema.json",
    AI_SYSTEM / "schemas" / "status-metadata.schema.json",
    AI_SYSTEM / "graphs" / "concept-dependency-graph.yml",
    AI_SYSTEM / "roadmap" / "volumes.yml",
    AI_SYSTEM / "checklists" / "chapter-front-matter-template.yml",
    AI_SYSTEM / "scripts" / "validate_public_front_matter.py",
]

CANONICAL_TERMS = [
    "Logos",
    "Disease Logos",
    "Fallen Liturgy",
    "Chemical Temple",
    "Principalities",
    "Restoration",
]

PROMPT_REQUIRED_HEADINGS = [
    "## Purpose",
    "## Role",
    "## Inputs",
    "## Workflow",
    "## Output",
    "## Validation",
]

EXPECTED_PROMPTS = [
    "biblical-agent.md",
    "historical-theology-agent.md",
    "philosophy-agent.md",
    "psychology-agent.md",
    "anthropology-agent.md",
    "systems-mapping-agent.md",
    "diagram-agent.md",
    "critique-agent.md",
    "editorial-agent.md",
    "canonical-integration-agent.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")


def check_json(errors: list[str]) -> None:
    for path in (AI_SYSTEM / "schemas").glob("*.json"):
        try:
            json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_constitution_terms(errors: list[str]) -> None:
    text = read_text(GRAMMAR / "constitution.md")
    for term in CANONICAL_TERMS:
        if term not in text:
            errors.append(f"Constitution missing canonical term: {term}")


def check_prompts(errors: list[str]) -> None:
    prompts_dir = AI_SYSTEM / "prompts"
    for filename in EXPECTED_PROMPTS:
        path = prompts_dir / filename
        if not path.exists():
            errors.append(f"Missing prompt template: {path.relative_to(ROOT)}")
            continue
        text = read_text(path)
        for heading in PROMPT_REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.relative_to(ROOT)} missing heading: {heading}")


def check_stale_project_paths(errors: list[str]) -> None:
    allowed = {"_site", ".git"}
    stale_path = "project" + "/"
    stale_scaffold = "README" + "_PROJECT_SCAFFOLD"
    for path in ROOT.rglob("*"):
        if any(part in allowed for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".qmd", ".yml", ".yaml", ".json", ".py"}:
            continue
        text = read_text(path)
        if stale_path in text or stale_scaffold in text:
            errors.append(f"Stale project path reference in {path.relative_to(ROOT)}")


def check_restoration_marker(errors: list[str]) -> None:
    text = read_text(GRAMMAR / "constitution.md")
    markers = ["Christological resolution", "Restoration", "Christ exposes"]
    for marker in markers:
        if marker not in text:
            errors.append(f"Constitution missing restoration marker: {marker}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    if not errors:
        check_json(errors)
        check_constitution_terms(errors)
        check_prompts(errors)
        check_stale_project_paths(errors)
        check_restoration_marker(errors)

    if errors:
        print("Theological consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Theological consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
