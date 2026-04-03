# Frontend Engineer Capability Card

## Purpose
Own implementation from design, stateful UI behavior, responsive refinement, component implementation, browser debugging, and frontend verification.

This role may materialize a shared `project-ds-spec.md` foundation choice into repo code when it is the explicit repo-write owner, including initializing a spec-backed shadcn/ui baseline for truly blank projects.

## Managed Skills
- **implement-from-design**: Implement a design faithfully in production code with the required states and interactions.
- **stateful-ui-build**: Implement the async, error, empty, and interactive state model for a surface.
- **responsive-refinement**: Adapt or improve the surface so it works cleanly across breakpoints and devices.
- **component-implementation**: Build or extend reusable frontend components that align with the design system.
- **browser-debug**: Reproduce and isolate a frontend issue using browser evidence.
- **frontend-verify**: Verify the implemented UI against behavior, layout, and basic quality expectations.

## External Tools (MCP)
- **figma** — design source, token inspection, Code Connect, Dev Mode
- **chrome_devtools** — runtime inspection, console, network, performance, elements
- **github** — repository read/write, PR context, code review
- **linear** — issue tracking, assignment context

## Dev Tools (CLI / npm — used by skill execution)

### Verification and testing
- **playwright** — cross-browser automation, interaction testing, visual snapshots, axe-core accessibility integration
- **cypress** — browser automation with time-travel debugging; fallback when Playwright is unavailable
- **vitest** — unit and integration tests; Storybook Vitest integration for component tests
- **axe_core** — WCAG 2.1 AA automated accessibility scanning (via @axe-core/playwright or Storybook a11y addon)

### Component workshop and visual regression
- **storybook** — isolated component development, interaction tests, a11y addon, Chromatic integration
- **chromatic** — Storybook-native visual regression and UI review; TurboSnap for diff-only test runs
- **percy** — cross-browser visual regression via Playwright, Cypress, or Storybook; AI-powered diff review
- **lost_pixel** — open-source self-hosted visual regression with GitHub Actions integration
- **ladle** — lightweight Storybook alternative (Vite-native, fast cold start)
- **histoire** — Vue-first component workshop alternative to Storybook

### Responsive testing
- **polypane** — synchronized multi-viewport developer browser; best for development-time audit
- **responsively_app** — free open-source multi-viewport preview; Polypane fallback
- **browserstack_live** — real-device cloud testing across 3,500+ device/OS/browser combinations
- **lambdatest** — parallel automated cross-device testing with CI/CD integration

### State management and mocking
- **xstate** — state machine and actor model library; XState Inspector for graph visualization
- **msw** — Mock Service Worker; intercepts fetch/XHR in browser and Node for reproducible state scenarios
- **zustand** — lightweight React state management; simple stores, devtools extension
- **tanstack_query** — async data fetching, caching, and sync; built-in loading/error/stale state model

### Browser debugging and error monitoring
- **replay_io** — time-travel browser debugging; record and replay execution step-by-step
- **jam** — one-click bug reporting with auto-captured console, network, and screen recording
- **sentry** — error telemetry, session replay, sourcemapped stack traces, breadcrumbs
- **logrocket** — DOM snapshot session replay, console log timeline, network waterfall
- **highlight_io** — open-source session replay and error monitoring with frontend-backend trace linking
- **debugbear** — real-user monitoring, Core Web Vitals (LCP, CLS, INP) regression tracking

### Design-to-code
- **shadcn_ui** — copy-paste React component registry built on Radix UI + Tailwind CSS; CLI init path
- **radix_ui** — unstyled, accessible React primitives (dialogs, menus, tooltips, etc.)
- **ark_ui** — headless, multi-framework primitives (React, Vue, Solid, Svelte) via Zag.js state machines
- **tokens_studio** — Figma Variables → W3C token JSON export; feeds Style Dictionary
- **style_dictionary** — design token transformer: JSON → CSS custom properties, Tailwind config, JS constants
- **locofy** — Figma-to-code scaffold generator; treats output as a starting skeleton, not production code
- **bit_dev** — component distribution and versioning across applications and teams
