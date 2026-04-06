---
name: prototype-and-usability-validation
description: Build or evaluate the smallest prototype that can answer a design decision, then validate it through task-based walkthroughs or research sessions grounded in ISO 9241-11 usability dimensions.
trigger: When a flow or concept should be tested before full build or when a proposed interaction needs confidence beyond static review.
analysis_framework: task-based prototype validation using ISO 9241-11 usability dimensions of effectiveness, efficiency, and satisfaction
primary_mcp: paper
fallback_tools:
  - figma
  - chrome_devtools
required_inputs:
  - target decision or hypothesis
  - prototype scope or concept in scope
  - target participants or proxy user type
  - task scenarios to test
  - platform or device assumptions
recommended_passes:
  - prototype scope definition
  - task and success metric setup
  - session or walkthrough execution
  - usability signal synthesis
  - decision and residual risk shaping
tool_stack:
  prototype_build:
    primary: [paper, figma]
    secondary: [protopie, axure, uxpin]
  validation:
    primary: [maze, lyssna, usertesting]
    secondary: [lookback, optimal_workshop, chrome_devtools]
  fallback:
    primary: [figma, chrome_devtools]
tool_routing:
  - if: quick concept proofing or low-fidelity prototype creation is required
    use: [paper, figma]
  - if: realistic interactions, variables, or device behaviors materially affect the decision
    use: [protopie, axure, uxpin]
  - if: unmoderated task metrics or scalable participant feedback are required
    use: [maze, lyssna, usertesting]
  - if: moderated sessions or contextual probing matter most
    use: [lookback, usertesting]
  - if: first-click, navigation, or information-architecture validation matters more than motion fidelity
    use: [optimal_workshop]
  - if: a live coded prototype or behavior needs runtime spot-checking
    use: [chrome_devtools]
  - if: primary tools are unavailable
    use: [figma, chrome_devtools]
best_guess_output: A prototype summary with validation findings, decision guidance, and clearly labeled evidence limits.
output_artifacts:
  - knowledge/runs/<run-id>/product-designer-prototype-and-usability-validation.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: The prototype answers a real decision, the strongest usability risks are explicit, and any unresolved risk is clearly labeled.
mesh:
  inputs:
    - product-designer:wireframe-structure
    - ui-designer:screen-production-design
  next:
    - ux-researcher:foundational-research
    - product-designer:problem-framing
  context: "Validation tests the current design against user needs, identifying gaps that may require re-framing or foundational research."
---

# Prototype And Usability Validation

## Purpose

Use the smallest useful prototype and the strongest available validation path to answer a real design decision.

This skill applies task-based prototype testing and ISO 9241-11 usability dimensions to judge whether the proposed interaction is effective, efficient, and likely understandable enough to move forward.

This skill does not treat a prototype as proof of production readiness or replace full research, analytics, or accessibility validation.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/product-designer-prototype-and-usability-validation.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/runs/<run-id>/assets/`. 
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/runs/<run-id>/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths.
  - For `take_screenshot`, you MUST supply the `filePath` parameter pointing directly to the destination in the project workspace.
  - For `generate_image`, or tools that save to your `.gemini`/`.antigravity` brain directory or `/tmp`, you MUST use bash to manually move the image file into the project directory.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths or paths outside the workspace.

## Required Deliverable Sections

Within `## Skill: prototype-and-usability-validation`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Validation framing`: Define the decision, hypothesis, and why prototyping is the right validation method for this question.
- `### Required inputs and assumptions`: State the known prototype scope, participant type, tasks, and inferred assumptions required to proceed.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live interaction, structured system access, design or documentation artifacts, screenshots or static input, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record device, browser, prototype build or file version, auth state, data setup, and session conditions when known.
- `### Prototype model`: Build the model first by defining the screens, states, interactions, and intentionally omitted elements before testing.
- `### Validation plan`: State the tasks, scenarios, success signals, and the difference between moderated research, unmoderated testing, walkthroughs, or expert simulation.
- `### Tasks, success criteria, and failure signals`: Define what participants or the evaluator were asked to do and what counted as success or hesitation.
- `### Participant or walkthrough setup`: Describe participant profile, sample size, facilitation mode, or walkthrough assumptions.
- `### Session findings`: Record the highest-signal validation findings using the required finding schema below.
- `### Prioritized decision blockers`: Include all decision-changing usability problems as standalone findings, group lower-impact observations into patterns, and prefer no more than 10 standalone findings by default unless more are materially distinct.
- `### Systemic usability patterns`: Group recurring issues such as weak affordance, poor feedback, hidden requirements, or broken mental models.
- `### Coverage map`: State what tasks, screens, and conditions were deeply validated, lightly validated, or not validated.
- `### Decision, confidence, and next test`: State what the team can now decide, how strong the evidence is, and what next validation step would reduce the biggest remaining risk.
- `### Limits and unknowns`: Explain what the prototype could not realistically validate and what still requires production or real-user evidence.

For each finding inside `### Session findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Task or scenario:
- Usability signal:
- Likely cause:
- Impact on decision:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest evidence path available: live interaction -> structured systems -> design or documentation artifacts -> screenshots or static inputs -> inference.
- Start with `paper` when the fastest route to answering the decision is a lightweight prototype or concept artifact.
- Use `figma` when the prototype needs to stay close to design source files, linked flows, or shared review artifacts.
- Use `protopie`, `axure`, or `uxpin` when realistic conditions, variables, or richer interactions materially affect the question being tested.
- Use `maze`, `lyssna`, or `usertesting` when unmoderated task metrics or scalable participant feedback are required.
- Use `lookback` or `usertesting` when moderated sessions, contextual probing, or richer participant commentary matter more than raw task metrics.
- Use `optimal_workshop` when first-click behavior, navigation, or structural findability matters more than motion fidelity.
- Use `chrome_devtools` when the strongest available prototype is coded and needs runtime spot-checking.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, chrome_devtools`.
- If both paths fail, produce the best-guess output described as: A prototype summary with validation findings, decision guidance, and clearly labeled evidence limits.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Use named external tools only when they are connected or explicitly available in the environment.

## Workflow Notes

- Prototype only enough to answer the decision. More fidelity is not automatically better.
- Treat `required_inputs` as real prerequisites. If the decision, task scenarios, or participant profile is missing, infer a provisional set, prefix each inferred item with `Assumed validation input:`, and lower confidence for dependent findings.
- Build the prototype model before testing so the team can distinguish omitted scope from actual failure.
- Start with the test question, then define tasks and success signals, then run sessions or walkthroughs, then synthesize patterns and decision impact.
- When no real participants are available, make the evidence downgrade explicit and label the work as expert walkthrough or simulated validation instead of user research.
- Tie findings back to the decision the prototype was meant to answer. Do not confuse general polish comments with decision-relevant evidence.
- Distinguish clearly between observed usability signal, inferred cause, and recommendation direction.
- Group repeated hesitations into patterns instead of listing every instance as a standalone issue.
- Do not claim production confidence, accessibility compliance, or broad market validation from narrow prototype evidence.

