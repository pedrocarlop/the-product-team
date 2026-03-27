---
name: chrome-click
tool: mcp__chrome_devtools__click
description: Interact with UI elements to verify task completion paths, decision points, and transition logic in the live flow.
---

# Chrome: Click

Use this skill to interact with specific UI elements during flow review — triggering actions, completing steps, and exercising decision points to verify that the flow logic behaves as specified in `task-flows.md`.

## When to Use

- When verifying that a CTA or action trigger produces the correct flow transition
- When exercising a decision point to confirm both branches lead to the correct next steps
- When triggering error conditions by clicking in an invalid state to verify error recovery works
- When checking that back-navigation, cancel actions, and dismissal patterns return to the correct state

## How to Use

Call `mcp__chrome_devtools__click` with the selector or element description for the target UI element. After each click, observe:
- Did the expected navigation or state transition occur?
- Does the resulting screen match the next step in `task-flows.md`?
- Is the user's progress preserved (form data, selections, context)?
- Does the back/cancel action return to the correct prior state?

## What to Extract

- Interactions that produce incorrect or missing transitions
- Decision points where only one branch is correctly implemented
- Cancel or back actions that clear unexpected state or navigate incorrectly
- Clicks that produce no observable response (dead interactions)

## Notes for UX Flow Reviewer

Click every interactive element that represents a decision point or transition in the flow — do not assume an element works because it appears correctly in the design. Untested transitions are untested failure modes. Document each non-working interaction as a specific flow gap finding in `validation-ux-flow.md`.
