# Public Site Rebalance Plan

Status: Proposed implementation plan

## Aim

Rebalance the public Quarto site so The Keeping Between appears as an equal companion to the Architecture of Apostasy without exposing raw, provisional, or source-controlled materials prematurely.

## Current Safety

The Quarto render list currently includes only root `.qmd` files and `markdown/*.md`. The imported Keeping Between workspace lives under `keeping-between/`, so it is not rendered by default.

## Proposed Navigation

Current public navigation can later move toward:

| Current | Proposed |
|---|---|
| Home | Home |
| The Path | Architecture |
| The Church | Keeping Between |
| Library | The Path |
| About | Library |
|  | About |

## First Public Page

Create a root-level `keeping-between.qmd` only after internal review. It should introduce The Keeping Between as the embodied companion to the Architecture of Apostasy, then link selectively to public reading copies.

## Promotion Pattern

Internal material remains in:

`keeping-between/`

Public reading copies, when approved, belong in:

`markdown/`

The site should link public copies rather than directly exposing internal registers, prompts, raw sources, or provisional institutional drafts.
