# The Architecture of Apostasy

This repository is a collective archive of theological discussion, images, songs, and essays.

It also builds a public Quarto website for general readers. The site presents the material through browsable categories while preserving source files, PDFs, OCR, and drafts for editorial work.

The organization is intentionally simple:

- `raw/` contains the original source materials and raw OCR/text extraction.
- `markdown/` contains Markdown reading copies of the written documents.
- `gallery/` contains image files used by the archive.
- `markdown/gallery.md` is the Markdown image catalog.
- Quarto site pages live at the repository root as `.qmd` files.

## Website

Render the site locally with:

```bash
quarto render
```

Preview it locally with:

```bash
quarto preview
```

The generated site is written to `_site/`, which is ignored by Git.

GitHub Pages publishing is configured in `.github/workflows/publish.yml`. In GitHub repository settings, set Pages to deploy from **GitHub Actions**.

## Reading Copies

The main reading versions live in `markdown/`. Filenames use kebab-case.

## Source Materials

The source PDFs, original Markdown drafts, and OCR text live in `raw/`. Image OCR output is in `raw/images/`.

## Gallery

The image files live in `gallery/`. The image catalog with descriptions and notes is here:

- [Gallery catalog](markdown/gallery.md)

## Core Concepts

These concepts recur across the archive and form a shared vocabulary for the project.

- **Apostasy**: Not merely individual unbelief, but the repeated transformation of holy gifts, symbols, institutions, and rituals into systems of pride, control, performance, and idolatry.
- **Logos**: The divine ordering Word through whom creation coheres, the human person is rightly ordered, and all false patterns are judged and restored.
- **Disease Logos**: A framework for reading disease, addiction, hypocrisy, and embodied disorder as distortions of divine order made visible in the whole person.
- **The Chemical Temple**: The body as a living temple whose chemical, emotional, and spiritual patterns can either serve sober communion with God or reinforce counterfeit forms of comfort and worship.
- **Imago Dei**: The image of God in humanity, treated here as a central target of spiritual, cultural, institutional, and technological inversion.
- **Fallen liturgy**: A repeated pattern in which political, religious, cultural, or bodily practices become rival rituals of belonging, sacrifice, purification, and control.
- **Sacred time**: The relationship between biblical feasts, church tradition, Christmas, Sabbath, Christian liberty, and the movement from shadow to substance in Christ.
- **The broken quarantine**: The cosmological frame for how ancient rebellious powers, pre-diluvian archetypes, and modern systems are read as participating in the same long conflict.

## Reading Paths

Use these paths depending on what kind of entry point you want.

### Public Orientation

Start here for the broadest introduction to the project.

1. [Introduction Draft](markdown/introduction-draft.md)
2. [The Architecture of Apostasy](markdown/the-architecture-of-apostasy.md)
3. [Gallery catalog](markdown/gallery.md)

### Apostasy and Religious Systems

This path follows the critique of corrupted worship, institutional religion, and externalized holiness.

1. [The Architecture of Apostasy](markdown/the-architecture-of-apostasy.md)
2. [Ancient and Modern Monopolies of Faithless Religion](markdown/ancient-and-modern-monopolies-of-faithless-religion.md)
3. [Mormonism and Christianity](markdown/mormonism-and-christianity.md)
4. [The Weight of Glory: From Shadow to Substance](markdown/the-weight-of-glory-from-shadow-to-substance.md)

### Logos, Disease, and the Body

This path follows the archive's embodied theology of disorder, addiction, hypocrisy, care, and restoration.

1. [Disease Logos](markdown/disease-logos.md)
2. [Disease Logos and Care for the Long Afflicted](markdown/disease-logos-and-care-for-the-long-afflicted.md)
3. [From Hypocrisy to Disease Logos](markdown/from-hypocrisy-to-disease-logos.md)
4. [The Chemical Temple](markdown/the-chemical-temple.md)

### Sacred Time and Christian Liberty

This path focuses on Christmas, biblical feasts, Protestant critique, and the passage from calendar shadow to Christological substance.

1. [Pagan Origins of Christmas](markdown/pagan-origins-of-christmas.md)
2. [Protestantism and Christmas](markdown/protestantism-and-christmas.md)
3. [The True Timeline of Messiah](markdown/the-true-timeline-of-messiah.md)
4. [The Weight of Glory: From Shadow to Substance](markdown/the-weight-of-glory-from-shadow-to-substance.md)

### Cosmology and the Antediluvian Frame

This path follows the archive's most mythic and cosmological material.

1. [Introduction Draft](markdown/introduction-draft.md)
2. [Chapter 1: The Architecture of Pandemonium](markdown/chapter-1-the-architecture-of-pandemonium.md)
3. [Chapter 2: The Primordial Narrative](markdown/chapter-2-the-primordial-narrative.md)
4. [Chapter 3: The Broken Quarantine](markdown/chapter-3-the-broken-quarantine.md)

### Public Liturgy and Politics

This path reads national polarization through the language of fallen ritual, speech, desire, and political worship.

1. [The Fallen Liturgies of American Politics](markdown/the-fallen-liturgies-of-american-politics.md)

## Provisional Categories

This taxonomy is a first pass. Several documents overlap categories, especially the works on apostasy, Logos, embodied disorder, and liturgical corruption.

### Core Theological Cosmology and Antediluvian Framework

These appear to form a connected project on theological cosmology, non-human intelligences, spiritual mediation, the corruption of the Imago Dei, and the ancient-to-modern continuity of rebellion.

- [Introduction Draft](markdown/introduction-draft.md)
- [Chapter 1: The Architecture of Pandemonium](markdown/chapter-1-the-architecture-of-pandemonium.md)
- [Chapter 2: The Primordial Narrative](markdown/chapter-2-the-primordial-narrative.md)
- [Chapter 3: The Broken Quarantine](markdown/chapter-3-the-broken-quarantine.md)

### Apostasy, Religious Institutions, and Corrupted Worship

These works examine how holy signs, institutions, creeds, rituals, and religious systems can become mechanisms of performance, monopoly, or idolatry.

- [The Architecture of Apostasy](markdown/the-architecture-of-apostasy.md)
- [Ancient and Modern Monopolies of Faithless Religion](markdown/ancient-and-modern-monopolies-of-faithless-religion.md)
- [Mormonism and Christianity](markdown/mormonism-and-christianity.md)
- [The Weight of Glory: From Shadow to Substance](markdown/the-weight-of-glory-from-shadow-to-substance.md)

### Logos, Disease, Hypocrisy, and Embodied Restoration

These documents develop the relationship between the Logos, the human person, disease, hypocrisy, addiction, bodily disorder, sanctification, and Christian care.

- [Disease Logos](markdown/disease-logos.md)
- [Disease Logos and Care for the Long Afflicted](markdown/disease-logos-and-care-for-the-long-afflicted.md)
- [From Hypocrisy to Disease Logos](markdown/from-hypocrisy-to-disease-logos.md)
- [Hypocrisy Chapter Draft](markdown/hypocrisy-chapter-draft.md)
- [The Chemical Temple](markdown/the-chemical-temple.md)

### Calendar, Feasts, Christmas, and Sacred Time

These works focus on Christmas, midwinter syncretism, Protestant critique, biblical feasts, and the relationship between sacred calendar observance and Christian liberty.

- [Pagan Origins of Christmas](markdown/pagan-origins-of-christmas.md)
- [Protestantism and Christmas](markdown/protestantism-and-christmas.md)
- [The True Timeline of Messiah](markdown/the-true-timeline-of-messiah.md)
- [The Weight of Glory: From Shadow to Substance](markdown/the-weight-of-glory-from-shadow-to-substance.md)

### Political Theology and Public Liturgies

These works analyze politics as a spiritual ecosystem shaped by rival liturgies, distorted speech, tribal desire, and national disorder.

- [The Fallen Liturgies of American Politics](markdown/the-fallen-liturgies-of-american-politics.md)

### Literary and Mythopoetic Theology

These pieces use narrative, symbolic, or poetic form rather than direct essay structure.

- [Aru vaen: A Keeping of the Troth](markdown/aru-vaen-a-keeping-of-the-troth.md)

### Visual Theology and Diagrams

The gallery contains theological diagrams, symbolic illustrations, and OCR notes for image-based material.

- [Gallery catalog](markdown/gallery.md)
- [Raw image OCR index](raw/images/image-index.txt)

## Notes on Conversion

Markdown files converted from PDFs were extracted with local text extraction. They are useful reading/search copies, but the PDFs in `raw/` remain the source artifacts when formatting or page layout matters.

Some image OCR files are empty because the corresponding images are artwork rather than text-bearing documents.
