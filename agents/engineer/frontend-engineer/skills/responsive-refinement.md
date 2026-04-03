---
name: responsive-refinement
description: Adapt and improve a surface so it works cleanly across breakpoints and devices by constructing a breakpoint matrix, auditing layout behavior per viewport, and producing a prioritized set of responsive fixes — grounded in real tool evidence.
trigger: When responsive behavior is missing, inconsistent, or under-specified across breakpoints or device classes.
required_inputs:
  - the surface or component set being refined
  - the intended breakpoint set or device targets
  - the current codebase or design artifacts for the surface
  - any known issues or regression areas
  - the deployment environment (web, PWA, hybrid app)
recommended_passes:
  - breakpoint matrix and layout system inventory
  - per-breakpoint audit using runtime simulation tools
  - cross-device verification on real or cloud devices
  - visual regression check against baseline
  - finding synthesis and prioritized fix list
tool_stack:
  runtime:
    primary: [polypane, chrome_devtools_device_mode]
    secondary: [responsively_app, lambdatest_lt_browser, browserstack_live]
  visual_regression:
    primary: [chromatic]
    secondary: [percy]
  artifacts:
    primary: [figma, repository]
  fallback:
    primary: [reference, search_query]
tool_routing:
  - if: multi-breakpoint simultaneous inspection is needed during development
    use: [polypane]
  - if: quick in-browser viewport simulation or media query visualization
    use: [chrome_devtools_device_mode]
  - if: free open-source multi-viewport preview is preferred or Polypane is unavailable
    use: [responsively_app]
  - if: real-device cloud testing across many OS/browser combinations is needed
    use: [browserstack_live]
  - if: parallel automated cross-device test execution at scale is needed
    use: [lambdatest_lt_browser]
  - if: per-component visual regression across viewport widths is needed in a Storybook setup
    use: [chromatic]
  - if: cross-browser visual regression snapshots are needed outside Storybook
    use: [percy]
  - if: design intent for breakpoints must be verified
    use: [figma]
  - if: primary tools are unavailable, blocked, or out of credits
    use: [reference, search_query]
best_guess_output: A breakpoint matrix, per-breakpoint audit findings, and a prioritized responsive fix list with reproduction steps, cause analysis, and a verification plan.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer-responsive-refinement.md
done_when: Every breakpoint in the defined set has been audited, all Critical and Significant findings have a documented fix or accepted risk, and desktop and mobile behavior are both intentional and verifiable.
---

# Responsive Refinement

## Purpose

Adapt and improve a surface so it renders and behaves correctly across a defined set of breakpoints and device classes.

This skill applies structured layout auditing — breakpoint matrix construction, per-viewport inspection, cross-device verification, and visual regression — to produce a prioritized, evidence-based set of responsive fixes.

This skill does not redesign surfaces from scratch, make layout decisions without evidence of the intended design, or produce untraceable fixes. It does not substitute for accessibility auditing (WCAG compliance is a separate skill), though it flags obvious accessibility regressions triggered by responsive failures.

---

## Required Inputs and Assumptions

Required inputs:
- The surface or component set being refined (route, page, feature area, or component name)
- The intended breakpoint set or device targets (e.g., 320px, 375px, 768px, 1024px, 1280px, 1440px)
- The current codebase or design artifacts for the surface (repository access, Figma file, or screenshots)
- Any known issues or regression areas flagged by QA, design review, or stakeholders
- The deployment environment (web, PWA, hybrid app — affects touch behavior and safe area handling)

If inputs are missing, infer provisional values and prefix each with `Assumed context:`. Lower the confidence of any finding that depends on an inferred input.

Known vs unknown: The intended breakpoint set is sometimes specified in the design system but often implicit in the CSS. The target device range may be known at the product level but not documented per surface. Both must be resolved before the breakpoint matrix is built.

---

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live / real interaction** — Direct inspection of the running application using Polypane, Chrome DevTools, or Responsively App. Highest fidelity; requires local dev server or staging URL.
2. **Structured system access** — Cloud device testing via BrowserStack Live or LambdaTest LT Browser. Real device rendering; best for cross-OS, cross-browser, and touch behavior verification.
3. **Design artifacts or documentation** — Figma files, design tokens, or design system breakpoint documentation. Useful for verifying design intent; may not reflect shipped state.
4. **Screenshots / static input** — Stakeholder-provided screenshots or QA attachments. Limited to visible states; no interaction context.
5. **Inference** — Deriving expected behavior from code patterns, CSS media queries, or framework conventions. Last resort; must be labeled explicitly.

Declare which path was used and state its limitations in the deliverable. Prefer path 1 as the default. Combine paths 1 and 2 when real-device verification is required for the highest-risk breakpoints.

---

## Tool Stack

**Runtime — primary:**

**Polypane** (Chromium-based developer browser): Shows multiple synchronized viewport panes simultaneously. Every scroll, click, hover, and form input is mirrored across all panes. Supports CSS breakpoint emulation, device emulation, dark/light/reduced-motion mode per pane, media query overlays, accessibility overlays, and full-page screenshots. Best for development-time auditing where you need all breakpoints visible at once. Requires a paid license; available on macOS, Windows, Linux.

**Chrome DevTools Device Mode**: Built into Chrome. Provides viewport resizing, device preset emulation, media query bar visualization (color-coded by type: orange = min-width, blue = max-width, green = range), network throttling, CPU throttling, and custom device configuration. Best for quick in-browser inspection of specific breakpoints, debugging CSS media queries, and validating responsive CSS behavior without a separate tool.

**Runtime — secondary:**

**Responsively App**: Open-source, free multi-viewport browser. Previews multiple device widths simultaneously with synchronized scrolling and click mirroring. Lightweight and fast to set up. Best as a Polypane fallback or for teams that cannot use paid tooling. Available on macOS, Windows, Linux.

**LambdaTest LT Browser**: Dedicated responsive testing browser with 50+ pre-installed device viewport presets. Supports parallel testing, screenshot capture, session recording, and CI/CD integration via LambdaTest's cloud platform. Best for scaled cross-device test runs and regression checks in a CI pipeline.

**BrowserStack Live**: Cloud-based real-device testing across 3,500+ device/browser/OS combinations. Supports interactive live sessions, automated screenshots at multiple resolutions, video recording, and localization testing. Best for high-confidence real-device verification on iOS Safari, Android Chrome, and legacy browser versions that cannot be emulated locally.

**Visual regression:**

**Chromatic**: UI testing platform built around Storybook. Automatically captures pixel-level screenshots of every story at specified viewport widths and diffs them against the baseline. Integrates with CI/CD to catch responsive regressions before merge. Best for component libraries where stories already exist. Supports Chrome, Firefox, Safari, and Edge in parallel.

**Percy** (BrowserStack Percy): Visual review platform that captures responsive snapshots at configurable widths (configured via `.percy.yml`). Supports cross-browser snapshots. AI-powered Visual Review Agent (2025) draws bounding boxes around meaningful visual changes and filters out rendering noise. Best for full-page visual regression when Storybook is not in use.

**Artifacts:**

**Figma**: Verifying intended layout behavior per breakpoint when design files include responsive frames. Use to compare live rendering against design intent — not to drive fixes in isolation.

**Repository**: Reading CSS media queries, Tailwind responsive utilities, or component breakpoint logic to understand the layout system before auditing.

**Fallback:**

**Reference / search query**: Manual documentation lookup or web search when primary tools are unavailable. Label all fallback-sourced findings explicitly.

---

## Tool Routing

- Multi-breakpoint simultaneous inspection during development → start with Polypane.
- Quick in-browser viewport simulation or media query debugging → use Chrome DevTools Device Mode.
- Polypane unavailable or team prefers free tooling → use Responsively App.
- Real-device verification on iOS Safari, Android Chrome, or legacy browsers → use BrowserStack Live.
- Scaled automated cross-device test runs in CI → use LambdaTest LT Browser.
- Per-component visual regression in a Storybook project → use Chromatic.
- Full-page visual regression outside Storybook → use Percy.
- Design intent for any breakpoint is ambiguous → consult Figma before writing findings.
- All primary tools unavailable → use reference / search query; label output as `fallback`.
- Avoid relying on a single tool. Combining Polypane (development-time multi-viewport audit) with BrowserStack Live (real-device verification) and Chromatic (regression protection) produces stronger evidence than any one tool alone.

---

## Environment and Reproducibility

Record the following in the deliverable when known:

- URL or local dev server path used during the audit session
- Date of the audit session (responsive behavior can change between deploys)
- Tool versions: Polypane version, Chrome DevTools version, BrowserStack session ID
- Build or commit hash being tested
- Authentication state (signed-in vs. signed-out surfaces may reflow differently due to conditional content)
- Operating system and host browser (affects emulation accuracy for Polypane and DevTools)
- Whether real devices or emulators were used for each breakpoint finding
- Any feature flags or data states that affect layout (e.g., empty state vs. populated list)

If any of the above is unknown, state it explicitly. Do not present emulator behavior as equivalent to real-device behavior without noting the distinction.

---

## Model Building

Before auditing any breakpoint, the agent MUST construct a breakpoint matrix and layout system inventory.

**Step 1 — Define the breakpoint set.** Extract the canonical breakpoint definitions from: (a) the design system token file or CSS custom properties, (b) Tailwind config or equivalent framework config, (c) CSS media queries in the component files, (d) Figma design frames if code is unavailable. If breakpoints differ between sources, document the discrepancy before proceeding.

**Step 2 — Define the device target matrix.** Map each breakpoint to its representative device class:

| Breakpoint | Width | Device class | Primary OS/browser to verify |
|---|---|---|---|
| xs | 320px | Small mobile | Android Chrome, iPhone SE Safari |
| sm | 375px | Standard mobile | iPhone 14/15 Safari |
| md | 768px | Tablet portrait | iPad Safari, Android tablet |
| lg | 1024px | Tablet landscape / small laptop | Chrome, Safari |
| xl | 1280px | Desktop standard | Chrome, Firefox, Safari, Edge |
| 2xl | 1440px+ | Wide desktop | Chrome, Firefox |

Adjust this table to match the actual project breakpoints. Add custom rows for any non-standard breakpoints in the codebase.

**Step 3 — Inventory the layout system.** For the surface being audited, identify: (a) the CSS layout mechanism in use (CSS Grid, Flexbox, multi-column, or mixed), (b) how spacing, font sizes, and container widths are controlled at each breakpoint, (c) which components have explicit responsive variants vs. relying on implicit reflow, (d) any fixed-width or fixed-height elements that may not reflow.

**Step 4 — Map known issues before analysis begins.** Document any issues already reported by QA, design review, or stakeholders. These become the seed list for the audit; do not treat them as findings until reproduced and confirmed.

No per-breakpoint audit or findings may be written before the breakpoint matrix and layout system inventory are complete.

---

## Core Method Execution

Follow this sequence:

**Step 1 — Clarify the scope.** Confirm the surface, breakpoint set, and device targets. If the scope is vague, define a provisional scope, label it `Assumed context:`, and proceed.

**Step 2 — Build the breakpoint matrix and layout system inventory.** Per the Model Building section. Document in `### Breakpoint matrix` before proceeding.

**Step 3 — Per-breakpoint audit.** For each breakpoint in the matrix, inspect the following dimensions using Polypane or Chrome DevTools Device Mode:

- **Layout integrity**: Does the grid or flex layout reflow correctly? Are there overflow issues, horizontal scroll, or content clipping?
- **Typography**: Do font sizes, line heights, and text truncation behave correctly? Is any text too small to read on the target device?
- **Spacing and density**: Are padding, margin, and gap values appropriate for the viewport? Does density feel correct for touch vs. pointer input?
- **Images and media**: Do images scale correctly? Are aspect ratios preserved? Are `srcset` or picture element breakpoints firing correctly?
- **Interactive elements**: Are tap targets adequately sized (minimum 44×44px per Apple HIG / 48dp per Material)? Do hover states degrade gracefully on touch?
- **Navigation**: Does the navigation pattern (hamburger, tabs, sidebar) switch correctly at the right breakpoint? Are transitions smooth?
- **Component states**: Do empty states, loading states, and error states reflow correctly at each breakpoint?
- **Z-index and stacking**: Do overlays, modals, tooltips, and sticky elements behave correctly at each viewport width?

**Step 4 — Real-device verification.** For findings that involve touch behavior, iOS Safari-specific rendering, or any breakpoint where emulation fidelity is uncertain, verify on a real device via BrowserStack Live. Prioritize: smallest mobile breakpoint (320–375px), tablet (768px), and any breakpoint where a known OS/browser quirk is suspected.

**Step 5 — Visual regression check.** If Chromatic or Percy is available, run a snapshot pass against the current breakpoints and compare to baseline. Record any diffs that represent unintentional changes.

**Step 6 — Compare against design intent.** For any finding where the correct behavior is ambiguous, open the Figma file and verify the intended layout at that breakpoint. Label evidence as `design-sourced` or `inferred` accordingly.

**Step 7 — Synthesize and structure findings.** Apply the finding schema below. One finding per distinct issue — not one per screenshot. Merge duplicate observations across breakpoints into a single finding with a breakpoint range noted.

**Step 8 — Prioritize and group.** Apply the prioritization logic. Draft fixes for Critical and Significant findings.

---

## Structured Findings

Every finding must use this exact schema. No free-form output. Separate observation from interpretation. Every finding must be traceable to a source.

```
#### Finding <id>
Observation: [What was seen, without interpretation — describe the visual or behavioral state]
Evidence: [Tool used + breakpoint width + screenshot reference or session ID]
Repro steps: [Exact steps to reproduce: viewport width, device/emulator, interaction if applicable]
Cause: [Why this issue likely exists — labeled as inferred if not confirmed from code]
Impact: [Effect on usability, visual integrity, or user task completion at this breakpoint]
Confidence: [High / Medium / Low + rationale]
```

Confidence guide:
- **High** — Observed on real device via BrowserStack or on physical hardware, or reproduced on 3+ emulated breakpoints with consistent behavior.
- **Medium** — Observed in Polypane or Chrome DevTools emulation; not yet verified on real device.
- **Low** — Inferred from code analysis or a single screenshot; not yet reproduced interactively.

---

## Prioritization Logic

Prioritize findings by user impact and prevalence:

1. **Critical** — Layout breaks that make content unreadable, inaccessible, or that cause horizontal scroll on mobile. Navigation failures. Content clipping that hides essential UI. Affects the primary user task at a major breakpoint.
2. **Significant** — Spacing, sizing, or typography issues that degrade the experience but do not block task completion. Missing responsive variants for important components. Real-device–specific rendering bugs.
3. **Minor** — Polish issues: minor spacing inconsistencies, suboptimal density, visual roughness that does not affect usability. Group these into a `### Minor issues` block — do not list as standalone findings.

Do not include more than ten standalone findings. Surface-level observations that do not connect to a specific breakpoint or user impact belong in the coverage map, not in findings.

---

## Pattern Detection

After the per-breakpoint audit is complete, the agent must identify:

- **Recurring layout failures**: The same overflow, clipping, or reflow issue appearing at multiple breakpoints — signals a layout system problem rather than a one-off fix.
- **System-level causes**: Where issues share a root cause (e.g., a container component that does not constrain its children, a shared utility class with a fixed width), indicating a fix at the system level rather than per-component patching.
- **Breakpoint gaps**: Where the layout has no defined behavior between two defined breakpoints, causing a "dead zone" where the design neither works as mobile nor desktop.
- **Touch target failures**: Systematic under-sizing of interactive elements at mobile breakpoints — a pattern that requires a design-system-level fix, not individual component patches.
- **OS/browser-specific divergence**: Where a finding reproduces only on a specific platform (e.g., iOS Safari flex behavior, Android Chrome font scaling), indicating a targeted fix is needed rather than a broad layout change.

Distinguish one-off component bugs from system-level layout architecture issues. System-level patterns must be called out explicitly — they require a different fix strategy.

---

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- Be directional, not prescriptive — state what to fix or investigate, not the exact implementation
- Acknowledge evidence limits where confidence is Medium or Low
- Distinguish component-level fixes (scoped to one component) from layout-system-level fixes (affects many components)
- Note regression risk when a fix may affect other breakpoints or surfaces

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>. Risk: <regression risk if applicable>.`

---

## Coverage Map

State explicitly:

- **Deeply analyzed**: Breakpoints and surfaces audited with Polypane or real-device sessions, with full finding documentation.
- **Partially analyzed**: Breakpoints or surfaces inspected quickly or via screenshots only; evidence is incomplete.
- **Not analyzed**: Breakpoints excluded from this pass (e.g., very large screens, print media queries), surfaces not in scope, states that could not be triggered (e.g., authenticated-only surfaces when no credentials were available).

The coverage map sets expectations for what is safe to ship based on this pass vs. what requires further validation.

---

## Limits and Unknowns

Mandatory section. State:

- Which breakpoints were only emulated and not verified on real hardware
- Which OS/browser combinations were not tested (e.g., iOS Safari, Samsung Internet, Firefox on Android)
- Whether the audit covered all component states (empty, loading, error, populated) or only the happy path
- Where the intended design behavior at a breakpoint was inferred from code rather than confirmed from design artifacts
- Whether visual regression baselines were available or whether this pass established the baseline
- What real-device testing would increase confidence in Critical and Significant findings
- Any known environment factors that may affect reproducibility (e.g., feature flags, test data, authentication state)

Do not collapse this section to a single line. Specific unknowns must be named.

---

## Workflow Rules

- Build the breakpoint matrix and layout system inventory before writing any findings.
- Distinguish fact (directly observed in tool session) from inference (reasoned from code or design). Label every inference.
- Merge duplicate observations across breakpoints into a single finding with the affected breakpoint range noted.
- Do not write a finding for something that cannot be reproduced or traced to a specific cause.
- Do not hallucinate device behavior. If a real-device session was not run, label findings as `emulated` and note the confidence reduction.
- Record the tool path used for each finding so the evidence is reproducible.
- Keep fixes scoped to the surface being refined. Do not refactor shared layout components without flagging the regression risk explicitly.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/frontend-engineer-responsive-refinement.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

---

## Required Deliverable Sections

Within `## Skill: responsive-refinement`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Breakpoint matrix`: The full breakpoint set, mapped to device classes and target OS/browser combinations. Note source of breakpoint definitions (CSS tokens, Tailwind config, design file, or inferred).
- `### Layout system inventory`: CSS layout mechanism, spacing and sizing approach, components with explicit responsive variants, and any fixed-dimension elements flagged for review.
- `### Audit environment`: Tool path used, build/commit hash, date, authentication state, and any known environment factors.
- `### Findings`: Structured findings using the required schema. Organized by breakpoint or by component, not by screenshot.
- `### Pattern analysis`: System-level patterns identified across findings — shared root causes, breakpoint gaps, touch target failures, OS/browser-specific divergence.
- `### Recommendations`: Directional recommendations linked to findings. Distinguish component-level from layout-system-level fixes.
- `### Coverage map`: What was deeply, partially, and not analyzed.
- `### Limits and unknowns`: All confidence gaps, untested environments, and outstanding validation needs.
- `### Verification plan`: Specific steps to confirm fixes work correctly across the breakpoint set, including any regression areas to watch.

---

