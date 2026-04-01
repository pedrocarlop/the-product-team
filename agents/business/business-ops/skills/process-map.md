---
name: process-map
description: Map the current and target process so gaps and handoffs are visible.
trigger: When a workflow is unclear, inefficient, or changing.
primary_mcp: notion
fallback_tools: search_query, reference/ground
best_guess_output: A current-state and future-state process map.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops.md
section_anchor: "## Skill: process-map"
done_when: Owners, steps, and gaps are explicit.
---

# Process Map

## Purpose

Map the current and target process so gaps and handoffs are visible.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: process-map`, include:
- `### Current-state flow`: Describe how the process works today.
- `### Target-state flow`: Describe the intended future-state process.
- `### Owners and handoffs`: Identify ownership and handoff points across the flow.
- `### Bottlenecks`: Highlight the biggest delays, confusion points, or friction.
- `### Gaps`: Note missing steps, unclear ownership, or tooling holes.
- `### Recommended changes`: Summarize the changes needed to move from current state to target state.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A current-state and future-state process map.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the process representation linear enough to follow, even if the real system has edge cases.
- Separate observed current-state behavior from the recommended future state.
- Preserve role names and tooling references exactly when downstream ops work depends on them.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/business-ops.md`.
- Keep all work for this skill inside `## Skill: process-map`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Owners, steps, and gaps are explicit.
