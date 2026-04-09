---
name: usability-review
description: Run an expert usability inspection of a flow or surface by building a UI model, walking key tasks, and grounding findings in Nielsen's heuristics across the strongest available evidence path.
trigger: When UX quality needs a focused expert inspection pass before sign-off, bug filing, or remediation planning.
heuristic_framework: Nielsen 10 usability heuristics
primary_mcp: chrome_devtools
fallback_tools:
  - figma
  - reference/ground
required_inputs:
  - target flow or surface
  - top tasks to inspect
  - target user type
  - platform and state assumptions
recommended_passes:
  - learnability
  - efficiency
  - consistency
  - error prevention and recovery
tool_stack:
  live_web:
    primary: [chrome_devtools, playwright]
    secondary: [browserstack]
    support: [axe]
  native_apps:
    primary: [appium]
    platform_specific: [xcode_ui_testing, android_espresso]
    secondary: [browserstack_app_automate]
  design_artifacts:
    primary: [figma]
    secondary: [reference/ground]
  fallback_evidence:
    primary: [screenshots, video_capture]
    secondary: [vision_ocr]
tool_routing:
  - if: live web product is available and interactive
    use: [chrome_devtools, playwright]
  - if: issue needs reproducible multi-step traversal or state coverage
    use: [playwright]
  - if: issue may vary by browser, viewport, or device
    use: [browserstack]
  - if: target is native iOS or Android app
    use: [appium]
  - if: target is iOS-only and local project access exists
    use: [xcode_ui_testing]
  - if: target is Android-only and local project access exists
    use: [android_espresso]
  - if: runtime is unavailable but design artifacts exist
    use: [figma, reference/ground]
  - if: only screenshots or recordings exist
    use: [screenshots, video_capture, vision_ocr]
  - if: accessibility validation is relevant
    use: [axe]
best_guess_output: A usability review with concrete friction points, grouped patterns, and clearly marked evidence limits.
output_artifacts: knowledge/reviews/design-reviewer.md
done_when: The biggest usability risks are explicit, reproducible, severity-rated, grouped into actionable patterns, and labeled by evidence confidence.
---

# Usability Review

## Purpose

Run an expert usability inspection of a flow or surface using UI modeling, task walkthroughs, and heuristic evidence before concluding where the flow breaks down.

This skill evaluates likely friction, confusion, and recovery risk from an expert inspection standpoint.

This skill does not replace moderated research, analytics-backed behavioral evidence, or product prioritization decisions.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-reviewer-usability-review.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: usability-review`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Review framing`: Define the user goal, task context, intended audience, and why this is an expert inspection rather than user testing.
- `### Required inputs and assumptions`: State the target flow or surface, top tasks selected in advance, target user type, and platform or state assumptions.
- `### Heuristic framework and evaluator passes`: Name Nielsen's 10 usability heuristics as the default framework and list the passes used such as learnability, efficiency, consistency, and error prevention and recovery.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live interactive runtime with reproducible traversal, real-device or cross-browser validation, design artifact inspection, then screenshot or video inference.
- `### Tool selection rationale`: State which tools were used, why they were selected, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record viewport, browser, operating system, auth state, data setup, and build or prototype version when known.
- `### UI model`: Capture screens, flows, components, states, and transitions before evaluating issues.
- `### Task walkthroughs`: Simulate the main tasks step by step using goal -> action -> system response -> next step.
- `### Heuristic findings`: Evaluate the surfaced behavior against usability heuristics using the required finding schema below.
- `### Prioritized findings`: Include all critical and major issues as standalone findings, group minor issues into systemic patterns, and prefer no more than 15 standalone findings by default unless additional findings are materially distinct or high severity.
- `### Systemic patterns`: Cluster issues into recurring patterns such as weak feedback, poor affordance, broken mental model, or inconsistent labels.
- `### Coverage map`: State which screens or flows were well reviewed, lightly reviewed, or not reviewed.
- `### Severity, confidence, and coverage confidence`: Score severity using frequency, impact, and persistence, use blocking status as supporting context, separate confidence from severity, and state whether coverage came from full interactive traversal, partial traversal, static artifact review, or screenshot-only inference.
- `### Directional recommendations`: Offer pattern-level or flow-level improvement directions rather than overconfident final solutions.
- `### Limits and unknowns`: Explain what could not be validated and what still requires real user testing or product context.

For each finding inside `### Heuristic findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Violated heuristic:
- Likely cause:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the highest-fidelity path available: runtime real -> traversal reproducible -> real devices -> design static -> screenshots.
- Start with `chrome_devtools` for quick DOM, layout, console, network, and state inspection when a live web surface is available.
- Use `playwright` when the review requires reproducible traversal, branching states, or multi-step flows.
- Use `browserstack` when the issue may depend on browser differences, Safari or iOS behavior, viewport variance, or real devices.
- Use `appium` for native mobile app flows across iOS and Android.
- Use platform-native tooling such as `xcode_ui_testing` or `android_espresso` when local project-level app inspection is available and platform-specific behavior matters.
- Use `figma` when runtime does not exist or when the review is pre-implementation.
- Use screenshot or video fallback only when no interactive or design artifact path is available.
- Use `axe` as a supporting layer for accessibility violations, never as a substitute for full usability review.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, reference/ground`.
- If both paths fail, produce the best-guess output described as: A usability review with concrete friction points, grouped patterns, and clearly marked evidence limits.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single path.

## Workflow Notes

- Treat this as usability inspection by a simulated expert evaluator, not as user research or moderated testing.
- Treat `required_inputs` as real prerequisites. If top tasks are missing, infer a provisional top-task set from the surface, prefix each inferred item with `Assumed task:`, and lower confidence for downstream findings that depend on it.
- Build a UI model first. Do not jump straight to issue lists from loose impressions.
- Prefer live interaction over static review. When only design files or screenshots exist, make the evidence limits explicit.
- Run task walkthroughs before heuristics so findings stay grounded in user goals instead of generic commentary.
- Run multiple passes when the scope matters: learnability first, then efficiency, consistency, and error prevention and recovery.
- After all evaluator passes, merge duplicates and consolidate overlapping findings before prioritization.
- Cover the whole flow when possible. The agent is useful because it can inspect more combinations and more states than a quick human spot check.
- Use Nielsen's 10 usability heuristics by default unless the assignment overrides the framework explicitly.
- Use severity carefully. Severity is high-variance in inspection work, so record both rationale and confidence instead of pretending precision. Score severity using frequency, impact, and persistence; treat blocking status as supporting context rather than a substitute.
- Distinguish clearly between observed evidence, inferred cause, and recommendation.
- Do not claim emotional trust, business priority, or true user comprehension has been validated unless real user evidence exists.

