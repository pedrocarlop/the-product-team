---
name: chrome-navigate-page
tool: mcp__chrome_devtools__navigate_page
description: Explore the current product and competitor experiences first-hand to generate observational evidence for research synthesis.
---

# Chrome: Navigate Page

Use this skill to explore the live product and analogous products first-hand — observing how users are currently supported (or not supported) through the experience and identifying friction, missing affordances, and behavioral evidence for the research synthesis.

## When to Use

- When conducting a heuristic walkthrough of the current product before design begins
- When doing competitive analysis — exploring how analogous products solve the same user problem
- When observing the current user journey to identify friction points that the new design must address
- When grounding research insights in the actual product rather than abstract descriptions

## How to Use

Call `mcp__chrome_devtools__navigate_page` with the relevant product or competitor URL. Walk through the experience as a first-time user would:
- Navigate from the entry point through the primary task flow
- Note every point of friction, confusion, or unexpected behavior
- Identify what information is missing or presented too late
- Observe how errors, empty states, and edge cases are handled

## What to Extract

- Friction points in the current experience with their specific location in the flow
- Missing affordances — user actions that the product does not support but clearly should
- Behavioral evidence — patterns observable in the product that suggest what users are trying to do
- Competitive differentiators — specific ways analogous products outperform the current product

## Notes for UX Researcher

Document observations as evidence with their source ("Navigating [URL], step 3 of the checkout flow shows X, which suggests Y"). Evidence without a source cannot be validated. Hand synthesized insights — not raw observations — to the design role.
