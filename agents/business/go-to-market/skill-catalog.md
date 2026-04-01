# Go-To-Market Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `campaign-brief`

- Description: Prepare a campaign brief with audience, channel, creative direction, and KPI.
- Trigger: When marketing execution needs a crisp brief.
- Primary MCP/tool: notion
- Fallback: search_query, go-to-market/positioning-brief
- Best guess: A campaign brief ready for creative or channel execution.
- Output: logs/active/<project-slug>/deliverables/go-to-market.md
- Done when: Execution teams know the target, message, and metric.

## `customer-signal-synthesis`

- Description: Turn customer conversations, escalations, or feedback into market-ready insights.
- Trigger: When field signals need to be distilled into GTM action.
- Primary MCP/tool: notion, github
- Fallback: search_query, reference/ground
- Best guess: A synthesis of customer signals tied to GTM implications.
- Output: logs/active/<project-slug>/deliverables/go-to-market.md
- Done when: The team knows what to change in message, launch, or enablement.

## `launch-plan`

- Description: Build the launch plan with milestones, owners, dependencies, and readiness checks.
- Trigger: When a feature or product is moving toward release.
- Primary MCP/tool: notion, linear
- Fallback: go-to-market/positioning-brief, search_query
- Best guess: A launch plan with owners and launch gates.
- Output: logs/active/<project-slug>/deliverables/go-to-market.md
- Done when: The launch can be run without missing critical steps.

## `partner-thesis`

- Description: Define which partners matter, why, and what structure best fits the opportunity.
- Trigger: When partnership exploration or prioritization is needed.
- Primary MCP/tool: notion
- Fallback: search_query, go-to-market/positioning-brief
- Best guess: A partner thesis with targets and rationale.
- Output: logs/active/<project-slug>/deliverables/go-to-market.md
- Done when: The partnership strategy is specific enough to start outreach.

## `positioning-brief`

- Description: Define how the product should be positioned against alternatives for a target audience.
- Trigger: When a market-facing message needs sharpening.
- Primary MCP/tool: notion
- Fallback: search_query, reference/ground
- Best guess: A positioning brief with audience, alternatives, and message pillars.
- Output: logs/active/<project-slug>/deliverables/go-to-market.md
- Done when: The team can reuse the positioning consistently.

## `sales-enablement`

- Description: Produce the core sales narrative, objections, and proof points for the field.
- Trigger: When sales needs to communicate and defend the product clearly.
- Primary MCP/tool: notion
- Fallback: search_query, go-to-market/positioning-brief
- Best guess: A sales enablement pack with talk track and objection handling.
- Output: logs/active/<project-slug>/deliverables/go-to-market.md
- Done when: A seller can use it directly in discovery or demo.
