#!/usr/bin/env python3
"""Lightweight consistency checks for The Grammar of Apostasy.

This script intentionally checks mechanical consistency only. It does not replace
human theological judgment.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "architecture-of-apostasy"
GRAMMAR = PROJECT / "grammar-of-apostasy"
AI_SYSTEM = ROOT / "ai-system"

REQUIRED_FILES = [
    PROJECT / "README.md",
    PROJECT / "aspects" / "README.md",
    PROJECT / "aspects" / "visual-theology" / "README.md",
    PROJECT / "aspects" / "visual-theology" / "gallery-canon.md",
    GRAMMAR / "README.md",
    GRAMMAR / "constitution.md",
    GRAMMAR / "canonical-ontology.md",
    GRAMMAR / "editorial-style-guide.md",
    GRAMMAR / "agent-contracts.md",
    GRAMMAR / "checklists" / "theological-validation.md",
    AI_SYSTEM / "README.md",
    AI_SYSTEM / "schemas" / "agent-output.schema.json",
    AI_SYSTEM / "schemas" / "chapter.schema.json",
    AI_SYSTEM / "schemas" / "gallery-image.schema.json",
    AI_SYSTEM / "schemas" / "knowledge-graph.schema.json",
    AI_SYSTEM / "schemas" / "status-metadata.schema.json",
    AI_SYSTEM / "graphs" / "concept-dependency-graph.yml",
    AI_SYSTEM / "roadmap" / "volumes.yml",
    AI_SYSTEM / "checklists" / "chapter-front-matter-template.yml",
    AI_SYSTEM / "checklists" / "agent-prompt-test.md",
    AI_SYSTEM / "examples" / "agent-output" / "biblical-agent-sample.json",
    AI_SYSTEM / "examples" / "agent-output" / "image-review-agent-sample.json",
    AI_SYSTEM / "scripts" / "validate_public_front_matter.py",
    AI_SYSTEM / "scripts" / "intake_consistency_check.py",
]

CANONICAL_TERMS = [
    "Logos",
    "Disease Logos",
    "Fallen Liturgy",
    "Chemical Temple",
    "Principalities",
    "Restoration",
]

PROMPT_REQUIRED_HEADINGS = [
    "## Purpose",
    "## Role",
    "## Inputs",
    "## Workflow",
    "## Output",
    "## Validation",
]

EXPECTED_PROMPTS = [
    "biblical-agent.md",
    "historical-theology-agent.md",
    "philosophy-agent.md",
    "psychology-agent.md",
    "anthropology-agent.md",
    "systems-mapping-agent.md",
    "diagram-agent.md",
    "image-review-agent.md",
    "critique-agent.md",
    "editorial-agent.md",
    "canonical-integration-agent.md",
]

EXPECTED_PROMPT_TEST_SECTIONS = [
    "## Biblical Agent",
    "## Historical Theology Agent",
    "## Philosophy Agent",
    "## Psychology Agent",
    "## Anthropology Agent",
    "## Systems Mapping Agent",
    "## Diagram Agent",
    "## Image Review Agent",
    "## Critique Agent",
    "## Editorial Agent",
    "## Canonical Integration Agent",
]

AGENT_OUTPUT_REQUIRED_KEYS = [
    "agent",
    "task",
    "inputs",
    "summary",
    "findings",
    "claim_classifications",
    "citations",
    "risks",
    "open_questions",
    "recommended_next_action",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")


def check_json(errors: list[str]) -> None:
    for path in (AI_SYSTEM / "schemas").glob("*.json"):
        try:
            json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_constitution_terms(errors: list[str]) -> None:
    text = read_text(GRAMMAR / "constitution.md")
    for term in CANONICAL_TERMS:
        if term not in text:
            errors.append(f"Constitution missing canonical term: {term}")


def check_prompts(errors: list[str]) -> None:
    prompts_dir = AI_SYSTEM / "prompts"
    for filename in EXPECTED_PROMPTS:
        path = prompts_dir / filename
        if not path.exists():
            errors.append(f"Missing prompt template: {path.relative_to(ROOT)}")
            continue
        text = read_text(path)
        for heading in PROMPT_REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.relative_to(ROOT)} missing heading: {heading}")
        if "## AI Humility" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing heading: ## AI Humility")
        humility_markers = ["uncertainty", "rival readings", "missing sources", "pastoral risks"]
        for marker in humility_markers:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)} missing AI humility marker: {marker}")


def check_prompt_tests(errors: list[str]) -> None:
    text = read_text(AI_SYSTEM / "checklists" / "agent-prompt-test.md")
    for heading in EXPECTED_PROMPT_TEST_SECTIONS:
        if heading not in text:
            errors.append(f"agent-prompt-test.md missing section: {heading}")


def check_agent_output_examples(errors: list[str]) -> None:
    schema = json.loads(read_text(AI_SYSTEM / "schemas" / "agent-output.schema.json"))
    allowed_agents = set(schema["properties"]["agent"]["enum"])
    allowed_inputs = set(schema["properties"]["inputs"]["items"]["properties"]["kind"]["enum"])
    allowed_claim_types = set(
        schema["properties"]["claim_classifications"]["items"]["properties"]["classification"]["enum"]
    )
    allowed_confidence = set(schema["properties"]["findings"]["items"]["properties"]["confidence"]["enum"])

    for path in sorted((AI_SYSTEM / "examples" / "agent-output").glob("*.json")):
        try:
            data = json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid agent-output example JSON in {path.relative_to(ROOT)}: {exc}")
            continue
        extra = sorted(set(data) - set(AGENT_OUTPUT_REQUIRED_KEYS))
        missing = [key for key in AGENT_OUTPUT_REQUIRED_KEYS if key not in data]
        if extra:
            errors.append(f"{path.relative_to(ROOT)} has unexpected keys: {', '.join(extra)}")
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing keys: {', '.join(missing)}")
            continue
        if data["agent"] not in allowed_agents:
            errors.append(f"{path.relative_to(ROOT)} has invalid agent: {data['agent']}")
        for key in ["task", "summary", "recommended_next_action"]:
            if not isinstance(data[key], str) or not data[key].strip():
                errors.append(f"{path.relative_to(ROOT)} field '{key}' must be a non-empty string")
        array_keys = ["inputs", "findings", "claim_classifications", "citations", "risks", "open_questions"]
        for key in array_keys:
            if not isinstance(data[key], list):
                errors.append(f"{path.relative_to(ROOT)} field '{key}' must be an array")
        if any(not isinstance(data[key], list) for key in array_keys):
            continue
        for item in data["inputs"]:
            if item.get("kind") not in allowed_inputs or not item.get("reference"):
                errors.append(f"{path.relative_to(ROOT)} has invalid input entry")
        for item in data["findings"]:
            if not item.get("claim") or not item.get("support") or item.get("confidence") not in allowed_confidence:
                errors.append(f"{path.relative_to(ROOT)} has invalid finding entry")
        for item in data["claim_classifications"]:
            if not item.get("claim") or item.get("classification") not in allowed_claim_types:
                errors.append(f"{path.relative_to(ROOT)} has invalid claim classification entry")
        for item in data["citations"]:
            if not item.get("label") or not item.get("locator"):
                errors.append(f"{path.relative_to(ROOT)} has invalid citation entry")
        for key in ["risks", "open_questions"]:
            if not isinstance(data[key], list) or not all(isinstance(item, str) for item in data[key]):
                errors.append(f"{path.relative_to(ROOT)} field '{key}' must be a string array")


def check_stale_project_paths(errors: list[str]) -> None:
    allowed = {"_site", ".git"}
    stale_path = "project" + "/"
    stale_scaffold = "README" + "_PROJECT_SCAFFOLD"
    for path in ROOT.rglob("*"):
        if any(part in allowed for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".qmd", ".yml", ".yaml", ".json", ".py"}:
            continue
        text = read_text(path)
        if stale_path in text or stale_scaffold in text:
            errors.append(f"Stale project path reference in {path.relative_to(ROOT)}")


def check_restoration_marker(errors: list[str]) -> None:
    text = read_text(GRAMMAR / "constitution.md")
    markers = ["Christological resolution", "Restoration", "Christ exposes"]
    for marker in markers:
        if marker not in text:
            errors.append(f"Constitution missing restoration marker: {marker}")


def check_intake_consistency(errors: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, str(AI_SYSTEM / "scripts" / "intake_consistency_check.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip())
    if result.returncode != 0:
        errors.append("Intake consistency check failed")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    if not errors:
        check_json(errors)
        check_constitution_terms(errors)
        check_prompts(errors)
        check_prompt_tests(errors)
        check_agent_output_examples(errors)
        check_stale_project_paths(errors)
        check_restoration_marker(errors)
        check_intake_consistency(errors)

    if errors:
        print("Theological consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Theological consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
