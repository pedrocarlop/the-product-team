---
name: performance-investigation
description: Diagnose a platform or system performance issue and localize the bottleneck.
trigger: When performance is degraded and root cause is unclear.
primary_mcp: repository
fallback_tools: search_query, reference/trace
best_guess_output: A performance investigation with bottleneck and next step.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
done_when: The main performance constraint is identified credibly.
---

# Performance Investigation

## Purpose

Diagnose a platform or system performance issue and localize the bottleneck.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When performance is degraded and root cause is unclear.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/trace`.
- If both primary and fallback paths fail, produce the best-guess output described as: A performance investigation with bottleneck and next step.
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

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: The main performance constraint is identified credibly.
