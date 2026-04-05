# Trace: Product Designer — run-001

## Reasoning

1. Read assignment contract. Confirmed scope: 4-step onboarding flow design.
2. Opened `journey-flow-design` skill. Built task flow model: Profile -> Team -> Tools -> Checklist -> Complete.
3. Identified 5 states per step: empty, in-progress, complete, validation-error, resumed.
4. Designed progress indicator behavior: fill on completion (180ms ease-out), label fade-in (120ms, 40ms delay), reduced-motion instant transition.
5. Opened `screen-production-design` skill. Produced screen specs for desktop (sticky side rail) and mobile (compact dots + active label).
6. Documented component mapping: StepCard, StepIndicator, FormField, ValidationMessage.

## Tools Used

- figma: Created screen designs for all 4 steps across both breakpoints.
- paper: Generated high-fidelity mockups for review.

## Key Decisions

- Progress indicator is local to this feature, not promoted to shared DS.
- Validation errors are inline and block forward progress.
- Reduced motion removes fill animation but preserves focus advancement.

## Deliverables

- `knowledge/product-designer-journey-flow-design.md` (canonical)
- `knowledge/runs/run-001/product-designer-journey-flow-design.md` (snapshot)
