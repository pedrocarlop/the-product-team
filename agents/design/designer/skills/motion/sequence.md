---
name: sequence
description: Plan ordered motion across multiple elements so timing, hierarchy, and attention flow feel deliberate.
---

# Sequence

## Purpose

Use this skill to choreograph motion across multiple elements so the user can follow the intended order without cognitive overload.

## When to Use

- When several items enter, exit, or update together
- When attention should move from the primary element to supporting elements
- When the product needs a structured reveal, cascade, or step-by-step handoff

## When Not to Use

- When one element can communicate the whole change on its own
- When simultaneous motion would be clearer than a staged sequence
- When the user is already under load and extra choreography would slow them down

## Required Inputs

- The full set of elements involved in the sequence
- The intended attention order
- The trigger and completion condition
- The maximum acceptable total duration
- Any interruption, cancellation, or reverse path
- Reduced-motion behavior for the same interaction

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: designer
project: <slug>
deliverable: designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Rank the elements by importance.
2. Decide what should start first, what should follow, and what can happen in parallel.
3. Assign offsets so the sequence feels intentional rather than random.
4. Keep the total motion budget short enough to preserve task momentum.
5. Check the sequence from the user's perspective, not the animator's.
6. Define interruption, reverse, and cancellation behavior so the sequence does not break under real use.
7. Define the reduced-motion version so the order still reads clearly.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- One primary focus at a time
- Ordered motion that mirrors the user's reading path or task path
- Short, readable offsets instead of arbitrary delays
- Parallel motion only when it reduces clutter
- Clear completion state at the end of the sequence

## Output Contract

- A sequence map listing the ordered steps, affected elements, offsets, and completion conditions
- Timing and easing guidance for each step, including what runs in parallel and what must wait
- Reverse, interruption, and cancellation behavior where relevant
- Reduced-motion fallback that keeps the order understandable

## Examples

### Example 1

Input:
- Sequence: Empty state to populated dashboard
- Elements: Header, cards, chart, footer note

Expected output:
- Header fades and settles first.
- Cards appear in a 40ms stagger from left to right.
- Chart animates after the cards begin, not before.
- Footer note appears last and quietly.

## Guardrails

- Do not make every item equally important
- Do not let stagger durations become long enough to feel slow
- Do not use sequence to hide poor hierarchy
- Do not ignore the reverse or cancellation path
- Do not describe a cascade without saying which elements move at each step

## Optional Tools / Resources

- Figma prototypes
- Storyboards or frame-by-frame sketches
- Motion system timing tokens
- Screen recordings for attention flow review
