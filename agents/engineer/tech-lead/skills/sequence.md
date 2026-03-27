---
name: sequence
description: Break technical work into the right order, surface dependencies, and plan the safest path to delivery.
---

# Sequence

## Purpose

Use this skill to turn a technical initiative into a sensible order of work so dependencies, risks, and rollout constraints are visible before the team starts building.

## When to Use

- When a project needs a step-by-step implementation or migration plan
- When hidden dependencies or ordering constraints could block delivery
- When a change should be staged, rolled out, or phased across systems
- When a large task needs to be broken into smaller pieces for planning or sprinting

## When Not to Use

- When the decision itself is still unsettled
- When the task is a focused review rather than a plan
- When the work is small enough that sequencing adds no value

## Required Inputs

- The desired end state and target deadline, if any
- Known dependencies, teams, systems, or contracts involved
- Constraints on rollout, migration, testing, or reversibility
- The current baseline and what must remain working during the change
- Any milestones or checkpoints that should gate later work

## Workflow

1. Define the target outcome and identify the minimum safe path to get there.
2. List the dependencies, prerequisites, and irreversible steps.
3. Split the work into phases that reduce risk as early as possible.
4. Put validation, rollback, and communication steps in the sequence, not after it.
5. Call out what can happen in parallel and what must wait.
6. Confirm that the order still makes sense if one assumption changes.

## Design Principles / Evaluation Criteria

- Risk first, then speed
- Dependency visibility over hidden coupling
- Small, verifiable steps over one large leap
- Safe rollback and rollout paths
- Parallelize only where it does not create coordination debt

## Output Contract

- An ordered plan with clear phases or milestones
- Dependencies and prerequisites called out explicitly
- Any required validation, rollback, or checkpoint steps
- Notes on what can be parallelized safely

## Examples

### Example 1

Input:
- Goal: Replace a shared API contract
- Constraints: Multiple clients depend on it and migration must be gradual

Expected output:
- Plan: Introduce the new contract, dual-read or dual-write where needed, migrate clients in waves, verify behavior at each stage, then deprecate the old path.
- Rationale: The sequence reduces blast radius and preserves reversibility while adoption is in progress.

## Guardrails

- Do not assume ordering is obvious when dependencies exist
- Do not leave validation or rollback until the end of the plan
- Do not turn planning into a substitute for solving an architecture problem
- Do not over-plan trivial work

## Optional Tools / Resources

- Project plans or sprint boards
- Dependency maps
- Rollout and migration checklists
- Incident learnings from similar changes
