---
name: figma-get-screenshot
tool: mcp__figma__get_screenshot
description: Capture design comps from Figma to inspect component usage, composition, and design-system alignment.
---

# Figma: Get Screenshot

Use this skill to visually inspect the design package — checking which components are used, how they are composed, and whether the visual output aligns with the design system's established patterns.

## When to Use

- When reviewing `component-mapping.md` to verify that listed components match what is actually in the design
- When checking for unnecessary custom UI that deviates from approved patterns
- When comparing the proposed design against existing design-system components to flag drift
- When inspecting theming, spacing, and token usage in context

## How to Use

Call `mcp__figma__get_screenshot` with the Figma file URL or frame node ID. Review the returned screenshot for:
- Components that look custom but might have approved equivalents in the design system
- Inconsistent spacing, color, or typography that suggests token misuse
- Layout patterns that diverge from established page or section templates
- Missing or incomplete states (e.g., only default state shown, no error or empty state)

## What to Extract

- Specific components or patterns that violate design-system conventions
- Evidence of avoidable composition (wrapper components, duplicated layout logic)
- Missing states that should be covered per the PRD requirements

## Notes for Design System Reviewer

Compare what you see in the screenshot against the design system documentation and `component-mapping.md`. Every flagged deviation must reference either the approved component it should have used or the documentation that defines the correct pattern. Do not flag subjective style preferences — only documented system violations.

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for component evidence and system context
- [Storybook Docs](https://storybook.js.org/docs)
- [W3C Design Tokens Community Group](https://www.w3.org/community/design-tokens/)
- [Material Design Components](https://m3.material.io/components)
- [Apple Human Interface Guidelines Components](https://developer.apple.com/design/human-interface-guidelines/components)
- [zeroheight](https://zeroheight.com/)
