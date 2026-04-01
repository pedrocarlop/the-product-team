---
name: orient
description: Create onboarding and in-context guidance that helps users understand the value, next step, and safest path to progress without overexplaining.
---

# Orient

## Purpose

Use this skill to write onboarding and in-context guidance that helps users start confidently, reach value quickly, and learn only what they need right now.

## When to Use

- When a flow needs onboarding, setup guidance, or first-run messaging
- When users need lightweight education before they can take meaningful action
- When current guidance explains the product at length but still leaves users unsure how to begin

## When Not to Use

- When the task is primarily rewriting error, confirmation, or recovery states
- When the problem is naming, terminology, or cross-flow consistency
- When the main issue is structural complexity that needs UX redesign rather than instructional copy

## Required Inputs

- User type, starting knowledge, and target first success moment
- Flow stage where guidance appears such as onboarding, setup, empty, or blocked state
- Product behavior, prerequisites, and any irreversible or risky actions
- Existing components or patterns available for teaching in context
- Constraints such as step count, screen size, tone, and localization

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

1. Define the first meaningful outcome the user should reach.
2. Identify what the user must know before acting versus what can be taught later.
3. Write guidance that supports the next useful action rather than explaining the whole product.
4. Use headings, helper text, empty states, and contextual prompts to teach in place.
5. Remove reassurance, feature tours, or background information that delays action without reducing risk.
6. Check whether experienced users can move forward without being slowed down unnecessarily.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Value before feature explanation
- Progressive disclosure instead of front-loaded instruction
- Low anxiety and clear next-step guidance
- Respect for user momentum and existing knowledge
- Contextual teaching over generic tours
- Coverage of first-time, blocked, and empty moments

## Output Contract

- Onboarding or setup copy tied to the first meaningful user outcome
- Contextual guidance patterns for empty, blocked, or first-time moments
- Suggested sequence for what to explain now, later, or only on demand

## Examples

### Example 1

Input:
- New analytics dashboard for first-time team admins
- Users must connect one data source before seeing value
- Current empty state explains every dashboard module in detail

Expected output:
- Empty-state heading focused on the first outcome
- One short explanation of why connecting a source matters
- CTA and helper text guiding the user to the next safe step

## Guardrails

- Do not overload onboarding with every feature or edge case
- Do not use generic reassurance that does not help the user act
- Do not block experienced users without a clear reason
- Do not write teaching copy that contradicts the actual setup flow

## Optional Tools / Resources

- Activation metrics or drop-off notes
- Product walkthroughs, mocks, or screenshots
- Research notes about first-run confusion
- Existing empty-state or onboarding patterns in the design system
