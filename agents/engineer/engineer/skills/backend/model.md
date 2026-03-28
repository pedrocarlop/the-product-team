---
name: model
description: Shape backend work into explicit domain, data, and contract decisions before implementation starts.
---

# Model

## Purpose

Use this skill to turn a request into a clear backend model: resources, invariants, state transitions, persistence boundaries, and error shapes. The goal is to remove ambiguity before code is written.

## When to Use

- When a new endpoint, background job, or integration needs a stable contract
- When schema changes, cache strategy, or transaction boundaries are part of the work
- When business rules could be implemented in multiple places and need one source of truth

## When Not to Use

- When the contract and data model are already settled and the task is pure implementation
- When the work is only about observability, rollout safety, or production hardening
- When the issue is a small bug fix with no meaningful modeling decisions

## Required Inputs

- The business operation or user action being supported
- Any existing API schema, database schema, or service boundary
- Known constraints around auth, consistency, scale, idempotency, and latency
- Production failure modes that matter, if they are already known

## Workflow

1. Restate the operation in backend terms: actors, resources, states, and outcomes.
2. Identify the core invariants that must never be violated.
3. Decide where each rule belongs: handler, service, persistence layer, queue, or external system.
4. Define the request and response contract, including validation and error cases.
5. Map the data model: tables, indexes, migrations, transactions, and any cache or async boundaries.
6. Call out the assumptions, tradeoffs, and open questions before implementation starts.

## Design Principles / Evaluation Criteria

- Explicit boundaries are better than implicit behavior
- One domain rule should have one owner
- Idempotency and rollback should be designed early, not patched later
- The model should be easy to test without a live production dependency

## Output Contract

- A concise backend model with actors, resources, and state transitions
- The proposed API contract or service interface
- Data and migration notes, including indexes and transaction boundaries when relevant
- A short list of open questions or tradeoffs that still need confirmation

## Examples

### Example 1

Input:
- Task: Add an endpoint to create invoice payments
- Constraints: Duplicate submissions are possible and payments must not double-charge

Expected output:
- Model: idempotent create-payment flow keyed by an external payment token
- Contract: validation for token, amount, and currency, with conflict handling on reuse
- Data notes: unique constraint on the idempotency key and a transaction around payment state update

## Guardrails

- Do not skip modeling and jump into code when the contract is still unstable
- Do not hide data-loss or consistency tradeoffs behind vague phrases like "handle it in code"
- Do not place business rules in the database if they need to be testable in the service layer

## Optional Tools / Resources

- Existing API specs or service docs
- Database schema and migration history
- Product requirements or incident notes
- GitHub, if repo conventions or prior implementations need to be checked

