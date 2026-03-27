---
name: figma-get-screenshot
tool: mcp__figma__get_screenshot
description: Capture a screenshot of a Figma frame or component to review copy in its visual context.
---

# Figma: Get Screenshot

Use this skill to view the actual design comps and inspect copy in context — labels, button text, helper text, error messages, and empty states as they appear in the designed layout.

## When to Use

- Before writing a copy review finding to verify the exact wording shown in the design
- When you need to see copy density, label placement, or truncation risk in context
- When checking whether error copy is visually prominent enough relative to the UI around it
- When comparing copy across multiple screens to assess terminology consistency

## How to Use

Call `mcp__figma__get_screenshot` with the Figma file URL or specific node ID for the frame you want to inspect. Review the returned screenshot for:
- All visible text strings (labels, CTAs, helper text, error messages, empty states)
- Copy that is part of the component versus copy that is placeholder text
- Truncation or overflow that might indicate copy length issues

## What to Extract

- Exact copy strings for each reviewed element
- Any inconsistency between copy shown in the design and the terminology in the PRD
- Copy elements that are too long, too vague, or use non-standard terminology

## Notes for Copy Reviewer

Never write a finding based on the file names or component names in Figma — only judge the copy that users will actually read. If the screenshot shows placeholder copy, flag it as an open item rather than a finding.

## Optional Tools / Resources

- Figma MCP for screenshot grounding and inline copy checks
- Notion MCP for terminology, voice, and editorial notes
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [GOV.UK Style Guide](https://www.gov.uk/guidance/style-guide/a-to-z)
- [Plain Language Guide](https://digital.gov/guides/plain-language/)
- [Carbon Content Guidelines](https://carbondesignsystem.com/guidelines/content/overview/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
