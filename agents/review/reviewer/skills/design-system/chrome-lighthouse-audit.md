---
name: chrome-lighthouse-audit
tool: mcp__chrome_devtools__lighthouse_audit
description: Run an automated Lighthouse audit to surface accessibility, performance, and best-practice signals that reveal design-system implementation quality.
---

# Chrome: Lighthouse Audit

Use this skill to run an automated audit on the current product page and surface objective quality signals — accessibility violations, performance issues, and best-practice gaps — that indicate design-system implementation quality or confirm that pattern choices have downstream risks.

## When to Use

- When reviewing whether the current implementation meets the accessibility baseline the design system requires
- When checking if the design's component choices have known performance or accessibility implications
- When supporting a finding with an automated audit result rather than a subjective observation
- When the design proposes using a custom component instead of a native or system one — verify the tradeoff is justified

## How to Use

Call `mcp__chrome_devtools__lighthouse_audit` on the relevant product URL. Review the returned report for:
- Accessibility score and violations (especially contrast, focus management, ARIA usage)
- Best-practice violations that suggest component misuse
- Performance flags that correlate to heavy custom components replacing lighter system ones

## What to Extract

- Accessibility violations that are attributable to component or pattern choices
- Scores that contradict the design's claim of design-system alignment
- Specific audit items to cite as evidence in `validation-ds.md` findings

## Notes for Design System Reviewer

Use the Lighthouse audit to support findings with data, not to replace design judgment with an automated score. A passing score does not mean the design is system-aligned. A failing audit item that is attributable to a specific component choice is strong evidence for a blocker or major finding.
