# Product Team for Codex

This repository has the Product Team workflow installed.

## Entry Point

- Use `product-team-orchestrator` as the coordination entrypoint for cross-functional, ambiguous, staged, or review-heavy work.
- On every request, first reason about the best possible team for the job. Only skip specialist flow when that team would not materially improve the outcome over direct execution.
- If you engage the workflow, `/logs` is the only persistent project-memory and handoff surface.

## Workflow Rules

- Keep one role per subagent.
- Staff the minimum viable set of specialists.
- Base staffing on actual role needs, not task keywords alone.
- Require the fit-check protocol before a specialist accepts ownership.
- Reconcile role plans before substantial orchestrated execution.
- Get explicit approval before substantial orchestrated execution.
- Read installed role definitions in `.codex/agents/product-team-<discipline>/<role>/`.
- Use `.codex/product-team/references/logs-workflow-contract.md` as the canonical `/logs` contract reference when the target repo's own docs are silent.
