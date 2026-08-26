# Document Intake Checklist

Use this checklist when receiving or preparing a new essay, diagram, song, image, discussion, prompt, canonical chapter, source note, or raw archive item.

The goal is not to publish more material. The goal is to preserve source material faithfully, classify it honestly, and move it forward only when it serves the path of return into Christ.

## Intake Identity

- [ ] Name the document or artifact.
- [ ] Identify the artifact type:
  - [ ] Essay
  - [ ] Mythic or devotional work
  - [ ] Song
  - [ ] Image or image note
  - [ ] Discussion
  - [ ] Source note
  - [ ] Prompt
  - [ ] Canonical chapter
  - [ ] Raw archive item
  - [ ] Intake batch
- [ ] Identify the proposed archive category and status labels from the current archive and method conventions.
- [ ] Identify the intended repository location:
  - [ ] `intake/` staging only
  - [ ] `raw/`
  - [ ] `markdown/`
  - [ ] root `.qmd`
  - [ ] `architecture-of-apostasy/`
  - [ ] `gallery/`
  - [ ] `raw/images/`
  - [ ] `ai-system/`

## Theological Orientation

- [ ] What created good is being examined?
- [ ] What corruption, false logos, or fallen liturgy is being exposed?
- [ ] What cry is being heard?
- [ ] What wound does this document carry?
- [ ] Does the document clarify the path of return, or merely enlarge the archive?
- [ ] Does it resolve in Christ, or only diagnose collapse?
- [ ] Does it preserve the Anti-Nehushtan rule: tools, documents, symbols, AI, and institutions remain signs and servants?
- [ ] If the batch includes both an essay and an image, is there a clear companion-image relationship?

## Claim Classification

- [ ] Identify the claim types present:
  - [ ] Doctrine
  - [ ] Exegesis
  - [ ] Typology
  - [ ] Analogy
  - [ ] Historical judgment
  - [ ] Prophetic warning
  - [ ] Pastoral counsel
  - [ ] Speculative synthesis
- [ ] Distinguish what the document proves from what it proposes.
- [ ] Mark any strong claims that need visible citations.
- [ ] Mark any contested claims that need rival readings.
- [ ] Mark any psychological, medical, trauma-related, addiction-related, or abuse-related material that needs `ai-system/checklists/pastoral-risk-review.md`.

## Source And Evidence Review

- [ ] Preserve original source material in `raw/` when applicable.
- [ ] Confirm that public reading copies do not replace or overwrite source material.
- [ ] For files arriving through `intake/`, confirm accepted files are moved out of staging after validation.
- [ ] Identify evidence already present.
- [ ] Identify evidence still needed.
- [ ] Identify rival readings or tradition-specific objections.
- [ ] Identify whether the piece needs bibliography, footnotes, source notes, or a visible caveat.

## Repository Placement

- [ ] If it is raw source material, keep it in `raw/` or `raw/images/`.
- [ ] If it is a public reading copy, place it in `markdown/`.
- [ ] If it is public orientation, place it in a root `.qmd` page.
- [ ] If it develops canonical grammar, place it under `architecture-of-apostasy/`.
- [ ] If it is an AI/code support artifact, place it under `ai-system/`.
- [ ] If it is a public image asset, place it under `gallery/`.
- [ ] If a public essay has a clear companion image, place the image near the top of the Markdown copy after the title/source block unless already present.
- [ ] If an image is paired with an essay, add the relationship to `markdown/gallery.md` and include the image in `images.qmd`.
- [ ] If it is only a working note, do not present it as public or canonical.

## Mechanical Checks

- [ ] Check links and paths.
- [ ] Check front matter if the destination format uses it.
- [ ] Check filenames for kebab-case where public files are created.
- [ ] Check that public pages render with `quarto render`.
- [ ] Run `python3 ai-system/scripts/intake_consistency_check.py`.
- [ ] Run `python3 ai-system/scripts/theological_consistency_check.py` when touching canonical grammar, AI system files, or cross-system references.
- [ ] Confirm no unrelated essay body content was edited.
- [ ] Confirm `intake/README.md` remains and successfully ingested staging files were removed from `intake/`.

## Editorial Decision

- [ ] Publish now.
- [ ] Revise before publication.
- [ ] Convert or extract to another format.
- [ ] Route to canonical review.
- [ ] Hold in `raw/`.
- [ ] Decline public use.

## Reviewer Notes

- Intake reviewer:
- Date:
- Decision:
- Follow-up issues:
- Known limitations:
