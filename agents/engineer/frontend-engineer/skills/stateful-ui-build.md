---
name: stateful-ui-build
description: Build the full async state model for a UI surface by constructing a state inventory first, then implementing loading, error, empty, and interactive states with explicit transitions — grounded in the state machine before any code is written.
trigger: When a frontend feature surface has async data dependencies, user-triggered state changes, or behavioral requirements across more than one lifecycle state (loading, error, empty, interactive, optimistic).
required_inputs:
  - the surface name and its primary async operations (data fetches, mutations, side effects)
  - the API contract or data shape each operation returns
  - any known error modes or failure conditions
  - the target framework and existing state management stack when known
recommended_passes:
  - state machine / state inventory construction
  - loading and skeleton state implementation
  - error and recovery state implementation
  - empty and first-run state implementation
  - interactive transition and optimistic update implementation
  - state coverage verification
tool_stack:
  runtime:
    primary: [repository, xstate_inspector, browser_devtools]
    secondary: [storybook, vitest_browser_mode]
  artifacts:
    primary: [storybook_stories, msw_handlers]
  verification:
    primary: [vitest, playwright, react_testing_library]
  fallback:
    primary: [reference/trace, search_query]
tool_routing:
  - if: codebase is accessible and contains existing state logic
    use: [repository] — read current state handling before building the inventory
  - if: state machine visualization or actor graph is needed to validate transitions
    use: [xstate_inspector] — connect to running app via XState DevTools Chrome extension
  - if: runtime behavior must be observed (network timing, render cycles, DevTools Performance)
    use: [browser_devtools]
  - if: individual states need to be rendered and verified in isolation
    use: [storybook] — write one story per state (loading, error, empty, loaded, interactive)
  - if: network responses need to be mocked to reach specific states reproducibly
    use: [msw_handlers] — define per-story or per-test MSW request handlers that intercept fetch/XHR
  - if: unit-level async state transitions or hook behavior must be tested
    use: [vitest + react_testing_library] — test state transitions in a JSDOM environment
  - if: full-page or cross-surface state flows must be verified end-to-end
    use: [playwright] — assert visible state labels, aria-live regions, or skeleton presence
  - if: primary tools are unavailable or repository is not accessible
    use: [reference/trace, search_query] — produce inferred state model, label output as `inferred`
best_guess_output: A stateful UI implementation covering all critical lifecycle states, with a documented state inventory, MSW-backed Storybook stories for each state, and a verification log confirming state coverage.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: stateful-ui-build"
done_when: The state inventory is complete, all critical states (loading, error, empty, interactive) are implemented and verifiable in code or Storybook, transitions are explicit and tested, and no state is handled only by silence or missing UI.
---

# Stateful UI Build

## Purpose

Implement the full async, error, empty, and interactive state model for a UI surface.

This skill applies state machine thinking to frontend implementation: before any code is written, the agent constructs a state inventory that defines every possible state the surface can be in, the events that trigger transitions, and the data requirements at each state. The implementation then follows directly from that model.

This skill applies structured implementation reasoning — state modeling, transition mapping, component decomposition, mocking strategy — to produce code that is explicit, testable, and behaviorally complete.

This skill does not skip model construction to go directly to code, does not treat "loading" as a single boolean flag, does not implement states as implicit fallthrough logic, and does not leave error or empty states as unstyled null renders.

## Required Inputs and Assumptions

Required inputs:
- The surface name and its primary async operations (data fetches, mutations, real-time subscriptions)
- The API contract or data shape returned by each operation, including error response shapes
- Known error modes: network failure, auth expiry, partial data, rate limiting, empty result set
- The framework in use (React, Vue, Svelte, etc.) and the existing state management stack
- Any optimistic update requirements (writes that should reflect in UI before server confirmation)

If inputs are missing, infer provisional values and prefix each with `Assumed context:`. Lower the confidence of any finding that depends on an inferred input. If the API contract is missing, infer from component props, existing network calls in the repository, or route handler signatures.

Known vs unknown: the happy path is usually documented. Error shapes, empty conditions, and intermediate states often are not. Both must be explicitly resolved or assumed before the state model is built.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live / real interaction** — Observe the surface running in a real environment (dev, staging, or production). Trigger each state by manipulating network conditions, data, or auth. Highest fidelity; captures timing, flicker, and race conditions.
2. **Structured system access** — Read the repository directly: component code, API call sites, state management stores, server handlers. Covers the full implementation surface but reflects code intent, not runtime behavior.
3. **Design artifacts or documentation** — Figma handoff specs, PRD state tables, or OpenAPI schemas. Useful as a contract source; may be incomplete or out of date relative to implementation.
4. **Screenshots / static input** — Visual snapshots of the surface in specific states. Limited to visible UI; no transition or timing context.
5. **Inference** — State model inferred from component structure, naming conventions, or framework patterns. Must be labeled explicitly. Last resort only.

Declare which path was used. Declare its limitations in the deliverable. Prefer path 2 (repository) as the default. Combine paths when they address different evidence gaps — e.g., path 2 for the state model and path 1 (DevTools) for timing validation.

## Tool Stack

**Repository (runtime — primary):** Direct access to the codebase via the `repository` MCP. Use to read existing state logic, identify current state handling patterns, locate API call sites, and understand component composition before writing anything. Always start here when the repository is accessible.

**XState v5 (runtime — primary):** XState is a state machine and actor model library (25k+ GitHub stars, 1M+ weekly npm downloads). Use it when state transitions are complex, conditional, or involve multiple concurrent actors (e.g., a form that depends on both a fetch and a user action). XState v5 centers on the actor model: promise actors for async operations, machine actors for orchestrating transitions, and `useActor` / `useMachine` hooks for React integration. The XState Inspector Chrome extension visualizes the state graph in real time. Use XState when the surface has more than 3–4 distinct states with non-trivial transition rules, or when an optimistic update must be rolled back on failure.

**TanStack Query v5 (runtime — primary for server state):** TanStack Query is the standard for async server-state management (data fetching, caching, background revalidation). In v5, the key state flags are `isPending` (no cached data, request in flight), `isError`, `isSuccess`, and `isFetching` (background refetch). Use `placeholderData: keepPreviousData` to prevent empty flicker during pagination or filter changes. `useMutation` provides `isPending`, `isError`, and `onMutate` / `onError` / `onSettled` callbacks for optimistic updates. Use TanStack Query as the default server-state layer; reach for XState only when cross-query orchestration or machine-driven transitions are needed.

**Zustand (runtime — secondary for client state):** Zustand is a lightweight, hook-based global state library (~4KB). Use it for client-side UI state that must be shared across components but is not tied to a server response — e.g., a selected item ID, a modal visibility flag, a multi-step form accumulator. Zustand's single-store model with a flat action API avoids the boilerplate of Redux Toolkit for most mid-size apps. Prefer Zustand over React Context when the state is updated frequently or subscribed to by many components.

**Jotai (runtime — secondary for fine-grained derived state):** Jotai is an atomic state library. Use it when individual pieces of UI state are independent and derived from each other — e.g., a filtered list derived from a raw list atom and a filter atom. Jotai's atom model prevents unnecessary re-renders at the component level. Prefer Jotai over Zustand when the state graph is compositional rather than centralized.

**Redux Toolkit (runtime — secondary for large-scale normalized state):** Redux Toolkit (RTK) is the official Redux toolset. Use it when the app has complex normalized entity state, requires middleware (e.g., logging, analytics, offline sync), or the team already relies on the Redux DevTools time-travel debugger. RTK Query (built into Redux Toolkit) provides a full data-fetching and caching layer as an alternative to TanStack Query. Choose RTK when the project already uses Redux or when strict, auditable state history is a requirement.

**Storybook v8 (artifacts — primary for state simulation):** Storybook is a frontend workshop for building UI components in isolation. Write one story per state: `Loading`, `Error`, `Empty`, `Loaded`, `Interactive`, `Optimistic`. Use the `play` function (powered by Testing Library) to simulate interactions within a story. Use the `msw-storybook-addon` to inject MSW handlers per story so each state is driven by a real (mocked) network response, not a prop override. Storybook stories serve as living documentation and the first verification layer for state coverage.

**MSW — Mock Service Worker v2 (artifacts — primary for network mocking):** MSW intercepts fetch and XHR requests at the Service Worker level in the browser and at the Node `http` module level in test environments. This means the same handler definitions work in Storybook, Vitest, and Playwright without changing application code. Define handlers that return loading delays (`delay(1500)`), success payloads, error status codes (400, 401, 404, 500), and empty arrays. This allows every state to be triggered deterministically in isolation.

**Vitest + React Testing Library (verification — primary for unit/integration):** Vitest is the default unit test runner for Vite-based projects in 2025. Use it with React Testing Library to assert that components render the correct UI in each state, that error messages appear on failure, and that retry callbacks fire. Use `waitFor` and `findBy*` queries to handle async resolution. Combine with MSW's Node handler setup for fully realistic async test scenarios without network calls.

**Playwright (verification — primary for E2E state flows):** Playwright tests full-page state flows in a real browser. Use it to verify that loading skeletons appear on navigation, that error banners appear and retry buttons work, and that empty states are shown when an API returns zero results. Use Playwright's `page.route()` as an alternative or supplement to MSW for request interception in E2E tests.

**Browser DevTools / XState Inspector (runtime — secondary for observation):** Chrome DevTools Network panel for observing real timing, waterfall, and response shapes. XState Inspector (available as a browser extension for XState v5) for visualizing the live state graph and active transitions. Use these when implementation behavior diverges from the model.

**Fallback — reference/trace + search_query:** When the repository is inaccessible or no existing implementation exists, use reference documentation (framework docs, TanStack Query docs, XState docs) and web search to produce a model and implementation template. Label all output as `inferred`.

## Tool Routing

- Repository accessible → start there. Read state logic before writing the model.
- Server-state (data fetching, caching, background sync) → use TanStack Query v5 as the default.
- Complex cross-state orchestration, rollback on failure, or multi-actor flows → layer in XState v5.
- Shared client-side UI state (not server state) → use Zustand (flat, centralized) or Jotai (atomic, derived).
- Large app with normalized entities or existing Redux setup → use Redux Toolkit.
- State isolation and visual verification → write Storybook stories, one per state.
- Network response simulation → use MSW handlers in Storybook and Vitest; same handlers for both.
- Unit assertion on async state transitions → use Vitest + React Testing Library + MSW Node handlers.
- End-to-end state flow verification → use Playwright.
- Real runtime timing observation → use Browser DevTools Network + Performance panels.
- State machine visualization → use XState Inspector Chrome extension.
- Primary tools unavailable → use reference/trace + search_query; label output `inferred`.
- Never rely on a single tool. The full coverage chain is: model (repository/XState) → isolation (Storybook + MSW) → unit verification (Vitest + RTL) → E2E confirmation (Playwright).

## Environment and Reproducibility

Record the following in the deliverable:

- Framework and version (e.g., React 19, Next.js 15 App Router, Vite 6)
- State management libraries in use and their versions (TanStack Query v5, XState v5, Zustand v5, etc.)
- Storybook version and active addons (msw-storybook-addon version)
- MSW version (v2 for Service Worker + Node handler API)
- Node environment used for Vitest (JSDOM vs browser mode via Playwright)
- Build or environment flag differences (dev vs. production error boundaries, feature flags)
- Whether the API contract used is live, mocked, or inferred from code
- Network conditions observed (e.g., throttled to Slow 3G in DevTools)

If any of the above is unknown, state it explicitly. Do not present timing-sensitive behavior (e.g., skeleton duration, flash of loading state) observed under one network condition as universally representative.

## Model Building

Before any implementation, the agent MUST construct a state inventory. No component code may be written before this model is complete.

**Step 1 — Name the surface and its async boundary.** What is the component or page being modeled? What is the top-level async operation that drives its data lifecycle?

**Step 2 — Enumerate all states.** For every async operation on the surface, define:
- `idle` — operation has not started (initial mount before any fetch is triggered)
- `pending` — operation is in flight; no cached data exists
- `loading_background` — operation is refetching while stale cached data is displayed
- `success` — operation resolved with data
- `empty` — operation resolved successfully but returned zero results or a null payload
- `error` — operation resolved with an error (network, HTTP 4xx/5xx, parse failure)
- `error_partial` — some data returned but part of the operation failed (partial success)
- `optimistic` — a mutation is in flight; the UI reflects the expected success state before confirmation
- `optimistic_rollback` — the mutation failed; the UI must revert to the pre-mutation state

Not every surface will have all states. Prune the list to what is observable and consequential. Label pruned states as `Not applicable` with a reason.

**Step 3 — Map transitions.** For each state pair that can transition (e.g., `pending → success`, `success → error`), identify:
- The triggering event (mount, user action, timer, WebSocket message)
- The side effect (network call, local write, optimistic update)
- The guard condition (only transition if authenticated, only retry N times)

**Step 4 — Define data requirements per state.** What data must be present? What shape? What is the minimum required to render the state without crashing?

**Step 5 — Identify race conditions and edge cases.** Can the user trigger a new fetch while one is in flight? Can auth expire mid-request? Can a mutation fire against stale data?

The state inventory output must be a named table or list in the deliverable before any implementation subsection is written.

## Core Method Execution

Follow this sequence. Do not skip steps.

**Step 1 — Read the existing implementation.** Use the repository tool to locate: the component file, its data-fetching logic, any existing state variables or flags, error handling, and loading conditions. Document what is currently implemented and what is missing before making any changes.

**Step 2 — Build the state inventory.** Apply the model-building steps above. Output the inventory as a table in `### Surface and state model`.

**Step 3 — Implement the loading state.**
- For TanStack Query: use `isPending` (no cached data, first fetch) to render a skeleton. Use `isFetching` alongside cached data to render a subtle background-refetch indicator (e.g., a spinner in a corner, not a full page skeleton).
- For XState: gate the loading render on the machine being in a `loading` or `fetching` state node.
- Use a content skeleton (not a spinner alone) that matches the layout of the loaded content — same number of rows, card shapes, or columns. This reduces layout shift on resolution.
- Ensure the skeleton is accessible: use `aria-busy="true"` on the container and `aria-label="Loading <content name>"` on the skeleton region.
- Do not block interactive chrome (navigation, back button, other surface areas) during loading.

**Step 4 — Implement the error and recovery state.**
- Distinguish error types: network failure (no response), server error (5xx), client error (4xx — auth, validation, not found), and parse error (malformed response).
- Render an error UI that names what failed, not just "Something went wrong." Use the error message from the response when safe to surface.
- Provide a recovery action: a retry button that re-triggers the failed operation, a link to a fallback surface, or an escalation path (support link).
- For TanStack Query, use `refetch()` from `useQuery` as the retry handler. Set `retry: 3` and `retryDelay: attemptIndex => Math.min(1000 * 2 ** attemptIndex, 30000)` for exponential backoff on transient errors.
- Wrap subtrees in React Error Boundaries for render-phase errors (not fetch errors). Error Boundaries catch JavaScript exceptions in the render tree; TanStack Query's `isError` handles network/API failures.
- For XState, model error as an explicit state node with a `RETRY` event transition back to `loading`.
- Log errors to the observability layer (e.g., Sentry) in the error handler, not in the render function.

**Step 5 — Implement the empty state.**
- An empty state is a valid success with zero results. Never conflate empty with loading or error.
- Render content-specific empty messaging: tell the user why there is nothing here and what they can do. "No items found" is weaker than "You haven't added any items yet. Add your first item →".
- If the surface supports creation, include a primary CTA in the empty state. If it is read-only, explain what will populate it.
- For first-run experiences (empty because user has not yet acted), use the empty state to onboard — show an illustration, explain the value, reduce friction to first action.

**Step 6 — Implement interactive transitions.**
- For user-triggered state changes (button click → mutation → result), implement the full arc: pre-action, in-flight (optimistic or loading), confirmed success, and error recovery.
- Optimistic updates: apply the expected state immediately using TanStack Query's `onMutate` callback (write to the query cache before the server responds) and roll back using `onError` with the snapshot returned by `onMutate`. XState can model this as an `optimistic` state that transitions to `success` or `rollback`.
- Prevent double-submission: disable the trigger button while a mutation is in flight using `isPending` from `useMutation`.
- For multi-step flows (wizards, progressive forms), model each step as a distinct state node in XState. Use `useSelector` to derive the current step without exposing the full machine state to child components.
- Ensure transitions are perceivable: use CSS transitions for state changes that swap large content regions; avoid jarring instant swaps.

**Step 7 — Write Storybook stories for each state.** Create one story per state node from the inventory. Use MSW handlers to drive each story from the network layer, not from prop overrides. This ensures stories test the real data flow, not just the render layer. Name stories clearly: `Default`, `Loading`, `BackgroundRefetch`, `Error`, `ErrorPartial`, `Empty`, `Interactive`, `Optimistic`, `OptimisticRollback`.

**Step 8 — Write unit and integration tests.** Use Vitest + React Testing Library + MSW Node handlers. Assert: loading state renders skeleton, error state renders error UI and retry button, empty state renders empty message, success state renders data. Use `waitFor` for async assertions. Test the retry callback fires `refetch`.

**Step 9 — Run E2E verification.** Use Playwright to exercise the full state flow in a real browser. Assert aria attributes, visible text, and interactive element state at each transition point.

**Step 10 — Produce the verification log.** Document which states were reached in testing, how each was triggered, and any gaps.

## Structured Findings

Every state gap or implementation issue must use this exact schema. No free-form output. Separate observation from interpretation. Every finding must be traceable to a source (file, line, or test run).

```
#### Finding <id>
Observation: [What the current implementation does or does not do — no interpretation]
Evidence: [File path + line, test output, or DevTools screenshot reference]
State affected: [Which state node(s) from the inventory]
Cause: [Why this gap exists — labeled as inferred if not confirmed]
Impact: [User-visible consequence; severity if a real user hits this state]
Confidence: [High / Medium / Low + rationale]
```

Confidence guide:
- **High** — directly observed in code or runtime, confirmed by test failure, or reproducible via DevTools.
- **Medium** — inferred from code structure or a single test environment; not yet cross-validated in production.
- **Low** — inferred from absence of code, naming patterns, or a single static screenshot.

## Prioritization Logic

Prioritize findings and implementation work by user impact:

1. **Critical** — States that crash the UI, block all user action, or silently discard data (e.g., unhandled Promise rejection that results in a blank surface, a mutation that fires twice because the submit button is not disabled). Implement before any other state work.
2. **Significant** — States that degrade experience or increase support load: errors with no recovery path, empty states with no explanation, loading states that block interaction unnecessarily.
3. **Minor** — Polish gaps: skeleton shape mismatch, transition duration off, copy that is correct but not ideal. Group these into a single `### Minor gaps` block rather than listing as standalone findings.

Do not include more than eight standalone findings. Observations that do not affect behavior belong in the coverage map, not in findings.

## Pattern Detection

After the state inventory and initial findings are complete, the agent must identify:

- **Missing state classes**: Surfaces where an entire category of state (e.g., all error handling, all empty states) is absent — indicates a systemic gap, not an isolated bug.
- **State collapse**: Where multiple distinct states are handled by the same branch (e.g., `if (!data)` catching both `pending` and `empty`) — this produces incorrect UI when data is loading vs. when it is absent.
- **Unguarded race conditions**: Where a new fetch can be triggered while a previous one is in flight without cancellation or deduplication — TanStack Query deduplicates by key, but imperative fetch calls do not.
- **Optimistic update without rollback**: Where mutations apply local state changes but have no `onError` rollback — leaves the UI in a permanently incorrect state on failure.
- **Error boundary gaps**: Where render-phase errors in async-dependent components are not caught by an Error Boundary — results in full subtree unmount with no user feedback.
- **Accessibility gaps in state transitions**: Where `aria-live` regions are absent during state changes, leaving screen readers with no announcement of content changes.

Distinguish implementation gaps (code is wrong or missing) from design gaps (the state exists in code but the UI treatment is inadequate).

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- Be directional, not prescriptive — state what to address, not the exact implementation unless there is a clear correct approach
- Acknowledge evidence limits where confidence is Medium or Low
- Prefer TanStack Query, XState, Zustand, or Jotai solutions over ad-hoc state flags — explain why the library approach reduces the class of problem

Format: `Rec <id> [Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly:

- **Deeply implemented and verified**: States that have code, Storybook stories, MSW handlers, and at least one automated test (Vitest or Playwright).
- **Partially implemented**: States that have code but lack stories, tests, or have an incomplete UI treatment.
- **Not implemented**: States from the inventory that have no code path — surfaces where the state is simply unreachable in the UI.
- **Not applicable**: States pruned from the inventory with the reason documented.

The coverage map sets the bar for what is done vs. what remains.

## Limits and Unknowns

Mandatory section. State:

- What network conditions or environments were not tested (e.g., only tested on localhost, not on a throttled connection)
- Where the API error response shape was inferred from code rather than confirmed against a schema
- Where optimistic update rollback behavior was implemented but not tested against a real server rejection
- Where React Error Boundaries were added but the specific render-phase errors they should catch were not enumerated
- Where timing behavior (skeleton duration, transition feel) was not validated in a real browser
- Where race condition handling was modeled but not stress-tested with parallel requests
- What real-world validation would increase confidence in the critical-path state flows

Do not omit this section or collapse it to a single line. Low-confidence areas must be named.

## Workflow Rules

- Build the state inventory before writing any component code. No implementation without a model.
- Distinguish fact (directly read from repository or observed in runtime) from inference (reasoned from naming, structure, or documentation). Label every inference.
- Do not treat `isLoading` as a single boolean. Decompose into `isPending` (no data, first fetch) vs. `isFetching` (background refetch with cached data) — these require different UI treatments.
- Never conflate empty state with loading state. `data === undefined` during a fetch is different from `data.length === 0` after a successful fetch.
- Model error types separately: network error, HTTP error, auth error, parse error. Each has a different recovery path.
- Merge duplicate state gaps before writing findings. One finding per distinct behavioral gap — not one per affected component.
- Record the tool path used for each phase (repository read, Storybook story, Vitest test, Playwright run) so the verification is reproducible.
- Avoid hallucinating API response shapes. If the contract is not confirmed, label it `Assumed context:` and lower confidence.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### stateful-ui-build` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: stateful-ui-build`, include:

- `### Surface and state model`: The full state inventory table — state name, description, data requirements, transition triggers, and any guard conditions. This section must be complete before any implementation section is written.
- `### Loading state`: Implementation description for pending and background-refetch states. Skeleton approach, aria attributes, and any layout-shift mitigation. Tool path used (TanStack Query `isPending` / XState state node / Zustand flag).
- `### Error and recovery state`: Per-error-type implementation: network failure, HTTP 4xx, HTTP 5xx, parse error. Error UI description, recovery action (retry, fallback link, escalation), retry strategy (exponential backoff config), and Error Boundary placement.
- `### Empty state`: Implementation of the zero-results case. Copy rationale, CTA if applicable, first-run vs. no-results distinction.
- `### Interactive transitions`: Optimistic update implementation (onMutate, onError rollback, snapshot pattern). Double-submission prevention. Multi-step state modeling if applicable. Transition animation approach.
- `### Storybook stories and MSW handlers`: List of stories written, the MSW handler for each, and the network response each story simulates.
- `### Verification notes`: Which states were reached in Vitest, which in Playwright, which only in Storybook. Which remain untested and why.
- `### Findings`: Structured findings using the required schema.
- `### Recommendations`: Directional recommendations linked to findings.
- `### Coverage map`: What is deeply implemented and verified, partially implemented, not implemented, and not applicable.
- `### Gaps in evidence`: What could not be confirmed, what was inferred, and what requires real-world validation.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: stateful-ui-build`.
- Record which tool path was used for each phase (repository read, Storybook, Vitest, Playwright).
- Label each evidence item as `sourced` (read from repository or observed in runtime), `fallback` (produced from reference docs or web search), or `inferred` (reasoned from absence or naming).
- Ensure the section meets this done-when bar: the state inventory is complete, all critical states are implemented and verifiable in code or Storybook, transitions are explicit and tested, and no state is handled only by silence or a missing UI branch.
