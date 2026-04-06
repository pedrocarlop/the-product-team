---
name: pattern-extraction
description: Systematically extracts successful patterns, workflows, and rule sets from execution trails into reusable "instincts".
trigger: When the orchestrator notices repetitive behaviors, successful workarounds, or when requested explicitly to extract a pattern.
primary_mcp: logs, repository
fallback_tools: reference/ground
best_guess_output: A set of atomic instincts ready to be promoted or saved.
output_artifacts: knowledge/instincts/<pattern-name>.yaml
done_when: The learned pattern is codified as a reusable instinct with a confidence score.
---

# Pattern Extraction (Continuous Learning)

## Purpose

To implement a Continuous Learning loop similar to a human team reflecting on past work. By observing successful execution paths or repeated corrections in the `/logs`, the orchestrator extracts atomized "instincts" (patterns) and saves them, effectively evolving the team's capabilities over time without manual updates.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: orchestrator
project: <slug>
deliverable: instinct.md
confidence: <0.0-1.0>
inputs_used: [/logs/<project>, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task in terms of this skill's trigger: Extracting patterns after observing successful workflows or repeated corrections.
- Identify the source material (usually execution traces in `logs/active/` or `logs/archive/`).

### Step 3: Run The Tool Sequence
- Use the primary tools to read the `trace.md` or `feedback.md` of a completed run.
- Identify patterns: 
  - Did the team repeatedly use a specific architectural workaround?
  - Was there a recurring test failure that had a consistent fix?
  - Did a user repeatedly ask for a specific code style?
- Extract the pattern into an **Atomic Instinct**.
- Give it a `confidence` score (e.g. 0.3 for a single observation, 0.9 for a universally repeated pattern).

### Step 4: Produce The Deliverable Using The CLI
- Do not write raw markdown files for instincts.
- Use the `instinct_cli.py` to persist the pattern into the cross-project memory store.
- Execute: `scripts/instinct_cli.py save --name "<id>" --description "<trigger context>" --pattern "<Action/Pattern text>" --confidence "<low|medium|high|guaranteed>"`
- Example: `python3 scripts/instinct_cli.py save --name "prefer-functional-components" --description "when writing UI components" --pattern "Use functional components and hooks over class components. Evidence: Noticed frontend-engineer defaulting to functional patterns successfully." --confidence "high"`

### Step 5: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful extraction details.
- **What didn't**: trade-offs, noise, or known limitations.
- **Next steps**: whether this instinct should be promoted globally to all roles.
