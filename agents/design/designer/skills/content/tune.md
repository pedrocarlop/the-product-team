---
name: tune
description: Refine conversational voice, response calibration, and dialogue tone so the assistant sounds trustworthy, context-appropriate, and emotionally attuned across turns and states.
---

# Tune

## Purpose

Use this skill to refine how a conversational assistant sounds so its responses match the user's emotional context, the product's trust requirements, and the voice guidelines across every dialogue state.

## When to Use

- When the dialogue script works functionally but the voice feels wrong for the moment
- When different conversational states need distinct tonal treatment: errors, confirmations, sensitive topics, escalations
- When response length, warmth, confidence calibration, or hedging needs adjustment
- When the assistant's voice drifts across turns and needs consistency enforcement

## When Not to Use

- When the core problem is what the assistant should handle or its capabilities scope
- When the dialogue structure itself is incomplete or the turn logic is broken
- When the main issue is fallback or recovery behavior rather than wording and voice

## Required Inputs

- The current script, prompt template, or response draft in context
- The target audience, emotional moment, and trust level required
- Voice guidelines, brand tone documentation, or personality spec
- State-specific requirements: error tone, success tone, escalation tone, sensitive-topic tone
- Constraints on response length, formatting, channel behavior, or platform norms
- Adjacent turns or dialogue context that the response must feel consistent with

## Workflow

1. Read the response in its full conversational context and identify the emotional temperature the moment demands.
2. Compare the draft against the voice spec and flag where tone, confidence, or register mismatches.
3. Strip unnecessary hedging, filler phrases, and stylistic noise that dilute trust or clarity.
4. Calibrate sentence length, directness, warmth, and formality to the specific state and user moment.
5. Check consistency across neighboring turns so the voice does not shift abruptly within a dialogue.
6. Verify that the tuned wording still accurately describes what the assistant can and will do.

## Design Principles / Evaluation Criteria

- Tone must serve the user's moment, not just the brand personality
- Clarity must survive any style change; tuning should never obscure meaning
- Confidence calibration matters: do not overclaim or understate capability
- Brevity must not sacrifice needed guidance or reassurance
- Voice consistency across turns and states builds trust; inconsistency erodes it
- Error and recovery moments deserve more tonal care, not less

## Output Contract

- Revised dialogue text or response variants with tone annotations
- Notes on state-specific tonal shifts and the rationale behind each
- A short rationale for changes that affect user trust, comfort, or perceived competence
- Flagged areas where the voice spec may need updating based on tuning discoveries

## Examples

### Example 1

Input:
- Draft: "I'm sorry for any inconvenience. Please retry later."
- Context: System timeout during active checkout support conversation

Expected output:
- "Something went wrong while we loaded that. Please try again in a moment."
- Rationale: Removes corporate apology template; shorter, clearer, and more direct for a recovery moment where the user needs to act

### Example 2

Input:
- Draft: "I can help you with that! Let me look into it right away!"
- Context: User reporting a billing discrepancy, frustrated tone

Expected output:
- "Let me check your billing details now."
- Rationale: Drops forced enthusiasm that misreads the emotional moment; matches the user's need for competent, calm resolution

## Guardrails

- Do not change the meaning or capability claims while tuning the tone
- Do not add marketing language to operational or support copy
- Do not make failure responses sound euphemistic, evasive, or dismissive
- Do not tune individual responses in isolation from the surrounding dialogue flow
- Do not let voice personality override functional clarity

## Optional Tools / Resources

- Existing voice guidelines, personality spec, or brand tone documentation
- `search-query` for comparable voice patterns across the dialogue corpus
- `apply-patch` for updating the authored conversation artifact
- Dialogue flow diagrams showing where the response sits in the turn sequence
