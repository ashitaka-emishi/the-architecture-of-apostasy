# Codex Prompt — Append Guardian/Troth Module

Use this prompt from the root of the existing AoA/Troth scaffold after unpacking this append package outside the repository.

---

You are integrating an append-only theological development package into an existing Architecture of Apostasy / Aru Va'en / Book of Wolves workbench.

## Non-negotiable constraints

1. Read `AGENTS.md`, `context/START_HERE.md`, `context/CURRENT_DECISIONS.md`, and `CODEX_CONTEXT.md` first.
2. Never edit or overwrite `source/aru-vaen/` or any other frozen source artifact.
3. Preserve the project's layer distinctions: source artifacts, user decisions, constructive theology, exegesis, mythopoetics, liturgy, and open proposals are not interchangeable.
4. Source-of-truth order remains:
   - user decisions;
   - frozen `source/`;
   - proposition register;
   - working syntheses;
   - proposals/research.
5. If this package conflicts with an existing decision, report the conflict. Do not silently harmonize it.
6. Treat all files in this package as working additions unless the existing project explicitly promotes them.
7. Do not turn the Book of Wolves letters into doctrinal mini-essays. Preserve epistolary situations as the design rule.
8. Keep redemption open to the fallen.
9. Preserve the existing Aru Va'en revision direction: violence remains real, but resolution emphasizes non-cooperation, bearing, shielding, naming, truth-telling, peaceful resistance, and communion of keeping. Hold before hitting; when holding fails, wolves may throw immediate attackers back without drawing blood; never maim or kill; show the Shepherd's grief growing when restraint falters.

## Integration work

1. Copy workstream files into matching repository paths:
   - `doctrine/*.md` → `doctrine/`
   - `aru-vaen/*.md` → `aru-vaen/`
   - `book-of-wolves/*.md` → `book-of-wolves/`
2. Merge, do not replace:
   - `context/CURRENT_DECISIONS_APPEND.md` into `context/CURRENT_DECISIONS.md`
   - `context/OPEN_QUESTIONS_APPEND.md` into `context/OPEN_QUESTIONS.md`
3. Merge unique records from:
   - `registers/proposition-register.append.json`
   - `registers/artifact-register.append.json`
   into the existing project registers.
4. Preserve existing IDs. If an incoming ID already exists:
   - compare content;
   - update only if the current user decision is clearly newer;
   - otherwise report the collision for human review.
5. Update any project index or workstream manifest required by the existing scaffold.
6. Run:
   - `python scripts/check_project.py`
   - `python scripts/build_context.py`
7. Review the generated diff for accidental changes to `source/`.
8. Produce a short integration report containing:
   - files added;
   - decisions merged;
   - propositions added/changed;
   - ID collisions;
   - unresolved conflicts;
   - open questions added;
   - validation results.

## Current conceptual core of this package

- Vaelun = threshold/boundary guardianship.
- Vaerun = threshold guardianship that may require crossing.
- Hrovan = hall/center guardianship; closest to throne guardian.
- Aruvan = accumulated, diachronic body of keeping; not a fourth rank.
- Living Lamb = the kept-and-gathered face of the same creaturely communion whose keeping-face is Aruvan; life restored to agency and companionship beneath the Shepherd.
- Fang does not confer guilt; fleece does not confer virtue.
- The Troth precedes throne, pasture, fang, and fleece.
- The Shepherd is not a super-guardian or highest throne.
- Even the keeper must be kept; nothing faithful keeps alone.
- Unclaimed Virtue rejects moral self-sovereignty.
- Letters progress through Guardianship → Fang/Fleece → Aruvan/Living Lamb → Troth → Shepherd → Return → Vaerun relinquishment.
- Vaerun does not receive the final word; the community does.
