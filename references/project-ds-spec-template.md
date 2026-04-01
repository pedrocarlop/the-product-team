# Project DS Spec Template

Use this template for `logs/active/<project-slug>/deliverables/project-ds-spec.md`.

This is the product's own design system specification. It is not the company reference library.

## Role Intent

- `ui-designer` seeds the initial direction for greenfield work from up to 3 inspiration-only references in `.codex/product-team/references/reference-design-systems/`.
- `design-systems-designer` expands and maintains the system-level rules that downstream component, widget, and layout work should follow.
- A repo implementation owner later materializes this shared spec into the product's actual DS folder and code artifacts.

## Recommended Header

```yaml
---
role: shared-design
owners: [ui-designer, design-systems-designer]
project: <slug>
deliverable: project-ds-spec
confidence: <0.0-1.0>
inputs_used: [<file-paths>]
evidence_mode: <sourced|fallback|inferred>
---
```

## Section Ownership

- `ui-designer` owns the initial direction and may refresh it only when the product's visual/system direction materially changes.
- `design-systems-designer` owns the operational system sections and should keep them aligned with real design/code evidence.
- Both roles should update only the sections they explicitly own in the assignment.

## Design Principles And Brand Posture

State the product's visual posture, tone, constraints, and the anti-patterns to avoid.

## Reference Inspirations

List the selected company references, what was borrowed, what was rejected, and why the result is still project-specific.

## Typography Direction

Document the intended type personality, hierarchy principles, and reading rhythm.

## Color And Token Direction

Capture the desired color posture, semantic token intent, and any rules that should survive implementation.

## Implementation Foundation

Document whether the product should bootstrap from an existing implementation foundation such as shadcn/ui, or avoid one.

When the recommendation is to use shadcn/ui, record:

- why it fits this product instead of acting as a default habit
- whether the repo is blank enough for initialization versus needing incremental adoption
- the intended official setup path, such as `shadcn/create` or `pnpm dlx shadcn@latest init -t <framework>`
- the expected baseline choices that must match the product spec, such as preset or style, primitive base, `tailwind.cssVariables`, base color, icon library, registries, and any first components or blocks to seed
- which parts remain product-specific and must still be shaped by this spec rather than copied from shadcn defaults

## Spacing And Layout Rules

Define layout rhythm, density, grid tendencies, responsive intent, and section-level spacing behavior.

## Atomic Primitives

Define the core primitives the system is built from, such as type, icon, color, elevation, radius, borders, and surface rules.

## Component Families

List the component families the product should standardize and the usage principles behind them.

## Widget And Layout Patterns

Describe recurring layout/composition patterns and when they should be reused versus kept local.

## State, Motion, And Accessibility Rules

Define interaction tone, state behavior, animation guardrails, and accessibility principles that apply across the product.

## Governance And Adoption

Document ownership, how new system patterns are proposed, and how the product DS folder should consume this spec.

## QA Notes And Open Questions

Track unresolved design-system risks, verification notes, and follow-up work.
