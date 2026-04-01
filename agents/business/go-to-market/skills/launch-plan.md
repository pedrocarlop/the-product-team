---
name: launch-plan
description: Build the launch plan with milestones, owners, dependencies, and readiness checks.
trigger: When a feature or product is moving toward release.
primary_mcp: notion, linear
fallback_tools: go-to-market/positioning-brief, search_query
best_guess_output: A launch plan with owners and launch gates.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
section_anchor: "## Skill: launch-plan"
done_when: The launch can be run without missing critical steps.
---

# Launch Plan

## Purpose

Build the launch plan with milestones, owners, dependencies, and readiness checks.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: launch-plan`, include:
- `### Launch scope`: Define what is launching and what is excluded from this launch.
- `### Milestones and gates`: List the major checkpoints and the criteria to clear each one.
- `### Owners`: Assign owners or owning teams to the critical workstreams.
- `### Dependencies`: Capture upstream or cross-functional dependencies.
- `### Readiness checklist`: Provide the concrete checks that determine if the launch is ready.
- `### Risks and blockers`: Call out risks, unresolved blockers, and what would delay launch.
- `### Open decisions`: Note the launch-time decisions that still need resolution.

## Tool Path

- Start with `notion, linear`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `go-to-market/positioning-brief, search_query`.
- If both paths fail, produce the best-guess output described as: A launch plan with owners and launch gates.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Make the critical path visible instead of presenting every task as equally important.
- Tie readiness checks to observable evidence, not vague confidence.
- Keep owners and blockers current enough that a launch manager could run from the artifact.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Keep all work for this skill inside `## Skill: launch-plan`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The launch can be run without missing critical steps.
