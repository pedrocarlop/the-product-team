---
name: critique
description: "Evaluate a design through structured heuristic analysis, scoring usability across cognitive load, discoverability, affordance, and error prevention to produce actionable findings. Use when reviewing wireframes, prototypes, or implemented frontend screens."
---

# Critique (Usability Review)

## Overview

"Critique" replaces subjective design opinions ("I don't like this color") with objective, heuristic-grounded evaluation. A strong usability critique identifies barriers that prevent users from reaching their goals, scores their severity, and traces failures back to established human-computer interaction principles (e.g., Nielsen's Heuristics).

## When to Use

- When a designer submits wireframes, flows, or high-fidelity UI for team review.
- When auditing an existing, legacy screen for friction or high drop-off rates.
- When evaluating if a complex technical requirement was translated well into the UI.
- When standardizing UI components against accessibility or usability norms.

## When Not to Use

- When the task requires validating the underlying business requirements or product strategy.
- When reviewing backend APIs or non-visual systems.
- When generating original designs from scratch (use a `designer` skill).

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Align on the Primary Task and Persona

Identify what the critique is measuring against:
- "Can an *enterprise administrator* successfully *bulk-delete user accounts*?"
- "Can a *first-time mobile user* complete *checkout* in under 3 minutes?"

### Step 2: Execute the Heuristic Sweep

Evaluate the design against standard usability heuristics. Look explicitly for:
- **Discoverability**: Can the user clearly see the primary action?
- **Cognitive Load**: Is the user forced to memorize information from previous screens? (Recognition over Recall).
- **System Status**: Is the system providing immediate feedback (loading, success, error)?
- **Consistency**: Are patterns used identically here as they are elsewhere in the app?

### Step 3: Stress-Test Affordances and Error Prevention

Analyze the physical and destructive interactions:
- **Affordance**: Does a button look clickable? Does a disabled element clearly explain *why* it is disabled?
- **Error Prevention**: Are destructive actions safeguarded (e.g., confirmation modals, required typing)?
- **Recovery**: If an error occurs, does the UI provide a clear, actionable path to fix it?

### Step 4: Rank Findings by Severity and Frequency

Do not list 50 equal issues. Categorize them:
- **Critical/Blocker**: Prevents task completion. Must fix.
- **High**: Major friction or high probability of error.
- **Medium**: Annoyance or cognitive strain.
- **Low**: Polish or minor visual inconsistency.

### Step 5: Deliver Actionable Recommendations

For every finding, provide: `[The Flaw]` + `[The Broken Heuristic]` + `[The Suggested Fix]`.

## Decision Tree: Is the Critique Objective?

```
Is the finding grounded in a usability heuristic or accessibility standard?
├── YES → Does it evaluate a specific element or flow?
│   ├── YES → Is there a concrete, actionable fix suggested?
│   │   ├── YES → The critique is valid.
│   │   └── NO → Provide a fix (Step 5). Saying "this is bad" is insufficient.
│   └── NO → Narrow the scope. Don't say "the page is busy." Say "the 3 sidebars distract."
└── NO → Discard the finding. Personal preference is not a design critique.
```

## Worked Examples

### Example 1: Critiquing a Destructive Settings Panel

**Input:** A settings page with a red "Delete Account" button next to "Save Changes."
**Workflow Application:**
- **Primary Task**: User updating their email address safely.
- **Heuristic Sweep**: Violates *Error Prevention*. The proximity of a destructive action to a primary action is dangerous.
- **Severity**: High (Accidental deletion is catastrophic).
- **Recommendation**: "Move 'Delete Account' into a separated 'Danger Zone' section at the bottom of the page, and require the user to manually type 'DELETE' to confirm."

### Example 2: Critiquing a Data-Heavy Dashboard

**Input:** A reporting dashboard that shows raw UUIDs instead of User Names.
**Workflow Application:**
- **Primary Task**: Admin identifying highly active users.
- **Heuristic Sweep**: Violates *Recognition over Recall*. A human cannot parse UUIDs easily.
- **Severity**: Medium (Creates friction, forces tab-switching).
- **Recommendation**: "Resolve the UUIDs to human-readable 'First/Last Name' strings, and place the UUID in a secondary tooltip or copy-to-clipboard icon."

## Guardrails

- **Never use "I like" or "I feel" language.** Use "This violates [Heuristic]" or "This increases cognitive load."
- **Always provide a specific fix.** A critique without a proposed solution is just complaining.
- **Do not evaluate visual aesthetics (brand colors, illustration style) unless it directly impacts usability (e.g., contrast accessibility).**

## Troubleshooting

### Issue: The designer is defensive about the critique
**Cause**: The critique attacked the author or focused on subjective opinions.
**Solution**: Relentlessly anchor feedback to the *User Task* and the *Established Heuristics*. Evaluate the artifact, not the designer.

### Issue: The critique list has 40 minor issues but misses blockers
**Cause**: The reviewer got distracted by pixel alignment instead of checking the user flow.
**Solution**: Enforce Step 1. You must walk through the *Primary Task* start-to-finish before critiquing padding or font sizes.

### Issue: The critique asks for changes that violate the design system
**Cause**: The reviewer evaluated the screen in a vacuum.
**Solution**: Always check the proposed fix against global Design System tokens and components. If the system is flawed, propose a system update, not a local override.
