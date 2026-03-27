---
name: adapt
description: Adjust product behavior, content structure, and visual treatment to fit cultural, legal, and regional expectations without losing product intent.
activation_hints:
  - "Use when a surface needs cultural review beyond translation."
  - "Route here for dates, currencies, forms of address, imagery, color meaning, legal disclosures, and regional conventions."
  - "Do not use for pure string expansion or RTL mirroring."
---

# Adapt

## Purpose

Use this skill to make a localized experience feel appropriate for the target region, not merely translated into it.

## When to Use

- When dates, currencies, names, or addresses need locale-aware treatment
- When imagery, symbols, colors, or gestures could carry different meanings
- When legal, privacy, or disclosure expectations vary by region
- When the product needs localized workflow or content structure adjustments

## When Not to Use

- When the problem is only longer translated strings
- When the main issue is mirrored directionality in RTL locales
- When no locale-specific convention materially changes the experience

## Required Inputs

- Target locales and any regional subvariants
- Screenshots, Figma context, or flow diagrams
- Cultural or legal requirements already known
- Existing product terminology that must stay consistent
- Any locale-specific constraints from legal, content, or engineering

## Workflow

1. Identify the locale-specific expectations that could change the user experience.
2. Check whether the current design encodes one region's norms as if they were universal.
3. Adjust labels, format patterns, imagery, and disclosure space to fit the locale.
4. Flag any items that require legal, content, or domain expert review.
5. Keep the core product intent stable while adapting presentation and structure.
6. Verify that the localized version still feels trustworthy and culturally natural.

## Design Principles / Evaluation Criteria

- Locale fit over literal reuse
- Legal and cultural accuracy over convenience
- User trust over one-size-fits-all presentation
- Clear separation between product intent and regional expression
- Adaptation should be traceable, not improvised

## Output Contract

- Locale-specific adaptation decisions
- Items that require expert or legal review
- Content or layout changes needed to support the adaptation
- Any unresolved regional assumptions

## Examples

### Example 1

Input:
- Surface: Checkout summary
- Locale: Germany
- Concern: Currency and date display

Expected output:
- Recommendation: Format currency and dates with locale-aware conventions, leave room for longer disclosure text, and avoid US-centric shorthand.

## Guardrails

- Do not invent legal requirements
- Do not change product meaning to chase local familiarity
- Do not assume imagery, colors, or gestures are neutral everywhere
- Do not leave regional conventions implicit when they affect trust or comprehension

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, and Notion MCP for localized screen review and decision notes
- [Lokalise](https://lokalise.com/)
- [W3C Internationalization](https://www.w3.org/International/)
- [Unicode CLDR](https://cldr.unicode.org/)
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
