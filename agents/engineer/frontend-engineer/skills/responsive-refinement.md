---
name: responsive-refinement
description: Adapt or improve the surface so it works cleanly across breakpoints and devices.
trigger: When responsive behavior is missing or under-specified.
primary_mcp: repository, chrome_devtools
fallback_tools: figma, reference/verify
best_guess_output: A responsive implementation or refinement pass.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
done_when: Desktop and mobile behavior are both acceptable and intentional.
---

# Responsive Refinement

## Purpose

Adapt or improve the surface so it works cleanly across breakpoints and devices.

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
- Restate the task in terms of this skill's trigger: When responsive behavior is missing or under-specified.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, reference/verify`.
- If both primary and fallback paths fail, produce the best-guess output described as: A responsive implementation or refinement pass.
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
- Ensure the work meets this done-when bar: Desktop and mobile behavior are both acceptable and intentional.
