---
name: atomic-library-build
description: Build or reorganize the component library using atomic design as the structuring model.
trigger: When reusable components need a clear system structure.
primary_mcp: figma
fallback_tools: paper, repository
best_guess_output: An atomic component library plan or build description.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
section_anchor: "## Skill: atomic-library-build"
done_when: Atoms, molecules, organisms, and higher-level patterns are clearly organized.
---

# Atomic Library Build

## Purpose

Build or reorganize the component library using atomic design as the structuring model.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: atomic-library-build`, include:
- `### Library scope`: Define what the library covers and what remains out of scope.
- `### Atomic layers`: Group the system into atoms, molecules, organisms, templates, or equivalent layers.
- `### Promotion rules`: State when something graduates from a one-off pattern into the shared library.
- `### Gap list`: Identify components or primitives that are still missing.
- `### Adoption order`: Recommend the order in which teams should consume or migrate to the library.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, repository`.
- If both paths fail, produce the best-guess output described as: An atomic component library plan or build description.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Use the atomic model as a structure, not as a reason to over-fragment the system.
- Treat `logs/active/<project-slug>/deliverables/project-ds-spec.md` as the canonical source for which primitives, component families, and widget/layout patterns should exist.
- Tie the library hierarchy back to how teams actually build screens.
- Call out where current components sit at the wrong layer today.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Also update `logs/active/<project-slug>/deliverables/project-ds-spec.md`.
- Keep all work for this skill inside `## Skill: atomic-library-build`.
- In `project-ds-spec.md`, update `## Atomic Primitives`, `## Component Families`, and `## Widget And Layout Patterns`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Atoms, molecules, organisms, and higher-level patterns are clearly organized.
