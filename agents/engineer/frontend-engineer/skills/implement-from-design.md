---
name: implement-from-design
description: Implement a design faithfully in production code with the required states and interactions.
trigger: When approved design work is ready for implementation.
primary_mcp: repository, figma
fallback_tools: chrome_devtools, reference/trace
best_guess_output: Working UI implementation aligned to the design spec.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
done_when: The implemented surface matches the intended structure and behavior.
---

# Implement From Design

## Purpose

Implement a design faithfully in production code with the required states and interactions.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: frontend-engineer
project: <slug>
deliverable: frontend-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When approved design work is ready for implementation.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `chrome_devtools, reference/trace`.
- If both primary and fallback paths fail, produce the best-guess output described as: Working UI implementation aligned to the design spec.
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

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: The implemented surface matches the intended structure and behavior.
