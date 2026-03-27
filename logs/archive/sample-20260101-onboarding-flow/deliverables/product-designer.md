# Product Designer Deliverables

## Task Flow
- Step 1: Profile Setup (name, photo, department, start date)
- Step 2: Team Assignment (manager selection, team channel join)
- Step 3: Tool Access (request access to required tools from a checklist)
- Step 4: Welcome Checklist (read handbook, complete compliance training, schedule 1:1)

## Screen States
Each step has 4 states: empty (first visit), in-progress (partially filled), complete (all fields valid), error (validation failure).

## Component Mapping
- `StepIndicator`: horizontal progress bar, 4 segments, uses `--color-primary` for complete
- `OnboardingCard`: content container per step, uses `--spacing-lg` padding
- `FormField`: standard text input with validation, existing component
- `ChecklistItem`: checkbox + label, uses `--color-success` on complete

## Responsive Behavior
- Desktop: side-by-side layout for step indicator + content (min-width: 768px)
- Mobile: stacked layout, step indicator becomes compact dots
