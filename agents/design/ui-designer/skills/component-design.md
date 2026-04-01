---
name: component-design
description: Create or extend reusable UI components needed by the surface.
trigger: When the feature needs reusable UI patterns, not just one-off screens.
primary_mcp: figma
fallback_tools: paper, stitch
best_guess_output: A component proposal or production component design.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
done_when: Component purpose, states, and intended reuse are explicit.
---

# Component Design

## Purpose

Create or extend reusable UI components needed by the surface.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: ui-designer
project: <slug>
deliverable: ui-designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When the feature needs reusable UI patterns, not just one-off screens.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, stitch`.
- If both primary and fallback paths fail, produce the best-guess output described as: A component proposal or production component design.
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

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: Component purpose, states, and intended reuse are explicit.
