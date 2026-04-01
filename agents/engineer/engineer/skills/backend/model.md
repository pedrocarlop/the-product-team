---
name: model
description: "Shape backend work into explicit domain, data, and contract decisions before implementation starts. Use when building a new API endpoint, designing a database schema, or defining a business process handler."
---

# Model

## Overview

"Model" defines the core logic, resources, and rules that govern a backend system. A good model separates the abstract "business rules" (Invariants) from the "persistence layer" (Database) and the "delivery contract" (API). Without modeling, code often becomes a collection of ad-hoc scripts that fight each other for state control.

## When to Use

- When a new business capability needs a stable API or service interface.
- When existing logic is "leaky" or hard to test due to complex dependencies.
- When changing a database schema, transaction boundary, or caching strategy.
- When building an idempotent handler for asynchronous operations.

## When Not to Use

- When the task is a simple bug fix (e.g., incorrect string formatting) with no logic changes.
- When the work is purely administrative (e.g., updating a dependency version).
- When the problem is only about rollout (e.g., a feature flag or CI/CD tweak).

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: engineer
project: <slug>
deliverable: engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

### Step 2: Define Actors and Resources

Identify the "Who" and the "What":
- **Actors**: Users, system tasks, external webhooks (e.g., "Workspace Admin", "Billing Service").
- **Resources**: The entities that change state (e.g., "Invoice", "TeamMember", "Workspace").

### Step 3: Establish Domain Invariants

Specify the rules that must **never** be violated, regardless of how the data is stored or accessed:
- "An invoice cannot be paid twice." (Idempotency)
- "A team must have exactly one owner." (Cardinality)
- "A user cannot join a workspace without a valid invite." (Authorization)

### Step 4: Draw state transitions

For every resource, map its lifecycle:
- `Initialized` → `Pending` → `Active` → `Archived`
- Define the **triggers** (User Action vs. System Timeout) and the **conditions** (Balance > 0) that cause a transition.

### Step 5: Define the API Contract (Delivery)

Specify how the outside world interacts with the model:
- **Request**: URL, Verb (POST/PUT/GET), Payload fields, Types, and mandatory/optional flags.
- **Response**: Success payload, Status codes (200/201/204), and **structured Error objects**.

### Step 6: Design the Persistence Strategy (Database)

Decide how the model is stored:
- **Relational (SQL)**: Tables, columns, foreign keys, indexes, and migrations.
- **Transaction Boundaries**: Which operations must succeed or fail together?
- **Concurrency**: How do we handle race conditions? (e.g., Optimistic Locking / Transaction Isolation).

### Step 7: Identify External Dependencies and Side Effects

List everything the model depends on or affects:
- **Inputs**: Third-party APIs (Stripe, Slack), other services.
- **Side Effects**: Emails sent, webhooks fired, background jobs enqueued.

### Step 8: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Decision Tree: Is the model "stable"?

```
Is the Data Schema decoupled from the API Contract?
├── YES → Can you change a database column name without breaking the API?
│   ├── YES → OK (Stable).
│   └── NO → Redraw the mapping layer.
└── NO → High risk of "Leaky Model." Add a DTO (Data Transfer Object) layer.
```

## Worked Examples

### Example 1: Invoice Payment Handler

**Input:** Endpoint to process a customer payment.
**Model:**
- **Resource**: `PaymentTransaction` (Pending → Succeeded/Failed).
- **Invariants**: `idempotency_key` must be unique to prevent double-charging.
- **Contract**: `POST /payments` { `amount`, `currency`, `card_token`, `payment_id` }.
- **Persistence**: `transactions` table with a `UNIQUE INDEX` on `payment_id + idempotency_key`.
- **Side Effect**: Update `Invoice` state to `PAID` via a background job after payment success.

### Example 2: Team Invite Creation

**Input:** Invite a user to a private workspace.
**Model:**
- **Resource**: `WorkspaceInvite` (Created → Sent → Accepted/Expired).
- **Invariants**: Invited email must not already be an active member. Workspace must not exceed member limit.
- **Contract**: `POST /invites` { `email`, `role` }.
- **Persistence**: `invites` table. Transaction includes: 1) Check member count, 2) Write invite record.
- **Side Effect**: Fire `SendInviteEmail` event.

## Guardrails

- **Never place business rules in the Database layer.** Rules belong in the Domain/Service layer for testability.
- **Always design for Idempotency.** Assume every request might be retried (Network loss, timeout).
- **Do not return raw Database objects in the API.** Use explicit DTOs to avoid leaking sensitive or internal fields.
- **Always define an "Error Shape."** 400 Errors should include a machine-readable code and a human-readable message.

## Troubleshooting

### Issue: The model is too "leaky" (API tied to DB)
**Cause**: Using the same objects for persistence and delivery.
**Solution**: Introduce a mapping layer. Translate DB rows into API Responses explicitly.

### Issue: Race conditions during state updates
**Cause**: No transaction boundaries or missing unique constraints.
**Solution**: Wrap the update in a database transaction. Use `SELECT FOR UPDATE` or optimistic versioning.

### Issue: Side effects failing silently
**Cause**: Sync processing of external calls without retry logic.
**Solution**: Move side effects to background queues (e.g., Bull, Sidekiq, Celery). Use transactional outboxes where possible.
