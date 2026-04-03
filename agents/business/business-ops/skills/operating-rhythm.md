---
name: operating-rhythm
description: Encode expert meeting models (Lencioni, Rockefeller) into a 2026-ready AI-automated cadence.
trigger: When synchronization breaks, decisions are slow, or rituals feel "stale."
best_guess_output: A high-performance operating rhythm blueprint with automated triage and intelligence capture.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops-operating-rhythm.md
done_when: Cadence is mapped to DRI owners, Lencioni meeting types, and integrated with the 2026 tool stack.
---

# Operating Rhythm

## Purpose
Establish a high-performance execution cadence that minimizes meeting fatigue while maximizing decision velocity. This skill applies **Lencioni’s Meeting Advantage** and **Rockefeller Habits** to ensure every ritual has a clear DRI, a specific purpose, and an automated intelligence loop using 2026 toolsets.

## Required Inputs and Assumptions
Define the following before analysis:
- **Calendar Audit**: Current meeting load and distribution.
- **Strategy Artifacts**: OKRs in Profit.co, projects in Linear.
- **Team structure**: DRI assignments and headcount.
- **Assumptions**: If inputs are missing, the skill infers a "High-Growth Scaling" baseline (Daily Huddle, Weekly Tactical, Monthly Strategic, Quarterly Planning).

## Input Mode and Evidence Path
Gather evidence hierarchically:
1. **Live Signals**: Fireflies.ai transcripts and Fellow.app agenda archives.
2. **System State**: Profit.co OKR progress and Linear/Asana execution velocity.
3. **Static Input**: Screenshots of weekly/monthly team calendars.
4. **Inference**: Based on standard Rockefeller Habits if no data is provided.

## Tool Stack (Capabilities)
Define access layers:
- **Intelligence Layer**: Fireflies.ai (Intelligence Capture).
- **Ritual Layer**: Fellow.app (Ritual Management).
- **Strategy Layer**: Profit.co (Strategy Execution).
- **Automation Layer**: Zapier Central (AI Triage/Signal routing).

## Tool Routing (Decision System)
- **IF** real-time meeting intelligence is required **USE** [Fireflies.ai].
- **IF** ritual enforcement and agenda management are needed **USE** [Fellow.app].
- **IF** strategy-to-execution alignment is the goal **USE** [Profit.co].
- **IF** automated triage from voice-to-ticket is needed **USE** [Zapier Central].

## Environment and Reproducibility
- **State**: Current rituals, attendee load, and decision bottleneck log.
- **Version**: Current Organizational Chart and OKR cycle.
- **Reproducibility**: Must be reproducible using the same calendar snapshot and OKR state.

## Model Building (Before Analysis)
Before evaluating rhythm, the agent must construct:
1. **Synchronization Map**: Classify existing meetings into Lencioni’s types (Administrative, Tactical, Strategic, Developmental).
2. **Signal-to-Action Model**: Map how signals flow from Capture (Fireflies) -> Triage (Zapier) -> Execution (Linear).
3. **DRI Inventory**: Mapping every ritual to a singular accountable owner.

## Core Method Execution
1. **Ritual Audit**: Identify and tag "Zombie" meetings (low value, high frequency).
2. **Cadence Design**: Restructure the flow using Rockefeller Habits (Daily Huddles for alignment, Weekly Tactical for KPI review).
3. **DRI Assignment**: Ensure every meeting has one Directly Responsible Individual.
4. **Tool Orchestration**:
   - Configure **Fellow.app** for pre-meeting async contributions.
   - Set **Fireflies.ai** as the default "AI Scribe" for all sessions.
   - Link **Profit.co** dashboards to the Monthly Strategic review.
5. **Automation Loop**: Deploy **Zapier Central** to monitor Action Item signals and auto-populate backlogs.

## Structured Findings
Each finding must include:
- **Observation**: Meeting type, duration, and objective.
- **Efficiency Score**: 1-10 based on Lencioni criteria.
- **Content Density**: Ratio of "Updates" vs "Decisions".
- **DRI Coverage**: Confirmation of singular accountability.

## Prioritization Logic
- **P0**: Missing DRIs for core ceremonies or tactical session "Slippage".
- **P1**: Meeting high "Update" density replacing async communication.
- **P2**: Disconnect between meeting content and Profit.co OKRs.

## Pattern Detection
Identify recurring failures:
- **"Update Fatigue"**: Rituals used only for status sharing (replace with async).
- **"Strategic Drift"**: Tacticals that ignore strategic OKRs.
- **"DRI Overload"**: One individual owning too many rituals.

## Recommendations
- **Directional Fixing**: Reassigning DRIs or converting to async status updates.
- **Strategic Alignment**: Hard-linking agendas to Profit.co milestones.
- **Automation Deployment**: Scaling the AI Capture/Triage loop.

## Coverage Map
- **Deeply Analyzed**: Core execution rituals (Daily/Weekly).
- **Partially Analyzed**: Ad-hoc problem-solving sessions.
- **Not Analyzed**: 1:1 sessions and confidential HR reviews.

## Limits and Unknowns
- Cannot validate the "psychological safety" without sentiment analysis tools.
- Informal communication (Slack threads) may exist outside the documented cadence.

## Workflow Rules
- **No Agenda, No Meeting**: Enforce via Fellow.app integration.
- **AI-First Documentation**: Every decision must be captured by Fireflies.ai.
- **Strategy Anchor**: Monthly reviews MUST start with a Profit.co walkthrough.

## Output Contract
- **Target**: `logs/active/<project-slug>/deliverables/business-ops-operating-rhythm.md`.
- **Merge Rules**: Standalone deliverable.
- **Artifacts**: Current vs Proposed Cadence table; Automation flow diagram.
