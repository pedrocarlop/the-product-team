---
name: reuse
description: Find approved patterns, components, and prior deliverables worth reusing before inventing new ones.
trigger: When a task may already be covered by an existing pattern.
primary_mcp: repository, deliverables
fallback_tools: reference/ground, search_query
best_guess_output: A reuse recommendation with exact patterns to follow.
output_artifacts: knowledge/reference-reuse.md
done_when: The preferred reusable pattern is explicit and justified.
---

# Reuse

## Purpose

Find approved patterns, components, and prior deliverables worth reusing before inventing new ones.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/reference-reuse.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

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

