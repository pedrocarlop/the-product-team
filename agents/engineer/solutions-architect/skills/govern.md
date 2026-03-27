---
name: govern
description: Set architecture standards, review paths, exception handling, and decision records that keep solutions safe, consistent, and supportable.
activation_hints:
  - "Use when architecture needs policy, review, ownership, or exception handling."
  - "Route here for standards, governance, architecture reviews, and guardrails."
  - "Do not use for one-off design choices, option comparison, or system wiring."
---

# Govern

## Purpose

Use this skill to define how architectural decisions are approved, recorded, enforced, and changed over time.

## When to Use

- When a solution needs standards or guardrails
- When decision rights, review paths, or escalation rules are unclear
- When exceptions need to be controlled and traceable
- When architecture changes should be documented as durable records

## When Not to Use

- When the task is mainly decomposing the problem
- When the task is choosing among options
- When the task is primarily integration design or rollout sequencing

## Required Inputs

- The architecture area that needs governance
- The people who own, review, and approve decisions
- The standards, policies, or controls that should apply
- The risks and failure modes the governance should address
- The review cadence or enforcement mechanism

## Workflow

1. Define the scope of the governed architectural area.
2. Write the smallest standard that makes the decision repeatable and safe.
3. Assign ownership, approval rights, and escalation paths.
4. Define how exceptions are requested, reviewed, approved, and tracked.
5. State how the standard is enforced and how drift is detected.
6. Record the decision in a durable system so future teams can reuse it.

## Design Principles / Evaluation Criteria

- Governance should make good decisions easier
- Every standard needs an owner and a review path
- Exceptions must be explicit and time-bound
- Standards should be simple enough to apply in practice
- Durable records matter as much as the rule itself

## Output Contract

- Governance standard or policy summary
- Decision rights and approval path
- Exception handling and escalation notes
- Enforcement or review cadence
- Decision record or ADR guidance

## Examples

### Example 1

Input:
- Need: standardize which cloud services are approved for production
- Risk: teams are making inconsistent choices across projects

Expected output:
- Governance: approved service list, review authority, exception process, and annual review cadence
- Rationale: reduces drift and keeps architecture decisions auditable

## Guardrails

- Do not create policy without ownership
- Do not let exceptions become the hidden standard
- Do not overcomplicate governance for a small decision
- Do not confuse documentation with enforcement

## Optional Tools / Resources

- Decision logs and ADRs
- Review checklists and approval workflows
- Standards repositories or policy docs
- Incident follow-up records
