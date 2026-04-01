---
name: coordinate
description: Launch specialists in sequence, pass artifact paths, and enforce evidence_mode reporting.
trigger: After staffing approval or while running a staged workflow.
primary_mcp: logs, subagents
fallback_tools: orchestrator/log, context review
best_guess_output: An up-to-date execution state with handoffs and blocker handling.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator.md
done_when: Every active stage has one owner and downstream roles can read their inputs directly.
---

# Coordinate

## Purpose

Launch specialists in sequence, pass artifact paths, and enforce evidence_mode reporting.

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
- Restate the task in terms of this skill's trigger: After staffing approval or while running a staged workflow.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `logs, subagents`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `orchestrator/log, context review`.
- If both primary and fallback paths fail, produce the best-guess output described as: An up-to-date execution state with handoffs and blocker handling.
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

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/orchestrator.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: Every active stage has one owner and downstream roles can read their inputs directly.
