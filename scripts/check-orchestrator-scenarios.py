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
    route_skill = (ROOT / "agents/orchestrator/orchestrator/skills/route.md").read_text()
    staff_skill = (ROOT / "agents/orchestrator/orchestrator/skills/staff.md").read_text()
    reconcile_skill = (ROOT / "agents/orchestrator/orchestrator/skills/reconcile.md").read_text()
    coordinate_skill = (ROOT / "agents/orchestrator/orchestrator/skills/coordinate.md").read_text()
    agents_fragment = (ROOT / "assets/AGENTS.fragment.md").read_text()

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
    expect("02_staffing.md" in orchestrator_prompt and "03_unified-plan.md" in orchestrator_prompt and "04_approval.md" in orchestrator_prompt, "Unified planning and approval files missing from orchestrator prompt.", failures)
    expect("status.md" in orchestrator_prompt and "context.md" in orchestrator_prompt, "Continuity files missing from orchestrator prompt.", failures)
    expect(
        "substantial multi-role execution" in orchestrator_prompt
        or "substantial multi-archetype execution" in orchestrator_prompt,
        "Approval gate missing from orchestrator prompt.",
        failures,
    )
    expect("This is the plan" in orchestrator_prompt, "Orchestrator prompt missing explicit approval handoff opener.", failures)
    expect("Do you want to proceed?" in orchestrator_prompt, "Orchestrator prompt missing explicit approval handoff question.", failures)
    expect(
        "03_unified-plan.md" in orchestrator_prompt
        and "04_approval.md" in orchestrator_prompt
        and "status.md" in orchestrator_prompt
        and "context.md" in orchestrator_prompt,
        "Orchestrator prompt missing required approval handoff log references.",
        failures,
    )
    expect("mismatch note" in orchestrator_prompt.lower(), "Misfit staffing path missing from orchestrator prompt.", failures)
    expect(
        "Request `plans/<role>.md` only when" in orchestrator_prompt
        or "Request `plans/<archetype>.md` only when" in orchestrator_prompt,
        "Orchestrator prompt missing optional specialist-planning rule.",
        failures,
    )
    expect("Preserve all material implementation detail" in orchestrator_prompt, "Orchestrator prompt missing detail-preservation rule.", failures)
    expect("Critical details that must survive merge" in orchestrator_prompt, "Orchestrator prompt missing must-carry detail contract.", failures)
    expect("author `03_unified-plan.md`" in orchestrator_prompt or "authors `03_unified-plan.md`" in orchestrator_prompt, "Orchestrator prompt missing authoritative plan ownership.", failures)
    expect("no piecemeal replanning" in orchestrator_prompt or "no repeated plan churn" in orchestrator_prompt, "Orchestrator prompt missing anti-churn guardrail.", failures)
    expect("role catalog" in orchestrator_prompt.lower(), "Orchestrator prompt missing role-catalog guidance.", failures)
    expect("Classify likely domain(s) first" in route_skill, "Route skill missing domain-first decision rule.", failures)
    expect("actual role needs rather than keywords alone" in route_skill, "Route skill missing anti-keyword-routing guidance.", failures)
    expect("Read the full canonical role catalog only when" in route_skill, "Route skill missing lazy role-catalog rule.", failures)
    expect("Coordination cost estimate" in route_skill, "Route skill missing coordination-cost output.", failures)
    expect("Bypass orchestration when the task is" in route_skill, "Route skill missing explicit bypass criteria.", failures)
    expect("Start from the best-team assessment recorded during routing" in staff_skill, "Staff skill missing routing-to-staffing continuity.", failures)
    expect("accept assignments directly unless" in staff_skill, "Staff skill missing assignment-first specialist behavior.", failures)
    expect("Request `plans/<role>.md` only when" in staff_skill, "Staff skill missing optional advisory-planning rule.", failures)
    expect("execution-grade detail" in staff_skill, "Staff skill missing detailed role-plan request rule.", failures)
    expect("Critical details that must survive merge" in staff_skill, "Staff skill missing must-carry detail request rule.", failures)
    expect("lossless" in reconcile_skill.lower(), "Reconcile skill missing lossless merge rule.", failures)
    expect("Critical detail register" in reconcile_skill, "Reconcile skill missing critical detail register output.", failures)
    expect("approved role plans alongside `03_unified-plan.md`" in coordinate_skill, "Coordinate skill missing role-plan carry-forward rule.", failures)
    expect("Do not replace execution-critical detail" in coordinate_skill, "Coordinate skill missing anti-summary guardrail.", failures)
    expect("Route by domain before staffing" in agents_fragment, "Managed AGENTS guidance missing domain-first routing instruction.", failures)
    expect("Default to direct Codex execution" in agents_fragment, "Managed AGENTS guidance missing direct-first instruction.", failures)
    expect("actual role needs, not task keywords alone" in agents_fragment, "Managed AGENTS guidance missing anti-keyword staffing rule.", failures)
    expect("skill-catalog.md" in agents_fragment, "Managed AGENTS guidance missing role-local skill catalog rule.", failures)
    expect("Request role plans only when" in agents_fragment, "Managed AGENTS guidance missing optional advisory-plan rule.", failures)
    expect("preserve all material specialist detail" in agents_fragment.lower(), "Managed AGENTS guidance missing detail-preservation rule.", failures)
    expect("Do you want to proceed?" in agents_fragment, "Managed AGENTS guidance missing explicit approval handoff question.", failures)

    approve_skill = (ROOT / "agents/orchestrator/orchestrator/skills/approve.md").read_text()
    expect("This is the plan" in approve_skill, "Approve skill missing explicit approval handoff opener.", failures)
    expect("Do you want to proceed?" in approve_skill, "Approve skill missing explicit approval handoff question.", failures)
    expect(
        "03_unified-plan.md" in approve_skill
        and "04_approval.md" in approve_skill
        and "status.md" in approve_skill
        and "context.md" in approve_skill,
        "Approve skill missing required approval handoff log references.",
        failures,
    )

    specialist_files = discover_toml_paths(ROOT)
    for path in specialist_files:
      data = load_toml(path)
      role = data["name"]
      prompt = data["system_prompt"]
      if role in {"orchestrator", "reference"}:
          continue

      expect("Default behavior" in prompt, f"{role}: missing default behavior heading.", failures)
      expect("skill-catalog.md" in prompt, f"{role}: missing role-local skill catalog instruction.", failures)
      expect("Read <skill-paths> skills for this task." in prompt, f"{role}: missing closing skill-read note contract.", failures)
      expect("assignment is clearly mismatched" in prompt, f"{role}: missing mismatch handling contract.", failures)
      expect("Only write `logs/active/<project-slug>/plans/" in prompt, f"{role}: missing optional plan trigger.", failures)
      expect("approval gate is in place" in prompt, f"{role}: missing conditional approval gating language.", failures)
      expect(f"logs/active/<project-slug>/plans/{role}.md" in prompt, f"{role}: missing plan path in prompt.", failures)
      expect("optional specialist input" in prompt.lower(), f"{role}: missing optional advisory-plan rule.", failures)
      expect("execution-grade plan" in prompt, f"{role}: missing detailed planning rule.", failures)
      expect("Critical details that must survive merge" in prompt, f"{role}: missing must-carry detail section contract.", failures)
      expect("Do not silently drop planned concrete details" in prompt, f"{role}: missing execution detail preservation rule.", failures)
      expect("Escalate blockers" in prompt or "escalate to the orchestrator" in prompt, f"{role}: missing escalation-before-replan rule.", failures)

      if data["execution_policy"]["role_kind"] == "reviewer":
          expect(f"logs/active/<project-slug>/reviews/{role}.md" in prompt, f"{role}: missing review path in prompt.", failures)
          expect("review pass" in prompt, f"{role}: missing explicit review trigger.", failures)
      else:
          expect(f"logs/active/<project-slug>/deliverables/{role}.md" in prompt, f"{role}: missing deliverable path in prompt.", failures)

    logs_readme = (ROOT / "logs/README.md").read_text()
    expect("Project goal" in logs_readme and "Latest deliverables" in logs_readme and "Next step" in logs_readme, "logs/README.md does not define continuity expectations clearly enough.", failures)
    expect("Direct execution still requires" in logs_readme, "logs/README.md does not define direct execution logging.", failures)
    expect("Domain classification" in logs_readme, "logs/README.md missing domain routing field.", failures)
    expect("best-team assessment shows specialist staffing would not materially improve the outcome" in logs_readme, "logs/README.md does not limit direct execution through best-team assessment.", failures)
    expect("Role Catalog Usage" in logs_readme, "logs/README.md missing role-catalog usage guidance.", failures)
    expect("Orchestrated work must" in logs_readme, "logs/README.md does not define orchestration requirements.", failures)
    expect("skill-catalog.md" in logs_readme, "logs/README.md missing role-local skill catalog guidance.", failures)
    expect("Treat role plans as optional advisory input to the orchestrator" in logs_readme, "logs/README.md missing optional advisory-plan contract.", failures)
    expect("Execution-grade specialist plan" in logs_readme, "logs/README.md missing detailed specialist plan contract.", failures)
    expect("Critical detail register" in logs_readme, "logs/README.md missing unified-plan detail register contract.", failures)
    expect("preserve all material specialist detail" in logs_readme.lower(), "logs/README.md missing detail-preservation rule.", failures)
    expect("Execute the approved cycle before allowing another material planning iteration" in logs_readme, "logs/README.md missing anti-churn execution rule.", failures)
    expect("This is the plan" in logs_readme, "logs/README.md missing explicit approval handoff opener.", failures)
    expect("Do you want to proceed?" in logs_readme, "logs/README.md missing explicit approval handoff question.", failures)

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
