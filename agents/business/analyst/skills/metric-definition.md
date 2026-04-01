---
name: metric-definition
description: Define the business or product metric model so downstream analysis measures the right thing.
trigger: When the team is debating how success or performance should be measured.
primary_mcp: notion, repository
fallback_tools: search_query, reference/ground
best_guess_output: A metric definition pack with formulas, segments, and caveats.
output_artifacts: logs/active/<project-slug>/deliverables/analyst.md
section_anchor: "## Skill: metric-definition"
done_when: The metric can be computed and interpreted consistently.
---

# Metric Definition

## Purpose

Define the business or product metric model so downstream analysis measures the right thing.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: metric-definition`, include:
- `### Metric name and purpose`: Define the metric and what decision it should support.
- `### Formula`: Specify the formula, inputs, exclusions, and aggregation logic.
- `### Segments and cuts`: List the segment dimensions or slices the team should use.
- `### Source of truth`: Name the source systems, tables, dashboards, or artifacts that should anchor the number.
- `### Caveats`: Capture interpretation limits, lag, or known blind spots.
- `### Instrumentation gaps`: Call out missing tracking or data-quality issues that weaken confidence.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A metric definition pack with formulas, segments, and caveats.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Prefer one operational definition over a long list of alternatives unless the ambiguity itself is the key finding.
- Be explicit about denominator choices, exclusions, and time windows.
- Preserve source-system naming where downstream analysts or engineers need exact traceability.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/analyst.md`.
- Keep all work for this skill inside `## Skill: metric-definition`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The metric can be computed and interpreted consistently.
