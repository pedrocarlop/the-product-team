---
name: sales-enablement
description: Encodes the method for developing AI-driven sales enablement and training programs, focused on contextual supercoaching, real-time feedback, and behavior-led skill validation for 2026 GTM teams.
trigger: When a GTM leader needs to build or update sales training, coaching, or content enablement systems to improve rep win rates and meeting readiness.
best_guess_output: A comprehensive sales enablement blueprint including a tool stack, coaching methodology, and performance measurement framework.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market-sales-enablement.md
section_anchor: sales-enablement
done_when: The program architecture is defined, tools are routed based on capabilities, and a behavior-led measurement system is in place.
---

# Sales Enablement and Training

## 2. Purpose
This skill defines the process for designing a modern, AI-integrated sales enablement program. It focuses on "Supercoaching" (pre-meeting readiness and real-time guidance) rather than just post-call analysis. It applies behavioral reasoning to shift from tribal wisdom to evidence-backed coaching.

## 3. Required Inputs and Assumptions
- **Required Inputs**: Current GTM strategy, ICP profiles, existing sales content, current win/loss data, target training gaps.
- **Known vs Unknown**: We know the target tools (Highspot, Seismic, Proshort, etc.); we assume the user has access to or is willing to adopt these platforms.
- **Assumptions**: The organization is moving towards a unified GTM stack and values AI-driven automation for rep productivity.

## 4. Input Mode and Evidence Path
1. **Live / Real Interaction**: Observation of sales calls or recorded sessions (Gong/Chorus).
2. **Structured System Access**: Data from CRM (Salesforce) and Enablement platforms (Highspot/Seismic).
3. **Design Artifacts**: Review of existing sales decks, email templates, and playbooks.
4. **Inference**: Extrapolating from industry benchmarks (2026 GTM trends).

## 5. Tool Stack (Capabilities)
- **Runtime**:
    - Primary: Highspot (Content), Proshort (Supercoaching), Lavender (Email AI).
    - Secondary: Allego (Social Learning), Second Nature (AI Roleplay), Gong (Revenue Intelligence).
- **Artifacts**:
    - Primary: Seismic (Enterprise Governance).
- **Fallback**:
    - Primary: Mindtickle (Readiness).

## 6. Tool Routing (Decision System)
- **If**: Need real-time communication coaching for prospecting -> Use: **Lavender**.
- **If**: Need just-in-time meeting preparation for specific personas -> Use: **Proshort**.
- **If**: Need high-fidelity practice with simulated buyers -> Use: **Second Nature**.
- **If**: Need unified enterprise content and analytics -> Use: **Seismic** or **Highspot**.
- **If**: Need post-call reality analysis and pipeline risks -> Use: **Gong**.

## 7. Environment and Reproducibility
- **Platform**: GTM Tech Stack (CRM + Enablement platform).
- **State**: Assume auth is handled via SSO; data is synchronized across the GTM ecosystem.
- **Version**: 2026.1 Build (AI Agent integration).

## 8. Model Building (Before Analysis)
Before designing the program, the agent must map:
- **Rep Persona Model**: Tenure, skill gaps, quota attainment history.
- **Buyer Journey Model**: Key touchpoints where enablement is critical.
- **Tool Dependency Map**: How data flows from Gong to Highspot to Proshort.

## 9. Core Method Execution
1. **Discovery & Audit**: Analyze current CRM data to identify win/loss patterns.
2. **Gap Mapping**: Match identified gaps to behavior-led outcomes.
3. **Content Personalization Engine**: Configure Seismic/Highspot for AI-driven assembly of sales materials.
4. **Supercoaching Workflow**: Implement Proshort for 10-minute "meeting-ready" preps.
5. **Real-time Feedback Loop**: Deploy Lavender for email and Gong for call-based coaching.
6. **Validation**: Use Second Nature for AI roleplays to certify reps before they go live.

## 10. Structured Findings
- **Finding Observation**: Evidence of rep friction in early-stage discovery.
- **Evidence**: Gong transcripts show 40% of calls fail to move to Stage 2.
- **Repro Steps**: Analyze discovery calls using specific "Supercoach" prompts.
- **Cause**: Lack of persona-specific objection handling.
- **Impact**: Reduced pipeline velocity.
- **Confidence**: High (backed by CRM data).

## 11. Prioritization Logic
- **High Impact**: Meeting-ready preparation (Proshort) and real-time email coaching (Lavender).
- **Medium Impact**: Certification and formal readiness (Mindtickle).
- **Low Impact**: General tribal knowledge sharing (Social learning).

## 12. Pattern Detection
- Identify if the sales cycle is elongating due to "Content Silos" (reps unable to find relevant materials).
- Detect if "Tribal Wisdom" (anecdotal success) is overriding data-driven sales methods.

## 13. Recommendations
- Transition from weekly manual coaching to "Just-in-Time" AI coaching.
- Deploy AI agents to automate the assembly of "Digital Sales Rooms" in Highspot based on buyer signals.

## 14. Coverage Map
- **Deeply Analyzed**: AI Coaching (Proshort/Allego), Email AI (Lavender), Content Enablement (Highspot/Seismic).
- **Partially Analyzed**: CRM integration, formal certification.
- **Not Analyzed**: Incentive compensation models, sales hiring processes.

## 15. Limits and Unknowns
- Real-world rep adoption rates cannot be fully predicted without pilot testing.
- The efficacy of AI roleplay depends on the quality of training data for the simulated personas.

## 16. Workflow Rules
- Build the Rep Persona Model before recommending specific coaching tools.
- Distinguish between "Activity metrics" (volume) and "Outcome metrics" (win rate).
- Avoid prescribing a "one-size-fits-all" training program; personalize by rep tenure.

## 17. Output Contract
- **Target File**: `logs/active/<project-slug>/deliverables/go-to-market-sales-enablement.md`.
- **Constraint**: All recommendations must align with the 2026 "Supercoaching" methodology.
