---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture the live product's DOM to audit copy in the shipped experience and compare it against the design intent.
---

# Chrome: Take Snapshot

Use this skill to inspect the copy that is actually rendered in the live product — error messages, labels, confirmation dialogs, and empty states — to compare against the design and identify drift or residual copy issues.

## When to Use

- When reviewing whether existing product copy conflicts with the new design's copy direction
- When checking whether previously flagged copy issues have been fixed in the shipped UI
- When auditing the current product to establish a copy baseline before the new design is implemented
- When verifying that the component's rendered text matches the approved copy

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the relevant page. Parse the returned DOM for visible text nodes. Focus on:
- Error message strings rendered in alert or validation components
- Button and CTA label text
- Empty-state heading and body text
- Any copy string that differs from the design's intent

## What to Extract

- Rendered copy strings to compare against the design
- Inconsistencies between live copy and the copy specified in `ui-spec.md`
- Any legacy copy that is inconsistent with the new direction

## Notes for Copy Reviewer

The snapshot shows what is rendered, not what is designed. Use this skill to verify parity between the design's copy intent and the actual product copy. Discrepancies become findings in `validation-copy.md`.
