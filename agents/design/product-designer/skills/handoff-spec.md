---
name: handoff-spec
description: Produce a delivery-ready handoff by tracing the approved problem frame, flow, structure, states, content, and dependencies into explicit downstream contracts for design, content, and engineering.
trigger: When discovery, flow, or prototype work is ready to be handed to downstream UI, content, and engineering roles.
analysis_framework: delivery traceability and state-complete handoff contract
primary_mcp: notion, figma
fallback_tools:
  - paper
  - reference/verify
required_inputs:
  - approved problem frame or objective
  - flow, screen, or prototype artifacts
  - downstream consumers and expected deliverables
  - known dependencies, constraints, or launch context
recommended_passes:
  - source artifact inventory
  - downstream contract mapping
  - state and dependency completeness review
  - ambiguity and blocker isolation
  - handoff packaging
tool_stack:
  handoff_sources:
    primary: [notion, figma]
    secondary: [zeplin, axure]
  documentation:
    primary: [reference/verify]
    secondary: [uxpin, protopie]
  fallback:
    primary: [paper, reference/verify]
tool_routing:
  - if: source designs, flows, and annotations are accessible
    use: [figma, notion]
  - if: engineering handoff needs inspect views, redlines, or spec-oriented annotations outside the primary design file
    use: [zeplin, axure]
  - if: code-backed components or implementation-ready specs already exist alongside the design system
    use: [uxpin]
  - if: interaction recordings or rich prototype annotations are the clearest behavior source
    use: [protopie]
  - if: only lightweight notes or linked references remain
    use: [paper, reference/verify]
best_guess_output: A handoff spec linking flow, structure, behavior, open questions, and downstream ownership with clearly labeled evidence limits.
output_artifacts:
  - knowledge/runs/<run-id>/product-designer-handoff-spec.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: A downstream role can continue without reopening the design problem, behavior rules, or missing-state questions.
---

# Handoff Spec

## Purpose

Translate design work into a downstream delivery contract that preserves intent, coverage, and dependencies.

This skill applies delivery traceability so the approved problem frame, flow, structure, behavior, content, and open questions are explicit enough for downstream roles to continue without rediscovery.

This skill does not replace implementation planning, engineering estimation, or final acceptance criteria owned by downstream roles.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/product-designer-handoff-spec.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/runs/<run-id>/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

## Required Deliverable Sections

Within `## Skill: handoff-spec`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Handoff framing`: Define what is being handed off, to whom, and what downstream work this package is expected to unlock.
- `### Required inputs and assumptions`: State the known source artifacts, maturity level, dependencies, and inferred assumptions required to package the handoff.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live interaction, structured system access, design or documentation artifacts, screenshots or static input, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record platform, build or prototype version, design file references, component library version, and artifact dates when known.
- `### Source-of-truth model`: Name the exact problem frame, flow, wireframe, prototype, annotations, and other artifacts treated as canonical.
- `### Assignment type and maturity`: Classify the work as `new design` or `extension of existing pattern`, and note whether it is framing-ready, flow-ready, prototype-ready, or implementation-ready.
- `### Experience summary`: Summarize the user job, flow, intended outcome, and the critical constraints downstream teams must preserve.
- `### Flow and screen inventory`: List the screens, states, transitions, and flow stages that downstream teams must preserve.
- `### State, edge-case, and dependency inventory`: Call out loading, empty, error, permission, and external-system dependencies that affect implementation or content.
- `### Downstream contract matrix`: Separate what UI, content, and engineering each need to deliver, decide, or verify.
- `### Exploration prerequisites`: For `new design`, point to the exploration, comparison, or validation work required before concrete UI production should be treated as final.
- `### Handoff gaps and ambiguities`: Record the highest-signal missing contracts or unresolved ambiguities using the required finding schema below.
- `### Prioritized handoff blockers`: Include all build-blocking or review-blocking issues as standalone findings, group lower-impact gaps into patterns, and prefer no more than 12 standalone findings by default unless more are materially distinct.
- `### Systemic delivery patterns`: Group recurring gaps such as missing state coverage, unclear ownership, weak content dependency mapping, or behavior ambiguity.
- `### Open questions and explicit follow-ups`: List unresolved decisions, owners, and the expected next action when known.
- `### Coverage map`: State what was fully handed off, partially handed off, and not yet handed off.
- `### Limits and unknowns`: Explain what could not be packaged confidently and what still requires downstream rediscovery or validation.

For each finding inside `### Handoff gaps and ambiguities`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Downstream consumer:
- Missing or ambiguous contract:
- Delivery risk:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest evidence path available: live interaction -> structured systems -> design or documentation artifacts -> screenshots or static inputs -> inference.
- Start with `notion, figma` when source decisions, flows, and annotated designs are accessible.
- Use `zeplin` or `axure` when inspect views, spec-oriented annotations, or developer-facing handoff detail are the clearest delivery layer.
- Use `uxpin` when code-backed components or implementation-oriented specs are already part of the source of truth.
- Use `protopie` when the clearest behavior evidence lives in rich interaction prototypes or recordings.
- Use `reference/verify` when linked artifacts, existing docs, or implementation references are the strongest remaining evidence.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/verify`.
- If both paths fail, produce the best-guess output described as: A handoff spec linking flow, structure, behavior, open questions, and downstream ownership with clearly labeled evidence limits.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Use named external tools only when they are connected or explicitly available in the environment.

## Workflow Notes

- Build the source-of-truth model first. Do not jump straight to a handoff checklist without confirming what artifacts are canonical.
- Treat `required_inputs` as real prerequisites. If the source artifacts, ownership model, or maturity level is missing, infer a provisional set, prefix each inferred item with `Assumed handoff input:`, and lower confidence for dependent findings.
- Start by inventorying source artifacts, then map downstream contracts, then check state and dependency completeness, then isolate blockers and open questions.
- Preserve edge cases, dependencies, and non-obvious behavior. Handoffs fail when compressed summaries drop the hard parts.
- Separate what is decided from what is still open. Downstream teams need to know what is safe to implement and what still needs confirmation.
- Distinguish clearly between observed source evidence, inferred gap, and recommendation direction.
- Group minor ambiguities into patterns when they point to the same delivery weakness.
- When the assignment is `new design`, explicitly protect room for downstream exploration instead of packaging exploratory work as settled UI.

