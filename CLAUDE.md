# The Architecture of Apostasy — Claude Instructions

## SDLC Skill

When the user types `sdlc`, `sldc`, or `$sdlc-workflow` — with or without a following issue number or `next` — read and follow `.agents/skills/sdlc-workflow/SKILL.md` in full before taking any action. That file is the authoritative workflow definition, shared with Codex (Codex is the primary consumer; this file is Claude's pointer to the same skill, not a separate copy). Key points from it:

- `sdlc next` / `sldc next`: inspect open issues and milestone ordering, recommend the next issue, and **stop for user confirmation** before branching or editing anything.
- `sdlc <N>` / `sldc <N>`: run the state helper, determine the smallest correct continuation for that issue, and proceed accordingly.
- Always run the state helper first: `python3 .agents/skills/sdlc-workflow/scripts/sdlc_state.py inspect-issue <N> --repo ashitaka-emishi/the-architecture-of-apostasy --cwd .`
- Never touch essay content in `raw/` or `markdown/` as a side effect of SDLC work. Issues under milestone "M6: Essay-Level Revisions" additionally require explicit owner sign-off before implementation starts, even inside a multi-issue batch command.
- Use `Co-authored-by: Claude <noreply@anthropic.com>` (not the Codex trailer) when Claude materially performs the work.
- Open PRs as ready, not draft. Do not merge or close issues without explicit user instruction.
- Squash merge only.

## Format Ingestion Skill

When the user asks to ingest, process, or import a staging/drop folder (default `newfiles/` at the repo root — images, essay drafts, PDFs), read and follow `.agents/skills/format-ingestion/SKILL.md` in full before taking any action. That file is the authoritative workflow definition, shared with Codex (Codex is the primary consumer; this file is Claude's pointer to the same skill). Key points from it:

- View every image and read every document before deciding placement — never guess from a staging filename alone.
- Follow this repo's actual placement conventions (images → `gallery/` + `markdown/gallery.md` + `raw/images/`; essays → `markdown/` + `essays.qmd` with sources preserved in `raw/`; other PDFs/sources → `raw/`).
- Never edit the body of an existing essay or page as a side effect of ingestion.
- Run the Validation Pipeline below before declaring ingestion complete.
- Only delete the staging folder (or the successfully placed portion of it) after validation passes.
- Do not `git add`, commit, or push as part of ingestion unless the user explicitly asks.

## Repository

**GitHub:** `ashitaka-emishi/the-architecture-of-apostasy`
**Site:** GitHub Pages via Quarto
**Primary branch:** `master`

## Validation Pipeline

```bash
python3 ai-system/scripts/theological_consistency_check.py
quarto render
```

Run the consistency check whenever `ai-system/`, `architecture-of-apostasy/`, or their cross-references are touched. `quarto render` is the general site-build check for anything under root `.qmd`, `markdown/`, or `_quarto.yml`.

## Key Directories

Full placement rules live in `CONTRIBUTING.md` and `architecture-of-apostasy/grammar-of-apostasy/constitution.md` — read those before adding new content. Summary:

| Path | Contents |
|---|---|
| `markdown/` | Public reading copies of essays |
| `raw/` | Original sources (PDFs, drafts, OCR/source notes) |
| `gallery/` | Public image assets |
| `architecture-of-apostasy/` | Canonical theological workspace and Grammar of Apostasy constitution |
| `ai-system/` | AI-facing prompts, schemas, scripts, and validation tooling |
| `.agents/skills/sdlc-workflow/` | SDLC workflow skill (shared with Codex) |
| `.agents/skills/format-ingestion/` | Staging-folder ingestion skill (shared with Codex) |

## Branch Naming

- `fix/<issue-number>-<short-slug>`
- `feature/<issue-number>-<short-slug>`
- `docs/<issue-number>-<short-slug>`
- `chore/<issue-number>-<short-slug>`

## Active Milestones

- **M1: Foundations & Public Orientation** — issues #7–#12
- **M2: Archive Structure** — issues #13–#15
- **M3: Canonical Grammar Expansion** — issues #16–#21
- **M4: AI/Code Tooling** — issues #22–#25
- **M5: Sourcing & Rival Readings** — issues #26–#31
- **M6: Essay-Level Revisions** — issues #32–#35 (each requires explicit owner sign-off before implementation)
