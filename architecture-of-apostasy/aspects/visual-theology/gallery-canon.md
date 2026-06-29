# Gallery Canon

This canon governs how images fit within The Architecture of Apostasy.

## Placement

The gallery exists across four layers:

1. `gallery/`: public image assets used by the Quarto website.
2. `images.qmd`: public visual gallery page.
3. `markdown/gallery.md`: canonical public catalog of image descriptions and source notes.
4. `raw/images/`: source prompt text, OCR notes, and image metadata.
5. `architecture-of-apostasy/aspects/visual-theology/`: theological interpretation, classification, and validation.
6. `ai-system/`: image-related schemas, prompts, generation workflows, and validation tooling when those are added.

The image files should stay in `gallery/` unless the publication system changes.

## Theological Function

Images in this project may function as:

1. Symbolic theology: visual metaphor for apostasy, idolatry, restoration, sacrifice, or spiritual conflict.
2. Conceptual diagram: structured map of terms, flows, dependencies, or theological systems.
3. Devotional image: visual meditation ordered toward Christ, repentance, mercy, or hope.
4. Warning image: depiction of distortion, false worship, violence, hypocrisy, or idolatry.
5. Chapter illustration: visual anchor for a specific essay, volume, or reading path.
6. Research artifact: raw generated image, OCR text, prompt record, or draft asset not yet public-canonical.

## Canonical Classification Fields

Every major gallery item should eventually have:

1. Title.
2. Public filename.
3. Source note filename.
4. Image type.
5. Related aspect.
6. Canonical terms.
7. Short description.
8. Theological reading.
9. Christological resolution.
10. Risks or cautions.
11. Related essays or chapters.
12. Publication status.

## Image Type Vocabulary

Use these values consistently:

1. `symbolic-art`.
2. `conceptual-diagram`.
3. `devotional-image`.
4. `warning-image`.
5. `chapter-illustration`.
6. `research-artifact`.

## Validation Rules

An image is ready for public-canonical use when:

1. The image has a stable filename in `gallery/`.
2. The image has a description in `markdown/gallery.md`.
3. The image has a source note or prompt/OCR record in `raw/images/` unless the source is unavailable.
4. The image is connected to at least one canonical term or project aspect.
5. The image does not create a theological claim stronger than the surrounding text can support.
6. Warning images do not end in despair, spectacle, or contempt.
7. Crucifixion or Christological images are handled with reverence and doctrinal care.
8. Diagrams distinguish model from doctrine.

## Current Gallery Map

| Image | Type | Aspect | Canonical Terms |
|---|---|---|---|
| Starry Road to the Church | devotional-image | Restoration | Restoration, Church, pilgrimage |
| The Trinitarian Structural Model of Creation, Spirit, and Power | conceptual-diagram | Logos and Powers | Logos, Creation, Principalities, Restoration |
| Divine Ordering, Human Response, and Structural Forms | conceptual-diagram | Logos and Powers | Logos, Creation, Human Response, Structural Forms |
| Dark Mirror with Crown of Thorns | symbolic-art | Apostasy and Religious Systems | Scapegoat, false reflection, Christological exposure |
| Via Dolorosa, Christ Carrying the Cross | devotional-image | Restoration | Christological Resolution, Sacrifice, Restoration |
| Cracked Idol with Red Void | warning-image | Apostasy and Religious Systems | Idolatry, Nehushtan, Disease Logos |
| Burning Mask and Shadow Figure | warning-image | Chemical Temple | Hypocrisy, Chemical Temple, false self |
| Crucifixion Under Storm Clouds | devotional-image | Restoration | Sacrifice, Judgment, Mercy |
| Three Crosses at Calvary | devotional-image | Restoration | Cross, Sacrifice, Christological Resolution |
| Hammer and Knife with Blood | warning-image | Political Theology and War | Violence, Sacrifice, Fallen Liturgy |
| Blood-Drenched Crowned Cross | devotional-image | Restoration | Cross, Sacrifice, Restoration |
| Monumental Cross | chapter-illustration | Political Theology and War | Monumental Cross, Fallen Liturgy, Political Worship |
| Crucified Cross | devotional-image | Political Theology and War | Crucified Cross, Sacrifice, Christological Exposure |

## Required Public Catalog Note

The public gallery should remain descriptive and accessible. Deeper interpretive
claims belong here or in the related aspect/chapter unless the public page is
being intentionally expanded.

## Future Work

1. Add a machine-readable gallery schema in `ai-system/schemas/`.
2. Add `ai-system/roadmap/gallery.yml`.
3. Add image generation and review prompt templates.
4. Add links from each image to related essays and aspect notes.
5. Add a diagram style guide for conceptual diagrams.
