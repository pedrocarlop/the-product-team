---
name: chrome-lighthouse-audit
tool: mcp__chrome_devtools__lighthouse_audit
description: Run an automated Lighthouse audit to surface accessibility, performance, and best-practice risks in the implementation.
---

# Chrome: Lighthouse Audit

Use this skill to run an automated quality audit on the implemented page and surface objective signals — accessibility violations, performance regressions, and best-practice gaps — that support or contradict the engineering review verdict.

## When to Use

- As a mandatory check during every engineering review pass
- When the implementation uses custom components in place of native or design-system elements — verify the tradeoff did not introduce accessibility regressions
- When the PRD includes non-functional requirements for performance or accessibility
- When supporting a `fail` or `pass_with_notes` verdict with objective audit data

## How to Use

Call `mcp__chrome_devtools__lighthouse_audit` on the implemented feature URL. Evaluate the report across all categories:
- **Accessibility**: Any violation is a candidate for a blocker or major finding
- **Performance**: Flag regressions relative to the pre-implementation baseline when available
- **Best Practices**: Violations that relate to the component or API choices made during implementation
- **SEO**: Relevant only when the PRD includes discoverability requirements

## What to Extract

- Accessibility audit items with their WCAG criteria and impact level
- Performance scores and the specific metrics that contribute to them
- Best-practice violations that link to implementation decisions (e.g., deprecated API usage)

## Notes for Engineering Reviewer

Cite specific Lighthouse audit items in `validation-report.md` findings. Do not report raw scores as findings — translate each audit item into what it means for the implementation risk. A score of 90 with a critical contrast violation is still a blocker.
