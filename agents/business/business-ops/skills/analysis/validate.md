---
name: validate
description: Confirm that a proposed or built solution matches agreed business requirements through structured review, UAT planning, and sign-off criteria.
---

# Validate

## Purpose

Use this skill to verify that the solution, process, or documentation still aligns with the agreed business requirements and that stakeholders can confidently sign off.

## When to Use

- When requirements have been documented and need verification
- When UAT scripts or acceptance checks must be planned
- When a proposed solution needs to be checked against business intent

## When Not to Use

- When the business need has not yet been clarified
- When requirements still need to be written or reworked
- When the task is primarily process mapping or stakeholder discovery

## Required Inputs

- The requirement set and traceability references
- The solution, process, or document under review
- Stakeholders responsible for acceptance
- Known acceptance rules, thresholds, or pass/fail standards
- Any open risks, gaps, or unresolved assumptions

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

1. Compare the proposed outcome to the documented requirement set.
2. Check that each requirement has a clear validation path.
3. Draft or review validation criteria and UAT scenarios.
4. Identify mismatches, gaps, or ambiguities before sign-off.
5. Confirm who can approve and what evidence is needed.
6. Record whether the solution meets, partially meets, or fails the agreed need.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Validation should be traceable, not subjective
- Requirements must be checked against evidence, not intuition
- Edge cases matter when deciding readiness
- Sign-off needs a named owner and a clear standard
- Gaps should be documented explicitly, not implied

## Output Contract

- A validation summary against the agreed requirements
- UAT or acceptance criteria mapped to requirements
- A list of gaps, risks, and follow-up actions
- A clear recommendation on readiness or sign-off status

## Examples

### Example 1

Input:
- Requirement: "Users must not be able to submit without an approved attachment."

Expected output:
- Validation note: "The current build allows submission with a missing attachment, so REQ-004 is not met."
- Follow-up: "Update the workflow or document an approved exception before sign-off."

## Guardrails

- Do not treat demos as validation without explicit pass/fail criteria
- Do not sign off on vague requirements
- Do not blur the line between uncovered gaps and accepted exceptions
- Do not accept a solution that cannot be traced back to a requirement

## Optional Tools / Resources

- Requirement traceability matrix
- UAT scripts or test cases
- Sign-off documents
- Stakeholder review notes or defect logs

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Harvard Business Review (hbr.org)](https://hbr.org/), [BA Times (batimes.com)](https://www.batimes.com/), [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [ProductPlan Glossary and Guides (productplan.com)](https://www.productplan.com/glossary/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/)
