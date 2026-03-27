---
name: name
description: Create clear, scalable names for features, settings, concepts, and navigation labels that match user vocabulary and stay consistent over time.
---

# Name

## Purpose

Use this skill to choose durable user-facing names that are clear, distinct, and easy to apply consistently across product surfaces.

## When to Use

- When a new feature, setting, navigation item, or concept needs a name
- When existing labels are internally driven, overloaded, or hard to distinguish
- When the product needs a terminology decision that will affect multiple screens or documents

## When Not to Use

- When the task is improving a local sentence or CTA rather than naming a concept
- When the term is already decided and only needs consistency cleanup across the flow
- When the problem is page structure or content hierarchy rather than terminology choice

## Required Inputs

- What the concept, feature, or setting actually does
- Who the primary user is and how they are likely to talk about it
- Nearby concepts it could be confused with
- UI constraints such as navigation width, button length, or localization sensitivity
- Any existing glossary, banned terms, or legal or brand constraints

## Workflow

1. Define the concept in plain language and separate it from implementation detail.
2. Identify likely user vocabulary and the closest competing terms in the product space.
3. Generate candidate names that are concrete, distinct, and workable in UI constraints.
4. Test candidates for ambiguity, overlap, scalability, and fit across navigation, headings, settings, and support content.
5. Choose the recommended term and document acceptable alternatives or banned wording.
6. Note any dependent labels that should align with the final name.

## Design Principles / Evaluation Criteria

- User vocabulary over internal jargon
- Distinctness from adjacent concepts
- Scalability across UI surfaces and support materials
- Brevity within interface constraints
- Localization friendliness and low ambiguity
- Long-term maintainability, not short-term cleverness

## Output Contract

- Recommended name with 2 to 4 viable alternatives when the decision is open
- A short explanation of why the chosen term fits the user model
- Guidance for related labels, variants, or forbidden terminology

## Examples

### Example 1

Input:
- New feature lets teams collect reusable prompts for common tasks
- Current internal term is "prompt repository"
- Surface includes navigation, onboarding, and empty states

Expected output:
- Recommended name: "Prompt library"
- Alternatives: "Saved prompts", "Shared prompts"
- Guidance: Avoid "repository" because it sounds technical and does not match user vocabulary

## Guardrails

- Do not pick names based only on internal architecture or team shorthand
- Do not collapse distinct concepts into one term just for simplicity
- Do not optimize for novelty if it reduces clarity
- Do not ignore how the name behaves in translated strings or constrained UI surfaces

## Optional Tools / Resources

- Product glossary or naming history
- Competitive audits or user vocabulary research
- Navigation maps, UI mocks, and screen constraints
- Localization guidance for translation-sensitive terms
