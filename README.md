# The Architecture of Apostasy

A collective archive of theological discussion, images, songs, and essays, published as a Quarto site.

- Repository: <https://github.com/ashitaka-emishi/the-architecture-of-apostasy>
- Public site: <https://ashitaka-emishi.github.io/the-architecture-of-apostasy/>

## Repository Structure

This repository has three main layers:

1. Public publication layer.
2. Canonical theological workspace.
3. AI/code system.

The split matters: public reading material, theological canon, and agent machinery
should remain related but not mixed together casually.

```text
.
├── architecture-of-apostasy/   # Canonical theological workspace
├── ai-system/                  # AI prompts, schemas, scripts, and machine-readable files
├── gallery/                    # Public image assets used by the Quarto site
├── markdown/                   # Public Markdown reading copies
├── raw/                        # Original source files, PDFs, drafts, OCR, prompts, notes
├── *.qmd                       # Public Quarto site pages
├── _quarto.yml                 # Quarto website configuration
└── .github/workflows/          # GitHub Actions publishing and validation workflows
```

- `raw/` contains original source materials, PDFs, drafts, and OCR/text extraction.
- `markdown/` contains Markdown reading copies of the written documents.
- `gallery/` contains public image files used by the archive. The theological canon for image use lives in `architecture-of-apostasy/aspects/visual-theology/`.
- `architecture-of-apostasy/` contains the main theological project workspace, including the Grammar of Apostasy and sub-aspect scaffolds.
- `ai-system/` contains prompts, schemas, scripts, machine-readable maps, and other AI-facing implementation files.
- Root-level `.qmd` files define the public Quarto site.
- `.github/workflows/publish.yml` builds and deploys the site to GitHub Pages.

## Theological Workspace

The main theological project is `architecture-of-apostasy/`.

Important subfolders:

- `architecture-of-apostasy/grammar-of-apostasy/` contains the constitution, ontology, methodology, glossary, and editorial rules.
- `architecture-of-apostasy/aspects/` contains major sub-aspects such as Fallen Liturgies, The Chemical Temple, Sacred Time and Shadow, Restoration, and Visual Theology.

## AI System

The AI/code layer is `ai-system/`.

It contains:

- agent prompt templates,
- JSON schemas,
- machine-readable graph and roadmap files,
- validation checklists,
- consistency scripts.

See [AI System README](ai-system/README.md) for architecture, usage, and expansion rules.

## Development

This repository stores source material, the public website source, the theological
project workspace, and AI-facing support files.

## Local Commands

Render the site:

```bash
quarto render
```

Preview the site:

```bash
quarto preview
```

Check repository status:

```bash
git status -sb
```

Run the theological consistency check:

```bash
python3 ai-system/scripts/theological_consistency_check.py
```

## Publishing

The default branch is `master`.

GitHub Pages is configured to deploy from GitHub Actions. On pushes to `master`, the workflow renders the Quarto site and publishes the generated `_site/` output.

The theological consistency workflow also runs on pushes to `master` and on pull requests. It checks the Architecture workspace, Grammar of Apostasy constitution, AI system schemas/prompts, and stale path references.

The generated `_site/` directory is ignored locally and should not be committed.

## Contributor Docs

- [Contributing guide](CONTRIBUTING.md)
- [Quarto site config](_quarto.yml)
- [GitHub Pages workflow](.github/workflows/publish.yml)

## External Docs

- [GitHub Pages: configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Actions documentation](https://docs.github.com/actions)
- [Quarto: GitHub Pages](https://quarto.org/docs/publishing/github-pages.html)
- [Quarto: publishing basics](https://quarto.org/docs/publishing/)

## Notes

Public orientation material such as core concepts and reading paths lives on the Quarto site rather than in this README.
