---
name: system-audit
description: Build a design-system health model from design, code, documentation, and adoption evidence before diagnosing drift, duplication, governance gaps, and next actions.
trigger: When the system needs a baseline before extension, migration, or cleanup and the team needs evidence-backed priorities instead of design-system opinions.
analysis_framework: Design-system audit with inventory modeling, drift analysis, duplication tracing, adoption-risk assessment, and prioritized remediation
primary_mcp: figma, repository
fallback_tools:
  - paper
  - reference/ground
required_inputs:
  - active project context and current design-system goal
  - live or documented design-system surfaces such as Figma files, repository packages, Storybook, or docs
  - current `project-ds-spec.md` when it exists
  - known product surfaces, brands, or themes in scope
recommended_passes:
  - surface inventory
  - system model construction
  - design versus code parity check
  - duplication and drift analysis
  - governance and adoption risk analysis
  - remediation prioritization
tool_stack:
  workspace:
    primary: [figma, repository]
    secondary: [paper]
  documentation:
    primary: [zeroheight, supernova, notion]
    secondary: [paper]
  code_truth:
    primary: [storybook, chromatic]
    secondary: [repository, chrome_devtools]
  fallback:
    primary: [reference/ground, paper, chrome_devtools_take_screenshot, lighthouse_audit]
tool_routing:
  - if: live design files and code artifacts are both accessible
    use: [figma, repository]
  - if: component docs, status tables, or system documentation are better maintained in a platform such as zeroheight or Supernova
    use: [zeroheight, supernova]
  - if: the most trustworthy implementation evidence lives in isolated component docs or visual baselines
    use: [storybook, chromatic]
  - if: only static exports, notes, or partial docs exist
    use: [paper, reference/ground]
best_guess_output: A design-system audit with explicit scope, findings, systemic patterns, confidence-tagged priorities, and the minimum next moves needed to stabilize the system.
output_artifacts:
  - knowledge/design-systems-designer-system-audit.md
  - knowledge/assets/ (for visual artifacts)
done_when: The team can point to the audited surfaces, understand the highest-risk drift and duplication patterns, and act on a prioritized remediation sequence without re-running discovery.
---

# System Audit

## Purpose

Build an evidence-backed view of current design-system health before recommending cleanup, investment, or governance changes.

This skill applies inventory modeling, parity tracing, and adoption-risk analysis to distinguish cosmetic inconsistency from structural system failure.

This skill does not treat aspiration docs as proof, collapse multiple issues into vague “inconsistency” language, or prescribe a redesign before the system model exists.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` when the assignment mentions zeroheight, Supernova, Storybook, Chromatic, Penpot, Tokens Studio, Specify, or other external system tooling.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-systems-designer-system-audit.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/assets/`. 
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths.
  - For `take_screenshot`, you MUST supply the `filePath` parameter pointing directly to the destination in the project workspace.
  - For `generate_image`, or tools that save to your `.gemini`/`.antigravity` brain directory or `/tmp`, you MUST use bash to manually move the image file into the project directory.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths or paths outside the workspace.

## Required Inputs And Assumptions

- Require the assignment contract, `logs/active/<project-slug>/context.md`, the current repo surface, and `project-ds-spec.md` when it exists.
- Prefer real design, code, and documentation surfaces over summaries about those surfaces.
- If scope, brands, themes, or adoption surfaces are missing, infer the minimum audit boundary and prefix it with `Assumed context:`.

## Input Mode And Evidence Path

- Prefer evidence in this order: live product or design-system surface, structured repo or tooling access, design-system documentation, static exports, then inference.
- Name the strongest evidence path used and state which surfaces remained documentation-only.
- When Storybook or Chromatic exist, use them as implementation truth for state coverage and regression history instead of assuming Figma parity.

## Environment And Reproducibility

- Record the repo branch or snapshot, relevant design workspace or file, theme or brand scope, and any permissions or missing tools that limited the audit.
- Capture whether the audit covered one product, one library, or a multi-surface system.
- If versions or access state are unknown, write `Unknown at time of analysis`.

## Model Building

Build the audit model before findings:

- System surfaces: foundations, components, patterns, docs, and implementation packages
- Evidence anchors: where each surface is proven in design, code, and documentation
- Ownership boundaries: who appears to own tokens, components, docs, and release behavior
- Adoption surfaces: where teams consume the system and where they bypass it

## Required Deliverable Sections

Within `## Skill: system-audit`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Audit objective`: State why the audit is being run and what downstream decision it must support.
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Audit model`: Summarize the system surfaces, evidence anchors, and ownership boundaries you built before analysis.
- `### Audit passes`: List the passes used.
- `### Audit scope`: State which products, libraries, files, themes, or surfaces were audited.
- `### Findings table`: Summarize the major findings with severity, affected surfaces, and confidence.
- `### Project ds-spec alignment`: State where the current system aligns with or drifts from `project-ds-spec.md`.
- `### Duplication and drift`: Call out redundant patterns and design/code divergence.
- `### Adoption risks`: Explain what makes the system hard to use or trust today.
- `### Audit findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized remediation sequence`: Order the fixes by system leverage, blast radius, and reversibility.
- `### Systemic patterns`: Group recurring issues such as token sprawl, variant drift, undocumented exceptions, or code-first bypasses.
- `### Recommendations`: Tie each recommendation to one or more findings or patterns.
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `figma, repository`.
- Use `chrome_devtools` when auditing a live implementation for token correctness, computed styles, or accessibility compliance.
- Use `zeroheight` or `supernova` when documentation status, component status, or system metadata is better maintained there than in the repo.
- Use `storybook` or `chromatic` when isolated implementation states or regression evidence materially improve confidence.
- Use `paper` or `reference/ground` only when live surfaces are missing or blocked.
- If all strong paths fail, produce the best-guess output and clearly mark it `inferred`.

## Workflow Notes

- Build the system model before judging health.
- Trace at least one evidence anchor for every major foundation or component family included in a critical finding.
- Separate surface inconsistency from structural issues like missing ownership, broken token semantics, or undocumented variant sprawl.
- Use `project-ds-spec.md` as the primary benchmark and external tooling norms only as enrichment.
- Consolidate repeated low-impact issues into patterns before prioritization.

## Prioritization Logic

- Highest priority: system failures that create broad inconsistency, broken adoption, or expensive design/code divergence.
- Medium priority: duplicated primitives, overlapping component families, or documentation gaps that slow teams repeatedly.
- Lower priority: cosmetic inconsistencies that do not materially change user experience, code reuse, or trust in the system.

