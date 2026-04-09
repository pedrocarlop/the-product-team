---
name: token-architecture
description: Construct a token-system model across primitives, semantics, themes, and code-delivery constraints before defining naming, aliasing, and migration rules.
trigger: When the system needs a durable token foundation, cross-platform alignment, or a cleaner bridge between design authoring and implementation.
analysis_framework: DTCG-aligned token architecture with source-of-truth analysis, semantic layering, theme modeling, and delivery-path validation
primary_mcp: figma
fallback_tools:
  - paper
  - repository
required_inputs:
  - current token sources or style sources in design and code
  - `project-ds-spec.md` when it exists
  - known themes, brands, platforms, or modes
  - current implementation posture such as CSS variables, Tailwind, design-token JSON, or platform exports
recommended_passes:
  - source-of-truth inventory
  - token model construction
  - naming and alias analysis
  - theme and mode analysis
  - code-delivery compatibility check
  - migration sequencing
tool_stack:
  workspace:
    primary: [figma, repository]
    secondary: [paper]
  token_platforms:
    primary: [tokens_studio, penpot, supernova, specify]
    secondary: [style_dictionary]
  interoperability:
    primary: [dtcg, style_dictionary]
  fallback:
    primary: [paper, repository]
tool_routing:
  - if: token truth lives in Figma variables, styles, or Tokens Studio exports
    use: [figma, tokens_studio]
  - if: token truth or documentation lives in Penpot, Supernova, or Specify
    use: [penpot, supernova, specify]
  - if: the assignment needs interoperable token output or platform delivery rules
    use: [dtcg, style_dictionary]
  - if: code implementation details are clearer in the repo than in design tools
    use: [repository]
  - if: only static files or notes exist
    use: [paper, repository]
best_guess_output: A token architecture proposal with explicit token layers, naming rules, semantic aliases, theme logic, code-delivery implications, and migration guidance.
output_artifacts:
  - knowledge/design-systems-designer-token-architecture.md
  - knowledge/assets/ (for visual artifacts)
done_when: Token layers, naming, aliasing, theme handling, and code-delivery constraints are explicit enough that new token work can scale without inventing a parallel system.
---

# Token Architecture

## Purpose

Define a durable token architecture that can survive real theming, cross-platform delivery, and design-to-code translation.

This skill applies a DTCG-aligned token modeling method: inventory sources, define layers, resolve semantics, validate delivery constraints, and only then recommend naming or migration rules.

This skill does not rename tokens for cosmetic reasons, invent layers that the team cannot operate, or confuse documentation structure with token architecture.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` for the current token-tool landscape, especially DTCG, Style Dictionary, Tokens Studio, Penpot, Supernova, and Specify.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-systems-designer-token-architecture.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

## Required Inputs And Assumptions

- Require the assignment contract, `logs/active/<project-slug>/context.md`, token or style sources, and `project-ds-spec.md` when available.
- Require known theme, brand, density, locale, or platform splits when they materially change token structure.
- If token sources are incomplete, infer the minimum architecture needed and mark each inference with `Assumed context:`.

## Input Mode And Evidence Path

- Prefer live token sources, token JSON, variable collections, or repo exports before prose documentation.
- When the project uses Tokens Studio, Penpot, Supernova, or Specify, use those outputs as evidence for real token structure instead of flattening everything into generic “design styles.”
- State whether the code-delivery layer was validated from actual exports, config files, or only inferred from repo conventions.

## Environment And Reproducibility

- Record which token sources were inspected, which theme or brand dimensions were covered, and which code target formats were validated.
- Capture whether the architecture must fit web-only delivery or multi-platform output.
- Note any gaps such as missing token exports, hidden Figma collections, or undocumented theme modes.

## Model Building

Build the token model before findings:

- Source layers: raw values, semantic aliases, component-facing tokens, and runtime variables
- Theme dimensions: brand, mode, density, platform, or locale
- Delivery targets: CSS variables, Tailwind theme objects, JSON, native exports, or generated packages
- Ownership split: where designers author, where code transforms, and where runtime consumes

## Required Deliverable Sections

Within `## Skill: token-architecture`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Token objective`
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Token model`: Describe source layers, theme dimensions, delivery targets, and ownership boundaries.
- `### Architecture passes`
- `### Token layers`: Define the token stack such as raw, semantic, and component-level tokens.
- `### Naming conventions`: Document how tokens are named and grouped.
- `### Semantic aliases`: Explain how semantic tokens map to raw primitives.
- `### Theme and mode strategy`: Explain how brands, modes, density, or platform variations are represented.
- `### Cross-platform mapping`: Note constraints or naming differences that affect implementation.
- `### Project ds-spec translation`: Explain how the project direction becomes an operational token model.
- `### Migration notes`: Describe how existing tokens or styles should normalize into the new model.
- `### Token findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized token risks`: Separate critical architecture risks from transitional cleanup.
- `### Systemic patterns`: Group recurring issues such as semantic leakage, alias overuse, theme collisions, or code-delivery mismatch.
- `### Recommendations`
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `figma`.
- Use `tokens_studio` when token authoring or import/export logic clearly lives there.
- Use `penpot`, `supernova`, or `specify` when those systems are the clearest source for token truth, distribution, or metadata.
- Use `dtcg` and `style_dictionary` as architecture anchors when interoperability or export rules matter.
- Use `repository` to validate real delivery constraints and runtime naming.
- If the strong paths fail, use `paper, repository` and mark the output `fallback` or `inferred`.

## Workflow Notes

- Anchor interoperability to DTCG terminology whenever possible.
- Validate whether the project needs raw tokens, semantic tokens, and component tokens, or whether one of those layers is currently unnecessary overhead.
- Keep token layers shallow enough that designers and engineers can reason about them.
- Do not treat shadcn/ui, Tailwind, or any implementation system as a replacement for token architecture; treat them as delivery constraints.
- If `project-ds-spec.md` recommends shadcn/ui, explicitly map the token posture to CSS variables and theme structure rather than inventing a competing language.

## Prioritization Logic

- Highest priority: architecture flaws that break theming, alias clarity, or cross-platform delivery.
- Medium priority: naming collisions, redundant token families, or weak semantic separation that slow teams down but do not yet break output.
- Lower priority: cosmetic naming cleanup without material system impact.

