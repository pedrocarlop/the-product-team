---
slug: 20260101-onboarding-flow
objective: Guided employee onboarding flow for HR portal
confidence_score: 0.95
last_sync: 2026-01-03-15:00
status: complete
current_run_id: run-003
---

# Context

## Goal

Build a guided 4-step employee onboarding flow for the HR portal: profile setup, team assignment, tool access, and welcome checklist.

## Constraints

- Must integrate with existing profile API.
- No manager approval gate for tool access in v1 (deferred to v2).
- Must work on desktop and mobile.

## Done When

- All 4 onboarding steps render correctly with proper state handling (empty, in-progress, complete, error, resumed).
- Step transitions preserve task momentum and define reduced-motion behavior.
- Design review passes on desktop and mobile.

## Staffed Roles

| Role | Skill Paths | Assignment Mode |
|---|---|---|
| `product-designer` | `journey-flow-design`, `screen-production-design` | primary_executor |
| `frontend-engineer` | `component-implementation`, `responsive-behavior` | primary_executor |
| `design-reviewer` | `usability-review` | peer_reviewer |

## Primary Tools

- `product-designer`: figma, paper
- `frontend-engineer`: exec_command, repository
- `design-reviewer`: figma, repository

## Status

Complete. All deliverables finalized, review passed. Archived.

## Key Decisions

- 4-step flow (profile, team, tools, checklist) chosen over single-page form for better task completion rates.
- Request-only tool access (no manager approval gate in v1).
- Progress indicator remains local to onboarding feature in v1; not promoted to shared design system.
