---
name: format-ingestion
description: Ingest dropped files (images, essay drafts, PDFs, and other formats) from a staging folder — usually "intake" at the project root — into the correct project locations, integrate them into the relevant site/index pages, run project validation, and clear the ingested staging contents once everything lands correctly. Use when the user says to ingest, process, import, or "deal with" intake/ (or a similarly named drop folder), or asks to get new essays/images/files into the site or project.
---

# Format Ingestion

Takes whatever a user dumped into a staging folder (default `intake/` at the
project root) — images, markdown drafts, PDFs, mixed formats — and moves each
item to where it actually belongs in the project, wires it into the pages that
list/link that kind of content, validates the result, and clears the ingested
staging contents. The staging folder is a landing zone, never a final home for
content.

This skill is project-agnostic in shape but needs project-specific placement
rules to act correctly. Section "Project conventions" below documents the
current rules for **The Architecture of Apostasy** theology site
(`the-architecture-of-apostasy` / Quarto site in this repo). If invoked in a
different repository, do not assume those rules apply — derive placement from
that project's own CONTRIBUTING.md / README / existing folder structure
instead, and ask the user if it's genuinely ambiguous.

## When to use

- User mentions a staging/drop folder (commonly `intake/`) that needs sorting.
- User has added new essays, images, or source PDFs and wants them "in the
  project" / "on the site" / "integrated."
- User asks to clean up or process files sitting outside the normal project
  structure.

## When not to use

- Editing existing, already-placed essays or pages (this skill only ingests
  *new* material; it must never rewrite existing canonical content).
- General file organization unrelated to a drop/staging folder.

## Workflow

1. **Locate the staging folder.** Default to `intake/` at the project root.
   If it doesn't exist or contains only `README.md` / `.gitkeep`, say so and
   stop — nothing to do.
2. **Inventory every file** in the folder (including subfolders). For each
   file, determine: file type, apparent subject/title, and whether it pairs
   with another file in the folder (e.g. a `.md` draft and a `.pdf` export of
   the same essay are one logical item, not two).
3. **Read/view every file before deciding where it goes.** For images, actually
   view them (do not guess placement from the filename alone — staging
   filenames are often meaningless, e.g. a phone-camera timestamp). For text
   documents, read enough to understand subject and tone.
4. **Classify each item** using the project conventions below (or the target
   project's own conventions if this isn't the theology site).
5. **Plan the placement** for every item and present it as a short plan before
   writing anything, when the batch is more than a couple of files or when any
   item's category/placement is genuinely ambiguous. For a single obvious file,
   proceed directly.
6. **Execute placement**: copy/move files into their real homes with
   proper kebab-case public filenames, and update every index/listing page
   that needs to reference the new item (see per-type steps below). Never
   silently invent a new theological category or heading — if nothing existing
   fits, propose one and say so explicitly rather than filing it under a
   mismatched heading.
7. **For new essays with companion images, add the image near the top.** If a
   newly ingested Markdown essay has a clear companion image in the same
   staging batch, or the source itself clearly pairs the image with the essay,
   place the image after the `# Title` and any `Source:` line unless the essay
   already includes it in a suitable location. Also record the pairing in the
   image's `Comments:` line in `markdown/gallery.md`. Do not force a pairing
   when the relationship is unclear.
8. **Never edit the body of an existing essay or page** while ingesting new
   material — this mirrors the project's own guardrail in
   `raw/recommended-improvements.md` ("Do not modify existing essay content
   unless explicitly requested").
9. **Validate**: run `python3 ai-system/scripts/intake_consistency_check.py`,
   `quarto render`, and
   `python3 ai-system/scripts/theological_consistency_check.py` (theology site;
   substitute the target project's own build/lint/check commands elsewhere).
   Fix anything the ingestion itself broke.
10. **Clear ingested staging contents** — but only after every accepted file has
    been successfully placed and validation has passed. Preserve
    `intake/README.md`. If any file could not be placed (unrecognized format,
    ambiguous subject, failed validation), leave that file in the staging
    folder and tell the user why.
11. **Report a summary**: what arrived, where each item landed, which pages
    were updated, anything skipped and why.
12. **Do not `git add`, commit, or push.** Leave the resulting changes in the
    working tree for the user to review and commit themselves, unless they
    explicitly ask you to commit in this conversation.

## Project conventions (The Architecture of Apostasy theology site)

Source of truth: `CONTRIBUTING.md` at the repo root. Re-check it before acting
in case rules have changed; the mapping below reflects the structure observed
in this repo.

### Images → `gallery/`

1. View the image and write a one-sentence factual description (subject,
   composition, notable symbols) — no interpretive theology unless it's
   obvious from the image itself.
2. Copy the file into `gallery/<kebab-case-descriptive-name>.<ext>` (keep the
   original extension; don't transcode).
3. Add a tab-separated line to `raw/images/image-index.txt`:
   `../../gallery/<file>	<Title Case Name>`
4. If there's meaningful source/OCR/prompt context worth preserving, add
   `raw/images/<kebab-case-name>.txt` with those notes (optional — many
   existing entries have "No readable OCR text detected" or are simply
   omitted).
5. Add an entry to `markdown/gallery.md` following the existing pattern per
   image: `## Title`, the image embed (relative path `../gallery/...`), then
   `- File:`, `- Description:`, `- Notes:`, `- Comments:` bullets. Leave
   `Comments:` blank unless there's a specific essay tie-in worth noting.
6. If the image is a companion to a specific essay (thematically obvious),
   say so in the `Comments:` line of `markdown/gallery.md`, mirroring how
   `ceaseless-prayer.jpg` and `the-ungraspable-light.jpg` reference their
   companion essays. Don't force a tie-in that isn't there.
7. If the companion essay is newly ingested in the same batch, add the image
   near the top of that essay's public Markdown copy after the title/source
   block unless it is already present.

### Essay drafts (`.md`, and prose extracted from `.docx`/`.pdf`) → `markdown/` + `essays.qmd`

1. If a raw source exists alongside the draft (a `.pdf` export, a `.docx`,
   etc.), that source goes to `raw/` under its original/faithful filename
   (see PDF rule below) — don't rename or reformat it.
2. Write the public reading copy to `markdown/<kebab-case-title>.md`:
   - First line is a plain `# Title` heading (no YAML front matter — this
     project's `markdown/*.md` files don't use it).
   - If a raw source file was preserved, add a line right after the title:
     `` Source: `raw/<Original File Name>.pdf` ``
   - Otherwise preserve the essay content as given; do not add commentary,
     citations, or edits the author didn't write. Light cleanup (stray OCR
     artifacts, obviously broken markdown escaping) is fine; substantive
     editing is not.
3. Add a link to `essays.qmd` under the thematic category (`##` heading) that
   already fits the essay's subject best, alphabetization/order matching the
   surrounding list. If genuinely no existing category fits, propose a new
   `##` category to the user rather than forcing a mismatch.
4. Do not also create a root-level `.qmd` page or touch `_quarto.yml`'s navbar
   for an individual essay — root `.qmd` pages are reserved for structural site
   pages (Home, Method, Reader's Guide, etc.), not essay content. Essays live
   only in `markdown/` + the `essays.qmd` index.
5. Leave `archive.qmd` and `reading-paths.qmd` alone unless the user
   specifically asks for the new essay to be woven into a reading path —
   that's an editorial/curatorial judgment call, not a mechanical ingestion
   step.

### PDFs and other original source material → `raw/`

1. Copy as-is into `raw/`, preserving the original filename (raw/ favors
   faithfulness to the source over kebab-case naming — see existing files like
   `raw/The Ungraspable Light.pdf`).
2. If the PDF is the only copy of an essay (no `.md` draft alongside it) and
   the user wants it on the site, extract the text into a `markdown/` reading
   copy per the essay rule above, with a `Source:` line pointing back to the
   `raw/` PDF.
3. If the PDF is purely reference/source material not meant to become a public
   essay, leave it in `raw/` and don't force a `markdown/` copy or an
   `essays.qmd` entry.

### Anything else (unrecognized formats, ambiguous subject matter)

Don't guess. Leave the file in the staging folder, tell the user what it is
and why you're not sure where it goes, and ask.

## Guardrails specific to this project

- Never edit the content of an existing file under `markdown/` or a root
  `.qmd` page as a side effect of ingestion.
- Never invent new canonical theological terms/categories on your own
  authority — that's governed by
  `architecture-of-apostasy/grammar-of-apostasy/constitution.md`. If new
  material seems to need a new canonical concept, flag it for human review
  instead of encoding it yourself.
- Kebab-case is for public filenames in `gallery/` and `markdown/`; `raw/`
  keeps original filenames/casing.
- Always run `quarto render` and the theological consistency check before
  declaring ingestion complete, and before deleting the staging folder.
- Only delete the staging folder (or the portion of it that was successfully
  placed) after validation passes — never delete first. For this repo's
  permanent `intake/` folder, delete or move ingested contents but keep
  `intake/README.md`.
