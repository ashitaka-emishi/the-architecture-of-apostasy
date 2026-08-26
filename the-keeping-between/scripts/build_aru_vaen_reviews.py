#!/usr/bin/env python3
"""Build and verify the Keeping reviews and final audit gate for Aru Va'en."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "aru-vaen" / "ARU_VAEN.md"
REVIEW_DIR = ROOT / "aru-vaen" / "reviews"
FINAL_AUDIT = REVIEW_DIR / "06_FINAL_CROSS_KEEPING_AUDIT.md"
TEXT_START = "<!-- BEGIN LOCKED CANDIDATE TEXT -->"
TEXT_END = "<!-- END LOCKED CANDIDATE TEXT -->"
USER_START = "## Your review"


PACKETS = [
    {
        "number": 1,
        "key": "N",
        "heading": "## The First Keeping: Night",
        "title": "Night",
        "file": "01_NIGHT_REVIEW.md",
        "review_status": "accepted 2026-08-10",
        "index_status": "Accepted 2026-08-10",
        "coverage": "Invocation and AV-01 through AV-04",
        "source": "Definitive PDF search text 1-140",
        "decisions": "D-024, D-025, D-027, D-029, D-037, D-067, D-070, D-073, and D-075",
        "purpose": [
            "Preserve the definitive invocation and establish the cry as interruption.",
            "Introduce Vaelun, Vaerun, and Hrovan as distinct accountable callings rather than ranks.",
            "Foreshadow Vaerun's measure-error through fear of being found wanting before the crossing office and the hall's trust.",
        ],
        "findings": [
            ("Source and continuity", "Pass. The PDF title, invocation, first-person voice, cry, offices, torn banners, and initial charge remain recognizable."),
            ("Literary register", "Pass provisionally. The cadence remains oral and elemental; repeated uses of old and fear have been sharply reduced."),
            ("Christological order", "Pass under the final close. The ache remains creaturely mythic apprehension rather than a force prior to the Shepherd."),
            ("Authority", "Pass. The Hrovan bears a real office whose stone seat does not certify the faithfulness of his answer."),
        ],
        "judgments": [
            "Does the invocation still carry enough age and mystery without becoming metaphysical explanation?",
            "Is Vaerun's fear of failing to become the measure clear, or is it stated too directly?",
            "Does the explanation of Vaelun, Vaerun, and Hrovan remain mythic, or does it read like a glossary inside the story?",
            "Do the final two sentences about the stone seat anticipate the Hrovan's Morning confession too explicitly?",
            "Does the First Keeping end with enough forward pressure into the crossing?",
        ],
    },
    {
        "number": 2,
        "key": "P",
        "heading": "## The Second Keeping: Pre-Dawn",
        "title": "Pre-Dawn",
        "file": "02_PRE_DAWN_REVIEW.md",
        "review_status": "accepted 2026-08-11",
        "index_status": "Accepted 2026-08-11",
        "coverage": "AV-05 through AV-07",
        "source": "Definitive PDF search text 141-390",
        "decisions": "D-016, D-024, D-032, D-037, D-062 through D-066, D-071 through D-073, D-077, and D-084",
        "purpose": [
            "Cross the veil without treating wolf, sheep, sickness, or shape as a fixed moral taxonomy.",
            "Make the Shepherd recognizably Christological through his wounded human body and the lamb in his scarred hands.",
            "Preserve the private bond and answering howl while reserving the three-part saying for departure.",
        ],
        "findings": [
            ("Source and continuity", "Pass. The borderlands, failed pasture, wounded lamb, hill, Shepherd, report, bond, and howl retain the PDF sequence."),
            ("Moral agency", "Pass. The prose distinguishes harm, suffering, fear, and possible cessation by action and condition rather than bodily class."),
            ("Christological recognition", "Pass. Scarred human hands and non-possessive grief make the Shepherd recognizable without superscription or hidden-identity staging."),
            ("Formula placement", "Pass. The older private repetition is removed; the report scene now carries uncertainty rather than a second ceremonial formula."),
        ],
        "judgments": [
            "Is the account of afflicted and attacking creatures concrete enough, or does it still explain the moral taxonomy too openly?",
            "Does the first sight of the Shepherd feel recognizably Christological without giving too much away?",
            "Is the sentence about grief having room for every creature earned at this early appearance?",
            "Does removing the private full formula weaken the intimacy between Hrovan and Vaerun, or strengthen the later departure?",
            "Does the answering howl retain the old liturgical force of the source?",
        ],
    },
    {
        "number": 3,
        "key": "C",
        "heading": "## The Third Keeping: The Calling of the Truvane",
        "title": "The Calling of the Truvane",
        "file": "03_CALLING_REVIEW.md",
        "review_status": "accepted 2026-08-10",
        "index_status": "Accepted 2026-08-10",
        "coverage": "AV-08 through AV-11",
        "source": "Definitive PDF search text 391-694",
        "decisions": "D-024, D-035 through D-038, D-049, D-065, D-071, D-072, and D-073",
        "purpose": [
            "Gather a listening community and introduce the four curses without turning them into fixed identities.",
            "Place the Hrovan's uncertainty and the Gravane's objection before the commission.",
            "Preserve differentiated calling portraits, allow refusal without failure, and end in the exact communal departure saying.",
        ],
        "findings": [
            ("Source and continuity", "Pass. The hollow, Gravane, old tongue, twelve named companions, character gestures, and Aru va'en responses remain."),
            ("Authority and objection", "Pass. The Hrovan remains responsible while admitting uncertainty, and the Gravane's objection changes the charge."),
            ("Refusal", "Pass. After Murn, a frightened candidate not ready for this crossing receives the same brow-to-brow gesture and the shared confession None of us is the measure without shame or coercion."),
            ("Liturgical speech", "Pass provisionally. New speech is concentrated in accepted formulas, but the total dialogue density requires human judgment."),
        ],
        "judgments": [
            "Do the sensory descriptions of the four curses feel like remembered warning or inserted explanation?",
            "Does the refusal scene read as genuine freedom without making refusal morally superior?",
            "Are Harrow, Murn, and Little Vey preserved strongly enough without overshadowing the other companions?",
            "Does the reduced treatment of the remaining eight companions retain enough individuality?",
            "Is the sequence from objection to calling to departure paced correctly?",
            "Does the exact three-part departure saying land with sufficient communal force?",
        ],
    },
    {
        "number": 4,
        "key": "E",
        "heading": "## The Fourth Keeping: Eternal Dawn",
        "title": "Eternal Dawn",
        "file": "04_ETERNAL_DAWN_REVIEW.md",
        "review_status": "accepted 2026-08-11",
        "index_status": "Accepted 2026-08-11",
        "coverage": "AV-12 through AV-20",
        "source": "Definitive PDF search text 695-1289",
        "decisions": "D-030, D-033, D-034, D-039 through D-055, D-062 through D-066, D-071, D-074, D-080 through D-082, D-087, and D-088",
        "purpose": [
            "Preserve the Black Sun's accusation and physical danger while replacing violence as the solution.",
            "Make the wolves' least-harm work at the circle mirror the Shepherd's prior work within it.",
            "Stage the lamb's healing, the first return, Harrow's death, Vey's limited wound, and Vaerun's false-cleanliness collapse as one ordeal.",
        ],
        "findings": [
            ("Violence and resistance", "Pass. The user confirmed the D-081 compression remains physically legible without becoming procedural; representative actions show costly restraint without drawing assailant blood or making force victorious."),
            ("Active Shepherd", "Pass. He calls continuously, heals the lamb, reorders fang, paw, and voice within the circle, then completes the fourfold action by opening the returning sheep's eye once."),
            ("Black Sun", "Pass. It weaponizes true fragments into a false final sentence rather than functioning as infallible revelation."),
            ("Return", "Pass. The user approved the E-06 compression: the sheep's settled movement remains intact while repeated labels, reactions, procedural choreography, and separate guardrails are reduced."),
            ("Companion continuity", "Pass. Harrow alone dies; Vey survives with one torn ear; Murn and the others remain embodied; wounds do not become credentials."),
        ],
        "judgments": [
            "Is the least-harm choreography physically legible without becoming procedural?",
            "Does the Shepherd remain the center throughout the long action, or do the wolves temporarily take over the myth?",
            "Do the four curse restorations preserve mystery while clearly separating deformation from wound or disability?",
            "Is Little Vey used with sufficient restraint, especially across noticing, seeking, wounding, and steadying Vaerun?",
            "Does Harrow's death remain grievous without becoming heroic payment?",
            "Does the first-return sequence feel earned and visible rather than diagrammed?",
            "Does Vaerun's wish for silence remain the interior climax of the Black Sun?",
            "Which negative or explanatory lines should be converted back into image, action, or silence?",
            "Is the Keeping too long, and if so, where does its pressure become repetition rather than liturgy?",
        ],
    },
    {
        "number": 5,
        "key": "M",
        "heading": "## The Fifth Keeping: Mourn",
        "title": "Mourn",
        "file": "05_MOURN_REVIEW.md",
        "review_status": "accepted 2026-08-11",
        "index_status": "Accepted 2026-08-11",
        "coverage": "AV-21 through AV-27, including AV-26A",
        "source": "Definitive PDF search text 1290-1668, with the user-established Morning meal added before the close",
        "decisions": "D-021, D-031, D-032, D-045 through D-069, D-071, D-073, D-074, D-085, and D-086",
        "purpose": [
            "Preserve fang-as-cradle and revise the Aruvan vision toward relinquishment without annihilation.",
            "Make Morning an ordinary wounded firstfruits of new creation rather than resurrection or reset.",
            "Display Vethra communally, enact the proper ordering in a shared meal, and close under the Shepherd's priority.",
        ],
        "findings": [
            ("Aruvan and Living Lamb", "Revision check passes. The single opening and the phrase `one communion under two forms` carry their relation without turning either into a second saving power."),
            ("Morning and continuity", "Pass. Harrow remains dead, all accepted wounds remain, the same hill and blood remain, and no ancestor becomes operative."),
            ("Vethra", "Revision check passes. Every companion bears it, Morning pauses only over Harrow and Ostra, and Vethra is neither scar, halo, payment, resurrection, nor institutional Sigil."),
            ("Hrovan and meal", "Pass. The exact confession receives silence; service rather than rank orders the open-ring meal beneath the Shepherd."),
            ("Final close", "Pass. Living Vey names the Shepherd's priority rather than unmasking him, and Vaerun completes the accepted three-line narration."),
        ],
        "judgments": [
            "Does the Aruvan vision remain mythic, or does it explain the relation to the Living Lamb too explicitly?",
            "Does relinquishment without annihilation remain clear without sounding like institutional theory?",
            "Is the transition from vision to ordinary wounded morning emotionally and temporally convincing?",
            "Does the Vethra passage preserve subtlety, costliness, and eschatological hope without becoming a doctrinal definition?",
            "Do the Harrow and Ostra Vethra glimpses carry enough of the whole company?",
            "Does the meal show the proper ordering naturally, or does it feel like every office is being checked off?",
            "Are Eucharistic and new-creation resonances present without creating a sacrament or completed eschaton?",
            "Does Harrow's absence remain perceptible through the meal without becoming an operative presence?",
            "Does the final exchange arrive with enough silence and simplicity?",
        ],
    },
]


def split_candidate(text: str) -> dict[str, str]:
    positions = []
    for packet in PACKETS:
        pos = text.find(packet["heading"])
        if pos < 0:
            raise ValueError(f"Missing candidate heading: {packet['heading']}")
        positions.append(pos)

    sections = {}
    for index, packet in enumerate(PACKETS):
        start = 0 if index == 0 else positions[index]
        end = positions[index + 1] if index + 1 < len(positions) else len(text)
        sections[packet["file"]] = text[start:end].strip() + "\n"
    return sections


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def findings_table(rows: list[tuple[str, str]]) -> str:
    lines = ["| Lens | Review finding |", "|---|---|"]
    lines.extend(f"| {lens} | {finding} |" for lens, finding in rows)
    return "\n".join(lines)


def judgment_list(items: list[str]) -> str:
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, 1))


def default_user_section(packet: dict) -> str:
    key = packet["key"]
    prompts = []
    for index, judgment in enumerate(packet["judgments"], 1):
        prompts.append(
            f"### {key}-{index:02d}: {judgment}\n\n"
            "**Comment:**\n\n"
            "**Requested wording or action:**\n"
        )
    return (
        f"{USER_START}\n\n"
        "### Disposition\n\n"
        "- [ ] Accept this Keeping as written.\n"
        "- [ ] Accept after specified revisions.\n"
        "- [ ] Return for substantial reworking.\n\n"
        "### Overall comment\n\n"
        "**Comment:**\n\n"
        "**Most important revision:**\n\n"
        + "\n".join(prompts)
    ).rstrip() + "\n"


def preserved_user_section(path: Path, packet: dict) -> str:
    if not path.exists():
        return default_user_section(packet)
    current = path.read_text(encoding="utf-8")
    marker = current.find(USER_START)
    if marker < 0:
        return default_user_section(packet)
    return current[marker:].rstrip() + "\n"


def render_packet(packet: dict, candidate_text: str, draft_hash: str, user_section: str) -> str:
    return f"""# Human Review {packet['number']}: {packet['title']}

**Canon status:** `working_synthesis`  
**Human review:** {packet.get('review_status', 'pending')}  
**Candidate source:** [`ARU_VAEN.md`](../ARU_VAEN.md)  
**Coverage:** {packet['coverage']}  
**Source baseline:** {packet['source']}  
**Controlling decisions:** {packet['decisions']}  
**Candidate SHA-256:** `{draft_hash}`

This packet contains an exact locked copy of the candidate passage. Add comments only under **Your review** so the packet can be checked against the active draft. Approval here records your literary and theological judgment of this Keeping; it does not silently alter the candidate or promote another Keeping.

## What This Keeping Must Do

{bullets(packet['purpose'])}

## Review Findings

{findings_table(packet['findings'])}

## Judgments Reserved for You

{judgment_list(packet['judgments'])}

## Text Under Review

{TEXT_START}
{candidate_text.rstrip()}
{TEXT_END}

{user_section.rstrip()}
"""


def render_index(draft_hash: str) -> str:
    rows = "\n".join(
        f"| {packet['number']} | [{packet['title']}]({packet['file']}) | {packet['coverage']} | {packet.get('index_status', 'Pending')} |"
        for packet in PACKETS
    )
    return f"""# Aru Va'en Human Review Packets

**Canon status:** `working_synthesis`  
**Candidate:** [`../ARU_VAEN.md`](../ARU_VAEN.md)  
**Project myth status:** `user_established` under D-090  
**Candidate SHA-256:** `{draft_hash}`

These five packets support final human review one Keeping at a time. Each packet contains:

- the complete candidate text for that Keeping;
- its source range and controlling decisions;
- focused literary, theological, and continuity findings;
- judgments that remain the user's alone; and
- a comment ledger that can be edited without changing the locked candidate text.

## Review Order

| # | Packet | Coverage | Human review |
|---|---|---|---|
{rows}

## Commenting Protocol

1. Read the locked text as a whole before answering individual prompts.
2. Check one disposition in **Your review**.
3. Put comments and requested wording beneath the relevant prompt.
4. Do not edit between the locked-text markers; revisions belong in the active candidate after discussion.
5. The five Keeping reviews, final cross-Keeping audit, and complete myth were accepted through D-090. Any future prose change requires a new reviewed revision cycle.

## Final Whole-Myth Gate

The complete five-Keeping project myth is accepted under D-090. The findings and final disposition are recorded in [`06_FINAL_CROSS_KEEPING_AUDIT.md`](06_FINAL_CROSS_KEEPING_AUDIT.md).
"""


def extract_locked_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    start = text.find(TEXT_START)
    end = text.find(TEXT_END)
    if start < 0 or end < 0 or end <= start:
        raise ValueError(f"Missing locked-text markers in {path.relative_to(ROOT)}")
    return text[start + len(TEXT_START):end].strip() + "\n"


def write_packets() -> None:
    candidate = DRAFT.read_text(encoding="utf-8")
    draft_hash = hashlib.sha256(DRAFT.read_bytes()).hexdigest()
    sections = split_candidate(candidate)
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)

    for packet in PACKETS:
        path = REVIEW_DIR / packet["file"]
        user_section = preserved_user_section(path, packet)
        path.write_text(
            render_packet(packet, sections[packet["file"]], draft_hash, user_section),
            encoding="utf-8",
        )

    (REVIEW_DIR / "README.md").write_text(render_index(draft_hash), encoding="utf-8")


def check_packets() -> list[str]:
    errors = []
    if not DRAFT.exists():
        return [f"Missing candidate: {DRAFT.relative_to(ROOT)}"]
    candidate = DRAFT.read_text(encoding="utf-8")
    sections = split_candidate(candidate)

    for packet in PACKETS:
        path = REVIEW_DIR / packet["file"]
        if not path.exists():
            errors.append(f"Missing review packet: {path.relative_to(ROOT)}")
            continue
        try:
            locked = extract_locked_text(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if locked != sections[packet["file"]]:
            errors.append(f"Locked candidate text is out of sync: {path.relative_to(ROOT)}")

    if not (REVIEW_DIR / "README.md").exists():
        errors.append("Missing review packet index: aru-vaen/reviews/README.md")
    if not FINAL_AUDIT.exists():
        errors.append("Missing final audit packet: aru-vaen/reviews/06_FINAL_CROSS_KEEPING_AUDIT.md")
    else:
        draft_hash = hashlib.sha256(DRAFT.read_bytes()).hexdigest()
        hash_line = f"**Candidate SHA-256:** `{draft_hash}`"
        if hash_line not in FINAL_AUDIT.read_text(encoding="utf-8"):
            errors.append("Final audit candidate hash is out of sync: aru-vaen/reviews/06_FINAL_CROSS_KEEPING_AUDIT.md")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Create or refresh review packets")
    parser.add_argument("--check", action="store_true", help="Verify locked text against the candidate")
    args = parser.parse_args()

    if not args.write and not args.check:
        parser.error("choose --write or --check")

    if args.write:
        write_packets()
    if args.check:
        errors = check_packets()
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("Aru Va'en review packets are synchronized.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
