---
name: frame-problem
description: Turn a raw request into a clear product problem, constraints, success criteria, and decision frame.
trigger: When the request is vague or outcome-first.
primary_mcp: notion, repository
fallback_tools: search_query, reference/ground
best_guess_output: A framing brief with objective, constraints, and success criteria.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
done_when: The team can tell what problem is being solved and what is out of scope.
---

# Frame Problem

## Purpose

Turn a raw request into a clear product problem, constraints, success criteria, and decision frame.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: product-lead
project: <slug>
deliverable: product-lead.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: When the request is vague or outcome-first.
- Identify the required inputs, existing artifacts, and dependencies.
- Name the output this skill must produce.

### Step 3: Run The Tool Sequence
- Use the primary MCP/tool first: `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both primary and fallback paths fail, produce the best-guess output described as: A framing brief with objective, constraints, and success criteria.
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

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Record which tool path was used and why.
- Ensure the work meets this done-when bar: The team can tell what problem is being solved and what is out of scope.
