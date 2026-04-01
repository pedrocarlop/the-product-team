---
name: campaign-brief
description: Prepare a campaign brief with audience, channel, creative direction, and KPI.
trigger: When marketing execution needs a crisp brief.
primary_mcp: notion
fallback_tools: search_query, go-to-market/positioning-brief
best_guess_output: A campaign brief ready for creative or channel execution.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
section_anchor: "## Skill: campaign-brief"
done_when: Execution teams know the target, message, and metric.
---

# Campaign Brief

## Purpose

Prepare a campaign brief with audience, channel, creative direction, and KPI.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: campaign-brief`, include:
- `### Objective`: State the campaign goal and what success should change.
- `### Audience`: Define the target audience and any key segmentation.
- `### Core message`: Summarize the primary message or angle the campaign should carry.
- `### Channels`: Name the channels, surfaces, or media the campaign should use.
- `### Creative direction`: Describe the creative approach, tone, or constraints that should guide execution.
- `### KPI and measurement`: Define the KPI and how performance should be tracked.
- `### Dependencies`: Note key assets, approvals, or coordination needs.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, go-to-market/positioning-brief`.
- If both paths fail, produce the best-guess output described as: A campaign brief ready for creative or channel execution.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the brief executable by channel or creative teams without a second translation pass.
- Reuse established positioning language when it exists; do not invent a conflicting thesis.
- Make the KPI specific enough that reporting can tie back to the brief later.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Keep all work for this skill inside `## Skill: campaign-brief`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Execution teams know the target, message, and metric.
