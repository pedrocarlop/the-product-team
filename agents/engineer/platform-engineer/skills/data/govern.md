---
name: govern
description: Define and enforce data governance for privacy, access, retention, lineage, quality controls, and auditability.
---

# Govern

## Purpose

Use this skill to make data safe to use and easy to audit by defining how sensitive data is classified, protected, retained, deleted, and monitored.

## When to Use

- When data contains PII, sensitive business data, or regulated fields
- When access controls, masking, or row-level and column-level restrictions are needed
- When retention, deletion, or anonymization rules must be implemented
- When documenting lineage, ownership, and audit evidence

## When Not to Use

- When the work is just source ingestion or transformation implementation
- When the main need is schedule design or retry tuning
- When the task is a normal modeling request without governance implications

## Required Inputs

- Data classification and sensitivity level
- Applicable policy, regulatory, or contractual constraints
- Who needs access and why
- Retention, deletion, and anonymization requirements
- Audit or evidence expectations
- Relevant source, model, and consumption layers

## Workflow

1. Classify the data and identify which fields need protection.
2. Define the minimum necessary access model for each role or consumer.
3. Apply metadata tags, masking, and warehouse-level controls where appropriate.
4. Document retention and deletion behavior so it can be executed and audited.
5. Confirm lineage from source to consumer so sensitive data flows are visible.
6. Add quality and freshness checks for governed datasets.
7. Record the governance decision and evidence in a durable system of record.

## Design Principles / Evaluation Criteria

- Least privilege by default
- Governance must be enforceable, not just documented
- Sensitive fields should be discoverable in metadata
- Retention and deletion should be operational, not manual
- Auditability matters as much as protection

## Output Contract

- Classification and control recommendations
- Access, masking, and retention policy notes
- Deletion or anonymization procedure
- Audit or evidence checklist
- Documentation updates for affected datasets

## Examples

### Example 1

Input:
- Dataset: Customer support exports with email, phone, and ticket text
- Need: Restrict access and define retention

Expected output:
- Recommendation: Tag sensitive fields, limit access to approved roles, define a retention schedule, and document a deletion path for expired records
- Rationale: Reduces exposure while keeping the dataset operationally usable

## Guardrails

- Do not rely on informal agreements for sensitive data access
- Do not treat retention as a one-time cleanup task
- Do not hide PII in undocumented derived tables
- Do not leave audit trails to ad hoc manual notes

## Optional Tools / Resources

- Data classification policy
- Access-control settings and audit logs
- Retention or deletion runbooks
- Lineage and catalog metadata

