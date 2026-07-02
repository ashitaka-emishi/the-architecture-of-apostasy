#!/usr/bin/env python3
"""Validate front matter on newly added public Markdown files.

The check is mechanical: it requires a YAML front matter block with a title and
validates optional status metadata fields when they are present.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "ai-system" / "schemas" / "status-metadata.schema.json"
PUBLIC_SUFFIXES = {".md", ".qmd"}
EXCLUDED_PARTS = {
    ".git",
    ".github",
    ".quarto",
    "_site",
    "ai-system",
    "raw",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


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


def default_candidate_paths(base_ref: str) -> list[Path]:
    paths: set[Path] = set()
    for line in run_git(["diff", "--name-only", "--diff-filter=A", f"{base_ref}...HEAD"]):
        paths.add(ROOT / line)
    for line in run_git(["ls-files", "--others", "--exclude-standard"]):
        paths.add(ROOT / line)
    return sorted(paths)


def is_public_markdown(path: Path) -> bool:
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return False
    return (
        path.suffix in PUBLIC_SUFFIXES
        and path.is_file()
        and not any(part in EXCLUDED_PARTS for part in relative.parts)
    )


def parse_front_matter(path: Path) -> tuple[dict[str, object], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{rel(path)} missing opening front matter delimiter"]

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
    if end_index is None:
        return {}, [f"{rel(path)} missing closing front matter delimiter"]

    data: dict[str, object] = {}
    current_key: str | None = None
    errors: list[str] = []

    for raw_line in lines[1:end_index]:
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            if current_key is None:
                continue
            item = raw_line.strip()
            if not item.startswith("- "):
                continue
            current_value = data.setdefault(current_key, [])
            if not isinstance(current_value, list):
                errors.append(f"{rel(path)} front matter field '{current_key}' mixes scalar and list values")
                continue
            current_value.append(item[2:].strip().strip("\"'"))
            continue
        if ":" not in raw_line:
            errors.append(f"{rel(path)} front matter line is not a key/value pair: {raw_line}")
            current_key = None
            continue
        key, value = raw_line.split(":", 1)
        current_key = key.strip()
        value = value.strip()
        if value == "":
            data[current_key] = []
        elif value.startswith("[") and value.endswith("]"):
            data[current_key] = [
                item.strip().strip("\"'")
                for item in value[1:-1].split(",")
                if item.strip()
            ]
        else:
            data[current_key] = value.strip("\"'")

    return data, errors


def schema_properties() -> dict[str, dict[str, object]]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return schema.get("properties", {})


def validate_metadata(
    path: Path,
    metadata: dict[str, object],
    properties: dict[str, dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    title = metadata.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append(f"{rel(path)} front matter must include a non-empty title")

    for key, rule in properties.items():
        if key not in metadata:
            continue
        value = metadata[key]
        expected_type = rule.get("type")
        if expected_type == "array":
            if not isinstance(value, list):
                errors.append(f"{rel(path)} front matter field '{key}' must be a list")
                continue
            if not value:
                errors.append(f"{rel(path)} front matter field '{key}' must not be empty when present")
                continue
            if len(value) != len(set(value)):
                errors.append(f"{rel(path)} front matter field '{key}' must not contain duplicates")
            blank = [item for item in value if not item.strip()]
            if blank:
                errors.append(f"{rel(path)} front matter field '{key}' must not contain blank values")
            allowed = set(rule.get("items", {}).get("enum", []))
            invalid = [item for item in value if allowed and item not in allowed]
            if invalid:
                errors.append(
                    f"{rel(path)} front matter field '{key}' has invalid values: {', '.join(invalid)}"
                )
        elif expected_type == "string":
            if not isinstance(value, str):
                errors.append(f"{rel(path)} front matter field '{key}' must be a string")
                continue
            allowed = set(rule.get("enum", []))
            if value not in allowed:
                errors.append(f"{rel(path)} front matter field '{key}' has invalid value: {value}")
        else:
            errors.append(f"{rel(path)} front matter field '{key}' has unsupported schema type")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Specific Markdown files to validate.")
    parser.add_argument(
        "--base-ref",
        default="origin/master",
        help="Base ref for detecting newly added public Markdown files.",
    )
    args = parser.parse_args()

    candidates = [ROOT / path for path in args.paths] if args.paths else default_candidate_paths(args.base_ref)
    public_files = [path for path in candidates if is_public_markdown(path)]
    properties = schema_properties()
    errors: list[str] = []

    for path in public_files:
        metadata, parse_errors = parse_front_matter(path)
        errors.extend(parse_errors)
        if parse_errors:
            continue
        errors.extend(validate_metadata(path, metadata, properties))

    if errors:
        print("Public front matter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if public_files:
        print(f"Public front matter validation passed for {len(public_files)} file(s).")
    else:
        print("Public front matter validation passed; no new public Markdown files found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
