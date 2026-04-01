#!/usr/bin/env python3
"""Render managed archetype system_prompt fields from TOML metadata and the shared baseline template."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import EXCLUDED_ROLES, discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]

UNIVERSAL_GUARDRAILS = {
    "Skip the mandatory fit-check protocol",
    "Silently accept a mismatched assignment or missing dependency",
    "Bypass the orchestrator for staffing, sequencing, or approval decisions",
    "Start substantial execution before the orchestrator approval gate when one is required",
    "Start substantial execution before the orchestrator signals execution when an approval gate is in place",
}

NEVER_LINE = (
    "Never: silently accept a mismatched assignment, bypass the orchestrator for "
    "staffing/sequencing/approval, take repo-write ownership without explicit "
    "assignment, rework another role's approved artifacts without orchestrator "
    "direction, or add planning ceremony the task does not need."
)

SYSTEM_PROMPT_RE = re.compile(
    r'(system_prompt\s*=\s*""")\n.*?(""")',
    re.DOTALL,
)


def render_skill_routing(skill_groups: dict[str, list[str]]) -> str:
    """Render skill routing section from skill_groups config."""
    if not skill_groups:
        return ""
    lines = [
        "",
        "Skill routing — select the right discipline group for each part of the task:",
    ]
    for group_name, skills in skill_groups.items():
        skills_str = ", ".join(skills)
        lines.append(f"- {group_name}/ → {skills_str}.")
    lines.append("")
    lines.append("You may chain multiple discipline groups in a single execution without handoff.")
    return "\n".join(lines)


def render_tool_proactivity(capabilities: dict) -> str:
    """Render tool proactivity section from recommended_external_mcp and recommended_external_skills."""
    rec_mcp = capabilities.get("recommended_external_mcp", [])
    rec_skills = capabilities.get("recommended_external_skills", [])
    if not rec_mcp and not rec_skills:
        return ""

    lines = [
        "",
        "Tool proactivity — always offer before acting:",
        "- At each stage of your work, check which tools from your capabilities would improve the outcome. Before using any tool or MCP server, propose the action to the orchestrator so it can ask the user. Format: \"Would you like me to [action] using [tool]? This would [benefit].\" Examples:",
        "  - \"Would you like me to send this wireframe to Paper.Design so you can review and iterate on the canvas?\"",
        "  - \"Would you like me to push this prototype to Google Stitch for interactive exploration?\"",
        "  - \"Would you like me to run a Lighthouse audit via Chrome DevTools to check accessibility scores?\"",
        "  - \"Would you like me to pull the latest analytics from Amplitude to inform this decision?\"",
        "- If a tool or MCP server from your capabilities is not yet configured, include setup requirements in your proposal: what the user needs to provide (API key, account, install command).",
        "- Do not silently skip tools that would materially improve output quality or speed — always surface the option.",
        "- Do not use tools without offering first. The user decides whether to proceed.",
    ]
    if rec_mcp:
        lines.append("")
        lines.append("Recommended external MCP servers (propose setup when relevant):")
        for mcp in rec_mcp:
            lines.append(f"- {mcp['display_name']} (`{mcp['name']}`) — {mcp['purpose']}. Setup: {mcp['setup']}.")
    if rec_skills:
        lines.append("")
        lines.append("Recommended session skills (propose activation when relevant):")
        for skill in rec_skills:
            lines.append(f"- `{skill['name']}` — {skill['purpose']}.")
    return "\n".join(lines)


def render_assignment_contract(role_name: str, output_path: str, repo_write_policy: str) -> str:
    lines = [
        "- Treat every orchestrator assignment as an explicit contract. Before acting, confirm it names `assignment_mode`, `owned_outputs`, `reads_from`, `repo_write_owner`, `repo_write_scope`, and `return_expected`.",
        "- If any assignment contract field is missing, stop and return a brief mismatch note naming the missing fields and the minimum fix needed.",
        f"- `assignment_mode = plan`: write only `logs/active/<project-slug>/plans/{role_name}.md`.",
        f"- `assignment_mode = deliverable`: write only the files listed in `owned_outputs` (normally `{output_path}`) and do not edit repo-tracked files.",
    ]
    if repo_write_policy == "explicit_owner_only":
        lines.extend(
            [
                f"- `assignment_mode = implementation`: you may edit repo-tracked files only when `repo_write_owner = \"{role_name}\"` and `repo_write_scope` is explicit, non-empty, and non-overlapping with any other active owner's scope for this stage.",
                "- If `repo_write_owner` differs, or `repo_write_scope` is missing, ambiguous, or overlapping, stop and return a mismatch note instead of coding.",
            ]
        )
    elif repo_write_policy == "direct_only":
        lines.append("- `assignment_mode = implementation`: direct-mode repo work stays with the orchestrator. If a staffed specialist is already the repo-write owner for this stage, do not implement in parallel from the main thread.")
    else:
        lines.append("- You never own repo-tracked implementation in staffed workflows. If `assignment_mode = implementation` or the assignment asks for production-code changes, stop and return a brief mismatch note back to the orchestrator.")
    return "\n".join(lines)


def render_execution_repo_rules(role_name: str, repo_write_policy: str) -> str:
    if repo_write_policy == "explicit_owner_only":
        return (
            f" If `assignment_mode` is not `implementation`, do not edit repo-tracked files. "
            f"When implementing, edit repo-tracked files only when `repo_write_owner` matches "
            f'`"{role_name}"` and only within `repo_write_scope`; if the scope needs to expand or '
            "overlaps another owner, stop and escalate with a mismatch note."
        )
    if repo_write_policy == "direct_only":
        return " In direct execution, you may edit repo-tracked files yourself. Once orchestration is active and a staffed implementation owner exists, become coordination-only for repo-tracked code until you explicitly reset routing back to direct execution."
    return " Do not edit repo-tracked files in staffed workflows; your execution output is limited to the `/logs` files listed in `owned_outputs`."


def render_prompt(data: dict) -> str:
    display_name = data["display_name"]
    description = data["description"].strip().rstrip(".")
    role_name = data["name"]
    owns = data["role_boundary"]["owns"]
    role_kind = data["execution_policy"]["role_kind"]
    repo_write_policy = data["execution_policy"].get("repo_write_policy", "never")
    must_not_do = data["role_boundary"].get("must_not_do", [])

    owns_str = ", ".join(owns)

    role_guardrails = [g for g in must_not_do if g not in UNIVERSAL_GUARDRAILS]
    guardrail_bullets = "\n".join(f"- {g}" for g in role_guardrails)

    if role_kind == "reviewer":
        output_type = "reviews"
        reviewer_extra = " Write review output only when the orchestrator requests a review pass."
    else:
        output_type = "deliverables"
        reviewer_extra = ""
    output_path = f"logs/active/<project-slug>/{output_type}/{role_name}.md"

    # Build skill routing section if skill_groups exist
    skill_groups = data.get("capabilities", {}).get("skill_groups", {})
    skill_routing = render_skill_routing(skill_groups)

    # Build tool proactivity section
    capabilities = data.get("capabilities", {})
    tool_proactivity = render_tool_proactivity(capabilities)

    prompt = f"""
You are the {display_name} in the direct-first orchestrator workflow.

Role charter:
- {description}.
- Primary ownership: {owns_str}.
- Work only from orchestrator-issued assignments for the active project at `logs/active/<project-slug>/`.
- Before meaningful work, quickly read the `skill-catalog.md` file in your own role folder. This is mandatory and is the fast scan for this role's local skills only.
{skill_routing}
Default behavior:
- Start by reading the assignment contract, then execute only the mode, outputs, and repo-write scope the orchestrator assigned.
- Use `skill-catalog.md` to identify matching role-local skills, then open only the matching `skills/*.md` files instead of reading the whole skill tree.
{render_assignment_contract(role_name, output_path, repo_write_policy)}
- If you previously authored an approved plan for this cycle, treat it as the detailed execution spec for your owned work unless the orchestrator explicitly changes it.
- If the assignment is clearly mismatched, blocked by missing inputs, or overlaps another role, stop and return a brief mismatch note with the reason and recommended adjustment.
- Only write `logs/active/<project-slug>/plans/{role_name}.md` when the orchestrator explicitly asks for advisory planning or sequencing input.
- If an approval gate is in place, wait for the orchestrator to signal execution before substantial work begins.
{tool_proactivity}
When advisory planning is requested: write `logs/active/<project-slug>/plans/{role_name}.md` as an execution-grade plan, not a summary. Cover objective, constraints, assumptions, owned scope, non-scope, detailed implementation approach, concrete decisions, step-by-step work breakdown, deliverables, dependencies, edge cases, failure and recovery behavior, validation or acceptance criteria, risks, and status. Include a `Role-local skills consulted` section naming the matching role-local skills you read and the best-practice implications that materially shape the plan. Include a final `Critical details that must survive merge` section with the exact specifics downstream work depends on, such as states, copy, thresholds, timings, token names, interaction rules, file touchpoints, test expectations, rollout constraints, or other non-negotiable implementation details. Plans are optional specialist input — the orchestrator decides how to merge and sequence them, but requested plans must be detailed enough that another strong practitioner in your domain could execute without guessing.

During execution: follow the current orchestrator direction, keep `logs/active/<project-slug>/{output_type}/{role_name}.md` current.{reviewer_extra}{render_execution_repo_rules(role_name, repo_write_policy)} If you authored an approved plan for this cycle, use it as the detailed spec for your work unless the orchestrator explicitly changes it. Do not silently drop planned concrete details for brevity; escalate needed changes first. Escalate blockers, conflicts, ambiguous ownership, and material scope changes to the orchestrator. In your closing handoff, append `Read <skill-paths> skills for this task.` with the role-local skills you opened from `skills/`; if none matched, append `Read no additional role-local skills for this task.`

Guardrails:
{guardrail_bullets}
- {NEVER_LINE}
"""
    return prompt


def update_toml_text(original: str, new_prompt: str) -> str:
    def replacer(match: re.Match[str]) -> str:
        return f'{match.group(1)}\n{new_prompt.rstrip()}\n{match.group(2)}'

    result, count = SYSTEM_PROMPT_RE.subn(replacer, original, count=1)
    if count == 0:
        raise ValueError("Could not find system_prompt = \"\"\"...\"\"\" block in TOML")
    return result


def discover_specialist_tomls(root: Path = ROOT) -> list[Path]:
    paths: list[Path] = []
    for toml_path in discover_toml_paths(root):
        data = load_toml(toml_path)
        if data["name"] not in EXCLUDED_ROLES:
            paths.append(toml_path)
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render managed archetype system_prompt fields from TOML metadata."
    )
    parser.add_argument(
        "--write", action="store_true",
        help="Update each TOML's system_prompt in place.",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Fail if any TOML's system_prompt does not match the rendered version.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    toml_paths = discover_specialist_tomls(ROOT)
    stale: list[str] = []
    updated = 0

    for path in toml_paths:
        original_text = path.read_text(encoding="utf-8")
        data = load_toml(path)
        rendered = render_prompt(data)
        new_text = update_toml_text(original_text, rendered)

        if original_text == new_text:
            continue

        if args.check:
            stale.append(data["name"])
            continue

        if args.write:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
        else:
            print(f"--- {data['name']} (would update)")
            print(rendered)

    if args.check:
        if stale:
            print(
                f"FAIL: {len(stale)} managed archetype role(s) have stale system_prompt: {', '.join(stale)}. "
                "Run `python3 scripts/render_role_prompts.py --write`.",
                file=sys.stderr,
            )
            return 1
        print(f"All {len(toml_paths)} managed archetype prompts are current.")
        return 0

    if args.write:
        print(f"Updated {updated} of {len(toml_paths)} managed archetype prompts.")
        return 0

    if not stale and updated == 0:
        print(f"All {len(toml_paths)} specialist prompts already match the template.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
