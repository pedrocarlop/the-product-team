# Scenario: Design System Audit

## Task
Audit the design system of a mid-size SaaS product that has accumulated inconsistencies over 18 months of rapid feature development. The system has divergent spacing scales, three competing typography ramps, and undocumented color overrides across product areas.

## Requirements
1. **Token Inventory**: Catalog the existing spacing, typography, and color tokens. Identify which tokens are canonical vs. ad-hoc overrides.
2. **Inconsistency Report**: Document specific inconsistencies with severity ratings (critical / major / minor). Include examples of where each inconsistency manifests in the product.
3. **Remediation Priorities**: Rank the inconsistencies by impact and effort. Provide a phased remediation roadmap (quick wins, medium-term, long-term).
4. **Governance Recommendations**: Propose processes to prevent future drift, including contribution guidelines, review workflows, and deprecation policies.

## Output Contract
Produce a `system-audit.md` artifact with ## sections for each requirement above. Include at least one summary table for the token inventory and one for the prioritized issues.
