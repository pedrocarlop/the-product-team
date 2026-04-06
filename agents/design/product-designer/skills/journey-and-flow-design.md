name: journey-and-flow-design
description: Map the end-to-end journey by building an experience model of actors, entry points, states, branches, and operational dependencies before defining screens or polished UI.
trigger: When a feature, service, or multi-step task needs clear behavioral structure before wireframes, prototyping, or implementation.
mesh:
  inputs:
    - ux-researcher:research-synthesis
    - product-lead:write-prd
  next:
    - product-designer:wireframe-structure
  context: "Defines the behavioral skeleton of the experience before structural design."
analysis_framework: journey mapping and task-flow modeling with service-blueprint thinking for cross-channel dependencies
primary_mcp: figma
fallback_tools:
  - paper
  - notion
required_inputs:
  - target user or actor
  - trigger or entry point into the experience
  - target job or intended outcome
  - known policies, dependencies, or constraints
  - current-state artifacts or prior framing when known
recommended_passes:
  - experience model construction
  - happy-path mapping
  - alternate and failure-path mapping
  - decision-point and rule mapping
  - dependency and edge-case review
tool_stack:
  design_mapping:
    primary: [figma, figjam]
    secondary: [miro, whimsical]
  validation:
    primary: [maze, lyssna]
    secondary: [optimal_workshop]
  documentation:
    primary: [notion]
  fallback:
    primary: [paper, notion]
tool_routing:
  - if: flows must be authored or updated in the primary design workspace
    use: [figma, figjam]
  - if: branching logic, workshops, or collaborative mapping matter more than frame fidelity
    use: [miro, whimsical]
  - if: click-through path validation is possible on prototypes
    use: [maze]
  - if: information architecture or route findability needs lightweight validation
    use: [lyssna, optimal_workshop]
  - if: only narrative or static documentation exists
    use: [notion, paper]
best_guess_output: A journey map or flow artifact with entry points, primary and alternate paths, decision points, service dependencies, and explicit edge-case coverage.
output_artifacts:
  - knowledge/runs/<run-id>/product-designer-journey-and-flow-design.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: The main path, critical branches, decision points, and operational dependencies are explicit enough that downstream structure and interaction work does not have to infer route logic.
mesh:
  inputs:
    - product-designer:problem-framing # The journey maps the specific problem/job defined in the frame
    - product-lead:write-prd # Ensures the journey aligns with the functional requirements
  next:
    - product-designer:wireframe-structure
    - ui-designer:ui-concept-direction
  context: "Journey mapping translates a bounded problem into a sequence of steps and decision points, providing the backbone for structural wireframes."
---

# Journey And Flow Design

## Purpose

Map the end-to-end journey by building an experience model of actors, entry points, states, branches, and service dependencies before screen-level design begins.

This skill applies task-flow reasoning, journey mapping, and service-blueprint thinking to make route logic explicit.

This skill does not optimize visual styling, assume the happy path is enough, or hide unresolved branches behind generic flow diagrams.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/product-designer-journey-and-flow-design.md`).
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

## Required Deliverable Sections

Within `## Skill: journey-and-flow-design`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Flow objective`: Define the experience or service being mapped and what downstream decision this flow definition must support.
- `### Required inputs and assumptions`: State the known actors, entry points, outcomes, constraints, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live runtime or current journey evidence, structured design artifacts, collaborative mapping artifacts, static screenshots or docs, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record platform, channel, auth state, data setup, prototype version, and relevant policy assumptions when known.
- `### Experience model`: Build the actor -> trigger -> goal -> step -> state -> decision -> dependency model before evaluating path quality.
- `### Flow passes`: List the passes used such as experience model construction, happy-path mapping, alternate and failure-path mapping, decision-point and rule mapping, and dependency and edge-case review.
- `### Entry points and preconditions`: Describe where the journey starts, what context the actor brings, and what must already be true.
- `### Main path`: Document the primary path in sequence with step, user action, system response, and resulting state.
- `### Alternate, failure, and recovery paths`: Capture meaningful branches, breakdowns, detours, and recovery loops.
- `### Decision points and rules`: State where user choice, business rules, or system conditions change the route.
- `### State and dependency inventory`: List the critical states, integrations, approvals, or support processes that influence the flow.
- `### Flow findings`: Record findings using the required finding schema below.
- `### Prioritized flow risks`: Include all major ambiguities or breakpoints as standalone findings and group lower-risk issues into patterns.
- `### Systemic flow patterns`: Group recurring issues such as broken loops, hidden dependencies, dead-end branches, or policy-driven complexity.
- `### Recommendations`: Offer directional changes to simplify, clarify, or validate the flow without pretending the screen solution is already done.
- `### Coverage map`: State which routes were deeply mapped, partially mapped, and not mapped.
- `### Limits and unknowns`: Explain what still needs validation with users, operations, or technical owners.

For each finding inside `### Flow findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Trigger:
- Path or branch:
- Breakdown or ambiguity:
- Impact:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest evidence path available: live journey evidence -> structured design artifacts -> collaborative mapping -> static docs -> inference.
- Start with `figma` when the canonical flow or adjacent design context already lives in the design workspace.
- Use `figjam` when the flow needs collaborative branching, sequencing, or workshop-style synthesis before frame production.
- Use `miro` or `whimsical` when the strongest artifact is a broad map, workshop board, or quick branching diagram rather than a canonical design file.
- Use `maze` when click-through validation of a proposed route is possible and the team needs fast path evidence.
- Use `lyssna` or `optimal_workshop` when route findability, labeling, or information architecture needs lightweight validation.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, notion`.
- If both paths fail, produce the best-guess output described as: A journey map or flow artifact with entry points, primary and alternate paths, decision points, service dependencies, and explicit edge-case coverage.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single mapping surface.

## Workflow Notes

- Build the experience model first. Do not start with boxes and arrows detached from user goals and operating conditions.
- Treat `required_inputs` as real prerequisites. If the actor, trigger, or outcome is missing, infer a provisional set, prefix each inferred item with `Assumed path context:`, and lower confidence for downstream findings that depend on it.
- Map the happy path first, then actively look for alternate paths, failure paths, and recovery loops.
- Keep system rules and policy constraints visible. Many critical route branches are caused by business logic, permissions, and fulfillment dependencies rather than user choice alone.
- Separate observed path evidence from inferred causes and from recommendation direction.
- Prefer explicit state language over vague journey prose.
- If the flow crosses teams or systems, note the handoff moments where ownership changes and latent failure risk increases.
- After all passes, consolidate repeated issues into systemic patterns before prioritization.

