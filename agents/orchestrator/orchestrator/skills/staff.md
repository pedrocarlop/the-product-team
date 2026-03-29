---
name: staff
description: Select the minimum viable role set and assign ownership.
activation_hints:
  - "Use after routing decides orchestration is needed."
  - "Use when a staffed role may be redundant, missing, or incorrectly assigned."
---

# Staff

## Purpose

Staff work deliberately with the minimum viable team.

## Rules

- One role = one subagent.
- Prefer the minimum viable set of specialists.
- Include reviewers only when they materially reduce risk.
- Specialists accept assignments directly unless there is a clear mismatch.
- Request specialist plans only when written advice is needed to resolve ambiguity or tradeoffs.

## Staffing Heuristics

- Use `engineer` for product implementation (frontend, backend, fullstack, mobile, ML).
- Use `platform-engineer` for API contracts, databases, infrastructure, performance, security.
- Add `designer` when UX, IA, copy, layout, or visual decisions are not already fixed.
- Add `design-systems` for token architecture, component-library, or design-engineering bridge work.
- Add `product-lead` for discovery, prioritization, or requirements ownership.
- Add `analyst` for metrics design, financial modeling, or forecasting.
- Add `go-to-market` for growth, positioning, launch, or partnerships.
- Add `reviewer` for independent cross-discipline validation.

## Output

Update `logs/active/<project-slug>/context.md` with staffed roles and ownership map.
