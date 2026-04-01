---
name: handoff-spec
description: Prepare the structured design handoff for downstream UI, content, and engineering work.
trigger: When discovery and flow work must be handed downstream.
primary_mcp: notion, figma
fallback_tools: paper, reference/verify
best_guess_output: A handoff spec linking flow, structure, and open questions.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
done_when: A downstream role can continue without reopening the design problem.
---

# Handoff Spec

## Purpose

Prepare the structured design handoff for downstream UI, content, and engineering work.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: product-designer
project: <slug>
deliverable: product-designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When discovery and flow work must be handed downstream.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/verify`.
- If both primary and fallback paths fail, produce the best-guess output described as: A handoff spec linking flow, structure, and open questions.
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

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: A downstream role can continue without reopening the design problem.
