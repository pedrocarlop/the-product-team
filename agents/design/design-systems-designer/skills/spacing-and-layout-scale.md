---
name: spacing-and-layout-scale
description: Define the spacing, sizing, and layout scale that underpins UI consistency.
trigger: When system consistency depends on clearer spatial rules.
primary_mcp: figma
fallback_tools: paper, repository
best_guess_output: A spacing and layout scale with usage guidance.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md
done_when: Designers can compose surfaces without inventing spacing ad hoc.
---

# Spacing And Layout Scale

## Purpose

Define the spacing, sizing, and layout scale that underpins UI consistency.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: design-systems-designer
project: <slug>
deliverable: design-systems-designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When system consistency depends on clearer spatial rules.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, repository`.
- If both primary and fallback paths fail, produce the best-guess output described as: A spacing and layout scale with usage guidance.
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

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: Designers can compose surfaces without inventing spacing ad hoc.
