---
name: apply-patch
tool: apply_patch
description: Write the IA design package — task flows, site maps, navigation specs, and component mappings.
---

# Apply Patch

Use this skill to write the information architecture design package. All four output artifacts must be authored completely before handing off to reviewers.

## When to Use

- After completing research and structural planning for the new IA
- When writing the site map, navigation hierarchy, labeling system, or taxonomy in `task-flows.md` and `ui-spec.md`
- When documenting the component choices for navigation and findability surfaces in `component-mapping.md`
- When revising artifacts in response to reviewer feedback

## How to Use

Invoke `apply_patch` targeting the correct output file path. Each artifact has a specific role:
- **research-and-rationale.md**: Document why the IA is structured as it is — user mental models, findability evidence, structural constraints
- **task-flows.md**: Map user navigation paths — entry points, wayfinding decisions, dead-end prevention
- **ui-spec.md**: Specify each navigation surface — component, label, hierarchy depth, responsive behavior
- **component-mapping.md**: Map each IA element to a `CMP-*` component with the source reference

## What to Produce

Every navigation surface must specify:
- Component name and variant
- Label text (exact string, consistent with the approved taxonomy)
- Hierarchy depth and parent-child relationships
- Responsive behavior at each breakpoint

## Notes for Information Architect

Do not write stubs — every navigation node and taxonomy entry must be fully specified. An IA spec that lists "secondary navigation TBD" is incomplete and will block the engineering reviewer.
