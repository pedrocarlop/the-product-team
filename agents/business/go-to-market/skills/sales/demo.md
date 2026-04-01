---
name: demo
description: Design and deliver prospect-specific technical demos that show the product solving the buyer's real use case in a credible environment.
---

# Demo

## Purpose

Use this skill to build and present demos that answer the prospect's real question with a believable narrative, relevant data, and the smallest useful surface area.

## When to Use

- When discovery has identified a concrete use case to show
- When the prospect needs to see workflow, UX, or technical behavior in context
- When a live or recorded demo needs to be tailored to a buyer, segment, or integration stack
- When the demo must support a champion, technical evaluator, or executive stakeholder

## When Not to Use

- When the main task is still figuring out what the prospect cares about
- When the goal is to prove a single technical claim with evidence or a prototype
- When the question is mostly about risk reduction, security, or deployment feasibility

## Required Inputs

- The target use case and desired decision from the demo
- Prospect-specific data, systems, or scenario details
- Audience, meeting length, and delivery format
- Known constraints on environment, branding, security, or access
- The proof points the demo must make obvious

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: go-to-market
project: <slug>
deliverable: go-to-market.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Define the single story the demo needs to tell.
2. Choose the smallest set of screens, flows, APIs, or artifacts that prove the story.
3. Use prospect-relevant data or realistic stand-ins instead of generic samples.
4. Script the demo around outcomes, not feature inventory.
5. Rehearse transitions, failure points, and fallback paths before the live session.
6. Capture follow-up materials or async recordings for stakeholders who are not present.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Narrative first, feature list second
- Relevance beats completeness
- Credibility matters more than polish
- The demo should map cleanly to the prospect's environment
- Every scene should answer a buyer question

## Output Contract

- A demo narrative or talk track
- The environment, sample data, or setup used
- A walkthrough plan for live or async delivery
- Follow-up notes on what landed, what did not, and what needs proof next

## Examples

### Example 1

Input:
- Prospect: Fintech platform
- Ask: "Show us how this fits with our event pipeline and access model."

Expected output:
- Demo plan: Use a scenario built around their event flow, permissions, and audit needs
- Delivery: Live walkthrough with a recorded backup for security reviewers

## Guardrails

- Do not demo features that are irrelevant to the prospect's use case
- Do not use fake credibility markers or over-curated data
- Do not promise future product behavior during the walkthrough
- Do not let the demo drift away from the decision the buyer needs to make

## Optional Tools / Resources

- Product sandbox or demo environment
- GitHub for code-backed examples
- Recorded walkthrough tools
- Notes from discovery and stakeholder interviews
