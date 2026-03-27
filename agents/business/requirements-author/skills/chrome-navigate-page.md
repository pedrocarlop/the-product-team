---
name: chrome-navigate-page
tool: mcp__chrome_devtools__navigate_page
description: Explore the current product to ground requirements in the actual experience, existing patterns, and real constraints.
---

# Chrome: Navigate Page

Use this skill to explore the live product before authoring requirements. Requirements grounded in observed product behavior are more accurate, more consistent with existing conventions, and less likely to conflict with existing functionality.

## When to Use

- Before writing requirements for a change to an existing feature — understand how it currently works
- When the normalized brief is ambiguous about what currently exists versus what needs to be built
- When verifying that a proposed requirement does not conflict with existing product behavior
- When exploring adjacent features that the new requirement must stay consistent with

## How to Use

Call `mcp__chrome_devtools__navigate_page` with the URL of the relevant product area. Walk through the existing experience to understand:
- What the current user journey looks like before the requested change
- What terminology and labels are already in use (use them in requirements to ensure consistency)
- What edge cases and states already exist that the new requirements must account for
- What the current entry and exit points are for the feature being changed

## What to Extract

- Existing terminology to use verbatim in `REQ-*` items (do not invent new terms for existing concepts)
- Current constraints visible in the UI that the requirements must acknowledge (e.g., field limits, permission gates)
- Existing states that the new requirements must not break

## Notes for Requirements Author

Navigate before writing. Requirements authored without exploring the current product often duplicate existing behavior, conflict with existing patterns, or use different terminology for the same concept. The product is the primary source of truth for existing behavior.

## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, GitHub MCP, Slack MCP
- Reference websites: [Atlassian Product Requirements Guide (atlassian.com)](https://www.atlassian.com/agile/product-management/requirements), [Google Technical Writing Resources (developers.google.com)](https://developers.google.com/tech-writing), [Microsoft Writing Style Guide (learn.microsoft.com)](https://learn.microsoft.com/en-us/style-guide/welcome/), [ProductPlan Guides (productplan.com)](https://www.productplan.com/learn/), [NN/g UX Documentation Articles (nngroup.com)](https://www.nngroup.com/)
