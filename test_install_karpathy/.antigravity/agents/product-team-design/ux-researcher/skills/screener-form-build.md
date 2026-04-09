---
name: screener-form-build
description: Applies participant profiling, quota sampling logic, and screener design best practices to build a form that recruits the right people with minimum respondent burden.
trigger: When a study needs recruitment filtering — qualitative or quantitative — and inclusion/exclusion criteria must be operationalized into a form.
mesh:
  inputs:
    - ux-researcher:research-plan
  next:
    - ux-researcher:study-ops-and-recruiting
  context: "Filters potential participants to ensure study validity."
best_guess_output: A structured screener with participant profile model, qualification logic per question, quota targets, and backup plan.
output_artifacts:
  - knowledge/ux-researcher-screener-form-build.md
  - knowledge/assets/ (for visual artifacts)
done_when: The screener contains a documented participant profile model, ≤10 questions with explicit qualify/disqualify logic per answer, quota targets, and a named tool path used to deploy it.
required_inputs:
  - research plan (study goals, participant type, sample size)
  - study method (e.g., usability test, interview, survey)
recommended_passes: 2 — first pass builds participant profile model and criteria; second pass writes and validates questions
tool_stack:
  runtime:
    primary: Typeform
    secondary: Google Forms, Tally
  artifacts:
    primary: knowledge/ux-researcher.md
  fallback:
    primary: Notion (structured questionnaire doc), research-plan skill (criteria source)
tool_routing:
  - if: completion rate and participant experience are priorities
    use: Typeform (conversational, one-question-at-a-time, conditional logic)
  - if: zero setup cost or internal-only screener
    use: Google Forms (native Sheets integration, no overhead)
  - if: lean team, free tier required, GDPR compliance needed
    use: Tally (unlimited responses, broad question types)
  - if: screener and participant recruitment must be in one tool
    use: Lyssna or User Interviews or Prolific (native screener + panel)
  - if: recruiting from a live product via intercept
    use: Ethnio (intercept-based with built-in screener)
  - if: enterprise org with existing contract
    use: SurveyMonkey or Qualtrics
  - if: all tools unavailable
    use: Notion for structured questionnaire doc; label output as fallback
---

# Screener Form Build

## Purpose

This skill builds a participant screener by constructing a participant profile model first, then translating that model into a deployment-ready form. It applies quota sampling logic to set realistic targets and screener design best practices — behavioral disqualifiers, progressive disclosure, short length — to maximize completion rate without sacrificing sample quality.

It does NOT conduct participant outreach, manage scheduling, or write a discussion guide. It does NOT write questions before the participant profile model is complete.

---

## Required Inputs and Assumptions

**Required:**
- Research plan with study goals, target participant type, and sample size targets.
- Study method (moderated interview, unmoderated usability test, survey, diary study, etc.).

**Known vs unknown:**
- If a research plan exists, pull inclusion/exclusion criteria from it directly.
- If no research plan exists, infer criteria from the study method and goals, label all inferred criteria as `[assumption]`, and flag for researcher review before deployment.

**Rule:** Missing inputs are never blockers. Infer, label, and proceed.

---

## Input Mode and Evidence Path

Path used: **(3) Design artifacts / documentation** as primary, **(5) Inference** as fallback.

- Primary: Read the research plan deliverable or brief to extract participant type, behaviors, and constraints.
- Fallback: If no documentation is available, infer participant profile from study method context and label all inferred attributes.

**Limitations:** Screener quality is bounded by the specificity of the research plan. If criteria are vague, the screener will flag this and use conservative qualifying logic.

---

## Tool Stack

**Runtime primary — Typeform:** Conversational, one-question-at-a-time format with conditional logic and branching. Highest completion rate. Use when participant experience and perceived form quality matter.

**Runtime secondary — Google Forms:** Zero-cost, zero-friction. Native Google Sheets integration for live data monitoring. Use for internal screeners or when speed of setup is the constraint.

**Runtime secondary — Tally:** Free-tier-generous, GDPR compliant, unlimited responses. Use for lean teams that cannot pay Typeform prices but need more control than Google Forms.

**Integrated alternatives — Lyssna / User Interviews / Prolific / Respondent:** Screener built natively inside the recruitment platform. Eliminates the need for a separate form tool. Use when the same platform manages both recruiting and testing.

**Intercept — Ethnio:** Recruits from a live product with built-in screener. Use when the target participant is an active product user.

**Enterprise — SurveyMonkey / Qualtrics:** Use when the org has an existing contract or needs longitudinal tracking alongside UX research.

**Fallback — Notion:** Structured questionnaire documented as a Notion page when no form tool is accessible. Label output as `fallback`.

---

## Tool Routing

- Completion rate and experience are priorities → **Typeform**
- Zero cost, internal audience, or Google Workspace org → **Google Forms**
- Free tier + GDPR required, lean team → **Tally**
- Single-tool for screener + recruitment → **Lyssna / User Interviews / Prolific**
- Recruiting from live product → **Ethnio**
- Enterprise contract exists → **SurveyMonkey / Qualtrics**
- All tools unavailable → **Notion** (label: fallback)

Prefer combining: use a dedicated form tool for the screener and a recruitment platform for distribution, unless the recruitment platform has native screener support.

---

## Environment and Reproducibility

- Platform and device are unknown at skill invocation; assume web-based form tool access.
- Auth state: unknown — if tool requires login and access is not confirmed, fall back to Notion.
- Version: tool features described reflect 2025 capabilities; branching logic and quota caps may vary by plan tier.
- If tool is unavailable or out of credits, switch to next tool in routing order and document the path used.

---

## Model Building

**The agent MUST construct a participant profile model before writing any screener questions.**

### Participant Profile Model schema

```
Target user definition:
  Description: [who this person is in behavioral/contextual terms]
  Primary use case or context: [what they do that's relevant to the study]

Inclusion criteria:
  - [criterion 1]: [why it's required]
  - [criterion 2]: [why it's required]

Exclusion criteria:
  - [criterion 1]: [why it disqualifies — conflict of interest, wrong context, etc.]
  - [criterion 2]: [why it disqualifies]

Quota logic:
  Total target: [n]
  Segments:
    - [segment label]: [n or %] — [rationale]
    - [segment label]: [n or %] — [rationale]
  Backup quota: [n additional, if primary sample is hard to recruit]

Assumption flags:
  - [any criterion inferred without source — label [assumption]]
```

Do not proceed to question design until this model is written and reviewed.

---

## Core Method Execution

### Step 1 — Source the research plan
Read the research plan deliverable. Extract: study goals, target participant type, key behaviors or contexts, sample size, and any explicit inclusion/exclusion criteria. If the plan is absent, infer and flag.

### Step 2 — Build the participant profile model
Complete the schema above. Define inclusion criteria (must-have attributes), exclusion criteria (disqualifying attributes), and quota segments with targets. Flag assumptions.

### Step 3 — Map criteria to question types
For each criterion, determine the question type that operationalizes it:
- Demographic criterion → single-choice or short-answer question
- Behavioral criterion → frequency, recency, or scenario question
- Attitudinal criterion → scaled or multiple-choice question
- Conflict of interest / professional exclusion → direct yes/no disqualifier

### Step 4 — Write questions in priority order
Order: demographics → behavioral/attitudinal qualifiers → topic-specific disqualifiers.
Rules:
- Put the most critical disqualifier as early as possible.
- Keep total question count ≤ 10 for completion rate.
- Use behavioral disqualifiers ("In the past 3 months, how often have you...") not leading questions ("Do you use our product regularly?").
- Apply progressive disclosure: if a respondent is already disqualified, branch them to end without showing remaining questions.

### Step 5 — Define branching and qualification logic
For each answer option, state: qualify, disqualify, or continue. Make this explicit — do not leave recruiter inference.

### Step 6 — Set quota caps
Define how many people in each segment can qualify. Prevent over-recruitment of one segment.

### Step 7 — Deploy to chosen tool
Apply tool routing. Build form in selected tool. Configure branching logic. Set disqualify screens. Test the form before distribution.

### Step 8 — Write backup plan
State what happens if the primary quota is not met within the recruitment window: adjusted criteria, extended timeline, alternative panel, or looser segment definition.

---

## Structured Findings

Use this schema for every screener question.

```
Screener Question
Number:
Question text:
Answer options:
Qualifying logic:
  Include if:
  Exclude if:
Rationale:
```

**Example:**

```
Screener Question
Number: 3
Question text: In the past 3 months, how often have you managed a project with more than 2 collaborators?
Answer options:
  A. Never
  B. Once or twice
  C. Monthly
  D. Weekly or more
Qualifying logic:
  Include if: C or D
  Exclude if: A or B
Rationale: Study requires active project management behavior; infrequent users will not represent the target context.
```

---

## Prioritization Logic

Order questions as follows:

1. **Hard disqualifiers first** — profession/industry exclusions (e.g., "Do you work in market research?"), age requirements. Eliminates unqualified respondents before they invest time.
2. **Primary behavioral qualifiers** — frequency, recency, or context of the target behavior. Core filter.
3. **Secondary behavioral qualifiers** — sub-behaviors or contexts that define segment.
4. **Attitudinal or needs-based qualifiers** — used for segment diversity, not primary filtering.
5. **Demographics** — collect last; they do not disqualify in most studies and are less sensitive when asked after rapport is established through earlier questions.

Exception: if a demographic criterion is a hard requirement (e.g., age gate, geography), move it to position 1–2.

---

## Pattern Detection

Before finalizing the screener, check for:

- **Overlapping criteria:** Two questions that test the same attribute — consolidate into one.
- **Redundant questions:** Questions whose answer is already implied by a previous answer — remove.
- **Criteria too narrow (undersupply risk):** Multiple simultaneous qualifiers that produce a very small addressable population. Flag and propose a tiered alternative (primary criteria + desirable criteria).
- **Criteria too broad (wrong sample risk):** A qualifier so common that it does not actually filter — tighten with frequency or recency.

Document findings in an `### Ops notes` subsection.

---

## Recommendations

Each recommendation must link to a criterion in the participant profile model.

- State quota targets per segment with rationale.
- Flag any criterion that is likely to produce undersupply and propose a backup criterion.
- Recommend recruitment channel based on participant type (panel, intercept, internal database, social).
- Note if incentive level should be adjusted for hard-to-recruit profiles.
- If using a recruitment platform with native screener (Lyssna, Prolific, User Interviews), recommend building screener natively to reduce tool fragmentation.

---

## Coverage Map

Document what the screener can and cannot address.

| Profile attribute | Coverage status | Notes |
|---|---|---|
| [attribute] | Covered | Question [n] addresses directly |
| [attribute] | Partially covered | Proxy question used; not a direct measure |
| [attribute] | Not addressable | Cannot be verified via self-report screener |

Attributes that are not addressable via screener should be moved to session-start verification (e.g., ask during scheduling confirmation or at the start of the session).

---

## Limits and Unknowns

The screener cannot control:

- **Participant honesty:** Respondents may game answers to qualify. Behavioral questions reduce but do not eliminate this risk.
- **Panel quality:** Third-party panels (Prolific, User Interviews) vary in attentiveness and demographic accuracy. Always include an attention check if using panels at scale.
- **Dropout rate:** Expect 30–60% dropout between screener completion and session attendance. Recruit above target accordingly.
- **Self-report accuracy:** Frequency and recency questions rely on participant memory. Treat as approximate.
- **Demographic representation:** A screener can set targets but cannot guarantee representation without quota enforcement in the recruitment platform.

---

## Workflow Rules

1. Build the participant profile model before writing any questions.
2. Put the most critical disqualifier at or near question 1.
3. Keep total questions ≤ 10. If more are needed, move lower-priority criteria to session-start verification.
4. Make qualification logic explicit per answer option. Do not leave recruiter inference.
5. Label all inferred criteria as `[assumption]`.
6. Match tool selection to team constraints (cost, speed, completion rate priority).
7. Test the form before distributing — verify branching sends disqualified respondents to end screen.
8. Do not hallucinate criteria not present in the research plan or explicitly flagged as assumptions.

---

  - `### Participant profile model` — completed schema
  - `### Screening questions` — all questions in structured schema format
  - `### Qualification logic` — qualify/disqualify rules per answer
  - `### Quota targets` — segment targets and backup quota
  - `### Coverage map` — attribute coverage table
  - `### Ops notes` — tool path used, compensation, cadence, pattern detection findings
  - `### Backup plan` — what to do if primary quota is not met
- Record which tool path was used and label the section: `sourced`, `fallback`, or `inferred`.
- Do NOT modify any other skill sections in the shared role deliverable.
- Update the role-level `## Reflection` footer by appending or refreshing `### screener-form-build` with `What worked`, `What didn't`, and `Next steps`.
- Done when: the screener has a documented participant profile model, ≤10 questions with explicit qualify/disqualify logic per answer, quota targets, and a named tool path.

---

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/ux-researcher-screener-form-build.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.
