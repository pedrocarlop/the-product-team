# Reviewer Capability Card

## Purpose
Validate work across all disciplines — requirements, UX flows, usability, copy, design system, engineering, and quality assurance.

## Managed Skills
- **requirements**: validation of PRDs vs requests
- **ux-flow**: behavioral traversal and logic checks
- **usability**: heuristic evaluation and friction audits
- **copy**: tone, clarity, and error message review
- **design-system**: component and token compliance
- **engineering**: production-readiness, security, and performance
- **qa**: automation, coverage, and gating

## Input/Output Contract
- **Takes**: `logs/active/<project-slug>/context.md`, any specialist deliverables in `deliverables/`
- **Produces**: `logs/active/<project-slug>/plans/reviewer.md`, `logs/active/<project-slug>/reviews/reviewer.md`

## External Tools (MCP)
- **figma**: Visual comparison of implementation vs design.
- **chrome_devtools**: Performance audits, network inspection, and snapshotting.
- **github**: Code review and PR approval.
- **browserstack**: Cross-device and cross-browser validation.
- **sentry**: Regressions and error rate monitoring.

## Reference Skills
- `reference`: Evidence collection for review findings.
