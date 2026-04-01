---
name: elicit
description: Gather and refine business needs into structured, testable requirements by interviewing stakeholders, probing assumptions, and capturing edge cases.
---

# Elicit

## Purpose

Use this skill to turn a vague business request into a complete, structured understanding of what stakeholders need, why they need it, and where the uncertainty still lives.

## When to Use

- When the problem statement is broad, ambiguous, or conflicting across stakeholders
- When you need to identify who is affected, what is broken, and what success means
- When edge cases, exceptions, dependencies, or hidden constraints are not yet known

## When Not to Use

- When the business need is already fully documented and only needs to be mapped or specified
- When the task is primarily about process flow visualization rather than discovery
- When you are validating a finished solution against agreed criteria

## Required Inputs

- The original request, ticket, or prompt
- Known stakeholders, users, and impacted teams
- Current problem statement or symptoms
- Any constraints, deadlines, or business rules already known
- Supporting context such as notes, transcripts, screenshots, or prior documents

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

1. Restate the request in plain business terms and identify what is still unknown.
2. List the stakeholders, users, and downstream teams who may be affected.
3. Separate facts, assumptions, opinions, and open questions.
4. Ask focused questions that expose business need, current pain, edge cases, and success criteria.
5. Capture constraints, dependencies, and non-obvious failure modes.
6. Confirm the business problem is understood well enough to move into mapping or specification.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Questions should reduce ambiguity, not generate more of it
- Business goals should be captured before proposing a solution
- Hidden stakeholders and failure modes must be surfaced early
- Evidence should be separated from assumptions
- Discovery should produce clarity, not just more notes

## Output Contract

- A concise problem statement
- A stakeholder and impact list
- A set of open questions and assumptions
- A first-pass list of business needs and success criteria

## Examples

### Example 1

Input:
- Request: "We need to fix the onboarding flow"

Expected output:
- Clarified problem statement: "New users are dropping out during onboarding because the form asks for too much information too early."
- Open questions: "Which step has the highest drop-off? Which user segments are most affected? What data is truly required at signup?"

## Guardrails

- Do not jump to solution ideas before the business problem is understood
- Do not treat a single stakeholder opinion as the full requirement
- Do not skip impacted teams that may only appear downstream
- Do not conflate symptoms with root causes

## Optional Tools / Resources

- Interview notes or transcripts
- Existing process docs and policies
- Support tickets, bug reports, and feedback themes
- Stakeholder maps or org charts

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Harvard Business Review (hbr.org)](https://hbr.org/), [BA Times (batimes.com)](https://www.batimes.com/), [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [ProductPlan Glossary and Guides (productplan.com)](https://www.productplan.com/glossary/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/)
