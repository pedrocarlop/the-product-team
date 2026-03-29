#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import discover_toml_paths, load_toml

ROOT = Path(__file__).resolve().parents[1]


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    orchestrator = load_toml(ROOT / "agents/orchestrator/orchestrator/orchestrator.toml")
    orchestrator_prompt = orchestrator["system_prompt"]
    orchestrator_catalog = (ROOT / "agents/orchestrator/orchestrator/skill-catalog.md").read_text()
    route_skill = (ROOT / "agents/orchestrator/orchestrator/skills/route.md").read_text()
    staff_skill = (ROOT / "agents/orchestrator/orchestrator/skills/staff.md").read_text()
    agents_fragment = (ROOT / "assets/AGENTS.fragment.md").read_text()
    package_readme = (ROOT / "assets/package-README.md").read_text()

    # Orchestrator prompt checks
    expect("direct execution by default" in orchestrator_prompt.lower(), "Orchestrator prompt missing direct-first rule.", failures)
    expect(
        "single-domain" in orchestrator_prompt
        and "implementation-first" in orchestrator_prompt
        and ("clearly scoped" in orchestrator_prompt or "easily inferable" in orchestrator_prompt),
        "Direct-routing criteria missing from orchestrator prompt.",
        failures,
    )
    expect("materially improve the outcome" in orchestrator_prompt, "Orchestrator prompt missing direct-execution best-team gate.", failures)
    expect(
        ("actual role needs" in orchestrator_prompt or "actual archetype needs" in orchestrator_prompt)
        and "keywords" in orchestrator_prompt,
        "Orchestrator prompt missing anti-keyword-routing guidance.",
        failures,
    )
    expect("full catalog only when the task is ambiguous" in orchestrator_prompt.lower(), "Orchestrator prompt missing lazy role-catalog rule.", failures)
    expect("coordination cost" in orchestrator_prompt.lower(), "Orchestrator prompt missing coordination-cost check.", failures)
    expect(
        "one role = one subagent" in orchestrator_prompt.lower()
        or "one archetype = one subagent" in orchestrator_prompt.lower(),
        "One-subagent-per-staffed-owner rule missing from orchestrator prompt.",
        failures,
    )
    expect("context.md" in orchestrator_prompt, "Orchestrator prompt missing context.md reference.", failures)
    expect("Do you want to proceed?" in orchestrator_prompt, "Orchestrator prompt missing explicit approval handoff question.", failures)
    expect("skill-catalog.md" in orchestrator_prompt, "Orchestrator prompt missing skill-catalog scan rule.", failures)
    expect("role catalog" in orchestrator_prompt.lower(), "Orchestrator prompt missing role-catalog guidance.", failures)

    # Skill catalog checks
    expect("Read this file first on every request before meaningful work." in orchestrator_catalog, "Orchestrator skill catalog missing every-request scan rule.", failures)

    # Route skill checks
    expect("Classify likely domain(s) first" in route_skill, "Route skill missing domain-first decision rule.", failures)
    expect("Check `logs/TIMELINE.md`" in route_skill or "Read `logs/TIMELINE.md`" in route_skill, "Route skill missing timeline check.", failures)

    # Staff skill checks
    expect("One role = one subagent" in staff_skill, "Staff skill missing one-role-one-subagent rule.", failures)
    expect("minimum viable" in staff_skill, "Staff skill missing minimum viable team rule.", failures)

    # AGENTS fragment checks
    expect("Route every request in this repository through `product-team-orchestrator` by default." in agents_fragment, "Managed AGENTS guidance missing all-requests-through-orchestrator rule.", failures)
    expect("Only bypass Product Team when the user explicitly says not to use Product Team" in agents_fragment, "Managed AGENTS guidance missing explicit opt-out rule.", failures)
    expect("Do not infer an opt-out from simplicity, urgency, or implementation bias alone." in agents_fragment, "Managed AGENTS guidance missing no-inferred-opt-out rule.", failures)
    expect("Route by domain before staffing" in agents_fragment, "Managed AGENTS guidance missing domain-first routing instruction.", failures)
    expect("Default to direct Codex execution" in agents_fragment, "Managed AGENTS guidance missing direct-first instruction.", failures)
    expect("skill-catalog.md" in agents_fragment, "Managed AGENTS guidance missing role-local skill catalog rule.", failures)

    # Package README checks
    expect("Every request in this repository should go through `product-team-orchestrator` by default." in package_readme, "Package README missing default-all-requests-through-orchestrator rule.", failures)
    expect("Only an explicit user opt-out" in package_readme, "Package README missing explicit opt-out rule.", failures)
    expect("direct path is chosen inside the orchestrator" in package_readme, "Package README missing direct-inside-orchestrator clarification.", failures)

    # Specialist checks
    specialist_files = discover_toml_paths(ROOT)
    for path in specialist_files:
      data = load_toml(path)
      role = data["name"]
      prompt = data["system_prompt"]
      if role in {"orchestrator", "reference"}:
          continue

      expect("Default behavior" in prompt, f"{role}: missing default behavior heading.", failures)
      expect("skill-catalog.md" in prompt, f"{role}: missing role-local skill catalog instruction.", failures)
      expect("assignment is clearly mismatched" in prompt, f"{role}: missing mismatch handling contract.", failures)
      expect("Escalate blockers" in prompt or "escalate to the orchestrator" in prompt, f"{role}: missing escalation rule.", failures)

      if data["execution_policy"]["role_kind"] == "reviewer":
          expect(f"logs/active/<project-slug>/reviews/{role}.md" in prompt, f"{role}: missing review path in prompt.", failures)
      else:
          expect(f"logs/active/<project-slug>/deliverables/{role}.md" in prompt, f"{role}: missing deliverable path in prompt.", failures)

    # Logs README checks
    logs_readme = (ROOT / "logs/README.md").read_text()
    expect("context.md" in logs_readme, "logs/README.md missing context.md reference.", failures)
    expect("TIMELINE.md" in logs_readme, "logs/README.md missing TIMELINE.md reference.", failures)

    role_catalog = ROOT / "references" / "role-catalog.md"
    expect(role_catalog.exists(), "references/role-catalog.md is missing.", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Prompt-level orchestrator scenario checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
