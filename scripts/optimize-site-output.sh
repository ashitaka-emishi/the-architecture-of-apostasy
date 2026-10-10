#!/usr/bin/env bash
set -euo pipefail

site_dir="_site"
gallery_dir="${site_dir}/gallery"

if [[ ! -d "${gallery_dir}" ]]; then
  echo "Expected ${gallery_dir} to exist after Quarto render." >&2
  exit 1
fi

if ! command -v cwebp >/dev/null 2>&1; then
  echo "cwebp is required to generate optimized site images." >&2
  exit 1
fi

cwebp -quiet -q 78 -resize 1000 0 "gallery/pillars.png" -o "${gallery_dir}/pillars-1000.webp"
cwebp -quiet -q 78 -resize 1000 0 "gallery/the-keeping.png" -o "${gallery_dir}/the-keeping-1000.webp"
cwebp -quiet -q 78 -resize 1000 0 "gallery/the-measure.png" -o "${gallery_dir}/the-measure-1000.webp"
cwebp -quiet -q 74 -resize 640 0 "gallery/aoa-logo-home.webp" -o "${gallery_dir}/aoa-logo-home-640.webp"
cwebp -quiet -q 78 -resize 960 0 "gallery/aoa-logo-home.webp" -o "${gallery_dir}/aoa-logo-home-960.webp"
cwebp -quiet -q 78 -resize 96 0 "gallery/aoa-logo-emblem.webp" -o "${gallery_dir}/aoa-logo-emblem-nav.webp"

find "${site_dir}" -name '*.html' -print0 | while IFS= read -r -d '' html; do
  perl -0pi -e '
    s/ role="menu"(?=[^>]*aria-label="Toggle navigation")//g;
    s/<link href="([^"]*)site_libs\/bootstrap\/bootstrap-[^"]+\.min\.css" rel="stylesheet"[^>]*>\n//g;
    s/<img src="(\.?\.?\/?gallery\/aoa-logo-emblem)\.webp" alt="The Architecture of Apostasy" class="navbar-logo ([^"]*)">/<img src="${1}-nav.webp" width="96" height="120" alt="The Architecture of Apostasy" class="navbar-logo $2" decoding="async">/g;
    s#<img src="gallery/aoa-logo-home\.webp" class="aoa-hero-logo img-fluid" alt="The Architecture of Apostasy brand image, carrying the site'"'"'s title treatment\.">#<picture><source srcset="gallery/aoa-logo-home-640.webp 640w, gallery/aoa-logo-home-960.webp 960w, gallery/aoa-logo-home.webp 1122w" sizes="(max-width: 640px) 76vw, 476px"><img src="gallery/aoa-logo-home-640.webp" width="640" height="800" class="aoa-hero-logo img-fluid" alt="The Architecture of Apostasy brand image, carrying the site'"'"'s title treatment." fetchpriority="high" decoding="async"></picture>#g;
    s#<img src="(\.?\.?/?)gallery/pillars\.png" class="path-image no-lightbox img-fluid" alt="A dark gold and black diagram titled The Path, The Keeping, and The Measure, showing a circular movement of diagnosis, fidelity, and discernment under Christ\.">#<img src="${1}gallery/pillars-1000.webp" width="1000" height="563" class="path-image no-lightbox img-fluid" alt="A dark gold and black diagram titled The Path, The Keeping, and The Measure, showing a circular movement of diagnosis, fidelity, and discernment under Christ." loading="lazy" decoding="async">#g;
    s#<img src="(\.?\.?/?)gallery/pillars\.png" class="path-image no-lightbox img-fluid figure-img">#<img src="${1}gallery/pillars-1000.webp" width="1000" height="563" class="path-image no-lightbox img-fluid figure-img" loading="lazy" decoding="async">#g;
    s#<img src="(\.?\.?/?)gallery/the-keeping\.png" class="([^"]*)" alt="A dark gold and black poster titled The Keeping, showing six stages: received life, the Troth, faithful attention, embodied loyalty, costly endurance, and communal witness\.">#<img src="${1}gallery/the-keeping-1000.webp" width="1000" height="563" class="$2" alt="A dark gold and black poster titled The Keeping, showing six stages: received life, the Troth, faithful attention, embodied loyalty, costly endurance, and communal witness." loading="lazy" decoding="async">#g;
    s#<img src="(\.?\.?/?)gallery/the-keeping\.png" class="path-image no-lightbox img-fluid figure-img">#<img src="${1}gallery/the-keeping-1000.webp" width="1000" height="563" class="path-image no-lightbox img-fluid figure-img" loading="lazy" decoding="async">#g;
    s#<img src="(\.?\.?/?)gallery/the-measure\.png" class="([^"]*)" alt="A dark gold and black poster titled The Measure, showing six stages for discerning what a life or institution serves: ruling logos, trained desire, embodied practice, asked sacrifice, revealed fruit, and Christic alignment\.">#<img src="${1}gallery/the-measure-1000.webp" width="1000" height="563" class="$2" alt="A dark gold and black poster titled The Measure, showing six stages for discerning what a life or institution serves: ruling logos, trained desire, embodied practice, asked sacrifice, revealed fruit, and Christic alignment." loading="lazy" decoding="async">#g;
    s#<img src="(\.?\.?/?)gallery/the-measure\.png" class="path-image no-lightbox img-fluid figure-img">#<img src="${1}gallery/the-measure-1000.webp" width="1000" height="563" class="path-image no-lightbox img-fluid figure-img" loading="lazy" decoding="async">#g;
  ' "${html}"
done
