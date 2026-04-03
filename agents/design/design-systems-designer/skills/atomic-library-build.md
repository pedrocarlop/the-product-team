---
name: atomic-library-build
description: Build a component-library structure by modeling primitives, composition layers, promotion rules, and system boundaries before assigning atoms, molecules, organisms, and higher-level patterns.
trigger: When reusable components need a clearer system structure, a library reorganization, or a repeatable promotion path from one-off patterns into shared assets.
analysis_framework: Atomic-design-informed library structuring with composition modeling, duplication tracing, promotion analysis, and adoption sequencing
primary_mcp: figma
fallback_tools:
  - paper
  - repository
required_inputs:
  - current component inventory in design or code
  - `project-ds-spec.md` when it exists
  - known product patterns, widget families, or layout shells
  - current reuse problems, promotion bottlenecks, or migration goals when known
recommended_passes:
  - library inventory
  - composition model construction
  - layer assignment
  - promotion and gap analysis
  - adoption sequencing
tool_stack:
  workspace:
    primary: [figma, repository]
    secondary: [paper]
  documentation:
    primary: [zeroheight, supernova]
    secondary: [paper]
  implementation_truth:
    primary: [storybook, chromatic]
    secondary: [repository]
  fallback:
    primary: [paper, repository]
tool_routing:
  - if: design and component grouping live primarily in design files
    use: [figma]
  - if: implementation packages or Storybook reveal the real library structure better than design
    use: [repository, storybook, chromatic]
  - if: component cataloging, status, or system documentation is stronger in zeroheight or Supernova
    use: [zeroheight, supernova]
  - if: only static exports or notes exist
    use: [paper, repository]
best_guess_output: An atomic component-library structure with explicit layers, promotion rules, missing pieces, and a pragmatic migration order.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer-atomic-library-build.md
done_when: The team has a defensible library structure, knows what belongs in each layer, and can promote or reject new shared components without re-litigating the model.
---

# Atomic Library Build

## Purpose

Organize the component library around real composition layers rather than a flat pile of reusable pieces.

This skill applies an atomic-design-informed method: inventory the library, model how primitives compose into larger patterns, identify duplication or layer confusion, and then define promotion rules and adoption order.

This skill does not force every pattern into atomic design dogma, or use the language of atoms and organisms to justify over-fragmented libraries.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` when Storybook, zeroheight, Supernova, or other library-management tooling provides stronger evidence than design files alone.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/design-systems-designer-atomic-library-build.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Inputs And Assumptions

- Require the current component inventory, current reuse pain points, and `project-ds-spec.md` when it exists.
- Prefer evidence from actual reusable assets and implemented patterns over roadmap aspirations.
- If the current library boundary is unclear, infer the smallest stable scope and mark it `Assumed context:`.

## Input Mode And Evidence Path

- Prefer live component inventories in design and code, then documentation platforms, then static exports, then inference.
- When Storybook exists, use it to validate stateful component boundaries and real implementation groupings.
- State which parts of the library were validated from actual reusable components versus only described in docs.

## Environment And Reproducibility

- Record which design files, packages, Storybook catalogs, or docs were used.
- Capture whether the library is product-specific, platform-shared, or multi-brand.
- Note any missing runtime or documentation access that limits certainty about component boundaries.

## Model Building

Build the library model before findings:

- Primitives: tokens, icons, typography, and low-level affordances
- Component layers: atoms, molecules, organisms, templates, and product-specific patterns when applicable
- Promotion boundary: what must be stable before entering the shared library
- Consumption surfaces: how teams actually assemble screens and flows

## Required Deliverable Sections

Within `## Skill: atomic-library-build`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Library objective`
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Library model`: Describe primitives, composition layers, and promotion boundaries.
- `### Library passes`
- `### Library scope`: Define what the library covers and what remains out of scope.
- `### Atomic layers`: Group the system into atoms, molecules, organisms, templates, or equivalent layers.
- `### Promotion rules`: State when something graduates from a one-off pattern into the shared library.
- `### Gap list`: Identify components or primitives that are still missing.
- `### Adoption order`: Recommend the order in which teams should consume or migrate to the library.
- `### Library findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized structure risks`: Highlight the structural failures most likely to create duplication or slow adoption.
- `### Systemic patterns`: Group recurring layer confusion, wrapper proliferation, or component-family overlap.
- `### Recommendations`
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `figma`.
- Use `repository`, `storybook`, or `chromatic` when code structure reveals the real reusable boundaries better than design.
- Use `zeroheight` or `supernova` when component catalogs, documentation, or status metadata materially improve the inventory.
- Use `paper, repository` when only static evidence exists.
- If strong paths fail, provide the best-guess output and mark it with the correct evidence label.

## Workflow Notes

- Use atomic design as a structuring heuristic, not a rigid taxonomy.
- Tie every proposed layer to how teams actually build screens.
- Call out components that sit at the wrong layer today and explain why.
- Prefer fewer, clearer shared layers over a clever hierarchy that teams will not maintain.
- Use `project-ds-spec.md` as the canonical target for primitives, families, and widget patterns.

## Prioritization Logic

- Highest priority: mis-layering or missing primitives that cause widespread duplication or inconsistent composition.
- Medium priority: promotion-rule ambiguity that causes reusable assets to sprawl or stagnate.
- Lower priority: taxonomy cleanup that does not materially change how teams build or adopt components.

