---
name: harmonize
description: Align terminology, tone, and copy patterns across a flow so the product sounds consistent from screen to screen and state to state.
activation_hints:
  - "Use when the same concept is named or described inconsistently across a feature or flow."
  - "Route here for terminology normalization, tone alignment, and reusable message patterns."
  - "Do not use for single-string rewrites, naming a brand-new concept, or information hierarchy work."
---

# Harmonize

## Purpose

Use this skill to make a feature or flow sound coherent by standardizing terminology, tone, and repeated copy patterns across screens and states.

## When to Use

- When the same concept is named differently across screens, states, or components
- When tone changes abruptly between onboarding, default, success, and failure moments
- When a feature has been written incrementally and no longer feels like one coherent experience

## When Not to Use

- When only one local string needs rewriting and there is no broader consistency issue
- When the core task is selecting a durable new product name rather than aligning existing language
- When the main issue is screen organization or UX flow rather than language consistency

## Required Inputs

- The relevant screens, strings, or copy inventory for the flow
- The core concepts that repeat across the experience
- Any existing voice, tone, or terminology guidance
- User journey context so state-specific tone can be calibrated correctly
- Constraints such as localization, legal wording, or component reuse rules

## Workflow

1. Inventory the key strings across the full flow, including default, success, error, and empty states.
2. Identify repeated concepts, inconsistent labels, and moments where tone should intentionally shift.
3. Select the canonical term and preferred pattern for each recurring concept or message type.
4. Rewrite the affected copy so users encounter one coherent vocabulary and one consistent voice.
5. Document any deliberate tonal differences by context so future work follows the same logic.
6. Verify the final pass against the full journey, not isolated screens.

## Design Principles / Evaluation Criteria

- Terminology consistency for repeated concepts
- Tone coherence without flattening important context differences
- Reusable message patterns for buttons, helper text, and state messaging
- Clear differentiation between user-facing and internal language
- Future maintainability so teams can extend the pattern without guessing

## Output Contract

- A terminology map with preferred and rejected terms
- Standardized copy updates for the affected screens or states
- Short rationale for tone and pattern decisions that should be reused later

## Examples

### Example 1

Input:
- Flow uses "workspace," "project," and "team space" for the same object
- Screens include onboarding, settings, and invite flows

Expected output:
- Preferred term: "workspace"
- Rewritten strings across the flow using the same term
- Pattern note: Use calm, direct tone in settings and more encouraging tone in onboarding

## Guardrails

- Do not standardize terms without checking whether they actually represent different concepts
- Do not erase context-specific tone differences that help users in high-stakes moments
- Do not create a new vocabulary system that conflicts with established product language without calling that out
- Do not review one screen in isolation when the problem spans the flow

## Optional Tools / Resources

- Flow screenshots or Figma frames
- Existing terminology glossary and voice guidance
- Prior release notes or support references showing language confusion
- Localization notes for preferred source strings
