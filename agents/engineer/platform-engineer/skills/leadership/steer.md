---
name: steer
description: Set technical direction, frame tradeoffs, and align teams on the simplest architecture that solves the actual problem.
---

# Steer

## Purpose

Use this skill to decide or guide the technical direction of a team or product area so the work stays aligned with the target architecture, the real constraint, and the lowest-risk path forward.

## When to Use

- When a decision affects architecture, interfaces, dependencies, or team boundaries
- When a choice should be documented as an ADR or shared decision record
- When the team needs a recommendation on build vs buy, sequencing, or migration direction
- When a proposal feels larger or more complex than the problem actually requires

## When Not to Use

- When the request is only to implement a clearly decided change
- When the issue is localized to one component and has no meaningful architectural impact
- When the main need is code review feedback rather than direction-setting

## Required Inputs

- The problem statement and desired outcome
- The current architecture, constraints, and known dependencies
- Who is affected, including other teams or systems
- Any reversibility, migration, or sequencing constraints
- Existing decision records, docs, or prior discussions that shape the choice

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Clarify the decision being made and separate it from the implementation details.
2. Check whether the choice is reversible, cross-team, or likely to create new long-term standards.
3. Compare the simplest viable option against the more flexible or ambitious alternatives.
4. Identify the tradeoffs, failure modes, and costs of reversal for each option.
5. Align the relevant people before implementation begins when the decision crosses boundaries.
6. Record the decision in the right durable artifact if the change is architectural enough to repeat or revisit.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Simplicity over overengineering
- Reversibility over premature commitment when the cost of change is high
- Explicit alignment over surprise decisions
- Documented rationale over memory
- Fit to the actual problem over abstract idealism

## Output Contract

- A clear recommendation with the key tradeoffs
- A note on whether the decision should become an ADR or shared record
- A reversibility assessment, including what it would cost to change later
- The next alignment or implementation step

## Examples

### Example 1

Input:
- Problem: Two services need a new shared interface
- Constraint: Another team depends on the result
- Risk: The interface may need to evolve in the next quarter

Expected output:
- Recommendation: Start with the smallest stable contract, document it as a shared decision, and avoid adding flexibility that is not needed yet.
- Rationale: The boundary matters more than optimization, and the interface should stay easy to change while the shape is still uncertain.

## Guardrails

- Do not introduce complexity to preempt hypothetical future needs
- Do not make cross-team decisions without the right people in the loop
- Do not treat architectural intuition as a substitute for a written rationale
- Do not turn every implementation detail into a platform decision

## Optional Tools / Resources

- MCP: GitHub MCP, Linear MCP, Notion MCP, Sentry MCP, Chrome DevTools MCP
- Websites: [Atlassian Team Playbook](https://www.atlassian.com/team-playbook), [Google Engineering Practices](https://google.github.io/eng-practices/), [GitHub Engineering Blog](https://github.blog/engineering/), [DORA / DevOps Research](https://cloud.google.com/devops), [Martin Fowler](https://martinfowler.com/)
- ADR templates or decision logs
- Architecture diagrams
- Dependency maps or system inventories
- Prior incident reviews and migration notes
