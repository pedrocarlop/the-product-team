---
name: interaction-spec
description: Specify the important interaction rules, state changes, and transitions.
trigger: When implementation needs behavior-level clarity.
primary_mcp: figma, repository
fallback_tools: paper, reference/trace
best_guess_output: An interaction spec tied to states and user actions.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
done_when: An engineer can implement the interaction without guessing behaviors.
---

# Interaction Spec

## Purpose

Specify the important interaction rules, state changes, and transitions.

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
- Restate the task in terms of this skill's trigger: When implementation needs behavior-level clarity.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `figma, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/trace`.
- If both primary and fallback paths fail, produce the best-guess output described as: An interaction spec tied to states and user actions.
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
- Ensure the work meets this done-when bar: An engineer can implement the interaction without guessing behaviors.
