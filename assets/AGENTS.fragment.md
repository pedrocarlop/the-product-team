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
- When staffing specialists, every assignment must define `assignment_mode`, `owned_outputs`, `reads_from`, `repo_write_owner`, `repo_write_scope`, and `return_expected`.
- Staffed specialists may always write their owned `/logs` artifacts. Repo-tracked app code must have one explicit implementation owner per stage.
- If a staffed implementation owner exists for the current stage, the orchestrator must stop main-thread repo implementation unless it explicitly resets routing back to direct execution.
- During execution, keep approved detail alive until a newer deliverable supersedes it.
- Do not reopen the process piecemeal during execution. If the plan materially changes, rerun the full cycle through the orchestrator.
- Let staffed archetypes route internally across their discipline groups instead of spawning extra same-domain handoffs.
- Read installed role definitions in `.codex/agents/product-team-<discipline>/<role>/`.
- Each staffed archetype must quickly scan its own role-local `skill-catalog.md`, open only the matching local skill files, and end its closing handoff with `Read <skill-paths> skills for this task.`
- Use `.codex/product-team/references/role-catalog.md` as the canonical staffing reference.

## Verification

- Before considering any task complete, verify that all changes pass the relevant tests, linting, formatting, and type-checks.
- Every project `context.md` must include a `Done when` section with concrete, verifiable completion criteria.
- If the user did not specify completion criteria, infer reasonable defaults (tests pass, behavior verified, linting clean) and write them explicitly.
- Do not close a project until every `Done when` item is satisfied or explicitly marked as deferred with a reason.
- For frontend work, additionally verify that pages load on both desktop and mobile and that design litmus checks pass (see role-local frontend-design skills).

## Prompt Structure

For best results, structure requests with:
- **Goal**: what you want to achieve
- **Context**: relevant background, files, prior decisions
- **Constraints**: timelines, technologies, patterns to follow
- **Done when**: concrete criteria for when the task is complete

## Reasoning Calibration

Not every task needs maximum reasoning. The orchestrator will calibrate reasoning effort when staffing specialists:
- **Medium**: simple, well-scoped, single-domain tasks (fix a typo, add a field, rename a variable)
- **High**: typical implementation and design tasks (default for most work)
- **Extra-high**: genuinely complex coordination, long-horizon autonomous work, novel architecture
