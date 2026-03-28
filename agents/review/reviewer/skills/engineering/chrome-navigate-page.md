---
name: chrome-navigate-page
tool: mcp__chrome_devtools__navigate_page
description: Navigate the live implementation to exercise user flows end-to-end and validate that all approved states and transitions are correctly implemented.
---

# Chrome: Navigate Page

Use this skill to walk through the implemented experience in the live product, following the task flows defined in `task-flows.md`. This is the primary way to verify implementation parity — not by reading code, but by exercising the actual experience.

## When to Use

- When starting an engineering review — navigate to the feature before reading any artifacts
- When verifying that each task flow in `task-flows.md` can be completed without dead ends
- When checking that navigation between states (loading → loaded → error → recovery) works correctly
- When verifying that scope boundaries are respected — features outside the approved scope are not implemented

## How to Use

Call `mcp__chrome_devtools__navigate_page` with the URL of the implemented feature. Follow each task flow step by step:
1. Start from the entry point defined in `task-flows.md`
2. Complete the happy path first
3. Then exercise each alternate path, error state, and recovery
4. Note any state that cannot be reached or behaves differently than specified

## What to Verify

- All entry points from `task-flows.md` are reachable and render correctly
- Transitions between states match the approved flow sequence
- No states produce a dead end or unrecoverable UI condition
- The scope boundary is enforced — nothing outside the approved `[in scope]` items is implemented

## Notes for Engineering Reviewer

Navigate before reading the implementation code. Your job is to verify the shipped experience, not to audit the source. What the code says it does is secondary to what the browser actually renders.
