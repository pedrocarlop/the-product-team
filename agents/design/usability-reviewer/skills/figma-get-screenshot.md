---
name: figma-get-screenshot
tool: mcp__figma__get_screenshot
description: Capture design comps to evaluate usability heuristics in the designed visual layout before implementation.
---

# Figma: Get Screenshot

Use this skill to inspect the design comps visually and evaluate usability heuristics — discoverability, cognitive load, feedback clarity, and error prevention — as they appear in the designed layout, not just in the written spec.

## When to Use

- When evaluating whether the primary action is visually prominent enough (discoverability heuristic)
- When assessing cognitive load — how much information is on screen at once?
- When checking that error states and feedback messages are visually distinct and positioned close to the relevant element
- When reviewing whether confirmation dialogs for destructive actions are sufficiently clear and interruptive
- When assessing the learnability of the layout — does the visual hierarchy teach the user the interaction model?

## How to Use

Call `mcp__figma__get_screenshot` with the Figma file URL or frame node ID for the screen being reviewed. Evaluate the returned screenshot for:
- **Primary action prominence**: Is the most important action the most visually prominent?
- **Error state visibility**: Is the error message close to the element that caused it?
- **Confirmation dialog clarity**: Is the destructive action's consequence clearly stated?
- **Progress feedback**: Does the design show the user where they are in a multi-step process?
- **Information density**: Is there too much information on screen for the user's cognitive bandwidth?

## What to Extract

- Specific heuristic violations visible in the design layout
- Visual hierarchy issues that reduce discoverability or increase cognitive load
- Missing feedback states — designs that show default but not loading, error, or success

## Notes for Usability Reviewer

Evaluate the design as a user would experience it, not as a designer who knows the intent. If the layout's visual hierarchy does not make the correct next action obvious at a glance, it is a discoverability finding — regardless of whether the correct action is technically present.

## Optional Tools / Resources

- Chrome DevTools MCP, Figma MCP, and Notion MCP for screenshot grounding and issue notes
- [Maze](https://maze.co/)
- [Optimal Workshop](https://www.optimalworkshop.com/)
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Baymard Institute](https://baymard.com/)
- [WebAIM](https://webaim.org/)
