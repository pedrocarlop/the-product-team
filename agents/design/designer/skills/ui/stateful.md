---
name: stateful
description: "Specify the complete visual state model for a UI surface so every control, container, and feedback area has defined appearance, content, and transition behavior across all interactive and data-driven states. Use when a feature has async moments, many interaction points, or high state variability."
---

# Stateful

## Overview

A "stateful" design defines every visual moment a user might encounter. Good UI is not a static screen; it's a dynamic collection of states: idle, hover, focus, active, loading, empty, success, and error. Without explicit state coverage, engineering must guess how to indicate progress or failures, leading to "broken" or inconsistent user experiences.

## When to Use

- When a new feature or component has a lifecycle (e.g., "Requesting" → "Processing" → "Completed").
- When a UI surface depends on external data that could be missing, slow, or unauthorized.
- When an interaction model requires complex feedback (e.g., multi-file uploads, multi-step forms).
- When a design system's primitive states are insufficient for a custom component's needs.

## When Not to Use

- When a surface's visual treatment is already defined and only layout logic or architecture is being changed.
- When the task is a copy/wording update with no visual state changes.
- When the interaction model is already standard (e.g., a simple native button) and designers only need to point to the system.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Inventory the Stateful Entities

List every UI element on the surface that can change based on data or user interaction:
- **Interactive controls**: Buttons, inputs, links, tabs.
- **Data containers**: Lists, grids, detail panels, charts.
- **Feedback areas**: Toast notifications, inline banners, empty-state placeholders.

### Step 2: Establish the State Matrix

For each entity, define its appearance across the four primary state categories:

| Category | States to Define |
| :--- | :--- |
| **Interactive** | Default, Hover, Focus, Pressed, Active, Disabled |
| **Data-Driven** | Loading (skeleton/shimmer), Empty, Populated, Partial, Unauthorized |
| **Outcome** | Success (confirmation), Error (error message, retry affordance) |
| **Lifecycle** | Initializing, Processing, Stale, Expired |

### Step 3: Reference the Design System

Before creating new visual treatments, check the design system for existing state variants and tokens:
- Use system-defined **Interactive Tokens** for standard hover/focus states.
- Use system-defined **Feedback Tokens** for success (green/positive) vs. error (red/critical) moments.
- Inherit **Global States** (e.g., standard "No results found" pattern) where possible.

### Step 4: Define Visual and Content Transformations

For every state in the matrix, specify:
- **Visual change**: Color shift, opacity, border, iconography, or hidden/visible toggle.
- **Content change**: Placeholder text, error copy, specific instruction, or icon swap.
- **Affordance change**: Is the element interactive? Is it blocked? Does it have a tooltip?

### Step 5: Define State Transitions (Motion Logic)

Identify how states change from one to another:
- **Immediate**: Instant switch for high-urgency feedback.
- **Eased**: Standard fade/slide/scale (e.g., 200ms) for most interactive states.
- **Progressive**: Skeleton screens or shimmers for data-driven loading states.
- **Destructive**: Visual removal or "crunching" of elements.

### Step 6: Verify Accessibility and Stability

Test each state for:
- **Contrast**: Does the error text meet AA standards? Is the disabled state distinguishable enough?
- **Hierarchy**: Does the primary action remain obvious in a "partial success" state?
- **Layout Stability**: Does adding an error message or loading spinner shift the rest of the UI (Layout Shift)?

## Decision Tree: Do I need a State Matrix?

```
Does the UI depend on an asynchronous data fetch?
├── YES → Do you have an "Empty" and "Error" state mapped?
│   ├── NO → Create a State Matrix.
│   └── YES → Is the "Loading" transition defined?
│       ├── NO → Create a State Matrix.
│       └── YES → OK (Skip).
└── NO → Are there more than 3 interactive elements on the page?
    ├── YES → Create a State Matrix.
    └── NO → OK (Manual check only).
```

## Worked Examples

### Example 1: Profile Image Upload

**Input:** A user wants to change their profile photo.
**States:**
- **Idle**: Current photo (or initials) with "Change" button.
- **Selecting**: Native file picker open (no UI change yet).
- **Processing**: Hero image blurred, circular spinner overlay, primary "Save" button disabled.
- **Success**: New image fades in, 1s "Success" toast, return to Idle.
- **Error (File too large)**: "Image is larger than 5MB" inline red text, retry button, "Save" disabled.

### Example 2: Search Results List

**Input:** A real-time filtered list of entries.
**States:**
- **Initial**: Empty state with "Start typing to search" guidance.
- **Loading**: 3-row skeleton shimmer replacing the list area.
- **Populated**: Results displayed with highlighted matches.
- **No Results**: "No matches for 'XYZ'" illustration + "Clear search" link.
- **Partial**: "Showing 50 of 2,400 results" with "Load more" button at bottom.
- **Unauthorized**: "Upgrade to Pro to see all results" banner + blurred list.

## Guardrails

- **Never leave an async moment without a designed treatment.** Engineering should never have to invent a "loading spinner" or "generic alert."
- **Always design for the empty state first.** It is the most frequent first impression.
- **Do not collapse distinct visual states.** "Disabled" and "Error" are not the same; they require different user paths.
- **Always provide a recovery affordance for error states.** State alone isn't enough; the user needs to know how to fix it (e.g., "Retry", "Contact Support").

## Troubleshooting

### Issue: State descriptions are too vague
**Cause**: Using words like "Clean" or "Modern" instead of "Background: --token-brand-primary".
**Solution**: Force usage of design tokens or specific CSS properties (color, opacity, border-radius).

### Issue: Layout shifts during state transitions
**Cause**: Elements are added/removed from the DOM without reserved space.
**Solution**: Define fixed heights or use "ghost" shells that reserve space for error messages or spinners.

### Issue: The UI feels "broken" during slow loads
**Cause**: Missing skeleton screens or meaningful progress feedback.
**Solution**: Apply the "Progressive" transition rule — shimmers are better than blank white space.
