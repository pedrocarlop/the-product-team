# Frontend Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `browser-debug`

- Description: Reproduces and isolates a frontend issue by constructing a browser evidence model — combining runtime inspection, session replay, error telemetry, and source-level analysis — then producing a structured finding with root cause, repro steps, and a fix direction.
- Trigger: When UI behavior is wrong, unexpected, or unreproducible and browser-level evidence is required to localize the source of truth. Triggered by bug reports, QA findings, production errors, or a failing automated test.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A structured debugging report with a browser evidence model, reproduction steps, root cause hypothesis, fix direction, and open unknowns — labeled as sourced, fallback, or inferred to match the evidence path used.
- Output: knowledge/frontend-engineer-browser-debug.md
- Done when: The issue is localized to a specific component, state boundary, network dependency, or JavaScript execution path, with reproduction steps verified and a concrete fix direction stated.

## `component-implementation`

- Description: Build or extend reusable frontend components by constructing the component API surface model first — props, variants, states, composition boundaries — then implementing against the design system spec, primitives layer, and component workshop.
- Trigger: When implementation needs a reusable component, not just a one-off screen. When a design handoff is ready and the component must integrate into or bootstrap a design system foundation.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A reusable component with a defined props API, all required variants and interactive states, a Storybook story covering the key states, and adoption notes for downstream implementers.
- Output: knowledge/frontend-engineer-component-implementation.md
- Done when: The component is reusable, aligned to the design system spec, all variants and states are implemented and documented in Storybook stories, and downstream consumers can adopt it without inferring unsupported patterns.

## `executor`

- Description: Close the shipping loop — read all knowledge artifacts, build the app, run the full test suite, fix failures iteratively, and repeat until all checks pass or the fix budget is exhausted. This is the recursive execution skill that transforms deliverables into shipped software.
- Trigger: When all knowledge artifacts (design, spec, implementation) are available and the goal is to get to a green, verified, shippable state without human orchestration of individual fix cycles.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A ship report declaring the final status (shipped / blocked / partial), the number of fix iterations used, all resolved failures with their root causes, any unresolved blockers with structured findings, and the commit SHA or file diff that represents the shipped state.
- Output: knowledge/frontend-engineer-executor.md
- Done when: The test suite exits green (zero failing tests), the E2E smoke suite passes across primary viewports, axe-core reports zero critical or serious violations, and the build produces a deployable artifact — OR the fix budget is exhausted and all remaining blockers are surfaced as structured findings.

## `frontend-verify`

- Description: Applies structured UI verification — behavior checks, layout fidelity, visual regression, and basic accessibility — to confirm the implemented frontend matches design intent and quality expectations before handoff.
- Trigger: When frontend implementation is complete and requires validation before handoff to design review, QA, or release.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A frontend verification result with a UI model, structured behavior and layout findings, visual regression status, accessibility scan summary, and explicit residual risk.
- Output: knowledge/frontend-engineer-frontend-verify.md
- Done when: All in-scope surfaces have been verified against behavior, layout, and basic quality expectations; all findings are documented with evidence and repro steps; and residual risks are explicitly named.

## `implement-from-design`

- Description: Build an implementation map from an approved design — inventory surfaces, map components and tokens, verify state coverage — then write production code that faithfully reproduces the design intent, including all required states and interactions.
- Trigger: When approved design work is ready for implementation and the implementation target (component, route, surface) has been clearly scoped.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A working UI implementation that faithfully reproduces the approved design, covers all required states and interactions, and is aligned to the project design system spec.
- Output: knowledge/frontend-engineer-implement-from-design.md
- Done when: The implemented surface matches the approved design's structure, spacing, typography, color, and behavioral states; all required states are covered in code; the fidelity gaps section explicitly accounts for any deviations; and the code touchpoints are identified so downstream review can verify the right surface.

## `responsive-refinement`

- Description: Adapt and improve a surface so it works cleanly across breakpoints and devices by constructing a breakpoint matrix, auditing layout behavior per viewport, and producing a prioritized set of responsive fixes — grounded in real tool evidence.
- Trigger: When responsive behavior is missing, inconsistent, or under-specified across breakpoints or device classes.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A breakpoint matrix, per-breakpoint audit findings, and a prioritized responsive fix list with reproduction steps, cause analysis, and a verification plan.
- Output: knowledge/frontend-engineer-responsive-refinement.md
- Done when: Every breakpoint in the defined set has been audited, all Critical and Significant findings have a documented fix or accepted risk, and desktop and mobile behavior are both intentional and verifiable.

## `stateful-ui-build`

- Description: Build the full async state model for a UI surface by constructing a state inventory first, then implementing loading, error, empty, and interactive states with explicit transitions — grounded in the state machine before any code is written.
- Trigger: When a frontend feature surface has async data dependencies, user-triggered state changes, or behavioral requirements across more than one lifecycle state (loading, error, empty, interactive, optimistic).
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A stateful UI implementation covering all critical lifecycle states, with a documented state inventory, MSW-backed Storybook stories for each state, and a verification log confirming state coverage.
- Output: knowledge/frontend-engineer-stateful-ui-build.md
- Done when: The state inventory is complete, all critical states (loading, error, empty, interactive) are implemented and verifiable in code or Storybook, transitions are explicit and tested, and no state is handled only by silence or missing UI.
