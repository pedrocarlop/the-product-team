---
name: study-ops-and-recruiting
description: Define the operational plan for scheduling, recruiting, consent, and study logistics.
trigger: When research needs a concrete execution plan beyond the study design.
primary_mcp: notion, google_forms
fallback_tools: ux-researcher/screener-form-build, open
best_guess_output: A study ops plan with recruiting flow and logistics.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
done_when: The study can be scheduled and staffed cleanly.
---

# Study Ops And Recruiting

## Purpose

Define the operational plan for scheduling, recruiting, consent, and study logistics.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: ux-researcher
project: <slug>
deliverable: ux-researcher.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When research needs a concrete execution plan beyond the study design.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion, google_forms`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `ux-researcher/screener-form-build, open`.
- If both primary and fallback paths fail, produce the best-guess output described as: A study ops plan with recruiting flow and logistics.
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

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: The study can be scheduled and staffed cleanly.
