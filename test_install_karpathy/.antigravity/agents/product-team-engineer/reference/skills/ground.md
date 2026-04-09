---
name: ground
description: Ground decisions in the real target repo and any named source system before proposing work.
trigger: When a role needs factual grounding before choosing a path.
primary_mcp: repository, named source systems
fallback_tools: search_query, open
best_guess_output: A concise grounding inventory with sources and unknowns.
output_artifacts: knowledge/reference-ground.md
done_when: The team can cite concrete repo/system evidence instead of assumptions.
---

# Ground

## Purpose

Ground decisions in the real target repo and any named source system before proposing work.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/reference-ground.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: ground`, include:
- `### Question being grounded`: State the question or uncertainty this grounding pass addresses.
- `### Sources checked`: List the repo, documents, systems, or tools consulted.
- `### Confirmed facts`: Record the concrete facts established from those sources.
- `### Unknowns`: Capture what could not be confirmed.
- `### Implications for downstream roles`: Explain what later specialists should take forward.

## Tool Path

- Start with `repository, named source systems`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, open`.
- If both paths fail, produce the best-guess output described as: A concise grounding inventory with sources and unknowns.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the artifact fact-first; downstream roles should be able to quote it without reinterpreting.
- Separate present-state facts from assumptions or inferred conclusions.
- Preserve exact source paths, names, or identifiers when they matter to later implementation work.

