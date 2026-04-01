---
name: partner-thesis
description: Define which partners matter, why, and what structure best fits the opportunity.
trigger: When partnership exploration or prioritization is needed.
primary_mcp: notion
fallback_tools: search_query, go-to-market/positioning-brief
best_guess_output: A partner thesis with targets and rationale.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
done_when: The partnership strategy is specific enough to start outreach.
---

# Partner Thesis

## Purpose

Define which partners matter, why, and what structure best fits the opportunity.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: go-to-market
project: <slug>
deliverable: go-to-market.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When partnership exploration or prioritization is needed.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, go-to-market/positioning-brief`.
- If both primary and fallback paths fail, produce the best-guess output described as: A partner thesis with targets and rationale.
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

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: The partnership strategy is specific enough to start outreach.
