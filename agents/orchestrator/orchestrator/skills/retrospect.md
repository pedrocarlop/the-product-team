---
name: retrospect
description: Identify recurring workflow failures and propose targeted prompt, skill, or validation fixes.
trigger: When the same failure pattern repeats across requests or roles.
primary_mcp: timeline, context, deliverables
fallback_tools: repository review
best_guess_output: A concrete system fix proposal tied to evidence.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator-retrospect.md
done_when: The root cause, fix location, and verification path are explicit.
---

# Retrospect

## Purpose

Identify recurring workflow failures and propose targeted prompt, skill, or validation fixes.

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
- Restate the task in terms of this skill's trigger: When the same failure pattern repeats across requests or roles.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `timeline, context, deliverables`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `repository review`.
- If both primary and fallback paths fail, produce the best-guess output described as: A concrete system fix proposal tied to evidence.
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

