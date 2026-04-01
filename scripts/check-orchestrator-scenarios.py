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
    "engineer": "explicit_owner_only",
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
    route_skill = (ROOT / "agents/orchestrator/orchestrator/skills/route.md").read_text()
    staff_skill = (ROOT / "agents/orchestrator/orchestrator/skills/staff.md").read_text()
    coordinate_skill = (ROOT / "agents/orchestrator/orchestrator/skills/coordinate.md").read_text()
    agents_fragment = (ROOT / "assets/AGENTS.fragment.md").read_text()
    package_readme = (ROOT / "assets/package-README.md").read_text()
    logs_readme = (ROOT / "logs/README.md").read_text()

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
    expect(
        "parallel subagent" in orchestrator_prompt.lower() or "parallel agents" in orchestrator_prompt.lower(),
        "Orchestrator prompt missing parallel subagent delegation guidance.",
        failures,
    )
    expect(
        all(token in orchestrator_prompt for token in ("assignment_mode", "owned_outputs", "reads_from", "repo_write_owner", "repo_write_scope", "return_expected")),
        "Orchestrator prompt missing explicit assignment contract fields.",
        failures,
    )
    expect(
        "In direct execution, you may edit repo-tracked files yourself." in orchestrator_prompt,
        "Orchestrator prompt missing direct-mode repo write rule.",
        failures,
    )
    expect(
        "Once orchestration is chosen and a staffed implementation owner exists" in orchestrator_prompt,
        "Orchestrator prompt missing coordination-only-after-delegation rule.",
        failures,
    )
    expect(
        "Allow only one repo-writing owner per execution stage by default." in orchestrator_prompt,
        "Orchestrator prompt missing one-repo-owner-per-stage rule.",
        failures,
    )
    expect(
        "Staffing an implementation owner disables parallel main-thread implementation for that stage." in orchestrator_prompt,
        "Orchestrator prompt missing no-duplicate-main-thread-implementation rule.",
        failures,
    )

    # Orchestrator must use model_reasoning_effort (not reasoning_effort)
    orchestrator_raw = (ROOT / "agents/orchestrator/orchestrator/orchestrator.toml").read_text()
    expect(
        "model_reasoning_effort" in orchestrator_raw,
        "Orchestrator must use model_reasoning_effort (not reasoning_effort).",
        failures,
    )
    bare_key = re.search(r'^reasoning_effort\s*=', orchestrator_raw, re.MULTILINE)
    expect(
        bare_key is None,
        "Orchestrator uses legacy reasoning_effort key instead of model_reasoning_effort.",
        failures,
    )

    # Skill catalog checks
    expect("Read this file first on every request before meaningful work." in orchestrator_catalog, "Orchestrator skill catalog missing every-request scan rule.", failures)

    # Route skill checks
    expect("Classify likely domain(s) first" in route_skill, "Route skill missing domain-first decision rule.", failures)
    expect("Check `logs/TIMELINE.md`" in route_skill or "Read `logs/TIMELINE.md`" in route_skill, "Route skill missing timeline check.", failures)

    # Staff skill checks
    expect("One role = one subagent" in staff_skill, "Staff skill missing one-role-one-subagent rule.", failures)
    expect("minimum viable" in staff_skill, "Staff skill missing minimum viable team rule.", failures)
    expect("Repo write authority" in staff_skill, "Staff skill missing repo-write authority section.", failures)
    expect("Do not assign more than one repo-write owner in the same stage" in staff_skill, "Staff skill missing single repo owner guardrail.", failures)

    # Coordinate skill checks
    expect("assignment_mode" in coordinate_skill and "repo_write_owner" in coordinate_skill and "repo_write_scope" in coordinate_skill, "Coordinate skill missing explicit assignment contract.", failures)
    expect("Repo-tracked app code has a separate handoff rule" in coordinate_skill, "Coordinate skill missing repo ownership handoff rule.", failures)
    expect("Do not allow duplicate repo owners for the same stage" in coordinate_skill, "Coordinate skill missing duplicate repo owner guardrail.", failures)

    # AGENTS fragment checks
    expect("Route every request in this repository through `product-team-orchestrator` by default." in agents_fragment, "Managed AGENTS guidance missing all-requests-through-orchestrator rule.", failures)
    expect("Only bypass Product Team when the user explicitly says not to use Product Team" in agents_fragment, "Managed AGENTS guidance missing explicit opt-out rule.", failures)
    expect("Do not infer an opt-out from simplicity, urgency, or implementation bias alone." in agents_fragment, "Managed AGENTS guidance missing no-inferred-opt-out rule.", failures)
    expect("Route by domain before staffing" in agents_fragment, "Managed AGENTS guidance missing domain-first routing instruction.", failures)
    expect("Default to direct Codex execution" in agents_fragment, "Managed AGENTS guidance missing direct-first instruction.", failures)
    expect("skill-catalog.md" in agents_fragment, "Managed AGENTS guidance missing role-local skill catalog rule.", failures)
    expect("repo_write_owner" in agents_fragment and "repo_write_scope" in agents_fragment, "Managed AGENTS guidance missing explicit repo ownership contract.", failures)
    expect("Repo-tracked app code must have one explicit implementation owner per stage." in agents_fragment, "Managed AGENTS guidance missing one-owner repo rule.", failures)

    # Package README checks
    expect("Every request in this repository should go through `product-team-orchestrator` by default." in package_readme, "Package README missing default-all-requests-through-orchestrator rule.", failures)
    expect("Only an explicit user opt-out" in package_readme, "Package README missing explicit opt-out rule.", failures)
    expect("the direct path is chosen inside the orchestrator" in package_readme, "Package README missing direct-inside-orchestrator clarification.", failures)
    expect("Repo-tracked app code is stricter: one explicit implementation owner per stage by default." in package_readme, "Package README missing repo implementation ownership rule.", failures)

    # Logs README checks
    expect("The orchestrator assigns repo implementation with an explicit contract" in logs_readme, "logs/README.md missing explicit repo ownership contract.", failures)
    expect("Only one explicit `repo_write_owner` should exist per execution stage by default." in logs_readme, "logs/README.md missing single repo owner rule.", failures)

    # Specialist checks
    specialist_files = discover_toml_paths(ROOT)
    prompts_by_role: dict[str, str] = {}
    for path in specialist_files:
        data = load_toml(path)
        role = data["name"]
        prompt = data["system_prompt"]
        prompts_by_role[role] = prompt
        if role in {"orchestrator", "reference"}:
            continue

        expect("Default behavior" in prompt, f"{role}: missing default behavior heading.", failures)
        expect("skill-catalog.md" in prompt, f"{role}: missing role-local skill catalog instruction.", failures)
        expect("assignment is clearly mismatched" in prompt, f"{role}: missing mismatch handling contract.", failures)
        expect("Escalate blockers" in prompt or "escalate to the orchestrator" in prompt, f"{role}: missing escalation rule.", failures)
        expect(
            all(token in prompt for token in ("assignment_mode", "owned_outputs", "reads_from", "repo_write_owner", "repo_write_scope", "return_expected")),
            f"{role}: missing explicit assignment contract fields.",
            failures,
        )
        expect("repo-tracked files" in prompt, f"{role}: missing repo-tracked file guardrail.", failures)
        expected_policy = expected_repo_write_policy(role)
        expect(
            data["execution_policy"].get("repo_write_policy") == expected_policy,
            f"{role}: repo_write_policy must be {expected_policy!r}.",
            failures,
        )
        if expected_policy == "explicit_owner_only":
            expect(
                f'`repo_write_owner = "{role}"`' in prompt and "`repo_write_scope`" in prompt,
                f"{role}: missing explicit repo ownership implementation rule.",
                failures,
            )
        else:
            expect(
                "You never own repo-tracked implementation in staffed workflows." in prompt,
                f"{role}: missing artifact-only repo implementation refusal rule.",
                failures,
            )

        if data["execution_policy"]["role_kind"] == "reviewer":
            expect(f"logs/active/<project-slug>/reviews/{role}.md" in prompt, f"{role}: missing review path in prompt.", failures)
        else:
            expect(f"logs/active/<project-slug>/deliverables/{role}.md" in prompt, f"{role}: missing deliverable path in prompt.", failures)

        # Verify Codex-native model_reasoning_effort key is used
        raw_toml = path.read_text()
        expect(
            "model_reasoning_effort" in raw_toml,
            f"{role}: must use model_reasoning_effort (not reasoning_effort).",
            failures,
        )
        bare_key = re.search(r'^reasoning_effort\s*=', raw_toml, re.MULTILINE)
        expect(
            bare_key is None,
            f"{role}: uses legacy reasoning_effort key instead of model_reasoning_effort.",
            failures,
        )

    # Logs README checks
    expect("context.md" in logs_readme, "logs/README.md missing context.md reference.", failures)
    expect("TIMELINE.md" in logs_readme, "logs/README.md missing TIMELINE.md reference.", failures)

    role_catalog = ROOT / "references" / "role-catalog.md"
    expect(role_catalog.exists(), "references/role-catalog.md is missing.", failures)

    # Regression scenarios
    expect(
        "Once orchestration is chosen and a staffed implementation owner exists" in orchestrator_prompt
        and "You never own repo-tracked implementation in staffed workflows." in prompts_by_role.get("product-lead", "")
        and "You never own repo-tracked implementation in staffed workflows." in prompts_by_role.get("designer", "")
        and '`repo_write_owner = "engineer"`' in prompts_by_role.get("engineer", ""),
        "Regression scenario missing: cross-functional workflow must keep product/design artifact-only while the engineer owns repo implementation and the orchestrator stops coding in parallel.",
        failures,
    )
    expect(
        "In direct execution, you may edit repo-tracked files yourself." in orchestrator_prompt,
        "Regression scenario missing: single-domain direct execution must still allow orchestrator repo edits.",
        failures,
    )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Prompt-level orchestrator scenario checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
