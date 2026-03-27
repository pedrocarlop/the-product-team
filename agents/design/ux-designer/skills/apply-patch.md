---
name: apply-patch
tool: apply_patch
description: Write the UX design package — user flows, wireframe-level specs, IA decisions, and component scaffolding.
---

# Apply Patch

Use this skill to write the four UX design artifacts. UX design output defines the interaction structure and user journey — it is the foundation that visual design and engineering build on.

## When to Use

- After completing flow mapping and IA decisions, when ready to document the design package
- When writing flows that cover all paths — happy, alternate, error, edge, and recovery
- When revising artifacts in response to UX flow review feedback
- When updating component mappings after verifying pattern availability in the system

## How to Use

Invoke `apply_patch` targeting the correct output file path:

- **research-and-rationale.md**: UX rationale — user mental models, flow decisions, IA choices, and tradeoffs documented with evidence
- **task-flows.md**: Complete user journey — entry points, all decision branches, error and recovery paths, and task completion criteria
- **ui-spec.md**: Wireframe-level specification — screen layout, component placement, interaction behavior, state transitions, and content structure
- **component-mapping.md**: Every interaction pattern mapped to a `CMP-*` component with source reference

## What to Produce

Every task flow must cover:
- All entry points to the task
- Happy path with all expected decision points
- At least one alternate path per significant branch
- Error state and recovery path for each user-facing failure
- Empty state when the task begins with no data
- Task completion confirmation

## Notes for UX Designer

Flows that only show the happy path are incomplete and will fail UX flow review. Wireframes without state specifications are incomplete and will fail design-system review. Write the full flow before starting the wireframe spec.
