---
name: expand
description: Design interfaces to survive text expansion across locales without truncation, clipping, or fragile fixed-width assumptions.
---

# Expand

## Purpose

Use this skill to make layouts resilient to text expansion so translated UI still reads cleanly and behaves predictably.

## When to Use

- When source strings may become significantly longer in target locales
- When fixed widths, truncation, or overflow are likely to break the design
- When a UI needs to support multiple scripts or text densities without redesigning per locale

## When Not to Use

- When the primary issue is RTL ordering or icon mirroring
- When the main need is localized content strategy rather than layout resilience
- When the surface is already proven to handle worst-case string lengths

## Required Inputs

- Source strings and target locales
- Screenshots, mocks, or Figma context for the surface
- Known character limits, if any
- Constraints from the design system or component library
- Any strings with high growth risk, such as CTAs, dates, names, or table headers

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

1. Identify the longest likely translated version, not just the English source.
2. Inspect the container, typography, and spacing rules that could fail under growth.
3. Replace fixed widths with flexible sizing, wrapping, or intrinsic layout where possible.
4. Reserve overflow budget for critical labels and interactive controls.
5. Check adjacent components for cascading breakage, especially in rows, grids, and toolbars.
6. Verify that the layout still feels balanced when the longest strings land.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Flexibility over pixel rigidity
- Wrapping before truncation
- Consistent spacing under growth
- No hidden overflow or clipped affordances
- Scalable patterns that work across several locales, not just one translation pair

## Output Contract

- Recommended layout adjustments for text growth
- Components or containers that need flexible sizing
- Any unavoidable truncation, with a clear rationale
- Risks that still need locale testing

## Examples

### Example 1

Input:
- Surface: Primary action button
- Source label: "Save"
- Target locale: German

Expected output:
- Recommendation: Replace fixed button width with intrinsic width plus padding and allow the container row to wrap if needed.
- Rationale: The translated label may be materially longer than the source and should not clip.

## Guardrails

- Do not solve growth problems by silently cutting off meaning
- Do not design only for the average translation length
- Do not assume all locales expand equally
- Do not break component consistency just to fit one long string

## Optional Tools / Resources

- Figma MCP for inspecting and adjusting layout constraints
- Design system component specs
- Locale string length estimates or translation previews
- Pseudo-localization output for growth testing
