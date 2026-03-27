#!/usr/bin/env python3
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text())


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    orchestrator = load_toml(ROOT / "agents/orchestrator/orchestrator/orchestrator.toml")
    orchestrator_prompt = orchestrator["system_prompt"]
    route_skill = (ROOT / "agents/orchestrator/orchestrator/skills/route.md").read_text()
    staff_skill = (ROOT / "agents/orchestrator/orchestrator/skills/staff.md").read_text()
    agents_fragment = (ROOT / "assets/AGENTS.fragment.md").read_text()

    expect("simple, operational, low-risk, self-contained" in orchestrator_prompt, "Direct-routing criteria missing from orchestrator prompt.", failures)
    expect("best possible role set" in orchestrator_prompt, "Orchestrator prompt missing best-team assessment requirement.", failures)
    expect("specialist staffing would not materially improve the outcome" in orchestrator_prompt, "Orchestrator prompt missing direct-execution best-team gate.", failures)
    expect("underlying role needs" in orchestrator_prompt and "not keywords" in orchestrator_prompt, "Orchestrator prompt missing anti-keyword-routing guidance.", failures)
    expect("one role = one subagent" in orchestrator_prompt.lower(), "One-role-per-subagent rule missing from orchestrator prompt.", failures)
    expect("02_staffing.md" in orchestrator_prompt and "03_unified-plan.md" in orchestrator_prompt and "04_approval.md" in orchestrator_prompt, "Unified planning and approval files missing from orchestrator prompt.", failures)
    expect("status.md" in orchestrator_prompt and "context.md" in orchestrator_prompt, "Continuity files missing from orchestrator prompt.", failures)
    expect("substantial orchestrated execution before explicit" in orchestrator_prompt or "substantial orchestrated execution until approval is explicit" in orchestrator_prompt, "Approval gate missing from orchestrator prompt.", failures)
    expect("decline" in orchestrator_prompt and "recommendation" in orchestrator_prompt, "Misfit staffing path missing from orchestrator prompt.", failures)
    expect("reconcile" in orchestrator_prompt.lower() and "03_unified-plan.md" in orchestrator_prompt, "Orchestrator prompt missing authoritative merge behavior.", failures)
    expect("no piecemeal replanning" in orchestrator_prompt or "no repeated plan churn" in orchestrator_prompt, "Orchestrator prompt missing anti-churn guardrail.", failures)
    expect("read the canonical role catalog" in orchestrator_prompt.lower() or "role catalog" in orchestrator_prompt.lower(), "Orchestrator prompt missing role-catalog-first staffing rule.", failures)
    expect("Always identify the minimum viable best team" in route_skill, "Route skill missing best-team-first decision rule.", failures)
    expect("actual role needs rather than keywords alone" in route_skill, "Route skill missing anti-keyword-routing guidance.", failures)
    expect("Read the full canonical role catalog" in route_skill, "Route skill missing role-catalog read requirement.", failures)
    expect("Start from the best-team assessment recorded during routing" in staff_skill, "Staff skill missing routing-to-staffing continuity.", failures)
    expect("staffed specialists act as advisors first" in staff_skill, "Staff skill missing advisory-first specialist behavior.", failures)
    expect("read `.codex/product-team/references/role-catalog.md` end to end" in agents_fragment, "Managed AGENTS guidance missing role catalog instruction.", failures)
    expect("reason about the best possible team for the job" in agents_fragment, "Managed AGENTS guidance missing best-team-first instruction.", failures)
    expect("actual role needs, not task keywords alone" in agents_fragment, "Managed AGENTS guidance missing anti-keyword staffing rule.", failures)
    expect("Treat role plans as advisory input" in agents_fragment, "Managed AGENTS guidance missing advisory-plan rule.", failures)

    specialist_files = sorted((ROOT / "agents").glob("*/*/*.toml"))
    for path in specialist_files:
      data = load_toml(path)
      role = data["name"]
      prompt = data["system_prompt"]
      if role in {"orchestrator", "reference"}:
          continue

      expect("fit-check" in prompt.lower(), f"{role}: missing fit-check heading.", failures)
      expect("accept ownership" in prompt or "accept partial" in prompt, f"{role}: missing ownership decision contract.", failures)
      expect("Do not execute until the orchestrator approves" in prompt or "Do not begin substantial work until the orchestrator" in prompt, f"{role}: missing approval gating language.", failures)
      expect(f"logs/active/<project-slug>/plans/{role}.md" in prompt, f"{role}: missing plan path in prompt.", failures)
      expect("advisory" in prompt.lower(), f"{role}: missing advisory-plan rule.", failures)
      expect("Escalate blockers" in prompt or "escalate to the orchestrator" in prompt, f"{role}: missing escalation-before-replan rule.", failures)

      if data["execution_policy"]["role_kind"] == "reviewer":
          expect(f"logs/active/<project-slug>/reviews/{role}.md" in prompt, f"{role}: missing review path in prompt.", failures)
          expect("review pass" in prompt, f"{role}: missing explicit review trigger.", failures)
      else:
          expect(f"logs/active/<project-slug>/deliverables/{role}.md" in prompt, f"{role}: missing deliverable path in prompt.", failures)

    logs_readme = (ROOT / "logs/README.md").read_text()
    expect("Project goal" in logs_readme and "Latest deliverables" in logs_readme and "Next step" in logs_readme, "logs/README.md does not define continuity expectations clearly enough.", failures)
    expect("Direct execution still requires" in logs_readme, "logs/README.md does not define direct execution logging.", failures)
    expect("Best possible team assessment" in logs_readme, "logs/README.md missing best-team routing field.", failures)
    expect("best-team assessment shows specialist staffing would not materially improve the outcome" in logs_readme, "logs/README.md does not limit direct execution through best-team assessment.", failures)
    expect("Orchestrated work must" in logs_readme, "logs/README.md does not define orchestration requirements.", failures)
    expect("Treat role plans as advisory input to the orchestrator" in logs_readme, "logs/README.md missing advisory-plan contract.", failures)
    expect("Execute the approved cycle before allowing another material planning iteration" in logs_readme, "logs/README.md missing anti-churn execution rule.", failures)

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
