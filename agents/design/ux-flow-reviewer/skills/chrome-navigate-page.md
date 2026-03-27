---
name: chrome-navigate-page
tool: mcp__chrome_devtools__navigate_page
description: Follow user flows in the live product to verify that navigation paths are complete, reachable, and free of dead ends.
---

# Chrome: Navigate Page

Use this skill to walk through user flows in the live product (or prototype) following the task flows defined in `task-flows.md`. Flow logic can only be fully validated by exercising the actual navigation — not by reading the flow description.

## When to Use

- As the primary method for verifying that each task flow in `task-flows.md` can be completed
- When checking that all entry points described in the flow are reachable from the product
- When verifying that navigation between steps does not produce dead ends or orphaned screens
- When tracing alternate paths and error recovery paths to confirm they resolve correctly

## How to Use

Call `mcp__chrome_devtools__navigate_page` with the entry point URL for each flow. Walk through each path:
1. Navigate to the entry point — verify it exists and is reachable
2. Follow the happy path step by step — verify each transition occurs and leads to the correct next step
3. Navigate back to branch points and follow alternate paths — verify they resolve and do not dead-end
4. Navigate to states that should trigger errors — verify error states are reachable and lead to recovery

## What to Extract

- Entry points that are not reachable as described in the flow
- Steps that produce no navigation change (dead interactions)
- States from which the user cannot proceed or return
- Transitions that do not match the `task-flows.md` specification

## Notes for UX Flow Reviewer

Navigate every path defined in `task-flows.md`, not just the happy path. An unverified alternate path is an untested failure mode. If the prototype or implementation does not support a path, document it as a gap — do not assume the path works.
