---
name: interview-guide-build
description: Write the interview or discussion guide with sequencing, probes, and evidence goals.
trigger: When live research sessions need a structured guide.
primary_mcp: notion
fallback_tools: search_query, ux-researcher/research-plan
best_guess_output: An interview guide that supports comparable sessions.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
done_when: A moderator can run sessions without improvising the core script.
---

# Interview Guide Build

## Purpose

Write the interview or discussion guide with sequencing, probes, and evidence goals.

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
- Restate the task in terms of this skill's trigger: When live research sessions need a structured guide.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, ux-researcher/research-plan`.
- If both primary and fallback paths fail, produce the best-guess output described as: An interview guide that supports comparable sessions.
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
- Ensure the work meets this done-when bar: A moderator can run sessions without improvising the core script.
