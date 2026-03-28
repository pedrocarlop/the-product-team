---
name: model
description: Design warehouse and transformation models that produce correct, documented, testable, and analysis-ready datasets.
---

# Model

## Purpose

Use this skill to turn raw data into trustworthy analytical structures with clear grain, stable naming, documented logic, and tests that catch bad data before it reaches users.

## When to Use

- When designing staging, intermediate, or mart models
- When defining metrics, grains, dimensions, or facts
- When changing warehouse schema or transformation logic
- When adding dbt tests, model docs, or lineage-aware migrations

## When Not to Use

- When the work is only about loading source data into landing tables
- When the main need is schedule coordination or retry behavior
- When the request is about access policy, retention, or privacy controls

## Required Inputs

- Source tables or landing datasets
- Target consumer and use case
- Required grain, metric definitions, and business rules
- Existing naming conventions and layer boundaries
- Downstream dependencies and compatibility constraints
- Performance or cost constraints

## Workflow

1. Define the grain before writing any transformation logic.
2. Choose the correct layer for each rule: staging for structural cleanup, intermediate for business logic, mart for consumer-facing outputs.
3. Keep transformation models deterministic, documented, and easy to test.
4. Add primary-key, not-null, uniqueness, and referential checks where they matter.
5. Trace lineage to understand every downstream dependency before changing a field or contract.
6. Review query patterns and materialization choices to avoid unnecessary warehouse cost.
7. Document any schema change with impact, backfill, and rollback notes.

## Design Principles / Evaluation Criteria

- One clear grain per model
- Business logic belongs in testable transformation layers
- Consumer-facing marts should not depend directly on raw sources
- Documentation and tests are part of the model, not optional extras
- Schema changes should be backward-compatible whenever possible

## Output Contract

- Model architecture or dbt file changes
- Documented grain, columns, and business rules
- Relevant tests and descriptions
- Lineage or migration notes for affected downstream assets
- Performance or materialization recommendation

## Examples

### Example 1

Input:
- Need: Monthly revenue mart for finance
- Sources: Orders, refunds, customer accounts
- Concern: Different tables have conflicting row grains

Expected output:
- Recommendation: Build staged source-aligned models, an intermediate revenue consolidation model, and a mart with one row per month per account
- Rationale: Separates cleanup, logic, and reporting grain so the mart is testable and stable

## Guardrails

- Do not hide business logic in staging models
- Do not change mart contracts without checking lineage and downstream usage
- Do not skip tests because the source is "trusted"
- Do not materialize large models full-refresh by default when incremental would be safer

## Optional Tools / Resources

- dbt project files and docs
- Warehouse explain plans and job history
- Data dictionary or metric definitions
- Downstream dashboard and product dependencies

