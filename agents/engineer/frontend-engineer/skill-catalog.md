# Frontend Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `browser-debug`

- Description: Reproduce and isolate a frontend issue using browser evidence.
- Trigger: When UI behavior is wrong and browser evidence is required.
- Primary MCP/tool: chrome_devtools
- Fallback: repository, reference/trace
- Best guess: A debugging summary with cause and fix direction.
- Output: logs/active/<project-slug>/deliverables/frontend-engineer.md
- Done when: The issue is localized to a concrete source of truth.

## `component-implementation`

- Description: Build or extend reusable frontend components that align with the design system.
- Trigger: When implementation needs a reusable component, not just a one-off screen.
- Primary MCP/tool: repository, figma
- Fallback: reference/reuse, chrome_devtools
- Best guess: A reusable component implementation with intended states and props.
- Output: logs/active/<project-slug>/deliverables/frontend-engineer.md
- Done when: The component is reusable and aligned to system expectations.

## `frontend-verify`

- Description: Verify the implemented UI against behavior, layout, and basic quality expectations.
- Trigger: When frontend work is ready for validation before handoff.
- Primary MCP/tool: repository, chrome_devtools
- Fallback: reference/verify, figma
- Best guess: A frontend verification result with any remaining risks.
- Output: logs/active/<project-slug>/deliverables/frontend-engineer.md
- Done when: The UI is verified or residual issues are explicit.

## `implement-from-design`

- Description: Implement a design faithfully in production code with the required states and interactions.
- Trigger: When approved design work is ready for implementation.
- Primary MCP/tool: repository, figma
- Fallback: chrome_devtools, reference/trace
- Best guess: Working UI implementation aligned to the design spec.
- Output: logs/active/<project-slug>/deliverables/frontend-engineer.md
- Done when: The implemented surface matches the intended structure and behavior.

## `responsive-refinement`

- Description: Adapt or improve the surface so it works cleanly across breakpoints and devices.
- Trigger: When responsive behavior is missing or under-specified.
- Primary MCP/tool: repository, chrome_devtools
- Fallback: figma, reference/verify
- Best guess: A responsive implementation or refinement pass.
- Output: logs/active/<project-slug>/deliverables/frontend-engineer.md
- Done when: Desktop and mobile behavior are both acceptable and intentional.

## `stateful-ui-build`

- Description: Implement the async, error, empty, and interactive state model for a surface.
- Trigger: When a frontend feature depends on robust state behavior.
- Primary MCP/tool: repository
- Fallback: chrome_devtools, reference/trace
- Best guess: A stateful UI implementation with clear behavior across critical states.
- Output: logs/active/<project-slug>/deliverables/frontend-engineer.md
- Done when: Key states are implemented and verifiable in code.
