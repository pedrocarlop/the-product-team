---
name: chrome-list-console-messages
tool: mcp__chrome_devtools__list_console_messages
description: Read browser console output to diagnose runtime errors, warnings, and unexpected behavior during implementation verification.
---

# Chrome: List Console Messages

Use this skill to inspect the browser console for runtime errors, warnings, and log output after implementing a change. This is the fastest way to catch component errors, missing props, token resolution failures, and state management bugs before handing off to the engineering reviewer.

## When to Use

- After implementing a component or feature, before writing `implementation-notes.md`
- When a UI state is not rendering as expected and you need to identify the root cause
- When checking for console warnings about accessibility violations (ARIA, focus, contrast)
- When verifying that async operations (API calls, data loading) complete without errors

## How to Use

Call `mcp__chrome_devtools__list_console_messages` after navigating to the implemented page. Review all output for:
- `Error` level: Must be resolved before handoff
- `Warning` level: Evaluate whether the warning indicates a risk — many are blocking for production
- `Log` level: Review debug output that reveals unexpected state or data flow

## What to Extract

- Any error that originates from the implemented component (filter by file path or component name)
- Warnings about prop mismatches, missing keys, or deprecated API usage
- Any output that contradicts the expected behavior described in `tech-plan.md`

## Notes for Engineer

Do not hand off to the engineering reviewer with unresolved console errors. Warnings must be evaluated — a missing `key` prop warning in a list is a blocker; an informational logging warning from a third-party library may not be. Document any accepted warnings in `implementation-notes.md` with the reason they are acceptable.
