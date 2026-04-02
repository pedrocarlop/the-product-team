# Skill Authoring Guide

## Purpose

This guide defines how to create high-quality, production-ready skills.  
It ensures all skills follow a consistent standard: method-driven, evidence-based, structured, and reproducible.

This is not a prompt-writing guide.  
It is a **system design guide for agent capabilities**.

---

## Core Principles

1. **Method over prompt**  
   A skill must encode a real expert workflow, not generic instructions.

2. **Evidence over opinion**  
   Outputs must be grounded in observable input, data, or explicitly stated assumptions.

3. **Structure over prose**  
   Outputs must be structured, scannable, and reusable.

4. **Constraints over freedom**  
   Reduce ambiguity. The skill should guide decisions, not defer them.

5. **Tool-aware, not tool-dependent**  
   Tools support execution but do not define the method.

6. **Reproducibility**  
   Another agent should be able to follow the same process and reach similar conclusions.

---

## Required Skill Structure

Every skill must include the following components.

---

### 1. Frontmatter (Execution Contract)

```yaml
---
name:
description:
trigger:
best_guess_output:
output_artifacts:
section_anchor:
done_when:
---

Optional but recommended:

required_inputs:
recommended_passes:
tool_stack:
tool_routing:

Rules:
	•	description → describe the method, not the task
	•	trigger → when to use the skill
	•	done_when → must be measurable and explicit

⸻

2. Purpose

Explain:
	•	What the skill does
	•	What type of reasoning it applies
	•	What it explicitly does NOT do

Keep it short and operational.

⸻

3. Required Inputs and Assumptions

Define:
	•	Required inputs
	•	Known vs unknown
	•	Assumptions

Rule:
If inputs are missing → infer them and label clearly as assumptions.

⸻

4. Input Mode and Evidence Path

Always define how evidence is gathered.

Use this hierarchy:
	1.	Live / real interaction
	2.	Structured system access (APIs, DB, logs)
	3.	Design artifacts or documentation
	4.	Screenshots / static input
	5.	Inference (last resort)

Rules:
	•	Declare which path is used
	•	Declare limitations of that path

⸻

5. Tool Stack (Capabilities)

Define tools by capability layer:

tool_stack:
  runtime:
    primary: []
    secondary: []
  artifacts:
    primary: []
  fallback:
    primary: []


⸻

6. Tool Routing (Decision System)

Define when to use which tools:

tool_routing:
  - if: real system is accessible
    use: [runtime tools]
  - if: multi-step interaction is required
    use: [automation tools]
  - if: only static inputs exist
    use: [artifact tools]

Rules:
	•	Use conditional logic
	•	Avoid single-tool bias
	•	Prefer combining tools when needed

⸻

7. Environment and Reproducibility

Capture:
	•	Platform / device
	•	State (auth, data, environment)
	•	Version (build, dataset, prototype)

If unknown → explicitly state.

⸻

8. Model Building (Before Analysis)

The agent must construct a model before evaluating.

Examples:
	•	UX → UI model (flows, components, states)
	•	Product → system model (actors, dependencies)
	•	Data → schema / relationships
	•	Code → architecture / modules

Rule:
No conclusions before model construction.

⸻

9. Core Method Execution

Define the step-by-step workflow.

Examples:
	•	Walkthroughs
	•	Analysis loops
	•	Comparisons
	•	Transformations

Rules:
	•	Must follow a clear sequence
	•	Must be grounded in a real method
	•	Avoid generic commentary
	
If the discipline has a recognized external framework (e.g., WCAG, ISO standards, domain-specific guidelines), the skill must explicitly anchor to it and map its method to that framework.

⸻

10. Structured Findings

Define a strict schema.

Finding

Observation:
Evidence:
Repro steps:
Cause:
Impact:
Confidence:

Rules:
	•	No free-form output
	•	Separate observation from interpretation
	•	Every finding must be traceable

⸻

11. Prioritization Logic

Define how outputs are prioritized:
	•	Severity / impact / importance
	•	Group minor issues
	•	Limit standalone findings unless justified

Example rules:
	•	Always include critical issues
	•	Group low-impact issues into patterns

⸻

12. Pattern Detection

The agent must identify:
	•	Recurring issues
	•	System-level problems
	•	Broken mental models

This distinguishes expert output from surface-level output.

⸻

13. Recommendations

Rules:
	•	Must link to findings
	•	Must be directional, not overconfident
	•	Avoid prescribing without evidence

⸻

14. Coverage Map

State:
	•	What was deeply analyzed
	•	What was partially analyzed
	•	What was not analyzed

⸻

15. Limits and Unknowns

Mandatory section.

Include:
	•	What could not be validated
	•	What requires real-world validation
	•	Where confidence is low

⸻

16. Workflow Rules

The agent must:
	•	Build a model before analysis
	•	Distinguish fact vs inference
	•	Merge duplicates
	•	Avoid redundancy
	•	Avoid hallucinated data
	•	Keep reasoning grounded

⸻

17. Output Contract

Define:
	•	Where output is written
	•	What section is updated
	•	What must NOT be modified

⸻

Quality Bar (Non-Negotiable)

A skill is valid only if:
	•	Outputs are reproducible
	•	Findings are evidence-based
	•	Structure is consistent
	•	Method is explicit
	•	Limitations are transparent

⸻

Anti-Patterns to Avoid

Do NOT:
	•	Write vague instructions
	•	Skip model-building
	•	Mix observation with opinion
	•	Over-index on tools
	•	Output unstructured text
	•	Ignore uncertainty

⸻

Skill Creation Workflow

When creating a new skill:
	1.	Identify the underlying method
	2.	Define required inputs
	3.	Define evidence paths
	4.	Define tool stack and routing
	5.	Define model-building step
	6.	Define execution steps
	7.	Define output schema
	8.	Define prioritization logic
	9.	Define coverage and limits
	10.	Define done_when criteria

⸻

Done When

A skill is complete when:
	•	It encodes a real expert workflow
	•	It produces structured outputs
	•	It clearly states evidence and limitations
	•	It is reusable across contexts
	•	It avoids hidden assumptions

⸻

Usage

Use this guide when:
	•	Creating a new skill
	•	Reviewing or refactoring an existing skill
	•	Debugging low-quality agent outputs

All skills in the repository must comply with this guide.

