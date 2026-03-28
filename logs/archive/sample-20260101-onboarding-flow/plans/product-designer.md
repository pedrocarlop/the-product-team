# Product Designer Plan

**Objective**: Design the onboarding flow UX and component specs.

**Constraints**:
- Use existing design system tokens and components unless a gap is proven
- Keep the core flow understandable on mobile first
- Support reduced-motion behavior for onboarding progress changes

**Assumptions**:
- 4 onboarding steps based on HR brief
- Existing design system components cover most needs
- Mobile-first responsive approach

**Scope**: Task flow mapping, screen and state design for all 4 steps, component token specification, responsive breakpoint documentation, progress motion specification, and error/recovery behavior.

**Non-scope**:
- Backend data contract changes
- Net-new design-system primitives unless the existing system cannot represent the approved layout or states

**Implementation approach**:
- Keep the flow linear and legible: one primary task per step, one persistent progress affordance, and clear completion criteria.
- Reuse existing form, checkbox, and card patterns, but create a local `StepIndicator` spec for this feature if the design system lacks one.
- Specify every state needed for implementation: first visit, partial progress, validation error, success, and revisit after completion.
- Define progress motion as guidance, not decoration, so the user can tell which step changed without slowing the task down.

**Steps**:
1. Map end-to-end task flow with entry/exit conditions per step
2. Design screen layouts for desktop and mobile, including the compact mobile progress treatment
3. Define all states per screen: empty, partial, complete, validation error, and resumed-in-progress
4. Specify components with design tokens, variants, content rules, and validation behavior
5. Define progress and step-transition motion, including reduced-motion fallbacks
6. Document exceptions, edge cases, and implementation notes for engineering

**Deliverables**: `deliverables/product-designer.md`

**Dependencies**: HR checklist content, existing design system tokens.

**Validation / acceptance criteria**:
- Each step has explicit completion rules and a visible incomplete or error state
- Mobile and desktop layouts preserve the same task order and progress comprehension
- Step changes are perceivable without relying on color alone
- Reduced-motion mode preserves progress feedback without large-area movement

**Risks**:
- Mobile breakpoints may require new design system tokens if existing ones don't cover the layout
- Progress motion could become decorative unless tied tightly to step completion and focus changes

**Critical details that must survive merge**:
- `StepIndicator` is a local v1 component with 4 steps, labels visible on desktop, compact dots plus current-step label on mobile.
- On successful step completion, the current step segment fills over 180ms ease-out, the next step label fades in over 120ms after a 40ms delay, and keyboard focus moves to the next step heading.
- Reduced motion removes the fill animation and label fade; the next step state updates instantly while focus still advances.
- Validation errors stay inline under the field, and the step indicator never animates forward until the step is actually valid.
- Desktop layout keeps the progress rail sticky beside the card; mobile moves progress above the card with no horizontal scroll.

**Status**: Complete.
