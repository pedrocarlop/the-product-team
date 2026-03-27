---
name: search-query
tool: search_query
description: Research domain patterns, regulatory requirements, and industry precedents to ground PRD decisions in evidence.
---

# Search Query

Use this skill to research the domain, regulatory environment, and established product patterns before authoring requirements. Requirements grounded in external evidence are more defensible and less likely to introduce new risks.

## When to Use

- When the request involves a domain with regulatory or compliance requirements (privacy, accessibility, financial, healthcare)
- When researching how comparable products define similar features — to calibrate scope and acceptance criteria
- When the normalized brief names a technical or business concept that needs clarification before it can be specified precisely
- When looking for established patterns for non-functional requirements (performance benchmarks, security standards, accessibility mandates)

## How to Use

Call `search_query` with a targeted query. Prefer specific, bounded queries:
- `"WCAG 2.1 AA form validation requirements"` — not `"accessibility requirements"`
- `"GDPR consent collection UX requirements"` — not `"privacy requirements"`
- `"e-commerce checkout abandonment industry benchmarks"` — not `"checkout metrics"`

## What to Extract

- Specific regulatory requirements to include as non-functional requirements with the regulation citation
- Industry benchmark values to use in success metrics (e.g., p95 load time targets)
- Established terminology from the domain to use in `REQ-*` items
- Precedents for scope boundaries — what comparable products include and exclude in similar features

## Notes for Requirements Author

Cite research sources in the PRD under the `dependencies` or `risks` sections when regulatory or compliance constraints are involved. A requirement that references `WCAG 2.1 AA criterion 1.4.3` is traceable; one that says "must be accessible" is not.

## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, GitHub MCP, Slack MCP
- Reference websites: [Atlassian Product Requirements Guide (atlassian.com)](https://www.atlassian.com/agile/product-management/requirements), [Google Technical Writing Resources (developers.google.com)](https://developers.google.com/tech-writing), [Microsoft Writing Style Guide (learn.microsoft.com)](https://learn.microsoft.com/en-us/style-guide/welcome/), [ProductPlan Guides (productplan.com)](https://www.productplan.com/learn/), [NN/g UX Documentation Articles (nngroup.com)](https://www.nngroup.com/)
