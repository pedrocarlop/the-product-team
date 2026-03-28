---
name: chrome-lighthouse-audit
tool: mcp__chrome_devtools__lighthouse_audit
description: Run an automated Lighthouse audit to surface accessibility baseline risks that indicate usability and interaction quality issues.
---

# Chrome: Lighthouse Audit

Use this skill to run an automated accessibility and usability audit on the reviewed design's current implementation (if available) or on analogous pages to establish a baseline. Automated audit results provide objective evidence for findings that might otherwise be subjective.

## When to Use

- When evaluating the accessibility baseline of the implementation — contrast, focus management, ARIA usage
- When supporting a heuristic finding with an automated audit result (e.g., supporting a "feedback" heuristic violation with a contrast audit failure)
- When the reviewed design proposes a pattern that has known accessibility implications
- When checking whether the current product page that the design modifies already has baseline accessibility violations that must not be worsened

## How to Use

Call `mcp__chrome_devtools__lighthouse_audit` on the relevant product page. Evaluate the accessibility section for:
- **Contrast violations**: Fail if any element fails WCAG AA contrast thresholds
- **Focus order issues**: Flags when focus sequence does not match visual order
- **Missing labels**: Form fields, icon buttons, or interactive elements without accessible names
- **ARIA misuse**: Roles or properties that contradict the element's visual behavior

## What to Extract

- Accessibility violations that represent heuristic failures (poor feedback, broken focus, missing affordance)
- Contrast scores for text elements that affect readability
- Specific audit item IDs to cite in `validation-usability.md` findings

## Notes for Usability Reviewer

Use the Lighthouse audit to complement, not replace, manual usability evaluation. A 100% accessibility score does not mean the design is usable — but an accessibility failure almost always signals a heuristic violation. Translate every audit item into the heuristic it violates before including it in a finding.
