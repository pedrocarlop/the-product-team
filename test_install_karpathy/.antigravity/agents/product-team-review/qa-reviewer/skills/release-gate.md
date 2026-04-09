---
name: release-gate
description: Make a release recommendation by building a release-readiness model and weighing blockers, residual risk, evidence quality, rollback posture, and operating readiness instead of treating test completion as automatic safety.
trigger: When work is nearing release and needs a structured ship, conditional-ship, or no-ship QA gate.
mesh:
  inputs:
    - qa-reviewer:test-plan-review
  next:
    - go-to-market:launch-plan
  context: "Final QA gate before handing off to GTM for launch."
decision_framework: release-readiness synthesis across blockers, residual risk, evidence quality, rollback posture, and owner readiness
primary_mcp: repository, logs
fallback_tools:
  - qa-reviewer/runtime-network-audit
  - qa-reviewer/test-plan-review
required_inputs:
  - exact release candidate, build, or branch under review
  - release scope and critical user journeys
  - available test, runtime, and issue evidence
  - rollback, monitoring, and operational readiness context
  - explicit ship criteria or decision deadline when known
recommended_passes:
  - release scope and evidence inventory
  - blocker validation
  - residual risk assessment
  - evidence quality and freshness review
  - rollback and readiness posture check
tool_stack:
  synthesis:
    primary: [repository, logs]
    secondary: [qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review]
  artifacts:
    primary: [reference/verify]
  fallback:
    primary: [qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review]
tool_routing:
  - if: release evidence, issue state, and repository context are all accessible
    use: [repository, logs]
  - if: runtime confidence is the main uncertainty
    use: [qa-reviewer/runtime-network-audit]
  - if: planned coverage depth is the main uncertainty
    use: [qa-reviewer/test-plan-review]
  - if: direct evidence is partial and prior QA artifacts are the strongest available signal
    use: [reference/verify]
best_guess_output: A release gate recommendation with blocking issues, residual risk, and explicit confidence.
output_artifacts: knowledge/reviews/qa-reviewer.md
done_when: The release recommendation is unambiguous, evidence-based, explicit about residual risk, and clear about what must happen before or after ship.
---

# Release Gate

## Purpose

Make a release recommendation by synthesizing QA evidence into a release-readiness model before declaring ship, conditional ship, or no-ship.

This skill applies evidence-based release decision reasoning across blockers, residual risk, evidence quality, rollback posture, and operating readiness.

This skill does not replace product leadership approval, incident command authority, or execution of rollback and monitoring plans.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/qa-reviewer-release-gate.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: release-gate`, include:
- `### Gate framing`: Define the exact release candidate, environment, scope, ship criteria, and decision horizon.
- `### Required inputs and assumptions`: State what evidence was available, what was missing, and which assumptions the reviewer had to make.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: current release evidence and live signals, structured logs and repository context, prior QA artifacts, then inference.
- `### Tool selection rationale`: State which tools were used, why they were selected, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record the release environment, build or version identifiers, auth and data assumptions, feature flags, and any environment-parity caveats.
- `### Release-readiness model`: Build the model first by listing critical journeys, operational dependencies, open defects, known mitigations, and go-live containment mechanisms before deciding ship status.
- `### Gate passes`: List the passes used such as release scope and evidence inventory, blocker validation, residual risk assessment, evidence quality and freshness review, and rollback and readiness posture check.
- `### Evidence reviewed`: Summarize the test evidence, runtime evidence, open issues, mitigations, and supporting artifacts that informed the gate.
- `### Gate findings`: Record findings using the required finding schema below.
- `### Ship recommendation`: State one top-level recommendation only: ship, ship with explicit risk acceptance, or no-ship.
- `### Blocking issues`: Include all must-fix or must-validate conditions that prevent a clean ship.
- `### Non-blocking risks`: Record the residual risks that do not block release but still need explicit ownership, monitoring, or follow-up.
- `### Residual non-blocking risks`: Record what remains risky but acceptable only with explicit ownership or monitoring.
- `### Evidence quality and confidence`: Separate weak evidence from positive evidence and explain whether evidence is current, partial, stale, or indirect.
- `### Rollback and readiness posture`: Capture rollback availability, monitoring readiness, owner readiness, containment paths, and operational support posture.
- `### Rollback and operational readiness`: Capture rollback availability, monitoring posture, owner readiness, containment plans, and alertability.
- `### Required follow-up`: State the exact next actions, ownership expectations, or post-ship checks required.
- `### Systemic release patterns`: Group recurring weaknesses such as missing observability, repeated flaky validation, or risky manual steps.
- `### Coverage map`: State what was deeply reviewed, partially reviewed, and not reviewed before the gate.
- `### Limits and unknowns`: Explain what decision uncertainty remains and what still requires real-world validation.

For each finding inside `### Gate findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps or validation path:
- Gate implication:
- Likely cause area:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest release-decision evidence path available: current release evidence and live signals -> structured logs and repository context -> prior QA artifacts -> inference.
- Start with `repository, logs` when release notes, defects, validation evidence, and operational signals are accessible.
- Use `logs` when confidence depends on recent runtime evidence, alerting posture, or operational anomalies near release time.
- Use `repository` to confirm scope, open-change surfaces, coverage artifacts, and the exact candidate under review.
- Use `qa-reviewer/runtime-network-audit` when runtime behavior or production-like flow confidence is the main unresolved risk.
- Use `qa-reviewer/test-plan-review` when coverage sufficiency, risk mapping, or test depth is the main unresolved risk.
- Use `reference/verify` when prior QA outputs or linked validation artifacts are the strongest evidence available.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review`.
- If both paths fail, produce the best-guess output described as: A release gate recommendation with blocking issues, residual risk, and explicit confidence.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-input gate.

## Workflow Notes

- Treat this as a synthesis skill. The goal is not to rerun every test, but to decide whether the available evidence supports ship.
- Treat `required_inputs` as real prerequisites. If ship criteria, rollback posture, or release scope are missing, infer a provisional frame, prefix each inferred item with `Assumed gate context:`, and lower confidence for gate findings that depend on it.
- Build the release-readiness model before making a recommendation. Do not jump from a list of bugs to ship or no-ship.
- Keep the top-level recommendation binary enough to act on even when the supporting evidence is nuanced.
- Separate absence of evidence from evidence of safety. Missing proof should lower confidence, not silently convert to a pass.
- Evaluate operational readiness as part of QA gating. Weak rollback, monitoring, or ownership posture can turn moderate defects into blocking release risk.
- Run the passes in sequence so the decision stays grounded: scope and evidence inventory first, blockers second, residual risk third, evidence quality fourth, then rollback and readiness posture.
- After all passes, group repeated weaknesses into systemic patterns rather than scattering them across many one-off findings.
- Distinguish clearly between observed evidence, inferred risk, and recommendation direction.

