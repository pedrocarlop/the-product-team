---
name: model
description: Shape the domain, API contract, persistence, and state transitions for a full-stack feature before any layer is built.
activation_hints:
  - "Use when a feature needs explicit domain rules, API boundaries, or persistence decisions."
  - "Route here before coding if the request still has contract drift, unclear invariants, or risky schema changes."
  - "Do not use for release-only work or for UI structure once the model is settled."
---

# Model

## Purpose

Use this skill to define the full-stack model behind a feature: resources, invariants, states, API shapes, and persistence boundaries.

## When to Use

- When a feature needs a stable request and response contract
- When database changes, transactions, cache boundaries, or auth rules are involved
- When frontend and backend need to agree on the same data shape before implementation

## When Not to Use

- When the contract is already settled and the task is pure implementation
- When the work is only about screen layout or deployment mechanics
- When the issue is a narrow bug fix with no meaningful data or contract decision

## Required Inputs

- The user action or business operation being supported
- Any existing schema, service boundary, or OpenAPI spec
- Constraints around auth, consistency, latency, idempotency, and rollback
- Known failure modes or edge cases that matter

## Workflow

1. Restate the feature in domain terms: actors, resources, and state changes.
2. Identify the invariants that must not be violated.
3. Decide where each rule belongs: handler, service, persistence, queue, or client.
4. Define the API contract, including validation and error cases.
5. Map the persistence changes, migrations, and transaction boundaries.
6. Call out assumptions, tradeoffs, and open questions before coding starts.

## Design Principles / Evaluation Criteria

- One domain rule should have one owner
- Contracts should be explicit enough to test without guessing
- State transitions should be easy to reason about and hard to break
- Persistence should support the queries the feature needs, not an abstract ideal

## Output Contract

- A concise feature model with actors, resources, and states
- The proposed API contract or service interface
- Data and migration notes, including indexes and transactions when relevant
- A short list of open questions or tradeoffs that still need confirmation

## Guardrails

- Do not jump into code while the contract is still unstable
- Do not hide consistency or rollback tradeoffs behind vague language
- Do not place business rules where they cannot be tested cleanly

## Optional Tools / Resources

- Existing API specs or service docs
- Database schema and migration history
- Product requirements or incident notes
- GitHub or repo conventions when prior implementations need to be checked
