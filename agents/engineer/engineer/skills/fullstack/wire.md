---
name: wire
description: Plan the screen structure, data binding, and state scaffolding for a full-stack feature once the API contract and data model are known.
---

# Wire

## Purpose

Use this skill to plan how a full-stack feature maps to screens, data flows, and component structure so implementation can begin with clear boundaries between frontend rendering, API calls, and state management.

## When to Use

- When the API shape and data model are known and the UI implementation needs to be planned
- When you need to decide which data loads where, what triggers fetches, and how state flows between components
- When loading, error, empty, and optimistic-update states must be designed into the component tree before coding starts

## When Not to Use

- When the API contract or data model is still being decided
- When the request is for visual design, branding, or design system decisions
- When the work is only about backend logic, database schema, or deployment

## Required Inputs

- The API contract, data model, or feature slice that drives the UI
- Any existing screens, mocks, or wireframes from design
- The component library and framework conventions in use
- State requirements: loading, empty, error, success, disabled, and optimistic update
- Auth, permission, and data-fetching constraints that affect rendering
- Known performance constraints such as pagination, lazy loading, or bundle size

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

1. Map each screen to the API endpoints and data entities it depends on.
2. Define the component tree and decide where state lives: server state, client state, URL state, or derived.
3. Identify data-fetching boundaries and decide what loads eagerly, lazily, or optimistically.
4. Specify how each component handles loading, error, empty, and stale-data conditions.
5. Draft the responsive layout structure and note where server-rendered versus client-rendered boundaries apply.
6. Annotate implementation decisions that affect backend contract expectations or require API changes.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Data flow clarity before visual polish
- Each component should have a single clear data responsibility
- State management boundaries should be explicit and minimal
- Loading and error states must be first-class implementation concerns, not afterthoughts
- The plan should be specific enough to code against, but flexible enough to adjust during review

## Output Contract

- A screen-to-API mapping showing which endpoints feed which views
- Component tree or structure sketch with state ownership annotations
- Data-fetching and state-management notes for each major section
- State handling specs for loading, error, empty, and edge conditions
- Implementation notes on auth gating, permission checks, and render boundaries
- Open questions about API contract gaps or missing backend support

## Guardrails

- Do not add visual design decisions that belong to the designer
- Do not leave data-fetching strategy implicit when components have complex dependencies
- Do not plan component structure without considering the real API response shape
- Do not ignore auth, permission, or error states that will materially change the rendered output

## Optional Tools / Resources

- Existing design system components and layout patterns
- API documentation, OpenAPI specs, or GraphQL schemas
- Product screenshots or prototypes from design
- Device and breakpoint constraints
- Framework documentation for state management and data fetching
