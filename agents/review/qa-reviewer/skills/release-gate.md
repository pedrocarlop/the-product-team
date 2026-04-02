---
name: release-gate
description: Make the ship or no-ship recommendation by weighing blockers, residual risk, evidence quality, and rollback posture.
trigger: When work is nearing release and needs a QA gate.
primary_mcp: repository, logs
fallback_tools: qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review
best_guess_output: A release gate recommendation with blocking issues and residual risk.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
section_anchor: "## Skill: release-gate"
done_when: The release recommendation is unambiguous, evidence-based, and explicit about residual risk.
---

# Release Gate

## Purpose

Make the ship or no-ship recommendation by weighing blockers, residual risk, evidence quality, and rollback posture.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: release-gate`, include:
- `### Gate framing`: Define the exact release candidate, scope, environment, and decision horizon.
- `### Evidence reviewed`: Summarize the requirements, test evidence, runtime evidence, and open issues considered.
- `### Ship recommendation`: State ship, ship with explicit risk acceptance, or no-ship, with one clear recommendation.
- `### Blocking issues`: List the conditions that must be resolved before release when the recommendation is not clean ship.
- `### Non-blocking risks`: Record residual risks that do not block release but still require ownership or follow-up.
- `### Evidence quality and confidence`: Explain how strong, partial, or stale the underlying evidence is.
- `### Rollback and readiness posture`: Capture rollback availability, monitoring posture, owner readiness, and containment options.
- `### Required follow-up`: State the exact next actions, owners, or checks needed after the gate.
- `### Limits and unknowns`: Explain what decision uncertainty remains.

## Tool Path

- Start with `repository, logs`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review`.
- If both paths fail, produce the best-guess output described as: A release gate recommendation with blocking issues and residual risk.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- A release gate is a synthesis skill. It should integrate evidence from other review work instead of re-running every check from scratch.
- Keep the recommendation binary at the top level even when nuance exists underneath.
- Separate lack of evidence from evidence of safety. Missing proof should lower confidence, not silently become a pass.
- Document what makes a risk acceptable now, not just what is broken.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/qa-reviewer.md`.
- Keep all work for this skill inside `## Skill: release-gate`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The release recommendation is unambiguous, evidence-based, and explicit about residual risk.
