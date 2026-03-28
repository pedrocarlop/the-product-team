---
name: apply-patch
tool: apply_patch
description: Write the full UX/UI design package — task flows, UI spec, component mapping, and research rationale.
---

# Apply Patch

Use this skill to write the four design package artifacts. This is the primary output mechanism for the Product Designer role — all design decisions are captured in these files.

## When to Use

- After completing research and design planning, when you are ready to author the full package
- When revising design artifacts in response to reviewer feedback
- When updating `component-mapping.md` after verifying components against the design system

## How to Use

Invoke `apply_patch` targeting the correct output file path. Write all four artifacts as a coherent package:

- **research-and-rationale.md**: Why these decisions were made — user evidence, design precedents, system constraints, and tradeoff documentation
- **task-flows.md**: Every user path from entry to completion — happy path, alternates, errors, empty states, and recovery
- **ui-spec.md**: Every screen and state specified completely — component, variant, content, behavior, and responsive treatment
- **component-mapping.md**: Every `CMP-*` entry with component name, source system, props, and any justified exceptions

## What to Produce

Completeness requirements before writing:
- All states covered: happy path, alternate, error, empty, loading, success, and destructive confirmation
- All responsive breakpoints specified (or explicitly noted as unchanged)
- All `CMP-*` entries resolved — no "TBD" component selections

## Notes for Product Designer

Do not write stubs. A design package with "component TBD" or "error state to be defined" will fail the design-system review. Finish the design before writing the package, not while writing it.
