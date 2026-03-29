---
name: route
description: Decide whether a request should be executed directly or routed into the multi-agent workflow.
activation_hints:
  - "Use at the start of every new request."
  - "Use when deciding whether orchestration overhead is justified."
---

# Route

## Purpose

Decide quickly whether a request needs orchestration or direct execution.

## Decision Criteria

- Start from the request and repository context.
- Classify likely domain(s) first.
- If single-domain, consult only the relevant discipline slice from the role catalog.
- Read the full role catalog only when the task is ambiguous or cross-functional.
- Check `logs/TIMELINE.md` for past project context.
- Route to direct execution when work is single-domain, clearly scoped, and specialist staffing would not materially improve the outcome.
- Route to orchestration when the task needs cross-functional ownership, meaningful specialist judgment, or review gates.

## Output

Create `logs/active/<project-slug>/context.md` with the project goal, constraints, and initial direction. Append a row to `logs/TIMELINE.md`.
