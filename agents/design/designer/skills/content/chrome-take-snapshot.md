---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture the current DOM snapshot of a live product to inspect the conversation surface, UI states, and existing interaction patterns.
---

# Chrome: Take Snapshot

Use this skill to capture the DOM structure of the current product's conversation interface. This gives structural insight into how the existing chatbot or AI surface is built, which informs dialogue flow design decisions.

## When to Use

- When the conversation surface already exists in the product and you need to understand its current state model
- When verifying that the proposed dialogue states align with the rendered component structure
- When checking how error or empty states are currently displayed in the live UI
- When grounding the design in the actual DOM rather than assumptions

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the page that hosts the conversation UI. Inspect the returned DOM for:
- Existing message container structures
- State class names that reveal how error, loading, or empty states are triggered
- Input affordances and submit patterns
- Any hardcoded dialogue strings visible in the DOM

## What to Extract

- Current message rendering structure (to align the new flow with existing patterns)
- State indicators — loading spinners, error banners, empty-state containers
- Any inline copy already in the DOM that the new dialogue must stay consistent with

## Notes for Conversation Designer

Use the snapshot to close the gap between designed dialogue states and what the UI can actually render. If the DOM reveals a constraint (e.g., no multi-turn message threading), document it in `research-and-rationale.md` as a design constraint.
