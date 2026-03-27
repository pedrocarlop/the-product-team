---
name: choose
description: Compare architecture options, vendors, and patterns, then select the best fit using explicit tradeoffs, risks, and decision criteria.
activation_hints:
  - "Use when multiple implementation paths are viable."
  - "Route here for option analysis, vendor selection, make-vs-buy decisions, and recommendation writing."
  - "Do not use for breaking down the problem, wiring systems together, or setting policy."
---

# Choose

## Purpose

Use this skill to compare feasible architecture options and make a defensible recommendation that stakeholders can review and approve.

## When to Use

- When there are multiple viable patterns or vendors
- When the team needs a clear recommendation with tradeoffs
- When cost, risk, security, or operability will change the answer
- When a decision needs to be captured for later reference

## When Not to Use

- When the problem has not yet been decomposed clearly
- When the work is mostly implementation sequencing or integration detail
- When there is only one realistic option

## Required Inputs

- The decision to be made
- The candidate options and any hard constraints
- Evaluation criteria such as cost, scale, security, latency, and operability
- Stakeholder preferences or non-negotiables
- Known failure modes, risks, and dependencies

## Workflow

1. Define the decision and the acceptable options.
2. Establish the criteria that matter and weight them by business impact.
3. Compare each option against the same criteria and note the tradeoffs.
4. Identify the failure modes, hidden costs, and lock-in risks for each choice.
5. Make a recommendation and explain why it is the best fit for the current context.
6. Record the decision and the rejected alternatives for future reference.

## Design Principles / Evaluation Criteria

- Decisions should be explicit, not implied
- Tradeoffs matter more than feature lists
- The best option is the one that fits the real constraints
- Rejected alternatives should be documented, not forgotten
- A recommendation must survive stakeholder scrutiny

## Output Contract

- Decision statement with a recommended option
- Comparison matrix or scored rationale
- Key tradeoffs and risks
- Rejected alternatives with reasons
- Decision record suitable for architecture review or handoff

## Examples

### Example 1

Input:
- Decision: Choose the integration pattern for a SaaS partner
- Options: direct REST, event-driven sync, or managed middleware

Expected output:
- Recommendation: event-driven sync
- Rationale: best balance of decoupling, retry handling, and long-term operability

## Guardrails

- Do not recommend an option without criteria
- Do not hide the downside of the chosen path
- Do not optimize for elegance when the team needs operability
- Do not let preference override evidence

## Optional Tools / Resources

- Vendor docs and pricing pages
- Architecture review notes
- Cost models or capacity estimates
- Decision logs and ADRs
