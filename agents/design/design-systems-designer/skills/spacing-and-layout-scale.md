---
name: spacing-and-layout-scale
description: Build a layout-system model across spacing primitives, composition roles, breakpoints, and density expectations before defining the scale and its usage rules.
trigger: When teams are inventing spacing ad hoc, layout rhythm is inconsistent, or the system needs a clear spatial foundation that can survive responsive implementation.
analysis_framework: Layout-scale design with spatial inventory, semantic role mapping, breakpoint analysis, and migration prioritization
primary_mcp: figma
fallback_tools:
  - paper
  - repository
required_inputs:
  - current layouts, spacing usage, and breakpoint behavior in design or code
  - `project-ds-spec.md` when it exists
  - known density expectations or platform constraints
  - target breakpoints, grids, or container behavior when available
recommended_passes:
  - spatial inventory
  - layout model construction
  - scale candidate analysis
  - semantic role mapping
  - breakpoint and density analysis
  - migration sequencing
tool_stack:
  workspace:
    primary: [figma, repository]
    secondary: [paper]
  design_authoring:
    primary: [penpot, tokens_studio]
    secondary: [supernova]
  implementation_truth:
    primary: [storybook, chromatic]
    secondary: [repository]
  fallback:
    primary: [paper, repository]
tool_routing:
  - if: the most reliable layout evidence lives in Figma or design files
    use: [figma]
  - if: spacing tokens or layout primitives are maintained in Penpot, Tokens Studio, or Supernova exports
    use: [penpot, tokens_studio, supernova]
  - if: responsive behavior and component spacing are easier to verify in code
    use: [repository, storybook, chromatic]
  - if: only screenshots, static exports, or notes exist
    use: [paper, repository]
best_guess_output: A spacing and layout scale with explicit primitives, semantic usage rules, breakpoint behavior, migration guidance, and known exceptions.
output_artifacts:
  - knowledge/runs/<run-id>/design-systems-designer-spacing-and-layout-scale.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: Designers and engineers have a scale and semantic usage map they can apply to real layouts without reinventing spacing, breakpoint, or density rules.
---

# Spacing And Layout Scale

## Purpose

Define a spacing and layout scale that fits actual product composition instead of idealized examples.

This skill applies spatial inventory, breakpoint analysis, and semantic-role mapping to turn scattered spacing choices into a reusable layout system.

This skill does not produce a tidy numeric scale without validating real composition needs, or pretend every layout problem should be solved by one spacing token ladder.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` when the assignment references token tooling, Storybook, Penpot, or other system platforms that may hold stronger layout evidence.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-systems-designer-spacing-and-layout-scale.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/runs/<run-id>/assets/`. 
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/runs/<run-id>/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths.
  - For `take_screenshot`, you MUST supply the `filePath` parameter pointing directly to the destination in the project workspace.
  - For `generate_image`, or tools that save to your `.gemini`/`.antigravity` brain directory or `/tmp`, you MUST use bash to manually move the image file into the project directory.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths or paths outside the workspace.

## Required Inputs And Assumptions

- Require real product layouts, key screen types, breakpoint expectations, and `project-ds-spec.md` when it exists.
- Require enough evidence to understand stack spacing, inset spacing, section rhythm, container widths, and density behavior.
- If breakpoints or density expectations are missing, infer them conservatively and mark them `Assumed context:`.

## Input Mode And Evidence Path

- Prefer live layout evidence from design files and implementation over abstract spacing guidelines.
- Use Storybook or code evidence when responsive behavior or component internals are more trustworthy than static design mocks.
- State whether the scale was validated against real breakpoints or only inferred from desktop artifacts.

## Environment And Reproducibility

- Record the surfaces inspected, breakpoint or viewport assumptions, theme or density assumptions, and any missing runtime states.
- Note whether the scale is intended for web only or must generalize across multiple platforms.
- Record any constraints such as legacy CSS utilities or grid systems that materially affect the recommendation.

## Model Building

Build the layout model before findings:

- Spatial primitives: inset, stack, gap, section, container, grid, and radius-adjacent spacing when relevant
- Composition layers: component internal spacing, component-to-component spacing, page-section rhythm, and outer shell spacing
- Responsive behavior: breakpoint changes, density shifts, container changes, and content-driven exceptions

## Required Deliverable Sections

Within `## Skill: spacing-and-layout-scale`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Scale objective`
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Layout model`: Describe the spatial primitives, composition layers, and responsive behavior model.
- `### Scale passes`
- `### Scale definition`: Define the core spacing and sizing values and how they relate.
- `### Semantic usage`: Map raw values to semantic layout roles such as stack, inset, gap, or section spacing.
- `### Breakpoint adjustments`: Describe any breakpoint-specific spacing behavior.
- `### Exceptions`: Call out where the scale should intentionally bend or stop.
- `### Migration notes`: Explain how existing layouts should move onto the scale.
- `### Spacing findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized layout risks`: Highlight the spacing or layout failures that most harm consistency or implementation clarity.
- `### Systemic patterns`: Group recurring issues such as mixed density models, container drift, or component-level spacing hacks.
- `### Recommendations`
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `figma`.
- Use `repository`, `storybook`, or `chromatic` when layout rhythm or responsive behavior is clearer in code than in design artifacts.
- Use `penpot`, `tokens_studio`, or `supernova` when spatial primitives are authored or distributed there.
- Use `paper, repository` when only static references exist.
- If all strong paths fail, provide the best-guess output and label it `inferred`.

## Workflow Notes

- Optimize for spatial rules that survive real product composition, not perfect gallery layouts.
- Separate component-internal spacing from page-composition spacing so the scale does not become a dumping ground.
- Document where the scale is normative and where it is advisory.
- Keep the scale connected to component structure and breakpoint behavior.
- Prefer a smaller number of durable semantic roles over a long list of rarely used numeric steps.

## Prioritization Logic

- Highest priority: spacing failures that break layout rhythm across many surfaces or cause recurring responsive bugs.
- Medium priority: inconsistent semantic usage that slows teams or creates near-duplicate layout utilities.
- Lower priority: isolated spacing blemishes that do not materially affect composition or implementation reuse.

