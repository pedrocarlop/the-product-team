---
name: experiment-readout
description: Interpret an experiment and translate the result into a decision.
trigger: When a test or rollout needs analysis and recommendation.
primary_mcp: notion, repository
fallback_tools: analyst/metric-definition, search_query
best_guess_output: An experiment readout with result, confidence, and next step.
output_artifacts: logs/active/<project-slug>/deliverables/analyst.md
done_when: A decision-maker can accept, reject, or iterate the experiment.
---

# Experiment Readout

## Purpose

Interpret an experiment and translate the result into a decision.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: analyst
project: <slug>
deliverable: analyst.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When a test or rollout needs analysis and recommendation.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `analyst/metric-definition, search_query`.
- If both primary and fallback paths fail, produce the best-guess output described as: An experiment readout with result, confidence, and next step.
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

- Write or update `logs/active/<project-slug>/deliverables/analyst.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: A decision-maker can accept, reject, or iterate the experiment.
