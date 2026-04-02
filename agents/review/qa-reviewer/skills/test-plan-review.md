---
name: test-plan-review
description: Review the proposed test strategy as risk coverage, not as a checklist of generic test types.
trigger: When a release or feature needs a better test strategy review.
primary_mcp: repository, logs
fallback_tools: reference/trace, search_query
best_guess_output: A test plan review with risk-based recommendations.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
section_anchor: "## Skill: test-plan-review"
done_when: Critical risks have explicit coverage, missing depth is visible, and blind spots are named.
---

# Test Plan Review

## Purpose

Review the proposed test strategy as risk coverage, not as a checklist of generic test types.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: test-plan-review`, include:
- `### Review framing`: Define the release scope, available test artifacts, and what risks the plan is expected to cover.
- `### Risk inventory`: Enumerate the major product, technical, and operational risks that need coverage.
- `### Coverage matrix`: Map each major risk to current planned tests, evidence, owners, and gaps.
- `### Depth by risk`: Evaluate whether each risk has appropriate depth across unit, integration, end-to-end, manual, or monitoring layers.
- `### Missing states and environments`: Call out missing coverage for breakpoints, browsers, data conditions, feature flags, failure paths, or permissions.
- `### Release-critical gaps`: Highlight the risks that remain under-tested enough to affect launch decisions.
- `### Recommended additions`: Suggest the highest-value test additions or reshaping of effort.
- `### Residual blind spots`: State what would still remain uncertain even after the proposed improvements.

## Tool Path

- Start with `repository, logs`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A test plan review with risk-based recommendations.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Review the plan against risk, not against idealized process.
- Prefer explicit risk-to-test mapping over generic statements like "add more E2E coverage."
- Separate missing coverage from insufficient depth. A risk can be covered but still be under-tested.
- Make environment and state coverage explicit because many release bugs hide outside the happy path.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/qa-reviewer.md`.
- Keep all work for this skill inside `## Skill: test-plan-review`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Critical risks have explicit coverage, missing depth is visible, and blind spots are named.
