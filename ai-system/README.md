# AI System

This folder contains the machine-facing side of The Architecture of Apostasy.
It is intentionally separate from the theological workspace in
`../architecture-of-apostasy/`.

Use this folder for prompts, schemas, scripts, machine-readable maps, validation
templates, and other implementation artifacts that help agents work under the
Grammar of Apostasy.

The governing theological authority for this folder is:

`../architecture-of-apostasy/grammar-of-apostasy/constitution.md`

## Structure

- `prompts/` contains reusable prompt templates for the canonical AI agents.
- `schemas/` contains JSON schemas for agent output, chapter metadata, and the knowledge graph.
- `graphs/` contains machine-readable concept maps.
- `roadmap/` contains machine-readable volume and chapter planning.
- `checklists/` contains agent-facing tests and machine-readable templates.
- `examples/` contains schema-valid examples for agent outputs and similar contracts.
- `scripts/` contains validation and consistency tooling.

The GitHub Actions workflow that runs these tools must remain in
`../.github/workflows/` because GitHub requires that location.

## Design Principle

The AI System is an implementation layer, not the theological source of truth.
It exists to help agents and contributors preserve the Grammar of Apostasy while
drafting, mapping, validating, and expanding the project.

Human-facing theological claims belong in `../architecture-of-apostasy/`.
Machine-facing contracts belong here.

## Architecture

```text
ai-system/
├── README.md
├── prompts/      # Agent role prompts and workflows
├── schemas/      # JSON contracts for agent/chapter/graph data
├── graphs/       # Machine-readable concept dependency maps
├── roadmap/      # Machine-readable volume and chapter plans
├── checklists/   # Agent tests and templates
├── examples/     # Schema-valid example artifacts
└── scripts/      # Local and CI validation tools
```

The intended flow is:

```text
Constitution
  -> agent prompts
  -> structured agent output
  -> schemas/checklists
  -> critique and integration
  -> human editorial review
  -> public or canonical theological artifact
```

## Current Components

### Prompts

`prompts/` contains one reusable prompt per canonical agent:

- Biblical Agent
- Historical Theology Agent
- Philosophy Agent
- Psychology Agent
- Anthropology Agent
- Systems Mapping Agent
- Diagram Agent
- Image Review Agent
- Critique Agent
- Editorial Agent
- Canonical Integration Agent

Each prompt should include:

1. Purpose.
2. Role.
3. Inputs.
4. Workflow.
5. Output.
6. Validation.

### Schemas

`schemas/` defines machine-readable contracts:

- `agent-output.schema.json` defines the standard output shape for AI agents.
- `chapter.schema.json` defines metadata expected for structured chapter work.
- `gallery-image.schema.json` defines metadata for Visual Theology gallery images.
- `knowledge-graph.schema.json` defines nodes and edges for project maps.
- `status-metadata.schema.json` defines optional public Markdown status metadata.

Schemas should describe structure, not theology. The theology comes from the
constitution.

### Graphs

`graphs/concept-dependency-graph.yml` stores the seed dependency map for canonical
concepts such as God, Logos, Creation, Principalities, Disordered Logos, Fallen
Liturgy, Chemical Temple, Sacrifice, and Restoration.

### Roadmap

`roadmap/volumes.yml` stores the machine-readable volume roadmap. It mirrors the
human theological roadmap in the constitution and should be updated when volumes
or chapter plans change.

### Checklists

`checklists/` contains agent-facing validation and test material:

- `agent-prompt-test.md` documents a realistic prompt test.
- `chapter-front-matter-template.yml` gives a structured metadata template.
- `document-intake-checklist.md` routes new material through source,
  classification, placement, and review decisions.
- `pastoral-risk-review.md` reviews trauma, addiction, abuse, institutional,
  and psychological-formation material before publication or integration.

Human theological validation lives in:

`../architecture-of-apostasy/grammar-of-apostasy/checklists/theological-validation.md`

### Scripts

`scripts/theological_consistency_check.py` performs mechanical consistency checks.
It verifies required files, parses JSON schemas, checks agent prompt headings, and
looks for stale project-path references.

`scripts/validate_public_front_matter.py` checks newly added public Markdown and
Quarto files for front matter and validates optional status metadata fields when
they are present.

`scripts/intake_consistency_check.py` reports citation, canonical-resolution,
archive-listing, and raw-PDF source-note intake gaps.

Run it locally:

```bash
python3 ai-system/scripts/theological_consistency_check.py
python3 ai-system/scripts/validate_public_front_matter.py
python3 ai-system/scripts/intake_consistency_check.py
```

## How To Use

For a new chapter or concept:

1. Read the constitution in `../architecture-of-apostasy/grammar-of-apostasy/constitution.md`.
2. Choose the relevant aspect under `../architecture-of-apostasy/aspects/`.
3. Use the appropriate prompt from `prompts/`.
4. Capture structured output according to `schemas/agent-output.schema.json` when possible.
5. Validate chapter metadata against `schemas/chapter.schema.json` when structured metadata is added.
6. Run the theological consistency check.
7. Send the result through human editorial review before treating it as canonical.

For a new diagram:

1. Use `prompts/diagram-agent.md`.
2. Connect nodes and edges to the canonical terms.
3. Store machine-readable graph material in `graphs/` only when it is meant for agents.
4. Store public image assets in `../gallery/`.
5. Store theological interpretation in `../architecture-of-apostasy/aspects/visual-theology/`.

## Expansion Rules

Add new files here when they are machine-facing:

- New agent prompt: `prompts/[agent-name].md`
- New JSON schema: `schemas/[artifact-name].schema.json`
- New machine-readable graph: `graphs/[graph-name].yml`
- New machine-readable roadmap: `roadmap/[roadmap-name].yml`
- New validation script: `scripts/[script-name].py`
- New agent test/template: `checklists/[test-or-template-name].md`

Do not place theological essays, interpretive notes, public gallery commentary,
or chapter drafts in this folder. Put those in `../architecture-of-apostasy/` or
the public site layer as appropriate.

## Adding A New Agent

1. Define the agent's theological purpose in the constitution or agent contracts.
2. Add a prompt file in `prompts/`.
3. Include the required prompt headings.
4. Add the agent id to `schemas/agent-output.schema.json`.
5. Update `scripts/theological_consistency_check.py` so the prompt is required.
6. Add a prompt test in `checklists/`.
7. Run the consistency check.

## Adding A New Schema

1. Use JSON Schema draft 2020-12.
2. Give the schema a stable `$id`.
3. Keep required fields strict enough to be useful.
4. Avoid encoding contested theology into schema mechanics.
5. Add a sample or test when the schema becomes important to workflows.
6. Run the consistency check.

## Adding A New Validation Rule

Validation rules should catch mechanical drift, not replace judgment.

Good validation targets:

- missing required files,
- invalid JSON,
- stale paths,
- missing prompt headings,
- missing structured metadata,
- missing links to canonical terms.

Bad validation targets:

- pretending to decide theological truth,
- forcing one rhetorical style,
- suppressing marked speculation,
- rejecting work only because it is incomplete or exploratory.

## Continuous Integration

GitHub Actions runs:

`../.github/workflows/theological-consistency.yml`

That workflow calls:

```bash
python3 ai-system/scripts/theological_consistency_check.py
```

The workflow should fail only on mechanical consistency problems. Theological
judgment remains a human editorial responsibility.

## Roadmap

Near-term expansions:

1. Add a gallery/image schema.
2. Add an image-generation and image-review prompt.
3. Add sample agent-output JSON files.
4. Add metadata validation for chapter front matter.
5. Add a script that checks gallery assets against Visual Theology canon.
6. Add schema examples for the knowledge graph.
7. Add tests for every agent prompt.
