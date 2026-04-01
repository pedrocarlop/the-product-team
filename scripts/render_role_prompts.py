#!/usr/bin/env python3
"""Render managed specialist prompts from TOML metadata."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import EXCLUDED_ROLES, discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]
SYSTEM_PROMPT_RE = re.compile(r'(system_prompt\s*=\s*""")\n.*?(""")', re.DOTALL)


def repo_rule(role_name: str, repo_write_policy: str) -> str:
    if repo_write_policy == "explicit_owner_only":
        return (
            f"- You may edit repo-tracked files only when `assignment_mode = implementation`, "
            f'`repo_write_owner = "{role_name}"`, and `repo_write_scope` is explicit and bounded.'
        )
    if repo_write_policy == "never":
        return "- You never own repo-tracked implementation in staffed workflows; return a mismatch note instead."
    return "- In direct execution the orchestrator may edit repo-tracked files; staffed specialists must stay within assigned artifacts."


def render_prompt(data: dict) -> str:
    role_name = data["name"]
    display_name = data["display_name"]
    description = data["description"].strip().rstrip(".")
    role_kind = data["execution_policy"]["role_kind"]
    repo_write_policy = data["execution_policy"].get("repo_write_policy", "never")
    owns = ", ".join(data["role_boundary"]["owns"])
    skill_groups = data.get("capabilities", {}).get("skill_groups", {})
    output_type = "reviews" if role_kind == "reviewer" else "deliverables"
    output_path = f"logs/active/<project-slug>/{output_type}/{role_name}.md"
    configured_artifacts = data.get("outputs", {}).get("artifact_paths", [])
    extra_artifacts = [path for path in configured_artifacts if path != output_path]

    routing_lines = []
    if skill_groups:
        routing_lines.append("Skill routing:")
        for group_name, skills in skill_groups.items():
            routing_lines.append(f"- `{group_name}/`: {', '.join(skills)}")
    skill_routing = "\n".join(routing_lines)
    shared_artifact_line = ""
    if extra_artifacts:
        formatted = ", ".join(f"`{path}`" for path in extra_artifacts)
        shared_artifact_line = f"\n- When the assignment explicitly includes a shared workflow artifact you own, you may also update {formatted}."

    prompt = f"""
You are the {display_name} in the Product Team workflow.

Role charter:
- {description}.
- Primary ownership: {owns}.
- Work only from orchestrator-issued assignments for the active project at `logs/active/<project-slug>/`.
- Before meaningful work, read your own `skill-catalog.md` and then open the assigned `skill_paths` from `skills/`.
{skill_routing}
Default behavior:
- Treat every assignment as a strict contract with `assignment_mode`, `owned_outputs`, `reads_from`, `repo_write_owner`, `repo_write_scope`, `return_expected`, `skill_paths`, `primary_tools`, `fallback_policy`, and `evidence_mode`.
- If any required contract field is missing, stop and return a mismatch note naming the missing fields.
- Execute the assigned skill workflow, not a generic role summary.
- Use the required tool path automatically when the skill requires it.
- Enforce the fallback rule exactly: primary MCP -> alternative tool/MCP -> best guess inferred output.
- Label output evidence as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Escalate when setup, account access, destructive actions, or external publishing are needed.
- Keep your owned output current at `{output_path}`.
{repo_rule(role_name, repo_write_policy)}

Planning:
- Only write `logs/active/<project-slug>/plans/{role_name}.md` when the orchestrator explicitly requests advisory planning.
- Advisory plans must include objective, constraints, owned scope, skill paths consulted, tool path, fallback policy, risks, validation, and critical details that must survive merge.

Execution:
- If the assignment is blocked, mismatched, missing required tools, or overlaps another owner, return a mismatch note instead of improvising.
- Preserve concrete details from upstream artifacts; do not silently simplify them away.
- End each handoff with `Read <skill-paths> skills for this task.` listing the exact role-local skills opened.

Guardrails:
- Do not skip required `skill_paths`.
- Do not ask the orchestrator whether to use the skill's required MCP/tool path.
- Do not present inferred output as sourced evidence.
- Do not edit outside your owned artifact or assigned repo scope.
""".strip()
    if shared_artifact_line:
        prompt = prompt.replace(
            f"- Keep your owned output current at `{output_path}`.",
            f"- Keep your owned output current at `{output_path}`.{shared_artifact_line}",
        )
    return prompt


def update_toml_text(original: str, new_prompt: str) -> str:
    def replacer(match: re.Match[str]) -> str:
        return f'{match.group(1)}\n{new_prompt.rstrip()}\n{match.group(2)}'

    result, count = SYSTEM_PROMPT_RE.subn(replacer, original, count=1)
    if count == 0:
        raise ValueError("Could not find system_prompt block")
    return result


def discover_specialist_tomls(root: Path = ROOT) -> list[Path]:
    paths: list[Path] = []
    for toml_path in discover_toml_paths(root):
        data = load_toml(toml_path)
        if data["name"] not in EXCLUDED_ROLES and data["execution_policy"]["role_kind"] != "orchestrator":
            paths.append(toml_path)
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render managed specialist system prompts.")
    parser.add_argument("--write", action="store_true", help="Write prompts in place.")
    parser.add_argument("--check", action="store_true", help="Fail if prompts are stale.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    stale: list[str] = []
    updated = 0

    for path in discover_specialist_tomls(ROOT):
        original = path.read_text(encoding="utf-8")
        data = load_toml(path)
        rendered = update_toml_text(original, render_prompt(data))

        if original == rendered:
            continue

        if args.check:
            stale.append(data["name"])
            continue

        if args.write:
            path.write_text(rendered, encoding="utf-8")
            updated += 1
        else:
            print(f"--- {data['name']} (would update)")
            print(rendered)

    if args.check:
        if stale:
            print(
                f"FAIL: {len(stale)} role prompt(s) are stale: {', '.join(stale)}. "
                "Run `python3 scripts/render_role_prompts.py --write`.",
                file=sys.stderr,
            )
            return 1
        print("Managed specialist prompts are current.")
        return 0

    if args.write:
        print(f"Updated {updated} specialist prompt(s).")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
