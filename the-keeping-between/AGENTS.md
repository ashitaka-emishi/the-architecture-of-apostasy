# AGENTS.md — The Keeping Between Workbench

This repository is a biblical-theological, mythopoetic, liturgical, and editorial research workspace. The user is the final theological and literary authority. Codex is an analytical, research, continuity, and drafting assistant — not an autonomous magisterium and not the owner of the canon.

## Source-of-truth hierarchy

1. `context/CURRENT_DECISIONS.md` — explicit current decisions and corrections.
2. `source/` — frozen source artifacts. Never modify them in place.
3. `registers/proposition-register.json` — cross-project propositions with status and confidence.
4. Active workstream documents.
5. Open proposals.

When sources conflict, expose the conflict. Never silently choose the version that best fits a draft.

## Canon-status vocabulary

Use only these statuses:

- `source` — directly present in a recovered source artifact.
- `user_established` — explicitly established by the user in the working conversation/project.
- `working_synthesis` — coherent synthesis requiring continued review.
- `proposed` — candidate idea, wording, structure, or interpretation.
- `research` — exegetical/historical/source note, not project doctrine.
- `deprecated` — explicitly superseded; retained for traceability.

A generated idea MUST NOT be promoted from `proposed` or `working_synthesis` to `user_established` without explicit human approval.

## Non-negotiable theological/editorial rules

- **Christ is the measure.** The Troth must not become a second Logos, deity, or autonomous moral principle alongside Christ.
- The Troth names enduring fidelity to the Good as revealed and judged in Christ; refine this formulation only with explicit theological argument.
- **Unclaimed Virtue is not relativism.** It denies human self-certification of possessed virtue; it does not deny objective Good or the ability to name evil.
- **The victim is not the measure and the aggressor is not the measure.** Suffering must be heard without making suffering moral sovereignty.
- **Authority is entrusted, not possessed.** Authority assigns responsibility to decide; it does not prove the decision righteous.
- Greater authority implies greater accountability.
- No fellowship, Host, Truvane, keeper, office, myth, liturgy, or institution may identify itself with the Troth.
- There is currently **no canonical capital-O “Order.”** Do not invent one. `Host`, `Truvane`, `Vaelun`, `Gravane`, `Hrovan`, and other source terms retain their specific meanings.
- “Keeper” is a task/office image, not a morally superior species of person.
- Redemption must remain open to the fallen without denying harm, responsibility, truth, restitution, or judgment.
- Do not erase the reality of violence. The active revision direction is to replace violence-as-resolution with strong peaceful resistance to physical and spiritual violence.
- Preserve the intensity of the Black Sun as exposure, accusation, deformation, and spiritual/psychological assault.
- The cry is a major diagnostic, but not an infallible oracle. Hearing must be joined to truth, discernment, mercy, and Christological judgment.
- “The Troth remains” must never mean “our institution remains” or “we remain righteous.”

## Biblical research discipline

Keep claim classes distinct:

1. textual/lexical;
2. historical-critical;
3. canonical-theological;
4. constructive theological;
5. mythopoetic;
6. liturgical/pastoral.

Do not let a constructive Troth category masquerade as the lexical meaning of a biblical word. Do not make biblical texts say “Troth” merely because the project finds a canonical resonance there.

For new research:
- record the biblical passage;
- distinguish quotation from paraphrase;
- record source/page information for scholarship;
- preserve rival readings;
- identify the inferential step that connects exegesis to constructive theology.

## Aru Va'en revision protocol

Never edit `source/aru-vaen/`.

For each proposed revision:
1. identify the exact source passage;
2. state the revision goal;
3. identify symbolic/theological/ecclesial/Christological consequences;
4. check effects on the liturgy, Unclaimed Virtue, the Book of Wolves, and the glossary;
5. record unresolved tensions;
6. draft only after the change map is accepted.

## Book of Wolves protocol

The current preferred form is **The Book of Wolves: Letters Concerning the Keeping of the Troth**, a mythopoetic collection of letters among wolves beneath the Shepherd. This is proposed literary architecture, not ancient pseudepigraphy and not a claim to canonical Scripture.

Andren, the wolf who bears the office of Vaerun within the correspondence workstream, must not become the measure. The letters should permit him to be corrected, to confess error, and to refuse hagiography. This Book-of-Wolves naming does not revise the accepted *Aru Va'en* narration, where the narrator's personal name remains unstated.

## Authority protocol

When writing leaders, elders, Hrovan, Vaerun, or presiders, distinguish:
- office;
- competence;
- witness;
- responsibility;
- righteousness.

Never infer righteousness merely from office. Never infer absence of legitimate authority merely from admitted fallibility.

## Change protocol

Project-wide changes require updating:
- `context/CURRENT_DECISIONS.md`;
- affected proposition(s) in `registers/proposition-register.json`;
- `context/OPEN_QUESTIONS.md` if unresolved;
- `registers/artifact-register.json` if artifact status changes.

## Validation

After structural edits run:

```bash
python3 scripts/check_project.py
python3 scripts/build_context.py
```

Do not claim validation passed unless it was run.
