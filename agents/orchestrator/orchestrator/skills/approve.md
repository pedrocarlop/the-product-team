---
name: approve
description: Present the proposed workflow to the user and capture approval before substantial staffed execution.
trigger: Before multi-role execution or any costly external action.
primary_mcp: conversation context
fallback_tools: orchestrator/log
best_guess_output: A user-facing approval summary with scope, roles, and risks.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator-approve.md
done_when: The user can clearly approve or redirect the planned workflow.
---

# Approve

## Purpose

Present the proposed workflow to the user and capture approval before substantial staffed execution.

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
- Restate the task in terms of this skill's trigger: Before multi-role execution or any costly external action.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `conversation context`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `orchestrator/log`.
- If both primary and fallback paths fail, produce the best-guess output described as: A user-facing approval summary with scope, roles, and risks.
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

