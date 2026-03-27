---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture the live product's DOM to identify pattern drift between the current implementation and the design system.
---

# Chrome: Take Snapshot

Use this skill to inspect the current product implementation and identify existing design-system violations, legacy patterns, or drift that the new design must address or at minimum not worsen.

## When to Use

- When establishing a baseline of the current implementation's design-system conformance before reviewing the new design
- When checking whether the proposed design introduces new drift on top of existing violations
- When verifying that the target repository's component usage matches what the design system documents

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the relevant product page. Inspect the returned DOM for:
- Component class names that reveal which design-system components are actually used
- Custom CSS or inline styles that suggest off-system styling
- Structural HTML patterns that differ from the design-system's documented component markup
- Evidence of legacy components that are being replaced or extended

## What to Extract

- Component identifiers in the DOM (class names, data attributes, element types)
- Deviations from the design system's documented DOM structure
- Any drift that the new design's component-mapping must explicitly resolve

## Notes for Design System Reviewer

The DOM snapshot tells you what is shipped, not what is designed. Use this to flag when the proposed design would replace a known violation with an approved pattern (good) versus introduce a new violation on top of an existing one (blocker).
