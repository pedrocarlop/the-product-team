---
name: validate
description: Validate API contracts for HTTP semantics, error handling, pagination, auth, and consumer safety before they are treated as final.
---

# Validate

## Purpose

Use this skill to test whether an API contract behaves the way consumers expect and whether the design is internally consistent before implementation moves forward.

## When to Use

- When reviewing a proposed API for edge cases, ambiguity, or missing behavior
- When checking status codes, error envelopes, pagination, auth, or idempotency
- When confirming that a design is ready for consumer review or implementation
- When you need to catch spec drift or contract gaps before they become code

## When Not to Use

- When the core problem is still resource modeling or endpoint shape
- When the task is primarily about versioning policy or deprecation planning
- When you are packaging documentation after the contract is already accepted

## Required Inputs

- The draft API contract or OpenAPI spec
- The intended consumer workflow and failure scenarios
- Expected status codes, retries, and idempotency behavior
- Pagination, filtering, and auth requirements, if any
- Any known constraints from adjacent systems or existing APIs

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

1. Read the contract as a consumer would and look for missing or ambiguous behavior.
2. Check HTTP semantics, status codes, and error shapes for correctness.
3. Verify that pagination, filtering, sorting, and idempotency are handled consistently.
4. Confirm that auth, authorization, and state transitions are explicit.
5. Look for fields, examples, or behaviors that could create hidden coupling or breaking assumptions.
6. Summarize the gaps, risks, and changes required before the contract should be treated as final.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- A valid contract should be predictable under failure, not just success
- Status codes and error envelopes should be consistent everywhere
- Validation should catch consumer confusion before implementation creates it
- Missing behavior is a defect, not a documentation preference
- The safest contract is the one consumers can implement against with confidence

## Output Contract

- Validation findings ordered by severity
- Specific contract issues, missing cases, or ambiguous behaviors
- Clear recommendations for required fixes or follow-up decisions
- Any remaining risks that need consumer confirmation

## Examples

### Example 1

Input:
- `POST /payments` returns `200` with an error message in the body when card authorization fails

Expected output:
- Flag the response as invalid
- Recommend a consistent 4xx status code with a stable error envelope
- Note that consumers need machine-readable failures, not a success status with embedded error text

## Guardrails

- Do not approve contracts that rely on undocumented behavior
- Do not treat examples as proof that the schema is complete
- Do not accept inconsistent status codes or error shapes across endpoints
- Do not ignore ambiguous behavior just because it is unlikely

## Optional Tools / Resources

- OpenAPI linting or diff tools
- Consumer feedback or review notes
- Test cases, mock servers, or contract tests
- Existing API specs for comparison
