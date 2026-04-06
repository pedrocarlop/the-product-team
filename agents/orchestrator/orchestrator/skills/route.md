---
name: route
description: Decide direct execution vs orchestration, choose the right role, and assign exact skill paths for the task.
trigger: Every new request or material scope reset.
primary_mcp: repository, logs
fallback_tools: reference/ground, role-catalog review
best_guess_output: A routing decision with roles, skill_paths, and execution mode.
output_artifacts: knowledge/orchestrator-route.md
done_when: context.md routing block is current and the next owner is unambiguous.
---

# Route

## Purpose

Decide direct execution vs orchestration, choose the right role, and assign exact skill paths for the task.

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
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: Every new request or material scope reset.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 2b: Project Maturity & Context Check
- Check `context.md` and `TIMELINE.md` for project maturity.
- If it is a new venture (no code, no context), prioritize **Venture Discovery** and **Foundational Research**.
- If it is an evolving project (existing code, deep context), look for "Incremental Value-Add" opportunities.

### Step 2b-ii: Knowledge Continuity Scan (Progressive Disclosure)
1. Read `knowledge/index.md` to identify relevant domain categories for this request.
2. Read the tail of `knowledge/log.md` (last 20 entries) to see recent mutations.
3. Read TL;DR sections of deliverables in the matching categories.
4. Read full deliverables only for files directly relevant to the current request.
5. Follow `related` links for additional cross-cutting context.
- All relevant files must be included in `reads_from` when staffing agents downstream so that decisions compound across projects.

### Step 2c: Signal Scan For Specialized Roles & Value-Add
Before choosing a team pattern, scan the request for signals that indicate specialized roles are needed. Consult the **Signal-Based Role Triggers** table in `references/role-catalog.md`. For each signal detected:
- Note the associated primary role.
- **Identify Secondary Value-Add Roles**: For every primary role, suggest at least one adjacent discipline for a "Lean Pass" (e.g., Engineering feasibility for a new Design journey).
- Check whether excluding these roles would degrade the outcome.
- If yes, include them in the routing decision with an explicit `assignment_mode`.

Do not default to a single-role execution without first checking for cross-functional value.

### Step 2d: Ship Mode Detection

After scanning for roles, check whether the request is a **ship request** — explicitly asking to get working, deployed software (signals: "ship it", "make it work", "get it to green", "run it and fix it", "close the loop").

If ship mode is detected:
- Route the final stage to `frontend-engineer` with `skill_paths: ["executor"]`
- The executor stage must be the **last** stage in the pipeline — it runs after all design, spec, and implementation stages are complete
- Include in the executor assignment: `reads_from: ["knowledge/**"]`, `repo_write_scope` (explicit and bounded), and `done_when` criteria
- Do NOT staff the executor alongside implementation stages — it must run after them, not in parallel
- If implementation stages have not run yet (no `knowledge/frontend-engineer-implement-from-design.md` exists), run them first and route the executor as a downstream stage

If ship mode is NOT detected (research, design, spec, or partial implementation requested), do not add the executor stage.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, logs`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, role-catalog review`.
- If both primary and fallback paths fail, produce the best-guess output described as: A routing decision with roles, skill_paths, and execution mode.
- Mark the deliverable header and narrative as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.

### Step 4: Produce The Deliverable
- Synthesize the result into the owned deliverable with concrete findings, decisions, or instructions.
- Keep assumptions explicit, especially when using fallback or inferred mode.
- Carry forward any details downstream roles must preserve.

### Step 5: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

