---
name: accessibility-review
description: Run a barrier-focused accessibility review by building an accessibility model, traversing task paths, and grounding barrier findings in the strongest available evidence path.
trigger: When accessibility risk needs a structured expert review before release, sign-off, or remediation planning.
heuristic_framework: WCAG-informed barrier review with assistive technology impact framing
primary_mcp: chrome_devtools
fallback_tools:
  - figma
  - reference/ground
  - search_query
required_inputs:
  - target flow or surface
  - target users or assistive scenarios
  - platform, viewport, and state assumptions
  - known compliance scope or release context when available
recommended_passes:
  - semantic structure and naming
  - keyboard and focus traversal
  - perception and readability
  - status, errors, and recovery
  - motion, timing, and dynamic updates
tool_stack:
  runtime:
    primary: [chrome_devtools, playwright]
    secondary: [browserstack]
    support: [axe]
  native_apps:
    primary: [appium]
    platform_specific: [xcode_ui_testing, android_espresso]
  design_artifacts:
    primary: [figma]
    secondary: [reference/ground]
  fallback_evidence:
    primary: [screenshots, video_capture]
    secondary: [vision_ocr]
tool_routing:
  - if: live web product is available and interactive
    use: [chrome_devtools, playwright]
  - if: issue depends on multi-step traversal, dynamic states, or reproducible flows
    use: [playwright]
  - if: issue may vary by browser, viewport, operating system, or real device behavior
    use: [browserstack]
  - if: target is a native mobile app
    use: [appium]
  - if: target is iOS-only and local project access exists
    use: [xcode_ui_testing]
  - if: target is Android-only and local project access exists
    use: [android_espresso]
  - if: runtime is unavailable but design artifacts exist
    use: [figma, reference/ground]
  - if: only screenshots or recordings exist
    use: [screenshots, video_capture, vision_ocr]
  - if: DOM-backed automated checks can strengthen runtime evidence
    use: [axe]
best_guess_output: An accessibility review with evidence-tagged barriers, grouped patterns, and directional remediation guidance.
output_artifacts: logs/active/<project-slug>/reviews/design-reviewer.md
section_anchor: "## Skill: accessibility-review"
done_when: The reviewed surface has evidence-backed accessibility barriers, grouped patterns, coverage limits, and prioritized fix directions that distinguish observed issues from assumptions.
---

# Accessibility Review

## Purpose

Run a barrier-focused accessibility review of a product surface by modeling semantics, interaction paths, perception demands, and feedback exposure before drawing conclusions.

This skill evaluates observable accessibility risk and likely assistive technology impact.

This skill does not claim formal compliance certification, replace full screen-reader or human assistive testing, or assert that code-level remediation has already been validated.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: accessibility-review`, include:
- `### Review framing`: Define the surface reviewed, user goals, target users or assistive scenarios considered, and whether this is pre-release inspection, regression review, or remediation triage.
- `### Required inputs and assumptions`: State the target flow or surface, known assistive contexts, platform assumptions, and any missing inputs inferred by the reviewer.
- `### Coverage and assistive assumptions`: State the assistive scenarios, device assumptions, and what kind of runtime or artifact coverage the review actually achieved.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live interaction, structured runtime inspection, design artifacts, screenshots or recordings, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record browser, operating system, viewport, auth state, data setup, build or prototype version, and any assistive tooling actually used when known.
- `### Accessibility model`: Build the interaction and accessibility model first by documenting key screens, landmarks, headings, forms, controls, focus transitions, status regions, and dynamic states.
- `### WCAG lens and evaluator passes`: State the WCAG-informed lens used and list the passes run such as semantic structure and naming, keyboard and focus traversal, perception and readability, status and recovery, and motion or timing sensitivity.
- `### Semantic and structural findings`: Record issues related to landmarks, headings, names, roles, labels, reading order, and semantic structure.
- `### Keyboard and focus findings`: Record issues related to keyboard access, tab order, focus visibility, focus recovery, and interactive reachability.
- `### Perception and feedback findings`: Record issues related to contrast, readability, status messaging, errors, recovery cues, motion, and timing.
- `### Barrier findings`: Record findings using the required finding schema below.
- `### Prioritized barriers`: Include all critical and major barriers as standalone findings, group minor issues into patterns, and prefer no more than 15 standalone findings by default unless additional findings are materially distinct or high severity.
- `### Systemic patterns`: Cluster repeated problems such as unlabeled controls, broken focus recovery, weak error recovery, or inaccessible dynamic updates.
- `### Coverage map`: State what was deeply reviewed, partially reviewed, and not reviewed.
- `### Impact and confidence`: Separate user impact severity from evidence confidence and coverage confidence.
- `### Severity, confidence, and coverage confidence`: Separate user impact severity from evidence confidence and state whether coverage came from live runtime, partial traversal, static artifact review, or screenshot-only inference.
- `### Fix directions`: Link remediation directions to the findings without pretending every implementation fix has already been validated.
- `### Directional fix guidance`: Link remediation directions to the findings without pretending every fix has already been validated.
- `### Limits and unknowns`: Explain what still requires real assistive technology testing, manual engineering inspection, localization review, or cross-device verification.

For each finding inside `### Barrier findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Likely cause:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the highest-fidelity evidence path available: live interaction -> structured runtime inspection -> design artifacts -> screenshots or recordings -> inference.
- Start with `chrome_devtools` for DOM semantics, accessibility tree signals, state changes, focus behavior, console issues, and runtime inspection when a live web surface exists.
- Use `playwright` when the review depends on reproducible multi-step traversal, branching flows, asynchronous updates, or coverage of multiple states.
- Use `browserstack` when the issue may depend on Safari, iOS, Android, viewport variance, browser behavior, or real-device rendering and interaction.
- Use `appium` for native mobile app accessibility review across iOS and Android.
- Use platform-native tooling such as `xcode_ui_testing` or `android_espresso` when local project access exists and platform-specific behavior matters.
- Use `axe` as a supporting validation layer for detectable runtime issues, never as a substitute for manual barrier analysis.
- Use `figma` when runtime does not exist or when the review is pre-implementation.
- Use screenshot or video fallback only when no interactive or design artifact path is available.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: An accessibility review with evidence-tagged barriers, grouped patterns, and directional remediation guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-tool review.

## Workflow Notes

- Treat this as a barrier review, not as a formal certification pass.
- Treat `required_inputs` as real prerequisites. If target users or assistive scenarios are missing, infer a provisional set, prefix each inferred item with `Assumed scenario:`, and lower confidence for findings that depend on it.
- Build the accessibility model before analysis. Do not jump from surface impressions to issue lists.
- Prefer observable behavior over theoretical code critique whenever a live or inspectable runtime exists.
- Evaluate flows and states, not only static screens. Accessibility failures often appear during validation, async updates, modal transitions, focus changes, and recovery moments.
- Run evaluator passes in sequence so findings stay grounded: semantic structure first, keyboard and focus second, perception and readability third, then status, recovery, motion, and timing.
- Distinguish clearly between observed evidence, inferred cause, and recommendation direction.
- Use WCAG and platform conventions as interpretive framing, but keep every finding tied to concrete user impact and reproducible evidence.
- After all passes, merge duplicates and consolidate overlapping issues before prioritization.
- Always include critical barriers. Group low-impact or repetitive issues into patterns instead of inflating the standalone finding count.
- State clearly when a suspected issue could not be fully confirmed because the evidence path did not include real assistive technology, real devices, or implementation inspection.
- Do not imply that screen-reader output, switch control behavior, voice control behavior, or full cognitive accessibility outcomes were validated unless they were actually tested.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/design-reviewer.md`.
- Keep all work for this skill inside `## Skill: accessibility-review`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The reviewed surface has evidence-backed accessibility barriers, grouped patterns, coverage limits, and prioritized fix directions that distinguish observed issues from assumptions.
