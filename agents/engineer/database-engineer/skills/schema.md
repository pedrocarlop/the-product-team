---
name: schema
description: Design and review database schemas so tables, columns, constraints, and relationships stay correct, queryable, and evolvable.
activation_hints:
  - "Use when a task asks for a new table, column, relationship, constraint, or normalization change."
  - "Route here when schema shape, naming, nullability, or ownership needs to be defined or revised."
  - "Do not use for pure index tuning, migration rollout mechanics, or incident recovery."
---

# Schema

## Purpose

Use this skill to shape data models that are correct now and still maintainable as volume, consumers, and access patterns grow.

## When to Use

- When defining a new table or revising an existing one
- When choosing primary keys, foreign keys, nullability, defaults, or check constraints
- When deciding whether to normalize, denormalize, or split a table
- When documenting ownership, retention, or domain boundaries for a schema change

## When Not to Use

- When the only change is an index or a query plan improvement
- When the work is about deployment sequencing or backfill mechanics
- When the task is restoring service after a failed migration or broken database state

## Required Inputs

- The business object the schema must represent
- The main write and read queries the schema must support
- Data volume, growth expectations, and tenant or partitioning needs
- Constraints around nullability, retention, auditability, and compatibility
- Any existing schema that must remain interoperable during rollout

## Workflow

1. Identify the domain entity and the decisions the database must enforce.
2. Map the access patterns before choosing table shape or key strategy.
3. Prefer explicit constraints over application-only assumptions.
4. Choose names, types, and nullability to match long-term usage, not just the first release.
5. Validate that the design supports migrations, backfills, and future change without unnecessary lock risk.
6. Record any non-default choice that future engineers will need to understand.

## Design Principles / Evaluation Criteria

- Correctness first, then evolvability
- Constraints should encode invariants the application should not be trusted to enforce alone
- Names should be stable, descriptive, and consistent with the existing catalog
- Schemas should make common reads easy and dangerous writes difficult
- Every exception to the default model should have a reason

## Output Contract

- Proposed table and column definitions
- Constraint, relationship, and default recommendations
- Naming and nullability decisions with rationale
- Any schema risks, compatibility concerns, or rollout dependencies

## Examples

### Example 1

Input:
- New concept: customer billing address
- Needs: historical auditability and future country-specific rules

Expected output:
- A separate address table with stable keys, explicit foreign keys, and nullable fields only where the domain requires them
- A note that normalization is preferred until query patterns justify denormalization

## Guardrails

- Do not hide data integrity requirements behind application logic alone
- Do not choose types or names that will be difficult to migrate later
- Do not optimize for hypothetical complexity that no query pattern supports

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Sentry MCP
- Websites: [PostgreSQL Docs](https://www.postgresql.org/docs/), [MySQL Reference Manual](https://dev.mysql.com/doc/), [MongoDB Docs](https://www.mongodb.com/docs/), [Redis Docs](https://redis.io/docs/latest/), [Use The Index, Luke!](https://use-the-index-luke.com/)
- Existing schema docs and migration history
- Query plans, explain output, and performance notes
- Downstream service contracts or data-access patterns
