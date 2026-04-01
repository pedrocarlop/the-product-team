---
name: screener-form-build
description: Prepare the participant screener or intake form needed to recruit the right people.
trigger: When a study needs recruitment or intake filtering.
primary_mcp: google_forms
fallback_tools: notion, docs-style questionnaire
best_guess_output: A screener form or equivalent structured questionnaire.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
done_when: Recruiting can start with clear inclusion and exclusion criteria.
---

# Screener Form Build

## Purpose

Prepare the participant screener or intake form needed to recruit the right people.

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
- Restate the task in terms of this skill's trigger: When a study needs recruitment or intake filtering.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `google_forms`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `notion, docs-style questionnaire`.
- If both primary and fallback paths fail, produce the best-guess output described as: A screener form or equivalent structured questionnaire.
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
- Ensure the work meets this done-when bar: Recruiting can start with clear inclusion and exclusion criteria.
