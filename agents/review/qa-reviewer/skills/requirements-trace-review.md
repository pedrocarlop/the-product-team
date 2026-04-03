---
name: requirements-trace-review
description: Trace delivered behavior back to stated requirements and constraints by building a requirement model and an evidence matrix that separates confirmed matches, gaps, ambiguities, and unverified assumptions.
trigger: When implementation, design, or release readiness must be validated against upstream requirements, acceptance criteria, or policy constraints.
comparison_framework: requirement-to-evidence traceability across intent, delivered behavior, constraints, and confidence
primary_mcp: repository, logs
fallback_tools:
  - reference/verify
  - open
required_inputs:
  - source requirements, acceptance criteria, or constraint set
  - target implementation surface, flow, or release slice
  - available evidence artifacts such as code, tests, logs, or design assets
  - known non-functional constraints such as security, policy, or performance when relevant
  - decision context such as sign-off, regression review, or release gating when known
recommended_passes:
  - requirement extraction and normalization
  - surface and dependency mapping
  - evidence matching
  - mismatch and ambiguity classification
  - priority risk escalation
tool_stack:
  synthesis:
    primary: [repository, logs]
    secondary: [reference/verify]
  artifacts:
    primary: [open]
  fallback:
    primary: [reference/verify, open]
tool_routing:
  - if: source requirements and implementation evidence are both accessible
    use: [repository, logs]
  - if: requirements mostly live in linked artifacts or prior review material
    use: [reference/verify]
  - if: only static specs, tickets, screenshots, or linked documents exist
    use: [open]
best_guess_output: A requirements trace review with explicit matches, gaps, ambiguities, and unverified areas.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
done_when: The team can see where delivery matches intent, where it drifts, which constraints are unverified, and which gaps matter most for sign-off or release.
---

# Requirements Trace Review

## Purpose

Trace delivered behavior back to stated requirements and constraints by building a requirement model first, then mapping evidence against each requirement explicitly.

This skill applies structured traceability reasoning across intent, implementation surfaces, constraints, and evidence confidence.

This skill does not invent missing requirements, replace product clarification, or treat absence of proof as confirmation of delivery.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/qa-reviewer-requirements-trace-review.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: requirements-trace-review`, include:
- `### Review framing`: Define the source requirement set, review scope, and what evidence types count for this trace.
- `### Required inputs and assumptions`: State the known requirements, implementation surfaces, constraints, and any missing items inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live or current implementation evidence, structured repository and log evidence, linked requirement artifacts, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record the build, environment, artifact versions, data or auth assumptions, and requirement source references when known.
- `### Requirement model`: Build the model first by extracting and normalizing the requirement set, acceptance criteria, constraints, and downstream surfaces before evaluating matches or gaps.
- `### Trace passes`: List the passes used such as requirement extraction and normalization, surface and dependency mapping, evidence matching, mismatch and ambiguity classification, and priority risk escalation.
- `### Requirement matrix`: Map each major requirement or constraint to status, evidence, implementing surface, and confidence.
- `### Surface and flow mapping`: Show which screens, APIs, states, or system behaviors implement each requirement or constraint.
- `### Trace findings`: Record findings using the required finding schema below.
- `### Confirmed matches`: Record where delivered behavior clearly satisfies stated intent or constraints.
- `### Gaps and mismatches`: Capture missing behavior, contradictory behavior, or partial delivery.
- `### Ambiguities and unverified assumptions`: Note where the source requirement is vague, conflicting, implied, or only partially evidenced.
- `### Priority risks`: Highlight the highest-impact traceability gaps for product, engineering, compliance, or release decisions.
- `### Systemic traceability patterns`: Group repeated issues such as vague requirements, missing acceptance criteria, hidden dependencies, or absent evidence.
- `### Coverage map`: State what was deeply traced, partially traced, and not traced.
- `### Recommendations`: Link follow-up actions to the gaps without pretending every requirement dispute is already resolved.
- `### Limits and unknowns`: Explain what could not be verified from the available evidence.

For each finding inside `### Trace findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Requirement or constraint:
- Implementing surface:
- Gap type:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest traceability evidence path available: live or current implementation evidence -> structured repository and log evidence -> linked requirement artifacts -> inference.
- Start with `repository, logs` when both source requirements and implementation evidence are accessible.
- Use `repository` to inspect implementation surfaces, tests, configuration, and explicit acceptance references.
- Use `logs` when runtime evidence, audit trails, or execution records materially support or weaken the trace.
- Use `reference/verify` when prior QA artifacts, requirement documents, issue threads, or linked references are the strongest available trace path.
- Use `open` when only static specs, screenshots, or linked documentation remain.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, open`.
- If both paths fail, produce the best-guess output described as: A requirements trace review with explicit matches, gaps, ambiguities, and unverified areas.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-evidence trace.

## Workflow Notes

- Build the requirement model before analysis. Do not start with judgments about missing features before the requirement set is normalized.
- Treat `required_inputs` as real prerequisites. If the source requirement set or constraint list is missing, infer a provisional frame, prefix each inferred item with `Assumed requirement:`, and lower confidence for downstream findings that depend on it.
- Preserve upstream wording when it matters so downstream teams can resolve drift without accidental reinterpretation.
- Distinguish clearly between unmet requirements, ambiguous requirements, and unverified requirements. These are not interchangeable states.
- Treat non-functional constraints such as security, rollout, permissions, privacy, and performance as requirements when they materially affect acceptance.
- Run the passes in sequence so the matrix stays grounded: extract and normalize first, map surfaces second, match evidence third, then classify gaps, ambiguity, and priority.
- Do not let strong implementation evidence hide weak requirement clarity. Poorly specified intent is itself a traceability risk.
- After all passes, consolidate repeated issues into systemic traceability patterns before prioritization.
- Distinguish clearly between observed evidence, inferred interpretation, and recommendation direction.

