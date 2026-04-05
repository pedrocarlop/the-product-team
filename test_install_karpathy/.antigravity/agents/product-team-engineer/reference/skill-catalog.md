# Reference Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `ground`

- Description: Ground decisions in the real target repo and any named source system before proposing work.
- Trigger: When a role needs factual grounding before choosing a path.
- Primary MCP/tool: repository, named source systems
- Fallback: search_query, open
- Best guess: A concise grounding inventory with sources and unknowns.
- Output: knowledge/reference-ground.md
- Done when: The team can cite concrete repo/system evidence instead of assumptions.

## `reuse`

- Description: Find approved patterns, components, and prior deliverables worth reusing before inventing new ones.
- Trigger: When a task may already be covered by an existing pattern.
- Primary MCP/tool: repository, deliverables
- Fallback: reference/ground, search_query
- Best guess: A reuse recommendation with exact patterns to follow.
- Output: knowledge/reference-reuse.md
- Done when: The preferred reusable pattern is explicit and justified.

## `trace`

- Description: Trace a behavior through files, systems, or deliverables until the real source of truth is clear.
- Trigger: When implementation paths or ownership boundaries are unclear.
- Primary MCP/tool: repository, deliverables
- Fallback: reference/ground, open
- Best guess: A traced path from entry point to source of truth.
- Output: knowledge/reference-trace.md
- Done when: A downstream implementer knows exactly where the change lands.

## `verify`

- Description: Re-open evidence and confirm that the chosen conclusion still holds before handoff or approval.
- Trigger: Before finalizing a decision that depends on repo or tool evidence.
- Primary MCP/tool: repository, deliverables
- Fallback: reference/trace, search_query
- Best guess: A pass/fail/unresolved verification result with cited evidence.
- Output: knowledge/reference-verify.md
- Done when: The claimed conclusion is defended by present-state evidence.
