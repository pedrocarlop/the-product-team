---
name: design-code-mapping
description: Build a canonical system model of components, tokens, states, and ownership anchors before tracing how design artifacts map to implementation reality.
trigger: When design and engineering need a reliable bridge between system primitives, or when drift makes handoff and maintenance ambiguous.
analysis_framework: Design-to-code traceability with system-model construction, anchor matching, drift analysis, and ownership routing
primary_mcp: figma, repository
fallback_tools:
  - reference/trace
  - reference/verify
required_inputs:
  - current design-system source in design and code
  - concrete design anchors such as token names, component names, variants, or file references when available
  - current implementation packages, Storybook stories, or code anchors
  - `project-ds-spec.md` when it materially affects the intended mapping
recommended_passes:
  - canonical system model construction
  - anchor collection
  - design-to-code matching
  - drift and gap analysis
  - ownership routing
tool_stack:
  workspace:
    primary: [figma, repository]
    secondary: [reference/trace, reference/verify]
  implementation_truth:
    primary: [storybook, chromatic, github]
    secondary: [repository]
  documentation:
    primary: [zeroheight, supernova]
    secondary: [paper]
  fallback:
    primary: [reference/trace, reference/verify]
tool_routing:
  - if: both design and repo anchors are accessible
    use: [figma, repository]
  - if: Storybook, Chromatic, or code review history provides the clearest state or ownership evidence
    use: [storybook, chromatic, github]
  - if: component metadata or linked docs live in zeroheight or Supernova
    use: [zeroheight, supernova]
  - if: only partial traces exist
    use: [reference/trace, reference/verify]
best_guess_output: A design-code mapping with concrete anchors, traceable gaps, explicit ownership notes, and the minimum follow-up actions needed to close parity risk.
output_artifacts:
  - logs/active/<project-slug>/runs/<run-id>/deliverables/design-systems-designer-design-code-mapping.md
  - logs/active/<project-slug>/runs/<run-id>/deliverables/assets/ (for visual artifacts)
done_when: Design and engineering can identify the same primitives, states, and code anchors with enough precision to fix drift instead of debating what the system contains.
---

# Design Code Mapping

## Purpose

Create a traceable bridge between design-system artifacts and their implementation counterparts.

This skill applies canonical system modeling and anchor matching so the deliverable shows exactly what maps, what drifts, and who should fix the mismatch.

This skill does not satisfy the assignment with prose alone, or assume that a component documented in design must therefore exist in code.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` when Storybook, zeroheight, Supernova, Chromatic, or token platforms provide stronger traceability evidence than Figma alone.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/design-systems-designer-design-code-mapping.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `logs/active/<project-slug>/runs/<run-id>/deliverables/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

## Required Inputs And Assumptions

- Require concrete design anchors, concrete code anchors, and access to the repo or implementation surface.
- Prefer explicit identifiers, story names, file paths, token keys, and component names over inferred equivalence.
- If an anchor is missing, state `Assumed context:` and lower confidence for the mapping that depends on it.

## Input Mode And Evidence Path

- Prefer paired evidence from design and implementation. Documentation-only links are helpful but not sufficient proof of parity.
- Use Storybook or Chromatic when component states or variant behavior are easier to verify there than in code files alone.
- State where the mapping is exact, approximate, or unverified.

## Environment And Reproducibility

- Record the design source, code source, branch or snapshot, theme or brand scope, and any missing tools or permissions.
- Note whether the mapping covers tokens, components, composite patterns, or all three.
- Record any state coverage limitations such as missing interactive states or hidden design variants.

## Model Building

Build the canonical system model before findings:

- Design anchors: token collections, component names, variant properties, pattern sections
- Code anchors: package paths, exports, Storybook stories, theme variables, runtime wrappers
- Mapping status classes: exact, partial, missing in code, missing in design, renamed, or ambiguous
- Ownership surface: which team or role is best positioned to close each mismatch

## Required Deliverable Sections

Within `## Skill: design-code-mapping`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Mapping objective`
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Canonical system model`: Describe the design anchors, code anchors, and mapping-status classes.
- `### Mapping passes`
- `### Mapping table`: Provide a table with exactly these columns: `Design anchor`, `Token/component name`, `Code anchor`, `Status`, `Notes`.
- `### Drift and gap list`: Identify where design and code do not line up yet.
- `### Ownership notes`: State which team or role should close each mismatch.
- `### Follow-up actions`: List the next concrete fixes needed to complete the bridge.
- `### Mapping findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized parity risks`: Highlight mismatches that most directly harm delivery, QA, or adoption.
- `### Systemic patterns`: Group recurring issues such as naming divergence, wrapper leakage, or undocumented generated primitives.
- `### Recommendations`
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `figma, repository`.
- Use `storybook`, `chromatic`, or `github` when implementation states or ownership traces are clearer there.
- Use `zeroheight` or `supernova` when linked docs or component metadata strengthen traceability.
- Use `reference/trace, reference/verify` when only partial evidence exists.
- If all strong paths fail, produce the best-guess output and mark it `inferred`.

## Workflow Notes

- The mapping table is mandatory.
- Use concrete identifiers whenever available.
- Mark uncertain mappings explicitly instead of guessing silently.
- Do not treat documentation platforms or `project-ds-spec.md` as proof that code exists; they are intent sources, not implementation proof.
- When `project-ds-spec.md` recommends shadcn/ui, explicitly map `components.json`, registry namespaces, generated primitives, wrapper components, and token divergence from stock defaults.

## Prioritization Logic

- Highest priority: mapping gaps that block implementation, QA, or shared understanding of core system primitives.
- Medium priority: naming drift, wrapper ambiguity, or partial state mismatch that repeatedly slows teams.
- Lower priority: minor label differences that do not materially affect handoff or system maintenance.

