# Product Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `handoff-spec`

- Description: Prepare the structured design handoff for downstream UI, content, and engineering work.
- Trigger: When discovery and flow work must be handed downstream.
- Primary MCP/tool: notion, figma
- Fallback: paper, reference/verify
- Best guess: A handoff spec linking flow, structure, and open questions.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: A downstream role can continue without reopening the design problem.

## `interaction-spec`

- Description: Specify the important interaction rules, state changes, and transitions.
- Trigger: When implementation needs behavior-level clarity.
- Primary MCP/tool: figma, repository
- Fallback: paper, reference/trace
- Best guess: An interaction spec tied to states and user actions.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: An engineer can implement the interaction without guessing behaviors.

## `journey-and-flow-design`

- Description: Map the end-to-end journey, decisions, states, and edge cases for the experience.
- Trigger: When a feature or service flow needs clear behavioral structure.
- Primary MCP/tool: figma
- Fallback: paper, notion
- Best guess: A journey or flow artifact with key paths and branches.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: The main path and critical alternatives are unambiguous.

## `problem-framing`

- Description: Translate product goals and user context into a design-ready framing.
- Trigger: When design work needs a crisp problem statement and design lens.
- Primary MCP/tool: notion, repository
- Fallback: reference/ground, search_query
- Best guess: A design framing artifact with users, task, constraints, and success criteria.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: Downstream design work has a stable framing.

## `prototype-and-usability-validation`

- Description: Build and validate a prototype to test whether the proposed interaction actually works.
- Trigger: When a flow or concept should be tested before full build.
- Primary MCP/tool: paper
- Fallback: figma, browser inspection
- Best guess: A prototype summary with validation findings.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: The prototype answers a real decision and any unresolved risk is explicit.

## `wireframe-structure`

- Description: Build low-to-mid fidelity structural wireframes that clarify hierarchy and task flow.
- Trigger: When teams need screen structure before visual polish.
- Primary MCP/tool: figma
- Fallback: paper, repository grounding
- Best guess: A wireframe set aligned to the approved flow.
- Output: logs/active/<project-slug>/deliverables/product-designer.md
- Done when: Screen structure is clear enough for review or prototyping.
