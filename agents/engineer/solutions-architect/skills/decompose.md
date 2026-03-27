---
name: decompose
description: Break ambiguous business problems into architectural requirements, bounded decisions, dependencies, constraints, and risks.
---

# Decompose

## Purpose

Use this skill to turn a messy business request into a clear architectural problem statement that can be designed, compared, and reviewed.

## When to Use

- When the request spans multiple systems, teams, or constraints
- When requirements are incomplete, contradictory, or vague
- When success criteria, risks, or dependencies are not explicit
- When you need to separate functional needs from non-functional constraints

## When Not to Use

- When the architectural problem is already well bounded
- When the main task is comparing options or selecting a vendor
- When the work is primarily interface, contract, or migration design

## Required Inputs

- The business goal or request in plain language
- The stakeholders and operating teams involved
- Known constraints such as budget, timeline, compliance, and scale
- Existing systems, dependencies, and operational ownership
- Any current decision records, notes, or architecture artifacts

## Workflow

1. Restate the problem as a concrete architectural question.
2. Split the request into functional needs, non-functional needs, and constraints.
3. Identify the systems, teams, and workflows that are in scope and out of scope.
4. Surface assumptions, unknowns, dependencies, and risk areas.
5. Turn vague needs into decision-ready requirements with measurable thresholds where possible.
6. Produce a concise problem frame that can be handed to option selection or design work.

## Design Principles / Evaluation Criteria

- Good decomposition reduces ambiguity without overdesigning
- Requirements should be specific enough to validate later
- Constraints and assumptions must be visible, not hidden
- Scope boundaries should be explicit
- Risks are part of the problem definition, not an afterthought

## Output Contract

- Problem statement and scope boundary
- Functional and non-functional requirement list
- Assumptions, unknowns, and open questions
- Dependency and risk map
- Decision-ready summary for the next workflow step

## Examples

### Example 1

Input:
- Request: "We need a new partner integration for enterprise customers"
- Context: Sales wants it in one quarter, security review is required

Expected output:
- Decomposition: partner onboarding flow, auth and provisioning, data sync, security review, and rollout sequencing
- Risks: unclear partner API quality, ownership of support, compliance scope

## Guardrails

- Do not jump to a solution before the problem is framed
- Do not hide uncertainty behind broad statements
- Do not treat assumptions as settled requirements
- Do not carry analysis beyond the point where design work can begin

## Optional Tools / Resources

- Requirements docs or intake notes
- Stakeholder interview notes
- Existing architecture diagrams
- Decision logs and incident history
