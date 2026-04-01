---
name: component-governance
description: Define the rules for component ownership, variants, contribution, and deprecation.
trigger: When system growth needs operating rules, not just files.
primary_mcp: notion, figma
fallback_tools: repository, reference/reuse
best_guess_output: A governance model for component lifecycle and usage.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
section_anchor: "## Skill: component-governance"
done_when: Teams know how components enter, change, and leave the system.
---

# Component Governance

## Purpose

Define the rules for component ownership, variants, contribution, and deprecation.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: component-governance`, include:
- `### Ownership model`: Define who owns design, code, and release decisions for shared components.
- `### Contribution flow`: Describe how new components or changes are proposed and reviewed.
- `### Variant rules`: Set the rules for when to add, split, or reject variants.
- `### Deprecation policy`: Explain how components are sunset and migrated safely.
- `### Exception handling`: Document how urgent or one-off exceptions are approved and tracked.

## Tool Path

- Start with `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `repository, reference/reuse`.
- If both paths fail, produce the best-guess output described as: A governance model for component lifecycle and usage.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Write governance as an operating system teams can follow, not a slogan.
- Make ownership boundaries between design and engineering explicit.
- Prefer fewer, more durable rules over exhaustive bureaucracy.
- Treat `project-ds-spec.md` as the canonical handoff into the product's DS folder, and write governance that preserves that contract.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Also update `logs/active/<project-slug>/deliverables/project-ds-spec.md`.
- Keep all work for this skill inside `## Skill: component-governance`.
- In `project-ds-spec.md`, update `## Governance And Adoption`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Teams know how components enter, change, and leave the system.
