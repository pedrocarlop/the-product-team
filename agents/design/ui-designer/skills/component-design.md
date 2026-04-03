---
name: component-design
description: Create or extend reusable UI components with explicit anatomy, state coverage, reuse rules, and handoff signals.
trigger: When the feature needs reusable UI patterns, not just one-off screens.
primary_mcp: figma
fallback_tools: paper
best_guess_output: A reusable component proposal with explicit states, reuse rules, and handoff notes.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer-component-design.md
done_when: Component purpose, states, and intended reuse are explicit.
required_inputs:
  - component goal or user task
  - target surface or adjacent screens
  - known states, variants, and constraints
  - reuse expectations or design system context
  - implementation stack or component library when known
recommended_passes:
  - anatomy and hierarchy
  - variant and state coverage
  - reuse and adoption fit
  - accessibility and responsive behavior
tool_stack:
  - figma
  - chrome_devtools
  - paper
  - repository
inspiration_tools:
  - stitch # browse and screenshot only — never generate components with stitch
tool_routing:
  - If the task is a new reusable component concept, use `figma` first.
  - If high-fidelity production components are needed, use `paper`.
  - If inspiration-only reference layouts or component patterns are needed, browse stitch screenshots for visual reference only — do not generate components with stitch.
  - If the component already exists in code or must be verified in a live surface, use `chrome_devtools`.
  - If the task is docs-only, planning-only, or blocked on assets, use `paper` plus `repository` context.
  - If the repo has Storybook, treat it as a supporting verification surface for isolated states and documented variants.
---

# Component Design

## Purpose

Build reusable UI components as system objects, not one-off screen parts.

This skill defines component anatomy, variants, states, constraints, and reuse boundaries so the component can be adopted consistently across the product.

This skill does not replace screen production design, visual polish, or code implementation ownership. It also does not invent a new system primitive when an existing one can be extended cleanly.

## Required Inputs And Assumptions

- Required inputs: component goal, target surface, expected users, known states, reuse intent, and implementation context when available.
- Known vs unknown: treat missing library, token, or runtime details as unknowns rather than filling them in silently.
- Assumptions: if the component scope is underspecified, infer the narrowest reusable component that solves the stated need and label the assumption clearly in the deliverable.

## Input Mode And Evidence Path

Use this evidence hierarchy:
1. Live design tool or live component explorer when available.
2. Live implementation, browser inspection, or component sandbox when the component already exists in code.
3. Design artifacts, docs, and shared system references.
4. Screenshots, static exports, or recorded behavior.
5. Inference only when no stronger path is available.

Prefer Figma for composition and state modeling, Chrome DevTools for runtime verification, and repository context for adoption constraints. When the project already exposes Storybook, use it as a supporting source for isolated states, usage notes, and visual regression checks.

## Tool Selection Rationale

- `figma` is the primary path because component design needs explicit anatomy, variants, and shared visual decisions.
- `stitch` is for browsing and screenshotting existing reference layouts ONLY. NEVER generate screens, components, or HTML with stitch — it produces incomplete navigation and broken logic.
- `paper` is for creating or editing implementation-ready components. Use `generate_screen_from_text` or `edit_screens` to produce high-fidelity component structure and logic.
- `chrome_devtools` is the best supporting path when the component already exists in a live surface and behavior, layout, or accessibility need to be verified.
- `paper` is the right fallback for planning, contract writing, or unresolved scope when no reliable artifact path is available.
- `repository` context is useful for checking adjacent components, adoption constraints, and naming conventions.
- Storybook, Penpot, and v0 are useful external references when a project already uses them or when the team needs fast component exploration or isolated state validation, but they are supporting inputs, not the source of truth for this skill.

## Environment And Reproducibility

Record the component context that affects the outcome:
- Target product or route.
- Design tool file, frame, or board when known.
- Browser, viewport, OS, and auth state when runtime evidence is used.
- Component library, token set, or implementation branch when known.
- Any mocked or seeded data that changes variant or state behavior.

If these details are unknown, say so explicitly. The goal is to make the component decision reproducible, not to imply a precision that was not available.

## Model Building

Before judging the component, build a component model:
- Purpose: why the component exists.
- Anatomy: parts, slots, nested elements, and hierarchy.
- Behavior: variants, states, triggers, and transitions.
- Constraints: content limits, density, and layout boundaries.
- Adoption boundary: where the component belongs and where it should not be reused.
- System fit: whether the component extends an existing primitive or should become a new shared primitive.

No component recommendation should be made before this model is explicit.

## Core Method Execution

1. Confirm the assignment type: new design exploration or extension of an existing component.
2. Build the component model from the available evidence.
3. Inventory the component parts and decide whether subcomponents are needed.
4. Define the state and variant surface, including empty, loading, disabled, error, and overflow cases when relevant.
5. Test reuse boundaries against the surrounding system and adjacent screens.
6. Check accessibility, density, and responsive behavior alongside the visual structure.
7. Decide whether the component changes require `project-ds-spec.md` follow-up.
8. Record the resulting component decision in the shared deliverable with evidence and confidence.

## Structured Findings

Use this schema for each component decision, constraint, or risk:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Cause:
- Impact:
- Confidence:
- Recommendation direction:

Use one finding per meaningful issue or decision point. Keep observations separate from interpretation.

## Prioritization Logic

- Critical: accessibility blockers, missing core states, or reuse boundaries that would force duplicate components.
- High: token, layout, or interaction gaps that change how the component behaves across variants or breakpoints.
- Medium: naming, slot, or prop ergonomics that affect adoption or consistency.
- Low: polish-level inconsistencies that do not affect reuse or usability.

Merge duplicates, group related low-severity items, and keep the final output focused on the decisions that matter most for adoption.

## Coverage Map

- Deeply covered: component anatomy, state coverage, reuse rules, and accessibility constraints.
- Partially covered: adjacent screen integration, token inheritance, and implementation feasibility.
- Not covered: unrelated flows, backend behavior, and product strategy outside the component scope.

## Limits And Unknowns

- State what could not be validated because the component was only available in static form, a partial implementation, or a limited design artifact.
- State what still needs real implementation or browser verification.
- Call out any low-confidence assumptions about tokens, libraries, or variant behavior.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/ui-designer-component-design.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: component-design`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Assignment type`: State whether the component supports `new design` exploration or extends an existing system.
- `### Required inputs and assumptions`: Restate the inputs used and any assumptions made where scope was underspecified.
- `### Input mode and evidence path`: Identify the evidence hierarchy used and why the chosen path was the strongest available.
- `### Tool selection rationale`: State which tools were used, why they were selected, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record the browser, viewport, OS, auth state, data setup, and build or prototype version when known.
- `### Model building`: Summarize the component model before analysis.
- `### Core method execution`: Walk through the exact decision sequence used for the component.
- `### Structured findings`: Record component decisions or risks using the required finding schema.
- `### Prioritization logic`: Explain how critical, high, medium, and low items were ordered or grouped.
- `### Coverage map`: State what was deeply analyzed, partially analyzed, and not analyzed.
- `### Limits and unknowns`: Explain what could not be validated and where confidence is low.
- `### Component inventory`: List the components or subcomponents in scope and what each one is for.
- `### Variant and state table`: Define variants, states, triggers, and constraints in table form.
- `### Reuse rules`: State where the component should and should not be reused.
- `### Accessibility and layout notes`: Capture key layout, density, and accessibility requirements.
- `### Project ds-spec follow-up`: State whether the component changes require a `project-ds-spec.md` update and why.

## Tool Path

- Start with `figma`.
- If a live implementation or component explorer exists, use `chrome_devtools` to verify behavior, density, and accessibility details.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper`.
- Browse `stitch` ONLY to screenshot existing reference layouts — never generate with it.
- If both paths fail, produce the best-guess output described as: A component proposal or production component design.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Design for reuse, not for one screen only.
- Use `stitch` ONLY to browse and screenshot existing reference layouts for visual inspiration. Never generate screens, components, or HTML with stitch.
- The tool hierarchy is: `paper` creates new designs, `figma` + `paper` edit/inspect existing designs, `stitch` provides visual inspiration by browsing only.
- Use `paper` (via `generate_screen_from_text` or `edit_screens`) to create or edit the actual high-fidelity components.
- Prefer fewer variants backed by layout rules or tokens over a large set of bespoke permutations.
- Use Storybook when it exists to verify isolated states, usage guidance, and visual regressions, but keep the design source of truth in the shared deliverable.
- Use Penpot or v0 only as supporting exploration aids when a team already works that way, then bring the result back into the component contract.
- Tie component decisions back to the broader system and intended adoption.
- If reusable component families or widget patterns materially change, call out the required `project-ds-spec.md` follow-up instead of letting the component drift away from the shared system.
