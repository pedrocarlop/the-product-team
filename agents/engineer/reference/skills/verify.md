---
name: verify
description: Confirm that the grounded facts, traced paths, and reused patterns are actually supported by the codebase before the decision is finalized.
---

# Verify

## Purpose

Use this skill to confirm that the conclusions drawn from grounding, tracing, and reuse are backed by the repository as it exists now. Verification turns a plausible decision into a defensible one.

## When to Use

- When a path, pattern, or dependency has been selected and needs confirmation
- When a claimed source of truth must be checked against the actual code
- When a reused component or helper needs proof that it still matches the required behavior
- When a final reference summary must be validated before handoff

## When Not to Use

- When the task is still figuring out what exists
- When the task is still tracing the flow
- When the task is still selecting between reusable options

## Required Inputs

- The conclusion that needs verification
- The supporting evidence gathered during grounding, tracing, or reuse
- The files, modules, or repository areas that must be checked again
- Any pass/fail expectation or acceptance condition for the decision

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: reference
project: <slug>
deliverable: reference.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Restate the conclusion in a testable form.
2. Re-open the supporting files and confirm the evidence still matches the claim.
3. Check for contradictions, stale assumptions, or missing context.
4. Confirm that any reused pattern is still the approved pattern for the area.
5. Record the result with enough detail that another person can trust it.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Verification should confirm the claim against the present repository state
- If evidence is incomplete, the result is still unresolved
- A verified conclusion should be specific enough to defend in review
- Any contradiction must be surfaced explicitly

## Output Contract

- A clear pass, fail, or unresolved verification result
- The evidence checked to reach that result
- Any remaining risk, contradiction, or follow-up needed

## Examples

### Example 1

Input:
- Conclusion: The shared dialog component is the approved destructive-action pattern

Expected output:
- Verification result: Pass
- Evidence: Existing usage in account deletion and payment-method removal flows
- Remaining risk: None found in the current repository snapshot

## Guardrails

- Do not mark a conclusion as verified without checking the actual files again
- Do not treat partial evidence as full confirmation
- Do not ignore conflicts between the target repository and a named external source
- Do not widen the scope beyond the conclusion being verified

## Optional Tools / Resources

- MCP: Notion MCP, GitHub MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [DevDocs](https://devdocs.io/), [GitHub Docs](https://docs.github.com/), [RFC Editor](https://www.rfc-editor.org/), [IETF Datatracker](https://datatracker.ietf.org/)
- Repository search and direct file inspection
- Tests, fixtures, examples, and usage docs
- Comparison notes from grounding and tracing
- External source-system or design-system references if they were named
