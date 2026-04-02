---
name: test-plan-review
description: Review a test strategy by building a risk model and a coverage matrix that separates missing coverage, shallow coverage, environment blind spots, and residual uncertainty instead of treating test type counts as adequacy.
trigger: When a feature, milestone, or release needs a structured review of whether the proposed test plan covers the real risks.
analysis_framework: risk-based coverage review across product risk, technical depth, environment variance, and release criticality
primary_mcp: repository, logs
fallback_tools:
  - reference/trace
  - search_query
required_inputs:
  - release or feature scope under review
  - proposed tests, existing suites, or validation artifacts
  - major product, technical, and operational risks
  - target environments, browsers, devices, or states when known
  - timing, ownership, or launch constraints when known
recommended_passes:
  - risk inventory construction
  - coverage matrix mapping
  - depth and layering assessment
  - state and environment gap analysis
  - release-critical recommendation shaping
tool_stack:
  synthesis:
    primary: [repository, logs]
    secondary: [reference/trace]
  enrichment:
    primary: [search_query]
  fallback:
    primary: [reference/trace, search_query]
tool_routing:
  - if: repository evidence and current validation artifacts are accessible
    use: [repository, logs]
  - if: the strongest evidence is prior plans, traces, or linked QA artifacts
    use: [reference/trace]
  - if: external standards, browser constraints, or ecosystem behaviors materially affect coverage needs
    use: [search_query]
best_guess_output: A test plan review with explicit risk coverage, gaps, and priority recommendations.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
section_anchor: "## Skill: test-plan-review"
done_when: Critical risks have explicit coverage mapping, missing depth is visible, blind spots are named, and the highest-value additions are prioritized.
---

# Test Plan Review

## Purpose

Review a test strategy by building a risk model first, then mapping planned and existing coverage against that model explicitly.

This skill applies risk-based QA reasoning across product risk, technical depth, environment variance, and release criticality.

This skill does not equate more tests with better coverage, replace implementation of the tests themselves, or promise that a reviewed plan guarantees safety.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: test-plan-review`, include:
- `### Review framing`: Define the release or feature scope, available test artifacts, and what decisions this test-plan review must support.
- `### Required inputs and assumptions`: State the known risks, environments, ownership constraints, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: current test assets and implementation evidence, structured logs and prior QA traces, external or linked guidance, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record the target browsers, devices, states, datasets, feature flags, build version, and timing constraints when known.
- `### Risk model`: Build the model first by listing the major product, technical, and operational risks plus the affected flows and environments before evaluating the plan.
- `### Review passes`: List the passes used such as risk inventory construction, coverage matrix mapping, depth and layering assessment, state and environment gap analysis, and release-critical recommendation shaping.
- `### Risk inventory`: Enumerate the major product, technical, and operational risks that require explicit coverage.
- `### Coverage matrix`: Map each major risk to planned or existing tests, evidence quality, owners, and current gaps.
- `### Test-plan findings`: Record findings using the required finding schema below.
- `### Depth by risk`: Evaluate whether each risk has appropriate unit, integration, end-to-end, manual, synthetic, or monitoring coverage.
- `### Missing states and environments`: Call out missing coverage for breakpoints, browsers, devices, permissions, data conditions, feature flags, failure paths, or operational states.
- `### Release-critical gaps`: Highlight the under-tested risks that materially affect launch decisions.
- `### Systemic coverage patterns`: Group recurring weaknesses such as happy-path bias, weak failure-path coverage, environment blind spots, or ownership gaps.
- `### Recommended additions`: Suggest the highest-value test additions or reshaping of effort tied to the specific risks they close.
- `### Recommendations`: Suggest the highest-value test additions or reshaping of effort and link them to the specific risks they address.
- `### Coverage map`: State what was deeply reviewed, partially reviewed, and not reviewed.
- `### Residual blind spots`: State what would remain uncertain even after the recommended improvements.
- `### Limits and unknowns`: Explain what could not be verified from the available artifacts.

For each finding inside `### Test-plan findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Covered risk:
- Existing coverage:
- Gap type:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest coverage evidence path available: current test assets and implementation evidence -> structured logs and prior QA traces -> external or linked guidance -> inference.
- Start with `repository, logs` when the proposed plan, existing suites, failures, and validation artifacts are accessible.
- Use `repository` to inspect test suites, code paths, configuration, ownership signals, and implementation surfaces that should be covered.
- Use `logs` when recent failures, flaky behavior, runtime alerts, or previous validation results materially affect what coverage is needed.
- Use `reference/trace` when prior QA plans, historical audits, or linked traces are the strongest available plan context.
- Use `search_query` only when external platform behavior, browser/device nuances, or domain-specific constraints materially change the recommended test shape.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A test plan review with explicit risk coverage, gaps, and priority recommendations.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-source review.

## Workflow Notes

- Review the plan against risk, not against idealized process or test-count targets.
- Treat `required_inputs` as real prerequisites. If the risk model, environment scope, or ownership constraints are missing, infer a provisional set, prefix each inferred item with `Assumed test context:`, and lower confidence for downstream findings that depend on it.
- Build the risk model before analysis. Do not start with generic advice such as adding more end-to-end coverage.
- Prefer explicit risk-to-test mapping over generic statements. Every recommendation should close a named gap.
- Separate missing coverage from insufficient depth. A risk can be covered but still be under-tested.
- Make environment and state coverage explicit because many launch failures hide outside the happy path.
- Run the passes in sequence so the review stays grounded: inventory risks first, map coverage second, assess depth third, then surface environment gaps and release-critical implications.
- After all passes, consolidate repeated weaknesses into systemic coverage patterns before prioritization.
- Distinguish clearly between observed evidence, inferred risk, and recommendation direction.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/qa-reviewer.md`.
- Keep all work for this skill inside `## Skill: test-plan-review`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Critical risks have explicit coverage mapping, missing depth is visible, blind spots are named, and the highest-value additions are prioritized.
