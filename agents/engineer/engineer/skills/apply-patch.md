---
name: apply-patch
tool: apply_patch
description: Implement approved code changes and write engineering artifacts — tech plan and implementation notes.
---

# Apply Patch

Use this skill to implement the approved solution — writing product code, tests, and engineering documentation. It is the primary execution tool for this role.

## When to Use

- When implementing features, components, or fixes aligned to the approved design package
- When writing or updating `tech-plan.md` and `implementation-notes.md`
- When writing tests that cover the states and requirements defined in the design package
- When making targeted fixes in response to engineering review findings

## How to Use

Invoke `apply_patch` with the target file path and the precise code change. Before patching:
1. Read the existing file to understand the current structure and conventions
2. Verify the change aligns with the approved `ui-spec.md` and `component-mapping.md`
3. Preserve traceability — reference `REQ-*`, `UI-*`, and `CMP-*` identifiers in comments or implementation notes

## What to Produce

- **Product code**: Components, logic, styles, and tests that implement the approved design
- **tech-plan.md**: Architecture decision, component approach, risk callouts, tradeoffs
- **implementation-notes.md**: What was built, what was deferred, and any approved scope changes

## Notes for Engineer

Patch one logical unit at a time — do not bundle unrelated changes in a single patch. Every scope deviation from the approved design must be documented in `implementation-notes.md` as a tradeoff, not silently absorbed. Unrelated refactors are explicitly out of scope.
