---
name: clarify
description: Rewrite confusing labels, instructions, errors, and other interface copy so users understand what happened and what to do next.
activation_hints:
  - "Use when interface copy is vague, jargon-heavy, ambiguous, or hard to act on."
  - "Route here for labels, helper text, instructions, CTA text, and state messaging that need clearer wording."
  - "Do not use for naming strategy, content hierarchy redesign, or cross-flow terminology systems work."
---

# Clarify

## Purpose

Use this skill to rewrite interface copy so users can understand the message quickly, trust what it means, and know what to do next.

## When to Use

- When labels, CTA text, helper text, or instructions are hard to understand
- When error, loading, success, or empty-state copy does not guide the user clearly
- When terminology drift is making the interface feel inconsistent

## When Not to Use

- When the main problem is screen structure, grouping, or hierarchy rather than sentence clarity
- When the task is choosing durable product names across multiple surfaces
- When the copy problem is primarily a full-flow consistency issue rather than a local rewrite

## Required Inputs

- The exact source strings or the surface where they appear
- User goal and task moment for each string
- Platform or surface constraints such as button width, truncation, or localization sensitivity
- Relevant product terminology, business rules, or prohibited language
- Any screenshots, mocks, or flow context needed to interpret the copy in place

## Workflow

1. Identify what the user needs to understand, decide, or do at this moment.
2. Read the copy in context, including the surrounding UI, prior step, and likely emotional state.
3. Remove jargon, ambiguity, passive phrasing, and filler that does not help the user act.
4. Rewrite the string to be specific, direct, and compatible with UI and localization constraints.
5. Check nearby strings for terminology or tone conflicts and normalize them if needed.
6. Verify that the rewrite still matches the product behavior and does not overpromise.

## Design Principles / Evaluation Criteria

- Clarity over cleverness
- User vocabulary over internal product language
- Actionable guidance, especially in error and recovery moments
- Brevity without losing meaning
- Tone matched to the user's context and stress level
- Compatibility with localization, truncation, and component constraints

## Output Contract

- Exact replacement strings for the affected interface copy
- Notes on any terminology decisions needed to keep the copy consistent
- Short rationale for rewrites that materially change tone, structure, or user guidance

## Examples

### Example 1

Input:
- Source string: "Submission failed"
- Context: Failed payment update in account settings
- User goal: Update billing details successfully

Expected output:
- Replacement string: "We couldn't update your card. Check the card details and try again."
- Rationale: Explains the failed action and gives the user a clear next step.

## Guardrails

- Do not invent product behavior, policies, or recovery options that do not exist
- Do not rewrite for style alone if the original is already clear
- Do not introduce marketing language into operational UI copy
- Do not ignore state context, available actions, or severity of the moment

## Optional Tools / Resources

- Notion MCP, Figma MCP, and Chrome DevTools MCP for source context and UI grounding
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [GOV.UK Style Guide](https://www.gov.uk/guidance/style-guide/a-to-z)
- [Plain Language Guide](https://digital.gov/guides/plain-language/)
- [Carbon Content Guidelines](https://carbondesignsystem.com/guidelines/content/overview/)
- [Nielsen Norman Group](https://www.nngroup.com/)
