# Product Lead Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `experiment-brief`

- Description: Define a product experiment with hypothesis, metrics, scope, and decision rules.
- Trigger: When the team wants to validate an idea before full commitment.
- Primary MCP/tool: notion, linear
- Fallback: analyst/experiment-readout, search_query
- Best guess: An experiment brief with metrics and stop/go criteria.
- Output: logs/active/<project-slug>/deliverables/product-lead.md
- Done when: The experiment can be run and judged without inventing criteria later.

## `frame-problem`

- Description: Turn a raw request into a clear product problem, constraints, success criteria, and decision frame.
- Trigger: When the request is vague or outcome-first.
- Primary MCP/tool: notion, repository
- Fallback: search_query, reference/ground
- Best guess: A framing brief with objective, constraints, and success criteria.
- Output: logs/active/<project-slug>/deliverables/product-lead.md
- Done when: The team can tell what problem is being solved and what is out of scope.

## `prioritize-roadmap`

- Description: Rank work against impact, effort, sequencing, and strategic fit.
- Trigger: When multiple candidate bets compete for attention.
- Primary MCP/tool: notion, linear
- Fallback: analyst/metric-definition, search_query
- Best guess: A ranked roadmap or priority decision with rationale.
- Output: logs/active/<project-slug>/deliverables/product-lead.md
- Done when: The ordering is explicit and tradeoffs are documented.

## `stakeholder-memo`

- Description: Prepare a concise decision memo or update for stakeholders.
- Trigger: When a product decision needs alignment or reporting.
- Primary MCP/tool: notion
- Fallback: search_query, reference/verify
- Best guess: A stakeholder memo with recommendation, risks, and asks.
- Output: logs/active/<project-slug>/deliverables/product-lead.md
- Done when: A stakeholder can read once and know the decision required.

## `write-prd`

- Description: Write a delivery-grade PRD with scope, scenarios, decisions, and acceptance criteria.
- Trigger: When engineering or design need a precise product spec.
- Primary MCP/tool: notion, repository
- Fallback: reference/ground, search_query
- Best guess: A PRD or equivalent product specification.
- Output: logs/active/<project-slug>/deliverables/product-lead.md
- Done when: Executors can build without product ambiguity.
