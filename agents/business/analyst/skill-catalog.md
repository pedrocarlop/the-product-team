# Analyst Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `dashboard-story`

- Description: Turn operational or product metrics into a narrative summary for the team.
- Trigger: When raw metrics exist but the decision story is missing.
- Primary MCP/tool: notion
- Fallback: analyst/funnel-analysis, search_query
- Best guess: A narrative metrics readout with key insights and actions.
- Output: logs/active/<project-slug>/deliverables/analyst.md
- Done when: The audience understands the story behind the numbers.

## `experiment-readout`

- Description: Interpret an experiment and translate the result into a decision.
- Trigger: When a test or rollout needs analysis and recommendation.
- Primary MCP/tool: notion, repository
- Fallback: analyst/metric-definition, search_query
- Best guess: An experiment readout with result, confidence, and next step.
- Output: logs/active/<project-slug>/deliverables/analyst.md
- Done when: A decision-maker can accept, reject, or iterate the experiment.

## `forecast-model`

- Description: Create a forecast with assumptions, ranges, and sensitivity analysis.
- Trigger: When planning depends on future volume, revenue, or adoption.
- Primary MCP/tool: notion
- Fallback: search_query, analyst/metric-definition
- Best guess: A forecast model summary with assumptions and scenarios.
- Output: logs/active/<project-slug>/deliverables/analyst.md
- Done when: The forecast is decision-usable and assumption-driven.

## `funnel-analysis`

- Description: Analyze a funnel to locate the main drop-offs, likely causes, and next actions.
- Trigger: When conversion or progression performance is under question.
- Primary MCP/tool: repository, notion
- Fallback: search_query, reference/trace
- Best guess: A funnel analysis with major drop-offs and hypotheses.
- Output: logs/active/<project-slug>/deliverables/analyst.md
- Done when: The team knows where to focus and why.

## `metric-definition`

- Description: Define the business or product metric model so downstream analysis measures the right thing.
- Trigger: When a team needs crisp metric definitions before analysis or instrumentation.
- Primary MCP/tool: notion, repository
- Fallback: search_query, reference/ground
- Best guess: A metric definition pack with formulas, segments, and caveats.
- Output: logs/active/<project-slug>/deliverables/analyst.md
- Done when: The metric can be implemented or reported consistently.
