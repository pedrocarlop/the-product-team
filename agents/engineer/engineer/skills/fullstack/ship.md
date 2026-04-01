---
name: ship
description: Validate, harden, and release a full-stack feature safely with end-to-end tests, API and UI verification, migration sequencing, and observability across the entire request path.
---

# Ship

## Purpose

Use this skill to turn an implemented full-stack feature into a safe production release by verifying the complete request path from frontend through API to database, confirming rollout safety, and ensuring observability covers both client and server.

## When to Use

- When code is complete across frontend and backend and the remaining work is validation and rollout
- When a database migration, API change, and UI update must be deployed in the right order
- When end-to-end test coverage, cross-layer observability, or rollback planning must be tightened before release

## When Not to Use

- When the feature contract or API design is still changing
- When the work is only about modeling, slicing, or wireframing
- When the feature lives entirely in one layer and does not cross the stack

## Required Inputs

- The implemented API endpoints, UI changes, and data migrations
- Test results across unit, integration, and end-to-end layers
- Feature flag configuration and deployment sequence constraints
- Database migration plan: forward migration, backward compatibility, and rollback SQL
- Observability setup: API latency metrics, error rates, client-side error tracking, and alerting

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: engineer
project: <slug>
deliverable: engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Verify the implemented behavior end-to-end: frontend calls the correct API, API returns the expected shape, database state is consistent.
2. Confirm test coverage across layers: unit tests for business logic, integration tests for API contracts, and end-to-end tests for critical user paths.
3. Validate deployment sequencing: can the migration run before the API deploy? Can the old UI work with the new API during rollout?
4. Check that feature flags gate both the frontend surface and the API behavior so partial rollout is safe.
5. Confirm observability: API latency and error metrics, client-side error tracking, database query performance, and alert thresholds.
6. Document the rollback plan: which deploy to revert first, whether the migration is reversible, and what data state to expect after rollback.
7. State the release criteria and the specific signals that would trigger a rollback.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- A feature is not shipped until the full request path is verified, not just individual layers
- Deployment order matters: migrations, API, and frontend must be sequenced to avoid breaking intermediate states
- Rollback must be tested or at minimum documented for each layer independently
- Observability must cover the new path specifically, not rely on general dashboards
- Cleanup of temporary flags, dual-write logic, and compatibility shims should be scheduled at ship time

## Output Contract

- A release-readiness summary covering frontend, API, and data layer status
- End-to-end test and validation evidence for critical paths
- Deployment sequence with migration, API, and frontend ordering
- Rollout plan: flag configuration, percentage ramp, and canary criteria
- Rollback plan per layer with expected data state after reversal
- Cleanup backlog: flags to remove, temporary compatibility code to delete, monitoring to adjust

## Guardrails

- Do not treat passing unit tests as release readiness when the feature crosses layers
- Do not ship database migrations without confirming backward compatibility during rollout
- Do not deploy frontend changes that depend on an API change before the API is live
- Do not leave temporary feature flags or dual-write logic untracked after launch

## Optional Tools / Resources

- MCP: GitHub MCP, Chrome DevTools MCP, Notion MCP, Sentry MCP, Postman MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [Node.js Docs](https://nodejs.org/en/docs), [React Docs](https://react.dev/), [PostgreSQL Docs](https://www.postgresql.org/docs/), [Postman Learning Center](https://learning.postman.com/)
- CI pipeline output and test reports
- Database migration tooling and rollback scripts
- Feature flag management dashboard
- APM and error tracking dashboards
