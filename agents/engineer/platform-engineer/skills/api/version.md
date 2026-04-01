---
name: version
description: Define API versioning, compatibility, and deprecation strategy so contract changes are deliberate and consumer impact is controlled.
---

# Version

## Purpose

Use this skill to decide how an API should evolve across versions without surprising consumers or creating unnecessary version churn.

## When to Use

- When a contract change could affect existing consumers
- When a new major version is being considered
- When fields, enums, paths, behaviors, or auth requirements are changing
- When deprecation, sunset dates, or migration guidance needs to be planned

## When Not to Use

- When the task is only about modeling endpoints or schemas for the first time
- When you are validating an existing design against HTTP or OpenAPI rules
- When the task is strictly about writing examples or publishing documentation

## Required Inputs

- The current contract and the proposed change
- A list of known consumers, if any
- The expected lifespan of the endpoint or resource
- Any current versioning conventions already in use
- The business timeline for rollout, deprecation, and migration

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Classify the change as additive, behavioral, compatibility-sensitive, or breaking.
2. Check whether the change can be expressed without a new version.
3. If versioning is needed, choose the least disruptive version strategy that still gives consumers a clear migration path.
4. Define deprecation and sunset timing only after consumer impact is understood.
5. Write down migration guidance that makes the old and new contracts easy to compare.
6. Confirm that the version strategy matches the team’s long-term support expectations.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Additive changes should not force a new major version
- Breaking changes deserve explicit migration planning
- Version inflation creates avoidable consumer burden
- Deprecation should be visible, predictable, and time-bound
- Compatibility decisions should be based on real consumer behavior, not guesswork

## Output Contract

- Versioning decision with rationale
- Compatibility assessment of the proposed change
- Deprecation and sunset plan, if applicable
- Migration notes that highlight what consumers must change

## Examples

### Example 1

Input:
- Add a new optional `deliveryInstructions` field to an order response

Expected output:
- No new major version
- Note that the change is additive and backwards-compatible
- Document that the field is optional and safe for existing consumers to ignore

## Guardrails

- Do not introduce a new version for additive changes
- Do not hide breaking changes behind a minor release number
- Do not set deprecation dates without a migration path
- Do not assume consumers can absorb change just because the implementation can

## Optional Tools / Resources

- Existing versioning policy
- Consumer inventories or API catalogs
- Changelogs, release notes, and migration guides
- Contract diff tools or change-review notes
