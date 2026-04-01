---
name: standardize
description: Turn a working operational pattern into a durable SOP, checklist, or control with clear ownership, steps, and review cadence.
---

# Standardize

## Purpose

Use this skill to turn a known operational flow into a reliable standard that people can follow without re-deciding how it works every time.

## When to Use

- When a recurring task is handled inconsistently
- When a process needs a clear owner, sequence, and definition of done
- When teams need a shared standard for execution or quality control

## When Not to Use

- When the process is still unclear and needs mapping first
- When the main issue is cross-functional coordination or escalation
- When the problem is a recurring defect that needs analysis and improvement

## Required Inputs

- The process or workflow that should be standardized
- The teams, systems, and artifacts involved
- The current best-known way of doing the work
- Known exceptions, edge cases, and compliance constraints
- Any ownership or review requirements

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: business-ops
project: <slug>
deliverable: business-ops.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Confirm the process is stable enough to standardize without guessing.
2. Define the trigger, purpose, owner, and expected outcome.
3. Write the steps in a sequence that a new person could follow.
4. Include edge cases, escalation paths, and the definition of done.
5. Assign review cadence and change ownership so the standard stays current.
6. Check that the standard is usable in real work, not just readable in theory.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Standards should reduce decision load
- Owners should be named, not implied
- The document should match how work actually happens
- Exceptions must be documented, not hidden
- Review cadence is part of the standard, not an afterthought

## Output Contract

- An SOP, checklist, or runbook
- A named owner and review cadence
- A list of exceptions and escalation rules
- A short note on what was intentionally not standardized

## Examples

### Example 1

Input:
- Process: "Monthly vendor invoice approval"

Expected output:
- SOP step: "Finance reviews invoice against contract, checks variance threshold, and routes approval to the named owner within two business days."
- Review note: "Revisit quarterly or when contract terms change."

## Guardrails

- Do not write standards that people cannot realistically follow
- Do not omit edge cases because they are annoying to document
- Do not standardize before the process is stable enough
- Do not leave the standard without an owner or review date

## Optional Tools / Resources

- Existing process maps or current runbooks
- Templates, checklists, or policy docs
- Exception logs and historical incidents
- Stakeholder feedback from the people doing the work

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [McKinsey Operations Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/operations/our-insights), [Asana Work Innovation Lab (asana.com)](https://asana.com/resources), [Harvard Business Review Operations (hbr.org)](https://hbr.org/topic/operations), [Lean Enterprise Institute (lean.org)](https://www.lean.org/explore-lean/)
