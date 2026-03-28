---
name: extract
description: Identify reusable components, tokens, and patterns and promote them into the design system with clear ownership, structure, and migration intent.
---

# Extract

Use this skill to turn repeated UI decisions into system assets instead of letting them remain scattered across feature work.

## When to Use

- When similar components or patterns appear in multiple places
- When hard-coded values or custom variants are creating drift
- When a feature has revealed a reusable design-system gap worth formalizing

## How to Use

Audit the target area for repetition, inconsistency, and hidden token usage. Decide whether each opportunity is best expressed as a component, variant, pattern, or token update. Extraction should reduce entropy, not create a library full of one-off abstractions.

Define the reusable asset with system discipline: naming, anatomy, variants, state coverage, token dependencies, accessibility expectations, and adoption path. If the proposed asset does not clearly improve reuse or consistency, do not extract it.

## What to Produce

- A list of reusable components, variants, patterns, or tokens to add or revise
- The rationale for why each item belongs in the system
- Proposed naming, scope, and migration guidance for adopters

## Notes for Design Systems Designer

Extract only what has clear systemic value. A weak abstraction multiplies confusion faster than a missing component does.
