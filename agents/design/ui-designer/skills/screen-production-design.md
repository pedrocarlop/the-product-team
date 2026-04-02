---
name: screen-production-design
description: Converge an approved UI direction into implementation-ready screens by locking hierarchy, layout, tokens, states, and any required `project-ds-spec.md` deltas.
trigger: When a concept must become a production-ready design.
primary_mcp: figma
fallback_tools: paper, stitch
best_guess_output: A production-ready screen spec or screen set with handoff notes and required `project-ds-spec.md` updates.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
section_anchor: "## Skill: screen-production-design"
done_when: Layout, hierarchy, tokens, and core states are specified clearly.
required_inputs:
  - upstream direction or winning variant section
  - target surface, route, or screen set
  - known breakpoints and state scope, or a note that they are unknown
  - current `project-ds-spec.md` when one exists
recommended_passes:
  - source inheritance check
  - screen inventory and hierarchy lock
  - layout and token lock
  - responsive and state sweep
  - handoff and spec delta review
tool_stack:
  runtime:
    primary: [figma]
    secondary: [stitch, v0, framer]
  artifacts:
    primary: [project-ds-spec.md, reference-design-systems, paper]
    secondary: [penpot, storybook]
  fallback:
    primary: [open]
    secondary: [playwright]
tool_routing:
  - if: canonical direction exists in Figma or Stitch
    use: [figma]
  - if: production-shaped iteration is needed against a live preview or prompt-first mock
    use: [v0, framer]
  - if: reusable component libraries and inspectable variants matter most
    use: [penpot]
  - if: handoff needs component-level visual verification or regression checks
    use: [storybook, playwright]
  - if: only static artifacts or annotations exist
    use: [paper, open]
---

# Screen Production Design

## Purpose

Converge an approved direction into implementation-ready screens, states, and system deltas.

This skill turns a selected concept or winning variant into the definitive screen design for build.

It does not explore new concepts, conduct broad usability review, or redefine the product strategy.

## Required Inputs and Assumptions

- Required inputs
  - An upstream direction from `ui-concept-direction` or a winning variant from `ui-variant-exploration`
  - The target surface, route, or screen set
  - Any known breakpoint or state requirements
  - The current `project-ds-spec.md` when a shared system artifact already exists
- Known vs unknown
  - Known: the design direction that should be preserved, the screen(s) in scope, and any required handoff constraints
  - Unknown: precise state coverage, implementation foundation, and whether the system spec needs changes
- Assumptions when inputs are missing
  - If the upstream direction is missing, infer the latest approved concept and label that assumption clearly
  - If breakpoints are missing, assume desktop and mobile at minimum, plus tablet when layout density makes it relevant
  - If state scope is missing, assume empty, loading, error, disabled, hover, focus, and long-content cases

## Input Mode and Evidence Path

Use the strongest available evidence path in this order:

1. Canonical Figma frames, variants, annotations, and component settings
2. Shared `project-ds-spec.md` and upstream concept or variant deliverables
3. Implementation previews, screenshots, or prototype exports
4. Inference from adjacent screens and established design conventions

Declare which path was used and its limitations.
If evidence is partial, label the missing parts explicitly instead of filling them with polish.

## Tool Selection Rationale

- `figma` is the primary path because it is the best source for authoritative layout, spacing, variants, tokens, and handoff-ready screen structure.
- `stitch` is useful when the upstream concept was authored there or when the screen needs to stay in a prompt-to-canvas loop during convergence.
- `v0` is useful when a blank or near-blank frontend needs a production-shaped preview quickly, especially if code-first iteration will inform the screen structure.
- `framer` is useful when breakpoint behavior, motion, and interactive presentation need to be validated in a polished prototype environment.
- `penpot` is useful when the team benefits from open, library-driven design system inspection, shared components, and inspectable production specs.
- `storybook` is useful when the screen is expressed through reusable components and the handoff needs component-level visual verification.
- `playwright` is useful when the implementation preview or prototype needs screenshot or trace-based confirmation.
- `paper` and `open` are fallback paths for static artifact review when a live design environment is unavailable.

## Environment and Reproducibility

Record the following whenever it is known:

- Platform or device used to inspect the design
- Auth, data, and environment state
- Figma file or frame version, prototype URL, or preview build version
- Breakpoint, viewport, or container size

If any of those are unknown, say so.
Do not silently substitute an assumed environment for an observed one.

## Model Building

Build a screen model before making production decisions.

The model should capture:

- Route or surface boundaries
- Screen inventory and navigation context
- Information hierarchy
- Component inventory and reuse boundaries
- State inventory
- Token and spacing relationships
- Spec deltas that may affect `project-ds-spec.md`

No production conclusion should be made before that model exists.

## Core Method Execution

1. Confirm the upstream direction and the exact scope of the production pass.
2. Translate the chosen direction into a screen inventory and hierarchy model.
3. Lock the layout structure, spacing scale, and token usage before polishing details.
4. Sweep responsive behavior and interface states together instead of treating them separately.
5. Identify any required `project-ds-spec.md` changes when the production pass changes system direction.
6. Prepare the handoff notes so engineering can preserve the exact structure, states, and constraints.
7. Mark any unresolved assumptions or partial evidence so the next pass can close them deliberately.

If the assignment is a `new design` pass, this is convergence-only work.
Do not use it to continue concept exploration.
If no upstream direction exists for a `new design` assignment, stop and note the mismatch instead of inventing one.
If no upstream `project-ds-spec.md` exists for `new design`, stop and note the mismatch instead of inventing around it.

## Structured Decisions

Use a strict schema for each locked design decision or spec delta.

#### Decision <id>
- Observation:
- Evidence:
- Repro steps:
- Cause:
- Impact:
- Confidence:

Use one decision entry for each materially different screen, state, token, or system choice.
Separate observation from interpretation.
If a decision is provisional, label it as such.

## Prioritization Logic

- Lock hierarchy, layout, and state coverage before visual flourish.
- Treat responsive breaks, empty/error/loading states, and reuse constraints as high priority because they affect implementation risk.
- Group minor alignment or spacing cleanup into patterns instead of writing isolated micro-decisions.
- Only create standalone decision entries for issues or choices that change the handoff or system spec.

## Coverage Map

State which parts of the design were deeply covered, partially covered, and not covered.

- Deeply covered: the selected screen set, chosen hierarchy, and the core responsive or state matrix
- Partially covered: secondary states, long-content stress cases, or adjacent screens that influence reuse
- Not covered: unrelated flows, alternate concepts, and implementation details outside the production scope

## Limits and Unknowns

Include:

- What could not be validated in the available evidence path
- What still requires implementation or prototype review
- Where confidence is low because the upstream direction or spec is incomplete

Do not present inferred structure as if it were observed.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: screen-production-design`, include:
- `### Assignment type`: State whether this is `new design` convergence or an extension of an existing pattern.
- `### Chosen direction`: For `new design`, name the exact upstream concept or variant section being converged.
- `### Inherited principles`: List the traits from the winning direction that must remain visible in the production design.
- `### Non-goals`: State what this production pass is not trying to solve or reinvent.
- `### Project ds-spec alignment`: Name the exact sections of `project-ds-spec.md` this production pass is inheriting, where the screen is extending them, and whether any spec updates are required.
- `### Screen inventory`: List the screens or states covered in the production design set.
- `### Layout and tokens`: Define the layout model, hierarchy, and token usage concretely.
- `### State coverage`: Specify all core states required for implementation.
- `### Implementation notes`: Call out constraints and details engineering must preserve.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, stitch`.
- If both paths fail, produce the best-guess output described as: A production-ready screen spec or screen set.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- This is convergence-only work for `new design`; do not use it as a substitute for concept exploration.
- Inherit from `logs/active/<project-slug>/deliverables/project-ds-spec.md`, not directly from company reference files.
- Preserve the winning direction's distinguishing traits instead of collapsing back to safe defaults.
- When production decisions materially change the recommended implementation foundation, update `## Implementation Foundation` in `project-ds-spec.md` instead of burying the change inside screen notes.
- If no upstream direction exists for a `new design` assignment, stop and note the mismatch instead of inventing one.
- If no upstream `project-ds-spec.md` exists for `new design`, stop and note the mismatch instead of inventing around it.
- Use current ecosystem alternatives as support tools when helpful, including `v0` for prompt-first production previews, `framer` for interaction and breakpoint shaping, `penpot` for library-driven inspection, and `storybook` plus `playwright` for verification-oriented handoff checks.
- Keep those alternatives supportive, not authoritative; the selected direction still comes from the upstream design evidence.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Read `logs/active/<project-slug>/deliverables/project-ds-spec.md` first and update it only when the production pass materially changes system direction.
- Keep all work for this skill inside `## Skill: screen-production-design`.
- In `project-ds-spec.md`, limit updates to `## Implementation Foundation`, `## Spacing And Layout Rules`, `## Component Families`, `## Widget And Layout Patterns`, and `## State, Motion, And Accessibility Rules`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Layout, hierarchy, tokens, and core states are specified clearly.
