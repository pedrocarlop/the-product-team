---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture the DOM of the current product state to gather evidence for PRD grounding issues and acceptance criteria verification.
---

# Chrome: Take Snapshot

Use this skill to capture the current product's DOM as evidence when you identify a discrepancy between the PRD and the live product. The snapshot provides a durable record of the actual product state at review time.

## When to Use

- When you have identified a contradiction between the PRD and the live product and need to document the evidence
- When verifying that an acceptance criterion is observable in the current DOM structure
- When checking that the product's current terminology matches the `REQ-*` labels in the PRD
- When capturing the current state of a feature that the PRD claims to modify

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the relevant page. Parse the returned DOM for:
- Visible text that contradicts or confirms PRD terminology
- Component structures that reveal implementation constraints the PRD must acknowledge
- State indicators (loading, error, empty) that already exist and must be accounted for in requirements

## What to Extract

- Specific text strings that differ from the PRD's terminology (document both in the review finding)
- Component or structural evidence of existing constraints that the PRD does not mention
- Confirmation that a PRD-described behavior is actually present or absent in the current product

## Notes for Requirements Reviewer

Use the snapshot to make findings concrete. A finding that says "PRD says X but the current product shows Y (see DOM snapshot taken at [URL])" is actionable. A finding that says "requirements seem inconsistent with the product" is not.

## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, GitHub MCP, Slack MCP
- Reference websites: [Atlassian Product Requirements Guide (atlassian.com)](https://www.atlassian.com/agile/product-management/requirements), [Google Engineering Practices: Reviewing Design Docs (google.github.io)](https://google.github.io/eng-practices/), [Microsoft Writing Style Guide (learn.microsoft.com)](https://learn.microsoft.com/en-us/style-guide/welcome/), [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [NN/g UX Documentation Articles (nngroup.com)](https://www.nngroup.com/)
