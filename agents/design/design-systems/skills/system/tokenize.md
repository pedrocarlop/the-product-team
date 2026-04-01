---
name: tokenize
description: "Define, name, layer, and mode design tokens so the design system expresses values as a maintainable contract instead of scattered literals. Use when a feature has repeated hard-coded values, when light/dark modes need better structure, or when tokens are drift from design/code."
---

# Tokenize

## Overview

"Tokenize" turns raw design values (Hex, Pixels, Rem) into a structured system of names and roles. A good token system is a "shared contract" between design and code. Without tokens, every UI change requires finding and replacing scattered literals, leading to "Visual Debt" and broken themes.

## When to Use

- When a new feature or design pattern introduces new visual values (e.g., a "Neutral Grey 500").
- When audit or migration reveals hard-coded literals that should be centralized.
- When the design system needs to support multiple modes: Light/Dark, High Contrast, Compact/Comfortable.
- When the existing naming taxonomy is confusing or "one-level deep" (e.g., only `blue-500`).

## When Not to Use

- When the task is purely about component layout or assembly logic.
- When the visual value is a one-off exception (e.g., a specific marketing illustration color).
- When the problem is the distribution or installation of tokens, not their definition.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

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

### Step 2: Discover and Inventory Raw Values

Collect any visual literals that need systematic naming:
- **Colors**: Hex, HSL, RGB.
- **Spacing/Size**: Px, Rem, %, absolute grid values.
- **Typography**: Font size, Weight, Letterspacing, Line height.
- **Shadows/Elevation**: Blur, Spread, Opacity, Y-offset.

### Step 3: Categorize by Taxonomy Layer

Assign every value to its correct level in the system:

| Layer | Type | When to Use | Example |
| :--- | :--- | :--- | :--- |
| **Primitive** | Reference | For internal context only. Hard-coded values. | `palette-blue-500` |
| **Semantic** | Alias | For application-wide logic. Use in 90% of cases. | `color-action-primary` |
| **Component** | Specific | For one specific control type only. | `button-primary-bg` |

### Step 4: Apply Naming Taxonomy (The System)

Follow a consistent naming structure:
- `{category}-{property}-{intent}-{state}`
- **Examples**:
  - `color-text-primary`
  - `space-system-layout-inline-xl`
  - `color-surface-danger-hover`

Avoid naming by "how it looks" (e.g., `blue`, `bold`, `large`). Name by **intent** (e.g., `brand`, `critical`, `headline`).

### Step 5: Define Mode Behavior (The Map)

Specify how tokens change based on system mode (Light/Dark):
- **Base (Light)**: `color-surface-primary` → White (`#FFFFFF`).
- **Mode (Dark)**: `color-surface-primary` → Deep Grey (`#121212`).
- Check contrast ratios for **both** modes.

### Step 6: Verify the Map and Contract

Ensure the token is ready for adoption:
- **Design Alignment**: Can a designer select this token in Figma?
- **Code Alignment**: Is there a corresponding CSS variable or JS constant name?
- **Redundancy**: Does this token already exist under a different name? (Minimize tokens).

### Step 7: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Decision Tree: Is this a new token?

```
Is the visual value reused more than 3 times in the product?
├── YES → Does a semantic token with the same intent exist?
│   ├── YES → Use the existing token (Skip).
│   └── NO → Is it a one-off for a specific component?
│       ├── YES → Create a Component Token.
│       └── NO → Create a Semantic Token.
└── NO → Use a Local Literal (No token).
```

## Worked Examples

### Example 1: Action Color Token

**Inventory**: Hex `#1E40AF`.
**Taxonomy**:
- **Primitive**: `palette-blue-600` → `#1E40AF`.
- **Semantic**: `color-action-primary` → `palette-blue-600`.
- **Component**: `button-primary-bg` → `color-action-primary`.
**Rationale**: By linking the button to the semantic "Action Primary," we can change the whole product's accent color in one place.

### Example 2: Spacing Logic (Layout)

**Inventory**: `24px` padding on sections.
**Taxonomy**:
- **Primitive**: `size-primitive-24` → `1.5rem`.
- **Semantic**: `space-system-section-padding` → `size-primitive-24`.
**Rationale**: If we change the "Section Padding" token, every section across the platform updates instantly.

## Guardrails

- **Never name a semantic token by its value.** (e.g., `color-brand-blue` is a failure; `color-brand-primary` is a success).
- **Always handle both Light and Dark modes.** If a token works in one but breaks in the other, it is an incomplete token.
- **Do not create "Token Sprawl."** If an existing token works, reuse it. Every new token adds maintenance debt.
- **Always check contrast.** Semantic text tokens must meet WCAG AA contrast against their intended surfaces.

## Troubleshooting

### Issue: Token names are too long or confusing
**Cause**: Over-categorization or including too many modifiers.
**Solution**: Flat naming where intent is clear is usually better than deep nested hierarchies. Use `{category}-{intent}-{state}` as the baseline.

### Issue: Design and Code are drifting
**Cause**: Manual updates to tokens in one place but not the other.
**Solution**: Use a single source of truth (e.g., Style Dictionary or Tokens Studio) to export tokens into both CSS and Figma.

### Issue: Confusion between Semantic vs. Component tokens
**Cause**: Using component tokens for general layout or vice versa.
**Solution**: If it's used on more than one component type (e.g., on both a Button and a Link), it MUST be a Semantic token.
