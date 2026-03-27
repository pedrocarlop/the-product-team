---
name: slice
description: Break a full-stack feature into the smallest safe end-to-end increment that can be modeled, wired, tested, and shipped without drift.
---

# Slice

## Purpose

Use this skill to turn a broad feature request into a shippable vertical slice with a clear first cut, explicit boundaries, and a safe path to expand later.

## When to Use

- When the feature spans API, data, and UI and needs a bounded first milestone
- When the work is likely to grow, but one thin end-to-end path should land first
- When scope needs to be reduced without losing the real user outcome

## When Not to Use

- When the request is already small enough to implement directly
- When the main issue is schema design, screen layout, or release hardening rather than scope definition
- When the work is only about one layer of the stack

## Required Inputs

- The user outcome or business goal
- Known constraints around API shape, data model, UI states, and rollout safety
- Existing dependencies, feature flags, and adjacent work
- Any deadlines, risk limits, or must-ship paths

## Workflow

1. Restate the request as a vertical slice that one user can complete.
2. Identify the minimum API, data, and UI surface needed to prove the outcome.
3. Separate must-have scope from follow-up scope.
4. Name the hidden risks that make the slice unsafe if included too early.
5. Define the sequence of work so contract, model, wireframe, and release steps stay aligned.
6. Confirm what is explicitly out of scope for this slice.

## Design Principles / Evaluation Criteria

- Small enough to finish, useful enough to matter
- One slice should prove the contract end to end
- Scope cuts should reduce risk, not remove the actual user value
- The first increment should create learning without creating rework

## Output Contract

- A thin vertical slice with clear in-scope and out-of-scope items
- The smallest API and data requirements needed for that slice
- A short sequencing note for implementation and release
- Any follow-up slices that should wait until the first one is validated

## Guardrails

- Do not turn slice planning into architecture theater
- Do not include extra endpoints, screens, or migrations just because they seem convenient
- Do not hide risk by calling a large feature "just one slice"

## Optional Tools / Resources

- Product requirements or PRDs
- Existing API specs and schema docs
- Feature flag plans and release notes
- Notes from design, backend, or QA on major dependencies
