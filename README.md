# The Architecture of Apostasy

A collective archive of theological discussion, images, songs, and essays, published as a Quarto site.

- Repository: <https://github.com/ashitaka-emishi/the-architecture-of-apostasy>
- Public site: <https://ashitaka-emishi.github.io/the-architecture-of-apostasy/>

## Development

This repository stores both source material and the public website source.

- `raw/` contains original source materials, PDFs, drafts, and OCR/text extraction.
- `markdown/` contains Markdown reading copies of the written documents.
- `gallery/` contains image files used by the archive.
- Root-level `.qmd` files define the public Quarto site.
- `.github/workflows/publish.yml` builds and deploys the site to GitHub Pages.

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

## Publishing

The default branch is `master`.

GitHub Pages is configured to deploy from GitHub Actions. On pushes to `master`, the workflow renders the Quarto site and publishes the generated `_site/` output.

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
