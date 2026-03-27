---
name: gate
description: Evaluate QA evidence against release criteria and decide whether the build is ready to move forward.
---

# Gate

## Purpose

Use this skill to decide whether the current QA evidence is strong enough for the next stage to proceed.

## When to Use

- When a feature needs a release readiness decision
- When test results, bugs, and sign-off notes must be consolidated
- When a build needs a clear pass, conditional pass, or block outcome
- When downstream work should not start until quality evidence is reviewed

## When Not to Use

- When the team still needs a test plan or coverage map
- When the main task is implementing automated checks
- When the release evidence has not been gathered yet
- When the request is only to record exploratory findings

## Required Inputs

- The acceptance criteria or release criteria being checked
- The test results, bug notes, and validation evidence available
- Any known blockers, exceptions, or remaining risks
- The owner or destination for unresolved issues
- Any rules for what counts as a pass, conditional pass, or block

## Workflow

1. Compare the evidence with the stated quality criteria.
2. Separate blocking issues from nonblocking observations.
3. Check whether failures are real product risks or test noise.
4. Decide whether the work passes, passes with notes, or must be blocked.
5. State the exact reasons for the decision in plain language.
6. Assign each blocker to an owner or next action.
7. Record the gate result so the next stage does not have to guess.

## Design Principles / Evaluation Criteria

- Blocking issues must be explicit and actionable
- A gate decision should reflect real risk, not optimism
- Nonblocking notes should stay visible without obscuring the decision
- The next stage should know exactly what remains unresolved
- Pass decisions should be consistent across similar releases

## Output Contract

- Clear gate decision: pass, conditional pass, or block
- Short list of blockers or notes with owners
- Summary of evidence reviewed
- Any follow-up required before the next stage can start

## Examples

### Example 1

Input:
- Artifact: release candidate for a checkout update
- Evidence: integration passed, E2E failed on one edge case, bug filed

Expected output:
- Decision: `block`
- Reason: the failing edge case affects the release criteria
- Next step: fix the bug and rerun the affected checks

## Guardrails

- Do not pass work that still has unresolved blockers
- Do not block on noise that does not change the release risk
- Do not bury the decision inside a long narrative
- Do not skip recording the owner of each real issue

## Optional Tools / Resources

- Test reports and validation summaries
- Bug trackers and review notes
- Release criteria or sign-off checklists
- Workflow-state records
