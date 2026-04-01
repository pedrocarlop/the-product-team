---
name: align
description: Translate a product decision into shared understanding across the immediate team and adjacent stakeholders so execution moves in one direction.
---

# Align

## Purpose

Use this skill to make sure a product decision — scope change, prioritization call, or tradeoff — is understood and actionable by the people who need to build, support, and sell it.

## When to Use

- When engineering, design, or QA need context on why a scope or priority changed
- When sales, support, or marketing need to update their plans based on a product decision
- When a roadmap change requires re-setting expectations with stakeholders who were counting on a different outcome
- When a tradeoff was made and the reasoning needs to be documented before it is forgotten

## When Not to Use

- When the decision has not been made yet — alignment follows decisions, it does not replace them
- When the alignment need is at the executive or board level (escalate to CPO)
- When the issue is cross-portfolio strategy rather than a single product area

## Required Inputs

- The specific decision, tradeoff, or scope change being communicated
- The teams and stakeholders who are directly affected
- The reasoning behind the decision, including what was considered and rejected
- The timeline and next steps each audience needs to act on
- Any commitments that are changing or being dropped

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: product-lead
project: <slug>
deliverable: product-lead.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. State the decision and the single most important reason behind it.
2. List who is affected and what changes for each team or stakeholder.
3. Address the likely objection or concern head-on — do not wait for it to surface later.
4. Define the concrete next steps: who does what by when.
5. Document the decision and rationale where the team can find it later.
6. Schedule a check-in if the decision has a built-in evaluation point.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Alignment should result in changed behavior, not just head-nodding
- The message should be concrete enough that each audience knows their next step
- Dropped commitments should be acknowledged, not quietly removed
- Rationale should be honest — if the reason is "we ran out of time," say that
- Good alignment prevents the same question from being re-asked next week

## Output Contract

- A concise alignment message or decision note
- Team-specific next steps where needed
- Acknowledged tradeoffs and dropped commitments
- Follow-up date or checkpoint if applicable

## Examples

### Example 1

Input:
- Decision: Cut the export feature from the current release to hit the launch date

Expected output:
- Alignment note: "Export is moving to the post-launch cycle because the remaining work conflicts with the launch-critical accessibility fixes. Sales should set expectations with the three customers who requested it. Engineering should close the in-progress branch and document the remaining work."

## Guardrails

- Do not use alignment to retroactively justify a decision that was never explicitly made
- Do not hide dropped scope — be direct about what is no longer happening
- Do not over-explain the strategic context when the audience just needs to know what changed
- Do not present contested decisions as unanimous

## Optional Tools / Resources

- Decision logs and roadmap documents
- Team standup notes and sprint plans
- Customer feedback and sales pipeline context
- Notion docs or Slack posts for async alignment

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Mind the Product (mindtheproduct.com)](https://www.mindtheproduct.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Product School Resources (productschool.com)](https://productschool.com/resources)
