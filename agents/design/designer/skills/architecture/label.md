---
name: label
description: Design the exact names users see in navigation, facets, headings, and other structural surfaces so each label is distinct, predictable, and usable.
---

# Label

## Purpose

Use this skill to choose the exact words that represent a structure, so users can predict what they will find before they click.

## When to Use

- When you need to name a navigation item, section, category, or facet
- When similar labels are competing with each other or creating ambiguity
- When the user-facing name must be shorter, clearer, or more durable than the internal one
- When a label must work across desktop, mobile, localization, and accessibility contexts

## When Not to Use

- When the main task is defining the underlying taxonomy itself
- When the issue is only a local sentence rewrite with no structural impact
- When the structure has not been settled enough for a stable label decision

## Required Inputs

- The structural element being named
- The user goal associated with that element
- The sibling labels and surrounding hierarchy
- The terms users already use, if known
- Any length, localization, or accessibility constraints

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

1. Identify what the label must help the user understand or do.
2. Compare candidate labels against siblings to avoid overlap or confusion.
3. Prefer user vocabulary over internal vocabulary unless the user term is misleading.
4. Check the label against its container, breadcrumb trail, and next-step destination.
5. Verify that the label still works when shortened, translated, or read out of context.
6. Record the decision with the scope of what it includes and excludes.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Distinct from sibling labels
- Predictable before click or selection
- Short enough for interface constraints
- Consistent with the surrounding taxonomy
- Stable enough to survive product growth

## Output Contract

- The chosen label text
- At least one rejected alternative when useful
- A short rationale for why the final label is clearer or safer
- Inclusion and exclusion notes if the label could be ambiguous

## Examples

### Example 1

Input:
- Internal label: "Initiatives"
- User task: Find ongoing work by topic

Expected output:
- Label note: "Use 'Projects' if users think in terms of bounded work items; keep 'Initiatives' only if that is the dominant user term."
- Rationale: "Initiatives is internal language and does not predict what users will find."

## Guardrails

- Do not pick a label that only makes sense to the team who built it
- Do not let labels vary across screens for the same concept
- Do not optimize for cleverness over predictability
- Do not ignore length and truncation constraints

## Optional Tools / Resources

- User interviews or terminology research
- Card-sort or first-click findings
- Existing navigation audits
- Localization guidance and accessibility checks

