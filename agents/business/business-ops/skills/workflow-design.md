---
name: workflow-design
description: Define a new operational workflow with roles, triggers, and artifacts.
trigger: When work needs a repeatable operating model.
primary_mcp: notion, repository
fallback_tools: business-ops/process-map, reference/reuse
best_guess_output: A workflow definition with triggers, owners, and outputs.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops.md
done_when: A team can follow the workflow without inventing steps.
---

# Workflow Design

## Purpose

Define a new operational workflow with roles, triggers, and artifacts.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: business-ops
project: <slug>
deliverable: business-ops.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When work needs a repeatable operating model.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `business-ops/process-map, reference/reuse`.
- If both primary and fallback paths fail, produce the best-guess output described as: A workflow definition with triggers, owners, and outputs.
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

- Write or update `logs/active/<project-slug>/deliverables/business-ops.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: A team can follow the workflow without inventing steps.
