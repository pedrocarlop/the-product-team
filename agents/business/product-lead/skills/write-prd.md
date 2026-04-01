---
name: write-prd
description: Write a delivery-grade PRD with scope, scenarios, decisions, and acceptance criteria.
trigger: When engineering or design need a precise product spec.
primary_mcp: notion, repository
fallback_tools: reference/ground, search_query
best_guess_output: A PRD or equivalent product specification.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
section_anchor: "## Skill: write-prd"
done_when: Executors can build without product ambiguity.
---

# Write PRD

## Purpose

Write a delivery-grade PRD with scope, scenarios, decisions, and acceptance criteria.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: write-prd`, include:
- `### Objective`: State the product objective and the user or business outcome the work should create.
- `### Scope`: Define what is included in this delivery slice.
- `### Non-goals`: Clarify nearby ideas that are explicitly not part of this effort.
- `### Key scenarios`: Describe the user scenarios or workflows the solution must support.
- `### Requirements and decisions`: Capture concrete product requirements and any settled decisions the team should treat as fixed.
- `### Acceptance criteria`: Give testable criteria that downstream executors can build and validate against.
- `### Dependencies and risks`: List cross-team dependencies, assumptions, and delivery risks.
- `### Open questions`: Flag unresolved decisions that still need follow-through.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A PRD or equivalent product specification.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Write requirements that are specific enough for execution without turning the deliverable into implementation pseudo-code.
- Preserve exact constraints, dates, and commitments from upstream source material.
- Keep open questions tight and actionable so the orchestrator can route follow-up cleanly.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Keep all work for this skill inside `## Skill: write-prd`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Executors can build without product ambiguity.
