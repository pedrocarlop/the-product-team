---
name: frontend-verify
description: Applies structured UI verification — behavior checks, layout fidelity, visual regression, and basic accessibility — to confirm the implemented frontend matches design intent and quality expectations before handoff.
trigger: When frontend implementation is complete and requires validation before handoff to design review, QA, or release.
required_inputs:
  - the surface, flow, or component scope to be verified
  - the design source (Figma file, Storybook URL, or design spec) used as the fidelity reference
  - the target breakpoints and devices
  - the environment where the implementation is running (localhost, staging, preview URL)
recommended_passes:
  - UI model construction (component inventory, flows, states, breakpoints)
  - behavior and interaction verification
  - layout and responsive fidelity check
  - visual regression pass against baseline or design reference
  - basic accessibility scan
  - findings consolidation and residual risk summary
tool_stack:
  runtime:
    primary: [playwright, chrome_devtools]
    secondary: [cypress, storybook]
  visual_regression:
    primary: [chromatic]
    secondary: [percy, lost_pixel]
  accessibility:
    primary: [axe_core]
  design_reference:
    primary: [figma]
  fallback:
    primary: [repository, search_query]
tool_routing:
  - if: components are isolated in Storybook and the team uses component-driven development
    use: [chromatic, storybook] for visual regression and interaction testing against story baselines
  - if: full page or multi-step user flows must be verified end to end
    use: [playwright] for scripted interaction and screenshot comparison
  - if: Chromatic is unavailable or not set up
    use: [percy] for cross-browser visual regression across Playwright, Cypress, or Storybook
  - if: a self-hosted or open-source visual regression alternative is needed
    use: [lost_pixel] with GitHub Actions integration
  - if: accessibility compliance against WCAG 2.1 AA is required
    use: [axe_core] integrated into Playwright or Cypress test run
  - if: layout, spacing, computed styles, or network behavior need live inspection
    use: [chrome_devtools] directly against the running implementation
  - if: design fidelity comparison against specs is needed
    use: [figma] as the reference source for dimensions, tokens, and states
  - if: no live environment is accessible
    use: [repository] for code review and static inference; label output as fallback
  - avoid: relying on a single tool; combine runtime interaction testing (Playwright) with visual regression (Chromatic or Percy) and accessibility scanning (axe-core) for thorough coverage
best_guess_output: A frontend verification result with a UI model, structured behavior and layout findings, visual regression status, accessibility scan summary, and explicit residual risk.
output_artifacts: knowledge/frontend-engineer-frontend-verify.md
done_when: All in-scope surfaces have been verified against behavior, layout, and basic quality expectations; all findings are documented with evidence and repro steps; and residual risks are explicitly named.
---

# Frontend Verify

## Purpose

This skill applies structured UI verification to confirm the implemented frontend meets behavior, layout, visual fidelity, and basic accessibility expectations before handoff.

Reasoning type: comparative and evaluative — checking what was built against what was designed, specified, or expected; classifying deviations; assessing their impact.

Methods anchored to: design-spec comparison, state-based component inspection, visual regression diffing, WCAG 2.1 AA automated scanning (via axe-core), and responsive layout verification across defined breakpoints.

This skill does NOT conduct usability testing, write new implementation code, produce design specifications, or make product decisions. It verifies existing implementation against known references and documents findings for the team to act on.

---

## Required Inputs and Assumptions

**Required:**
- The surface, flow, or component scope to be verified (e.g., "checkout flow — desktop and mobile", "Button and Input components in Storybook", "onboarding screens at 375px and 1280px")
- The design source used as the fidelity reference: a Figma file URL, Storybook URL, or written spec
- Target breakpoints and devices to cover
- The environment URL where the implementation is running (localhost, staging, or preview)

**Known vs unknown at verification time:**
- Known: what was implemented (code exists); what design was specified (Figma or spec)
- Often unknown: whether edge-case states (empty, error, loading, disabled) were designed and implemented; whether all responsive breakpoints are in scope

**Assumption rule:** If scope is not explicitly stated, infer it from the most recently shipped or changed component surface and label the scope as `Assumed context:`. Lower the confidence of findings that depend on inferred scope. If the design reference is missing, proceed with implementation-only checks and label the reference path as `inferred`.

---

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live / real interaction** — Agent or tester interacts directly with the running implementation in a browser. Highest fidelity for behavior, scroll, hover, focus, and animation. Requires a working environment URL.
2. **Structured system access** — Playwright or Cypress test suite runs against the live environment; Chromatic or Percy runs visual regression against a Storybook baseline or deployment. Provides reproducible, automated evidence.
3. **Design artifacts / documentation** — Figma file, Storybook stories, or written spec. Used as the comparison reference for fidelity checks. Limitations: may be out of date; does not capture implemented behavior.
4. **Screenshots / static input** — Manual screenshots or screen recordings shared by the team. Useful for asynchronous review; limited to visible states, no interaction context.
5. **Inference** — Code review alone when no live environment is accessible. Lowest fidelity. Label all output as `inferred`.

Declare which path was used in the `### Verification scope` section of the deliverable. Prefer path 2 (automated structured access) as the default when tools are configured. Combine paths 2 and 3 (automated testing + Figma reference) for the most reliable coverage.

---

## Tool Stack

**Runtime primary — Playwright**
Cross-browser automation framework using the Chrome DevTools Protocol. Supports Chromium, Firefox, and WebKit in a single API. Best for scripted multi-step interaction verification, network interception, responsive viewport testing, and screenshot-based visual comparison (`toHaveScreenshot()`). Runs 35–45% faster than Cypress in parallel CI mode. Native support for accessibility testing via `@axe-core/playwright`. Use for full-page and flow-level verification.

**Runtime secondary — Cypress**
Browser-automation framework with an exceptional in-browser debugging experience: time-travel, real-time reload, and a rich visual UI. Best for teams prioritizing developer experience over cross-browser coverage (Chromium + Firefox; no Safari/WebKit). Use when Playwright is not available or when the existing test suite is Cypress-based.

**Runtime secondary — Storybook**
Component development and isolated testing environment. Interaction tests via the `play` function simulate user behavior (click, type, submit) and assert on DOM state within isolated component stories. Component tests use Vitest integration. Use to verify component-level behavior, states, and slot/prop variations without mounting the full application.

**Visual regression primary — Chromatic**
Cloud-based visual regression and UI review platform built by the Storybook team. Captures pixel-level snapshots of every Storybook story across browsers, viewports, and themes. Runs with unlimited parallelization. Provides a collaborative approval workflow where engineers and designers review visual diffs in a shared dashboard. Best choice when the component library lives in Storybook.

**Visual regression secondary — Percy (BrowserStack)**
Full-page and component-level visual regression testing across Playwright, Cypress, Selenium, and Storybook. AI-powered Visual Review Agent (launched late 2025) reduces review time by 3x and auto-filters ~40% of visual noise. Permanent free tier (5,000 screenshots/month). Use when Chromatic is unavailable or when verifying full pages and user flow states — not just isolated components.

**Visual regression alternative — Lost Pixel**
Open-source visual regression testing tool (free core; managed tier from $100/month). Self-hostable with first-class GitHub Actions integration. Supports Storybook, Next.js, and Playwright compositions. Provides element masking, retry logic, and per-screenshot thresholds. Use when a self-hosted, zero-vendor-lock alternative to Chromatic or Percy is required.

**Accessibility — axe-core (Deque)**
Open-source accessibility engine. Detects on average 57% of WCAG 2.0/2.1/2.2 A, AA, and AAA issues automatically. Integrates directly into Playwright (`@axe-core/playwright`) and Cypress tests. Returns violations, incomplete items requiring manual review, and passing rules. Runs in CI on every build. Use for automated WCAG 2.1 AA compliance scanning.

**Design reference — Figma**
Primary source for design fidelity comparison: dimensions, spacing, color tokens, typography, component states, and interaction annotations. Use to compare the implementation against intended design intent at each breakpoint. Use the Inspect panel for exact values.

**Live inspection — Chrome DevTools**
In-browser inspector for computed styles, layout box models, network requests, console errors, and accessibility tree. Use to investigate specific deviations found during visual or behavior checks. Not a primary testing tool — a diagnostic instrument.

**Fallback — repository + search_query**
Code review of component source files when no live environment is available. Static inference only. Label all output as `fallback`.

---

## Tool Routing

- Storybook component library exists and Chromatic is configured → run Chromatic visual regression against the story set; review diffs in the Chromatic dashboard before approving.
- Full-page or multi-step flow verification required → use Playwright with `toHaveScreenshot()` for visual and behavioral checks across browsers and viewports.
- Cypress is the existing test framework → use Cypress for behavior checks; add Percy for visual regression if Chromatic is not configured.
- Self-hosted or open-source visual regression is required → use Lost Pixel with GitHub Actions.
- WCAG accessibility compliance is in scope → add `@axe-core/playwright` to the Playwright test suite; run before every handoff.
- Design fidelity comparison is needed → open the Figma source file; use the Inspect panel to extract reference values; compare against live computed styles in Chrome DevTools.
- No live environment is available → proceed with code review via repository; label all findings as `fallback`; raise environment setup as a blocker.
- Never rely on visual inspection alone. Combine automated regression (Chromatic or Percy) with behavior testing (Playwright or Cypress) and accessibility scanning (axe-core) for a defensible handoff.

---

## Environment and Reproducibility

Record the following in the deliverable when known:

- **Environment URL**: localhost port, staging URL, or Vercel preview URL
- **Build / commit reference**: the exact commit SHA or build ID being verified
- **Browsers tested**: Chromium, Firefox, WebKit — note which were covered and which were skipped
- **Viewport breakpoints tested**: exact pixel widths (e.g., 375px mobile, 768px tablet, 1280px desktop)
- **Auth state**: signed-in vs. signed-out; note which user role or persona was used
- **Data state**: seed data, empty state, populated state — specify which states were verified
- **Tool versions**: Playwright version, axe-core version, Chromatic build ID, Storybook version
- **Design reference version**: Figma file name + last-updated date or version

If any of the above is unknown, state it explicitly. Do not present findings from a single browser or viewport as universal. Do not treat a partially rendered or mock-data environment as representative of production behavior.

---

## Model Building

The agent must construct a UI model before running any checks. No findings may be written before the model is complete.

### UI model components

**1. Surface inventory**
List every surface, component, or flow in scope:
```
| ID   | Surface / Component        | Type         | Status     |
|------|----------------------------|--------------|------------|
| S01  | Login form                 | Page flow    | In scope   |
| S02  | Button component variants  | Component    | In scope   |
| S03  | Dashboard (empty state)    | Page state   | In scope   |
| S04  | Email notification layout  | Out of scope | Skipped    |
```

**2. State map**
For each surface, enumerate the states that must be verified:
- Default / loaded
- Loading / skeleton
- Empty state
- Error state
- Disabled / read-only
- Hover / focus / active (interaction states)
- Responsive variants per breakpoint

**3. Design reference map**
For each surface, confirm what design reference exists and note its status:
```
| Surface ID | Design Reference            | Status           |
|------------|-----------------------------|------------------|
| S01        | Figma: Login frame v3       | Confirmed        |
| S02        | Storybook stories           | Confirmed        |
| S03        | Figma: Dashboard empty v1   | Outdated — noted |
```

**4. Tool coverage map**
Note which tool will be used to verify each surface. If a surface cannot be tested with the available tool set, mark it as `manual-only` or `not-verified`.

No behavior checks, layout checks, or findings may be written before this model is complete and documented in `### Verification scope`.

---

## Core Method Execution

Follow this sequence. Each step must be completed before moving to the next.

**Step 1 — Confirm scope and environment**
Confirm the surface inventory, design reference availability, environment URL, and target breakpoints. If any element of scope is ambiguous, write a provisional interpretation labeled `Assumed context:` and proceed.

**Step 2 — Build the UI model**
Construct the surface inventory, state map, design reference map, and tool coverage map as defined in Model Building. Document in `### Verification scope`.

**Step 3 — Run behavior and interaction checks**
For each in-scope surface:
- Verify that primary user interactions work as intended (click, submit, navigate, focus, keyboard navigation).
- Verify state transitions: does loading resolve correctly? Do error states display when expected? Does empty state render correctly?
- Check that form validation messages appear and clear as expected.
- Verify that interactive components (modals, dropdowns, accordions, tabs) open, close, and manage focus correctly.
- Use Playwright or Cypress for scripted interaction; use Storybook play function for isolated component interaction.
- Record each check as Pass, Fail, or Not verified.

**Step 4 — Run layout and responsive checks**
For each in-scope surface at each target breakpoint:
- Compare the rendered layout against the Figma reference using Chrome DevTools (computed values) and visual inspection.
- Check spacing, alignment, typography size and weight, color tokens, and component dimensions against the design spec.
- Verify that responsive breakpoints trigger as expected: no content overflow, no collapsing text, no misaligned elements.
- Check touch target sizes on mobile viewports (minimum 44×44px per WCAG 2.5.5).
- Record observed values vs. specified values where deviations exist.

**Step 5 — Run visual regression pass**
- If Chromatic is configured: trigger a Storybook build and review the visual diff report in the Chromatic dashboard. Accept or reject changed snapshots.
- If Percy is used: run the Percy agent against the Playwright or Cypress suite; review the diff report in the Percy UI.
- If Lost Pixel is used: run the Lost Pixel action in CI; review diffs in the GitHub pull request check.
- If no visual regression tool is configured: take manual screenshots at each breakpoint and compare against the Figma reference visually. Label findings as `fallback`.
- For each visual diff: classify as intentional change, regression, or noise.

**Step 6 — Run accessibility scan**
- Integrate `@axe-core/playwright` into the Playwright test suite (or `cypress-axe` for Cypress).
- Run the axe scan against each in-scope page at its default loaded state.
- Collect violations by WCAG rule ID, impact level (critical, serious, moderate, minor), and element selector.
- Note incomplete items that require manual review (axe-core's "incomplete" category).
- Do not treat a zero-violation axe scan as a complete accessibility clearance — axe automates ~57% of WCAG checks; the remainder requires manual review.

**Step 7 — Consolidate findings**
- Apply the finding schema to every issue surfaced in steps 3–6.
- Merge duplicate issues (e.g., the same spacing token violation appearing on three components → one finding with three affected locations).
- Classify by priority using the prioritization logic below.
- Document residual risk for anything that could not be fully verified.

**Step 8 — Produce deliverable**
Write the structured sections below into the deliverable file.

---

## Structured Findings

Every finding must use this exact schema. No free-form findings. Separate observation from interpretation. Every finding must be traceable to a specific surface, state, and tool.

```
#### Finding <id>
Observation:   [What was seen — factual, no interpretation; include element, state, and viewport]
Evidence:      [Tool or method used + screenshot reference, diff ID, or axe rule ID]
Repro steps:   [Exact steps to reproduce — URL, auth state, viewport, interaction sequence]
Cause:         [Why this likely occurred — labeled as inferred if not confirmed from code]
Impact:        [Effect on user experience or design fidelity; link to WCAG rule if applicable]
Confidence:    [High / Medium / Low + rationale]
```

Confidence guide:
- **High** — Reproduced across multiple browsers or viewports; confirmed by automated tool output (axe violation, Chromatic diff, Playwright screenshot); deviation from Figma spec is clearly measurable.
- **Medium** — Reproduced in one browser or viewport; tool output is present but single-tool; design reference may be ambiguous.
- **Low** — Observed in manual inspection only; environment may not be representative; design reference is missing or outdated; inferred from code review with no live verification.

---

## Prioritization Logic

Prioritize findings by user impact and handoff risk:

1. **Critical** — Interactions that are broken or non-functional; WCAG critical or serious violations that block users with disabilities; layout failures that make content unreadable or unusable on any in-scope viewport.
2. **Significant** — Visible layout or fidelity deviations that are clearly inconsistent with the design intent; interaction states (error, empty, loading) that are missing or incorrect; accessibility issues at WCAG moderate level.
3. **Minor** — Small spacing or color deviations within tolerance; cosmetic inconsistencies that do not affect usability; WCAG minor violations or incomplete items that require manual review.

Rules:
- Always list critical findings individually, even if there is only one.
- Group minor findings of the same type (e.g., "three components have 4px spacing deviation at mobile") into a single grouped finding rather than separate line items.
- Do not include more than ten standalone findings. Surface-level observations that do not affect usability or fidelity belong in the coverage map, not in findings.

---

## Pattern Detection

After individual findings are documented, the agent must identify systemic patterns:

- **Recurring issues**: the same type of deviation appearing across 3+ components or surfaces — this signals a system-level problem (e.g., a design token not applied globally, a breakpoint handler missing in the shared layout component).
- **Missing state classes**: a category of states (e.g., all error states, all empty states) that are consistently absent or incorrectly implemented — indicates a gap in implementation scope, not a one-off bug.
- **Token drift**: computed CSS values that diverge from the design token system across multiple components — may indicate hardcoded values bypassing the token layer.
- **Accessibility patterns**: the same WCAG rule failing across multiple components (e.g., `color-contrast` on all secondary buttons) — indicates a systematic design or implementation issue, not isolated bugs.
- **Breakpoint regression clusters**: multiple unrelated components that break at the same viewport width — may indicate a global media query or grid configuration issue.

Distinguish one-off bugs from system-level patterns. System-level patterns must be called out explicitly in the findings summary and linked to a root cause hypothesis.

---

## Recommendations

Each recommendation must:
- Link to a specific finding by ID or a named pattern
- Be directional — state what should be addressed, not how to implement it
- Acknowledge evidence limits where confidence is Medium or Low
- Distinguish between: fix before handoff (blocks release), fix before release (should not ship), and low priority (document for backlog)

Format: `Rec <id> [links to Finding <id> or Pattern <name>]: <directional recommendation>. Priority: <Blocks handoff / Should fix before release / Low priority>.`

---

## Coverage Map

State explicitly for the deliverable:

- **Fully verified**: surfaces, states, and breakpoints verified with automated tools and design reference comparison.
- **Partially verified**: surfaces where some states, breakpoints, or tool passes were skipped; state the reason.
- **Not verified**: surfaces excluded from this pass; flows that could not be accessed; states that do not exist in the current environment.

The coverage map sets expectations for what the design reviewer or QA team can rely on vs. what needs further validation downstream.

---

## Limits and Unknowns

Mandatory section. State:

- What environments were not accessible (e.g., production data, authenticated enterprise states)
- What browsers or viewports were not covered in this pass
- Where the design reference is outdated or ambiguous — list by surface ID
- What interaction states could not be reproduced in the available environment
- Where axe-core's automated scan covers only a portion of WCAG — state that a manual accessibility review is still needed
- Where visual regression baselines do not yet exist (first run) — note that diffs require human approval, not automated pass/fail
- Where findings were made from code review alone (inferred) rather than live testing

Do not collapse this section to a single line. Every named unknown sets the scope of what the handoff recipient must handle.

---

## Workflow Rules

1. Build the UI model (surface inventory, state map, design reference map) before executing any checks.
2. Distinguish fact (automated tool output, measurable computed value) from inference (visual judgment, code review without live testing). Label every inference.
3. Merge duplicate findings before writing the final finding list. One finding per distinct issue — not one per browser, viewport, or screenshot.
4. Do not hallucinate design intent. If the design reference is missing for a surface, lower confidence and state the reference gap explicitly.
5. Record the tool path used for each check so the evidence is reproducible: tool name, run ID or diff URL, screenshot file path, or axe report reference.
6. Do not treat a clean visual regression diff as confirmation that behavior is correct — visual testing and behavior testing address different failure modes.
7. Do not present findings from an unrepresentative environment (mock data, local-only feature flags) as production-representative. State environment limitations explicitly.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/frontend-engineer-frontend-verify.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

---

## Required Deliverable Sections

Within `## Skill: frontend-verify`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Verification scope`: UI model — surface inventory, state map, design reference map, tool coverage map, environment details, and declared evidence path.
- `### Behavior checks`: Each in-scope interaction and state, recorded as Pass / Fail / Not verified with evidence references.
- `### Layout and responsive checks`: Layout fidelity at each breakpoint — observed vs. specified values for deviations; token and spacing conformance.
- `### Visual regression`: Tool used, baseline status, number of diffs, classification of diffs (intentional / regression / noise), diff report URL or reference.
- `### Accessibility scan`: axe-core run results — violations by impact level, WCAG rule IDs, affected elements, and incomplete items requiring manual review.
- `### Findings`: All findings in the structured schema, grouped by priority (Critical → Significant → Minor grouped).
- `### Pattern detection`: System-level patterns identified across findings, with root cause hypotheses.
- `### Recommendations`: Directional recommendations linked to findings, with handoff priority.
- `### Coverage map`: What was fully, partially, and not verified.
- `### Residual risk`: What remains uncertain, unverified, or blocked — explicitly named and owned.

---

