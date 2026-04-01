---
name: verify
description: Verify that accessibility fixes and specs actually work through manual checks, assistive technology testing, and repeatable acceptance criteria.
---

# Verify

## Purpose

Use this skill to confirm that accessibility requirements were implemented correctly and that the user experience is actually usable with the intended assistive technologies.

## When to Use

- When a fix needs to be checked before approval or release
- When you need to confirm that a specification was implemented faithfully
- When you need to re-test a previously identified issue after changes land
- When you need a repeatable checklist for accessibility acceptance

## When Not to Use

- When the task is to find undiscovered accessibility problems
- When the task is to annotate a design for handoff
- When the task is to rework the interface to make it more accessible

## Required Inputs

- The changed design, prototype, or implementation
- The original accessibility requirement or issue being verified
- The expected keyboard, screen reader, focus, or contrast behavior
- The device, browser, or assistive technology in use
- Any acceptance criteria or pass/fail threshold

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: designer
project: <slug>
deliverable: designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Revisit the original requirement so the verification matches the actual fix.
2. Test the path that was changed, not just the happy path around it.
3. Confirm keyboard reachability, focus order, and visible focus states.
4. Check semantics and announcements in the accessibility tree or with a screen reader.
5. Recheck contrast, motion, and state communication in the final rendered UI.
6. Compare the observed behavior with the expected outcome and note any regressions.
7. Record whether the item passes, fails, or needs a follow-up fix.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Verification should be concrete and repeatable
- Passing means the user can complete the task, not just that a tool reported no issues
- Manual testing is required for behaviors automated tools cannot see
- A verification pass should leave no ambiguity about what was tested

## Output Contract

- Clear pass/fail result for the accessibility requirement
- Test context: device, browser, and assistive technology used
- Notes on observed behavior and any remaining gaps
- Follow-up actions if the requirement is not fully met

## Examples

### Example 1

Input:
- Fix: Modal focus management
- Requirement: Focus should move into the modal on open and return to the trigger on close

Expected output:
- Verification result: Pass
- Notes: Focus lands on the modal heading when opened, tab order stays trapped inside the modal, and focus returns to the open button when closed

## Guardrails

- Do not mark a fix as verified without testing the changed behavior directly
- Do not rely solely on automated scanners for dynamic or assistive-technology behavior
- Do not widen the scope beyond the original requirement unless a new regression is discovered
- Do not treat an implementation as verified if the interaction still fails under keyboard or screen reader use

## Optional Tools / Resources

- Keyboard-only walkthroughs
- Axe or similar automated accessibility checks
- Screen readers such as NVDA or VoiceOver
- Browser accessibility tree inspection
- Design or implementation acceptance criteria
