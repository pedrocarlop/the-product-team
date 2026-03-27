# Decision: Component System Choice

**Date**: 2026-01-03

**Context**: The product-designer proposed using existing design system components. The frontend-engineer raised that the `StepIndicator` component doesn't exist in the current system and would need to be created.

**Position A (product-designer)**: Create a new `StepIndicator` component in the design system with full token support, so it can be reused across other multi-step flows.

**Position B (frontend-engineer)**: Build a local `StepIndicator` scoped to the onboarding feature to avoid the overhead of a design system PR and review cycle within the sprint timeline.

**Resolution**: The orchestrator sided with Position B (local component) for v1, given the sprint constraint. A follow-up task to promote it to the design system is noted for v2.

**Rationale**: Sprint timeline is the binding constraint. A local component ships faster and can be promoted later without rework risk.
