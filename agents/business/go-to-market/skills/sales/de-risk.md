---
name: de-risk
description: Identify, document, and reduce technical, security, integration, and delivery risks so the buyer can commit with confidence.
---

# De-risk

## Purpose

Use this skill to make the remaining risks visible, answer them with evidence, and ensure nothing in the sales process outpaces what delivery can actually support.

## When to Use

- When security, compliance, integration, or performance risks are slowing the deal
- When a stakeholder needs reassurance that the product fits their environment safely
- When a technical commitment needs validation with engineering or implementation
- When the handoff from sales into delivery needs to be made explicit

## When Not to Use

- When the problem is still basic discovery
- When the main need is a demo narrative or a bounded proof of value
- When the request is broad and no specific risk has been named yet

## Required Inputs

- The specific risk, objection, or concern being raised
- The evidence available today, including docs, architecture notes, or internal owners
- The delivery constraints that might affect the commitment
- Any deadlines from procurement, security, or evaluation stakeholders
- The systems or teams that must validate the answer

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

1. Name the risk in plain language and tie it to the deal impact.
2. Separate product limits, implementation limits, and unknowns.
3. Gather evidence from the most credible source available.
4. Turn promises into written, validated commitments or safe alternatives.
5. Escalate unresolved gaps to the right internal owner with a clear deadline.
6. Record the outcome so delivery and sales share the same understanding.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Risks should be explicit, not hidden in friendly language
- Evidence should come from authoritative sources
- Commitments must be deliverable
- The buyer should understand both the answer and any remaining caveats
- Sales and delivery should leave with the same record

## Output Contract

- A risk summary with status and owner
- Evidence or documentation used to resolve the concern
- Any validated commitments, caveats, or safe alternatives
- Notes for handoff to implementation, CS, or engineering

## Examples

### Example 1

Input:
- Risk: "Will this pass security review?"
- Context: Enterprise procurement needs current controls and a clear implementation path

Expected output:
- Response: Provide current-state security evidence, note any gaps honestly, and document what can be committed for delivery

## Guardrails

- Do not overstate security, compliance, or delivery readiness
- Do not convert an unresolved risk into a promise
- Do not let the prospect discover implementation limits after signature
- Do not leave risk decisions undocumented

## Optional Tools / Resources

- Security docs, architecture diagrams, and implementation notes
- Internal SMEs from engineering, security, or implementation
- Notion or CRM records for decision tracking
- Prospect questionnaires and procurement artifacts
