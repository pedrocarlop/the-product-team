# `/logs` Workflow Contract

`/logs` is the only persistent project-memory and handoff surface for the orchestrator-centered workflow.

## Project Slug

Use `logs/active/<project-slug>/` for active work.

- Format: `YYYYMMDD-<kebab-case-objective>`
- Collision handling: append `-2`, `-3`, and so on

## Directory Layout

```text
logs/
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
- Best possible team assessment
- Direct execution vs workflow decision
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
- Fit-check outcomes
- Advisory assignments for planning
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

Direct execution is for bounded tactical work and should be chosen only after the best-team assessment shows specialist staffing would not materially improve the outcome.

## Orchestrated Execution

Orchestrated work must:

- Use one role per subagent
- Require fit-check before ownership is accepted
- Require a role plan in `plans/<role>.md`
- Treat role plans as advisory input to the orchestrator, not as permission to execute or redefine the team process
- Merge role advice into one authoritative `03_unified-plan.md` before execution starts
- Pause for approval before substantial execution
- Start from the best-team assessment and staff only the minimum viable team
- Execute the approved cycle before allowing another material planning iteration, unless the orchestrator explicitly pauses and resets the workflow
- Store deliverables, reviews, and decision history in `/logs`

## Archive

Move completed or abandoned projects from `logs/active/` to `logs/archive/` only after `status.md` and `context.md` are current enough for a future continuation or audit.
