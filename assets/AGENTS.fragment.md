# Product Team for Codex

This repository has the Product Team workflow installed.

## Entry Point

- Route every request in this repository through `product-team-orchestrator` by default.
- Only bypass Product Team when the user explicitly says not to use Product Team, not to use the orchestrator, or otherwise asks to work outside the workflow for that request.
- Do not infer an opt-out from simplicity, urgency, or implementation bias alone.
- Default to direct Codex execution inside `product-team-orchestrator` for single-domain, implementation-first, clearly scoped work.
- Route by domain before staffing. Consult only the relevant discipline slice of `.codex/product-team/references/role-catalog.md` when the domain is obvious; read the full catalog only for ambiguous or cross-functional work.
- On every request, estimate whether specialist coordination will materially improve the outcome over direct execution. If not, stay direct within the orchestrator.
- When Product Team is active, `/logs` stores project context for continuity across conversations.

## Workflow Rules

- On every request, the orchestrator must quickly scan its own role-local `skill-catalog.md`, open the matching orchestrator skills relevant to the task, and use them whether the workflow stays direct or staffs subagents.
- Keep one archetype per subagent.
- Staff the minimum viable set of specialists.
- Base staffing on actual role needs, not task keywords alone.
- Let specialists accept assignments directly unless there is a clear mismatch, missing dependency, or ownership conflict.
- Request role plans only when written specialist advice is genuinely needed.
- Orchestration, routing, staffing, and planning happen in the context window. Only persist the project context (`context.md`) and deliverables to `/logs`.
- Get explicit approval before substantial multi-role execution.
- During execution, keep approved detail alive until a newer deliverable supersedes it.
- Do not reopen the process piecemeal during execution. If the plan materially changes, rerun the full cycle through the orchestrator.
- Let staffed archetypes route internally across their discipline groups instead of spawning extra same-domain handoffs.
- Read installed role definitions in `.codex/agents/product-team-<discipline>/<role>/`.
- Each staffed archetype must quickly scan its own role-local `skill-catalog.md`, open only the matching local skill files, and end its closing handoff with `Read <skill-paths> skills for this task.`
- Use `.codex/product-team/references/role-catalog.md` as the canonical staffing reference.
