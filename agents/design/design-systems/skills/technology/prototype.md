---
name: prototype
description: Build or specify high-fidelity prototypes that exercise real interactions, state transitions, and logic so design decisions can be validated before full implementation.
---

# Prototype

## Purpose

Use this skill to create a prototype that feels close to production and proves whether the interaction model, layout, and logic actually hold up.

## When to Use

- When a design needs to be tested with realistic behavior or state changes
- When motion, navigation, or interaction logic needs to be demonstrated
- When stakeholders need something more trustworthy than a static concept

## When Not to Use

- When the task is to audit an existing implementation
- When the only goal is documentation or handoff
- When the surface already exists and needs verification rather than proof of concept

## Required Inputs

- The goal of the prototype and what decision it must support
- The target fidelity level and interaction depth
- Any source design, flow, or behavior reference
- The states, edge cases, or data inputs the prototype must exercise
- The platform or tooling constraints that shape what is feasible

## Workflow

1. Identify the decision the prototype needs to unlock.
2. Select only the parts of the experience that materially affect that decision.
3. Model the interaction states, transitions, and timing needed to make the behavior believable.
4. Include realistic data, failures, and empty states where they affect trust in the concept.
5. Keep the prototype focused on proving the idea rather than finishing every surface.
6. Verify the prototype communicates the intended behavior without introducing misleading polish.

## Design Principles / Evaluation Criteria

- Fidelity should serve the decision, not vanity
- Interactions must be believable enough to test the real idea
- Edge cases matter when they change the user's understanding
- Prototype scope should stay tight and purposeful
- The prototype should reduce ambiguity, not create a second product

## Output Contract

- A prototype plan or build description
- The key interactions, transitions, and states represented
- A note on what the prototype proves and what it intentionally omits
- Any technical or tooling constraints that affect interpretation

## Examples

### Example 1

Input:
- Concept: Inline bulk-edit workflow with optimistic updates
- Goal: Decide whether the interaction feels safe and fast enough

Expected output:
- Prototype the edit, save, undo, and failure states
- Use realistic row data and delayed responses
- Call out that the prototype omits permissions and audit logging

## Guardrails

- Do not overbuild a prototype past the point needed to answer the question
- Do not hide unresolved logic behind visual polish
- Do not let the prototype become a substitute for production implementation decisions

## Optional Tools / Resources

- Flow diagrams and task sequences
- Design system components and motion patterns
- Real sample data or anonymized production data
- Implementation notes from engineering
