---
name: prove
description: Scope and run evidence-driven proofs of value or proof-of-concept work that answer one explicit technical question with measurable success criteria.
---

# Prove

## Purpose

Use this skill to turn a technical question into a bounded proof with agreed criteria, so the prospect can evaluate reality instead of speculation.

## When to Use

- When one objection or uncertainty is blocking the deal
- When the buyer needs a PoC, pilot, benchmark, or architecture validation
- When the team needs evidence from a real integration, API call, or working prototype
- When the success criteria can be written down before the work starts

## When Not to Use

- When no single technical question has been chosen yet
- When the work would quietly become an unpaid implementation
- When the primary task is risk reduction, stakeholder alignment, or security response

## Required Inputs

- The exact technical question the proof must answer
- Written success criteria and what failure looks like
- Scope limits, time box, and required systems or data
- The prospect's approval on what is in and out of scope
- Any dependencies on engineering, implementation, or customer systems

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

1. Translate the sales concern into one testable claim.
2. Write the proof scope narrowly enough that success is measurable.
3. Define pass, partial pass, and fail criteria before work begins.
4. Build or run only what is needed to answer the question.
5. Capture evidence in a form the prospect can review and reuse.
6. Confirm the result does not create hidden implementation promises.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- A proof should answer one question well
- Scope should be explicit and time-bound
- Evidence should be visible, not implied
- Success criteria should be agreed up front
- The proof should reduce uncertainty without expanding the deal's scope

## Output Contract

- The proof question and agreed scope
- Success criteria, evidence, and conclusion
- Any limitations, assumptions, or follow-up work
- A clear recommendation for next-step evaluation or close

## Examples

### Example 1

Input:
- Question: "Can your API support our expected throughput?"
- Constraint: Need an answer in one week

Expected output:
- Proof plan: Run a bounded benchmark with the expected request pattern and document pass/fail thresholds
- Result: Evidence package with the measured outcome and any caveats

## Guardrails

- Do not let the proof become open-ended
- Do not use a PoC to smuggle in implementation work
- Do not present unmeasured opinions as evidence
- Do not broaden scope without re-approval

## Optional Tools / Resources

- Product sandbox, API docs, and test credentials
- GitHub for prototype code or examples
- Logs, benchmarks, and screenshots
- Notion for proof scope and decision records
