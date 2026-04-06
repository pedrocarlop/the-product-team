---
name: system-qa-and-adoption
description: Build an operational model of verification surfaces, adoption audiences, and rollout dependencies before defining QA checks, blockers, and adoption guidance.
trigger: When the design system exists but consistency is untrusted, rollout is stalling, or the team needs a repeatable way to verify and adopt the system.
analysis_framework: Design-system operational QA with surface verification, adoption-blocker analysis, rollout planning, and exit-criteria definition
primary_mcp: repository, figma
fallback_tools:
  - chrome_devtools
  - reference/verify
required_inputs:
  - current implementation surfaces and adoption targets
  - current design-system docs or `project-ds-spec.md`
  - known rollout goals, constraints, or adoption complaints
  - available verification tools such as Storybook, Chromatic, browser inspection, or runtime QA
recommended_passes:
  - verification-surface inventory
  - adoption-audience model construction
  - QA check design
  - blocker and readiness analysis
  - rollout and exit-criteria definition
tool_stack:
  workspace:
    primary: [repository, figma]
    secondary: [chrome_devtools, reference/verify]
  implementation_truth:
    primary: [storybook, chromatic, chrome_devtools]
    secondary: [repository]
  documentation:
    primary: [zeroheight, supernova, notion]
    secondary: [paper]
  fallback:
    primary: [chrome_devtools, reference/verify]
tool_routing:
  - if: implementation and docs are accessible in repo and design files
    use: [repository, figma]
  - if: isolated component states or visual baselines are the best QA evidence
    use: [storybook, chromatic]
  - if: live browser verification is needed to confirm adoption or consistency issues
    use: [chrome_devtools]
  - if: adoption status, docs, or rollout metadata live in zeroheight or Supernova
    use: [zeroheight, supernova]
  - if: only static notes or partial screenshots exist
    use: [reference/verify]
best_guess_output: A system QA and adoption plan with verification checks, blocker analysis, rollout guidance, exit criteria, and clear confidence limits.
output_artifacts:
  - knowledge/runs/<run-id>/design-systems-designer-system-qa-and-adoption.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: Teams have a repeatable verification method, can see the highest adoption blockers, and know what must be true before the system rollout is considered operationally healthy.
---

# System QA And Adoption

## Purpose

Define how the system should be verified in practice and what must change for teams to adopt it reliably.

This skill applies an operational method: inventory verification surfaces, model target adopters, analyze blockers, and define rollout and exit criteria grounded in evidence.

This skill does not reduce adoption to “communicate better,” or reduce QA to a vague checklist without clear surfaces and evidence paths.

Read `../references/shared-method.md` for the shared deliverable contract, finding schema, evidence rules, and coverage requirements.

Read `../references/tooling-landscape.md` when Storybook, Chromatic, zeroheight, Supernova, or browser/runtime tools provide stronger verification evidence than static docs.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-systems-designer-system-qa-and-adoption.md`).
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

- Require current design-system surfaces, target adopters, known complaints or friction, and `project-ds-spec.md` when it exists.
- Prefer evidence from real verification surfaces and real adoption behavior over aspirational rollout plans.
- If the target adoption audience or rollout state is unclear, infer the smallest viable audience and mark it `Assumed context:`.

## Input Mode And Evidence Path

- Prefer implementation truth and live verification evidence first, then structured docs, then static artifacts, then inference.
- Use Storybook or Chromatic when the strongest QA evidence is component-state coverage or visual regression history.
- Use browser inspection when runtime behavior, real pages, or rollout surfaces need confirmation.
- State what was verified in live/runtime conditions versus what was only documented.

## Environment And Reproducibility

- Record the verification surfaces inspected, adoption audiences considered, environment or theme assumptions, and any missing runtime access.
- Capture whether the rollout covers one team, multiple teams, or multiple products.
- Note any blocked checks caused by auth, setup, or missing testable environments.

## Model Building

Build the operational model before findings:

- Verification surfaces: component stories, live screens, docs, tokens, and runtime UI states
- Adoption audiences: designers, engineers, PMs, QA, content, or adjacent teams
- Rollout dependencies: docs completeness, migration effort, tooling access, and ownership support
- Exit state: what “healthy adoption” actually means for this system

## Required Deliverable Sections

Within `## Skill: system-qa-and-adoption`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### QA and adoption objective`
- `### Required inputs and assumptions`
- `### Input mode and evidence path`
- `### Tool selection rationale`
- `### Environment and reproducibility`
- `### Operational model`: Describe the verification surfaces, adoption audiences, rollout dependencies, and target exit state.
- `### QA and adoption passes`
- `### QA checklist`: Define the checks used to verify system consistency.
- `### Adoption blockers`: List what prevents teams from using the system cleanly today.
- `### Rollout guidance`: Describe how teams should adopt or re-adopt the system.
- `### Verification method`: Explain how future QA should be run and evidenced.
- `### Exit criteria`: State what must be true before the adoption push is considered complete.
- `### QA and adoption findings`: Use the exact finding template from `../references/shared-method.md`.
- `### Prioritized blockers`: Highlight the blockers with the highest operational cost or adoption drag.
- `### Systemic patterns`: Group recurring issues such as docs discoverability gaps, brittle runtime parity, or unclear migration ownership.
- `### Recommendations`
- `### Coverage map`
- `### Limits and unknowns`

## Tool Path

- Start with `repository, figma`.
- Use `storybook` or `chromatic` when component-state QA and visual regression evidence are strongest.
- Use `chrome_devtools` when live browser verification is needed.
- Use `zeroheight`, `supernova`, or `notion` when rollout status and documentation maturity are better maintained there.
- Use `reference/verify` when only static evidence exists.
- If strong paths fail, produce the best-guess output and mark it with the correct evidence label.

## Workflow Notes

- Treat adoption as an operational systems problem, not only a design-quality problem.
- Tie every QA check to a specific surface and expected evidence.
- Make the rollout path realistic for teams with existing commitments.
- Use `project-ds-spec.md` as the canonical adoption artifact teams should consume before implementation details.
- Separate verification gaps from change-management gaps so recommendations stay actionable.

## Prioritization Logic

- Highest priority: blockers that make the system unsafe to trust or too costly to adopt.
- Medium priority: documentation and workflow gaps that repeatedly slow adoption or create avoidable QA churn.
- Lower priority: improvements that help clarity but do not materially change rollout readiness or verification confidence.

