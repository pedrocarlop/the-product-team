---
name: ground
description: Ground decisions in the real target repo and any named source system before proposing work.
trigger: When a role needs factual grounding before choosing a path.
primary_mcp: repository, named source systems
fallback_tools: search_query, open
best_guess_output: A concise grounding inventory with sources and unknowns.
output_artifacts: logs/active/<project-slug>/deliverables/reference.md
section_anchor: "## Skill: ground"
done_when: The team can cite concrete repo/system evidence instead of assumptions.
---

# Ground

## Purpose

Ground decisions in the real target repo and any named source system before proposing work.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

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

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/reference.md`.
- Keep all work for this skill inside `## Skill: ground`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team can cite concrete repo/system evidence instead of assumptions.
