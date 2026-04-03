---
name: browser-debug
description: Reproduces and isolates a frontend issue by constructing a browser evidence model — combining runtime inspection, session replay, error telemetry, and source-level analysis — then producing a structured finding with root cause, repro steps, and a fix direction.
trigger: When UI behavior is wrong, unexpected, or unreproducible and browser-level evidence is required to localize the source of truth. Triggered by bug reports, QA findings, production errors, or a failing automated test.
required_inputs:
  - a description of the observed incorrect behavior (what happened vs. what was expected)
  - the URL or application route where the issue occurs
  - browser and OS context when known (browser version, OS, viewport)
  - authentication or user-state context when relevant (logged in, role, account tier)
  - reproduction frequency when known (always, intermittent, only in production)
recommended_passes:
  - Pass 1 — Evidence model: construct component/state/network model before any analysis
  - Pass 2 — Live runtime inspection: Chrome DevTools Console, Network, Elements, Performance panels
  - Pass 3 — Session replay or recording analysis: LogRocket, Sentry Replay, Highlight.io, or Replay.io
  - Pass 4 — Error telemetry: Sentry error details, stack trace, sourcemaps, breadcrumbs
  - Pass 5 — Source localization: match evidence to component, state boundary, or network dependency
tool_stack:
  runtime:
    primary: [chrome_devtools]
    secondary: [replay_io, jam]
  session_replay:
    primary: [logrocket, sentry_replay]
    secondary: [highlight_io]
  error_telemetry:
    primary: [sentry]
    secondary: [debugbear]
  artifacts:
    primary: [repository, reference_trace]
  fallback:
    primary: [search_query, reference_trace]
tool_routing:
  - if: live browser session is accessible
    use: [chrome_devtools] for console errors, network requests, DOM state, and performance timeline
  - if: issue is intermittent or hard to reproduce manually
    use: [replay_io] for time-travel debugging — step through execution to the exact failure point
  - if: bug was reported by a user or QA tester without a dev session
    use: [jam] to review auto-captured console logs, network errors, and screen recording
  - if: error telemetry and session replay are already instrumented in production
    use: [sentry] for stack trace, breadcrumbs, sourcemapped frames, and session replay context
  - if: sentry is unavailable and session replay exists elsewhere
    use: [logrocket] for DOM snapshot replay, console log timeline, and network waterfall
  - if: self-hosted or open-source monitoring is required
    use: [highlight_io] for session replay, error events, and distributed frontend-backend trace linking
  - if: performance regression or Core Web Vitals degradation is part of the issue
    use: [debugbear] for real-user monitoring data, LCP/CLS/INP breakdowns, and regression timeline
  - if: no live session and no telemetry are available
    use: [repository, reference_trace] — static code analysis against the reported behavior
  - if: all primary tools are unavailable or produce no signal
    use: [search_query, reference_trace] — inferred debugging; label output as `inferred`
best_guess_output: A structured debugging report with a browser evidence model, reproduction steps, root cause hypothesis, fix direction, and open unknowns — labeled as sourced, fallback, or inferred to match the evidence path used.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer-browser-debug.md
done_when: The issue is localized to a specific component, state boundary, network dependency, or JavaScript execution path, with reproduction steps verified and a concrete fix direction stated.
---

# Browser Debug

## Purpose

This skill reproduces and isolates a frontend issue using browser evidence — runtime inspection, session replay, error telemetry, and source-level analysis.

Reasoning type: abductive — reasoning from observable browser evidence to the most probable cause. The agent forms a model of the system, then eliminates candidate causes by testing against evidence until one remains.

Methods anchored to: Chrome DevTools debugging protocol, session replay analysis, error telemetry triage (Sentry breadcrumbs + sourcemaps), and component-state boundary tracing.

This skill does NOT fix the issue, rewrite components, or make architectural recommendations. It localizes the source of truth and defines the fix direction so implementation work can proceed with confidence.

---

## Required Inputs and Assumptions

**Required:**
- Observed behavior: what the UI does vs. what it should do
- Route or surface: the URL, route, or component where the issue occurs
- Frequency: always reproducible, intermittent, or only in production

**Conditionally required:**
- Browser and OS: version and platform context — without this, browser-specific bugs cannot be confirmed
- Auth and data state: user role, account tier, specific data fixture — without this, state-dependent bugs may not reproduce
- Build version or deploy: commit SHA or deploy ID — without this, production vs. local divergence cannot be assessed

**Known vs unknown:**
- Known at trigger time: the symptom, the surface, and often the environment
- Often unknown: exact trigger sequence, whether the issue is state-dependent, which layer (JS, CSS, network, server) owns the failure

**Assumption rule:** If browser or auth context is not provided, state an assumed environment at the top of the evidence model and label it `assumed`. Lower the confidence of any finding that depends on that assumption.

---

## Input Mode and Evidence Path

Declare the evidence path before beginning analysis. Options:

1. **Live / real interaction** — direct browser session with DevTools open. Highest fidelity. Capture console, network, and DOM state in real time. Can reproduce the sequence and test hypotheses interactively.
2. **Structured system access** — session replay tools (LogRocket, Sentry Replay, Highlight.io, Replay.io) or error telemetry (Sentry) with sourcemaps and breadcrumbs. Strong fidelity. Captures real user sessions including state sequences that are hard to reproduce manually.
3. **Design artifacts / documentation** — component specs, API contracts, state machine docs, or design files. Useful for understanding intended behavior and identifying divergence. Cannot confirm runtime behavior.
4. **Screenshots / static input** — screenshots, screen recordings, or console output shared by reporters. Limited to visible states. No interaction history, no network context, no console timeline beyond what is in the screenshot.
5. **Inference** — no live session, no telemetry, no recording. Analysis is from code reading and issue description only. Must be labeled `inferred` throughout. Every conclusion is a hypothesis, not a finding.

**Declare the path used in the `### Browser evidence` section of the deliverable.**

---

## Tool Stack

**Runtime primary — Chrome DevTools**
Built into Chrome and Chromium-based browsers. The baseline debugging environment. Key panels:
- **Console**: JavaScript errors, warnings, log output, unhandled promise rejections
- **Network**: request/response timeline, payload inspection, failed requests, CORS errors, timing waterfall
- **Elements**: live DOM inspection, computed CSS, layout shifts
- **Sources**: JavaScript breakpoints, call stack, scope inspection, sourcemap-mapped original source
- **Performance**: frame rate, long tasks, layout recalculations, paint events, JS execution timeline
- **Application**: localStorage, sessionStorage, cookies, service workers, cache

Use Chrome DevTools as the default starting point for any live debugging session. No setup required. Provides the most comprehensive real-time signal.

**Runtime secondary — Replay.io**
Time-travel debugger for the web. Records browser execution at the engine level — not just the DOM, but actual JavaScript execution. Allows stepping backward and forward through any point in a session to inspect variables, call stacks, and state at any moment. Integrates with Playwright and Cypress for debugging flaky automated tests. Includes an MCP integration that lets AI agents like Claude Code receive precise root cause analysis from a recording.

Use Replay.io when the bug is intermittent, async-driven, or race-condition-related and cannot be reliably reproduced step by step. Also use it to debug CI test failures where the test passed locally but fails in the pipeline.

**Runtime secondary — Jam (Jam.dev)**
Browser extension that auto-captures a bug report package on demand: screen recording, console logs, network errors, user action replay, browser metadata, and device info. Reporters (QA, product, support) click one button and Jam produces a shareable link with all developer context attached. Integrates with Jira, Linear, GitHub, and Slack. Includes MCP support so an AI agent can ingest the Jam recording directly.

Use Jam when the bug was reported by a non-engineer who cannot share a DevTools session. The auto-captured console and network data reduces the reproduce-first bottleneck that makes QA-reported bugs expensive to triage.

**Session replay primary — LogRocket**
SDK-instrumented session replay for production apps. Captures DOM snapshots and mutations, console log timeline, network request waterfall, JavaScript exceptions, Redux or Zustand state diffs, and user action sequence. Replay UI shows exactly what the user saw alongside the technical signal. Search sessions by user, URL, error type, or custom event.

Use LogRocket when the issue is a production regression affecting real users and you need to watch the exact session where it occurred. Strong for "it works on my machine" issues that only appear under real-user data or environment conditions.

**Session replay primary — Sentry (with Session Replay)**
Error tracking platform with sourcemap-mapped stack traces, breadcrumb timelines, release-level regression detection, and integrated session replay. Sentry captures: the exception, the breadcrumb trail leading to it (clicks, navigation, console, network), the sourcemapped stack frame pointing to the original file and line, and a replay of the user session around the error. React component annotations surface which component triggered the exception.

Use Sentry as the primary telemetry tool when it is already instrumented in the codebase. The combination of error event + breadcrumbs + sourcemap + replay provides the highest-context starting point for production bug triage.

**Session replay secondary — Highlight.io**
Open-source, full-stack monitoring platform. Session replay, error monitoring, distributed tracing, and log correlation in one tool. Self-hostable. Pairs frontend session replay with backend traces and logs, enabling trace-linking from a frontend error to the originating backend span. Acquired by LaunchDarkly in March 2025.

Use Highlight.io when the team needs self-hosted monitoring, when the frontend issue may have a backend root cause requiring correlated traces, or as an open-source alternative to LogRocket and Sentry.

**Error telemetry secondary — DebugBear**
Frontend performance and real-user monitoring tool. Tracks Core Web Vitals (LCP, CLS, INP, FCP, TTFB) for real users, provides synthetic lab testing on a schedule, and surfaces performance regressions at the build or deploy level. Integrates with CI to catch performance regressions before they ship.

Use DebugBear when the issue is a performance regression — slow page load, layout shift, delayed interactivity, or Core Web Vitals drop — rather than a functional bug. Provides real-user field data that Chrome DevTools lab profiling cannot show.

**Artifacts — repository, reference/trace**
Source code, component architecture, API contracts, state machine definitions. Used when live tools are unavailable or to confirm code-level hypotheses formed from runtime evidence.

Use repository analysis as a complement to runtime evidence, not a replacement. A stack trace from Sentry pointing to `UserCard.tsx:47` makes code inspection precise. Without runtime evidence, code analysis produces plausible hypotheses only.

**Fallback — search_query, reference/trace**
Web search and documentation lookup when no tool access exists. Produces inferred output only. Every finding must be labeled `inferred`.

---

## Tool Routing

- Live browser session available → start with Chrome DevTools. Open Console first; network next; DOM/Elements third.
- Bug is intermittent, async, or race-condition-related → use Replay.io for time-travel stepping; import to AI agent via MCP if available.
- Bug was reported by QA or non-engineer → check for a Jam link first. If absent, ask reporter to install the Jam extension and reproduce before analyzing.
- Error telemetry is instrumented in production → go to Sentry first. Read: error message, stack trace (sourcemapped), breadcrumbs, and session replay link if available.
- LogRocket is instrumented and issue is session-specific → use LogRocket to find the user session; inspect the network waterfall and console timeline for the moment of failure.
- Issue may have a backend origin or team uses self-hosted monitoring → use Highlight.io for frontend-backend trace correlation.
- Issue is a performance regression (slow, shifts, poor INP) → use DebugBear for real-user field data; use Chrome DevTools Performance panel for profiling.
- No live session and no telemetry → use repository + reference/trace for code analysis. Label all output as `inferred`.
- All tools fail → produce best-guess output from available description. Label the entire section as `inferred` and flag for verification before acting on the fix direction.
- Do not use a single tool when two tools provide complementary signal. Sentry (error event) + Replay.io (execution trace) is stronger than either alone.

---

## Environment and Reproducibility

Capture the following before analysis. If unknown, state explicitly.

- **Browser and version**: Chrome 124, Firefox 126, Safari 17.x, Edge — bugs are often browser-specific
- **Operating system**: macOS, Windows, iOS, Android — rendering and input behaviors differ
- **Viewport and device**: desktop vs. mobile breakpoint; high-DPI vs. standard — layout bugs are often viewport-specific
- **Authentication state**: signed in vs. signed out; user role; account tier — state-dependent bugs will not reproduce without matching auth context
- **Data state**: specific records, edge-case data, empty state — many UI bugs only appear with specific data shapes
- **Build or deploy version**: commit SHA, deploy ID, or version tag — production divergence from local is a common source of "cannot reproduce"
- **Network conditions**: throttled, offline, VPN, CDN edge node — latency-sensitive bugs require matching network context
- **Environment**: local dev, staging, production — environment config differences (API endpoints, feature flags, env vars) are frequent root causes

**Reproducibility rule:** A finding is not valid until the repro steps are confirmed to produce the observed behavior in a documented environment. If the environment is inferred, label the finding as `unverified` and note what environment confirmation is required.

---

## Model Building

The agent must construct a browser evidence model before drawing any conclusions. No hypotheses before the model is complete.

### Evidence model components

**1. Component and state model**
Identify the component or subsystem where the incorrect behavior is visible:
```
| Layer          | Element                        | Notes                              |
|----------------|--------------------------------|------------------------------------|
| Component      | e.g., PaymentForm              | React/Vue/Svelte component or DOM  |
| State          | e.g., formErrors, cart.items   | Local state, Redux store, URL param|
| API dependency | e.g., POST /api/checkout       | Network dependency for this surface|
| CSS surface    | e.g., .modal-overlay z-index   | Relevant if issue is visual        |
```
Map what should happen and what the system is doing instead. This is the baseline for localization.

**2. Failure mode classification**
Before reading evidence, classify the failure type. This determines where to look first:

| Failure type           | Look first in                     |
|------------------------|-----------------------------------|
| JavaScript exception   | Console + Sentry stack trace      |
| Silent wrong state     | Console logs + Redux/Zustand diff |
| Network failure        | Network panel + API response body |
| CSS / layout defect    | Elements panel + computed styles  |
| Performance regression | Performance panel + DebugBear RUM |
| Race condition         | Replay.io time-travel + async timeline |
| Auth / permission error| Network 401/403 + auth state      |
| Environment-only bug   | Build config, env vars, feature flags |

**3. Evidence inventory**
Before analysis, list all available evidence sources:
```
| Source              | Available | Notes                                   |
|---------------------|-----------|-----------------------------------------|
| Live browser session| Yes / No  |                                         |
| Sentry error event  | Yes / No  | Error ID if available                   |
| LogRocket session   | Yes / No  | Session URL if available                |
| Replay.io recording | Yes / No  | Recording link if available             |
| Jam report          | Yes / No  | Jam link if available                   |
| Highlight.io trace  | Yes / No  |                                         |
| Console output      | Yes / No  | Pasted or screenshotted                 |
| Network HAR file    | Yes / No  |                                         |
| Repository access   | Yes / No  |                                         |
```
Flag missing evidence before analysis. Do not draw conclusions from evidence that does not exist.

No hypotheses, no root cause statements, no fix directions until the evidence model is built.

---

## Core Method Execution

Follow this sequence. Do not skip steps. Do not produce findings before Step 4.

**Step 1 — Clarify and scope the issue**
State the observed behavior and expected behavior in concrete terms. If the description is vague ("it's broken"), resolve it to: what element, what action, what visual or functional outcome is wrong. If context is missing, label the gap as `assumed` and proceed with the assumption stated.

**Step 2 — Classify the failure mode**
Using the failure mode table in Model Building, classify which category this issue falls into. This determines the inspection sequence.

**Step 3 — Build the evidence model**
Complete the component/state model and evidence inventory. Confirm which tools are available. Declare the evidence path (levels 1–5 from Input Mode section).

**Step 4 — Primary evidence collection**
Based on failure mode classification and available tools:

*JavaScript exception path:*
- Open Chrome DevTools Console. Capture the full error message, error type, and call stack.
- If Sentry is instrumented: navigate to the error event. Read the sourcemapped stack trace, breadcrumb trail, and session replay link. Note the file, line, and component.
- If Replay.io is available: step to the throw point and inspect scope variables at the moment of failure.

*Network failure path:*
- Open Chrome DevTools Network panel. Filter to the failing request. Read: HTTP status, response body, request headers, timing waterfall.
- Check for CORS preflight failures (status 0 or OPTIONS 403).
- Check request payload for malformed data.
- Cross-reference with backend logs or API contract if available.

*Silent wrong state path:*
- Check console for warnings that do not throw: React prop type violations, missing keys, undefined dereferences.
- If LogRocket is instrumented: use the Redux/Zustand state diff panel to watch state transitions. Identify the transition that produces the wrong value.
- Add targeted console.log or debugger statement at the state mutation boundary if live session is available.

*CSS / layout defect path:*
- Open Elements panel. Inspect computed styles on the affected element. Check for: overriding rules, specificity conflicts, incorrect values.
- Check responsive breakpoints. Use Chrome DevTools device toolbar to confirm viewport-specific behavior.
- Check z-index stacking context for layering issues. Check box model (padding, margin, border) for layout bugs.

*Performance regression path:*
- Open Chrome DevTools Performance panel. Record a page load or interaction. Identify: long tasks (>50ms), layout recalculations, forced synchronous layouts, paint events.
- Cross-reference with DebugBear field data for LCP, CLS, and INP to confirm whether the regression is visible to real users, not just in lab conditions.

*Race condition / intermittent path:*
- Use Replay.io to record a session and step through async execution. Identify: competing async operations, missing await, event handler race, stale closure.
- Reproduce under throttled network (Chrome DevTools Network: Slow 3G) to surface timing-dependent branches.

**Step 5 — Reproduce and confirm**
State the exact steps to reproduce the observed behavior in the documented environment. Attempt reproduction. If confirmed: mark finding as `sourced`. If reproduction fails: revisit environment assumptions and try again before lowering confidence.

**Step 6 — Localize to a source of truth**
Name the specific file, component, function, state key, network endpoint, or CSS rule that owns the failure. This is the done-when condition. It must be specific enough for an engineer to open that file and begin a fix.

**Step 7 — State the fix direction**
Describe the likely correction path without prescribing the implementation. Example: "The cart total is computed before the discount coupon is applied; the computation should run after the coupon reducer resolves." Directional — not a code change.

**Step 8 — Document open unknowns**
List what could not be confirmed before a fix can safely land (e.g., whether the same failure occurs in Firefox, whether the issue is present in staging vs. production only).

---

## Structured Findings

Every finding must conform to this schema. No free-form narrative in the findings section.

```
Finding [ID]
Observation:     [What was seen in the browser — factual, no interpretation]
Evidence:        [Tool + specific signal: e.g., "Sentry event #abc123: Uncaught TypeError at UserCard.tsx:47"]
Repro steps:     [Exact steps to reproduce in the stated environment]
Environment:     [Browser, OS, auth state, data state, build version]
Cause:           [Root cause hypothesis — labeled as inferred if not confirmed via breakpoint or replay]
Impact:          [Who is affected, what breaks, severity]
Confidence:      [High / Medium / Low — see criteria below]
Evidence path:   [sourced / fallback / inferred]
```

**Confidence criteria:**
- High: issue reproduced in live session or confirmed via Replay.io step-through; cause validated at the code level; Sentry or LogRocket provides corroborating evidence
- Medium: issue reproduced via session replay or telemetry but not in live session; cause is a strong hypothesis supported by multiple evidence signals
- Low: issue described by reporter but not reproduced; evidence is from screenshots or description only; cause is speculative

**Separation rule:** Observation and Cause must be written by different reasoning steps. Do not collapse what was seen into a root cause in the same sentence.

---

## Prioritization Logic

After all findings are documented:

1. **P0 — Production breakage**: issues that prevent core user flows (checkout, login, data save) or affect all users on a surface. Include regardless of confidence level. Flag Low-confidence P0 findings for immediate verification.
2. **P1 — Functional regression**: incorrect behavior that affects a significant portion of users or a key workflow, with a known workaround. Confidence must be Medium or High to file as standalone P1.
3. **P2 — Edge-case or partial defect**: incorrect behavior in narrow conditions (specific browser, specific data, specific role). Group Low-confidence P2 findings into a single `### Minor and unconfirmed observations` block rather than standalone findings.
4. **Intermittent issues**: flag explicitly as `intermittent — requires extended reproduction or Replay.io time-travel`. Do not promote to P0/P1 without at least one confirmed reproduction.

Limit standalone findings to eight. Observations that cannot be connected to a specific source of truth belong in the Coverage Map or Limits section.

---

## Pattern Detection

After evidence is collected, the agent must identify:

- **Recurring error type**: the same error class appearing at multiple surfaces or for multiple users — indicates a systemic issue (e.g., all API responses missing auth header after token refresh)
- **Environment-only regression**: issue present in production but not local — indicates build config, environment variable, CDN config, or feature flag divergence
- **State accumulation bugs**: incorrect behavior that only appears after a sequence of interactions — indicates stale closure, reducer side effect, or missing state reset
- **Third-party interference**: error originates in a vendor script (analytics, chat widget, A/B testing SDK) rather than in application code — do not assign to application team without confirmation
- **Browser-specific divergence**: issue present in one browser but not others — indicates browser API support gap, CSS rendering difference, or vendor-prefixed property issue
- **Data-shape dependencies**: issue only occurs with specific API response shapes (null fields, empty arrays, unexpected nesting) — indicates missing defensive coding at the component boundary

Distinguish application bugs (owned by the team) from infrastructure issues (CDN, third-party, environment config). They require different escalation paths.

---

## Recommendations

Each recommendation must:
- Reference the finding it addresses by ID
- Be directional — describe what to change, not how to implement it
- Distinguish between: fix (can act now), needs verification (reproduce before acting), and needs alignment (cross-team or infra dependency)
- Acknowledge evidence limits where confidence is Medium or Low

Format:
```
Recommendation [ID]
Finding:         [Finding ID]
Direction:       [What needs to change and why]
Type:            [Fix / Needs verification / Needs alignment]
Priority:        [P0 / P1 / P2 — derived from finding priority]
Blocker:         [What must be true before the fix can land safely — or "none"]
```

Do not recommend a fix without a confirmed source of truth. If confidence is Low, the recommendation is "verify reproduction in [environment] before acting."

---

## Coverage Map

Document what was analyzed and at what depth:

| Evidence source          | Coverage status     | Notes                                          |
|--------------------------|---------------------|------------------------------------------------|
| Chrome DevTools Console  | Full / Partial / None |                                              |
| Chrome DevTools Network  | Full / Partial / None |                                              |
| Chrome DevTools Elements | Full / Partial / None |                                              |
| Chrome DevTools Performance | Full / Partial / None |                                           |
| Sentry error event       | Full / Partial / None | Error ID if available                        |
| LogRocket session        | Full / Partial / None | Session URL if available                     |
| Replay.io recording      | Full / Partial / None | Recording link if available                  |
| Jam report               | Full / Partial / None | Jam link if available                        |
| Highlight.io trace       | Full / Partial / None |                                              |
| DebugBear RUM data       | Full / Partial / None |                                              |
| Repository / source code | Full / Partial / None | Files inspected                              |

State the overall evidence confidence: what proportion of available evidence was accessed. If key tools are unavailable (e.g., no Sentry instrumentation, no session replay), flag the analysis as limited and name the evidence that would change confidence.

---

## Limits and Unknowns

Mandatory section. Document honestly:

- What could not be reproduced: state the environment where reproduction was attempted and failed
- What requires production access: issues only observable in production cannot be fully confirmed in local/staging without matching environment
- What requires real-user session data: issues that only appear under specific user data shapes may need session replay or user-consented observation
- Where confidence is Low: findings marked Low that are driving the fix direction must be flagged explicitly
- Browser coverage gaps: if the issue was only analyzed in Chrome, state that Firefox, Safari, and mobile browsers have not been tested
- Auth and data state gaps: if the issue was analyzed under a single auth context, state what other contexts were not tested
- Third-party unknowns: if vendor scripts appear in the stack trace, state that the root cause may be outside the application codebase and requires vendor investigation

Do not omit this section or collapse to a single sentence. Confidence gaps must be named before implementation begins.

---

## Workflow Rules

1. Build the evidence model — component/state model + evidence inventory — before writing any hypothesis.
2. Classify the failure mode before collecting evidence. The classification determines where to look first and prevents wasted inspection time.
3. Declare the evidence path at the start of the deliverable. Label all output as `sourced`, `fallback`, or `inferred` to match the actual path used.
4. No root cause statements before evidence collection. "It's probably a race condition" is not a finding — it is a hypothesis. Hypotheses become findings only when evidence supports them.
5. Separate observation from interpretation. What you saw in the console is an observation. What caused it is an inference. Never collapse them in the same sentence.
6. Do not merge a CSS finding with a JavaScript finding into one root cause unless evidence confirms a causal link.
7. Repro steps must be stated before a finding is closed. Unconfirmed observations are hypothesis items, not findings.
8. If the repro environment cannot be matched, lower confidence and state what environment confirmation is needed before the fix lands.
9. Record which tool path was used and why. Evidence that cannot be traced to a tool or method is not evidence.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/frontend-engineer-browser-debug.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

---

## Required Deliverable Sections

Within `## Skill: browser-debug`, include:

- `### Evidence model`: component/state model, failure mode classification, evidence inventory, evidence path declared
- `### Observed issue`: the visible incorrect behavior stated concretely — what happens vs. what should happen
- `### Reproduction steps`: exact steps, environment, auth state, and data state required to reproduce
- `### Browser evidence`: all captured signals — console errors, network failures, DOM anomalies, replay links — labeled as sourced / fallback / inferred
- `### Findings`: all findings in the structured schema, prioritized
- `### Recommendations`: directional recommendations linked to findings
- `### Coverage map`: what evidence was fully, partially, and not analyzed
- `### Open unknowns`: what remains unresolved before a fix can safely land

---

