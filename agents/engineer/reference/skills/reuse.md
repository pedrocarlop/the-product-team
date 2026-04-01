---
name: reuse
description: Find approved patterns, components, and prior deliverables worth reusing before inventing new ones.
trigger: When a task may already be covered by an existing pattern.
primary_mcp: repository, deliverables
fallback_tools: reference/ground, search_query
best_guess_output: A reuse recommendation with exact patterns to follow.
output_artifacts: logs/active/<project-slug>/deliverables/reference.md
section_anchor: "## Skill: reuse"
done_when: The preferred reusable pattern is explicit and justified.
---

# Reuse

## Purpose

Find approved patterns, components, and prior deliverables worth reusing before inventing new ones.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: reuse`, include:
- `### Target problem`: Define what the team is trying to solve or avoid reinventing.
- `### Reusable candidates`: List the strongest reuse candidates found.
- `### Preferred pattern`: Name the recommended reusable pattern or artifact.
- `### Why chosen`: Explain why that option is the best fit.
- `### Exact files or artifacts to follow`: Identify the precise paths, components, or deliverables to copy from.
- `### Caveats`: Note mismatches, limits, or adjustments that still need care.

## Tool Path

- Start with `repository, deliverables`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A reuse recommendation with exact patterns to follow.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Prefer approved reuse paths over generic similarity.
- Keep exact file or artifact references concrete enough that downstream engineers can follow them directly.
- State why near-miss patterns were rejected so teams do not rediscover the same dead ends.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/reference.md`.
- Keep all work for this skill inside `## Skill: reuse`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The preferred reusable pattern is explicit and justified.
