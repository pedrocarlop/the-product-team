---
name: tune
description: Refine conversational tone, response style, and voice calibration so the assistant sounds appropriate, useful, and consistent.
activation_hints:
  - "Use when the conversation is structurally correct but the wording, tone, or response style needs refinement."
  - "Route here for voice calibration, emotional temperature, brevity, and personality consistency."
  - "Do not use for scope definition, script structure, or fallback design unless the issue is tone-specific."
---

# Tune

## Purpose

Use this skill to refine how the assistant sounds so its responses match the product context, user needs, and trust expectations.

## When to Use

- When the script works but the voice feels too formal, too casual, or inconsistent
- When response length, warmth, or confidence needs adjustment
- When different states need different tonal treatment, such as errors versus confirmations

## When Not to Use

- When the core issue is what the assistant should handle
- When the dialogue structure itself is incomplete
- When the main problem is recovery behavior rather than wording

## Required Inputs

- The current script or response draft
- The target audience and emotional context
- Any voice or brand guidance already established
- State-specific needs such as error, success, or sensitive-topic tone
- Constraints on length, formatting, or channel behavior

## Workflow

1. Read the response in context and identify the tone the moment requires.
2. Compare the draft against the intended voice and emotional temperature.
3. Remove unnecessary hedging, filler, or stylistic noise.
4. Adjust sentence length, directness, and warmth to fit the use case.
5. Check neighboring responses for consistency across the flow.
6. Verify that the final wording still matches the assistant's actual behavior.

## Design Principles / Evaluation Criteria

- Tone should fit the user's moment, not just the brand
- Clarity should survive any style change
- Confidence should not become overclaiming
- Brevity should not remove needed guidance
- Voice should feel consistent across turns and states

## Output Contract

- Revised response text or tone guidance
- Notes on any state-specific tonal shifts
- Short rationale for changes that affect trust or user comfort

## Examples

### Example 1

Input:
- Draft: "I'm sorry for any inconvenience. Please retry later."
- Context: System timeout during checkout support

Expected output:
- "Something went wrong while we loaded that. Please try again in a moment."
- Rationale: Shorter, clearer, and more direct for a recovery moment

## Guardrails

- Do not change the meaning while tuning the tone
- Do not add marketing language to operational copy
- Do not make failure responses sound euphemistic or evasive
- Do not tune in isolation from the actual flow behavior

## Optional Tools / Resources

- Existing voice guidelines or brand notes
- `search-query` for comparable voice patterns
- `apply-patch` for updating the authored conversation artifact

