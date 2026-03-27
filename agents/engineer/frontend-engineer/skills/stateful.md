---
name: stateful
description: Implement the full frontend state model so every component handles loading, empty, error, success, disabled, and transition states with correct data flow, DOM updates, and accessibility attributes.
---

# Stateful

## Purpose

Use this skill to implement the full state model of a frontend surface so every component correctly handles every runtime state. A production UI must manage not just the happy path but every data condition, network outcome, and permission state that can occur.

## When to Use

- When implementing a component or page that must handle idle, loading, empty, success, error, disabled, and partial data states
- When the design spec defines visual states but the implementation logic for state transitions, data fetching, and DOM updates needs to be planned
- When multiple components share state and need coordinated updates during loading, error recovery, or optimistic mutations

## When Not to Use

- When the main issue is visual design or choosing the right appearance for a state (route to UI designer)
- When the task is only to refine copy or microcopy within an already-implemented state
- When the state management architecture is already decided and only a small bug fix is needed

## Required Inputs

- The design spec with defined visual states and expected behavior per state
- The API contract, data shape, and known failure modes that drive state transitions
- The state management approach in use: server state (React Query, SWR), client state (Redux, Zustand, Context), URL state
- Component tree showing where state ownership and data-fetching boundaries live
- Accessibility requirements: ARIA live regions, focus management on state change, disabled attribute semantics
- Performance constraints: debounce, skeleton rendering, optimistic updates, stale-while-revalidate

## Workflow

1. Map each component to the data sources and events that drive its state transitions.
2. Define the state machine or conditional logic for each component: what state it starts in, what triggers each transition, and what the terminal states are.
3. Implement loading states with appropriate skeleton, spinner, or placeholder rendering tied to actual data-fetching lifecycle.
4. Implement error states with specific error type handling, retry logic, and user-facing recovery actions.
5. Handle edge conditions: empty data, partial data, stale cache, permission denial, and network timeout.
6. Wire accessibility attributes: `aria-busy` during loading, `aria-live` for dynamic content updates, `aria-disabled` semantics, and focus management after state transitions.

## Design Principles / Evaluation Criteria

- Every data-driven component must handle the full state lifecycle, not just the populated case
- State transitions must be deterministic: the same inputs should always produce the same rendered output
- Loading states must reflect actual async operations, not arbitrary timers
- Error handling must distinguish between recoverable and terminal errors
- Accessibility attributes must update in sync with visual state changes
- Optimistic updates must have rollback paths when the server response contradicts the assumption

## Output Contract

- Implemented components with explicit state handling for every defined state
- State transition logic documented in code comments or a state diagram
- Error boundary and recovery implementation notes
- Accessibility attribute mapping for each state (ARIA roles, live regions, focus management)
- Test coverage notes: which states are tested and which edge conditions remain
- Known gaps where the API contract or design spec does not fully define the expected behavior

## Examples

### Example 1

Input:
- Surface: File upload panel with multi-file support
- API: POST endpoint returns per-file success/failure; network timeout possible

Expected output:
- State machine: idle -> uploading (per-file progress) -> success/failed (per-file) -> idle (on clear)
- Implementation: Track each file's upload state independently; show retry for failed files; disable submit during active uploads
- Accessibility: `aria-busy="true"` on upload container during upload; `aria-live="polite"` region announces per-file completion; focus moves to retry button on failure
- Error handling: Network timeout after 30s triggers per-file error state with retry; total failure shows banner with "retry all" action

## Guardrails

- Do not render a component without handling what happens when its data is missing, loading, or failed
- Do not collapse distinct error types into one generic error message
- Do not leave async state transitions untested or assume they will always succeed
- Do not implement visual state changes without corresponding accessibility attribute updates
- Do not use `setTimeout` as a substitute for real loading state tied to data-fetching lifecycle

## Optional Tools / Resources

- Design spec with state definitions from the UI designer
- API documentation and error response schemas
- React Query, SWR, or equivalent data-fetching library docs
- Accessibility testing tools: axe-core, screen reader testing
- Storybook for rendering and reviewing each state in isolation
