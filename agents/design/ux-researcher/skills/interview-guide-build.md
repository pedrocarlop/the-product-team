---
name: interview-guide-build
description: Applies semi-structured interview method, laddering technique, JTBD probing, and think-aloud protocol to construct a moderated session guide with sequencing, probes, evidence goals, and bias review.
trigger: When live research sessions need a structured guide — generative interviews, evaluative sessions, or concept walkthroughs.
best_guess_output: An interview guide with session structure, questions, probes, evidence goals, and moderator notes that supports comparable sessions across participants.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: interview-guide-build"
done_when: A moderator can run all sessions from the guide without improvising the core script, every question is traceable to a research objective, and mandatory and optional probes are explicitly separated.
required_inputs:
  - Research objective or study goal
  - Participant profile or screener criteria
  - Session duration
recommended_passes: 2 (first pass — objective model and topic map; second pass — question draft, probe design, and bias review)
tool_stack:
  runtime:
    primary: notion
    secondary: dovetail, looppanel
  artifacts:
    primary: logs/active/<project-slug>/deliverables/ux-researcher.md
  fallback:
    primary: search_query, ux-researcher/research-plan
tool_routing:
  - if: notion is available and the research plan is linked
    use: notion — store guide, version across sessions, link to research plan page
  - if: team uses session recordings and post-session analysis
    use: dovetail — store guide alongside recordings for traceability; looppanel — structure guide sections as analysis codes
  - if: team records sessions via video
    use: grain or tl;dv — import guide as session agenda; tag transcript moments against guide sections
  - if: primary and secondary paths fail
    use: search_query to retrieve question templates; reference ux-researcher/research-plan for objective grounding
  - if: all paths fail
    use: best-guess output — label as inferred
---

## Purpose

Constructs a session guide for moderated qualitative research using semi-structured interview method as the primary frame. Applies laddering technique to surface underlying motivations, JTBD probing to reveal goal-driven behavior, and think-aloud protocol cues for evaluative sessions.

Does NOT conduct the session, transcribe recordings, synthesize findings, or recruit participants. Does NOT produce a rigid script — the guide supports moderation, not replacement of moderator judgment.

---

## Required Inputs and Assumptions

**Required inputs:**
- Research objective: the decision or uncertainty the sessions must inform
- Participant profile: who is being interviewed (role, behavior, experience level)
- Session duration: total time available for the session

**Known vs unknown:**
- If the research objective is stated — use it directly
- If the research plan exists — retrieve it via notion or the research-plan skill
- If participant criteria are missing — assume a primary user segment based on stated product context; label as assumption
- If session duration is missing — assume 60 minutes; label as assumption

**Rule:** If any required input is absent, infer and clearly label the inference as an assumption in the output section.

---

## Input Mode and Evidence Path

Evidence hierarchy applied to this skill:

1. Live/real interaction — not applicable (guide is pre-session)
2. Structured system access — research plan in Notion, linked study objectives, prior session notes
3. Design artifacts/documentation — research plan document, screener, any prior synthesis
4. Screenshots/static input — not applicable
5. Inference — used when research plan is absent or objectives are underspecified

**Path used:** Path 2 (Notion) when research plan is available. Path 3 when documentation exists outside Notion. Path 5 (inference) when inputs are missing — all inferences must be labeled.

**Limitations:** The guide is only as valid as the stated research objective. If the objective drifts during fieldwork, the guide may not support analysis.

---

## Tool Stack

**Runtime primary — Notion:** Store the interview guide as a linked page within the research plan. Version the guide before each session round. Use Notion to share the guide with the moderation team and collect pre-session comments.

**Runtime secondary — Dovetail:** Store the guide alongside session recordings. Use guide sections as tagging categories so captured evidence maps back to research questions post-session.

**Runtime secondary — Looppanel:** Structure guide sections as AI analysis codes. Looppanel will auto-code transcript moments against each research question during and after sessions.

**Optional session pairing — Grain:** Import the guide as a session agenda. Use clip-sharing to surface moments that answer specific guide questions for stakeholders.

**Optional session pairing — tl;dv:** Use the guide structure to tag transcript moments during recording. Best for lean teams with budget constraints.

**Fallback:** web search for question templates and reference to the research-plan skill when no plan document exists.

---

## Tool Routing

- Notion available + research plan linked → retrieve objective, write guide in Notion, link to plan
- Notion available + no plan → create guide in Notion, flag missing plan as a risk
- Dovetail in team stack → mirror guide sections as Dovetail tags before sessions begin
- Looppanel in team stack → define guide topics as Looppanel codes so auto-analysis aligns with guide intent
- Session will be recorded via video → pair with Grain (stakeholder-facing teams) or tl;dv (lean teams)
- Notion unavailable → write to deliverable file; use search_query to source question templates
- All tools unavailable → produce best-guess output; label as inferred

---

## Environment and Reproducibility

**Platform:** Sessions may be remote (Zoom, Google Meet, Teams) or in-person. The guide is platform-agnostic.

**State:** If a research plan exists in Notion, it must be retrieved before guide construction begins. If participant screener exists, it must be referenced for profile accuracy.

**Version:** The guide should be versioned before each session round (v1.0 for pilot, v1.1 for revisions post-pilot).

**If unknown:** If platform, session format, or participant count is not stated, explicitly note the assumption and flag for confirmation before sessions start.

---

## Model Building

Before writing any questions, the agent MUST construct a research objective model. No questions are drafted until this model is complete.

**Research objective model structure:**

```
Study goal: [The decision or uncertainty being addressed]
Research questions: [The 2–4 questions the sessions must answer]
Participant profile: [Who is being interviewed and why]
Evidence goals: [What types of evidence will answer each research question]
Session count: [How many sessions; pilot vs full round]
Analysis path: [How findings will be synthesized post-session]
```

This model determines which topics are mandatory, how much time each deserves, and which probing technique applies to each section.

---

## Core Method Execution

Guide construction follows this sequence. Do not skip steps.

**Step 1 — Retrieve and confirm the research objective model.**
Pull from Notion research plan if available. If not, construct the model from stated inputs. Label inferred elements.

**Step 2 — Build a topic map.**
List every topic the sessions need to cover. Map each topic to a research question. Mark topics as mandatory (directly answers a research question) or optional (useful but not essential).

**Step 3 — Select probing technique per topic.**
- Behavioral or motivational topics → laddering technique (ask about behavior, then "why", then "what does that mean to you")
- Goal or outcome topics → JTBD probing ("when [situation], you want to [goal], so you [behavior]")
- Evaluative or usability topics → think-aloud protocol cues ("as you look at this, talk me through what you're noticing")
- Exploratory or contextual topics → semi-structured open questions with minimal scaffolding

**Step 4 — Draft main questions.**
One main question per topic. Open-ended. Neutral language. No leading framing. Each question anchored to its research question and evidence goal.

**Step 5 — Design follow-up probes.**
2–4 probes per topic. Probes deepen, not redirect. At least one probe per topic uses the selected probing technique. Mark each probe as mandatory or optional.

**Step 6 — Sequence the guide.**
Order: warm-up → context and background → core topics (mandatory first) → optional topics → concept or stimulus (if evaluative) → close and reflection. Place lowest-stakes topics first to build rapport before probing sensitive areas.

**Step 7 — Conduct a bias review.**
Scan every question for: leading language, confirmation framing, assumption of behavior, and double-barreled structure. Rewrite flagged questions before finalizing.

**Step 8 — Write moderator notes.**
Add transition cues, time allocations, facilitation cautions, and instructions for handling off-topic responses.

---

## Structured Findings

Every guide section must follow this schema. No free-form sections. Every section must be traceable to a research question from the objective model.

```
### [Section name]

Topic: [One-line description of what this section covers]
Research question: [Which research question this section answers]
Evidence goal: [What type of evidence this section is designed to surface]
Time allocation: [Minutes; mark as mandatory or optional]

Main question:
[The single open-ended question the moderator asks]

Follow-up probes:
- [Probe 1] — [mandatory/optional] — [technique: laddering / JTBD / think-aloud / open]
- [Probe 2] — [mandatory/optional] — [technique]
- [Probe 3] — [mandatory/optional] — [technique]

Bias risks:
- [Risk 1: e.g., leading language in probe 2]
- [Risk 2: e.g., assumes prior behavior]

Moderator notes:
[Transition language, facilitation cautions, or skip conditions]
```

---

## Prioritization Logic

**Must-ask:** Questions directly answering a stated research question. These run in every session regardless of time pressure.

**Nice-to-have:** Questions that add depth or explore adjacent topics. These are skipped if the session runs long.

**Time-boxing rules:**
- Warm-up: no more than 10% of session time
- Core mandatory topics: at least 60% of session time
- Optional topics and close: remaining time
- If a session runs 10 minutes long: cut all optional probes first, then optional topics, then close early
- If a session runs 10 minutes short: deepen probing on the highest-priority topic using reserved optional probes

**Pilot session rule:** Run one pilot session before the full round. Use it to test time allocation and identify questions that generate non-answers. Revise the guide before the full round begins.

---

## Pattern Detection

Before finalizing the guide, the agent must check for:

**Topic clustering:** Are multiple questions probing the same behavior from different angles without distinct evidence goals? Consolidate if yes.

**Probe coverage gaps:** Does every mandatory topic have at least one probe using the selected technique? If not, add it.

**Leading question risks:** Does any question contain: "don't you think", "wouldn't you say", embedded assumptions about frequency or preference, or superlatives? Rewrite.

**Missing evidence goals:** Does every section have a stated evidence goal? If any section exists without one, it must be cut or reanchored to a research question.

**Participant profile hallucination risk:** Has any question been written that assumes a behavior or experience not confirmed in the screener? Flag and rewrite as exploratory.

---

## Recommendations

Recommendations must link to the research objective. They are directional, not prescriptive.

- **Sequencing:** Place the most sensitive or high-stakes topic in the second half of the session, after rapport is established. Never open with it.
- **Probing strategy:** Default to laddering for motivational topics. Switch to JTBD framing when participants describe past behavior — it surfaces the goal behind the action without asking "why" repeatedly.
- **Think-aloud cues:** For evaluative sessions, place think-aloud prompts at the start and reinforce them after silence exceeds 5 seconds. Do not interpret silence as non-engagement.
- **Probe depth:** Two probes per topic is the minimum. Four is the maximum before the session loses momentum. Reserve the deepest probe for the topic with the highest research priority.
- **Neutrality check:** If any team member wrote the questions, run a second-pass bias review with someone who was not involved in the study design.

---

## Coverage Map

After the guide is finalized, document coverage explicitly:

**Fully covered:** Research questions with at least one mandatory main question and two probes mapped to a clear evidence goal.

**Partially covered:** Research questions with a main question but weak or missing probes, or where the evidence goal is ambiguous.

**Not covered:** Research questions from the objective model with no corresponding guide section. Must be flagged — either add coverage or document the gap and its impact on the study.

The coverage map must be included in the `### Evidence goals` section of the deliverable.

---

## Limits and Unknowns

This guide does not guarantee:

- **Moderator skill:** A well-structured guide does not compensate for poor facilitation. Probes require judgment to deploy at the right moment.
- **Participant articulation:** Some participants will not answer open questions with useful depth. The guide cannot control this. Moderator notes should include instructions for re-probing without leading.
- **Session variability:** Topic order, time pressure, and participant energy will vary. The guide is a scaffold, not a script.
- **Transferability:** A guide built for one participant segment may not transfer to another without revision.
- **Post-session analysis alignment:** The guide supports analysis but does not guarantee that guide sections will map cleanly to emergent themes. Synthesis may surface topics the guide did not anticipate.

---

## Workflow Rules

1. Build the research objective model before writing any questions.
2. Anchor every question to a research question in the model.
3. Distinguish mandatory from optional at both the topic and probe level.
4. Write no leading questions. Run bias review before finalizing.
5. Do not hallucinate participant profiles. If the screener does not confirm a behavior, treat it as unknown.
6. Version the guide before each session round.
7. Run a pilot session and revise before the full round begins.
8. If inputs are missing, infer and label — do not silently assume.

---

## Output Contract

**Write to:** `logs/active/<project-slug>/deliverables/ux-researcher.md`

**Update only:** The section named `## Skill: interview-guide-build`

**On first run:** If the deliverable does not exist, create it with one YAML header, this skill section, and one trailing `## Reflection` block.

**Preserve:** All other skill sections in the shared role deliverable. Do not modify sections owned by other skills.

**Reflection update:** Append or refresh `### interview-guide-build` under `## Reflection` with:
- What worked
- What didn't
- Next steps

**Label the path used:** Every output section must be labeled `sourced` (from Notion or linked plan), `fallback` (from search or research-plan skill), or `inferred` (constructed from incomplete inputs).

**Done when:** A moderator can run all sessions from the guide without improvising the core script, every question is traceable to a research objective, and mandatory and optional probes are explicitly separated.
