---
name: figma-get-screenshot
tool: mcp__figma__get_screenshot
description: Capture locale variant frames from Figma to visually verify text expansion, RTL rendering, and cultural adaptation in context.
---

# Figma: Get Screenshot

Use this skill to visually inspect locale variant designs — comparing layouts side by side to identify text overflow, alignment issues, or cultural adaptation gaps that are only visible when the actual locale content is placed in the component.

## When to Use

- When reviewing locale-specific frames created for a target locale (e.g., Arabic RTL, German long-text, Japanese character-dense)
- When verifying that text expansion in a locale does not cause truncation, wrapping, or overflow
- When checking that icon-text alignment is correct in RTL locales
- When confirming that number formats, date formats, and currency symbols appear in the correct position for each locale

## How to Use

Call `mcp__figma__get_screenshot` with the node ID for the locale variant frame. Compare the returned screenshot against the base locale frame to identify:
- Text containers that overflow or truncate with longer locale strings
- Icons or decorative elements that are not flipped or repositioned for RTL
- Misaligned content that breaks the visual hierarchy under locale-specific text
- Cultural imagery or iconography that may carry unintended meaning in the target locale

## What to Extract

- Specific components or layout zones that fail under text expansion
- RTL rendering errors — elements not flipping, margins not reversing, alignment not switching
- Cultural adaptation gaps — imagery, color choices, or conventions that need locale overrides

## Notes for Localization Designer

Screenshot comparison is the fastest way to catch locale rendering issues. Always compare the base locale frame and the target locale frame side by side. Document every identified gap as a specific `CMP-*` adaptation requirement in `component-mapping.md`.
