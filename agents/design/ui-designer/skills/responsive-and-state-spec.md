---
name: responsive-and-state-spec
description: Build a matrix-based contract for how a UI behaves across breakpoints, device classes, and meaningful interface states.
trigger: When a design must survive real devices, async states, and content stress without losing hierarchy or usability.
primary_mcp: figma
fallback_tools: paper, chrome_devtools, search_query, open
required_inputs:
  - target surface or flow
  - expected breakpoints or device classes
  - meaningful states in scope
  - source material or prototype when available
  - known implementation constraints or release context when available
recommended_passes:
  - breakpoint inventory
  - state inventory
  - stress-case sweep
  - implementation signal check
  - exception review
tool_stack:
  - figma
  - chrome_devtools
  - playwright
  - browserstack
  - storybook visual tests
  - storybook interaction tests
  - chromatic
  - percy
  - axe
  - penpot
  - open
  - search_query
tool_routing:
  - if live runtime exists and breakpoint or state changes must be observed, use chrome_devtools and playwright.
  - if browser, device, or operating-system variance matters, add browserstack and Percy.
  - if component stories exist, use Storybook visual tests and interaction tests as the state harness.
  - if accessibility risk spans states, add axe as a supporting layer.
  - if the source of truth lives in another design tool, use that artifact path first and map it back to the shared matrix.
  - if only static artifacts exist, use figma plus open or search_query.
best_guess_output: A responsive and state specification with breakpoint matrix, state matrix, exceptions, stress cases, and implementation signals.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: responsive-and-state-spec"
done_when: Desktop, mobile, and critical states are explicitly covered, unsupported combinations are named, and implementation signals are clear enough for engineering to preserve.
---

# Responsive And State Spec

## Purpose

Define how a UI should hold up across breakpoints, device classes, and meaningful interface states.

This skill turns layout behavior into a reproducible matrix rather than a set of one-off comments.

This skill does not replace implementation QA, real-device verification, or accessibility review.

## Required Inputs and Assumptions

- Required inputs are the target surface or flow, expected breakpoint classes, meaningful states in scope, and any source material available.
- Known inputs include the surface shape, the likely interaction states, and the product context when provided.
- Unknown inputs include exact viewport limits, data volume, browser mix, and platform-specific rendering unless the assignment states them.
- If inputs are missing, infer a provisional set and label them clearly as assumptions.
- If the scope is only partly known, state the uncertainty instead of silently narrowing the matrix.

## Input Mode and Evidence Path

- Prefer the strongest available evidence path: live runtime, then structured inspection or design artifacts, then screenshots or static inference.
- For pre-implementation work, treat the design file or prototype as the source of truth and note that runtime behavior is still inferred.
- For implemented surfaces, prefer observable behavior over prose descriptions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- If the evidence is partial, say which breakpoint or state families were not directly verified.

## Tool Selection Rationale

- Use `figma` when the source is still a design artifact or prototype and the job is to define the matrix before implementation.
- Use `chrome_devtools` when the live surface exists and we need computed layout, runtime state, and DOM-backed inspection.
- Use `playwright` when the review needs reproducible viewport sweeps, branching state traversal, or screenshot capture.
- Use `browserstack` when browser, device, or operating-system variance could change the result.
- Use `axe` as a supporting layer when accessibility risk intersects with responsive or async state behavior.
- Use Storybook visual tests and interaction tests when the product has component stories and the state matrix can be validated at the component level.
- Use Chromatic or Percy when visual diffs need a baseline and review workflow across browsers or devices.
- Use Penpot when the source of truth lives outside Figma and the artifact needs libraries, components, variants, inspect data, or prototype cues.
- Use `open` and `search_query` when linked specs, docs, or repository notes are the clearest evidence path.

## Environment and Reproducibility

- Record viewport, browser, operating system, and auth state when runtime evidence exists.
- Record prototype version, design file, branch, or build identifier when those are the only sources available.
- Record the data setup or content state used to evaluate loading, empty, error, and overflow cases.
- If the environment is not fully known, say so and lower confidence for any state that depends on it.

## Model Building

- Build the responsive-state model before drawing conclusions.
- Inventory the surface into screens, components, containers, and transition points.
- Add the axes that matter: breakpoint, density, content length, loading, empty, error, success, focus, hover, disabled, and expanded or collapsed states.
- Identify which states are structural, which are transient, and which are exceptions.
- Mark any state that depends on a different data shape, locale, or permission set.

## Core Method

1. Inventory the breakpoints and screen classes that the surface must support.
2. Inventory the meaningful states and map which controls, panels, or messages change in each one.
3. Build a breakpoint/state matrix so every combination is either covered or explicitly excluded.
4. Check stress cases such as long text, empty data, slow loading, errors, and narrow containers.
5. Capture implementation signals that engineering must preserve, such as stacking order, truncation behavior, scrolling, and focus continuity.
6. Separate supported behavior from intentional exceptions and unsupported combinations.
7. Consolidate repeated issues into patterns before writing the deliverable.

## Structured Findings

Use this schema when the analysis surfaces a gap, contradiction, or unsupported combination.

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Cause:
- Impact:
- Confidence:
- Recommendation direction:

If no findings are present, say that explicitly and summarize the covered matrix instead.

## Prioritization Logic

- Treat collapsed layouts, broken reading order, hidden controls, unreachable actions, and missing critical states as high priority.
- Treat breakpoint-specific hierarchy drift, clipped content, and state-specific misalignment as medium priority unless they block use.
- Group minor spacing or density issues when they repeat across the matrix instead of splitting them into many small findings.
- Prefer standalone findings only when the issue changes the user path or implementation risk.

## Coverage Map

- Deeply reviewed: the breakpoint and state combinations that drive the main task flow.
- Partially reviewed: adjacent variants, secondary controls, and alternate content densities.
- Not reviewed: unsupported devices, niche browser behavior, unprovided locales, and states outside the assignment scope.

## Limits and Unknowns

- State clearly what could not be validated.
- State clearly which device, browser, or data permutations still need real-world verification.
- State clearly where confidence is low because the evidence path was static or partial.
- Do not imply that a visual parity check or accessibility audit has already been completed unless it actually was.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: responsive-and-state-spec`, include:
- `### Breakpoint matrix`: Specify how the UI changes across breakpoints and screen classes.
- `### State matrix`: List the meaningful interface states and how each one changes the UI.
- `### Exceptions`: Document intentional exceptions or breakpoint/state combinations that are unsupported.
- `### Stress cases`: Call out long text, empty data, loading, errors, and other resilience cases.
- `### Implementation signals`: Note the details engineering must preserve across device and state changes.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, chrome_devtools, search_query, open`.
- If the surface is implemented and runtime evidence is available, add `playwright` for reproducible sweeps and `browserstack` for cross-device variance.
- If component stories exist, add Storybook visual tests or interaction tests, and use Chromatic or Percy for visual diffs.
- If accessibility concerns affect states, add `axe` as a supporting validation layer.
- If both paths fail, produce the best-guess output described as: A responsive and state specification for the screen or flow.
- Record which tool path was used and why.

## Workflow Notes

- Treat responsive behavior and state behavior as a single matrix, not separate afterthoughts.
- Use the strongest evidence path available before leaning on inference.
- Make exceptions explicit so they are not mistaken for omissions.
- When repo or doc inspection is needed, use `open` or `search_query` rather than vague repository language.
- Prefer real state coverage over cosmetic breakpoint notes.
- If Storybook or Percy exists in the product stack, use them as the fastest way to validate state permutations and visual regressions.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: responsive-and-state-spec`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Desktop, mobile, and critical states are explicitly covered, unsupported combinations are named, and implementation signals are clear enough for engineering to preserve.
