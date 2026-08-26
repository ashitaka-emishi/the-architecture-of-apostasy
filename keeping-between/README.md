# The Keeping Between Workbench

A VS Code/Codex project scaffold for tracking the user's vision of the myth that is **Aru Va'en**: understanding it, placing it in its proper place, and embodying it faithfully. The doctrine, liturgy, letters, Keeping Between materials, and biblical-theological research base are downstream of that center.

The central design rule is separation of layers. Source text, user-established decisions, constructive theology, biblical exegesis, mythopoetic development, liturgy, and open proposals are related but **not interchangeable**.

## What is here

- `source/` — frozen source artifacts recovered from the current project library. Do not silently rewrite them.
- `aru-vaen/` — accepted project myth, its revision and review record, symbolic architecture, and character model.
- `doctrine/` — working doctrinal syntheses, including Unclaimed Virtue and authority.
- `liturgy/` — the apostolic greeting and companion greetings, plus liturgical design notes.
- `book-of-wolves/` — architecture for the proposed Book of Wolves epistolary work.
- `biblical/` — research method, Scripture map, and exegetical dossiers.
- `sermons/` — derived homiletical work not already preserved in `source/sermons/`.
- `institutional/` — provisional Keeping Between drafts; no order is presumed to exist or to require formation.
- `registers/` — machine-readable proposition, artifact, glossary, and workstream registers.
- `prompts/` — bounded Codex prompts for each workstream.
- `context/` — the small set of files Codex should read before work begins.
- `context/ACCEPTED_ARTIFACTS.md` — human-readable index of accepted project texts and control records.
- `scripts/` — zero-dependency validation and context-bundle utilities.
- `assets/posters/` — currently available Troth poster set.

## Source-of-truth order

1. Explicit user decisions in `context/CURRENT_DECISIONS.md`.
2. Frozen user-authored/source artifacts under `source/`.
3. Approved proposition register entries.
4. Working syntheses under `doctrine/`, `aru-vaen/`, `liturgy/`, and `book-of-wolves/`.
5. Open proposals and research notes.

If two layers conflict, **report the conflict; do not silently harmonize it**.

## First session in VS Code / Codex

1. Open this folder.
2. Read `AGENTS.md`.
3. Read `context/START_HERE.md` and `context/CURRENT_DECISIONS.md`.
4. Run:

```bash
python3 scripts/check_project.py
python3 scripts/build_context.py
```

5. Open `build/CODEX_CONTEXT.md`.
6. Pick one workstream from `registers/workstreams.json`.

A good first Codex task is:

> Read AGENTS.md, context/START_HERE.md, context/CURRENT_DECISIONS.md, registers/proposition-register.json, and aru-vaen/REVISION_BRIEF.md. Work only on the Aru Va'en revision dossier. Identify contradictions between the frozen PDF, the V3 draft, and current revision decisions. Do not rewrite the myth yet. Produce a section-by-section change map with theological, symbolic, ecclesial, Christological, and narrative consequences.

## Important current state

The revised five-Keeping *Aru Va'en* is accepted under D-090 and kept at `aru-vaen/ARU_VAEN.md`. Its frozen sources remain unchanged evidence of earlier forms. Any future change to the accepted myth begins a new recorded review cycle.

## Git

```bash
git init
git add .
git commit -m "Initialize Troth BI workbench"
```

No license is asserted over the user-authored source material by this scaffold.
