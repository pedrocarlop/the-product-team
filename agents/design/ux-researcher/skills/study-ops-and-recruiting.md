---
name: study-ops-and-recruiting
description: Applies the ResearchOps framework to design and execute the full operational pipeline for a study — recruiting, screening, scheduling, consent, incentives, and closeout logistics.
trigger: When a study design exists and a concrete execution plan is needed to schedule, staff, and run sessions.
required_inputs:
  - Study brief or research plan (method, session count, participant criteria)
  - Timeline and target session dates
  - Team ownership map (who runs sessions, who handles comms)
recommended_passes:
  - Run after study-design and screener-form-build
  - Feed outputs into synthesis and findings skills
best_guess_output: A structured study ops plan with recruiting pipeline, scheduling setup, consent process, incentive plan, and contingency design for each lifecycle phase.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher-study-ops-and-recruiting.md
done_when: Every ops component has a named owner, a tool, a handoff point, and a documented contingency. The study can be scheduled, staffed, and launched without open operational blockers.
tool_stack:
  runtime:
    primary: notion, rally_uxr
    secondary: calendly, ethnio, google_forms
  artifacts:
    primary: notion (ops plan), rally_uxr (participant CRM, scheduling, incentives)
  fallback:
    primary: screener-form-build skill, open/browser
tool_routing:
  - if: team has Rally UXR
    then: use Rally UXR as the single ops hub (CRM + scheduling + incentives via Tremendous)
  - if: in-product recruiting is needed
    then: add Ethnio for intercept + screening + pool management
  - if: ops platform is unavailable or not set up
    then: use Notion for plan documentation + Calendly for scheduling + Tremendous directly for incentives
  - if: external panel sourcing is needed
    then: route through User Interviews (managed recruitment), Prolific (demographic precision), or Respondent (B2B niche)
  - if: no tools available
    then: produce best-guess plan labeled "inferred" and flag setup requirements
---

# Study Ops and Recruiting

## Purpose

This skill applies the ResearchOps community framework (UXPA ResearchOps) to design and execute the full operational pipeline for a research study. It covers every phase from recruiting pipeline design through study closeout.

Reasoning type: dependency modeling + operational planning. The agent maps the operational dependency chain first, then designs each component against that chain.

This skill does NOT do: study design, discussion guide writing, analysis, or synthesis. It operates from an existing study brief and produces the logistics layer that enables sessions to happen.

---

## Required Inputs and Assumptions

**Required:**
- Study brief (method, session count, participant profile, session duration)
- Target session window (start date, end date)
- Team roster with assigned roles (moderator, notetaker, recruiter, ops owner)

**Known vs. unknown:**
- If participant criteria are missing → assume general target audience from product context and label as assumption
- If session count is missing → assume n=5 per segment as a starting default (label as assumption)
- If timeline is missing → assume 3-week recruiting lead time minimum (label as assumption)
- If team roster is missing → flag as unresolved; ownership must be explicit before launch

**Rule:** If required inputs are absent, infer minimum viable values, label each clearly as `[assumption]`, and continue building the plan. Do not block on missing inputs.

---

## Input Mode and Evidence Path

Evidence path used: **(3) Design artifacts and documentation** — the ops plan is built from the study brief, existing team context, and tool configuration knowledge.

Where live system access exists (Notion, Rally UXR via MCP), pull current project state and update in place. Where it does not, produce a fully documented plan ready for manual implementation.

**Limitations:** This skill cannot verify real-time tool availability, participant panel health, or calendar conflicts. Assumptions about lead times are based on standard ResearchOps benchmarks and must be validated against the actual recruiting environment.

---

## Tool Stack

**Runtime primary — ops planning and documentation:**
- **Notion** — Central ops hub. Houses the living study ops plan, consent templates, recruiting tracker, and logistics documentation. Updated throughout the study lifecycle.
- **Rally UXR** — Purpose-built ResearchOps platform. Manages participant CRM, study scheduling, incentive distribution (via Tremendous integration), and panel management. Primary choice for teams scaling a research ops function.

**Runtime secondary — scheduling and recruiting:**
- **Calendly** — General-purpose scheduling with calendar sync, buffer times, and round-robin routing. Use as standalone scheduling layer when Rally UXR is not available.
- **Ethnio** — In-product intercept + screener + scheduling + participant pool (CRM) + incentives. Use when in-product recruiting is required or the team owns its participant relationships.
- **Google Forms** — Zero-cost consent and intake forms. Use for lightweight consent collection when dedicated tooling is not available.

**Recruitment platforms (sourcing layer):**
- **User Interviews** — Full-service recruitment with managed scheduling. Best for B2C audiences with moderator-led sessions.
- **Prolific** — Academic-grade panel with precise demographic targeting. Best for quantitative or mixed-methods studies requiring demographic precision.
- **Respondent** — 4M+ verified B2B participants. Best for niche professional or enterprise audiences.
- **UserTesting** — Integrated platform for fast video feedback turnaround.
- **Sprig** — In-product micro-surveys for continuous discovery without scheduling overhead.

**Artifacts:** Notion (ops plan document), Rally UXR (CRM records, scheduling links, incentive payouts).

**Fallback:** screener-form-build skill (screener construction support), open/browser (reference and manual documentation).

---

## Tool Routing

- **Rally UXR available** → use as single ops hub: CRM, scheduling, incentives. Supplement with Notion for plan documentation.
- **In-product recruiting required** → add Ethnio for intercept + screener + pool. Connect to Calendly or Rally UXR for scheduling.
- **No dedicated ops platform** → Notion (docs) + Calendly (scheduling) + Tremendous (incentives, direct) + Google Forms (consent).
- **External panel needed** → User Interviews for managed B2C, Prolific for demographic precision, Respondent for B2B niche. Do not rely on a single sourcing channel.
- **Consent tooling unavailable** → Google Forms as minimum viable consent. Document process fully regardless of tool.
- **All tools unavailable** → produce complete ops plan as `[inferred]` documentation. Flag tool setup as a pre-launch blocker.

---

## Environment and Reproducibility

- **Platform:** Web-based tools (Notion, Rally UXR, Ethnio, Calendly, Tremendous). No local environment required.
- **Auth state:** Assumes team has access to configured workspace. If not → flag as blocker in the ops plan.
- **Data state:** Participant CRM state is unknown at plan time. Assume cold start unless existing panel is confirmed.
- **Version:** Tool capabilities as of 2025. Rally UXR Tremendous integration, Ethnio pool CRM, and Prolific demographic targeting are current capabilities.
- **Reproducibility:** This plan is a living document. Re-run the skill to update the ops plan as the study progresses.

---

## Model Building

Before any planning, the agent constructs the operational dependency model for the study lifecycle. No scheduling, no recruiting, no consent design happens before this model is complete.

**Operational dependency model:**

```
[Recruiting pipeline]
    → Screener live + sourcing channels active
    → Qualified leads in CRM

[Screening]
    → Screener responses reviewed
    → Disqualified participants removed
    → Qualified participants moved to scheduling pool

[Scheduling]
    → Calendar availability set (moderator + notetaker)
    → Scheduling links generated
    → Confirmation + reminder comms active

[Consent]
    → Consent form finalized and legally reviewed
    → Consent collected before session starts (hard gate)
    → Consent records stored

[Session]
    → Confirmed participants with consent on record
    → Moderator, notetaker, and tools ready
    → Recording/note-taking consent confirmed in session

[Incentive]
    → Incentive amount and format agreed
    → Delivery mechanism set up (Tremendous, Rally UXR, or manual)
    → Payout triggered within agreed window post-session

[Closeout]
    → No-shows and cancellations logged
    → Unfilled slots assessed for re-recruiting
    → Participant records updated in CRM
    → Incentive delivery confirmed
```

**Critical path:** Consent must be in place before scheduling opens. Recruiting has the longest lead time and must start first. Incentive setup must be confirmed before the first session.

---

## Core Method Execution

Grounded in: UXPA ResearchOps community framework, participant pipeline management, GDPR-aware consent management, IRB-style consent best practices, incentive compliance.

**Step 1 — Define the recruiting target**
- Extract participant criteria from study brief: demographics, behaviors, product usage, professional attributes.
- Define inclusion and exclusion criteria explicitly. Document disqualifiers.
- Set target n per segment. Add 30–40% buffer for no-shows and drop-off (e.g., need 8 completed sessions → recruit 11–12).

**Step 2 — Design the recruiting pipeline**
- Select sourcing channels based on participant profile (see tool routing). Do not use a single channel.
- Configure screener in Rally UXR or Ethnio (or screener-form-build skill as fallback).
- Set up participant CRM: status stages → Applied, Screened, Qualified, Scheduled, Confirmed, Completed, No-show.
- Define screener review cadence (daily during active recruiting window).

**Step 3 — Set up scheduling**
- Block moderator and notetaker calendars for session window.
- Configure scheduling tool (Rally UXR scheduler or Calendly): session duration, buffer time (minimum 15 min between sessions), max sessions per day.
- Generate scheduling links by segment if running multiple cohorts.
- Set up automated confirmation and reminder sequences (24h and 1h before session).

**Step 4 — Design the consent process**
- Draft consent form: study purpose, activities, recording notice, data use, right to withdraw, contact information.
- Apply GDPR-aware language: explicit opt-in, data retention policy, right to erasure.
- For sensitive topics or vulnerable populations: apply IRB-style review standard (independent review before fielding).
- Set consent as a hard gate: no participant proceeds to scheduling without signed consent.
- Store consent records in a durable, retrievable location (Notion, Rally UXR, or Google Drive).

**Step 5 — Design the incentive plan**
- Confirm incentive amount (benchmarks: $1–$3/min for consumer, $2–$5/min for professional, $5–$10/min for executive/specialist).
- Select delivery mechanism: Rally UXR (Tremendous integration), Tremendous direct, or gift card manual.
- Confirm compliance requirements: tax thresholds ($600 USD for US participants), international payout restrictions.
- Set delivery timeline: within 48–72 hours post-session as default.
- Communicate incentive terms to participants before session.

**Step 6 — Design contingencies**
- No-show plan: define threshold (e.g., >20% no-show rate triggers re-recruiting).
- Cancellation plan: define reschedule window and cancellation policy.
- Screener under-performance plan: identify backup sourcing channel before launch.
- Technical failure plan: define what happens if recording, video, or consent tool fails during a session.

**Step 7 — Assign ownership and document the plan**
- Name an owner for every ops component.
- Write the complete ops plan into the Notion document and the deliverable file.
- Review plan with the full team before recruiting opens.

---

## Structured Findings

Use the following schema for each ops component. Document all components before the study launches.

```
### [Ops Component Name]
Phase: [recruiting | screening | scheduling | consent | session | incentive | closeout]
Owner: [named person or role]
Tool: [primary tool, fallback tool]
Steps:
  1. [step]
  2. [step]
  ...
Handoff: [what triggers the next phase, who receives the handoff]
Failure mode: [what breaks this component]
Contingency: [what happens when it breaks]
```

**Example — Recruiting:**
```
### Recruiting Pipeline
Phase: recruiting
Owner: Research Ops Lead
Tool: User Interviews (primary), Prolific (backup)
Steps:
  1. Publish screener to User Interviews panel
  2. Set daily review of incoming responses
  3. Move qualified candidates to scheduling pool in Rally UXR
  4. If <50% fill rate by Day 5, activate Prolific channel
Handoff: Qualified candidates in CRM → scheduling step begins
Failure mode: Panel exhaustion, screener disqualifying too many candidates
Contingency: Loosen one non-critical inclusion criterion; activate backup channel; extend recruiting window by 3 days
```

---

## Prioritization Logic

**Sequence by dependency:**

1. **Consent process** — must be designed and reviewed before any participant communication. Hard gate.
2. **Recruiting pipeline** — longest lead time. Start immediately after consent is finalized. Cannot parallelize with consent.
3. **Incentive setup** — must be confirmed before first session. Can parallelize with recruiting.
4. **Scheduling setup** — configure after consent and CRM are live. Calendars blocked early; links generated once screener is active.
5. **Screener configuration** — parallelize with scheduling setup.
6. **Reminder and communication sequences** — set up after scheduling is configured.
7. **Contingency documentation** — complete before recruiting opens.

**What can parallelize:** Incentive setup, scheduling configuration, screener build, and reminder setup can all run concurrently once consent is finalized and recruiting is live.

**Longest lead time:** Recruiting. External panel sourcing through User Interviews or Respondent requires minimum 5–10 business days for niche audiences. Always start recruiting first.

---

## Pattern Detection

The agent must identify the following risks in every ops plan:

**Single points of failure:**
- Single sourcing channel → add backup channel before launch
- Single moderator with no backup → identify backup before scheduling opens
- Consent stored in only one location → duplicate to a second location

**Scheduling bottlenecks:**
- No buffer time between sessions → force minimum 15 min buffer
- Too many sessions per day for one moderator → cap at 4 sessions/day per moderator
- No automated reminders → manual follow-up creates load and increases no-show rate

**Consent gaps:**
- Consent collected after scheduling (not before) → reorder to hard gate
- No recording consent collected in session → add explicit verbal confirmation at session start
- Consent form missing data retention or right-to-withdraw language → flag for legal review

**Incentive compliance risks:**
- No tax threshold tracking for high-value incentives (>$600 USD in a calendar year per participant) → add tracking
- International participants with local payout restrictions → confirm Tremendous country coverage before recruiting
- Incentive terms not communicated before session → add to confirmation email

---

## Recommendations

Recommendations must link to identified ops risks. Do not produce generic best practices.

**Format:**
- Risk: [identified failure mode or gap]
- Recommendation: [specific action]
- Where to add buffer or automation: [specific point in the pipeline]

**Standing recommendations for all studies:**
- Risk: Single sourcing channel fails or under-performs
  Recommendation: Always activate a backup channel before Day 5 of recruiting. Do not wait for failure.
  Buffer point: Build backup channel setup into the recruiting kickoff, not the contingency plan.

- Risk: No-show rate degrades session count
  Recommendation: Recruit 30–40% above target. Send reminder at 24h and 1h before session.
  Automation point: Automate reminders in Rally UXR or Calendly — do not rely on manual outreach.

- Risk: Consent collected after scheduling opens
  Recommendation: Configure consent as a required step before scheduling link is accessible. Use Rally UXR gating or a Google Form + manual check.

- Risk: Incentive delivery delayed or failed
  Recommendation: Use Tremendous (via Rally UXR or direct) for same-day payout capability. Do not rely on manual gift card delivery for studies with >5 participants.

---

## Coverage Map

| Study Lifecycle Phase | Coverage |
|---|---|
| Screener design | Partial — screener-form-build skill owns screener construction; this skill integrates it |
| Recruiting pipeline design | Full |
| Sourcing channel selection | Full |
| Screening and qualification | Full |
| Scheduling setup | Full |
| Consent process design | Full |
| Session logistics | Partial — session facilitation is owned by the moderator; this skill covers pre-session ops |
| Incentive plan and delivery | Full |
| Participant CRM management | Full |
| Closeout and no-show handling | Full |
| Data analysis and synthesis | Not covered — owned by research-synthesis skill |
| Legal/compliance review | Not covered — must involve legal or compliance team for GDPR/IRB-level review |

---

## Limits and Unknowns

This skill cannot guarantee:

- **Participant no-show rates** — benchmarks are available (15–25% for consumer, 10–20% for professional) but actual rates depend on participant quality, incentive, and timing.
- **Tool availability** — Rally UXR, Ethnio, Calendly, and Tremendous uptime is not verified at plan time. Flag tool dependencies as operational risks.
- **Screener performance** — qualification rate depends on panel quality and screener design. A screener that qualifies <30% of applicants may require sourcing adjustment.
- **Legal and compliance edge cases** — GDPR, CCPA, and IRB standards vary by jurisdiction, study type, and participant vulnerability. This skill applies standard best practices but does not substitute for legal review.
- **Incentive international compliance** — Tremendous covers 200+ countries but not all. Verify country coverage for international studies before recruiting opens.
- **Calendar availability** — moderator and notetaker availability is assumed. Confirm and block calendars before publishing scheduling links.

---

## Workflow Rules

1. **Build the dependency model before scheduling.** No scheduling links, no recruiting posts, no participant communications until the dependency model is documented.
2. **Make ownership explicit.** Every ops component must have a named owner before the plan is considered complete. "Team" is not an owner.
3. **No single-threaded recruiting.** Always activate or designate a backup sourcing channel before the recruiting window opens.
4. **Document the consent process fully.** Consent form, delivery method, storage location, and retrieval process must all be documented — not just the form itself.
5. **Consent is a hard gate.** No participant reaches scheduling without consent on record.
6. **Incentive terms before sessions.** Participants must know incentive amount, format, and delivery timeline before the session — not after.
7. **Closeout is part of ops.** Logging no-shows, confirming incentive delivery, and updating CRM records are required steps, not optional cleanup.

---


**Required deliverable sections within `## Skill: study-ops-and-recruiting`:**
- `### Study schedule` — timeline, session window, recruiting milestones
- `### Recruiting flow` — sourcing channels, screener link, qualification criteria, CRM stages
- `### Consent and logistics` — consent form location, delivery method, storage, session tool setup
- `### Staffing and ownership` — named owner for every ops component
- `### Incentive plan` — amount, format, delivery mechanism, compliance notes
- `### Risks and contingencies` — failure modes and contingency for each ops component
