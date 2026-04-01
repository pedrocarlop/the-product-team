# Business Ops Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `execution-tracker`

- Description: Create the tracking model for operational follow-through and accountability.
- Trigger: When a plan needs an execution dashboard or tracker.
- Primary MCP/tool: linear, notion
- Fallback: business-ops/workflow-design
- Best guess: An execution tracking model with owners, status, and escalation rules.
- Output: logs/active/<project-slug>/deliverables/business-ops.md
- Done when: The team can track real work without ambiguity.

## `operating-rhythm`

- Description: Design the recurring meetings, checkpoints, and decision cadence for a team.
- Trigger: When the team needs a clearer operating system.
- Primary MCP/tool: notion, linear
- Fallback: business-ops/process-map
- Best guess: An operating rhythm proposal with ceremonies and decision points.
- Output: logs/active/<project-slug>/deliverables/business-ops.md
- Done when: The cadence is concrete enough to run next week.

## `process-map`

- Description: Map the current and target process so gaps and handoffs are visible.
- Trigger: When a workflow is unclear, inefficient, or changing.
- Primary MCP/tool: notion
- Fallback: search_query, reference/ground
- Best guess: A current-state and future-state process map.
- Output: logs/active/<project-slug>/deliverables/business-ops.md
- Done when: Owners, steps, and gaps are explicit.

## `tooling-audit`

- Description: Assess tool sprawl, gaps, and ownership across the operating stack.
- Trigger: When systems or tools are slowing execution down.
- Primary MCP/tool: notion, repository
- Fallback: search_query, reference/ground
- Best guess: A tooling audit with keep/change/remove recommendations.
- Output: logs/active/<project-slug>/deliverables/business-ops.md
- Done when: The stack decision is actionable and justified.

## `workflow-design`

- Description: Define a new operational workflow with roles, triggers, and artifacts.
- Trigger: When work needs a repeatable operating model.
- Primary MCP/tool: notion, repository
- Fallback: business-ops/process-map, reference/reuse
- Best guess: A workflow definition with triggers, owners, and outputs.
- Output: logs/active/<project-slug>/deliverables/business-ops.md
- Done when: A team can follow the workflow without inventing steps.
