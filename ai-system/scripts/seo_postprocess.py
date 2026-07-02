#!/usr/bin/env python3
"""Apply and verify SEO metadata in the rendered Quarto site.

Quarto generates the sitemap and robots.txt from the site URL, but this project
keeps essay reading copies as plain Markdown without YAML front matter. The
central metadata map lets us add stable search/social tags without changing
essay bodies or duplicating visible headings.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "_site"
METADATA_PATH = ROOT / "site-assets" / "seo-metadata.json"
QUARTO_CONFIG = ROOT / "_quarto.yml"
SITE_NAME = "The Architecture of Apostasy"

CONTROLLED_META = {
    "description",
    "og:description",
    "og:image",
    "og:site_name",
    "og:title",
    "og:type",
    "og:url",
    "twitter:card",
    "twitter:description",
    "twitter:image",
    "twitter:title",
}


def load_metadata() -> dict[str, object]:
    return json.loads(METADATA_PATH.read_text(encoding="utf-8"))


def read_site_url() -> str:
    text = QUARTO_CONFIG.read_text(encoding="utf-8")
    match = re.search(r"^\s*site-url:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text, re.MULTILINE)
    if not match:
        raise RuntimeError("_quarto.yml is missing website.site-url")
    return match.group(1).rstrip("/")


def page_url(site_url: str, rel_path: str) -> str:
    if rel_path == "index.html":
        return f"{site_url}/"
    return f"{site_url}/{rel_path}"


def absolute_asset_url(site_url: str, asset_path: str) -> str:
    return urljoin(f"{site_url}/", asset_path)


def html_tag_attrs(tag: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for key, _, quote, value in re.findall(r"([:\w-]+)(\s*=\s*)([\"'])(.*?)\3", tag):
        attrs[key.lower()] = html.unescape(value)
    return attrs


def remove_controlled_tags(head: str) -> str:
    head = re.sub(r"\s*<title>.*?</title>\s*", "\n", head, flags=re.IGNORECASE | re.DOTALL)
    head = re.sub(r"\s*<link\b[^>]*\brel=[\"']canonical[\"'][^>]*>\s*", "\n", head, flags=re.IGNORECASE)

    def keep_meta(match: re.Match[str]) -> str:
        tag = match.group(0)
        attrs = html_tag_attrs(tag)
        key = attrs.get("name") or attrs.get("property")
        return "" if key in CONTROLLED_META else tag

    return re.sub(r"\s*<meta\b[^>]*>\s*", keep_meta, head, flags=re.IGNORECASE)


def render_tags(site_url: str, rel_path: str, default_image: str, data: dict[str, str]) -> str:
    title = data["title"].strip()
    description = data["description"].strip()
    canonical = page_url(site_url, rel_path)
    image_path = data.get("image") or default_image
    image_url = absolute_asset_url(site_url, image_path)
    html_title = SITE_NAME if rel_path == "index.html" else f"{title} - {SITE_NAME}"
    page_type = "website" if rel_path == "index.html" else "article"

    def esc(value: str) -> str:
        return html.escape(value, quote=True)

    return "\n".join(
        [
            f"<title>{esc(html_title)}</title>",
            f'<meta name="description" content="{esc(description)}">',
            f'<link rel="canonical" href="{esc(canonical)}">',
            f'<meta property="og:title" content="{esc(title)}">',
            f'<meta property="og:description" content="{esc(description)}">',
            f'<meta property="og:url" content="{esc(canonical)}">',
            f'<meta property="og:site_name" content="{esc(SITE_NAME)}">',
            f'<meta property="og:type" content="{page_type}">',
            f'<meta property="og:image" content="{esc(image_url)}">',
            '<meta name="twitter:card" content="summary_large_image">',
            f'<meta name="twitter:title" content="{esc(title)}">',
            f'<meta name="twitter:description" content="{esc(description)}">',
            f'<meta name="twitter:image" content="{esc(image_url)}">',
        ]
    )


def rendered_pages(output_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in output_dir.rglob("*.html")
        if "site-assets" not in path.relative_to(output_dir).parts
    )


def apply_metadata() -> list[str]:
    metadata = load_metadata()
    site_url = read_site_url()
    default_image = str(metadata["default_image"])
    pages = metadata["pages"]
    errors: list[str] = []

    for path in rendered_pages(OUTPUT_DIR):
        rel_path = path.relative_to(OUTPUT_DIR).as_posix()
        data = pages.get(rel_path)
        if not isinstance(data, dict):
            errors.append(f"{rel_path} is missing from {METADATA_PATH.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")
        match = re.search(r"(<head[^>]*>)(.*?)(</head>)", text, flags=re.IGNORECASE | re.DOTALL)
        if not match:
            errors.append(f"{rel_path} has no <head> section")
            continue

        head_open, head_inner, head_close = match.groups()
        new_head = remove_controlled_tags(head_inner).rstrip()
        new_head = f"{new_head}\n{render_tags(site_url, rel_path, default_image, data)}\n"
        path.write_text(text[: match.start()] + head_open + new_head + head_close + text[match.end() :], encoding="utf-8")

    return errors


def check_metadata() -> list[str]:
    metadata = load_metadata()
    site_url = read_site_url()
    default_image = str(metadata["default_image"])
    pages = metadata["pages"]
    errors: list[str] = []

    for rel_path, data in pages.items():
        if not isinstance(data, dict):
            errors.append(f"{rel_path} metadata must be an object")
            continue
        for key in ("title", "description"):
            value = data.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{rel_path} metadata is missing {key}")
        image = data.get("image", default_image)
        if not (ROOT / image).exists():
            errors.append(f"{rel_path} references missing image {image}")

    for path in rendered_pages(OUTPUT_DIR):
        rel_path = path.relative_to(OUTPUT_DIR).as_posix()
        data = pages.get(rel_path)
        if not isinstance(data, dict):
            errors.append(f"{rel_path} is missing from {METADATA_PATH.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        title = data["title"].strip()
        description = data["description"].strip()
        canonical = page_url(site_url, rel_path)
        image_url = absolute_asset_url(site_url, data.get("image") or default_image)
        html_title = SITE_NAME if rel_path == "index.html" else f"{title} - {SITE_NAME}"

        expected = {
            "title": f"<title>{html.escape(html_title, quote=True)}</title>",
            "description": f'<meta name="description" content="{html.escape(description, quote=True)}">',
            "canonical": f'<link rel="canonical" href="{html.escape(canonical, quote=True)}">',
            "og:title": f'<meta property="og:title" content="{html.escape(title, quote=True)}">',
            "og:description": f'<meta property="og:description" content="{html.escape(description, quote=True)}">',
            "og:url": f'<meta property="og:url" content="{html.escape(canonical, quote=True)}">',
            "og:image": f'<meta property="og:image" content="{html.escape(image_url, quote=True)}">',
            "twitter:card": '<meta name="twitter:card" content="summary_large_image">',
            "twitter:title": f'<meta name="twitter:title" content="{html.escape(title, quote=True)}">',
            "twitter:description": f'<meta name="twitter:description" content="{html.escape(description, quote=True)}">',
            "twitter:image": f'<meta name="twitter:image" content="{html.escape(image_url, quote=True)}">',
        }
        for label, snippet in expected.items():
            if snippet not in text:
                errors.append(f"{rel_path} missing expected {label} tag")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify rendered SEO tags instead of applying them.")
    args = parser.parse_args()

    if not OUTPUT_DIR.exists():
        print("_site does not exist; run `quarto render` first.", file=sys.stderr)
        return 1

    errors = check_metadata() if args.check else apply_metadata()
    if errors:
        action = "SEO metadata check failed" if args.check else "SEO metadata postprocess failed"
        print(f"{action}:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.check:
        print("SEO metadata check passed.")
    else:
        print("SEO metadata applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
