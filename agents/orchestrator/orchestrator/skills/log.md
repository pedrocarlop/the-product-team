---
name: log
description: Keep context.md concise and current with role assignments, skill paths, and done-when criteria.
trigger: Any time routing, staffing, status, or risks change.
primary_mcp: logs
fallback_tools: repository review
best_guess_output: A refreshed context entry that reflects the true current state.
output_artifacts: logs/active/<project-slug>/runs/<run-id>/orchestrator-log.md
done_when: A teammate can resume from context.md or the run history without guessing.
---

# Log

## Purpose

Keep context.md and the project history (`runs/`) concise and current. Every relevant state change or prompt run must be recorded in a discrete run directory to ensure lossless context.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: orchestrator
project: <slug>
run_id: <run-id>
deliverable: orchestrator.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: Any time routing, staffing, status, or risks change.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `logs`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `repository review`.
- If both primary and fallback paths fail, produce the best-guess output described as: A refreshed context entry that reflects the true current state.
- Mark the deliverable header and narrative as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.

### Step 4: Produce The Deliverable
- Synthesize the result into the owned deliverable with concrete findings, decisions, or instructions.
- Keep assumptions explicit, especially when using fallback or inferred mode.
- Carry forward any details downstream roles must preserve.

### Step 4b: Update Knowledge Changelog
- If any knowledge deliverable was created, updated, or superseded during this logging cycle, append an entry to `knowledge/log.md`:
  ```
  ## [YYYY-MM-DD] <action> | <run-id> | <deliverable-file> | <one-line description>
  ```
  Actions: `created`, `updated`, `superseded`, `archived`.

### Step 5: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

