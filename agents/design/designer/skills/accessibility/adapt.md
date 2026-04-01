---
name: adapt
description: Adapt designs, patterns, and interactions so they work for keyboard users, screen reader users, and people with low vision, motion sensitivity, or cognitive load constraints.
---

# Adapt

## Purpose

Use this skill to change a design or interaction model so accessibility constraints are built into the experience instead of layered on afterward.

## When to Use

- When the current layout or interaction pattern excludes some users
- When a component needs a more accessible pattern than the one originally chosen
- When contrast, focus visibility, text size, motion, or structure needs to be redesigned
- When the interface needs to better support assistive technologies without losing product intent

## When Not to Use

- When the issue is only to document an existing decision
- When the task is to inspect for defects without changing the design
- When the implementation already exists and only verification is needed

## Required Inputs

- The original design, flow, or component
- The accessibility barrier that must be addressed
- The user task and the context in which the barrier appears
- Any product or design constraints that must be preserved
- Relevant design system components or patterns available for reuse

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

1. Identify the minimum change needed to remove the barrier without breaking the product goal.
2. Prefer established accessible patterns over custom interaction design.
3. Adjust structure, spacing, hierarchy, or affordance so the interaction is perceivable and operable.
4. Ensure states such as hover, focus, disabled, error, and loading remain accessible.
5. Recheck the design across responsive states, localization, and motion preferences.
6. Capture the updated accessibility requirements so the fix can be implemented consistently.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Accessibility improvements should preserve task clarity and product intent
- Changes should reduce reliance on memory, precision, or hidden affordances
- The adapted design should be robust across input modes and assistive technologies
- A good adaptation avoids introducing new barriers while fixing the old one

## Output Contract

- Revised design direction or interaction model
- Explanation of the accessibility barrier being removed
- Any tradeoffs introduced by the adaptation
- Notes needed for implementation or follow-up verification

## Examples

### Example 1

Input:
- Current design: Icon-only action buttons in a table row
- Barrier: Screen reader users cannot distinguish actions reliably

Expected output:
- Adaptation: Add visible labels where space allows or provide accessible names and predictable grouping
- Rationale: The action set remains usable with keyboard and assistive technology

## Guardrails

- Do not preserve inaccessible patterns just because they look familiar
- Do not fix one barrier in a way that creates another, such as a focus trap or poor contrast
- Do not assume a visual change is enough if keyboard or screen reader behavior is still unclear
- Do not introduce motion or complexity when a simpler pattern works better

## Optional Tools / Resources

- Design system components and tokens
- Figma prototype testing
- Contrast and typography checks
- Keyboard and screen reader notes from audits
