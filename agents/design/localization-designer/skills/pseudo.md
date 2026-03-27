---
name: pseudo
description: Use pseudo-localization to expose layout breakage, clipping, and string-handling issues before real translations are available.
activation_hints:
  - "Use when you need a fast localization stress test without waiting for translations."
  - "Route here for pseudo-localized previews, overflow detection, and string-handling checks."
  - "Do not use for RTL layout design or cultural adaptation decisions."
---

# Pseudo

## Purpose

Use this skill to stress-test the interface with pseudo-localized text so layout and string handling problems appear early.

## When to Use

- Before translation begins on a new or changed surface
- When you want to detect clipping, wrapping, or overflow issues quickly
- When the team needs confidence that components can survive longer, accented text

## When Not to Use

- When the task is to design true RTL behavior
- When the issue is regional convention rather than string length
- When the surface already has validated pseudo-localization coverage and only content changed

## Required Inputs

- The screen or component to test
- Source strings or a pseudo-localization build
- Target locales or string growth assumptions
- The environment or preview surface where the test will run
- Any known constraints, such as max lines or fixed-width controls

## Workflow

1. Apply pseudo-localization to the source strings or preview build.
2. Inspect the surface for overflow, clipping, broken alignment, and awkward line breaks.
3. Test interactive states, not just the default screen.
4. Compare the pseudo-localized result with the source to find fragile containers and assumptions.
5. Record the issues by component and severity.
6. Confirm the surface is ready for real translation handoff.

## Design Principles / Evaluation Criteria

- Pseudo-localization should reveal real layout risk
- Failures in pseudo-localization are production bugs waiting to happen
- Testing must cover states, not just one static frame
- The goal is detection, not visual polish

## Output Contract

- List of overflow, clipping, or wrapping failures
- Components or patterns that need layout hardening
- Any strings or states that require follow-up before translation
- Clear pass or fail guidance for localization readiness

## Examples

### Example 1

Input:
- Surface: Settings page
- Test method: Pseudo-localized strings with length padding

Expected output:
- Result: The sidebar labels fit, but the primary button row overflows and needs flexible width handling before translation starts.

## Guardrails

- Do not use pseudo-localization as a substitute for real locale QA
- Do not ignore state coverage just because the default screen looks fine
- Do not mark a surface ready when overflow still exists
- Do not confuse pseudo-localization failures with translation quality issues

## Optional Tools / Resources

- Lokalise or equivalent pseudo-localization tooling
- Figma MCP for inspecting affected layouts
- Visual regression screenshots
- Component constraints or max-width specifications
