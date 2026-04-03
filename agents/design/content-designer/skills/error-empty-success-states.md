---
name: error-empty-success-states
description: Applies state machine modeling, Nielsen's error heuristics, and the NNG empty-state framework to enumerate all non-default UI states and write recovery-first, severity-tiered messaging for each one.
trigger: When a feature needs state-specific messaging beyond the happy path — including error, empty, loading, timeout, partial-success, and success states.
required_inputs:
  - the feature or flow that needs state coverage (name and user goal)
  - the list of known system states, or enough product context to derive them
  - the product voice and severity guidelines when documented
  - existing copy or error codes from engineering when available
recommended_passes:
  - Pass 1 — State model: enumerate every possible state before writing any copy
  - Pass 2 — Severity triage: classify each state by error type and recovery availability
  - Pass 3 — Message drafting: write headline, body, CTA, and recovery action per state
  - Pass 4 — Pattern audit: check for missing recovery paths, inconsistent severity voice, and raw technical codes
  - Pass 5 — Coverage map: verify all critical states are covered and flag any gaps
tool_stack:
  runtime:
    primary: figma, notion
    secondary: storybook, sentry, datadog
  session_observation:
    primary: fullstory, logrocket
  testing:
    primary: maze, userzoom
  pattern_reference:
    primary: material_design_guidelines, apple_hig
  fallback:
    primary: search_query, reference/trace
tool_routing:
  - if: figma file exists with component states or error annotations
    use: figma to extract state inventory and annotate message variants inline
  - if: engineering has a Sentry project connected
    use: sentry to identify the most frequent error types by occurrence count — prioritize those first
  - if: Datadog dashboards are available
    use: datadog to surface error rate and latency data, informing timeout threshold copy and severity framing
  - if: FullStory or LogRocket sessions are available
    use: fullstory or logrocket to observe how users actually behave in error states — do they retry, abandon, or contact support?
  - if: messages need usability validation
    use: maze or userzoom to run unmoderated comprehension tests on error copy
  - if: Storybook is available for the component library
    use: storybook to document final state messages as component story annotations
  - if: primary tools are unavailable, blocked, or out of credits
    use: search_query + reference/trace; label all output as fallback
best_guess_output: A state inventory covering all system states, with a headline, body, CTA, recovery action, voice constraint, and confidence level per state — labeled as inferred where no live product access exists.
output_artifacts:
  - logs/active/<project-slug>/runs/<run-id>/deliverables/content-designer-error-empty-success-states.md
  - logs/active/<project-slug>/runs/<run-id>/deliverables/assets/ (for visual artifacts)
done_when: Every critical state has explicit user-facing messaging with a recovery action, no state exposes raw technical codes to users, severity voice is consistent across the message set, and the coverage map confirms all enumerated states are addressed or explicitly deferred.
---

# Error Empty Success States

## Purpose

This skill enumerates every non-default UI state a feature can enter and produces a complete, recovery-first message set for each one.

Reasoning type: structured enumeration followed by severity classification. The agent builds a state machine model first, then writes copy — never the reverse.

Methods anchored to:
- **Nielsen's 10 usability heuristics** — specifically heuristic #5 (error prevention: help users avoid problems before they occur) and heuristic #9 (help users recognize, diagnose, and recover from errors: plain language, state the problem, suggest a solution)
- **Nielsen Norman Group empty-state framework** — four distinct empty-state types: first use (never been populated), no results (search returned nothing), cleared data (user deleted content), error-as-empty (data failed to load)
- **State machine modeling** — enumerate all possible states before writing any copy; each state has a condition, a visual treatment, and a message set
- **Severity-tiered messaging** — system error (we caused it), user error (they caused it), warning (preventable problem), and success (confirmation of intended outcome) each require a distinct voice register
- **Recovery-first copy principle** — every error message must include a next action the user can take; restating the problem without a path forward is not acceptable

This skill does NOT design the visual components, define the interaction model for error states, or make engineering decisions about which states to implement. It writes the words for states that already exist or will exist in the product.

---

## Required Inputs and Assumptions

**Required:**
- The feature or flow name and the primary user goal it supports
- Known system states, or enough product and engineering context to derive them through state machine modeling
- Product voice guidelines or a reference example of existing in-product copy
- Error codes or technical identifiers from engineering when available (so they can be mapped to human-readable messages)

**Known vs unknown at skill invocation time:**
- Known: the happy-path flow and the feature's main user action
- Often unknown: the full set of edge-case states, the exact frequency of each error type in production, whether partial success states exist
- Frequently absent: documented severity classification for each error code

**Assumption rule:** If the state list is not provided, derive it from the feature's user goal using state machine modeling (see Model Building). Label every inferred state as `assumed` and flag it for product or engineering confirmation before shipping. If the product voice is undocumented, infer from existing in-product copy. Label inferred voice constraints as `assumed`.

---

## Input Mode and Evidence Path

Declare the evidence path used before starting state enumeration. Options:

1. **Live product access** — direct use of the feature in a staging or production environment. Highest fidelity; lets the agent trigger states deliberately and observe current messaging.
2. **Figma file with state annotations** — design file includes component states, error variants, or loading states. Strong coverage for UI states; may not reflect all engineering-side error conditions.
3. **Sentry / Datadog error data** — production error logs identify which errors occur, at what frequency, and with what codes. Use to prioritize which states need the most polished recovery copy.
4. **Storybook component library** — existing stories enumerate component variants including error, empty, and disabled states. Use to extract the existing state inventory.
5. **FullStory / LogRocket session recordings** — observe real user behavior in error and empty states. Use to understand what recovery paths users actually attempt vs. what is documented.
6. **Inference from product context** — no direct tool access; states are derived from feature description, user goal, and general knowledge of the error category. Label all output as `inferred`.

Declare the path in the `### State inventory` section of the deliverable. Use multiple paths when they address different gaps (e.g., Figma for UI states + Sentry for error frequency prioritization).

---

## Tool Stack

**Runtime primary — Figma**
Access component states, frame annotations, and error variant designs. Use to extract what states are already designed, annotate message variants directly on frames, and prepare a state-message spec that engineers can reference during implementation. Figma MCP enables direct frame and variant inspection without leaving the agent context.

**Runtime primary — Notion**
Document the state inventory, message set, and voice notes in a structured page. Use as the primary deliverable surface when the team uses Notion for content specs. Notion MCP enables direct page creation and updates.

**Runtime secondary — Storybook**
Storybook (storybook.js.org) is an open-source component explorer used by engineering teams to document UI states in isolation. When a Storybook instance is available, it provides a definitive list of component variants — including error, empty, loading, and disabled states — that reflects the actual implementation. Use Storybook as the ground-truth state inventory when Figma and engineering states have diverged. Final message sets can be documented as Storybook story annotations or CSF story args.

**Runtime secondary — Sentry**
Sentry (sentry.io) is an application monitoring and error tracking platform. Free tier available; team and business tiers for larger volumes. When connected, Sentry provides error occurrence counts, stack traces, and affected user counts per error type. Use to prioritize which error states need the most refined copy: a 400-occurrence-per-day network timeout deserves better recovery copy than a 2-occurrence-per-month edge case. Map Sentry error codes to human-readable state names in the state inventory.

**Runtime secondary — Datadog**
Datadog (datadoghq.com) provides infrastructure monitoring, APM, and log management. Use to surface error rates, latency percentiles, and API failure patterns. Latency data informs timeout threshold copy (e.g., "This is taking longer than usual" triggers at what threshold?). Error rate trends help distinguish intermittent states from chronic ones — intermittent errors call for softer "try again" copy; chronic failures warrant escalation paths.

**Session observation — FullStory**
FullStory (fullstory.com) records real user sessions including rage clicks, dead clicks, and navigation paths after errors. Use to observe what users actually do when they hit an error state: do they retry immediately, read the message, abandon, or navigate to a different page? Session evidence informs whether current copy is causing abandonment and whether the recovery CTA is being used.

**Session observation — LogRocket**
LogRocket (logrocket.com) combines session replay with performance and error monitoring. Closest alternative to FullStory. Also surfaces console errors and network failures alongside session playback, which helps correlate a specific error code with the moment in the user session where it appears.

**Usability testing — Maze**
Maze (maze.co) enables unmoderated usability testing at scale. Use to validate error message comprehension: do users understand what went wrong and what to do next? Run a quick concept test with multiple message variants to identify which recovery copy achieves the highest next-action rate. Starter tier is free; Pro tier for advanced analytics.

**Usability testing — UserZoom (now part of UserTesting)**
UserZoom supports moderated and unmoderated research. Use for more in-depth error message comprehension testing when qualitative reasoning matters (why didn't the user click "Try again"?). Better for complex or high-stakes error states (payment failures, data loss warnings).

**Pattern reference — Material Design Guidelines**
Google's Material Design 3 (m3.material.io) documents error message patterns for text fields, dialogs, snackbars, and banners. Strong reference for input validation errors, inline field errors, and toast notification copy. Use to check whether proposed message patterns align with established platform conventions.

**Pattern reference — Apple Human Interface Guidelines**
Apple HIG (developer.apple.com/design/human-interface-guidelines) documents error handling patterns for iOS, macOS, and cross-platform apps. Covers alert dialogs, destructive action confirmations, and system-level error patterns. Use when writing for Apple platform surfaces or when the product aspires to Apple-level error clarity standards.

**Fallback — search_query, reference/trace**
Use when primary and secondary tools are unavailable. Manual search for error message examples, empty-state patterns, and voice references. Label all output produced via fallback as `fallback`.

---

## Tool Routing

- Figma file exists with state annotations or component variants → use Figma to extract state inventory, then annotate message variants on frames.
- Notion is the team's documentation hub → write state inventory and message set as a Notion page; link from the Figma file.
- Sentry connected and error data available → use Sentry occurrence counts to prioritize message quality effort; map error codes to state names before writing copy.
- Datadog available with latency data → use Datadog to set timeout copy thresholds and distinguish chronic from intermittent errors.
- FullStory or LogRocket sessions available → analyze post-error user behavior before finalizing CTA labels; if users are abandoning instead of retrying, the recovery copy is failing.
- Storybook available → use it as the authoritative component state inventory; document final messages as story annotations.
- Message comprehension needs validation → run a Maze concept test on the top 3 highest-frequency error states with 2–3 copy variants per state.
- Apple or Android platform conventions matter → cross-reference Material Design and Apple HIG before finalizing severity voice.
- All primary tools unavailable → produce inferred state inventory from feature context; use search_query for pattern reference; label all output as `fallback`.
- Never rely on a single tool. Figma (state shape) + Sentry (priority) + FullStory (behavior observation) produces stronger copy decisions than any one tool alone.

---

## Environment and Reproducibility

Record the following in the deliverable:
- Date the state inventory was built (error states are implementation-dependent; they drift with engineering changes)
- Product version or feature flag state at time of analysis
- Figma file URL and frame names used as the source of truth
- Sentry project name and date range for error frequency data
- Whether the Storybook component library version was checked against the Figma file
- Whether session observation data (FullStory, LogRocket) was used and the date range reviewed

If any of the above is unknown, state it explicitly. Do not treat an older Figma file as a current representation of implemented states without confirming with engineering.

---

## Model Building

The agent MUST construct a complete state model before writing any copy. No copy may be drafted until the state inventory is complete and severity-classified.

### State machine modeling

For every feature, enumerate states in these categories:

**Loading states**
- Initial load (first time the component mounts)
- Refresh / background sync in progress
- Optimistic update pending

**Empty states — four NNG types**
- First use: the feature has never been populated (the user has no data yet)
- No results: a search, filter, or query returned zero matches
- Cleared data: the user explicitly deleted content
- Error-as-empty: data failed to load and the component renders visually empty

**Error states — severity tiers**
- System error (we caused it): server errors (5xx), infrastructure failure, data corruption, timeout exceeding threshold. User has no corrective action beyond retrying or contacting support.
- User input error (they caused it): validation failures, required fields missed, format violations, constraint violations (e.g., username taken). User has a clear corrective action.
- Permission / access error: unauthenticated, unauthorized, feature not enabled for their plan. Recovery is navigation or upgrade, not retry.
- Network error: request failed due to connectivity. Recovery is retry; message should not imply product failure.
- Timeout: request exceeded a threshold without resolution. Distinct from network error; may indicate a system problem.
- Partial success: some items succeeded, some failed (e.g., bulk upload where 8/10 files processed). Requires split-state messaging.

**Success states**
- Immediate confirmation: action completed synchronously (e.g., form saved).
- Deferred confirmation: action will complete asynchronously (e.g., export is processing, you will be notified).
- Destructive action completed: deletion, disconnect, cancel — requires a distinct voice to avoid feeling celebratory.

**Edge and boundary states**
- Rate limited: user has exceeded allowed frequency.
- Maintenance mode: system temporarily unavailable.
- Degraded mode: feature is partially available.
- Session expired: authentication lapsed mid-flow.

Build this as a table before writing any copy:

```
| State ID | Category          | Trigger condition                    | Recovery available? | Severity |
|----------|-------------------|--------------------------------------|---------------------|----------|
| S01      | Loading           | Initial component mount              | N/A                 | N/A      |
| S02      | Empty / first use | User has no items yet                | Yes — create action | Info     |
| S03      | Error / system    | 500 from API on submit               | Retry               | High     |
| S04      | Error / user      | Required field missing on submit     | Fix field           | Medium   |
| S05      | Success           | Form submitted successfully          | None needed         | Positive |
...
```

No copy writing begins until this table is complete. If states cannot be enumerated from available inputs, produce a best-guess inventory, label each row as `assumed`, and flag for engineering confirmation.

---

## Core Method Execution

Follow this sequence exactly.

**Step 1 — Declare inputs and evidence path**
State what feature is being covered, what the user's goal is, and which evidence path is being used (live product / Figma / Sentry / inference). If inputs are partial, state what is missing and what has been assumed.

**Step 2 — Build the state inventory table**
Enumerate all states using the Model Building framework above. Cover all six categories. For each state, record: state ID, category, trigger condition, whether recovery is available, and severity tier. Do not skip edge states — partial success, session expiry, and rate limiting are routinely omitted and routinely cause bad experiences.

**Step 3 — Classify severity and recovery type**
For each error state, apply the severity-tiered model:
- **High severity (system error):** Tone is honest and calm. Acknowledge the problem. Do not blame the user. Offer a retry or an escalation path. Never use exclamation marks.
- **Medium severity (user error):** Tone is clear and instructional. State specifically what is wrong and how to fix it. Do not lecture.
- **Low severity (warning, soft limit):** Tone is informative. State the constraint without creating alarm.
- **Positive (success, confirmation):** Tone matches the emotional weight of the action. A file saved is different from a payment completed.

Apply Nielsen heuristic #5 (error prevention): where a state can be avoided by design, note it. Example: a file format validation error can be prevented by restricting upload types before submission.

Apply Nielsen heuristic #9 (help users recover): every error message must answer three implicit user questions: What happened? Why? What do I do now?

**Step 4 — Apply the NNG empty-state framework**
For each empty state, determine which of the four NNG types it is:
- **First use:** Include a clear explanation of what the space is for and a primary action to populate it. This is a product orientation moment — avoid generic "No items yet" copy.
- **No results:** Acknowledge the search terms or filters used. Suggest a modification. Do not make the user feel they searched wrong.
- **Cleared data:** Acknowledge the action just completed. Offer undo if available. If not, confirm the state is intentional.
- **Error-as-empty:** Do not let this state look like "no results." It is an error. Distinguish it visually and in copy. Include a retry mechanism.

**Step 5 — Write message sets**
For each state, write the full message set using the schema in the Structured Findings section. Apply recovery-first copy principle: the CTA and recovery action are not optional. Every state that can be resolved by user action must tell the user exactly what that action is.

**Step 6 — Run pattern audit**
After the full message set is drafted, check for the three most common defects:
1. Missing recovery paths: any error state where the CTA is absent or says only "OK" or "Close"
2. Inconsistent severity voice: system errors that sound like user errors (blaming the user for infrastructure failure), or warnings that sound like critical failures
3. Raw technical codes: any message that exposes an error code, stack trace fragment, or internal identifier without a human-readable translation

**Step 7 — Produce coverage map**
Document which states are fully covered, which are partially drafted (pending product input), and which are deferred.

---

## Structured Findings

Every state message must conform to this schema. No free-form copy blocks in the deliverable.

```
State [ID]
State name:       [Descriptive name, e.g., "Upload failed — file too large"]
Category:         [Loading / Empty-first-use / Empty-no-results / Empty-cleared / Empty-error / Error-system / Error-user / Error-permission / Error-network / Error-timeout / Partial-success / Success]
Trigger:          [What causes this state to appear]
Severity:         [High / Medium / Low / Positive]
Headline:         [Short, plain-language headline — max 8 words — states the situation]
Body:             [One to two sentences. What happened (if non-obvious), and what to do next. No jargon, no error codes.]
CTA label:        [Button or link label — action verb + object, e.g., "Try again" / "Upload a different file" / "Go to settings"]
Recovery action:  [What the user actually does: retry the same action / modify input / navigate / contact support / wait]
Voice constraint: [Tone note specific to this state: e.g., "Calm and direct — do not imply data loss if data is intact" / "Avoid exclamation marks" / "Do not use 'Oops'"]
Confidence:       [High = confirmed state from Figma or Sentry / Medium = inferred from product context / Low = assumed, needs engineering confirmation]
```

**Separation rule:** Headline states the situation. Body explains and directs. CTA label is the action word. Never collapse explanation and action into the headline alone.

**Recovery action taxonomy:**
- `retry-same` — user clicks a button to retry the identical action (network errors, timeouts)
- `retry-modified` — user modifies input then retries (validation errors, format errors)
- `navigate` — user is directed to a different page or section (permission errors, upgrade prompts)
- `wait` — user is told the system will resolve the state without their input (async processes, maintenance)
- `contact-support` — escalation to human support (severe data or payment errors)
- `no-action` — state is informational; no user action needed (success confirmations)

---

## Prioritization Logic

Not all states deserve equal copy investment. Apply this order:

1. **Critical path errors first:** States that block the user's primary goal (e.g., form submit failure, payment error, data load failure on the main view) must have fully polished copy before any other state.

2. **High-frequency errors second:** Use Sentry occurrence counts or Datadog error rates to rank the remaining error states by how often users encounter them. A state that fires 500 times per day needs better copy than one that fires twice a month.

3. **Empty states for first-time users third:** First-use empty states are encountered by every new user and have high influence on activation. Prioritize before edge-case error states.

4. **Recovery messages over decoration:** A state's copy is not complete until the recovery action is defined. A beautifully written headline with no CTA is lower quality than a plain headline with a clear next step.

5. **Defer low-frequency, low-severity states explicitly:** If a state is very rare and low-severity, it can be deferred — but it must appear in the coverage map as `deferred` with a reason, not simply omitted.

---

## Pattern Detection

After the message set is drafted, the agent must check for and document:

**Missing recovery paths**
Scan every error and empty-error state for a defined CTA and recovery action. Any state where the CTA is "OK", "Close", or absent is a defect. Flag it explicitly: `[DEFECT — no recovery path defined for state S03]`.

**Inconsistent severity voice**
Check that system errors (we caused it) do not use language that implies user fault. Check that user errors (they caused it) are specific and instructional rather than punitive. Check that warnings do not use alarm language appropriate for failures. Voice inconsistency erodes user trust over time even when individual messages seem acceptable in isolation.

**Over-reliance on technical error codes**
Scan every body copy field for: HTTP status codes (404, 500), internal error identifiers, stack trace fragments, or database error strings. Any technical code exposed to users without a plain-language translation is a defect. Log the code in a separate developer-facing reference; never surface it as the primary user message.

**Duplicate states with divergent copy**
If the same underlying condition (e.g., "session expired") produces different messages in different parts of the product, flag the inconsistency. One state should have one message set.

**Error-as-empty misclassification**
Verify that states where data failed to load are not styled or worded the same as "no results" states. A failed data load must communicate that something went wrong and offer a retry. Treating it as an empty state is misleading.

---

## Coverage Map

Document in the deliverable:

| State ID | State name             | Coverage status     | Confidence | Notes                              |
|----------|------------------------|---------------------|------------|------------------------------------|
| S01      | Initial load           | Fully covered       | High       | Sourced from Figma                 |
| S02      | Empty / first use      | Fully covered       | Medium     | Inferred — no Figma variant found  |
| S03      | Upload failed / 500    | Fully covered       | High       | Sentry code 1042 mapped            |
| S04      | Session expired        | Deferred            | Low        | Engineering confirmation needed    |
| ...      | ...                    | ...                 | ...        | ...                                |

State the overall coverage confidence: what proportion of enumerated states are fully covered. If critical-path states are not fully covered, flag the deliverable as incomplete and do not mark done-when as met.

---

## Limits and Unknowns

Mandatory section. Document honestly:

- Which states could not be confirmed from available inputs and are marked `assumed`
- Where Sentry or Datadog data was unavailable and frequency prioritization was skipped
- Where session observation data (FullStory, LogRocket) was unavailable and recovery-action assumptions were not validated by user behavior
- Whether voice guidelines are formally documented or inferred from existing copy
- Whether the state inventory was reviewed by engineering (states may be missing if product context was the only source)
- Any states where the recovery action depends on a product or infrastructure decision not yet made (e.g., "Does this error support retry, or does it require a new session?")

Do not collapse this section to a single line. Unnamed unknowns become shipped defects.

---

## Workflow Rules

1. Build the state inventory before writing a single word of copy.
2. Classify every state by category and severity before writing messages.
3. Every error state must have a recovery action. If the recovery action is genuinely "contact support," that is acceptable — but it must be explicit, not absent.
4. No technical error codes in user-facing body copy. Map codes to human-readable messages; preserve the code in a developer reference.
5. Label every section of the deliverable as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
6. Do not treat error-as-empty states as empty states. They require distinct copy and a retry mechanism.
7. Check severity voice consistency across the full message set before finalizing. Read all error messages in sequence — inconsistency is visible at scale even when invisible in isolation.
8. If the state inventory cannot be confirmed with engineering before the skill run ends, prefix every unconfirmed state with `Assumed:` and add it to the Limits and Unknowns section.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/content-designer-error-empty-success-states.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `logs/active/<project-slug>/runs/<run-id>/deliverables/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

---

## Required Deliverable Sections

Within `## Skill: error-empty-success-states`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### State inventory` — the full enumerated state table with category, trigger, severity, and recovery availability per state; label each row as sourced, fallback, or inferred
- `### Message set` — every state message using the required schema (State ID / Headline / Body / CTA label / Recovery action / Voice constraint / Confidence)
- `### Pattern audit findings` — results of the three pattern checks: missing recovery paths, severity voice inconsistency, raw technical codes
- `### Coverage map` — what is fully covered, partially drafted, and deferred
- `### Limits and unknowns` — unconfirmed states, missing tool data, voice assumptions, pending engineering decisions

---

