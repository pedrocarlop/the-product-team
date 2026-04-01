---
name: regression-triage
description: Classify and prioritize regressions so the team knows what blocks release.
trigger: When a build or feature has defects and they need triage.
primary_mcp: repository, chrome_devtools
fallback_tools: reference/verify, open
best_guess_output: A regression triage with severity and release impact.
output_artifacts: logs/active/<project-slug>/deliverables/qa-reviewer.md
done_when: Blocking and non-blocking issues are clearly separated.
---

# Regression Triage

## Purpose

Classify and prioritize regressions so the team knows what blocks release.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: qa-reviewer
project: <slug>
deliverable: qa-reviewer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When a build or feature has defects and they need triage.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, open`.
- If both primary and fallback paths fail, produce the best-guess output described as: A regression triage with severity and release impact.
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

- Write or update `logs/active/<project-slug>/deliverables/qa-reviewer.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: Blocking and non-blocking issues are clearly separated.
