# Orchestrator Skill Catalog

Read this file first on every request before meaningful work.
It lists only the role-local skills in this folder and keeps descriptions short so you can scan cheaply.
Open only the matching skill files under `skills/`, then end your closing handoff with `Read <skill-paths> skills for this task.`

## Additional Skills

- `approve` — Present the orchestrated plan to the user, capture feedback, and enforce the approval gate in `04_approval.md`.
- `coordinate` — Run the approved execution sequence, pass inputs between specialists, and keep status current.
- `log` — Maintain the compressed project memory in `/logs`, especially `context.md` and decision history.
- `reconcile` — Turn specialist advice or sequencing constraints into one authoritative staged execution path and record it in `03_unified-plan.md`.
- `route` — Decide whether a request should be executed directly or routed into the multi-agent workflow, then record the decision in `00_routing.md`.
- `staff` — Select the minimum viable archetype set, launch one subagent per staffed archetype, and record ownership decisions in `02_staffing.md`.
