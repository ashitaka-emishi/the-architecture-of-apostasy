# Contributing

This repository is both an archive and a Quarto website. Contributions should preserve that split: public reading material belongs in the Quarto/Markdown layer, while original sources and OCR output belong in `raw/`.

The canonical internal rules for new theological development live in `architecture-of-apostasy/grammar-of-apostasy/constitution.md`. Use that constitution when adding new terms, chapters, diagrams, agent prompts, or schemas.

## Branch

The default branch is `master`.

## Local Workflow

1. Make edits in the appropriate location.
2. Run `quarto render`.
3. Run `python3 ai-system/scripts/theological_consistency_check.py`.
4. Check `git status -sb`.
5. Commit focused changes.
6. Push to `master` or open a pull request, depending on the collaboration pattern in use.

## Where Things Go

- Public Quarto pages: root-level `.qmd` files.
- Public reading copies: `markdown/`.
- Original PDFs, drafts, and extracted source text: `raw/`.
- Public image files: `gallery/`.
- Image source notes, prompts, and OCR records: `raw/images/`.
- Visual theology and gallery canon: `architecture-of-apostasy/aspects/visual-theology/`.
- Main theological workspace and sub-aspect scaffolds: `architecture-of-apostasy/`.
- AI-facing prompts, schemas, machine-readable maps, and validation scripts: `ai-system/`.
- GitHub Pages workflow: `.github/workflows/publish.yml`.

## Style

- Use kebab-case for new public Markdown filenames.
- Keep `raw/` sources as faithful to the original files as possible.
- Put public explanation and navigation in Quarto pages rather than in raw source files.
- Use the Grammar of Apostasy constitution for new canonical terms, chapter structures, agent outputs, and diagrams.
- Keep theological docs in `architecture-of-apostasy/` and AI/code artifacts in `ai-system/`.
- Keep public gallery assets in `gallery/`; develop theological image interpretation in `architecture-of-apostasy/aspects/visual-theology/`.
- Distinguish biblical teaching, historical theology, and speculative synthesis.
- End canonical chapters with Christological resolution.
- Run `quarto render` before publishing site changes.

## GitHub Pages

GitHub Pages is configured to deploy from GitHub Actions. The workflow renders the site and uploads `_site/` as the Pages artifact.

Official references:

- [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Actions documentation](https://docs.github.com/actions)
- [Quarto GitHub Pages publishing](https://quarto.org/docs/publishing/github-pages.html)
