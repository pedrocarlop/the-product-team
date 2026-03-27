---
name: wire
description: Design the screen structure, interaction flow, and state scaffolding for a full-stack feature once the model is known.
activation_hints:
  - "Use when the flow is understood and the next step is screen-level layout and behavior."
  - "Route here for wireframes, page skeletons, empty states, and responsive interaction rules."
  - "Do not use for visual polish, branding, or contract modeling."
---

# Wire

## Purpose

Use this skill to turn a modeled feature into wireframes that show what each screen contains, how it is arranged, and how the user moves through it.

## When to Use

- When the API and data shape are known and the UI needs to be planned
- When layout, hierarchy, or component placement needs to be defined without final styling
- When loading, empty, error, and success states must be designed into the flow

## When Not to Use

- When the main problem is deciding the feature model or API contract
- When the request is for final visuals, branding, or design-system decisions
- When the work is only about backend logic or rollout safety

## Required Inputs

- The mapped flow, feature slice, or user task
- Any screenshots, mocks, or existing screens to align with
- Component constraints, platform patterns, and breakpoints
- State requirements such as loading, empty, error, success, or disabled
- Accessibility, content, and technical constraints that affect layout

## Workflow

1. Establish the purpose of each screen and the user's primary task.
2. Lay out information from most important to least important.
3. Place controls and feedback where they help the user act quickly.
4. Define behavior for primary, secondary, and conditional actions.
5. Draft responsive variants when viewport changes the structure.
6. Annotate the key decisions that implementation must preserve.

## Design Principles / Evaluation Criteria

- Clarity before decoration
- Strong hierarchy with an obvious primary action
- Predictable component placement and behavior
- States and edge cases should be visible in the scaffold
- The wireframe should be specific enough to review, but loose enough to evolve

## Output Contract

- Low-fidelity wireframes or screen skeletons
- Interaction notes for primary paths and important branches
- Responsive or layout variants when relevant
- Callouts for unresolved structural questions or risky assumptions

## Guardrails

- Do not add visual styling that distracts from structure
- Do not leave critical interactions implied when they need to be explicit
- Do not design every pixel if the question is still about flow or hierarchy
- Do not ignore states that will materially change the user's path

## Optional Tools / Resources

- Existing design system components and layout patterns
- Product screenshots or prototypes
- Device and breakpoint constraints
- Accessibility guidance or interaction standards
