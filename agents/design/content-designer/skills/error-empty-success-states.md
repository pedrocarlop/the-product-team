---
name: error-empty-success-states
description: Design the messaging for non-happy-path states so users can recover or proceed confidently.
trigger: When a feature needs state-specific messaging beyond the default path.
primary_mcp: notion, figma
fallback_tools: reference/trace, search_query
best_guess_output: A state-message set for error, empty, loading, and success moments.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
done_when: Critical states have explicit user-facing messaging.
---

# Error Empty Success States

## Purpose

Design the messaging for non-happy-path states so users can recover or proceed confidently.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: content-designer
project: <slug>
deliverable: content-designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When a feature needs state-specific messaging beyond the default path.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both primary and fallback paths fail, produce the best-guess output described as: A state-message set for error, empty, loading, and success moments.
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

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: Critical states have explicit user-facing messaging.
