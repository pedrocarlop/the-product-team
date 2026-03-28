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

Use this skill to make the routing decision explicit, cheap, defensible, and logged before any planning or execution begins.

## Decision Criteria

- Start from the request and repository context, not the full role catalog.
- Classify likely domain(s) first.
- If the task is clearly single-domain, consult only the relevant discipline slice from `.codex/product-team/references/role-catalog.md` or `references/role-catalog.md` when staffing is actually being considered.
- Read the full canonical role catalog only when the task is ambiguous, cross-functional, or the right team is genuinely unclear.
- Read `logs/TIMELINE.md` for past project history, previous routing decisions, and which roles have been used for similar work.
- Estimate coordination cost versus likely direct-execution cost before escalating.
- Route to direct execution when the work is single-domain, implementation-first, clearly scoped or easily inferable, low ambiguity, and the best-team assessment shows specialist staffing would not materially improve the outcome.
- Route to orchestration when the best-team assessment reveals meaningful role-specific judgment, cross-functional ownership, ambiguity or tradeoffs, staging or review needs, large context surface, or continuity needs.
- Treat substantial builds and rebuilds as possible evidence for specialists, not an automatic escalation. Make the call from actual role needs rather than keywords alone.
- Bypass orchestration when the task is single-domain, implementation-heavy, clearly specified or easily inferable, and unlikely to benefit from cross-functional negotiation.
- Make the solo/direct vs multi-agent decision before any specialist planning starts.

## Output Contract

Write `logs/active/<project-slug>/00_routing.md` with:

- Original request
- Complexity assessment
- Domain classification
- Role slice or catalog consulted
- Best possible team assessment
- Solo/direct vs multi-agent workflow decision
- Rationale
- Coordination cost estimate
- Why orchestration overhead is or is not justified
- Initial next step

After writing `00_routing.md`, append a new row to `logs/TIMELINE.md` with the project date, slug, objective, workflow decision, planned roles (or `orchestrator (direct)`), status `planning`, and outcome `—`.
