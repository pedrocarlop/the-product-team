---
name: staff
description: Select the minimum viable archetype set, launch one subagent per staffed archetype, and record ownership decisions in `02_staffing.md`.
activation_hints:
  - "Use after `01_intake.md` is complete and the work requires orchestration."
  - "Use when a staffed role may be redundant, missing, or incorrectly assigned."
  - "Do not combine multiple specialist roles into a single staffed owner."
---

# Staff

## Purpose

Use this skill to staff work deliberately and keep ownership crisp across business, design, engineering, and review.

## Rules

- Start from the domain classification and best-team assessment recorded during routing.
- Re-open the full canonical role catalog only if the task is ambiguous or crosses domains in a way the routing slice did not resolve.
- One archetype = one subagent
- Prefer the minimum viable set of specialists
- Include reviewers only when they materially reduce risk
- Specialists accept assignments directly unless there is a clear mismatch, missing dependency, or ownership conflict.
- Start from the best-team assessment recorded during routing, then trim to the minimum viable staffed team for execution.
- Request `plans/<role>.md` only when written specialist advice is needed to resolve ambiguity, sequencing, or tradeoffs. Otherwise, move straight to orchestrator planning and execution.
- When you request a role plan, ask for execution-grade detail: concrete decisions, edge cases, validation expectations, a `Role-local skills consulted` section, and a final `Critical details that must survive merge` section.
- Record skill hints precisely enough that the orchestrator can later open the matching staffed-role skill files before writing `03_unified-plan.md`.
- Do not bounce incomplete plans back and forth between specialists. Collect advice only when needed, then let the orchestrator merge it once into the cycle plan.
- Base staffing on actual archetype needs rather than task keywords alone.

## Staffing Heuristics

- If routing concluded that a substantial build or rebuild belongs in orchestration, staff an implementation archetype rather than letting the orchestrator absorb build ownership.
- Use `engineer` when the work is primarily product implementation across frontend, backend, fullstack, mobile, or ML delivery.
- Use `platform-engineer` when API contracts, databases, data pipelines, infrastructure, performance, security, architecture, or engineering leadership are materially in scope.
- Add `designer` when UX flows, information architecture, copy, layout, visual direction, motion, accessibility, localization, or service design decisions are not already fixed and approved.
- Add `design-systems` when token architecture, component-library changes, design tooling, or design-engineering bridge work are in scope.
- Add `product-lead` when discovery, prioritization, requirements, portfolio tradeoffs, or delivery coordination need active ownership.
- Add `analyst` when the work depends on metrics design, financial modeling, forecasting, or revenue operations analysis.
- Add `go-to-market` when growth, positioning, launch, partnerships, customer-success, or sales-engineering work is part of the outcome.
- Add `business-ops` when process mapping, business analysis, or operational coordination is central to the task.
- Add `reviewer` when an independent cross-discipline validation pass will materially reduce risk.

## Output Contract

Write `logs/active/<project-slug>/02_staffing.md` with:

- Selected archetypes
- Launched subagents
- Assignment confirmations or mismatch notes
- Advisory planning requests, if any
- Rejected or replaced archetypes
- Final ownership map
- Staffing rationale
