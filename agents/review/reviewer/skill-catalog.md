# Reviewer Skill Catalog

Read this file first when you are staffed for orchestrated work.
It lists only the role-local skills in this folder and keeps descriptions short so you can scan cheaply.
Open only the matching skill files under `skills/`, then end your closing handoff with `Read <skill-paths> skills for this task.`

## requirements/

- `requirements/apply-patch` — Write the Reviewer plan and requirements-review artifacts inside `/logs`.
- `requirements/chrome-navigate-page` — Navigate the live product to verify that PRD requirements are grounded in actual product behavior and existing constraints.
- `requirements/chrome-take-snapshot` — Capture the DOM of the current product state to gather evidence for PRD grounding issues and acceptance criteria verification.

## ux-flow/

- `ux-flow/chrome-click` — Interact with UI elements to verify task completion paths, decision points, and transition logic in the live flow.
- `ux-flow/chrome-navigate-page` — Follow user flows in the live product to verify that navigation paths are complete, reachable, and free of dead ends.
- `ux-flow/figma-get-screenshot` — Capture flow diagrams and screen designs from Figma to evaluate sequence logic, decision points, and transition completeness.

## usability/

- `usability/critique` — Evaluate a design through structured heuristic analysis, scoring usability across cognitive load, discoverability, affordance, and error prevention to produce actionable findings. Use when reviewing wireframes, prototypes, or implemented frontend screens.
- `usability/chrome-click` — Interact with the live product UI to validate discoverability, affordance, feedback, and reversibility heuristics by exercising real interactions.
- `usability/chrome-lighthouse-audit` — Run an automated Lighthouse audit to surface accessibility baseline risks that indicate usability and interaction quality issues.
- `usability/figma-get-screenshot` — Capture design comps to evaluate usability heuristics in the designed visual layout before implementation.

## copy/

- `copy/apply-patch` — Write the Reviewer plan and copy-review artifacts inside `/logs`.
- `copy/chrome-take-snapshot` — Capture the live product's DOM to audit copy in the shipped experience and compare it against the design intent.
- `copy/figma-get-screenshot` — Capture a screenshot of a Figma frame or component to review copy in its visual context.

## design-system/

- `design-system/chrome-lighthouse-audit` — Run an automated Lighthouse audit to surface accessibility, performance, and best-practice signals that reveal design-system implementation quality.
- `design-system/chrome-take-snapshot` — Capture the live product's DOM to identify pattern drift between the current implementation and the design system.
- `design-system/figma-get-screenshot` — Capture design comps from Figma to inspect component usage, composition, and design-system alignment.

## engineering/

- `engineering/chrome-lighthouse-audit` — Run an automated Lighthouse audit to surface accessibility, performance, and best-practice risks in the implementation.
- `engineering/chrome-list-network-requests` — Inspect network traffic to verify that API calls, data loading, and error handling match the approved technical plan.
- `engineering/chrome-navigate-page` — Navigate the live implementation to exercise user flows end-to-end and validate that all approved states and transitions are correctly implemented.

## qa/

- `qa/automate` — Turn QA coverage into reliable automated tests, fixtures, and CI checks that run with strong signal and low maintenance cost.
- `qa/cover` — Design risk-based test coverage across layers, scenarios, and environments so the QA plan proves the feature behaves as intended.
- `qa/gate` — Evaluate QA evidence against release criteria and decide whether the build is ready to move forward.
- `qa/plan` — Turn a QA request into a structured test strategy with scope, risk boundaries, coverage targets, and executable matrices. Use when an epic or feature needs a defensible verification approach before it hits production.
