---
name: coordinate
description: Launch specialists in sequence, curate the Execution Manifest, and ensure lossless handoff to downstream roles.
trigger: After staffing approval or while running a staged workflow.
primary_mcp: logs, subagents
fallback_tools: orchestrator/log, context review
best_guess_output: An Execution Manifest indexing all specialist deliverables with status and path.
output_artifacts: knowledge/orchestrator-coordinate.md
done_when: Every specialist output is indexed in the manifest and implementation owners can access all original source materials.
---

# Coordinate

## Purpose

Launch specialists in sequence, pass artifact paths, and enforce evidence_mode reporting.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: orchestrator
project: <slug>
deliverable: orchestrator.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: After staffing approval or while running a staged workflow.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 2b: Check For Pending HTA Blocks
Before launching any subagent, check `context.md` for any role with `hta_status: unresolved`.
- If found → invoke `setup-check` for that role first and wait for resolution before launching it.
- If none found → proceed to Step 3.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `logs, subagents`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `orchestrator/log, context review`.
- If both primary and fallback paths fail, produce the best-guess output described as: An up-to-date execution state with handoffs and blocker handling.
- Mark the deliverable header and narrative as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.

### Step 3b: Handle hta_setup_required Signals
After each subagent returns, check its output for an `hta_setup_required` signal.
- If signal detected:
  1. Record `hta_status: unresolved` for that role in `context.md`, noting the blocked MCP and skill.
  2. Pause the coordinate workflow — do not launch downstream roles.
  3. Invoke `setup-check` skill.
  4. After `setup-check` resolves (`hta_status: configured` or `hta_status: fallback_authorized`), re-launch the subagent.
- If no signal → continue to the next stage normally.

### Step 4: Produce The Execution Manifest
- Curate the `orchestrator.md` as a registry of all specialist deliverables.
- For each completed skill, record: Skill Name | Owner | Deliverable Path | Status | Key Signals link.
- Do not summarize away the detail of the original artifacts; provide navigation and orientation only.
- Carry forward any critical dependencies or cross-role constraints.

### Step 5: Update Knowledge Index and Changelog
- After all specialists have completed, update `knowledge/index.md`:
  - Add any new deliverable files under the appropriate domain category.
  - Remove entries for superseded files.
- Append entries to `knowledge/log.md` for every deliverable created or updated during this coordination cycle:
  ```
  ## [YYYY-MM-DD] <action> | <run-id> | <deliverable-file> | <one-line description>
  ```
- If specialist outputs reveal cross-cutting concepts (competitors, personas, patterns), consider creating or updating entity pages in `knowledge/entities/`.

### Step 6: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

