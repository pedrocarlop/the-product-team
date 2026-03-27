---
name: staff
description: Select the minimum viable specialist set, launch one subagent per role, and record ownership decisions in `02_staffing.md`.
activation_hints:
  - "Use after `01_intake.md` is complete and the work requires orchestration."
  - "Use when a staffed role may be redundant, missing, or incorrectly assigned."
  - "Do not combine multiple specialist roles into a single staffed owner."
---

# Staff

## Purpose

Use this skill to staff work deliberately and keep ownership crisp across business, design, and engineering.

## Rules

- One role = one subagent
- Prefer the minimum viable set of specialists
- Include reviewers only when they materially reduce risk
- Require each staffed specialist to complete the fit-check protocol before ownership is accepted
- Start from the best-team assessment recorded during routing, then trim to the minimum viable staffed team for execution.

## Staffing Heuristics

- If routing concluded that a substantial build or rebuild belongs in orchestration, staff an implementation specialist subagent rather than letting the orchestrator absorb build ownership.
- Use `frontend-engineer` when the work is primarily client or UI implementation within an existing backend or static surface.
- Use `fullstack-engineer` when backend, data, API, auth, or server-rendering concerns are materially in scope.
- Add `product-designer` or `ui-designer` when UX flows, information architecture, copy, layout, visual direction, or component-state decisions are not already fixed and approved.

## Output Contract

Write `logs/active/<project-slug>/02_staffing.md` with:

- Selected roles
- Launched subagents
- Fit-check summaries
- Rejected or replaced roles
- Final ownership map
- Staffing rationale
