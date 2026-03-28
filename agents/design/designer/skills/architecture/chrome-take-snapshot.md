---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture the current product's navigation and structural DOM to understand the existing IA and identify patterns the new design must integrate with.
---

# Chrome: Take Snapshot

Use this skill to inspect the current product's navigation structure, content groupings, and labeling system as they are implemented in the live DOM. This grounds IA decisions in reality rather than assumptions about the existing product structure.

## When to Use

- Before proposing a navigation restructure — understand what currently exists
- When auditing the current product's taxonomy for inconsistencies that the new IA must address
- When verifying that a proposed IA change is compatible with the existing structural components
- When checking the current depth and breadth of navigation to inform the new hierarchy design

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the main product navigation or the specific section being restructured. Inspect the DOM for:
- Navigation container elements and their ARIA roles (`nav`, `role="navigation"`, `role="menubar"`)
- Menu item hierarchy and nesting depth
- Label strings used in current navigation (identify inconsistencies with proposed taxonomy)
- Structural landmarks that frame the current IA

## What to Extract

- Current navigation labels and hierarchy depth
- ARIA landmarks that define the existing structural skeleton
- Any patterns that the new IA must preserve for continuity (e.g., primary navigation slots)
- Inconsistencies between current label copy and the new taxonomy proposed in the PRD

## Notes for Information Architect

The snapshot reveals what users are navigating today. The new IA must account for existing mental models and navigation habits — document any proposed label changes in `research-and-rationale.md` with the rationale for why the change reduces confusion rather than adding it.
