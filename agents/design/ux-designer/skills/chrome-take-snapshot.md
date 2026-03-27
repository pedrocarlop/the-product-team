---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture the current product's DOM to understand the existing UX structure, interaction patterns, and information architecture.
---

# Chrome: Take Snapshot

Use this skill to inspect the live product's current UX structure — navigation patterns, modal and drawer usage, form flows, and content organization — before designing new flows. Grounding new UX decisions in the current product prevents introducing structural inconsistencies.

## When to Use

- Before redesigning an existing flow — understand how the current UX is structured in the DOM
- When auditing the current IA and navigation to identify the patterns the new design must integrate with
- When checking how the current product handles a specific state (modal, error, empty, step completion)
- When verifying that the proposed flow structure is consistent with how similar flows are implemented

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the relevant product page. Inspect the returned DOM for:
- Navigation component structure — menus, breadcrumbs, tabs, and their nesting
- Modal and drawer trigger patterns — what interaction opens them, how they are structured
- Form flow structure — how multi-step processes are organized in the DOM
- Content container patterns — how the current layout organizes primary and secondary content

## What to Extract

- Structural patterns to preserve or consciously deviate from in the new design
- Existing ARIA roles and landmarks that define the current UX scaffold
- Interaction patterns that users are already familiar with that the new design should not arbitrarily change
- Specific DOM evidence to cite in `research-and-rationale.md` when justifying a structural decision

## Notes for UX Designer

Consistency with the existing product is a UX value — not just a design-system constraint. When the new flow departs from an established interaction pattern, document why in `research-and-rationale.md`. Silent departures from familiar patterns increase cognitive load.
