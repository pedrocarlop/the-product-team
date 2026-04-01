---
name: release-gate
description: Make the final ship/no-ship recommendation based on requirements, testing, and runtime evidence.
trigger: When work is nearing release and needs a QA gate.
primary_mcp: repository, deliverables
fallback_tools: qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review
best_guess_output: A release gate recommendation with blocking issues and residual risk.
output_artifacts: logs/active/<project-slug>/deliverables/qa-reviewer.md
done_when: The release recommendation is unambiguous and evidence-based.
---

# Release Gate

## Purpose

Make the final ship/no-ship recommendation based on requirements, testing, and runtime evidence.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: qa-reviewer
project: <slug>
deliverable: qa-reviewer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When work is nearing release and needs a QA gate.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, deliverables`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review`.
- If both primary and fallback paths fail, produce the best-guess output described as: A release gate recommendation with blocking issues and residual risk.
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

- Write or update `logs/active/<project-slug>/deliverables/qa-reviewer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: The release recommendation is unambiguous and evidence-based.
