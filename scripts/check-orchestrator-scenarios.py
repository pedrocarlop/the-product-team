#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REPO_WRITE_POLICIES = {
    "orchestrator": "direct_only",
    "frontend-engineer": "explicit_owner_only",
    "backend-engineer": "explicit_owner_only",
    "platform-engineer": "explicit_owner_only",
    "reference": "never",
}


def expected_repo_write_policy(role: str) -> str:
    return EXPECTED_REPO_WRITE_POLICIES.get(role, "never")


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    orchestrator = load_toml(ROOT / "agents/orchestrator/orchestrator/orchestrator.toml")
    orchestrator_prompt = orchestrator["system_prompt"]
    orchestrator_catalog = (ROOT / "agents/orchestrator/orchestrator/skill-catalog.md").read_text()
    agents_fragment = (ROOT / "assets/AGENTS.fragment.md").read_text()
    package_readme = (ROOT / "assets/package-README.md").read_text()
    logs_readme = (ROOT / "logs/README.md").read_text()

    expect("skill_paths" in orchestrator_prompt, "Orchestrator prompt missing skill_paths assignment contract.", failures)
    expect("primary_tools" in orchestrator_prompt, "Orchestrator prompt missing primary_tools assignment contract.", failures)
    expect("fallback_policy" in orchestrator_prompt, "Orchestrator prompt missing fallback_policy assignment contract.", failures)
    expect("evidence_mode" in orchestrator_prompt, "Orchestrator prompt missing evidence_mode assignment contract.", failures)
    expect("primary MCP -> alternative tool/MCP -> best guess inferred output" in orchestrator_prompt, "Orchestrator prompt missing fallback rule.", failures)
    expect("Do not leave `skill_paths` implicit." in orchestrator_prompt, "Orchestrator prompt missing explicit skill_paths guardrail.", failures)
    expect("design-reviewer" in orchestrator_prompt and "qa-reviewer" in orchestrator_prompt, "Orchestrator prompt missing new reviewer roles.", failures)
    expect("ui-designer" in orchestrator_prompt and "ux-researcher" in orchestrator_prompt, "Orchestrator prompt missing split design roles.", failures)
    expect("frontend-engineer" in orchestrator_prompt and "backend-engineer" in orchestrator_prompt, "Orchestrator prompt missing split engineering roles.", failures)
    expect("Read this file first on every request before meaningful work." in orchestrator_catalog, "Orchestrator skill catalog missing every-request scan rule.", failures)
    expect("Primary MCP/tool:" in orchestrator_catalog, "Orchestrator skill catalog missing MCP toolchain summary.", failures)

    expect("skill_paths" in agents_fragment, "Managed AGENTS fragment missing skill_paths rule.", failures)
    expect("primary MCP -> alternative tool/MCP -> best guess inferred output" in agents_fragment, "Managed AGENTS fragment missing fallback rule.", failures)
    expect("shadcn/ui" in agents_fragment, "Managed AGENTS fragment missing shadcn/ui foundation rule.", failures)
    expect("ui-designer" in package_readme and "ux-researcher" in package_readme, "Package README missing new role examples.", failures)
    expect("project-ds-spec.md" in package_readme, "Package README missing project ds-spec guidance.", failures)
    expect("reference-design-systems" in package_readme, "Package README missing reference design systems library guidance.", failures)
    expect("shadcn/ui" in package_readme, "Package README missing shadcn/ui foundation guidance.", failures)
    expect("evidence_mode" in logs_readme, "logs/README.md missing evidence_mode in deliverable header.", failures)
    expect("skill_paths" in logs_readme, "logs/README.md missing assignment contract update.", failures)
    expect("shared-design" in logs_readme, "logs/README.md missing shared deliverable guidance.", failures)

    for path in discover_toml_paths(ROOT):
        data = load_toml(path)
        role = data["name"]
        prompt = data["system_prompt"]
        raw_toml = path.read_text(encoding="utf-8")

        expect("model_reasoning_effort" in raw_toml, f"{role}: must use model_reasoning_effort.", failures)
        expect(re.search(r"^reasoning_effort\\s*=", raw_toml, re.MULTILINE) is None, f"{role}: uses legacy reasoning_effort key.", failures)
        expect(data["execution_policy"].get("repo_write_policy") == expected_repo_write_policy(role), f"{role}: unexpected repo_write_policy.", failures)

        if role in {"orchestrator", "reference"}:
            continue

        expect("skill-catalog.md" in prompt, f"{role}: missing skill catalog instruction.", failures)
        expect("skill_paths" in prompt, f"{role}: missing skill_paths instruction.", failures)
        expect("primary MCP -> alternative tool/MCP -> best guess inferred output" in prompt, f"{role}: missing fallback sequence.", failures)
        expect("evidence as `sourced`, `fallback`, or `inferred`" in prompt or "Label output evidence as `sourced`, `fallback`, or `inferred`" in prompt, f"{role}: missing evidence labeling rule.", failures)
        expect("Do not ask the orchestrator whether to use the skill's required MCP/tool path." in prompt, f"{role}: missing automatic tool use guardrail.", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Prompt-level orchestrator scenario checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
