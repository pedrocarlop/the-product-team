---
name: prototype-and-usability-validation
description: Build and validate a prototype to test whether the proposed interaction actually works.
trigger: When a flow or concept should be tested before full build.
primary_mcp: paper
fallback_tools: figma, browser inspection
best_guess_output: A prototype summary with validation findings.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
done_when: The prototype answers a real decision and any unresolved risk is explicit.
---

# Prototype And Usability Validation

## Purpose

Build and validate a prototype to test whether the proposed interaction actually works.

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
- Restate the task in terms of this skill's trigger: When a flow or concept should be tested before full build.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `paper`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, browser inspection`.
- If both primary and fallback paths fail, produce the best-guess output described as: A prototype summary with validation findings.
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
- Ensure the work meets this done-when bar: The prototype answers a real decision and any unresolved risk is explicit.
