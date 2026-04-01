# Orchestrator Skill Catalog

Read this file first on every request before meaningful work.
It lists only the role-local skills in this folder and keeps descriptions short so you can scan cheaply.
Open only the matching skill files under `skills/`, then end your closing handoff with `Read <skill-paths> skills for this task.`

## Additional Skills

- `approve` — Present the plan to the user and capture approval before substantial execution.
- `coordinate` — Run the execution sequence across staffed specialists — launch agents, pass deliverables, handle errors, and keep context current. Use after approval or when direct execution has been chosen and needs orchestrated handoffs.
- `log` — Keep the project context.md concise and current.
- `reconcile` — Merge specialist input into one coherent execution plan.
- `retrospect` — Analyze recurring mistakes or quality issues and propose targeted instruction updates to prevent them. Use when the user reports a repeated mistake, when the same issue appears across multiple timeline entries, when a specialist repeatedly returns mismatches, or when the user explicitly asks for process improvement.
- `route` — Decide whether a request should be handled via direct execution or routed into the multi-agent workflow. Use at the start of every new request. Determines the execution mode, creates the project context, and appends to the timeline.
- `staff` — Select the minimum viable role set for an orchestrated task, assign ownership, and set reasoning calibration. Use after routing decides orchestration is needed, or when a staffed role may be redundant, missing, or incorrectly assigned.
