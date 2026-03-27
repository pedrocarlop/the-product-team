---
name: route
description: Decide whether a request should be executed directly or routed into the multi-agent workflow, then record the decision in `00_routing.md`.
activation_hints:
  - "Use at the start of every new request."
  - "Use when deciding whether orchestration overhead is justified."
  - "Do not skip this step, even for direct execution."
---

# Route

## Purpose

Use this skill to make the routing decision explicit, defensible, and logged before any planning or execution begins.

## Decision Criteria

- Always identify the minimum viable best team before deciding whether to stay direct or use orchestration.
- Route to direct execution when the work is simple, operational, low-risk, self-contained, clear in scope, and the best-team assessment shows specialist staffing would not materially improve the outcome.
- Route to orchestration when the best-team assessment reveals meaningful role-specific judgment, cross-functional ownership, ambiguity or tradeoffs, staging or review needs, or continuity needs.
- Treat substantial builds and rebuilds as strong evidence that the best team includes specialists, but make the call from actual role needs rather than keywords alone.

## Output Contract

Write `logs/active/<project-slug>/00_routing.md` with:

- Original request
- Complexity assessment
- Best possible team assessment
- Direct execution vs workflow decision
- Rationale
- Why orchestration overhead is or is not justified
- Initial next step
