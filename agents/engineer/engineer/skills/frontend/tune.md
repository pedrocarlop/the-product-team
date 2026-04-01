---
name: tune
description: Refine frontend microcopy, UI feedback wording, and state-specific messaging so the product surface communicates clearly, consistently, and proportionally to the user's context.
---

# Tune

## Purpose

Use this skill to refine the words a frontend surface uses to communicate with users so that labels, feedback messages, error text, and instructional copy are clear, consistent, and correctly calibrated for each UI state.

## When to Use

- When the UI works functionally but the copy feels too formal, too casual, or mismatched to the moment
- When error messages, success confirmations, empty states, or tooltip text need wording improvement
- When different UI states use inconsistent voice or conflicting levels of formality
- When a component's microcopy needs to match the design system's content guidelines

## When Not to Use

- When the core issue is what the UI should do, not what it says
- When the interaction structure or component logic is incomplete
- When the main problem is visual design, layout, or component behavior rather than wording

## Required Inputs

- The current UI copy in context: labels, button text, feedback messages, tooltips, empty states
- Screenshots or component specs showing where the copy appears
- The design system's content or voice guidelines, if they exist
- State-specific requirements: what the UI says during loading, error, success, empty, disabled
- Constraints on text length, truncation behavior, localization, or responsive breakpoints

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: engineer
project: <slug>
deliverable: engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Read each piece of copy in its visual and interaction context, not in isolation.
2. Check whether the wording matches the action the UI is performing and the state it is in.
3. Remove unnecessary filler, passive voice, and hedging that add length without adding meaning.
4. Adjust formality, directness, and specificity to fit the component type and user moment.
5. Verify consistency across related surfaces: does the same action use the same verb everywhere?
6. Confirm that the final copy fits the available space and does not break layout at edge lengths.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Copy should describe what happened and what to do next, not just what went wrong
- Labels should be scannable and unambiguous at a glance
- Consistency across components matters more than individual cleverness
- Error text must be specific enough to guide recovery
- Brevity must not sacrifice the information the user needs to proceed
- Microcopy should work for the longest realistic content, not just the demo string

## Output Contract

- Revised UI copy organized by component or screen area
- Notes on state-specific wording changes and the rationale for each
- Flagged inconsistencies across related surfaces that need alignment
- Length or truncation concerns for edge-case content

## Examples

### Example 1

Input:
- Draft: "We're unable to process your request at this time."
- Context: Timeout error during a save action on a form

Expected output:
- "Your changes could not be saved. Please try again."
- Rationale: Names the specific action that failed and gives a clear next step

### Example 2

Input:
- Draft: "No results" (empty state in a search component)
- Context: User searched for a term with no matches

Expected output:
- "No results for '[query]'. Try a different search term."
- Rationale: Reflects the user's input back and suggests a recovery action

## Guardrails

- Do not change the meaning of UI feedback while tuning the wording
- Do not add marketing or promotional language to operational UI copy
- Do not make error messages sound euphemistic or hide what actually happened
- Do not tune copy without checking how it renders in the actual component at various lengths
- Do not introduce inconsistency by tuning one surface without checking related surfaces

## Optional Tools / Resources

- Design system content guidelines or voice documentation
- Screenshots or prototypes showing the copy in context
- Browser dev tools for checking rendered text at various widths
- `apply-patch` for updating the frontend copy artifact
