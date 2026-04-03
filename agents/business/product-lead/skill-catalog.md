# Product Lead Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `experiment-brief`

- Description: Define a product experiment using Hypothesis-Driven Development and Pre-Registration of Decision Rules.
- Trigger: When the team wants to validate an idea before full commitment.
- Primary MCP/tool: notion, linear, amplitude, statsig, braintrust
- Fallback: analyst/experiment-readout, search_query
- Best guess: An experiment brief with metrics, decision rules, and model-based rationale.
- Output: logs/active/<project-slug>/deliverables/product-lead-experiment-brief.md
- Done when: The experiment can be run and judged without inventing criteria later.

## `frame-problem`

- Description: Turn a raw request into a clear product problem using 2026 AI-first discovery (Lane, Zeda.io).
- Trigger: When the request is vague, outcome-first, or lacks a bounded problem definition.
- Primary MCP/tool: lane, zeda_io, chat_prd, notion
- Fallback: search_query, reference/ground
- Best guess: A structured framing brief with a JTBD model and root-cause analysis (5 Whys).
- Output: logs/active/<project-slug>/deliverables/product-lead-frame-problem.md
- Done when: The problem is crisply bounded and the decision frame is clear to the team.

## `prioritize-roadmap`

- Description: Rank work against impact, effort, and strategic fit using RICE 2.0 and Outcome-Based Roadmapping.
- Trigger: When multiple candidate bets compete for attention or quarterly planning is initiated.
- Primary MCP/tool: jira_product_discovery, airtable_product_central, craft_io
- Fallback: analyst/metric-definition, search_query
- Best guess: A ranked roadmap or priority decision with rationale grounded in strategic fit and resource constraints.
- Output: logs/active/<project-slug>/deliverables/product-lead-prioritize-roadmap.md
- Done when: The ordering is explicit, tradeoffs are documented, and North Star alignment is verified.

## `stakeholder-memo`

- Description: Synthesize diverse signals into a high-stakes decision memo using the Pyramid Principle and Amazon 6-Page narrative styles.
- Trigger: When a product decision needs alignment, funding, or executive approval.
- Primary MCP/tool: notion, loom, grain
- Fallback: search_query, reference/verify
- Best guess: A stakeholder memo with recommendation, risks, and asks.
- Output: logs/active/<project-slug>/deliverables/product-lead-stakeholder-memo.md
- Done when: All primary stakeholders have received a clear, evidence-based recommendation with explicit asks.

## `write-prd`

- Description: Write a delivery-grade PRD that encodes logic, design-awareness, and technical feasibility for AI-first products.
- Trigger: When engineering or design need a precise, lossless product specification for execution.
- Primary MCP/tool: chat_prd, figr, vercel_v0, notion
- Fallback: reference/ground, search_query
- Best guess: A PRD or equivalent product specification with component-state models and Gherkin scenarios.
- Output: logs/active/<project-slug>/deliverables/product-lead-write-prd.md
- Done when: Executors can build without product ambiguity and logic/design edge cases are resolved.
