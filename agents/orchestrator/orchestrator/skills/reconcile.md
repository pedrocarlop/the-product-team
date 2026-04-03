---
name: reconcile
description: Merge conflicting specialist outputs into one executable direction without losing critical details.
trigger: When staffed roles disagree or outputs conflict.
primary_mcp: deliverables, context
fallback_tools: reference/trace, reference/verify
best_guess_output: A reconciled direction with explicit decisions and surviving details.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator-reconcile.md
done_when: Only one downstream direction remains and disputed points are resolved.
---

# Reconcile

## Purpose

Merge conflicting specialist outputs into one executable direction without losing critical details.

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
- Restate the task in terms of this skill's trigger: When staffed roles disagree or outputs conflict.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `deliverables, context`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, reference/verify`.
- If both primary and fallback paths fail, produce the best-guess output described as: A reconciled direction with explicit decisions and surviving details.
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

