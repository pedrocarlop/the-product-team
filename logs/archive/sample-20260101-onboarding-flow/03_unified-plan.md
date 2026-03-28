# Unified Plan

## Objective
Deliver a guided onboarding flow for the HR portal covering profile setup, team assignment, tool access, and welcome checklist.

## Required Direct Reads

- `product-designer`: `00_routing.md`, `01_intake.md`
- `frontend-engineer`: `00_routing.md`, `01_intake.md`, `plans/product-designer.md`, `deliverables/product-designer.md`
- `ux-flow-reviewer`: `00_routing.md`, `01_intake.md`, `03_unified-plan.md`, `deliverables/product-designer.md`, `deliverables/frontend-engineer.md`

## Execution Sequence

### Stage 1: Design (product-designer)
1. Map the onboarding task flow (4 steps + completion)
2. Design screen states for each step (empty, in-progress, complete, validation error, resumed state)
3. Specify component usage, design tokens, copy rules, and validation behavior
4. Define the `StepIndicator` interaction and progress motion, including reduced-motion fallback
5. Document mobile responsive behavior and sticky desktop progress layout

### Stage 2: Implementation (frontend-engineer)
1. Scaffold onboarding route and step components
2. Implement each step with form validation and inline recovery messaging
3. Integrate with existing profile API
4. Implement responsive breakpoints per design spec
5. Add progress indicator and step navigation exactly as specified by the designer plan and deliverable
6. Preserve reduced-motion behavior and focus movement during step changes

### Stage 3: Review (ux-flow-reviewer)
1. Walk through complete flow on desktop and mobile
2. Verify all states render correctly
3. Check navigation edge cases (back, refresh, deep link)
4. Verify progress behavior in normal and reduced-motion modes
5. Produce review report with pass/fail per criterion

## Critical Detail Register

- Progress indicator remains local to this feature in v1 and is not promoted to the shared design system during this cycle.
- Successful step completion fills the current progress segment over 180ms ease-out; the next step label fades in over 120ms after a 40ms delay.
- Reduced motion removes the progress fill and label fade; the state changes instantly while focus still advances to the next step heading.
- Validation errors remain inline and block progress advancement until the current step is valid.
- Desktop keeps a sticky side progress rail; mobile stacks progress above the onboarding card and uses compact dots plus the active-step label.

## Dependencies
- Stage 2 depends on Stage 1 deliverables
- Stage 3 depends on Stage 2 completion

## Validation / Acceptance Checkpoints
- Design checkpoint: all step states, progress behavior, and responsive layouts are specified before engineering starts.
- Implementation checkpoint: step transitions, validation blocking, and reduced-motion behavior match the design detail register.
- Review checkpoint: desktop, mobile, back navigation, refresh, deep links, and reduced-motion mode all pass.

## Review Points
- Design review after Stage 1
- Flow review after Stage 2

## Approval Gate
This plan requires user approval before execution begins.
