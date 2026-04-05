---
name: write-prd
description: Write a delivery-grade PRD that encodes logic, design-awareness, and technical feasibility for AI-first product development.
trigger: When engineering or design need a precise, lossless product specification for execution.
best_guess_output: A PRD or equivalent product specification.
output_artifacts: knowledge/product-lead-write-prd.md
done_when: Executors can build without product ambiguity, and logic/design edge cases are resolved.
---

## 1. Purpose
Write a delivery-grade PRD with scope, scenarios, decisions, and acceptance criteria. This skill applies behavioral reasoning and logic checking to ensure requirements are testable and implementation-ready. It does NOT perform code implementation.

## 2. Required Inputs and Assumptions
Define:
- **Required Inputs**: Problem statement, initial scope, user personas, technical constraints.
- **Assumptions**: If design mocks are missing, infer UI patterns using design-aware tools. If technical limits are unknown, label requirements as "Implementation-Dependent".

## 3. Input Mode and Evidence Path
Hierarchy:
1. **Live Interaction**: Direct access to project repository or Notion spec.
2. **Design Artifacts**: Figr/Figma screenshots or prototypes.
3. **Logic Inference**: AI-assisted logic checking (ChatPRD).
Rule: Declare which path is used and note any limitations.

## 4. Tool Stack (Capabilities)
- **Runtime**:
  - Primary: `chat_prd` (logic validation), `figr` (design-aware requirements), `vercel_v0` (prototyping).
  - Secondary: `notion`, `repository`.
- **Fallbacks**: `google_search` (competitive benchmarking).

## 5. Tool Routing (Decision System)
- `if: logic complexity is high` use `chat_prd` to stress-test requirements.
- `if: UI-heavy feature` use `figr` to ensure design-requirement alignment.
- `if: rapid mockup validation needed` use `vercel_v0` to build visual proof-of-concept.

## 6. Environment and Reproducibility
Capture:
- Project context / state.
- Tool versions and specific state (auth, data).

## 7. Model Building (Before Analysis)
The agent must construct a model before evaluation:
- **Component-State Model**: Map features to components and their states (Idle, Active, Loading, Error, Success).
- **Service Blueprint**: Map the user journey across system touchpoints (UI, API, Data).

## 8. Core Method Execution
Follow "The 3 Pillars of PRDs":
1. **Contextual Foundation (Why)**: Outcomes and goals via JTBD.
2. **Functional Architecture (How)**: Requirement Decomposition into Gherkin-style scenarios (Given-When-Then).
3. **Data Schema & System Integration (What)**: Define JSON schemas and dependencies.

Execution Loops:
- **Decomposition**: Break high-level goals into atomic units.
- **Stress-Testing**: Actively simulate state failures (offline, rate-limited).

## 9. Structured Findings
- **Finding Observation**: Precise gap or conflict.
- **Evidence**: Grounding source or tool output.
- **Cause/Impact**: Why it matters (Blocker vs. Polish).
- **Confidence**: Strength of the finding.

## 10. Prioritization Logic
- **P0 (Critical)**: Functional core and safety.
- **P1 (Standard)**: Edge cases and robustness.
- **P2 (UX)**: Performance and micro-interactions.

## 11. Pattern Detection
Identify:
- Recurring logic gaps.
- System-level architectural contradictions.

## 12. Recommendations
Must link to findings; directional and evidence-based.

## 13. Coverage Map
- Deeply specified areas.
- Placeholders/Discovery needed areas.

## 14. Limits and Unknowns
Mandatory. State unvalidated assumptions and technical black boxes.

## 15. Workflow Rules
- Build model before analysis.
- Distinguish fact vs inference.
- Avoid hallucinated data.

## 16. Output Contract
- **Path**: `knowledge/product-lead-write-prd.md`.
- **Lossless Deliverable Rules**:
  - Standalone file in specified path.
  - Do not overwrite role-level docs.
  - Preserve all nuance and rationale.
  - Link in `orchestrator.md`.

## 17. Required Deliverable Format
Within the output file, include:
- `### Objective`: User/business outcome.
- `### Scope`: Delivery slice definition.
- `### Non-goals`: Explicit exclusions.
- `### Key Scenarios (Gherkin)`: Scenarios in Given-When-Then.
- `### Requirements and Decisions`: Fixed product decisions.
- `### Acceptance Criteria`: Testable units.
- `## Reflection`: What worked/didn't, next steps.
