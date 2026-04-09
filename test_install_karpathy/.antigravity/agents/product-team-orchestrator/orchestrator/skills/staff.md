---
name: staff
description: Select the right-sized team, assign lossless contracts, and set primary_tools plus fallback policy.
trigger: Once orchestration is needed or a staffed role must change.
primary_mcp: repository, role metadata
fallback_tools: reference/verify, context review
best_guess_output: A staffing table with run_id, output_path, role, skill_paths, target_deliverables, primary_tools, and fallback policy.
output_artifacts: knowledge/orchestrator-staff.md
done_when: Every staffed role has one contract and target deliverables are explicitly named for each assigned skill within a unique run directory.
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
run_id: <run-id>
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

### Step 2b: Cross-Functional Value-Add Check
1. Scan the request against the **Signal-Based Role Triggers** table in `references/role-catalog.md`.
2. For every primary role, evaluate which discipline (Business, Design, Engineering) is missing.
3. Staff at least one "Lean Input" role from the missing discipline for a "High-Level Pass" or "Peer Review".
4. Justify exclusions only when the request is trivial or the missing discipline would provide zero value.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `repository, role metadata`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, context review`.
- If both primary and fallback paths fail, produce the best-guess output described as: A staffing table with run_id, output_path, role, skill_paths, primary_tools, and fallback policy.
- Mark the deliverable header and narrative as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.

### Step 3b: Knowledge Continuity Scan
Before defining assignments, scan `knowledge/` for all existing deliverables. For each staffed role, identify which prior knowledge files are relevant to their work and include them in `reads_from`. Decisions compound across projects — a market analysis must inform brand design, a competitor study must inform UI choices.

### Step 3c: Declare Run Context & Assignment Mode
For each staffed role, define:
- `run_id`: Unique identifier for this execution (e.g., `RUN-001`).
- `owned_outputs`: Paths in `knowledge/` this agent will write.
- `reads_from`: Paths in `knowledge/` this agent must read (including relevant prior knowledge from past projects).
- `assignment_mode`: `primary_executor` | `lean_input` | `peer_reviewer`.
- `hta_declared`: listing the MCP servers required (drawn from the role's `[capabilities].mcp_servers`).

Example contract:
```yaml
run_id: RUN-001
owned_outputs: [knowledge/ux-researcher-competitor-research.md]
reads_from: [knowledge/analyst-market-analysis.md, knowledge/product-lead-venture-discovery.md]
assignment_mode: primary_executor
hta_declared: [notion]
```

### Step 4: Produce The Staffing Execution Plan
- Synthesize the result into the `orchestrator.md` as the start of the Execution Manifest.
- For each role, define `target_deliverables` as a list of skill-specific filenames: `knowledge/<role>-<skill>.md`.
- Carry forward any details downstream roles must preserve from the orientation phase.

### Step 5: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

