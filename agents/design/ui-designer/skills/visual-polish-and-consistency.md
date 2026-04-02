---
name: visual-polish-and-consistency
description: Run an evidence-based final polish pass that checks hierarchy, spacing, typography, and cross-surface consistency before handoff.
trigger: When a design is structurally sound but still needs a final consistency and regression pass.
primary_mcp: figma
fallback_tools: paper, chrome_devtools
best_guess_output: A polished design with a concrete issue-fix list, consistency notes, and readiness limits.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: visual-polish-and-consistency"
done_when: The design reads as deliberate and consistent, with concrete fixes, coverage notes, and readiness gaps called out.
required_inputs:
  - target surface, route, or screen set
  - design source or implementation artifact
  - adjacent surfaces or system references for comparison
  - known breakpoints, states, and browser or device scope
  - release or merge threshold when known
recommended_passes:
  - hierarchy and alignment scan
  - typography and token alignment
  - cross-surface consistency check
  - breakpoint and state regression scan
  - final ship-readiness gate
tool_stack:
  runtime:
    primary: [chrome_devtools]
    secondary: [playwright, browserstack]
  artifacts:
    primary: [figma]
    secondary: [storybook, penpot, framer]
  fallback:
    primary: [screenshots, video_capture]
tool_routing:
  - if: a live implementation is available and interactive
    use: [chrome_devtools]
  - if: repeatable regression checks or before-and-after comparisons are needed
    use: [playwright]
  - if: a component explorer exists and the problem is component-level
    use: [storybook]
  - if: the canonical source of truth lives in a design tool
    use: [figma]
  - if: the review is happening in Penpot or Framer
    use: [penpot, framer]
  - if: browser, viewport, or device variance is suspected
    use: [browserstack]
  - if: only screenshots, exports, or recordings exist
    use: [screenshots, video_capture]
---

# Visual Polish And Consistency

## Purpose

Run the final pass on alignment, hierarchy, typography, spacing, and consistency.

This skill checks whether a design is visually deliberate, internally consistent, and safe to hand off without sanding away the intended concept.

This skill does not redesign the concept, widen scope, or treat taste-based polish as a substitute for source-of-truth validation.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.
- The role deliverable must end with `## Reflection`.

## Required Inputs and Assumptions

Required inputs:
- Target surface, route, or screen set.
- Source artifact to review, ideally the current implementation plus the design reference.
- Neighboring surfaces or component families that define the local visual system.
- Breakpoints and state scope when responsive or async behavior matters.

Assumptions:
- If the scope is missing, assume the most visible surface in the current flow and label that assumption.
- If the source of truth is incomplete, treat the missing area as a gap to call out, not a reason to invent details.
- If implementation access is unavailable, lower confidence and rely on artifact evidence or screenshots.

## Input Mode and Evidence Path

Use the strongest available evidence path in this order:
1. Live implementation or real interaction in `chrome_devtools`.
2. Repeatable runtime inspection with `playwright` or a component explorer such as `storybook`.
3. Design artifacts in `figma`, or equivalent source artifacts in `penpot` or `framer`.
4. Screenshots, static exports, or recordings.
5. Inference only when nothing else is available.

### Tool selection rationale

- Use `chrome_devtools` for computed layout, actual rendering, console evidence, and state-specific visual checks.
- Use `playwright` when the same comparison must be repeated across breakpoints, flows, or regression baselines.
- Use `storybook` when the component is isolated from the full app and visual consistency needs to be checked at the component layer.
- Use `figma` when the canonical design source is still upstream of implementation.
- Use `penpot` or `framer` when those are the actual design workspaces or when shared inspect/prototype context is needed.
- Use screenshots or recordings only as a lower-fidelity fallback, and state the limitation explicitly.

### Environment and reproducibility

Record the viewport, browser, operating system, auth state, data state, and build or prototype version when known.

If any of those are unknown, label them as unknown instead of assuming a stable environment.

## Model Building

Before evaluating polish, build a surface model that captures:
- Screens and component families in scope.
- Visual hierarchy and reading order.
- Spacing, density, and alignment rules.
- Token usage, typography scale, and color relationships.
- Breakpoints, hover, focus, loading, empty, and error states.
- Adjacent surfaces that should look and behave consistently.

No conclusions should be written before this model exists.

## Core Method Execution

1. Confirm the source of truth and the comparison scope.
2. Walk the surface for hierarchy, spacing, typography, alignment, and token drift.
3. Compare the surface against adjacent screens and the broader system so isolated polish does not create local inconsistency.
4. Check breakpoint and state coverage for regression risk, including loading, empty, error, hover, and focus behavior when relevant.
5. Merge duplicate issues, separate local noise from systemic patterns, and mark anything that would require upstream system changes.
6. Record concrete fixes, readiness limits, and any over-polish risk.

## Structured Findings

Use a strict issue/fix schema.

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Likely cause:
- Impact:
- Severity:
- Proposed fix:
- Confidence:

Rules:
- Separate observed drift from interpretation.
- Use exact visual evidence, not vague impressions.
- Every finding must end with a concrete fix direction.

## Prioritization Logic

- Always include blocking or high-impact issues as standalone findings.
- Group low-impact spacing, alignment, or typography nits into patterns when they share the same cause.
- Prefer fewer, stronger findings over a long list of near-duplicates.
- If a fix would materially change the concept, classify it as an upstream design decision or over-polish risk rather than a local polish task.

## Coverage Map

State which areas were:
- Deeply checked.
- Partially checked.
- Not checked.

Cover the full flow when possible, not just the hero screen.

## Limits and Unknowns

Call out what could not be validated, what requires real browser or device evidence, and where confidence is low.

If the environment, source, or breakpoint coverage is partial, say so directly.

## Required Deliverable Sections

Within `## Skill: visual-polish-and-consistency`, include:
- `### Visual issues`: List the concrete hierarchy, spacing, alignment, and typography issues found.
- `### Proposed fixes`: Pair each issue with the exact correction to apply.
- `### Consistency checks`: Describe the system-level checks used to confirm the surface aligns with adjacent work.
- `### Risk of over-polish`: Note where further polish would start to distort the chosen concept or consume disproportionate effort.
- `### Final readiness notes`: State what is now ship-ready and what still feels provisional.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, chrome_devtools`.
- If live implementation or repeatable regression evidence is available, use `chrome_devtools` and `playwright` as the strongest verification layer.
- If component-level baselines exist, add `storybook` checks before declaring the surface consistent.
- If both paths fail, produce the best-guess output described as: A polished design with corrected visual inconsistencies.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Use a concrete issue/fix list instead of a vague polish summary.
- Polish should sharpen the chosen direction, not sand it down into something generic.
- Use `project-ds-spec.md` as the system of record for polish decisions. The company reference library is only a sanity check against generic drift.
- Use `chrome_devtools` when real browser evidence is needed for the final consistency pass.
- Use `playwright` or `storybook` when you need the same check repeated after changes or across multiple states.
- Stop polishing when additional changes would require a concept change, token change, or component-system decision.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: visual-polish-and-consistency`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The design reads as deliberate and consistent, with concrete fixes, coverage notes, and readiness gaps called out.
