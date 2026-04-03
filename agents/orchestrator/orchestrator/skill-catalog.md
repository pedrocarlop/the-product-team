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
- Output: logs/active/<project-slug>/deliverables/orchestrator-approve.md
- Done when: The user can clearly approve or redirect the planned workflow.

## `coordinate`

- Description: Launch specialists in sequence, curate the Execution Manifest, and ensure lossless handoff to downstream roles.
- Trigger: After staffing approval or while running a staged workflow.
- Primary MCP/tool: logs, subagents
- Fallback: orchestrator/log, context review
- Best guess: An Execution Manifest indexing all specialist deliverables with status and path.
- Output: logs/active/<project-slug>/deliverables/orchestrator-coordinate.md
- Done when: Every specialist output is indexed in the manifest and implementation owners can access all original source materials.

## `log`

- Description: Keep context.md concise and current with role assignments, skill paths, and done-when criteria.
- Trigger: Any time routing, staffing, status, or risks change.
- Primary MCP/tool: logs
- Fallback: repository review
- Best guess: A refreshed context entry that reflects the true current state.
- Output: logs/active/<project-slug>/deliverables/orchestrator-log.md
- Done when: A teammate can resume from context.md without guessing.

## `reconcile`

- Description: Merge conflicting specialist outputs into one executable direction without losing critical details.
- Trigger: When staffed roles disagree or outputs conflict.
- Primary MCP/tool: deliverables, context
- Fallback: reference/trace, reference/verify
- Best guess: A reconciled direction with explicit decisions and surviving details.
- Output: logs/active/<project-slug>/deliverables/orchestrator-reconcile.md
- Done when: Only one downstream direction remains and disputed points are resolved.

## `retrospect`

- Description: Identify recurring workflow failures and propose targeted prompt, skill, or validation fixes.
- Trigger: When the same failure pattern repeats across requests or roles.
- Primary MCP/tool: timeline, context, deliverables
- Fallback: repository review
- Best guess: A concrete system fix proposal tied to evidence.
- Output: logs/active/<project-slug>/deliverables/orchestrator-retrospect.md
- Done when: The root cause, fix location, and verification path are explicit.

## `route`

- Description: Decide direct execution vs orchestration, choose the right role, and assign exact skill paths for the task.
- Trigger: Every new request or material scope reset.
- Primary MCP/tool: repository, logs
- Fallback: reference/ground, role-catalog review
- Best guess: A routing decision with roles, skill_paths, and execution mode.
- Output: logs/active/<project-slug>/deliverables/orchestrator-route.md
- Done when: context.md routing block is current and the next owner is unambiguous.

## `setup-check`

- Description: Handle an hta_setup_required signal — pause execution, ask the prompter to configure the HTA or authorize fallback, then resume.
- Trigger: When a subagent returns hta_setup_required during coordinate.
- Primary MCP/tool: conversation context
- Fallback: orchestrator/log
- Best guess: A resolved HTA decision (configure or fallback) logged to context.md.
- Output: logs/active/<project-slug>/deliverables/orchestrator-setup-check.md
- Done when: HTA is either configured and verified, or fallback is explicitly authorized by the prompter.

## `staff`

- Description: Select the right-sized team, assign lossless contracts, and set primary_tools plus fallback policy.
- Trigger: Once orchestration is needed or a staffed role must change.
- Primary MCP/tool: repository, role metadata
- Fallback: reference/verify, context review
- Best guess: A staffing table with role, skill_paths, target_deliverables, primary_tools, and fallback policy.
- Output: logs/active/<project-slug>/deliverables/orchestrator-staff.md
- Done when: Every staffed role has one contract and target deliverables are explicitly named for each assigned skill.
