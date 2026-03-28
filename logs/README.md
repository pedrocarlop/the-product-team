# `/logs` Workflow Contract

`/logs` is the only persistent project-memory and handoff surface for the direct-first orchestrator workflow.

## Project Slug

Use `logs/active/<project-slug>/` for active work.

- Format: `YYYYMMDD-<kebab-case-objective>`
- Collision handling: append `-2`, `-3`, and so on

## Directory Layout

```text
logs/
  TIMELINE.md
  active/
    <project-slug>/
      00_routing.md
      01_intake.md
      02_staffing.md
      03_unified-plan.md
      04_approval.md
      status.md
      context.md
      plans/
      deliverables/
      reviews/
      decisions/
  archive/
```

## Required Files

`00_routing.md`
- Original request
- Complexity assessment
- Domain classification
- Best possible team assessment
- Direct execution vs workflow decision
- Coordination cost estimate
- Rationale

`01_intake.md`
- Interpreted objective
- Constraints
- Dependencies
- Ambiguities and risks
- Initial staffing hypothesis

`02_staffing.md`
- Created only when orchestration is used
- Selected roles
- One role per subagent
- Assignment confirmations or mismatch notes
- Advisory planning requests, if any
- Final ownership map

`03_unified-plan.md`
- Created only when orchestration is used
- Unified staged plan
- Authoritative execution process for the current cycle
- Ownership by role
- Dependencies and sequence
- Review points
- Approval gate

`04_approval.md`
- Created only when orchestration is used
- Presented plan version
- User feedback
- Approval state
- Approved scope

`status.md`
- Current execution stage
- Active owners
- In-progress work
- Latest completed work
- Blockers
- Next action

`context.md`
- Project goal
- Current cycle and authoritative plan version
- Current state
- Approved direction
- Active roles
- Latest deliverables
- Open questions
- Next step

## Direct Execution

Direct execution still requires:

- `00_routing.md`
- `01_intake.md`
- `status.md`
- `context.md`

It does not require `02_staffing.md`, `03_unified-plan.md`, or `04_approval.md` unless the work is upgraded into orchestration.

Direct execution is the default for single-domain, implementation-first, clearly scoped or easily inferable work where the best-team assessment shows specialist staffing would not materially improve the outcome.

Bypass orchestration when the task is:

- Single-domain
- Implementation-heavy
- Clearly specified or easily inferable
- Unlikely to benefit from cross-functional negotiation

## Role Catalog Usage

- Route by domain before staffing.
- If the domain is obvious, consult only the relevant discipline slice of `references/role-catalog.md`.
- Read the full role catalog only when the task is ambiguous, cross-functional, or the right team is genuinely unclear.

## Orchestrated Execution

Orchestrated work must:

- Use one role per subagent
- Start from the best-team assessment and staff only the minimum viable team
- Let specialists accept assignments directly unless there is a clear mismatch, missing dependency, or ownership conflict
- Request a role plan in `plans/<role>.md` only when written specialist advice will improve ambiguity, tradeoff, or sequencing decisions
- Treat role plans as optional advisory input to the orchestrator, not as permission to execute or redefine the team process
- Let the orchestrator author one authoritative `03_unified-plan.md` before execution starts
- Pause for approval before substantial execution
- Execute the approved cycle before allowing another material planning iteration, unless the orchestrator explicitly pauses and resets the workflow
- Store deliverables, reviews, and decision history in `/logs`

## Status Lifecycle

`status.md` tracks the project through these states:

- **planning**: Routing, intake, and staffing are in progress. No execution has started.
- **in-progress**: The approved plan is being executed. Specialists are producing deliverables.
- **blocked**: Execution is paused due to a dependency, conflict, or external factor. The blocker must be described in `status.md`.
- **complete**: All deliverables are finalized and reviews are done. No further execution is needed.
- **archived**: The project has been moved to `logs/archive/`.

Transitions:
- `planning` → `in-progress`: orchestrator records approval in `04_approval.md`
- `in-progress` → `blocked`: a specialist or orchestrator identifies an unresolvable blocker
- `blocked` → `in-progress`: the blocker is resolved and documented
- `in-progress` → `complete`: all deliverables finalized, reviews done, orchestrator confirms
- `complete` → `archived`: project moved to `logs/archive/`

## Declined-Role Recording

When a specialist declines or flags a mismatch during staffing, record in `02_staffing.md`:

- Role name
- Decline rationale
- Recommended replacement role
- Whether the orchestrator accepted the recommendation or adjusted staffing

## Conflict Resolution

When specialists produce conflicting advice or deliverables:

1. Both positions are documented in `decisions/<topic>.md` with rationale.
2. The orchestrator consults the role whose ownership area covers the disputed scope.
3. The orchestrator makes a binding decision and updates `03_unified-plan.md`.
4. The resolution is recorded in `decisions/` with the reasoning.

## Archive

Move projects from `logs/active/` to `logs/archive/` when any of these conditions are met:

- **Complete**: `status.md` shows `complete` and all deliverables are finalized.
- **Abandoned**: The project is explicitly abandoned. Record the rationale in `context.md` before archiving.
- **Inactive**: The project has been inactive for 30+ days with no pending work items.

Before archiving, ensure `status.md` and `context.md` are current enough for a future continuation or audit.

## Timeline

`TIMELINE.md` is a chronological index of all projects maintained by the orchestrator.

Each row records:

| Column | Content |
|---|---|
| Date | Project start date (YYYY-MM-DD) |
| Slug | Project slug, linked to the project folder |
| Objective | One-line project goal |
| Workflow | `direct` or `orchestrated` |
| Roles | Comma-separated list of staffed roles, or `orchestrator (direct)` |
| Status | Current lifecycle status (`planning`, `in-progress`, `blocked`, `complete`, `archived`) |
| Outcome | One-sentence summary of what was delivered or why the project ended |

Maintenance rules:

- Append a new row when `00_routing.md` is created.
- Update Status when the project transitions (see Status Lifecycle above).
- Update Outcome when the project reaches `complete` or `archived`.
- Update the Slug link when a project moves from `active/` to `archive/`.
- Newest entries go at the bottom.
