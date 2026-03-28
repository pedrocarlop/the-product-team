---
name: figma-get-screenshot
tool: mcp__figma__get_screenshot
description: Capture flow diagrams and screen designs from Figma to evaluate sequence logic, decision points, and transition completeness.
---

# Figma: Get Screenshot

Use this skill to inspect the flow diagrams and screen designs in Figma and evaluate the logical completeness of the user journey — entry points, decision branches, transitions, and recovery paths — before or alongside live product verification.

## When to Use

- When reviewing `task-flows.md` against the visual flow diagrams to verify that all branches shown in the design are documented in the spec
- When checking that the designed screens cover all the states required by each flow step
- When identifying decision points in the flow that are shown in the design but missing from `task-flows.md`
- When comparing the designed alternate path screens against the documented alternate path logic

## How to Use

Call `mcp__figma__get_screenshot` with the node ID for the relevant flow diagram or screen set. Inspect for:
- Flow arrows and connectors — do they form a complete directed graph with no disconnected nodes?
- Screen coverage — is there a designed screen for every step in the task flow?
- Decision point labels — are all conditions clearly labeled on branches?
- Error and recovery screens — are they connected to the states that trigger them?

## What to Extract

- Disconnected flow nodes — steps in the design that have no incoming or outgoing connections
- Missing screens — flow steps that have no designed screen representation
- Unlabeled decision branches — forks with no condition specified
- Designed states not documented in `task-flows.md`

## Notes for UX Flow Reviewer

Use the screenshot to review the flow's logical completeness, not its visual design quality. Focus on whether every user decision leads somewhere, every error leads to recovery, and every task has a defined completion state. Leave visual design quality to the dedicated visual design reviewers.

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, and Notion MCP for flow diagrams, screenshots, and handoff notes
- [Maze](https://maze.co/)
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Baymard Institute](https://baymard.com/)
- [Storybook Docs](https://storybook.js.org/docs)
- [Material Design](https://m3.material.io/)
