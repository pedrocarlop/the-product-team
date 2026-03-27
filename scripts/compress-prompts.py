#!/usr/bin/env python3
"""Compress shared protocol blocks in specialist system_prompts.

Replaces the verbose fit-check, accept/decline, and shared guardrail blocks
with concise equivalents.  Role-specific content (charter, role-specific
guardrails) is preserved exactly.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"
EXCLUDED_DISCIPLINES = {"orchestrator"}
EXCLUDED_ROLE_NAMES = {"reference"}

# ---------------------------------------------------------------------------
# Regex anchors for each shared block
# ---------------------------------------------------------------------------

# Fit-check: from "Mandatory fit-check…" through step 7
FIT_CHECK_RE = re.compile(
    r"Mandatory fit-check protocol before any planning or execution:\n"
    r"1\. Restate the user request in your own words\.\n"
    r"2\. State whether you are the correct specialist for this request\.\n"
    r"3\. Explain why\.\n"
    r"4\. Define your scope boundary\.\n"
    r"5\. Identify dependencies on adjacent roles\.\n"
    r"6\. Define your expected output\.\n"
    r"7\. Choose exactly one: accept ownership, accept partial ownership, or decline and recommend another role\.",
)

FIT_CHECK_REPLACEMENT = (
    "Before planning or executing, complete the fit-check: "
    "(1) restate the request, "
    "(2) confirm you are the right specialist and why, "
    "(3) define scope boundary, "
    "(4) list dependencies on adjacent roles, "
    "(5) state expected output, "
    "(6) accept ownership, accept partial, or decline with a recommendation."
)

# Accept block — executor variant (deliverables)
ACCEPT_EXECUTOR_RE = re.compile(
    r"If you accept ownership or partial ownership:\n"
    r"- Write your role plan to `logs/active/<project-slug>/plans/([a-z0-9-]+)\.md`\.\n"
    r"- Structure the plan with: objective, assumptions, scope, steps, deliverables, dependencies, risks, and status\.\n"
    r"- Treat this plan as advisory input to the orchestrator\. Your job in the planning phase is to give your best advice on how the task should be tackled within your scope\.\n"
    r"- Do not start execution, rework another role's artifacts, or redefine the team process while writing your role plan\.\n"
    r"- Let the orchestrator decide staffing, sequencing, scope arbitration, and the final merged process in `03_unified-plan\.md`\.\n"
    r"- Do not begin substantial work until the orchestrator has reconciled plans and user approval exists when the work is meaningful or multi-step\.\n"
    r"- Once execution begins, follow the approved unified plan for the current cycle\.\n"
    r"- If the plan needs to change materially, escalate to the orchestrator so it can decide whether to finish the current cycle or reset into a new full planning pass\.\n"
    r"- Keep your deliverable summary current at `logs/active/<project-slug>/deliverables/\1\.md` when the orchestrator asks you to execute or review\.\n"
    r"- During approved execution, keep your deliverable summary current so future roles can continue from `/logs`\.\n"
    r"- Escalate blockers, conflicting inputs, ambiguous ownership, and review needs back to the orchestrator\.",
)

ACCEPT_EXECUTOR_TEMPLATE = (
    "On accept: write your plan to `logs/active/<project-slug>/plans/{role}.md` "
    "covering objective, assumptions, scope, steps, deliverables, dependencies, risks, status. "
    "Plans are advisory — the orchestrator reconciles them into `03_unified-plan.md`. "
    "Do not execute until the orchestrator approves. "
    "During execution, follow the unified plan and keep "
    "`logs/active/<project-slug>/deliverables/{role}.md` current. "
    "Escalate blockers, conflicts, and ambiguous ownership to the orchestrator."
)

# Accept block — reviewer variant (reviews)
ACCEPT_REVIEWER_RE = re.compile(
    r"If you accept ownership or partial ownership:\n"
    r"- Write your role plan to `logs/active/<project-slug>/plans/([a-z0-9-]+)\.md`\.\n"
    r"- Structure the plan with: objective, assumptions, scope, steps, deliverables, dependencies, risks, and status\.\n"
    r"- Treat this plan as advisory input to the orchestrator\. Your job in the planning phase is to give your best advice on how the task should be tackled within your scope\.\n"
    r"- Do not start execution, rework another role's artifacts, or redefine the team process while writing your role plan\.\n"
    r"- Let the orchestrator decide staffing, sequencing, scope arbitration, and the final merged process in `03_unified-plan\.md`\.\n"
    r"- Do not begin substantial work until the orchestrator has reconciled plans and user approval exists when the work is meaningful or multi-step\.\n"
    r"- Once execution begins, follow the approved unified plan for the current cycle\.\n"
    r"- If the plan needs to change materially, escalate to the orchestrator so it can decide whether to finish the current cycle or reset into a new full planning pass\.\n"
    r"- Keep your review output current at `logs/active/<project-slug>/reviews/\1\.md` when the orchestrator asks you to execute or review\.\n"
    r"- Write your review output only when the orchestrator explicitly requests a review pass\.\n"
    r"- Escalate blockers, conflicting inputs, ambiguous ownership, and review needs back to the orchestrator\.",
)

ACCEPT_REVIEWER_TEMPLATE = (
    "On accept: write your plan to `logs/active/<project-slug>/plans/{role}.md` "
    "covering objective, assumptions, scope, steps, deliverables, dependencies, risks, status. "
    "Plans are advisory — the orchestrator reconciles them into `03_unified-plan.md`. "
    "Do not execute until the orchestrator approves. "
    "During execution, follow the unified plan and keep "
    "`logs/active/<project-slug>/reviews/{role}.md` current. "
    "Write review output only when the orchestrator requests a review pass. "
    "Escalate blockers, conflicts, and ambiguous ownership to the orchestrator."
)

# Decline block
DECLINE_RE = re.compile(
    r"If you decline:\n"
    r"- Do not produce a role plan\.\n"
    r"- Return a concise rationale and the recommended replacement role so the orchestrator can record it in `02_staffing\.md`\.",
)

DECLINE_REPLACEMENT = (
    "On decline: return a concise rationale and the recommended replacement role "
    "for `02_staffing.md`. Do not produce a plan."
)

# Shared guardrails (4 lines)
SHARED_GUARDRAILS = [
    "- Skip the mandatory fit-check protocol\n",
    "- Bypass the orchestrator for staffing, sequencing, or approval decisions\n",
    "- Rework another role's approved artifacts or reopen planning without orchestrator direction\n",
    "- Start substantial execution before the orchestrator approval gate when one is required\n",
]

SHARED_GUARDRAILS_REPLACEMENT = (
    "- Never: skip fit-check, bypass the orchestrator for staffing/sequencing/approval, "
    "rework another role's approved artifacts without orchestrator direction, "
    "or start substantial execution before approval.\n"
)


def discover_specialist_tomls() -> list[Path]:
    """Find all specialist TOML files (excluding orchestrator and reference)."""
    tomls: list[Path] = []
    for toml_path in sorted(AGENTS_DIR.glob("*/*/*.toml")):
        discipline = toml_path.parent.parent.name
        if discipline in EXCLUDED_DISCIPLINES:
            continue
        if toml_path.stem in EXCLUDED_ROLE_NAMES:
            continue
        tomls.append(toml_path)
    return tomls


def compress_prompt(text: str) -> str:
    """Apply all compression transformations to a system_prompt string."""
    original = text

    # 1. Fit-check
    text = FIT_CHECK_RE.sub(FIT_CHECK_REPLACEMENT, text)

    # 2. Accept block (try reviewer first — it's the more specific pattern)
    match = ACCEPT_REVIEWER_RE.search(text)
    if match:
        role_name = match.group(1)
        replacement = ACCEPT_REVIEWER_TEMPLATE.format(role=role_name)
        text = ACCEPT_REVIEWER_RE.sub(replacement, text)
    else:
        match = ACCEPT_EXECUTOR_RE.search(text)
        if match:
            role_name = match.group(1)
            replacement = ACCEPT_EXECUTOR_TEMPLATE.format(role=role_name)
            text = ACCEPT_EXECUTOR_RE.sub(replacement, text)

    # 3. Decline block
    text = DECLINE_RE.sub(DECLINE_REPLACEMENT, text)

    # 4. Shared guardrails — replace the 4 individual lines with one merged line
    for guardrail in SHARED_GUARDRAILS:
        text = text.replace(guardrail, "")

    # Insert the merged guardrail line before the closing """
    # Find the Guardrails section and append
    if "Guardrails:\n" in text and SHARED_GUARDRAILS_REPLACEMENT not in text:
        # Find remaining guardrails after "Guardrails:\n"
        guardrails_idx = text.index("Guardrails:\n")
        after_header = text[guardrails_idx + len("Guardrails:\n"):]

        # If there are remaining role-specific guardrails, append shared line after them
        # Otherwise just add it after the header
        remaining_lines = []
        rest = ""
        for i, line in enumerate(after_header.split("\n")):
            if line.startswith("- "):
                remaining_lines.append(line + "\n")
            else:
                rest = "\n".join(after_header.split("\n")[i:])
                break

        new_guardrails = "Guardrails:\n" + "".join(remaining_lines) + SHARED_GUARDRAILS_REPLACEMENT + rest
        text = text[:guardrails_idx] + new_guardrails

    if text == original:
        return text  # Nothing changed

    # Clean up double blank lines
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    return text


def main() -> int:
    tomls = discover_specialist_tomls()
    if not tomls:
        print("No specialist TOML files found.", file=sys.stderr)
        return 1

    changed = 0
    unchanged = 0
    errors: list[str] = []

    for toml_path in tomls:
        content = toml_path.read_text(encoding="utf-8")

        # Extract system_prompt value
        prompt_start = content.find('system_prompt = """')
        if prompt_start == -1:
            errors.append(f"No system_prompt found: {toml_path.relative_to(ROOT)}")
            continue

        prompt_body_start = prompt_start + len('system_prompt = """')
        prompt_end = content.find('"""', prompt_body_start)
        if prompt_end == -1:
            errors.append(f"Unterminated system_prompt: {toml_path.relative_to(ROOT)}")
            continue

        original_prompt = content[prompt_body_start:prompt_end]
        compressed = compress_prompt(original_prompt)

        if compressed == original_prompt:
            unchanged += 1
            continue

        new_content = content[:prompt_body_start] + compressed + content[prompt_end:]
        toml_path.write_text(new_content, encoding="utf-8")
        changed += 1

        # Word count comparison
        orig_words = len(original_prompt.split())
        new_words = len(compressed.split())
        rel = toml_path.relative_to(ROOT)
        print(f"  {rel}: {orig_words} → {new_words} words ({orig_words - new_words} saved)")

    print(f"\nCompressed {changed} files, {unchanged} unchanged.")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for err in errors:
            print(f"  {err}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
