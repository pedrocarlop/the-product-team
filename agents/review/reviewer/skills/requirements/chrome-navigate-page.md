---
name: chrome-navigate-page
tool: mcp__chrome_devtools__navigate_page
description: Navigate the live product to verify that PRD requirements are grounded in actual product behavior and existing constraints.
---

# Chrome: Navigate Page

Use this skill to verify that the PRD's requirements accurately reflect current product behavior and that the proposed changes are consistent with how the product actually works. Requirements that contradict the live product are a common source of design and engineering blockers.

## When to Use

- When reviewing a requirement that modifies an existing feature — verify the current behavior matches the PRD's stated starting point
- When evaluating whether the PRD's acceptance criteria are testable in the actual product
- When checking whether the PRD's scope is consistent with what currently exists (no phantom features in scope)
- When verifying that the product terminology in the PRD matches what users actually see

## How to Use

Call `mcp__chrome_devtools__navigate_page` with the URL of the relevant product feature. During navigation, check:
- Does the current product behavior match the PRD's description of the starting state?
- Are the labels and terminology in `REQ-*` items consistent with what is currently shown to users?
- Can the acceptance criteria be verified in the current product (or after the change)?
- Are there existing constraints visible in the live product that the PRD does not acknowledge?

## What to Extract

- Contradictions between PRD claims and actual product behavior
- Terminology mismatches between the PRD and the live product labels
- Missing constraints that only become visible when you use the product
- Acceptance criteria that cannot be verified in the actual experience

## Notes for Requirements Reviewer

Navigating the product is the fastest way to catch grounding errors. A PRD that describes a feature that does not exist, or uses terminology that users never see, will send the designer in the wrong direction. Catch it here.

## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, GitHub MCP, Slack MCP
- Reference websites: [Atlassian Product Requirements Guide (atlassian.com)](https://www.atlassian.com/agile/product-management/requirements), [Google Engineering Practices: Reviewing Design Docs (google.github.io)](https://google.github.io/eng-practices/), [Microsoft Writing Style Guide (learn.microsoft.com)](https://learn.microsoft.com/en-us/style-guide/welcome/), [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [NN/g UX Documentation Articles (nngroup.com)](https://www.nngroup.com/)
