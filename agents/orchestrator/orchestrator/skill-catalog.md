# Orchestrator Skill Catalog

Read this file first on every request before meaningful work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `approve`

- Description: Present the proposed workflow to the user and capture approval before substantial staffed execution.
- Trigger: Before multi-role execution or any costly external action.
- Primary MCP/tool: conversation context
- Fallback: orchestrator/log
- Best guess: A user-facing approval summary with scope, roles, and risks.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: The user can clearly approve or redirect the planned workflow.

## `coordinate`

- Description: Launch specialists in sequence, pass artifact paths, and enforce evidence_mode reporting.
- Trigger: After staffing approval or while running a staged workflow.
- Primary MCP/tool: logs, subagents
- Fallback: orchestrator/log, context review
- Best guess: An up-to-date execution state with handoffs and blocker handling.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: Every active stage has one owner and downstream roles can read their inputs directly.

## `log`

- Description: Keep context.md concise and current with role assignments, skill paths, and done-when criteria.
- Trigger: Any time routing, staffing, status, or risks change.
- Primary MCP/tool: logs
- Fallback: repository review
- Best guess: A refreshed context entry that reflects the true current state.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: A teammate can resume from context.md without guessing.

## `reconcile`

- Description: Merge conflicting specialist outputs into one executable direction without losing critical details.
- Trigger: When staffed roles disagree or outputs conflict.
- Primary MCP/tool: deliverables, context
- Fallback: reference/trace, reference/verify
- Best guess: A reconciled direction with explicit decisions and surviving details.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: Only one downstream direction remains and disputed points are resolved.

## `retrospect`

- Description: Identify recurring workflow failures and propose targeted prompt, skill, or validation fixes.
- Trigger: When the same failure pattern repeats across requests or roles.
- Primary MCP/tool: timeline, context, deliverables
- Fallback: repository review
- Best guess: A concrete system fix proposal tied to evidence.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: The root cause, fix location, and verification path are explicit.

## `route`

- Description: Decide direct execution vs orchestration, choose the right role, and assign exact skill paths for the task.
- Trigger: Every new request or material scope reset.
- Primary MCP/tool: repository, logs
- Fallback: reference/ground, role-catalog review
- Best guess: A routing decision with roles, skill_paths, and execution mode.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: context.md routing block is current and the next owner is unambiguous.

## `staff`

- Description: Select the minimum viable team, assign contracts, and set primary_tools plus fallback policy.
- Trigger: Once orchestration is needed or a staffed role must change.
- Primary MCP/tool: repository, role metadata
- Fallback: reference/verify, context review
- Best guess: A staffing table with role, skill_paths, primary_tools, and fallback policy.
- Output: logs/active/<project-slug>/deliverables/orchestrator.md
- Done when: Every staffed role has one contract and no overlapping repo ownership.
