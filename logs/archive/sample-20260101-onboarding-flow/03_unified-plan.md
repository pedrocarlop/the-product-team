# Unified Plan

## Objective
Deliver a guided onboarding flow for the HR portal covering profile setup, team assignment, tool access, and welcome checklist.

## Execution Sequence

### Stage 1: Design (product-designer)
1. Map the onboarding task flow (4 steps + completion)
2. Design screen states for each step (empty, in-progress, complete, error)
3. Specify component usage and design tokens
4. Document mobile responsive behavior

### Stage 2: Implementation (frontend-engineer)
1. Scaffold onboarding route and step components
2. Implement each step with form validation
3. Integrate with existing profile API
4. Implement responsive breakpoints per design spec
5. Add progress indicator and step navigation

### Stage 3: Review (ux-flow-reviewer)
1. Walk through complete flow on desktop and mobile
2. Verify all states render correctly
3. Check navigation edge cases (back, refresh, deep link)
4. Produce review report with pass/fail per criterion

## Dependencies
- Stage 2 depends on Stage 1 deliverables
- Stage 3 depends on Stage 2 completion

## Review Points
- Design review after Stage 1
- Flow review after Stage 2

## Approval Gate
This plan requires user approval before execution begins.
