---
name: component-governance
description: Model component ownership, lifecycle states, decision rights, and contribution workflows before defining governance rules for change, variants, and deprecation.
trigger: When system growth needs operating rules, ownership clarity, or lifecycle control instead of relying on informal habits and tribal knowledge.
analysis_framework: Governance design with actor mapping, lifecycle modeling, decision-right analysis, and policy prioritization
primary_mcp: notion, figma
fallback_tools:
  - repository
  - reference/reuse
required_inputs:
  - current component contribution behavior or stated process
  - current design-system ownership model or closest proxy
  - `project-ds-spec.md` when it exists
  - any existing documentation, RFC process, review path, or release cadence
recommended_passes:
  - actor and decision-right inventory
  - lifecycle-state model construction
  - contribution and review flow analysis
  - variant and exception policy analysis
  - deprecation and migration analysis
tool_stack:
  workspace:
    primary: [notion, figma, repository]
    secondary: [reference/reuse]
  governance_platforms:
    primary: [zeroheight, supernova]
    secondary: [paper]
  implementation_truth:
    primary: [storybook, github]
    secondary: [repository]
  fallback:
    primary: [repository, reference/reuse]
tool_routing:
  - if: process and ownership evidence lives in workspace docs or tickets
    use: [notion, repository]
  - if: governance status or component readiness is maintained in zeroheight or Supernova
    use: [zeroheight, supernova]
  - if: real contribution and change evidence is clearest from code review or release surfaces
    use: [github, storybook, repository]
  - if: only static docs or partial notes exist
    use: [reference/reuse, repository]
best_guess_output: A governance model covering ownership, contribution, variants, exceptions, deprecation, and the minimum process needed to keep the library healthy.
output_artifacts:
  - knowledge/design-systems-designer-component-governance.md
  - knowledge/assets/ (for visual artifacts)
done_when: Teams can explain who decides, who reviews, which lifecycle state a component is in, and how components are introduced, changed, or removed without informal side channels.
---

# Component Governance

## Purpose

Define the operating system that lets a component library grow without becoming unowned or inconsistent.

This skill applies actor mapping, lifecycle-state modeling, and decision-right analysis to turn informal habits into reusable governance rules.

This skill does not write governance as brand voice, invent bureaucracy without evidence, or confuse documentation polish with actual operating clarity.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` when governance evidence lives in zeroheight, Supernova, Storybook, or other specialist systems instead of only in workspace docs.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-systems-designer-component-governance.md`).
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

- Require current ownership signals, contribution behavior, release or review habits, and `project-ds-spec.md` when it exists.
- Prefer observed process evidence over “how we usually do it” language.
- If team boundaries or review authority are unclear, infer the minimum viable operating model and prefix it with `Assumed context:`.

## Input Mode And Evidence Path

- Prefer actual process artifacts such as docs, review flows, issue history, or status tables over policy aspirations.
- Use component-status platforms when they provide stronger lifecycle evidence than static docs.
- State which governance rules are evidence-backed and which are proposed because process evidence was missing.

## Environment And Reproducibility

- Record the org or team surface inspected, current release or review cadence when known, and any missing stakeholders or tools that limit certainty.
- Capture whether governance must cover one product team or multiple product teams and platforms.
- Note whether lifecycle status is already tracked anywhere.

## Model Building

Build the governance model before findings:

- Actors: design-system owner, design reviewer, engineering owner, adopters, release approvers
- Lifecycle states: proposed, experimental, stable, deprecated, sunset, or equivalent
- Decision rights: who can add, change, split, merge, or retire components
- Operating artifacts: docs, RFCs, review queues, status tables, and migration announcements

## Required Deliverable Sections

Within `## Skill: component-governance`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Governance objective`
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Governance model`: Describe actors, lifecycle states, and decision rights.
- `### Governance passes`
- `### Ownership model`: Define who owns design, code, and release decisions for shared components.
- `### Contribution flow`: Describe how new components or changes are proposed and reviewed.
- `### Variant rules`: Set the rules for when to add, split, or reject variants.
- `### Deprecation policy`: Explain how components are sunset and migrated safely.
- `### Exception handling`: Document how urgent or one-off exceptions are approved and tracked.
- `### Governance findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized governance risks`: Highlight the process failures most likely to create system drift.
- `### Systemic patterns`: Group recurring ownership ambiguity, untracked variants, exception creep, or undocumented deprecation.
- `### Recommendations`
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `notion, figma`.
- Use `repository`, `github`, or `storybook` when real change behavior is clearer from implementation and review traces than from documentation.
- Use `zeroheight` or `supernova` when lifecycle status and docs workflows are maintained there.
- Use `reference/reuse, repository` when strong process evidence is unavailable.
- If strong paths fail, provide the best-guess output and mark the evidence level accurately.

## Workflow Notes

- Write governance as rules teams can actually follow under delivery pressure.
- Make ownership boundaries between design and engineering explicit.
- Prefer a small number of durable lifecycle states over elaborate workflow theater.
- Separate policy needed for shared components from policy needed only for one product team.
- Treat `project-ds-spec.md` as the canonical governance handoff into the product’s DS folder.

## Prioritization Logic

- Highest priority: governance gaps that allow uncontrolled component drift, unowned changes, or unsafe deprecations.
- Medium priority: unclear review flow or variant policy that causes repeated arguments and duplicate work.
- Lower priority: documentation polish issues that do not materially change who decides or how lifecycle changes happen.

