---
name: coordinate
description: "Run the execution sequence across staffed specialists — launch agents, pass deliverables, handle errors, and keep context current. Use after approval or when direct execution has been chosen and needs orchestrated handoffs."
---

# Coordinate

## Overview

The execution spine of the orchestrator. Coordinate launches specialists in the right order, ensures deliverables flow correctly between them, handles mid-execution surprises, and keeps `context.md` as the single source of truth. A weak coordinator drops context, orphans deliverables, or lets specialists drift off-task.

## When to Use

- After `staff` and `approve` have completed and execution is greenlit.
- During direct execution when the orchestrator needs to sequence file reads, tool calls, or specialist invocations.
- When a specialist completes and the next step in the sequence must begin.

## When Not to Use

- Before the routing and staffing decisions are made (use `route` and `staff` first).
- When the user has not approved a multi-role execution plan.

## Prerequisites

- `context.md` exists with objective, staffing, sequencing, and done-when criteria.
- Staffing decision is finalized (roles, ownership, sequencing).
- User approval is obtained for substantial multi-role work.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: orchestrator
project: <slug>
deliverable: orchestrator.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

### Step 2: Determine Execution Mode

Based on the staffing decision, choose:

| Mode | When | How |
|------|------|-----|
| **Sequential** | Role B needs Role A's output | Launch A → wait → pass deliverable → launch B |
| **Parallel** | Roles are independent | Launch A + B simultaneously → collect results |
| **Mixed** | Some parallel, some sequential | Parallel phase → sync point → sequential phase |

```
Can the next role start without the current role's deliverable?
├── YES → Run in parallel.
└── NO → Run sequentially (wait for deliverable).
```

### Step 3: Launch Specialists

For each specialist in the execution order:

1. **Compose the assignment**: include only what the specialist needs:
   - Their role and owned deliverable path.
   - The `context.md` reference.
   - Any upstream deliverable paths they should read.
   - The `skill_hint` from staffing (if set).
   - Specific constraints or decisions from the orchestrator.
   - The explicit assignment contract fields: `assignment_mode`, `owned_outputs`, `reads_from`, `repo_write_owner`, `repo_write_scope`, and `return_expected`.

   Use this contract shape:

   ```text
   assignment_mode: <plan | deliverable | implementation>
   owned_outputs:
   - <path>
   reads_from:
   - <path>
   repo_write_owner: <role-name | none>
   repo_write_scope:
   - <repo path or bounded area>
   return_expected: <deliverable | mismatch note | blocker | completion signal>
   ```

   If `assignment_mode` is not `implementation`, set `repo_write_owner: none` and leave `repo_write_scope` empty.
   If a specialist is the repo-write owner, make the scope explicit and bounded.

2. **Spawn the subagent** with the assignment.

3. **Specify return expectations**: what the specialist should return (deliverable, mismatch note, blocker, or completion signal).

### Step 4: Pass Deliverables Between Roles

Deliverables flow through files, not through the orchestrator's context compression:

```
designer writes → logs/active/<slug>/deliverables/designer.md
engineer reads  → logs/active/<slug>/deliverables/designer.md (directly)
```

**Deliverable passing rules:**
- Sequential roles read upstream deliverables directly from the `deliverables/` folder.
- Do not compress, summarize, or relay deliverable content through `context.md` — this loses critical detail.
- The orchestrator passes the _path_, not the _content_.
- Each specialist is responsible for reading its input deliverables at execution start.
- Repo-tracked app code has a separate handoff rule: one explicit `repo_write_owner` per stage by default.
- If you intentionally run parallel repo writers, their `repo_write_scope` values must be disjoint and stated in both assignments.

### Step 5: Monitor Execution and Verify Handoffs

While specialists are running:

- **For parallel agents**: wait for all to complete before proceeding to the sync point.
- **For sequential agents**: wait for each to complete, then **Verify the Artifact Handshake**:
    1. **Check YAML Header**: Does `logs/active/<slug>/deliverables/<role>.md` start with the required YAML block?
    2. **Check Reflection**: Does the file end with a `## Reflection` section?
    3. **Evaluate Confidence**: If the specialist reported `confidence < 0.7` in the header, the Orchestrator must read the reflection to decide if remedial action is needed.
    4. **Check Repo Ownership**: Did only the named `repo_write_owner` edit repo-tracked code for this stage, and did it stay within the assigned `repo_write_scope`?

- If a specialist returns a **mismatch note**: pause, evaluate, and decide whether to reassign, adjust scope, or escalate to the user.
- If a specialist returns a **blocker**: pause the sequence, resolve the blocker, then resume.

### Step 6: Handle Mid-Execution Changes (Plan Calibration)

If execution reveals something that changes the plan, or if a **Reflection** indicates a material risk:

```
Is the change or reflection risk material?
├── YES → Pause execution.
│   ├── Update context.md with the new risk/understanding.
│   ├── Re-evaluate staffing or reasoning levels.
│   └── If resetting, inform the user and get approval.
└── NO → Note it in context.md and continue.
```

**Never** improvise piecemeal adjustments mid-cycle. Either finish the current cycle or explicitly reset — no hybrid improvisation.

**Never** improvise piecemeal adjustments mid-cycle. Either finish the current cycle or explicitly reset — no hybrid improvisation.

### Step 7: Update Context

After each significant execution event, update `context.md`:

| Event | Context Update |
|-------|---------------|
| Specialist launched | Status: `<role> executing` |
| Specialist completed | Status: `<role> done`, note deliverable path |
| Blocker encountered | Status: `blocked on <description>`, add to open questions |
| Plan changed | Update staffing/sequencing sections |
| Phase completed | Summary of what was delivered |

Keep updates **concise**. Context.md is a live status document, not a log of everything that happened.

### Step 8: Close the Loop

When all specialists have completed and their deliverables are filed:

1. Verify each `Done when` criterion from `context.md` is satisfied.
2. If a reviewer is staffed, launch the review pass now.
3. Summarize the outcome to the user.
4. Move completed projects to `logs/archive/` if finished, or update status if ongoing.

### Step 9: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Worked Examples

### Example 1: Sequential Two-Role Flow
**Task:** Design and implement a settings page.

**Sequence:**
1. Launch `designer` with `context.md` → designer writes `deliverables/designer.md`.
2. Wait for designer to complete.
3. Launch `engineer` with `context.md` and `deliverables/designer.md` path.
4. Engineer reads designer's deliverable directly, implements, writes `deliverables/engineer.md`.
5. Update `context.md` status → done.

### Example 2: Parallel Exploration
**Task:** Research competitive landscape and define metrics strategy simultaneously.

**Sequence:**
1. Launch `go-to-market` (competitive analysis) and `analyst` (metrics framework) in parallel.
2. Wait for both to complete.
3. Orchestrator reads both deliverables, synthesizes insights for the user.
4. Update `context.md` with combined findings.

### Example 3: Mid-Cycle Replan
**Task:** Build onboarding flow. Designer discovers missing API endpoint during spec.

**Sequence:**
1. Launch `designer` → designer returns mismatch: "need API contract for user preferences."
2. **Pause.** Update `context.md` with the dependency.
3. Launch `platform-engineer` to define the API contract → writes `deliverables/platform-engineer.md`.
4. Resume `designer` with the API contract available.
5. Continue normal sequence → engineer implements.

## Guardrails

- Do not compress deliverable content through orchestrator context — pass file paths and let specialists read directly.
- Do not launch a downstream specialist before its upstream dependency has completed (unless parallelize is explicitly justified).
- Do not continue execution after a specialist reports a material mismatch — pause and evaluate.
- Do not allow duplicate repo owners for the same stage unless you have explicitly assigned disjoint `repo_write_scope` values.
- Do not let `context.md` go stale — update after every significant state change.
- Do not orphan deliverables — every specialist output must be either consumed by a downstream role or presented to the user.
- Do not allow specialists to negotiate the process after the orchestrator sets it — coordination is the orchestrator's job.
- Do not run more than 3 agents in parallel without considering context and token cost.

## Troubleshooting

### Issue: Specialist output doesn't match what the next role expects
**Cause:** The assignment didn't specify the deliverable format clearly enough.
**Solution:** Include explicit deliverable expectations in the assignment: "Write `deliverables/designer.md` covering screen structure, states, tokens, and interaction details."

### Issue: Parallel agents produce conflicting outputs
**Cause:** Independent agents made assumptions that contradict each other.
**Solution:** Reconcile before passing to downstream roles. Use the `reconcile` skill to merge conflicting outputs into a coherent direction.

### Issue: Context.md is stale or inconsistent
**Cause:** Updates were skipped during rapid execution.
**Solution:** Audit `context.md` at each sync point. It should always reflect: current status, completed deliverables, open blockers, and remaining work.

### Issue: Execution is taking too many turns
**Cause:** Over-orchestration — too many roles, too many sequential handoffs.
**Solution:** Ask: "Could I have done this faster with direct execution or fewer roles?" Consider collapsing the remaining work into direct execution.
