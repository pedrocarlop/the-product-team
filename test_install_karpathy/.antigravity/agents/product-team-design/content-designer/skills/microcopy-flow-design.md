---
name: microcopy-flow-design
description: Applies Torrey Podmajersky's Strategic UX Writing method, the STEM framework (Situation, Task, Expectation, Message), and Jobs-to-be-Done copy framing to produce a flow-level microcopy set — covering every screen, state, and decision point in a user flow with consistent voice, vocabulary, and sequencing logic.
trigger: When a feature or flow needs coherent UX writing — including new flows, redesigned flows with stale copy, flows with inconsistent nomenclature, or any surface where copy ambiguity is causing user drop-off or support volume.
mesh:
  inputs:
    - product-designer:wireframe-structure
  next:
    - ui-designer:screen-production-design
  context: "Ensures all user-facing strings are strategically mapped and consistent."
required_inputs:
  - the flow to be written (name, entry point, exit point, and key steps)
  - the user job or goal the flow supports (what the user is trying to accomplish)
  - any existing copy, design files, or content audits for the flow
  - the product's voice and tone guidelines or vocabulary list when available
  - the platform and interface context (web, mobile, native, email, etc.)
recommended_passes:
  - Pass 1 — Flow model construction: map every step, decision point, system state, and transition before writing a word
  - Pass 2 — Copy inventory: audit all existing copy in the flow; identify gaps, inconsistencies, and missing states
  - Pass 3 — STEM framing per step: apply Situation, Task, Expectation, Message to each screen
  - Pass 4 — Copy writing and nomenclature check: write all copy, verify label consistency across steps
  - Pass 5 — Error, loading, and empty state coverage: ensure supporting states are covered
tool_stack:
  runtime:
    primary: figma, notion
    secondary: zeroheight, lokalise
  testing:
    primary: maze
    secondary: optimal_workshop
  fallback:
    primary: search_query, reference/ground
tool_routing:
  - if: design files exist in Figma with annotated screens
    use: figma to read the flow structure, layer names, and existing copy annotations before writing
  - if: a style guide or content design system is maintained in Zeroheight
    use: zeroheight to extract voice principles, vocabulary rules, and approved terminology before writing any copy
  - if: the product uses string-based localization or i18n
    use: lokalise to pull existing string keys, check for string reuse, and flag any copy that will require translation and must stay within character limits
  - if: validated copy is required before shipping (e.g., key CTA or error message)
    use: maze for first-click tests or copy tests; use optimal_workshop for card sorting when nomenclature is uncertain
  - if: copy decisions need to be documented and shared with stakeholders or developers
    use: notion for the deliverable; use figma annotations for in-context handoff
  - if: figma is unavailable or the flow only exists as a written spec
    use: reconstruct the flow model from the written spec or product brief; label evidence path as structured-artifact
  - if: all primary tools are unavailable
    use: search_query and reference/ground; produce best-guess output labeled as inferred
best_guess_output: A flow-level microcopy set organized as a step-by-step copy table — with screen name, copy element type, proposed copy, STEM rationale, and voice rule applied — covering all reachable states in the flow. Labeled as inferred where no primary tool access exists.
output_artifacts:
  - knowledge/runs/<run-id>/content-designer-microcopy-flow-design.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: Every step in the flow has copy for all reachable states (default, loading, error, empty, success), copy is internally consistent in terminology and voice, all decision points have clear action labels, and the flow can be navigated without ambiguity by a first-time user.
---

# Microcopy Flow Design

## Purpose

This skill produces a complete, flow-level microcopy set — every user-facing string across every reachable state in a product flow — using structured UX writing methods anchored to Torrey Podmajersky's Strategic UX Writing framework, the STEM (Situation, Task, Expectation, Message) framework, and Jobs-to-be-Done copy framing.

Reasoning type: constructive — the agent builds a flow model first, then applies copy frameworks to each node in the model, then checks output for internal consistency before finalizing.

Methods anchored to:
- **Torrey Podmajersky's Strategic UX Writing** (voice, tone, vocabulary, sequencing — copy serves product strategy, not personal style)
- **STEM framework** (Situation, Task, Expectation, Message — four-part test for every piece of copy)
- **Jobs-to-be-Done copy framing** (copy is written from the perspective of what the user is hired to do, not what the system is doing)
- **Flow-level copy mapping** (step-by-step copy table that covers the full flow, not isolated strings)
- **Nomenclature consistency checking** (every label, noun, and action verb is audited for consistency across steps)

This skill does NOT: make product decisions about what a flow should do, design the interaction model, write marketing copy or long-form content, conduct user research, or finalize copy without accounting for the full flow context.

---

## Required Inputs and Assumptions

**Required:**
- The flow to be written: name, entry point, exit point, and a list of known steps or screens
- The user job or goal the flow supports (the JTBD frame — what is the user trying to accomplish?)
- Any existing copy, design files, content audits, or written specs for the flow
- Platform and interface context (web app, native iOS/Android, transactional email, voice, etc.)

**Optional but high-value:**
- Voice and tone guidelines or style guide reference
- Approved vocabulary list or nomenclature glossary
- Character limits for UI strings (especially for mobile or localized surfaces)
- Known user pain points or support tickets related to copy confusion in this flow

**Known vs unknown at copy time:**
- Known: the steps the user takes, the system states that can occur, the outcome the flow is designed to produce
- Often unknown: final microcopy approved by legal or compliance, localization constraints, final character limits per component type
- Often uncertain: the exact vocabulary the target user uses for product concepts (requires research or A/B validation to confirm)

**Assumption rule:** If voice guidelines do not exist, infer voice principles from existing product copy (from Figma, production, or documentation). Label any inferred voice rule as `Inferred from existing copy` and note it in the Voice Rules section. If JTBD framing is absent, write a provisional job statement — `User job (assumed): [statement]` — and anchor all copy to it.

---

## Input Mode and Evidence Path

Declare the evidence path used before writing any copy. Options:

1. **Live / real interaction** — Clicking through the actual product flow in a real session. Highest fidelity; captures system behavior, transition timing, and existing string values in context.
2. **Structured system access** — Figma files with annotated screens, Zeroheight style guide, Lokalise string library. Best balance of coverage and speed for most engagements.
3. **Design artifacts / documentation** — Written specs, PRDs, flow diagrams, user story maps. Sufficient for flow model construction; may lack final screen-level copy detail.
4. **Screenshots / static input** — Exported screens, recorded walkthroughs, or images shared by stakeholders. Limited to visible states; loading, error, and empty states may not be represented.
5. **Inference** — Flow model constructed from memory, conversation, or brief description. No design file access. Must label all copy output as `inferred`. Flag for review before implementation.

**Declare the evidence path in the `### Flow model` section of the deliverable.**

---

## Tool Stack

**Runtime primary — Figma**
Read design files to extract: the flow structure (frame order, connections), existing copy values on each layer, component labels, annotation notes, and any content placeholders. Figma is the source of truth for copy-in-context. Use for every pass where design files are available. The Figma MCP allows reading design context directly. Paid plans required for full component and variable inspection.

**Runtime primary — Notion**
The deliverable writing environment. Structure the step-by-step copy table, voice rules, STEM rationale, and recommendations here. Notion databases can also serve as a living copy registry — one row per string, with fields for screen, state, proposed copy, STEM analysis, status, and developer handoff key. Free tier sufficient for deliverable writing; team plans needed for collaborative review.

**Runtime secondary — Zeroheight**
Design system documentation platform that houses style guides, component copy guidelines, and voice and tone principles. Use to pull approved terminology, banned words, tone modifiers by context, and character limits per component type. Essential for ensuring microcopy complies with any established content design system. Paid plans required; typically owned by design system team.

**Runtime secondary — Lokalise**
Translation management and string localization platform. Use when the product ships in multiple locales or when strings are managed as keys in a codebase. Lokalise surfaces existing string keys, character limit constraints per locale, and approved translations — all of which constrain what copy can be proposed. Relevant for any product with i18n requirements. Paid SaaS; per-seat or per-project pricing.

**Testing — Maze**
Unmoderated usability and copy testing platform. Run first-click tests to validate whether CTA labels send users to the right next step. Run preference tests to compare copy variants on key decision-point messages. Maze provides quantitative results (click rate, time-to-first-click, preference %) from real users without researcher moderation. Paid plans required for most test types; free tier limited to basic tests.

**Testing — Optimal Workshop**
Suite of UX research tools including Treejack (information architecture testing), OptimalSort (card sorting), and Chalkmark (click testing). Use when copy decisions involve labeling a navigation structure, categorizing objects, or testing whether users understand a noun or concept. Useful for nomenclature validation before finalizing vocabulary in the copy table. Paid SaaS.

**Fallback — search_query, reference/ground**
Use for method reference (STEM framework lookup, Podmajersky examples), voice pattern benchmarking against competitor products, or copy inspiration when no design artifacts are available. Always label fallback output as `fallback` and note the limitation.

---

## Tool Routing

- Design files exist in Figma → read the flow structure and existing copy from Figma before writing anything. Do not reconstruct the flow from memory if Figma is available.
- Style guide or content system exists in Zeroheight → extract voice principles and approved vocabulary before the copy table pass. Any copy that contradicts Zeroheight guidance must be flagged.
- Product uses string keys or ships in multiple locales → check Lokalise for existing keys and character constraints before proposing new strings.
- CTA copy or key decision-point messages require validation before shipping → use Maze first-click or preference tests.
- Nomenclature or information architecture labeling is uncertain → use Optimal Workshop card sort or Treejack before finalizing vocabulary.
- Copy is being handed off to engineering → use Notion for the structured deliverable; annotate in Figma for in-context developer reference.
- Figma unavailable, flow exists only as written spec → reconstruct flow model from spec; label evidence path as `structured-artifact`.
- No tools available → produce best-guess output from flow description; label all copy as `inferred`; explicitly flag for human review before implementation.
- Never route to a single tool for the full pass. The strongest output combines Figma (flow context) + Notion (structured deliverable) + Zeroheight (voice compliance) + at minimum one testing tool for highest-risk copy decisions.

---

## Environment and Reproducibility

Record the following in the deliverable when known:

- **Platform and interface:** which surface the copy lives on (web app, native iOS, Android, email, push notification, voice). Copy constraints — character limits, truncation behavior, line breaks — are platform-specific.
- **Auth state:** copy often differs for signed-in vs. signed-out states. Declare which state the flow covers.
- **Design file version:** Figma file URL and version (use version history timestamp). UI copy in design files changes; the copy table must reference a specific version.
- **Locale scope:** is this copy for a single locale or is it the source string for translation? If source string, note which locale and any character limits imposed by translation expansion.
- **Voice guide version:** note the version or date of any voice/tone guide used. Voice guidelines evolve; copy written to an outdated guide may require revision.
- **String key reference:** if Lokalise or another string management tool is in use, note the key namespace and any keys that were reused vs. newly proposed.

---

## Model Building

The agent MUST construct a flow model before writing a single word of copy. Copy written without a flow model will be incoherent at the flow level — locally reasonable strings that contradict each other across steps.

### Flow model components

**1. Step inventory**

List every step, screen, or UI milestone in the flow in sequence. Assign each a step ID (S01, S02, …). For each step, note:

```
| Step ID | Step name          | Entry trigger         | Exit trigger              |
|---------|--------------------|-----------------------|---------------------------|
| S01     | [screen/step name] | [what brings user here] | [what moves user forward] |
```

**2. Decision points**

Identify every step where the user must make a choice, confirm an action, or select between paths. Decision points require copy that clearly labels each option and its consequence. List them separately.

**3. System states per step**

For each step, enumerate all reachable system states. Default to this checklist:

- Default (loaded, no user action yet)
- Loading / processing (system is working)
- Success / completion
- Error — user error (recoverable, user caused)
- Error — system error (unexpected, not user-caused)
- Empty state (no data, first use, or zero results)
- Disabled state (if applicable — action exists but cannot be taken yet)

**4. Transitions**

Note what copy or system message marks the transition between steps (e.g., a confirmation message, a toast, a redirect, an email trigger). These are often missed and cause copy gaps.

**5. Voice context per step**

Note the emotional context at each step: Is the user anxious? Confident? In a hurry? Just succeeded? Copy tone must be calibrated to the emotional register of the moment, not uniform across the flow.

No copy may be written before the flow model (steps 1–5) is complete.

---

## Core Method Execution

Follow this sequence strictly. Do not skip steps or write copy before the required model is built.

**Step 1 — Establish the JTBD frame**

Write one job statement for the flow using the JTBD format:
`When [situation], I want to [motivation], so I can [expected outcome].`

This anchors all copy decisions. Every string in the flow should help the user make progress toward this job. If a string does not serve the job, question whether it is necessary.

**Step 2 — Build the flow model**

Follow the model-building section above. Produce the step inventory, decision point list, state matrix, transition map, and voice context notes. Declare the evidence path.

**Step 3 — Run the copy inventory**

For each step in the flow model, extract all existing copy currently in use (from Figma, production, or documentation). Organize it in a pre-writing audit table:

```
| Step ID | Element type  | Existing copy         | Issue flag              |
|---------|---------------|-----------------------|-------------------------|
| S01     | Page heading  | "Welcome back"        | None                    |
| S02     | CTA label     | "Click here"          | Non-descriptive label   |
| S02     | Error message | (missing)             | No error state defined  |
```

Issue flags: Non-descriptive label / Inconsistent noun / Missing state / Tone mismatch / Character limit risk / Localization flag

**Step 4 — Apply STEM to each step**

For each step and each system state, write the STEM analysis before writing the copy:

- **Situation:** What has just happened? Where is the user in the flow? What does the system know about the user at this moment?
- **Task:** What is the user trying to do right now? What action do they need to take next?
- **Expectation:** What outcome does the user expect from taking that action? What would confuse or disappoint them?
- **Message:** Given S, T, and E — what is the most useful thing the product can say right now?

The Message field is the proposed copy. It must be derived from the first three fields, not written independently.

**Step 5 — Write the copy table**

Produce the step-by-step copy table (see Structured Findings schema below). Write copy for every element type on every step and every reachable state. Do not skip states. Use the STEM output from Step 4 as the source.

**Step 6 — Apply Podmajersky's Strategic UX Writing method**

After the copy table is drafted, review the full flow for:

- **Voice consistency:** Does the copy sound like the same product personality across all steps? Identify voice drift.
- **Tone calibration:** Is the tone appropriately modulated for the emotional context of each step? (E.g., error messages should not be chipper; success messages should not be clinical.)
- **Vocabulary discipline:** Are the same nouns used consistently for the same concepts? Run the nomenclature check.
- **Sequencing logic:** Does each piece of copy logically follow from the previous step? Is the information hierarchy in each message right — most important information first?

**Step 7 — Nomenclature consistency check**

Extract every noun and action verb used across the copy table. List each term and every step where it appears. Flag any case where the same concept is named differently (e.g., "workspace" in S01, "project" in S04, "team space" in the confirmation email — all referring to the same object). Resolve inconsistencies and update the copy table.

**Step 8 — Error, loading, and empty state coverage**

Review the copy table against the state matrix from Step 2. Verify every step has copy for every reachable state. Flag any missing state as a gap. Propose copy for all missing states before finalizing.

---

## Structured Findings

The primary deliverable output is a step-by-step copy table. Every row must conform to this schema.

```
| Step ID | Screen / step name | System state | Element type     | Proposed copy                        | STEM rationale (brief)              | Voice rule applied          | Character count | Status   |
|---------|-------------------|--------------|------------------|--------------------------------------|-------------------------------------|-----------------------------|-----------------|----------|
| S01     | [screen name]     | Default      | Page heading     | [proposed heading copy]              | S: [situation]; M: [message logic]  | [rule name or inferred]     | [n]             | Draft    |
| S01     | [screen name]     | Error        | Inline error     | [proposed error message]             | S: user missed required field       | Constructive, no blame      | [n]             | Draft    |
| S02     | [screen name]     | Loading      | Loading label    | [proposed loading message]           | T: user waiting; M: reassure + ETA  | Active voice, present tense | [n]             | Draft    |
```

**Element types to cover per screen:**
- Page heading / screen title
- Supporting body copy or subheading
- Field labels (for forms)
- Placeholder text (for inputs)
- Inline helper text
- Inline error messages
- CTA labels (primary and secondary)
- Toast / notification messages
- Loading messages
- Empty state heading and body
- Confirmation messages
- Modal titles and body
- Link labels (avoid "click here")
- Tooltip copy

**Schema rules:**
- Every element type present in the design must have a row in the copy table. Do not skip element types that are hard to write.
- STEM rationale must be present for every row. Even a one-line summary is required. If STEM analysis was not run for a row, the row is incomplete.
- Character count must be estimated for every string. Flag strings over the platform limit.
- Status values: Draft / Reviewed / Approved / Needs validation / Missing

---

## Prioritization Logic

After the copy table is written, rank copy elements by user impact to inform review and iteration priority:

1. **Critical** — Copy at decision points (CTA labels, confirmation dialogs, destructive action labels). A wrong word here causes user error or abandonment. These must be STEM-validated and nomenclature-checked before any other copy.
2. **High** — Error messages and empty states. Users who encounter these are already in distress. Poor copy here generates support tickets and erodes trust. Write these even if the design team thinks they are edge cases.
3. **Standard** — Default state copy (headings, body, field labels, helper text). Important but typically less time-sensitive than error paths.
4. **Low** — Loading states and tooltips. Valuable but rarely the cause of user failure if slightly off.

**Priority does not mean coverage.** All states must be covered in the copy table. Priority determines which rows get the first review cycle.

---

## Pattern Detection

After drafting the copy table, the agent must explicitly scan for and document:

**Voice drift**
Identify any point in the flow where the copy voice shifts — becomes more formal, more casual, more technical, or more marketing-oriented than adjacent steps. Voice drift is usually introduced by copy from different sources (dev-written error messages mixed with designer-written UI labels). Flag every instance.

**Label inconsistency**
Run the full nomenclature list from Step 7. Every case where the same concept appears under a different name is a nomenclature violation. These are high-priority fixes because they create a mental model split for the user.

**Missing states**
Compare the state matrix from the flow model against the copy table. Every state that has no proposed copy is a gap. List all gaps with their step ID and state type.

**Tone mismatch**
Identify any step where the copy tone is inappropriate for the emotional context. Common examples: error messages that are overly cheerful, success messages that are too terse, loading messages that make the wait feel longer by being verbose.

**Redundant copy**
Flag any copy that repeats information already established in the same flow step or the immediately preceding step. Redundancy adds cognitive load without value.

---

## Recommendations

After the copy table and pattern detection pass are complete, write recommendations for the highest-impact issues found.

Each recommendation must:
- Reference the step ID and element type it addresses
- State the issue (from pattern detection or STEM analysis)
- Propose the resolution
- Note any dependency on a product decision, design change, or research validation

Format:
```
Rec [ID]
Step: [Step ID + screen name]
Element: [Element type]
Issue: [What is wrong and why it matters to the user]
Proposed resolution: [What to change and to what]
Dependency: [Any blocker — product decision needed, design change required, localization constraint, etc.]
Priority: [Critical / High / Standard / Low]
```

Recommendations must be directional for the copy, not for the product design. If a copy problem is caused by a missing product feature or an unclear product decision, flag the dependency explicitly and provide the best possible copy given the current state.

---

## Coverage Map

Document in the deliverable which parts of the flow were fully covered, partially covered, or not covered in this pass.

```
| Step ID | Screen name | States covered                        | States missing    | Evidence path      |
|---------|-------------|---------------------------------------|-------------------|--------------------|
| S01     | [name]      | Default, Error, Loading               | Empty state       | Figma file         |
| S02     | [name]      | Default, Success                      | System error      | Written spec       |
| S03     | [name]      | Not covered — out of scope this pass  | —                 | —                  |
```

State the overall coverage confidence: what proportion of the flow's reachable states have proposed copy. If fewer than 80% of states are covered, flag the deliverable as partial and identify what is needed to complete it.

---

## Limits and Unknowns

Document honestly in this section:

- **Copy dependent on unresolved product decisions:** Any string where the copy cannot be finalized until a product decision is made (e.g., "Copy for the cancellation confirmation depends on whether partial refunds are supported — currently unresolved").
- **Vocabulary not yet validated:** Any noun or action label that has not been tested with users and may not match user mental models.
- **Missing voice guidelines:** If voice principles were inferred rather than sourced from an approved guide, note this and flag for content design review.
- **Localization unknowns:** If character limits for translated locales are unknown, strings over 40 characters are at risk of truncation in space-constrained languages.
- **States not designed yet:** If error or empty states are not yet designed, the copy table rows for those states are provisional — they may need to change once layout context is established.
- **Character limit uncertainty:** If the engineering implementation's truncation behavior is unknown, strings over a threshold (typically 50 characters for labels, 120 for body copy on mobile) should be flagged.

Do not omit this section. Presenting copy as finalized when key unknowns exist sets up implementation errors.

---

## Workflow Rules

1. Build the JTBD frame and flow model before writing a single string. Copy written without a flow model is not flow-level writing — it is string-by-string guessing.
2. Run the STEM analysis for every element type at every step. Copy that skips STEM may be locally plausible but systemically incoherent.
3. Write the copy table in step order, not by what is easiest to write. Starting with headings and skipping errors is a coverage failure.
4. Run the nomenclature check after drafting the full copy table, not during. Checking during writing interrupts flow; checking after catches drift that accumulated across steps.
5. Do not present a copy table as complete if any required system state is missing. Flag missing states explicitly.
6. Label every section of output as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
7. Do not collapse STEM rationale into the copy. Rationale is documentation for design review; copy is the output. They are separate fields.
8. Flag any copy recommendation that requires a product decision before it can be finalized. Do not hide blockers in the copy itself.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/content-designer-microcopy-flow-design.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/runs/<run-id>/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

---

## Required Deliverable Sections

Within `## Skill: microcopy-flow-design`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Flow model` — JTBD frame, step inventory, decision points, state matrix, transition map, voice context notes, evidence path declared
- `### Copy inventory` — Pre-writing audit table of existing copy with issue flags
- `### STEM analysis` — STEM breakdown per step and state (can be embedded in copy table or in a separate reference section)
- `### Step-by-step copy table` — Full copy table in structured schema, covering all steps and all reachable states
- `### Nomenclature register` — Every noun and action verb used across the flow, with any inconsistencies flagged and resolved
- `### Pattern detection findings` — Voice drift, label inconsistencies, missing states, tone mismatches, redundancies
- `### Recommendations` — Structured recommendations for all high-priority copy issues
- `### Coverage map` — What was fully, partially, and not covered in this pass
- `### Limits and unknowns` — Copy blockers, missing decisions, unvalidated vocabulary, localization risks

---

