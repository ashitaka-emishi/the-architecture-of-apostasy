#!/usr/bin/env python3
"""Generate the publication-status registry from library.qmd.

library.qmd's catalog tables are the single source of truth for each public
page's Status/Category. This script parses those tables and writes a JSON
registry keyed by rendered relative path, so publication_status_postprocess.py
can inject a status banner into the rendered HTML without any hand-maintained
duplicate of the catalog and without editing markdown/ or raw/ content.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIBRARY_PATH = ROOT / "library.qmd"
OUTPUT_PATH = ROOT / "ai-system" / "data" / "publication-status.json"

ROW_PATTERN = re.compile(
    r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*$"
)


def rendered_path(link: str) -> str | None:
    if link.endswith(".qmd"):
        return link[: -len(".qmd")] + ".html"
    if link.endswith(".md"):
        return link[: -len(".md")] + ".html"
    return None


def parse_library(text: str) -> dict[str, dict[str, object]]:
    registry: dict[str, dict[str, object]] = {}
    for line in text.splitlines():
        match = ROW_PATTERN.match(line.strip())
        if not match:
            continue
        label, link, category, status, summary = (part.strip() for part in match.groups())
        rel_path = rendered_path(link)
        if rel_path is None:
            continue
        statuses = [item.strip() for item in status.split(",") if item.strip()]
        if not statuses:
            continue
        registry[rel_path] = {
            "label": label,
            "category": category,
            "statuses": statuses,
            "summary": summary,
        }
    return registry


def main() -> int:
    text = LIBRARY_PATH.read_text(encoding="utf-8")
    registry = parse_library(text)
    if not registry:
        print("No catalog rows parsed from library.qmd; refusing to write an empty registry.", file=sys.stderr)
        return 1
    OUTPUT_PATH.write_text(json.dumps(registry, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {len(registry)} entries to {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
