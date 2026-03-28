# Unified Plan

## Objective
Deliver a guided onboarding flow for the HR portal covering profile setup, team assignment, tool access, and welcome checklist.

## Required Direct Reads

- `product-designer`: `00_routing.md`, `01_intake.md`
- `frontend-engineer`: `00_routing.md`, `01_intake.md`, `plans/product-designer.md`, `deliverables/product-designer.md`
- `ux-flow-reviewer`: `00_routing.md`, `01_intake.md`, `03_unified-plan.md`, `deliverables/product-designer.md`, `deliverables/frontend-engineer.md`

## Skill Sources Read

- Designer skills: `ux/flow`, `ux/specify`, `ui/stateful`, `motion/transition`, `motion/reduce`, `accessibility/annotate`
- Engineer skills: `frontend/stateful`, `frontend/translate`, `frontend/harden`
- Reviewer skills: `ux-flow/critique`, `qa/gate`

## Skill-Derived Best-Practice Implications

- State coverage must be complete before implementation starts: empty, in-progress, validation error, success, and resumed states.
- Progress feedback must be understandable without relying on animation or color alone.
- Step transitions should preserve task momentum, avoid large-area movement, and define reduced-motion behavior up front.
- Engineering should treat the design plan and deliverable as implementation inputs, not re-interpret the intended interaction model.
- Review must check reduced-motion behavior and navigation edge cases, not only the happy path.

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

## Detailed Merged Implementation By Role

### Product-designer
- Finalize task flow, state model, and responsive layout for all four steps.
- Specify local `StepIndicator` behavior, including validation blocking, focus movement, and reduced-motion fallback.
- Keep inline recovery behavior visible at the field level and prevent false forward progress in the indicator.

### Frontend-engineer
- Implement the onboarding route and step components against the design plan without simplifying state coverage.
- Keep the step indicator local to the feature in v1.
- Preserve focus movement, validation blocking, and reduced-motion behavior exactly as specified.

### UX-flow-reviewer
- Validate desktop and mobile behavior, happy path and recovery path coverage, and progress semantics under both motion modes.
- Flag any implementation that reintroduces decorative motion, color-only status communication, or missing error recovery.

## Critical Detail Register

- Progress indicator remains local to this feature in v1 and is not promoted to the shared design system during this cycle.
- Successful step completion fills the current progress segment over 180ms ease-out; the next step label fades in over 120ms after a 40ms delay.
- Reduced motion removes the progress fill and label fade; the state changes instantly while focus still advances to the next step heading.
- Validation errors remain inline and block progress advancement until the current step is valid.
- Desktop keeps a sticky side progress rail; mobile stacks progress above the onboarding card and uses compact dots plus the active-step label.

## Overlap Resolutions And Conflict Decisions

- Designer and engineer both referenced progress behavior; the designer's detailed interaction spec is authoritative, and the engineer implements it without redefining the UX.
- Multiple inputs referenced state coverage; the unified plan merges them into one requirement set instead of repeating separate lists.
- No remaining ownership conflicts: designer owns interaction definition, engineer owns implementation, reviewer owns independent validation.

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
