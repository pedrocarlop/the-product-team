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
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: A downstream role can continue without reopening the design problem, behavior rules, or missing-state questions.

## `interaction-spec`

- Description: Specify interaction behavior by modeling triggers, states, rules, feedback, and exceptional conditions so implementation can reproduce the intended behavior without guessing.
- Trigger: When implementation needs behavior-level clarity across user actions, system responses, states, and recovery paths.
- Primary MCP/tool: figma, repository
- Fallback: paper, reference/trace
- Best guess: An interaction spec tied to triggers, state transitions, rules, and clearly labeled ambiguities.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: An engineer can implement the interaction without guessing behaviors, hidden state rules, or recovery logic.

## `journey-and-flow-design`

- Description: Map the end-to-end journey by building an experience model of actors, entry points, states, branches, and operational dependencies before defining screens or polished UI.
- Trigger: When a feature, service, or multi-step task needs clear behavioral structure before wireframes, prototyping, or implementation.
- Primary MCP/tool: figma
- Fallback: paper, notion
- Best guess: A journey map or flow artifact with entry points, primary and alternate paths, decision points, service dependencies, and explicit edge-case coverage.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: The main path, critical branches, decision points, and operational dependencies are explicit enough that downstream structure and interaction work does not have to infer route logic.

## `problem-framing`

- Description: Translate product goals, evidence, user context, and delivery constraints into a design-ready frame by building an actor-job-constraint-success model before exploring solutions.
- Trigger: When design work needs a stable problem definition, bounded scope, and evidence-backed success criteria before flows or screens are produced.
- Primary MCP/tool: notion, repository
- Fallback: reference/ground, search_query
- Best guess: A design framing artifact with explicit users, jobs, constraints, risks, success criteria, and decision-driving unknowns.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: The design problem is bounded, evidence-tagged, and stable enough that downstream flow and wireframe work can proceed without rediscovering the brief.

## `prototype-and-usability-validation`

- Description: Build or evaluate the smallest prototype that can answer a design decision, then validate it through task-based walkthroughs or research sessions grounded in ISO 9241-11 usability dimensions.
- Trigger: When a flow or concept should be tested before full build or when a proposed interaction needs confidence beyond static review.
- Primary MCP/tool: paper
- Fallback: figma, chrome_devtools
- Best guess: A prototype summary with validation findings, decision guidance, and clearly labeled evidence limits.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: The prototype answers a real decision, the strongest usability risks are explicit, and any unresolved risk is clearly labeled.

## `wireframe-structure`

- Description: Build low-to-mid fidelity structural wireframes by converting an approved flow into screen-level hierarchy, navigation, and content scaffolding before visual polish begins.
- Trigger: When teams need screen structure, hierarchy, and task flow clarity before detailed visual design or implementation.
- Primary MCP/tool: figma
- Fallback: paper, reference/ground
- Best guess: A wireframe set aligned to the flow, with explicit hierarchy, navigation logic, and unresolved structural gaps.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: Screen structure is clear enough that reviewers can assess hierarchy and task completion without needing visual polish to infer intent.
