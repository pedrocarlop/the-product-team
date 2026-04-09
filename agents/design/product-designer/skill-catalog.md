# Product Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `handoff-spec`

- Description: Produce a delivery-ready handoff by tracing the approved problem frame, flow, structure, states, content, and dependencies into explicit downstream contracts for design, content, and engineering.
- Trigger: When discovery, flow, or prototype work is ready to be handed to downstream UI, content, and engineering roles.
- Primary MCP/tool: notion, figma
- Fallback: paper, reference/verify
- Best guess: A handoff spec linking flow, structure, behavior, open questions, and downstream ownership with clearly labeled evidence limits.
- Output: knowledge/product-designer-handoff-spec.md, knowledge/assets/ (for visual artifacts)
- Done when: A downstream role can continue without reopening the design problem, behavior rules, or missing-state questions.

## `interaction-spec`

- Description: Specify interaction behavior by modeling triggers, states, rules, feedback, and exceptional conditions so implementation can reproduce the intended behavior without guessing.
- Trigger: When implementation needs behavior-level clarity across user actions, system responses, states, and recovery paths.
- Primary MCP/tool: figma, repository
- Fallback: paper, reference/trace
- Best guess: An interaction spec tied to triggers, state transitions, rules, and clearly labeled ambiguities.
- Output: knowledge/product-designer-interaction-spec.md, knowledge/assets/ (for visual artifacts)
- Done when: An engineer can implement the interaction without guessing behaviors, hidden state rules, or recovery logic.

## `journey-and-flow-design`

- Description: Missing description.
- Trigger: Missing trigger.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: Missing best_guess_output.
- Output: Missing output_artifacts.
- Done when: Missing done_when.

## `problem-framing`

- Description: Translate product goals, evidence, user context, and delivery constraints into a design-ready frame by building an actor-job-constraint-success model before exploring solutions.
- Trigger: When design work needs a stable problem definition, bounded scope, and evidence-backed success criteria before flows or screens are produced.
- Primary MCP/tool: notion, repository
- Fallback: reference/ground, search_query
- Best guess: A design framing artifact with explicit users, jobs, constraints, risks, success criteria, and decision-driving unknowns.
- Output: knowledge/product-designer-problem-framing.md, knowledge/assets/ (for visual artifacts)
- Done when: The design problem is bounded, evidence-tagged, and stable enough that downstream flow and wireframe work can proceed without rediscovering the brief.

## `prototype-and-usability-validation`

- Description: Build or evaluate the smallest prototype that can answer a design decision, then validate it through task-based walkthroughs or research sessions grounded in ISO 9241-11 usability dimensions.
- Trigger: When a flow or concept should be tested before full build or when a proposed interaction needs confidence beyond static review.
- Primary MCP/tool: paper
- Fallback: figma, chrome_devtools
- Best guess: A prototype summary with validation findings, decision guidance, and clearly labeled evidence limits.
- Output: knowledge/product-designer-prototype-and-usability-validation.md, knowledge/assets/ (for visual artifacts)
- Done when: The prototype answers a real decision, the strongest usability risks are explicit, and any unresolved risk is clearly labeled.

## `wireframe-structure`

- Description: Missing description.
- Trigger: Missing trigger.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: Missing best_guess_output.
- Output: Missing output_artifacts.
- Done when: Missing done_when.
