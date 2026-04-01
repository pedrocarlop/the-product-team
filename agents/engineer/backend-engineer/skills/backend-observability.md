---
name: backend-observability
description: Add or refine logging, metrics, and diagnostics around backend behavior.
trigger: When debugging or operations depend on better backend visibility.
primary_mcp: repository
fallback_tools: search_query, reference/reuse
best_guess_output: An observability change or backend diagnostics plan.
output_artifacts: logs/active/<project-slug>/deliverables/backend-engineer.md
section_anchor: "## Skill: backend-observability"
done_when: Important backend behavior can be inspected after deployment.
---

# Backend Observability

## Purpose

Add or refine logging, metrics, and diagnostics around backend behavior.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: backend-observability`, include:
- `### Coverage goal`: Explain what backend behavior needs better visibility and why.
- `### Signals to add or refine`: Specify the logs, metrics, traces, or diagnostics to change.
- `### Where instrumentation lands`: Identify the services, code paths, or runtime boundaries involved.
- `### Alerting or debugging use`: State how the new signals should be used operationally.
- `### Risk or cost tradeoffs`: Note noise, cost, privacy, or performance tradeoffs.
- `### Verification notes`: Explain how to confirm the instrumentation is useful and working.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/reuse`.
- If both paths fail, produce the best-guess output described as: An observability change or backend diagnostics plan.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Optimize for actionable signals rather than maximum instrumentation volume.
- Preserve any existing observability patterns that should be reused instead of creating new conventions.
- Make operational consumers of the signals explicit so later teams know what “good” looks like.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/backend-engineer.md`.
- Keep all work for this skill inside `## Skill: backend-observability`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Important backend behavior can be inspected after deployment.
