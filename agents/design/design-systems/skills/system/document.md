---
name: document
description: Write system documentation that explains when to use an asset, when not to use it, how it works, and what adopters need to know.
---

# Document

## Purpose

Use this skill to create documentation that helps teams adopt design system assets correctly and confidently.

## When to Use

- When a published component or token set needs usage guidance
- When adopters need to understand when to use, when not to use, or how to choose between assets
- When accessibility, props, states, or examples should be captured in one reference
- When a system decision needs rationale so future contributors can follow it

## When Not to Use

- When the main problem is authoring or restructuring the asset itself
- When the request is about token architecture rather than explanation
- When the work is mostly approval, versioning, or deprecation policy

## Required Inputs

- The asset being documented and its intended audience
- The approved behavior, variants, states, and token dependencies
- Any accessibility requirements or implementation constraints
- Examples, screenshots, or source references that show the asset in context
- The terminology that should stay consistent across the system

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: design-systems
project: <slug>
deliverable: design-systems.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Identify the decision the documentation must support.
2. Capture the asset definition, use cases, and limits in plain language.
3. Explain when the asset should and should not be used.
4. Document variants, states, accessibility requirements, and token references.
5. Add examples or do/don't guidance where teams are likely to misapply the asset.
6. Verify that the documentation matches the actual behavior and does not overpromise.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Documentation should reduce decision friction
- Rationale matters as much as rules
- Usage guidance should be specific enough to prevent misuse
- Terminology should stay consistent with the system vocabulary
- Examples should reflect actual product behavior, not idealized abstractions

## Output Contract

- A usage guide or reference entry for the asset
- Clear `when to use` and `when not to use` guidance
- Notes on behavior, variants, accessibility, and token dependencies
- Examples or decision notes that help adopters avoid misuse

## Examples

### Example 1

Input:
- A new segmented control has three variants and two keyboard behaviors
- Teams keep using it where a tab bar would be more appropriate

Expected output:
- Usage guidance that distinguishes segmented control from tab bar
- Accessibility notes for keyboard interaction
- Variant descriptions and examples showing correct use

## Guardrails

- Do not document a component as if it supports behavior it does not actually have
- Do not write rules without explaining the decision behind them
- Do not bury important constraints in long prose
- Do not let examples conflict with the real implementation or design
- Do not treat documentation as an afterthought once the asset is published

## Optional Tools / Resources

- Notion or other documentation systems
- Existing system glossary, contribution notes, and migration guidance
- Screenshots, mocks, or coded previews
- Accessibility references and implementation notes
