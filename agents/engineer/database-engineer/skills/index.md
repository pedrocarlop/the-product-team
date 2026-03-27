---
name: index
description: Choose and validate database indexes that improve the right queries without introducing unnecessary write overhead or maintenance risk.
activation_hints:
  - "Use when a query is slow and the answer may be an index, partial index, covering index, or index removal."
  - "Route here when index strategy, planner behavior, or index bloat is part of the task."
  - "Do not use for schema modeling, migration sequencing, or disaster recovery work."
---

# Index

## Purpose

Use this skill to build or revise indexes that serve measured query patterns and keep write costs under control.

## When to Use

- When a query needs acceleration and the access pattern is known
- When deciding between B-tree, GIN, partial, or composite indexes
- When removing unused indexes or consolidating overlapping ones
- When verifying whether the planner is actually using an index

## When Not to Use

- When the problem is primarily table structure or normalization
- When the change needs rollout choreography or backfill coordination
- When the issue is a failed migration or blocked production recovery

## Required Inputs

- The exact query or query family to optimize
- Table size, cardinality, and selectivity information
- Current execution plan or latency symptoms
- Insert and update frequency for the table
- Any operational constraints such as online creation requirements

## Workflow

1. Identify the slow or expensive query and the predicates it actually uses.
2. Check whether an existing index already serves the access path.
3. Choose the smallest index shape that satisfies the query pattern.
4. Prefer partial or composite indexes only when the filter shape is stable and specific.
5. Validate the plan and compare read gains against write and storage costs.
6. Remove or avoid indexes that do not show a clear workload benefit.

## Design Principles / Evaluation Criteria

- Indexes should exist for observed queries, not imagined ones
- Smaller, targeted indexes are usually easier to maintain than broad catch-alls
- Every new index has a write amplification cost
- Planner confirmation matters as much as the index definition itself
- Unused indexes are technical debt, not harmless metadata

## Output Contract

- Recommended index definition or removal
- The query pattern the index supports
- Expected planner impact and tradeoffs
- Any follow-up validation needed after deployment

## Examples

### Example 1

Input:
- Query: recent active orders by customer
- Pattern: `WHERE customer_id = ? AND deleted_at IS NULL ORDER BY created_at DESC`

Expected output:
- A composite or partial index tailored to the exact filter and sort shape
- A note explaining why a general-purpose index would be broader than necessary

## Guardrails

- Do not create indexes without a matching workload
- Do not assume more indexes always mean faster reads
- Do not forget to account for write-heavy tables and online creation requirements

