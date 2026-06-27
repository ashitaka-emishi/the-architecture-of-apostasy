# Contributing

This repository is both an archive and a Quarto website. Contributions should preserve that split: public reading material belongs in the Quarto/Markdown layer, while original sources and OCR output belong in `raw/`.

## Branch

The default branch is `master`.

## Local Workflow

1. Make edits in the appropriate location.
2. Run `quarto render`.
3. Check `git status -sb`.
4. Commit focused changes.
5. Push to `master` or open a pull request, depending on the collaboration pattern in use.

## Where Things Go

- Public Quarto pages: root-level `.qmd` files.
- Public reading copies: `markdown/`.
- Original PDFs, drafts, and extracted source text: `raw/`.
- Raw image OCR: `raw/images/`.
- Image files: `gallery/`.
- GitHub Pages workflow: `.github/workflows/publish.yml`.

## Style

- Use kebab-case for new public Markdown filenames.
- Keep `raw/` sources as faithful to the original files as possible.
- Put public explanation and navigation in Quarto pages rather than in raw source files.
- Run `quarto render` before publishing site changes.

## GitHub Pages

GitHub Pages is configured to deploy from GitHub Actions. The workflow renders the site and uploads `_site/` as the Pages artifact.

Official references:

- [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Actions documentation](https://docs.github.com/actions)
- [Quarto GitHub Pages publishing](https://quarto.org/docs/publishing/github-pages.html)
