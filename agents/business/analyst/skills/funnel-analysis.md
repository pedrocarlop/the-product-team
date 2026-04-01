---
name: funnel-analysis
description: Analyze a funnel to locate the main drop-offs, likely causes, and next actions.
trigger: When conversion or progression performance is under question.
primary_mcp: repository, notion
fallback_tools: search_query, reference/trace
best_guess_output: A funnel analysis with major drop-offs and hypotheses.
output_artifacts: logs/active/<project-slug>/deliverables/analyst.md
section_anchor: "## Skill: funnel-analysis"
done_when: The team knows where to focus and why.
---

# Funnel Analysis

## Purpose

Analyze a funnel to locate the main drop-offs, likely causes, and next actions.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: funnel-analysis`, include:
- `### Funnel stages`: Define the funnel stages and who or what moves through them.
- `### Stage performance`: Summarize the observed conversion or volume at each stage.
- `### Largest drop-offs`: Highlight the biggest losses or bottlenecks.
- `### Likely causes`: Provide plausible explanations tied to the evidence available.
- `### Recommended actions`: Suggest the highest-leverage next actions for the team.
- `### Data quality caveats`: Note missing events, attribution gaps, or sampling issues that limit confidence.

## Tool Path

- Start with `repository, notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/trace`.
- If both paths fail, produce the best-guess output described as: A funnel analysis with major drop-offs and hypotheses.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the funnel definition stable across the whole section so the analysis does not mix incompatible stage logic.
- Distinguish observed drop-offs from hypothesized causes.
- Recommend actions that match the level of certainty in the data.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/analyst.md`.
- Keep all work for this skill inside `## Skill: funnel-analysis`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team knows where to focus and why.
