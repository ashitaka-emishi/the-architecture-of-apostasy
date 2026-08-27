#!/usr/bin/env python3
"""Inject publication-status banners into rendered essay pages.

Mirrors seo_postprocess.py's approach: quarto render produces static HTML,
and this script edits that rendered output in place using the registry from
ai-system/data/publication-status.json (see generate_publication_status.py).
This never touches markdown/ or raw/ source content — only the generated
_site/ output.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "_site"
REGISTRY_PATH = ROOT / "ai-system" / "data" / "publication-status.json"
INSERT_AFTER = '<main class="content" id="quarto-document-content">'
BANNER_MARKER = "aoa-status-banner"
BANNER_PATTERN = re.compile(
    r'<div class="aoa-status-banner">.*?<p class="aoa-status-banner-links">.*?</p></div>',
    re.DOTALL,
)

STATUS_STYLES = {
    "foundation": "accent",
    "canonical draft": "warning",
    "needs source strengthening": "warning",
    "needs rival readings": "warning",
    "needs claim narrowing": "warning",
    "needs pastoral review": "warning",
    "devotional/mythic": "muted",
    "working note": "muted",
    "source material": "muted",
    "public essay": "neutral",
}


def load_registry() -> dict[str, dict[str, object]]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def depth_prefix(rel_path: str) -> str:
    return "../" * (len(Path(rel_path).parts) - 1)


def badge_style(status: str) -> str:
    return STATUS_STYLES.get(status.lower(), "neutral")


def render_banner(rel_path: str, entry: dict[str, object]) -> str:
    prefix = depth_prefix(rel_path)
    statuses = entry["statuses"]
    summary = str(entry["summary"])

    badges = "".join(
        f'<span class="aoa-status-badge aoa-status-badge--{badge_style(status)}">{html.escape(status)}</span>'
        for status in statuses
    )

    return (
        f'<div class="{BANNER_MARKER}">'
        f'<div class="aoa-status-banner-badges">{badges}</div>'
        f'<p class="aoa-status-banner-summary">{html.escape(summary)}</p>'
        f'<p class="aoa-status-banner-links">'
        f'<a href="{prefix}library.html">Library Catalog</a>'
        f" &middot; "
        f'<a href="{prefix}method.html">Method</a>'
        f"</p>"
        f"</div>"
    )


def is_essay_page(rel_path: str, entry: dict[str, object]) -> bool:
    return rel_path.startswith("markdown/") and str(entry.get("category")) != "Image"


def rendered_pages(output_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in output_dir.rglob("*.html")
        if "site-assets" not in path.relative_to(output_dir).parts
    )


def apply_banners() -> list[str]:
    registry = load_registry()
    errors: list[str] = []

    for path in rendered_pages(OUTPUT_DIR):
        rel_path = path.relative_to(OUTPUT_DIR).as_posix()
        entry = registry.get(rel_path)
        if entry is None:
            continue

        text = path.read_text(encoding="utf-8")
        if not is_essay_page(rel_path, entry):
            if BANNER_MARKER in text:
                text = BANNER_PATTERN.sub("", text, count=1)
                path.write_text(text, encoding="utf-8")
            continue

        if BANNER_MARKER in text:
            continue
        if INSERT_AFTER not in text:
            errors.append(f"{rel_path} is missing the expected content wrapper to inject into")
            continue

        banner = render_banner(rel_path, entry)
        text = text.replace(INSERT_AFTER, INSERT_AFTER + banner, 1)
        path.write_text(text, encoding="utf-8")

    return errors


def check_banners() -> list[str]:
    registry = load_registry()
    errors: list[str] = []

    for path in rendered_pages(OUTPUT_DIR):
        rel_path = path.relative_to(OUTPUT_DIR).as_posix()
        entry = registry.get(rel_path)
        if entry is None:
            continue
        text = path.read_text(encoding="utf-8")
        if is_essay_page(rel_path, entry):
            if BANNER_MARKER not in text:
                errors.append(f"{rel_path} is missing the publication-status banner")
        elif BANNER_MARKER in text:
            errors.append(f"{rel_path} has a publication-status banner but is not an essay page")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify banners instead of applying them.")
    args = parser.parse_args()

    if not OUTPUT_DIR.exists():
        print("_site does not exist; run `quarto render` first.", file=sys.stderr)
        return 1

    errors = check_banners() if args.check else apply_banners()
    if errors:
        action = "Publication-status check failed" if args.check else "Publication-status postprocess failed"
        print(f"{action}:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.check:
        print("Publication-status check passed.")
    else:
        print("Publication-status banners applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
