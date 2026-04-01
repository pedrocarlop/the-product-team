---
name: flow
description: "Design task flows that cover entry points, happy paths, alternates, errors, empty states, recovery, and completion for a product experience. Use when mapping a new user journey, refactoring complex branching, or documenting state-dependent transitions."
---

# Flow

## Overview

A flow maps the user's movement through a product experience. It visualizes the logic, decisions, and states that occur between an initial entry point and a final goal. A poor flow captures only the "happy path," leaving engineers to guess how to handle interruptions, errors, and data-less states.

## When to Use

- When a new feature has multiple steps, decisions, or dynamic states.
- When an existing journey feels broken, confusing, or logically incomplete.
- When the team needs to align on service-layer logic before designing screen-level UI.
- When mapping recovery paths for errors, timeouts, or permission denials.

## When Not to Use

- When the task is a single-screen layout or hierarchy fix with no branching.
- When the journey is already established and only visual polish is needed.
- When the problem is technical implementation detail with no user-facing logic changes.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Define Entry Points and Intent

Start with why the user is here:
- **Source**: Where did they come from? (e.g., deep link, settings menu, toast notification).
- **Context**: What is the system state? (e.g., logged in, expired trial, first-run).
- **Intent**: What single thing are they trying to accomplish? (e.g., "delete team", "update billing").

### Step 2: Map the Happy Path

Define the shortest, most successful sequence of actions from Entry to Completion.
- Avoid detailing UI components yet; focus on **logic nodes**:
  - `Action` (User does X)
  - `System Response` (Result of X)
  - `Decision` (Choice A vs B)

### Step 3: Identify Alternates and Interruptions

For every step in the Happy Path, ask:
- "What if the user changes their mind or clicks away?"
- "What if a different choice is valid here?"
- "What if a prerequisite is missing (e.g., payment method) at this specific moment?"

### Step 4: Map Error and Recovery Loops

For every `Action` or `System Response`, identify failure points:
- **System Failure**: Timeout, 500 error, network loss.
- **Validation Failure**: Invalid input, business rule violation (e.g., name already taken).
- **State Failure**: Conflict (e.g., record already deleted by another user).

**Mandatory Recovery rule**: Every error node must lead somewhere — either back to a previous state for correction or to a clear exit path. Never leave the user at a dead end.

### Step 5: Incorporate Empty and Loading States

Identify moments of latency or data absence:
- **Loading state**: While the system processes a logic node.
- **Empty state**: When a list, dashboard, or container has no data to display after the flow starts.

### Step 6: Verify the Exit Nodes

Explicitly define how the flow ends:
- **Success**: Goal reached, visual confirmation provided.
- **Cancellation**: User opted out, system returned to a stable previous state.
- **Failure**: Goal unreached, user informed, transition to a relevant support/fallback surface.

## Decision Tree: Is this a Flow task?

```
Does the task involve more than one user decision or system state change?
├── YES → Use this skill.
└── NO → Is there a possibility of failure or interruption?
    ├── YES → Use this skill.
    └── NO → Use a UI/Screen-specific skill instead.
```

## Worked Examples

### Example 1: Workspace Invite Flow

**Input:** Feature to invite teammates via email.
**Actions:**
1. **Entry**: "Invite" button on Team Settings.
2. **Step 1 (Input)**: User enters email(s).
   - *Alternate*: Bulk upload from CSV.
3. **Step 2 (Validation)**: System checks if email is valid and workspace has capacity.
   - *Error*: Invalid email → Show inline error, stay at Step 1.
   - *Error*: No capacity → Show upgrade prompt, exit flow.
4. **Step 3 (Action)**: User clicks "Send Invites".
   - *Loading*: "Sending..." state.
5. **Step 4 (Success)**: Confetti + toast notification, return to Team Settings.

### Example 2: Subscription Cancellation

**Input:** Hard user journey to cancel a paid plan.
**Actions:**
1. **Entry**: Cancellation link hidden in Billing.
2. **Step 1 (Retention)**: "Why are you leaving?" survey.
   - *Interruption*: User clicks "Stay and get 20% off" → Transition to Success exit.
3. **Step 2 (Friction)**: "Are you sure? You will lose access to X, Y, Z."
4. **Step 3 (Action)**: Confirm cancellation button click.
5. **Step 4 (Completion)**: Visual feedback of pending cancellation, redirect to Plan Overview.

## Guardrails

- **Never model only the happy path.** This is the primary cause of product "dead ends."
- **Always define an exit path for every error.** Dead ends are non-negotiable failures.
- **Do not collapse distinct states.** A "loading error" is different from a "permission error." Keep them mapped separately if they require different user actions.
- **Use generic terms for UI elements.** (Use "Selection" instead of "Checkbox" to avoid premature design fixating).

## Troubleshooting

### Issue: Flow becomes too complex (Spaghetti)
**Cause**: Too many branches or attempts to map a whole app in one file.
**Solution**: Decompose. Break the flow into "Sub-flows" (e.g., "Registration" → "Onboarding" → "Activation"). Use references to link them.

### Issue: Specialist maps UI details instead of logic
**Cause**: Jumping to "how it looks" before "how it works."
**Solution**: Strip out CSS/Component mentions. Force the mapping into `Logic Nodes` (Action/System/Decision).

### Issue: Missing recovery paths
**Cause**: Optimistic bias.
**Solution**: Review every system response and ask "What if this fails?" If the answer isn't mapped, the flow is incomplete.
