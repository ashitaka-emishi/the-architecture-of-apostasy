# Intake Staging Folder

Place new documents, PDFs, images, and mixed batches here when they need to be
ingested into the site.

This folder is a landing zone, not a permanent archive. After intake succeeds,
the files you placed here should be moved into their real homes and removed from
this folder. Keep this `README.md` in place.

## How To Use

1. Drop new files into `intake/`.
2. Ask Codex to run the intake process.
3. Codex inventories every file, reads text files, and visually inspects images.
4. Codex classifies each item by type, theology, source needs, and site fit.
5. Codex proposes a placement plan when the batch is non-trivial or ambiguous.
6. Codex moves/renames accepted files into the correct project locations.
7. Codex updates the public site pages that list or display the new material.
8. Codex runs validation before declaring the intake complete.

## Placement Rules

- Original source files, PDFs, drafts, OCR, and source notes go in `raw/`.
- Public essay reading copies go in `markdown/` with kebab-case filenames.
- Public image assets go in `gallery/` with descriptive kebab-case filenames.
- Image source notes, prompts, OCR, and inspection notes go in `raw/images/`.
- Individual essays are listed in `essays.qmd`.
- Public images are listed in `images.qmd` and `markdown/gallery.md`.
- Broader editorial placement may also update `archive.qmd` or
  `reading-paths.qmd` when the new item clearly belongs there.

## Required Intake Checks

Every intake pass should answer these questions before publication:

- What kind of artifact is this?
- Does it belong on the public site, in raw preservation, or in canonical review?
- What created good, corruption, false logos, or fallen liturgy is involved?
- Does it clarify the path of return, or merely enlarge the archive?
- Does it need citations, rival readings, or pastoral-risk review?
- Does it fit an existing website category without inventing a new one?
- Does it preserve source material faithfully?
- Does it avoid editing unrelated existing essay content?

Then run:

```bash
python3 ai-system/scripts/intake_consistency_check.py
python3 ai-system/scripts/theological_consistency_check.py
quarto render
```

## Images

Images should be viewed before placement. Do not rely on staging filenames.

For each accepted public image:

- rename it descriptively in kebab-case;
- move it to `gallery/`;
- add or update inspection/source notes in `raw/images/` when useful;
- add an entry to `markdown/gallery.md`;
- add a matching entry to `images.qmd`;
- connect it to a companion essay when the relationship is clear.

## Essays With Companion Images

When an ingested Markdown essay has a companion image in the same intake batch,
or when the source document already clearly pairs the essay with an image:

1. Move the image to `gallery/` using the image rules above.
2. Place the image near the top of the essay, after the `# Title` and any
   `Source:` line, unless the essay already includes that image in an
   appropriate location.
3. Use a normal Markdown image embed:

   ```markdown
   ![Descriptive Alt Text](../gallery/descriptive-image-name.jpg)
   ```

4. Mention the essay relationship in the image's `Comments:` line in
   `markdown/gallery.md`.

Do not force an image pairing when the relationship is unclear.

## Ambiguous Or Blocked Files

Leave ambiguous files in `intake/` and report why they were not placed.
Examples include unsupported formats, unclear publication status, unclear
theological fit, missing source context, or material that needs human editorial
approval before publication.
