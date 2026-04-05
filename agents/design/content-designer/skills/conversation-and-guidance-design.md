---
name: conversation-and-guidance-design
description: Applies intent taxonomy, Grice's cooperative principle, progressive disclosure, and Google PAIR conversation design guidelines to design in-product guidance, assistant flows, and conversational interfaces that support task completion without over-explaining.
trigger: When the product needs embedded guidance, assistant copy, onboarding flows, chatbot dialogue, tooltips with logic, or any conversational surface where the system speaks to the user to help them complete a task.
required_inputs:
  - the user task or job the guidance must support
  - the surface or channel where guidance appears (tooltip, modal, chatbot, inline hint, walkthrough, voice)
  - the product voice and tone guidelines when available
  - known user confusion points or failure modes when available
recommended_passes:
  - Pass 1 — Intent model: map user jobs, confusion points, and surface entry conditions
  - Pass 2 — Guidance model: define flow states, assistant posture, escalation logic
  - Pass 3 — Message writing: write copy per guidance component using Grice's maxims
  - Pass 4 — Pattern audit: check for gaps, over-explanation, missing fallback paths
tool_stack:
  runtime:
    primary: notion
    secondary: figma, miro
  conversation_flow:
    primary: voiceflow
    secondary: landbot
  in_product_guidance:
    primary: pendo
    secondary: appcues, intercom
  testing:
    primary: maze
    secondary: usertesting
  fallback:
    primary: search_query, reference/ground
tool_routing:
  - if: designing multi-turn chatbot or assistant dialogue with branching logic
    use: voiceflow for flow authoring and dialogue simulation before writing final copy
  - if: designing in-product walkthroughs, tooltips, or feature announcements
    use: pendo or appcues to prototype and test guidance in the live product
  - if: mapping conversation flows collaboratively with the team
    use: miro or figjam for intent mapping and flow diagramming
  - if: the guidance lives inside a Figma-designed UI
    use: figma to annotate guidance states directly on the component
  - if: testing guidance comprehension or task completion with users
    use: maze for unmoderated testing or usertesting for moderated sessions
  - if: lightweight chat or no-code conversational flow is needed
    use: landbot as a simpler alternative to voiceflow
  - if: primary tools are unavailable, blocked, or out of credits
    use: search_query and reference/ground; label output as fallback
best_guess_output: A guidance and conversation design pack including a user intent map, guidance model, structured message library per flow state, escalation and fallback copy, and a pattern audit — labeled sourced, fallback, or inferred to match the evidence path used.
output_artifacts:
  - knowledge/runs/<run-id>/content-designer-conversation-and-guidance-design.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: Every user intent in scope has guidance copy for each flow state (entry, in-progress, reassurance, escalation, fallback); all copy passes Grice's relevance and quantity maxims; no guidance gap or missing escalation path remains undocumented.
---

# Conversation and Guidance Design

## Purpose

This skill designs the words a product uses to guide users through tasks — in tooltips, onboarding walkthroughs, assistant dialogue, chatbot flows, empty states with instructions, and any surface where the system speaks to help the user succeed.

Reasoning type: model-first then generative — construct the intent model and flow structure before writing a single word of copy.

Methods anchored to: Google PAIR (People + AI Research) Guidebook for conversation design; VUI (Voice User Interface) principles adapted for text interfaces; Erika Hall's conversation design approach from Just Enough Research; progressive disclosure (surface only what the user needs at this moment); intent taxonomy (categorize user jobs before writing); Grice's cooperative maxims (quantity, quality, relevance, manner) applied to guidance copy.

This skill does NOT write marketing copy, help center articles, or long-form documentation. It does not make product decisions about what a feature should do. It does not design the UI — it designs the words that sit inside the UI.

---

## Required Inputs and Assumptions

**Required:**
- The user task or job the guidance must support
- The surface or channel where guidance appears (tooltip, inline hint, modal, chatbot turn, walkthrough step, voice prompt)
- Product voice and tone guidelines when available
- Known user confusion points, drop-off moments, or failure modes when available

**Known vs unknown at start:**
- Known: what the feature does, what the surface is
- Often unknown: where exactly users get confused, what language users use to describe the task, whether users read guidance at all
- Unknown but needed: user vocabulary for the task — this must be inferred from prior research, support tickets, or labeled as `assumed`

**Assumption rule:** If user intent or confusion points are not documented, infer provisional intents from product context and feature scope. Prefix each with `Assumed intent:` and note that user research would validate or correct them. Do not write guidance for assumed intents at the same confidence level as research-backed intents.

---

## Input Mode and Evidence Path

Declare the evidence path before building the intent model. Options:

1. **Live / real interaction** — guidance is being designed during active user research or co-design sessions. Highest fidelity; user language is direct input.
2. **Structured system access** — Voiceflow flow diagrams, Pendo analytics on tooltip engagement, Intercom conversation logs, or Maze test results are available. Strong evidence about where users need guidance.
3. **Design artifacts / documentation** — Figma flows, journey maps, or prior guidance audits exist. Good for understanding surface context; may not reveal confusion points directly.
4. **Screenshots / static input** — UI screenshots or exported flows shared by the team. Visible states only; no behavioral signal.
5. **Inference** — no direct evidence; intent model built from product knowledge alone. Label all output as `inferred`. Flag for validation before shipping.

**Declare the path used in `### Evidence path` within the deliverable.**

---

## Tool Stack

**Voiceflow — conversation flow authoring**
Purpose-built tool for designing multi-turn assistant and chatbot dialogue. Supports branching logic, slot filling, and dialogue simulation. Use to prototype conversation flows before writing final copy — test how the dialogue feels before committing to a message library. Preferred for any product surface involving more than two sequential assistant turns.

**Landbot — lightweight conversational flows**
No-code chatbot and guided conversation builder. Better suited for linear or lightly branched flows, lead capture sequences, or simple onboarding wizards. Use when Voiceflow's complexity is not warranted or when a non-technical stakeholder needs to own the flow.

**Pendo — in-product guidance and analytics**
Product adoption platform with native walkthroughs, tooltips, banners, and in-app NPS. Use to author and deploy guidance directly in the live product, and to measure tooltip engagement, walkthrough completion, and feature adoption. Analytics reveal which guidance is being seen and which is skipped — critical signal for audits.

**Appcues — in-product onboarding flows**
Onboarding and feature announcement tooling. Comparable to Pendo for smaller teams. Use for multi-step onboarding flows, feature announcements, and checklists. Preferred when the team does not have a Pendo license.

**Intercom — conversational support and in-product messaging**
Combines live chat, chatbot flows (Fin), and product tours. Use when guidance is delivered through a support-adjacent channel or when the product already uses Intercom for support. Conversation logs are a valuable evidence source for understanding what users ask when they are stuck.

**Figma — guidance annotation in design**
Use to annotate guidance states directly on UI components and flows. Conversation flow diagrams in FigJam clarify entry/exit conditions for engineers and product managers. Use for guidance that is tightly coupled to a specific UI state rather than a standalone flow.

**Miro — intent mapping and flow diagramming**
Collaborative whiteboard for intent mapping workshops, user journey annotation, and conversation flow sketching. Use in early-stage design when the intent model is not yet settled and the team needs to align before tooling up in Voiceflow or Pendo.

**Maze — unmoderated guidance testing**
Test whether guidance copy achieves comprehension and task completion at scale. Use after a first draft is written to validate before shipping. Measures time-to-task, comprehension, and user confidence.

**UserTesting — moderated guidance testing**
Live session testing of guidance comprehension, tone fit, and task completion. Use when qualitative insight into why guidance is confusing is more valuable than quantitative metrics alone.

**Fallback — search_query, reference/ground**
Use when primary tools are unavailable. Search for guidance patterns on comparable surfaces; use reference/ground for framework application. Label all output as `fallback`.

---

## Tool Routing

- Multi-turn assistant or chatbot with branching logic → use Voiceflow for flow design and dialogue simulation before writing copy.
- Simple linear chat flow or non-technical team ownership needed → use Landbot.
- Guidance lives in the live product as tooltips, walkthroughs, or banners → use Pendo for authoring and analytics; Appcues if no Pendo license.
- Guidance delivered through support channel or Intercom is already in use → design within Intercom; mine conversation logs for confusion signals.
- Guidance is tightly coupled to a specific UI state → annotate in Figma; diagram entry/exit logic in FigJam.
- Team alignment on intent model needed before tooling up → use Miro for collaborative intent mapping.
- Guidance draft is ready to test → use Maze for unmoderated comprehension testing; UserTesting for moderated sessions.
- All primary tools unavailable → use search_query + reference/ground; label each output section as `fallback`.
- Do not begin writing copy before the intent model and guidance model are documented. Copy written without a model produces guidance that answers the wrong question.

---

## Environment and Reproducibility

- **Platform:** Voiceflow, Pendo, Appcues, and Maze are browser-based SaaS — no local install required
- **Auth state:** Voiceflow flows are workspace-scoped; Pendo and Appcues require product installation and analytics access; Maze tests require a published prototype or live URL
- **Data state:** Guidance copy is reproducible if the intent model and flow diagrams are preserved. If only the final copy is saved without the model, it cannot be audited or updated accurately when the product changes.
- **Version:** Log the product version or feature state the guidance was designed for. UI-coupled guidance ages quickly — a tooltip written for a three-step flow is incorrect if the flow changes to two steps.
- **Voice and tone dependency:** Guidance copy is calibrated to a voice and tone guideline. If that guideline changes, guidance must be re-reviewed. Log the tone guideline version used.

---

## Model Building

The agent must construct the intent model and guidance model before writing any copy. Copy without a model produces guidance that answers the wrong question or appears at the wrong moment.

### 1. User intent map

Map every user job or intent that the guidance must support. For each intent:

```
Intent ID:     [INT-01, INT-02, ...]
User job:      [What the user is trying to accomplish — in user language, not feature language]
Trigger:       [What moment or action brings the user to this point]
Confusion risk: [High / Medium / Low — how likely is the user to be stuck or uncertain here]
Current support: [Does any guidance exist? Is it working?]
Evidence source: [Research, analytics, support log, or Assumed intent:]
```

Group intents by task phase: discovery, onboarding, task execution, recovery, and offboarding/exit.

### 2. Flow states

For each intent, define the states the guidance must address:

- **Entry point** — first moment the user encounters this surface or task
- **In-progress** — user is mid-task; guidance supports continuation
- **Reassurance** — user has completed an action and needs confirmation it was right
- **Escalation trigger** — user signals confusion, error, or need for more help
- **Fallback** — system cannot complete the task; user must be redirected

Every intent must have a defined fallback. Guidance without a fallback path leaves users stranded.

### 3. Assistant posture

Define the register, authority level, and personality the guidance takes on this surface:

- **Register:** formal / neutral / conversational / friendly
- **Authority:** directive (tell the user what to do) / advisory (suggest an action) / informative (explain what happened)
- **Personality markers:** specific language patterns, terms to use, terms to avoid
- **Posture rule:** posture must be consistent within a flow. Switching from directive to advisory mid-flow without a reason creates cognitive friction.

The assistant posture must align with the product's voice and tone guideline. If no guideline exists, document the posture chosen and flag the gap.

---

## Core Method Execution

Follow this sequence. Do not skip steps or merge steps.

**Step 1 — Clarify the task scope**
Identify the specific user task or interaction surface this guidance must support. If the scope is vague, write a provisional task statement, label it `Assumed scope:`, and continue. Confirm with the product team before shipping.

**Step 2 — Build the intent taxonomy**
Apply intent taxonomy to categorize every user job in scope before writing a word. Intents fall into:
- **Navigational** — user wants to get somewhere (find a feature, reach a screen)
- **Transactional** — user wants to complete an action (submit, save, configure)
- **Informational** — user wants to understand something (what does this do, what happened)
- **Recovery** — user has hit an error or unexpected state and needs a path forward

Label each intent by type. Transactional and recovery intents carry the highest confusion risk and must have complete guidance coverage.

**Step 3 — Build the intent model**
Complete the user intent map (see Model Building above) for all in-scope intents. Do not write copy until every in-scope intent has a defined flow state map and evidence source noted.

**Step 4 — Define assistant posture**
Write the posture definition for this surface. Document register, authority level, personality markers, and the constraint on posture switching.

**Step 5 — Apply progressive disclosure**
For each intent and flow state, determine what the user needs to know at this exact moment — no more. Apply progressive disclosure:
- Surface only the information required to take the next action
- Reserve detail for a secondary layer (expandable hint, modal, help link) that the user can access on demand
- Never pre-empt questions the user has not yet reached
- Test: if you removed one sentence, would the user still know what to do? If yes, remove it.

**Step 6 — Write guidance copy using Grice's maxims**
Apply Grice's cooperative principle to every guidance message:
- **Quantity:** say exactly as much as needed — no more, no less. One instruction per message. One reassurance per state.
- **Quality:** only write what is true and accurate. Do not write reassurance that is not warranted ("you're all set!" when there is a pending step).
- **Relevance:** every sentence must connect to the user's current job. Cut anything that is interesting but not immediately necessary.
- **Manner:** be clear, brief, and ordered. Avoid ambiguous pronoun references. Avoid passive voice when the user needs to take action. Avoid jargon not established in the product's vocabulary.

**Step 7 — Apply Google PAIR conversation design principles**
For conversational surfaces (chatbots, assistants, guided flows):
- Design for comprehension, not just completion — the user should understand why the system is asking what it is asking
- Give the user a clear next action at every turn — never leave a turn that ends without a path forward
- Acknowledge what the user just did before directing what to do next
- Design for the edges: what happens if the user says something unexpected, provides no input, or provides the wrong type of input
- Avoid over-confirmation — not every user action needs a confirmation message; reserve confirmation for irreversible or high-stakes actions
- Use natural language patterns adapted from VUI design: short turns, explicit prompts, graceful re-prompting when input is unclear

**Step 8 — Write the message library**
Produce one message per guidance component per flow state. Use the structured component schema (see Structured Findings below). Do not combine multiple components into a single message block.

**Step 9 — Write escalation and fallback copy**
For every intent where the user may need more help than the guidance provides, write:
- Escalation copy: the message shown when the user signals confusion, clicks "I'm stuck", or triggers a defined error state
- Handoff message: the message when the system transfers to a human agent, help article, or support channel
- Fallback copy: the message when the system cannot complete the task at all (error, outage, unsupported input)

Fallback copy must never be a dead end. Every fallback must end with a path forward.

**Step 10 — Run the pattern audit**
Review the complete message library against the pattern detection criteria (see Pattern Detection below). Document findings before declaring the skill done.

---

## Structured Findings

Every guidance component must conform to this schema. No free-form copy blocks outside the schema.

```
Component [ID]
Intent:        [INT-01 — the user job this component supports]
Flow state:    [Entry / In-progress / Reassurance / Escalation / Fallback]
Surface:       [Tooltip / Modal / Inline hint / Chat turn / Walkthrough step / Voice prompt]
Trigger:       [What condition causes this component to appear]
Message:       [The exact copy — final wording]
Character limit: [If surface has a limit — note whether copy is within it]
Tone check:    [Quantity / Quality / Relevance / Manner — pass or flag]
Assistant posture: [Register + authority level at this moment]
Exit condition: [What happens after the user reads this — next step or component]
Evidence source: [sourced / fallback / inferred]
```

Separation rule: the message field must contain only the copy. Do not embed rationale or notes inside the message field — use a separate note line if needed.

---

## Prioritization Logic

After the message library is drafted:

1. **Score each intent by confusion risk x task criticality.** Confusion risk (High / Medium / Low) × task criticality (blocking / supporting / optional). High × blocking intents are P1 — guidance here must be complete, tested, and shipped before launch.
2. **P1 intents:** full component coverage required (entry, in-progress, reassurance, escalation, fallback). No gaps permitted.
3. **P2 intents:** entry and task-critical in-progress components required; escalation and fallback can be phased.
4. **P3 intents:** entry-point hint only; escalation deferred to help documentation.
5. **Do not ship P1 guidance without a tested fallback path.**

---

## Pattern Detection

After the message library is complete, the agent must check for and document:

- **Guidance gaps:** intents in scope that have no coverage in the message library. Every gap must be named and either filled or explicitly deferred with a reason.
- **Over-explanation:** messages that violate the quantity maxim — more than one instruction per message, or information the user does not need at this flow state. Flag and trim.
- **Missing escalation paths:** flow states that end without a path forward when the user is confused or the system fails. Every terminal state must have an exit.
- **Posture inconsistency:** turns or steps within a flow where the register or authority level shifts without a design reason. Flag and align.
- **False reassurance:** confirmation or success messages that are not warranted by the actual system state. Flag for accuracy review.
- **Jargon without establishment:** product or technical terms used in guidance that are not defined in the product vocabulary. Flag for plain-language substitution or define the term on first use.
- **Duplicate coverage:** multiple components addressing the same intent at the same flow state — consolidate.

---

## Coverage Map

Document which user tasks and intents are covered by the guidance library:

| Intent ID | User job | Coverage status | Flow states covered | Evidence source |
|-----------|----------|-----------------|---------------------|-----------------|
| INT-01    | ...      | Complete        | Entry, In-progress, Reassurance, Escalation, Fallback | sourced |
| INT-02    | ...      | Partial         | Entry, In-progress | inferred |
| INT-03    | ...      | Not covered     | —                   | — |

State the overall coverage confidence: what proportion of P1 intents have complete component coverage. If any P1 intent is missing an escalation or fallback path, flag the guidance as not shippable.

---

## Limits and Unknowns

Document honestly:

- Where intent classification is assumed rather than research-backed
- Which user confusion points are inferred from product context vs. observed in research or analytics
- Where progressive disclosure layering is untested — users may not discover secondary help content
- Where voice and tone guidelines did not exist and posture was designed from first principles
- Which guidance components were not user-tested before being included in the library
- Surface or platform constraints not yet confirmed (character limits, rendering environment, localization requirements)

---

## Workflow Rules

1. Build the intent model (user intent map, flow states, assistant posture) before writing any copy.
2. Apply intent taxonomy before assigning confusion risk or task criticality scores.
3. Apply progressive disclosure per flow state — do not front-load all information at entry.
4. Write one message per component per flow state. No message should serve two flow states.
5. Apply Grice's maxims as a filter on every message — flag any message that fails a maxim before marking it complete.
6. Every flow must have a defined fallback. No dead ends in any guidance path.
7. Run the pattern audit after the message library is complete, not before.
8. Label every output section as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
9. Do not mark the skill done if any P1 intent lacks a fallback path or any escalation path is undefined.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/content-designer-conversation-and-guidance-design.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/runs/<run-id>/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

---

## Required Deliverable Sections

Within `## Skill: conversation-and-guidance-design`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Evidence path` — which input mode and evidence tier was used; what is known vs. inferred
- `### Intent model` — user intent map with all in-scope intents, flow states, confusion risk scores, and evidence sources
- `### Assistant posture` — register, authority level, personality markers, and posture rules for this surface
- `### Message library` — all guidance components in the structured schema, grouped by intent
- `### Escalation and fallback copy` — all escalation triggers, handoff messages, and fallback paths
- `### Pattern audit` — findings from the pattern detection check: gaps, over-explanation, missing paths, posture inconsistencies
- `### Coverage map` — which intents are fully, partially, and not covered
- `### Limits and unknowns` — what is assumed, untested, or dependent on unconfirmed constraints

---

