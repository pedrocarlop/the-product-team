---
name: route
description: Decide direct execution vs orchestration, choose the right role, and assign exact skill paths for the task.
trigger: Every new request or material scope reset.
primary_mcp: repository, logs
fallback_tools: reference/ground, role-catalog review
best_guess_output: A routing decision with roles, skill_paths, and execution mode.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator-route.md
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

