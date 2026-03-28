# Product Team for Codex

This repository has the Product Team workflow installed.

## Entry Point

- Use `product-team-orchestrator` as the coordination entrypoint for cross-functional, ambiguous, staged, or review-heavy work.
- Default to direct Codex execution for single-domain, implementation-first, clearly scoped work.
- Route by domain before staffing. Consult only the relevant discipline slice of `.codex/product-team/references/role-catalog.md` when the domain is obvious; read the full catalog only for ambiguous or cross-functional work.
- On every request, estimate whether specialist coordination will materially improve the outcome over direct execution. If not, stay direct.
- If you engage the workflow, `/logs` is the only persistent project-memory and handoff surface.

## Workflow Rules

- Keep one archetype per subagent.
- Staff the minimum viable set of specialists.
- Base staffing on actual role needs, not task keywords alone.
- Let specialists accept assignments directly unless there is a clear mismatch, missing dependency, or ownership conflict.
- Request role plans only when written specialist advice is genuinely needed.
- Let the orchestrator define the merged process in `03_unified-plan.md`.
- Get explicit approval before substantial multi-role execution.
- If the orchestrator pauses for approval, it must summarize the plan, point to `03_unified-plan.md`, `04_approval.md`, `status.md`, and `context.md`, and end by asking "Do you want to proceed?"
- Do not reopen the process piecemeal during execution. If the plan materially changes, rerun the full cycle through the orchestrator.
- Let staffed archetypes route internally across their discipline groups instead of spawning extra same-domain handoffs.
- Read installed role definitions in `.codex/agents/product-team-<discipline>/<role>/`.
- Each staffed archetype must quickly scan its own role-local `skill-catalog.md`, open only the matching local skill files, and end its closing handoff with `Read <skill-paths> skills for this task.`
- Use `.codex/product-team/references/role-catalog.md` as the canonical staffing reference.
- Use `.codex/product-team/references/logs-workflow-contract.md` as the canonical `/logs` contract reference when the target repo's own docs are silent.
