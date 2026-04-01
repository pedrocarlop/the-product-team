---
name: dashboard-story
description: Turn operational or product metrics into a narrative summary for the team.
trigger: When a dashboard exists but the team needs the story behind the numbers.
primary_mcp: notion, repository
fallback_tools: analyst/funnel-analysis, search_query
best_guess_output: A narrative metrics readout with key insights and actions.
output_artifacts: logs/active/<project-slug>/deliverables/analyst.md
section_anchor: "## Skill: dashboard-story"
done_when: A reader can understand the important story without opening the dashboard first.
---

# Dashboard Story

## Purpose

Turn operational or product metrics into a narrative summary for the team.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: dashboard-story`, include:
- `### Executive summary`: Lead with the most important takeaway.
- `### Key metrics`: Name the few metrics that matter most to the story.
- `### Important changes`: Explain notable movement, anomalies, or trend breaks.
- `### What matters`: Interpret why those changes matter to the business or team.
- `### Recommended actions`: Suggest concrete next moves.
- `### Watch list`: Flag metrics or risks that need continued monitoring.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `analyst/funnel-analysis, search_query`.
- If both paths fail, produce the best-guess output described as: A narrative metrics readout with key insights and actions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Prioritize interpretation over raw metric dumps.
- Keep the story tightly scoped to the audience and operating cadence implied by the request.
- Separate noise from signal so the team does not chase temporary variance.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/analyst.md`.
- Keep all work for this skill inside `## Skill: dashboard-story`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A reader can understand the important story without opening the dashboard first.
