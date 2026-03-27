---
name: wire
description: Design wireframes and interaction scaffolding that make the structure, hierarchy, and behaviors of a flow easy to understand.
activation_hints:
  - "Use when the flow structure is known and you need screen-level layout, hierarchy, and interaction behavior."
  - "Route here for wireframes, page skeletons, responsive behavior, and interaction annotations."
  - "Do not use for final visual styling, branding, or copy-only edits."
---

# Wire

## Purpose

Use this skill to translate a mapped flow into wireframes that show what appears on each screen, how it is arranged, and how the user moves through it.

## When to Use

- When a task map exists and the next step is screen composition
- When layout, hierarchy, or component placement needs to be defined without visual polish
- When responsive behavior, empty states, or interaction rules need to be scaffolded

## When Not to Use

- When the main problem is deciding what the experience should do, not how it should appear on screen
- When the request is for brand styling, high-fidelity UI, or visual design detail
- When the work is primarily about measuring usability rather than drafting the structure

## Required Inputs

- The mapped flow, task structure, or IA
- Any screenshots or existing screens the wireframe should align with
- Component constraints, platform patterns, and breakpoints
- State requirements such as loading, empty, error, success, or disabled
- Any known accessibility, content, or technical constraints

## Workflow

1. Establish the screen purpose and the user's priority task for each view.
2. Lay out the information hierarchy from most important to least important.
3. Place controls, content, and supporting feedback where they help the user act quickly.
4. Define interaction behavior for primary, secondary, and conditional actions.
5. Draft responsive variants or structural shifts for smaller and larger viewports.
6. Annotate key decisions so implementation and review stay aligned.

## Design Principles / Evaluation Criteria

- Clarity before decoration
- Strong hierarchy with obvious primary action
- Predictable component placement and behavior
- States and edge cases should be visible in the scaffold
- The wireframe should be specific enough to review, but loose enough to evolve

## Output Contract

- Low-fidelity wireframes or screen skeletons
- Interaction notes for primary paths and important branches
- Responsive or layout variants when relevant
- Callouts for unresolved structural questions or risky assumptions

## Guardrails

- Do not add visual styling that distracts from structure
- Do not leave critical interactions implied when they need to be explicit
- Do not design every pixel if the question is still about flow or hierarchy
- Do not ignore states that will materially change the user's path

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for flow grounding and wireframe context
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Maze](https://maze.co/)
- [Dovetail](https://dovetail.com/)
- [Material Design](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
