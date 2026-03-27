---
name: figma-get-design-context
tool: mcp__figma__get_design_context
description: Retrieve the full design system context — components, tokens, variants, and spacing rules — before authoring any visual surface.
---

# Figma: Get Design Context

Use this skill to pull the complete, structured design system from Figma before making any visual design decision. The design system is the authoritative source for components, tokens, typography, spacing, and color — not memory, not convention, not approximation.

## When to Use

- Before selecting any component for the design package — verify exact names and available variants
- When specifying color, typography, or spacing — use tokens, not raw values
- When checking which component states are already defined in the system versus which need new design decisions
- When mapping the design to `CMP-*` entries in `component-mapping.md`

## How to Use

Call `mcp__figma__get_design_context` with the Figma file URL or the specific component library node. Extract:
- **Component names**: Use verbatim in `component-mapping.md` — never paraphrase
- **Token names**: For color, spacing, typography, and motion — use these in `ui-spec.md`
- **Variant conditions**: Which props trigger which visual state — critical for specifying all states
- **Annotation content**: Designers leave implementation notes in annotations — read them

## What to Extract

- Every token used in the design (specify by name, not value)
- All available component variants and their trigger conditions
- Constraints on component usage (max-width, minimum tap target, text truncation rules)
- Any design system exceptions documented in annotations

## Notes for UI Designer

Full design-system fidelity means zero hardcoded values in the spec. Every color is a token. Every spacing value is a token. Every typographic style is a text style. If you cannot find the token, flag it as a gap in `research-and-rationale.md` — do not use a raw value as a workaround.
