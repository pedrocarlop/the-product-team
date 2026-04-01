# Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
It lists only the role-local skills in this folder and keeps descriptions short so you can scan cheaply.
Open only the matching skill files under `skills/`, then end your closing handoff with `Read <skill-paths> skills for this task.`

## frontend/

- `frontend/translate` — Translate product specs, design intent, and implementation constraints into frontend code that matches the intended browser experience.
- `frontend/stateful` — Implement the full frontend state model so every component handles loading, empty, error, success, disabled, and transition states with correct data flow, DOM updates, and accessibility attributes.
- `frontend/harden` — Strengthen frontend code for browser resilience, rendering safety, client-side security, accessibility compliance, and perceived performance before release.
- `frontend/tune` — Refine frontend microcopy, UI feedback wording, and state-specific messaging so the product surface communicates clearly, consistently, and proportionally to the user's context.

## backend/

- `backend/implement` — Build backend services, handlers, migrations, and integrations from an agreed model without drifting from the contract.
- `backend/model` — Shape backend work into explicit domain, data, and contract decisions before implementation starts.
- `backend/observe` — Verify backend code behavior using tests, logs, query inspection, traces, and profiling to confirm correctness and performance after implementation.
- `backend/harden` — Strengthen backend services for data integrity, concurrency safety, operational resilience, and incident readiness before they handle production traffic.

## fullstack/

- `fullstack/model` — Shape the domain, API contract, persistence, and state transitions for a full-stack feature before any layer is built.
- `fullstack/ship` — Validate, harden, and release a full-stack feature safely with end-to-end tests, API and UI verification, migration sequencing, and observability across the entire request path.
- `fullstack/slice` — Break a full-stack feature into the smallest safe end-to-end increment that can be modeled, wired, tested, and shipped without drift.
- `fullstack/wire` — Plan the screen structure, data binding, and state scaffolding for a full-stack feature once the API contract and data model are known.

## mobile/

- `mobile/adapt` — Adapt mobile implementations for platform-specific behavior, device constraints, OS version differences, and native accessibility APIs across iOS and Android.
- `mobile/bridge` — Map mobile design specs to native and cross-platform code by resolving JS-to-native boundaries, platform API requirements, and mobile-specific implementation constraints.
- `mobile/compose` — Compose mobile screens, components, and interaction states from approved app patterns, tokens, and platform conventions.
- `mobile/ship` — Validate, harden, and release a mobile feature safely with device testing, app store submission checks, OTA update coordination, and mobile-specific rollback planning.

## ml/

- `ml/evaluate` — Design and interpret model, prompt, and retrieval evaluations so we know whether the system is actually good enough to ship.
- `ml/frame` — Turn a machine learning request into a justified problem framing with a baseline, success metric, and failure mode before any model work starts.
- `ml/monitor` — Keep a production model or LLM workflow healthy by watching drift, performance, and business impact after launch.
- `ml/serve` — Turn a validated model or LLM workflow into a production-ready serving path with clear latency, reliability, and rollback expectations.

## implementation/

- `implementation/apply-patch` — Implement approved code changes and write engineering artifacts — tech plan and implementation notes.
- `implementation/figma-get-design-context` — Retrieve full design specs — component structure, properties, tokens, and annotations — from the Figma file before implementing.
- `implementation/chrome-list-console-messages` — Read browser console output to diagnose runtime errors, warnings, and unexpected behavior during implementation verification.

## Additional Skills

- `frontend/frontend-design` — Set design quality standards for frontend interfaces — composition, typography, color, motion, imagery, and copy — with mandatory working model, worked examples, and reject-these-failures checks to avoid generic output.
