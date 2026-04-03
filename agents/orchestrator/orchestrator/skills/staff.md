---
name: staff
description: Select the right-sized team, assign lossless contracts, and set primary_tools plus fallback policy.
trigger: Once orchestration is needed or a staffed role must change.
primary_mcp: repository, role metadata
fallback_tools: reference/verify, context review
best_guess_output: A staffing table with role, skill_paths, target_deliverables, primary_tools, and fallback policy.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator-staff.md
done_when: Every staffed role has one contract and target deliverables are explicitly named for each assigned skill.
---

# Staff

## Purpose

Select the right-sized team, assign contracts, and set primary_tools plus fallback policy.

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
- Restate the task in terms of this skill's trigger: Once orchestration is needed or a staffed role must change.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 2b: Role Coverage Check
Before finalizing the team, verify:
1. Scan the request against the **Signal-Based Role Triggers** table in `references/role-catalog.md`.
2. For each triggered role not in the current team, justify its exclusion in the staffing table.
3. If more than 2 triggered roles are excluded, reconsider whether the team is under-staffed rather than right-sized.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, role metadata`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, context review`.
- If both primary and fallback paths fail, produce the best-guess output described as: A staffing table with role, skill_paths, primary_tools, and fallback policy.
- Mark the deliverable header and narrative as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.

### Step 3b: Declare HTA Requirements Per Role
For each staffed role, add an `hta_declared` field to its contract listing the MCP servers required to run its assigned `skill_paths` (drawn from the role's `[capabilities].mcp_servers`). This makes HTA dependencies explicit before execution begins.

Example contract addition:
```yaml
hta_declared: [notion, linear, github]
```

Note: this step declares requirements only — actual verification happens at subagent startup when each MCP is probed. If a role has no MCP dependencies, set `hta_declared: []`.

### Step 4: Produce The Staffing Execution Plan
- Synthesize the result into the `orchestrator.md` as the start of the Execution Manifest.
- For each role, define `target_deliverables` as a list of skill-specific filenames: `logs/active/<slug>/deliverables/<role>-<skill>.md`.
- Carry forward any details downstream roles must preserve from the orientation phase.

### Step 5: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

