---
name: chrome-click
tool: mcp__chrome_devtools__click
description: Interact with the live product UI to validate discoverability, affordance, feedback, and reversibility heuristics by exercising real interactions.
---

# Chrome: Click

Use this skill to interact with the live product by clicking elements, triggering state transitions, and observing how the UI responds. Usability heuristics cannot be fully evaluated from static screenshots — they require actual interaction.

## When to Use

- When evaluating discoverability — can a user find the primary action without guidance?
- When testing feedback — does the UI respond immediately and clearly to user actions?
- When checking reversibility — are destructive or high-stakes actions clearly reversible or confirmed?
- When verifying focus management — after a modal opens or a dialog appears, does focus move correctly?
- When exercising error prevention — does the UI prevent invalid actions or warn before irreversible ones?

## How to Use

Call `mcp__chrome_devtools__click` with the selector or element description for the target UI element. Observe the result for:
- **Immediate feedback**: Does the element respond visually within 100ms?
- **State change clarity**: Is it clear what changed and why?
- **Next step affordance**: After the click, does the UI make the next required action obvious?
- **Reversibility**: Is there a clear way to undo or go back?

## What to Extract

- Heuristic violations observed during interaction (cite the specific heuristic and the specific element)
- Focus management failures — focus lost, focus in wrong location, no visible focus indicator
- Missing or delayed feedback — actions that do not confirm they occurred
- Accidental action risks — destructive or irreversible actions without confirmation

## Notes for Usability Reviewer

Interact as a user would — not as a developer testing edge cases. Follow the task flows defined in `task-flows.md` and observe whether a real user could complete each step without guidance. Document each heuristic violation with the specific UI element and the specific heuristic it violates.
