---
name: tune
description: Refine frontend tone, interaction wording, and response style so the surface feels appropriate, useful, and consistent.
---

# Tune

## Purpose

Use this skill to refine how the frontend speaks to users so the wording matches the product context, user need, and trust expectations.

## When to Use

- When the UI works but the tone feels too formal, too casual, or inconsistent
- When response length, warmth, or confidence needs adjustment
- When different states need different wording treatment, such as errors versus confirmations

## When Not to Use

- When the core issue is what the UI should do
- When the interaction structure itself is incomplete
- When the main problem is recovery behavior rather than wording

## Required Inputs

- The current copy, prompt, or response draft
- The target audience and emotional context
- Any voice or brand guidance already established
- State-specific needs such as error, success, or sensitive-topic tone
- Constraints on length, formatting, or channel behavior

## Workflow

1. Read the wording in context and identify the tone the moment requires.
2. Compare the draft against the intended voice and emotional temperature.
3. Remove unnecessary hedging, filler, or stylistic noise.
4. Adjust sentence length, directness, and warmth to fit the use case.
5. Check neighboring surfaces for consistency across the flow.
6. Verify that the final wording still matches the product behavior.

## Design Principles / Evaluation Criteria

- Tone should fit the user's moment, not just the brand
- Clarity should survive any style change
- Confidence should not become overclaiming
- Brevity should not remove needed guidance
- Voice should feel consistent across states

## Output Contract

- Revised response text or tone guidance
- Notes on any state-specific tonal shifts
- Short rationale for changes that affect trust or user comfort

## Examples

### Example 1

Input:
- Draft: "We're unable to process your request at this time."
- Context: timeout during a checkout or save action

Expected output:
- "Something went wrong while we saved that. Please try again in a moment."
- Rationale: shorter, clearer, and more direct for a recovery moment

## Guardrails

- Do not change the meaning while tuning the tone
- Do not add marketing language to operational copy
- Do not make failure responses sound euphemistic or evasive
- Do not tune in isolation from the actual flow behavior

## Optional Tools / Resources

- Existing voice guidelines or brand notes
- Screenshots or prototypes showing surrounding states
- Browser or product context for the affected flow
- `apply-patch` for updating the authored frontend artifact
