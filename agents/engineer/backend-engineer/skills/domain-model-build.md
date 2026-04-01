---
name: domain-model-build
description: Implement the core backend domain logic and data transformations for a feature.
trigger: When business rules or backend state transitions must be encoded.
primary_mcp: repository
fallback_tools: reference/ground, reference/trace
best_guess_output: A backend domain model implementation or design.
output_artifacts: logs/active/<project-slug>/deliverables/backend-engineer.md
section_anchor: "## Skill: domain-model-build"
done_when: Core rules are explicit and live in a clear source of truth.
---

# Domain Model Build

## Purpose

Implement the core backend domain logic and data transformations for a feature.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: domain-model-build`, include:
- `### Domain entities or concepts`: Define the key entities, records, or concepts involved.
- `### Core rules`: State the domain rules or business logic that must hold.
- `### State transitions`: Describe lifecycle changes, transitions, or guarded mutations.
- `### Data transformations`: Explain derived data, normalization, or transformation logic.
- `### Code touchpoints`: Identify the modules, services, or model files involved.
- `### Open risks`: Call out ambiguity, edge cases, or domain gaps that remain.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, reference/trace`.
- If both paths fail, produce the best-guess output described as: A backend domain model implementation or design.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the core rules explicit enough that later changes do not splinter the domain model.
- Separate foundational domain logic from transport or API concerns.
- Preserve exact model or service names where downstream roles need a stable source of truth.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/backend-engineer.md`.
- Keep all work for this skill inside `## Skill: domain-model-build`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Core rules are explicit and live in a clear source of truth.
