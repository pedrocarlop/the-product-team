---
name: executor
description: Close the shipping loop — read all knowledge artifacts, build the app, run the full test suite, fix failures iteratively, and repeat until all checks pass or the fix budget is exhausted. This is the recursive execution skill that transforms deliverables into shipped software.
trigger: When all knowledge artifacts (design, spec, implementation) are available and the goal is to get to a green, verified, shippable state without human orchestration of individual fix cycles.
required_inputs:
  - project slug (to locate context.md and knowledge/ artifacts)
  - repo_write_scope (the bounded app/ path this pass owns)
  - done_when criteria (test suite, E2E flows, accessibility threshold — defaults apply if not stated)
  - environment target (localhost dev server, staging, preview URL)
recommended_passes:
  - context load (read all knowledge/ artifacts before touching code)
  - build check (confirm the app compiles and the dev server starts)
  - test loop (run → analyze → fix → re-run, up to fix_budget iterations)
  - E2E verification (playwright against live environment)
  - accessibility gate (axe-core, WCAG 2.1 AA, zero critical violations)
  - ship report (structured status: shipped / blocked / partial)
fix_budget: 5
tool_stack:
  runtime:
    primary: [exec_command, read_thread_terminal]
  test:
    primary: [vitest, playwright]
    secondary: [storybook, msw]
  accessibility:
    primary: [axe_core]
  code:
    primary: [repository, apply_patch]
  observation:
    primary: [chrome_devtools, view_image]
  fallback:
    primary: [search_query, reference_trace]
tool_routing:
  - if: app has unit/component tests
    use: [vitest] for the test loop
  - if: app has E2E test suite configured
    use: [playwright] for E2E verification pass
  - if: no E2E suite exists
    use: [playwright] to write a minimal smoke test covering primary user flows before verifying
  - if: fix requires inspecting runtime behavior
    use: [chrome_devtools, view_image] to observe before patching
  - if: fix requires installing a missing dependency
    use: [exec_command] to run the package manager install command
  - if: a test failure is caused by a missing MSW handler
    use: [msw] to add the handler; do not modify production code to bypass the test
  - if: primary tools are unavailable
    use: [search_query, reference_trace] to reason about fixes; label output as fallback
best_guess_output: A ship report declaring the final status (shipped / blocked / partial), the number of fix iterations used, all resolved failures with their root causes, any unresolved blockers with structured findings, and the commit SHA or file diff that represents the shipped state.
output_artifacts: knowledge/frontend-engineer-executor.md
done_when: The test suite exits green (zero failing tests), the E2E smoke suite passes across primary viewports, axe-core reports zero critical or serious violations, and the build produces a deployable artifact — OR the fix budget is exhausted and all remaining blockers are surfaced as structured findings.
---

# Executor

## Purpose

This skill closes the shipping loop. It reads every available knowledge artifact, builds the app, runs the full test suite, fixes failures with targeted patches, and repeats — until the implementation is shippable or the fix budget is exhausted.

Reasoning type: iterative and diagnostic — each iteration generates new evidence about what is failing, why, and what the minimal fix is. The loop terminates on a pass condition, not on a time limit.

This skill does NOT:
- Rewrite working code to improve style or architecture
- Add features or scope beyond what the knowledge artifacts specify
- Skip the context load phase and work from memory alone
- Accept a passing test as proof that design intent was met — E2E and axe-core gates are mandatory
- Spend more than one fix iteration on the same failure without escalating it to a structured blocker

---

## Required Inputs and Assumptions

**Required:**
- Project slug: used to locate `logs/active/<project-slug>/context.md` and all `knowledge/` artifacts
- `repo_write_scope`: the bounded path in `app/` this pass may modify (e.g., `app/web/`)
- `done_when` criteria: if not stated explicitly, defaults to: zero failing unit tests + E2E smoke pass + zero axe critical/serious violations
- Environment target: where the app runs (localhost port, staging URL, preview URL)

**Infer and label if missing:**
- If `repo_write_scope` is not in the assignment, infer from the most recent implementation artifact in `knowledge/` and label `Assumed context:`
- If no E2E suite exists, write a minimal smoke suite before running the E2E gate — do not skip the gate
- If the environment target is not specified, assume `localhost` with the port declared in `package.json` dev script

**Known vs unknown at executor time:**
- Known: what was designed and specified (knowledge/ artifacts); what code exists (app/ directory)
- Often unknown: whether all test fixtures reflect the final implementation; whether the dev server starts cleanly; whether the E2E suite covers the flows declared in the spec
- Resolve all unknowns through observation (run the command, read the output) before inferring

---

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live execution** — Run the command, read `read_thread_terminal` output. Highest fidelity. This is the default path.
2. **Structured test output** — Vitest/Playwright JSON reporters, axe-core reports. Structured, reproducible. Parse these before reading raw terminal.
3. **Code inspection** — Read source files to understand why a test fails before patching. Required before any fix is applied.
4. **Visual observation** — `view_image` or `chrome_devtools` screenshots. Use when a test fails visually or a layout assertion fails.
5. **Inference** — Used only when a tool is unavailable. Label explicitly as `inferred`. Do not apply a fix based on inference alone.

Declare which path was used for each fix iteration in the ship report. The fix is only as reliable as the evidence that motivated it.

---

## Tool Stack

**Execution — exec_command + read_thread_terminal**
The primary control loop. Every build, install, test run, and server start goes through `exec_command`. `read_thread_terminal` reads the output. Always capture full stderr. Do not truncate error output — the root cause is often in the last line of a stack trace.

**Unit/component testing — Vitest**
Run with `--reporter=json` for structured output. Parse the JSON before reading terminal output. Focus on the `numFailedTests`, `testResults[].assertionResults[]`, and `message` fields. Run only the failing test file on fix iterations (e.g., `vitest run src/components/Button.test.tsx`) to reduce feedback loop latency.

**E2E testing — Playwright**
Run with `--reporter=json`. On first run, execute the full suite. On fix iterations, re-run only the failing spec file. Use `--headed` flag via `exec_command` only when visual debugging is required. Set `--timeout=30000` as a reasonable default — increase only if a specific test is legitimately slow.

**Mock service layer — MSW**
When a test failure is caused by an unhandled API request, add the handler to the MSW fixtures rather than mocking it at the component level. MSW handlers are the authoritative mock layer — bypassing them creates a divergence between test and production behavior.

**Accessibility — axe-core**
Integrated via `@axe-core/playwright`. Run against every route in the E2E suite after the functional pass. Collect violations by WCAG rule ID and impact level. Block ship on: `critical` and `serious` violations. Document `moderate` and `minor` violations as open findings, not blockers.

**Patching — apply_patch + repository**
Read the relevant source file before patching. Apply the minimal change that resolves the failure. Do not refactor surrounding code. Record the patch as a structured finding in the ship report.

**Visual debugging — chrome_devtools + view_image**
Use when a Playwright screenshot assertion fails or a layout test produces an unexpected diff. Take a screenshot, observe the actual vs. expected state, then apply the fix. Do not guess at layout fixes without visual evidence.

---

## Tool Routing

- Unit/component test fails → run `vitest run <failing-file>` → read JSON output → inspect source → apply minimal patch → re-run
- E2E test fails on interaction → run Playwright with `--headed` → `view_image` screenshot → identify failure → patch → re-run
- E2E test fails on network request → add MSW handler for the missing endpoint → re-run (do not mock at call site)
- Build fails on missing dependency → run `<package-manager> add <package>` → re-run build
- Build fails on TypeScript error → read the full TS error → trace to source → apply typed fix → re-run
- axe-core critical violation → read the violating element → fix the DOM or ARIA attribute → re-run axe
- Same failure persists after 2 fix iterations → escalate to a structured blocker; do not burn fix budget on the same root cause
- Primary tools unavailable → label output as `fallback`; reduce confidence; surface as a risk in the ship report

---

## Environment and Reproducibility

Record in the ship report:

- **Repo commit SHA** at the start of the executor run
- **Node.js and package manager version** (`node -v`, `pnpm -v` or `npm -v`)
- **Dev server URL and port** confirmed running
- **Test runner versions**: Vitest version, Playwright version, axe-core version
- **Number of fix iterations used** vs. fix budget
- **Browser(s) tested**: Chromium (required), Firefox (recommended), WebKit (if in scope)
- **Viewports tested**: at minimum 375px mobile and 1280px desktop
- **Auth state during E2E**: signed-in vs. signed-out; which persona/role

---

## Model Building

Before the first test run, the executor must build an execution model. No test run may begin before this model is complete.

**Step 1 — Knowledge load.** Read every file in `knowledge/` relevant to the current project. This is non-negotiable. The executor must know what was designed, what was specified, and what the engineer implemented before running a single test. Specifically read:
- `knowledge/orchestrator.md` (Execution Manifest — index of all deliverables)
- `knowledge/project-ds-spec.md` (design system decisions)
- `knowledge/frontend-engineer-implement-from-design.md` (implementation map)
- `knowledge/frontend-engineer-stateful-ui-build.md` (state coverage)
- Any other `knowledge/frontend-engineer-*.md` files from prior passes

Record which files were read and what the key implementation decisions were. This is the difference between fixing to green and fixing to the wrong target.

**Step 2 — Codebase scan.** Read the directory structure under `repo_write_scope`. Identify: test configuration files, existing test files, E2E spec files, MSW handler directories, and the dev server start command. Do not write or modify anything yet.

**Step 3 — Baseline status.** Run the full test suite once before applying any fix. Record: total tests, passing, failing, error messages. This is the Iteration 0 baseline. All subsequent fix iterations are measured against it.

**Step 4 — Fix plan.** Group Iteration 0 failures by root cause type:
- `build` — compile or TypeScript errors
- `unit` — failed assertions in component/unit tests
- `e2e` — failed Playwright specs
- `missing-handler` — unhandled API requests in MSW
- `a11y` — axe-core violations

Prioritize: build → unit → missing-handler → e2e → a11y. A build failure blocks everything else. Do not run E2E until unit tests are green.

---

## Core Method Execution

Follow this sequence. Each step must complete before the next begins.

**Step 1 — Context load (mandatory, no exceptions)**
Execute the Model Building steps above. Record in `### Execution context` of the deliverable.

**Step 2 — Build check**
Run the build command (`pnpm build` or equivalent). If the build fails:
- Read the full error output
- Apply a targeted fix
- Re-run build
- Count against the fix budget
- If build is not green after 2 iterations, declare a `build-blocker` and halt

**Step 3 — Unit test loop**
Execute the fix loop for unit/component tests:

```
while failing_tests > 0 and iterations_used < fix_budget:
  1. Run: vitest run --reporter=json
  2. Parse JSON output: collect failing tests, error messages, stack traces
  3. For each unique failure (by error type + file):
     a. Read the failing test file
     b. Read the source file under test
     c. Identify the root cause (assertion mismatch, missing mock, wrong prop, type error)
     d. Apply the minimal fix — patch source or test, never both in the same iteration
     e. Record the fix as a structured finding
  4. Re-run: vitest run <failing-files-only>
  5. Increment iterations_used
  6. If the same failure persists after 2 consecutive iterations → escalate to structured blocker
```

If all unit tests pass before fix_budget is exhausted, proceed to Step 4.

**Step 4 — Dev server startup**
Confirm the dev server starts and is reachable at the environment target URL. Run: `pnpm dev` (or equivalent). Use `exec_command` in background mode. Wait for the "ready" signal in terminal output before proceeding. If the server fails to start, treat it as a `build-blocker`.

**Step 5 — E2E loop**
Execute the fix loop for Playwright E2E tests:

```
while e2e_failing > 0 and iterations_used < fix_budget:
  1. Run: playwright test --reporter=json
  2. Parse JSON output: collect failing specs, error messages, screenshot paths
  3. For each unique failure:
     a. view_image the failure screenshot (if available)
     b. Read the failing spec file
     c. Read the relevant source component
     d. Identify root cause: selector mismatch, timing, missing handler, wrong state
     e. Apply minimal fix
     f. Record as structured finding
  4. Re-run: playwright test <failing-spec-file>
  5. Increment iterations_used
  6. If same failure persists after 2 iterations → escalate to structured blocker
```

**Step 6 — Accessibility gate**
Run axe-core across all primary routes:
1. For each route in the E2E suite: inject axe-core via `@axe-core/playwright` and collect violations
2. Group violations by rule ID and impact level
3. For each `critical` or `serious` violation:
   - Read the violating element in the source
   - Apply a minimal ARIA or semantic HTML fix
   - Re-run axe on that route
   - Count against fix budget
4. `moderate` and `minor` violations → document as open findings, not blockers

**Step 7 — Ship report**
Produce the structured deliverable.

---

## Fix Rules

The following rules govern every fix applied during the loop. Violating them invalidates the executor pass.

1. **One cause per fix**: Each patch addresses exactly one root cause. If a fix would touch two unrelated failures, split into two iterations.
2. **Source before test**: Fix the source when the implementation is wrong. Fix the test only when the test is asserting something that was never in the spec (and document why).
3. **No scope expansion**: Do not add features, refactor code structure, rename identifiers, or clean up unrelated files during a fix iteration. The fix must be the minimum change that makes the failing assertion pass.
4. **Verify each fix**: Re-run the specific failing test after every patch. Do not batch multiple fixes and run once — the feedback loop must be tight.
5. **Budget discipline**: If `iterations_used >= fix_budget`, stop the loop immediately. Do not apply further fixes. Surface all remaining failures as structured blockers.
6. **No silent rewrites**: If a fix requires changing the component's public API (props, events, slots), escalate to the orchestrator — this is a scope change, not a fix.

---

## Structured Findings

Every fix applied and every unresolved failure must use this schema. No free-form notes.

```
#### Fix <id> | Iteration <n>
Type:          [build / unit / e2e / missing-handler / a11y]
Failure:       [Exact error message or test assertion that failed]
Evidence:      [Tool output reference — JSON path, screenshot file, axe rule ID]
Root cause:    [Why it failed — labeled `inferred` if not confirmed from source inspection]
Fix applied:   [Exact description of the patch: file path, what changed, why]
Verification:  [Test command re-run and result after fix]
Confidence:    [High / Medium / Low + rationale]
```

```
#### Blocker <id>
Type:          [build / unit / e2e / missing-handler / a11y]
Failure:       [Exact error message]
Evidence:      [Tool output reference]
Root cause:    [Most likely cause — labeled `inferred` if unconfirmed]
Iterations:    [How many fix attempts were made before escalating]
Unblocked by: [What would need to change for this to be resolvable — design change, API contract, missing fixture, upstream dependency]
```

---

## Prioritization Logic

Fix order within the loop:

1. **Build blockers** — nothing else can run until the build is clean
2. **Missing MSW handlers** — unhandled requests cause cascading unit and E2E failures; fix these first
3. **Unit test failures in shared utilities or hooks** — failures here propagate to many components
4. **Unit test failures in leaf components** — isolated; fix last within the unit loop
5. **E2E failures on primary user flows** — fix before secondary flows
6. **E2E failures on edge cases or error states** — fix after primary flows
7. **axe-core critical violations** — block ship
8. **axe-core serious violations** — block ship
9. **axe-core moderate/minor violations** — document; do not block ship

---

## Pattern Detection

After the loop completes, identify:

- **Systematic test failures**: the same error type appearing across multiple files — signals a missing fixture, wrong global setup, or misconfigured test environment
- **Selector drift**: Playwright selectors that fail because component markup changed without updating the spec — indicates a gap between implementation and E2E maintenance
- **MSW coverage gap**: multiple unhandled API requests — signals that the MSW handler file was not updated when new endpoints were added
- **TypeScript strictness cascades**: a type error in a shared type that propagates to many files — fix the shared type, not each instance

Call out system-level patterns explicitly. They recur across projects and belong in a retrospect note.

---

## Ship Status

The deliverable must declare exactly one of these statuses:

**`SHIPPED`**: All done_when criteria are met. Zero failing tests, E2E passes, axe-core zero critical/serious. The implementation is ready to deploy.

**`BLOCKED`**: The fix budget was exhausted before all criteria were met. The deliverable lists all structured blockers. The orchestrator must decide: extend the budget, escalate to design/product, or accept partial ship.

**`PARTIAL`**: Done_when criteria are met for unit tests and E2E but not for accessibility (or vice versa). Explicitly state which gate passed and which did not. Ship decision belongs to the orchestrator.

---

## Coverage Map

State explicitly:

- **Gates passed**: which test suites ran and exited green (unit, E2E, axe)
- **Gates failed / budget exhausted**: which suites did not pass and why
- **Fix iterations used**: `N / fix_budget`
- **Routes covered by E2E**: list each route and pass/fail
- **Routes covered by axe-core**: list each route and violation count by impact level

---

## Limits and Unknowns

Mandatory section. State:

- Whether a full MSW handler inventory was available before the test loop
- Whether the E2E suite covered all primary user flows or only a subset
- Whether any test was skipped due to environment unavailability (auth, seed data, external API)
- Whether the fix budget was sufficient or whether a higher budget would likely resolve remaining blockers
- Whether axe-core's automated scan was the full accessibility review (it is not — manual review still required for keyboard navigation, screen reader, and cognitive accessibility)
- Whether the dev server was running in a production-equivalent configuration or a local approximation

---

## Workflow Rules

1. Context load is not optional. Never start the test loop without reading `knowledge/`.
2. Build before test. Never run tests against a broken build.
3. Re-run the specific failing test after every fix — not the full suite — until that test is green. Then run the full suite to confirm no regression.
4. One fix per iteration. Do not batch.
5. Same failure twice → escalate to structured blocker. Do not loop indefinitely.
6. Fix source before test. The test is the spec — do not change it unless the spec was wrong.
7. No scope expansion. If a fix requires new features, return a scope-escalation note to the orchestrator instead.
8. Declare ship status explicitly. Never leave the deliverable without a `SHIPPED`, `BLOCKED`, or `PARTIAL` verdict.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at `knowledge/frontend-engineer-executor.md`.
- Do not merge this output into a shared role-level document.
- Every fix and every blocker must be recorded. Do not summarize or omit iterations.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end with `What worked`, `What didn't`, and `Next steps`.

---

## Required Deliverable Sections

Within `## Skill: executor`, include:

- `### Execution context`: Knowledge artifacts read, codebase scan summary, Iteration 0 baseline (total tests, passing, failing).
- `### Fix log`: Every fix applied, in order, using the structured finding schema. One entry per fix. Grouped by iteration.
- `### Blocker log`: Every unresolved failure using the structured blocker schema.
- `### E2E results`: Per-spec pass/fail, routes covered, viewports tested.
- `### Accessibility results`: axe-core results per route, violations by impact level, fixes applied.
- `### Ship status`: `SHIPPED` / `BLOCKED` / `PARTIAL` with rationale.
- `### Coverage map`: Gates passed/failed, fix budget used, routes covered.
- `### Residual risk`: Named unknowns, open accessibility findings, assumptions about environment or test coverage.
