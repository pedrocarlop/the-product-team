---
name: regression-triage
description: Triage regressions by building a regression model, validating reproduction status, and separating user impact, scope, evidence strength, and release impact instead of collapsing them into raw bug counts.
trigger: When a build, feature, or release candidate has defects and the team needs a structured blocking versus non-blocking decision.
decision_framework: regression triage across reproducibility, blast radius, user impact, release exposure, and confidence
primary_mcp: repository, chrome_devtools
fallback_tools:
  - reference/verify
  - open
required_inputs:
  - target build, branch, release candidate, or change window
  - candidate regressions or reported symptoms
  - affected flows, users, or business surfaces when known
  - environment and state assumptions for reproduction
  - release timing or decision context when known
recommended_passes:
  - regression inventory and deduplication
  - reproduction validation
  - scope and blast radius mapping
  - severity, frequency, and confidence separation
  - release impact and next action routing
tool_stack:
  runtime:
    primary: [repository, chrome_devtools]
    secondary: [logs]
  artifacts:
    primary: [reference/verify]
    secondary: [open]
  fallback:
    primary: [open]
tool_routing:
  - if: repository context and live runtime are both available
    use: [repository, chrome_devtools]
  - if: reproduction depends on runtime behavior, request flow, or browser-visible failure
    use: [chrome_devtools]
  - if: regression evidence mostly exists in implementation notes, commits, logs, or review artifacts
    use: [repository, reference/verify]
  - if: only linked issue context, screenshots, or static artifacts exist
    use: [open]
best_guess_output: A regression triage with evidence-tagged severity, blocking status, and next-action routing.
output_artifacts: knowledge/reviews/qa-reviewer.md
done_when: Blocking and non-blocking regressions are clearly separated with evidence, rationale, confidence, and next action, and duplicate or systemic issues are grouped instead of counted loosely.
---

# Regression Triage

## Purpose

Triage regressions by building a regression model first, then validating which reported issues are real, reproducible, and release-relevant.

This skill applies structured QA reasoning across reproducibility, user impact, blast radius, and release exposure.

This skill does not replace root-cause analysis, full remediation planning, or product prioritization beyond the evidence-supported release decision.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/qa-reviewer-regression-triage.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: regression-triage`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Review framing`: Define the build, branch, release candidate, change window, and the decision this triage must support.
- `### Required inputs and assumptions`: State the known defect sources, environment assumptions, affected flows, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live reproduction, structured runtime plus repository evidence, review artifacts or issue history, then static or inferred evidence.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record browser, operating system, viewport, auth state, data state, build version, feature flags, and parity gaps when known.
- `### Regression model`: Build the regression model first by listing candidate regressions, baseline expectations, affected surfaces, suspected change windows, and deduped issue groupings before severity calls.
- `### Regression inventory`: List the candidate regressions, grouped issue families, source signals, and current evidence status before prioritization.
- `### Reproduction status`: Record whether each issue is confirmed, intermittent, suspected, unresolved, or blocked by environment mismatch.
- `### Affected scope and users`: State which flows, users, accounts, devices, or business surfaces appear affected and how broad the blast radius is.
- `### Triage passes`: List the passes used such as regression inventory and deduplication, reproduction validation, scope and blast radius mapping, severity and frequency separation, and release impact routing.
- `### Regression findings`: Record findings using the required finding schema below.
- `### Prioritized regressions`: Include all release-blocking or major regressions as standalone findings, group minor or duplicate issues into patterns, and prefer no more than 15 standalone findings by default unless additional findings are materially distinct or high severity.
- `### Systemic patterns`: Group repeated regressions by shared flow, dependency, platform, or likely root-cause family.
- `### Severity and release impact`: Keep user severity separate from gate impact and explain the release implication for each major regression.
- `### Frequency and confidence`: Separate how often the issue appears from how strong the evidence is and where reproduction remains unstable.
- `### Severity, frequency, confidence, and release impact`: Keep these dimensions separate and explain where evidence is strong, intermittent, or weak.
- `### Blocking vs non-blocking decision`: Classify each major issue and justify the gate implication.
- `### Recommended next actions`: Route each issue toward fix now, verify further, monitor, add coverage, clarify scope, or accept temporary risk.
- `### Coverage map`: State what was deeply triaged, partially triaged, and not triaged.
- `### Limits and unknowns`: Explain where missing environment parity, low reproduction success, or stale evidence weakened the triage.

For each finding inside `### Regression findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Regression status:
- Likely cause area:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the highest-fidelity evidence path available: live reproduction -> structured runtime plus repository evidence -> review artifacts -> static evidence -> inference.
- Start with `repository, chrome_devtools` when code context and runnable behavior are both available.
- Use `chrome_devtools` when regression confirmation depends on visible runtime behavior, network activity, timing, or browser-state inspection.
- Use `repository` to map suspected regressions to change windows, feature flags, test coverage, and implementation surfaces.
- Use `reference/verify` when prior review artifacts, issue threads, linked evidence, or repository notes are the strongest available trace.
- Use `open` only when linked artifacts or static references are the best evidence left.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, open`.
- If both paths fail, produce the best-guess output described as: A regression triage with evidence-tagged severity, blocking status, and next-action routing.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-path triage.

## Workflow Notes

- Treat this as a decision skill, not a bug dump.
- Treat `required_inputs` as real prerequisites. If the change window, affected flows, or environment assumptions are missing, infer a provisional set, prefix each inferred item with `Assumed regression context:`, and lower confidence for downstream findings that depend on it.
- Build the regression model before analysis. Do not jump from defect reports straight to blocking decisions.
- Deduplicate first. Multiple reports may reflect the same regression and should be grouped before prioritization.
- Separate reproduction status from severity. A hard-to-reproduce issue can still be severe, and a frequent issue can still be low impact.
- Separate user impact from release impact. Some regressions matter because they block core release goals, while others matter because of broad user harm even if the release could technically proceed.
- Treat missing baseline knowledge as a real confidence limiter, not as proof the issue is acceptable.
- Use the passes in sequence so findings stay grounded: inventory first, reproduction second, scope third, then severity, frequency, confidence, and release routing.
- After all passes, merge duplicate findings and consolidate overlapping regressions into systemic patterns before final prioritization.
- Distinguish clearly between observed regression behavior, inferred cause area, and recommendation direction.

