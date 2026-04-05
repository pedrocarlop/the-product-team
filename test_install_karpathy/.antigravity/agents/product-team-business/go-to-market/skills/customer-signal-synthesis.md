---
name: customer-signal-synthesis
description: Synthesize multi-source buying signals, intent data, and conversation intelligence into actionable GTM priorities.
trigger: When a new campaign is being planned, or when an account list needs prioritization based on live signals.
best_guess_output: A prioritized list of accounts and contacts with specific 'why now' triggers and personalized messaging angles.
output_artifacts: knowledge/go-to-market-customer-signal-synthesis.md
done_when: All available signals from the tool stack have been aggregated, de-duplicated, and mapped to a prioritization matrix.
required_inputs: [Target account list, Ideal Customer Profile (ICP) definition, Product value propositions]
tool_stack:
  runtime:
    primary: [Clay, 6sense, Gong, Apollo]
    secondary: [Salesmotion, ZoomInfo]
  artifacts:
    primary: [CRM data, Meeting transcripts]
tool_routing:
  - if: "Deep enrichment and automation are needed"
    use: [Clay]
  - if: "High-intent account identification is required"
    use: [6sense]
  - if: "Post-call sentiment and direct customer voice are needed"
    use: [Gong]
---

# Customer Signal Synthesis

## 2. Purpose
The `customer-signal-synthesis` skill applies intent-based reasoning and multi-agent orchestration to transform raw digital noise into high-fidelity buying signals. It bridges marketing intent (6sense), sales research (Clay/Apollo), and direct customer conversations (Gong) to define GTM priorities.

## 3. Required Inputs and Assumptions
- **Required Inputs**: Account domains, ICP criteria, product value propositions, and access to signal tools.
- **Assumptions**: If intent data is missing for a specific account, the skill assumes a "neutral" intent score unless recent news signals (via Claygent) suggest otherwise.

## 4. Input Mode and Evidence Path
1. **Live System Access**: API-level integration with 6sense (intent) and Gong (conversations).
2. **Structured Enrichment**: Clay waterfall enrichment for contact and company data.
3. **Design Artifacts**: CRM exports or CSV account lists.
4. **Inference**: Using LLM analysis of news and job postings to infer strategic priorities when direct data is sparse.

## 5. Tool Stack (Capabilities)
- **Data Orchestration**: Clay (Waterfall enrichment, Claygent AI research).
- **Intent Intelligence**: 6sense (Predictive modeling, account intent stages).
- **Conversation Intelligence**: Gong (Sentiment analysis, keyword tracking).
- **Sales Intelligence**: Apollo (Contact database, engagement sequencing).

## 6. Tool Routing (Decision System)
- **6sense**: Use first to identify high-intent accounts (Top 10% filter).
- **Clay**: Use for deep research on high-intent accounts to find "why now" triggers.
- **Gong**: Use to pull specific objections or pain points from recent calls with similar personas.
- **Apollo**: Use to find specific contacts and initiate engagement sequences.

## 7. Environment and Reproducibility
- **Platform**: GTM Intelligence Stack (2026 Edition).
- **State**: Requires authenticated access to the primary tool stack.
- **Reproducibility**: Analysis can be re-run on a 7-day cycle to capture dynamic signal growth or decay.

## 8. Model Building (Before Analysis)
Construct a **Signal-Account Graph**:
- **Nodes**: Accounts, Contacts, Signals (Intent Surges, News Triggers, Call Sentiment).
- **Edges**: Relationships (e.g., "Contact X mentioned Pain Point Y in Gong call").
- **Schema**: Map 6sense intent stages to Clay-enriched pain points for each account.

## 9. Core Method Execution
1. **Ingest & Filter**: Load target accounts and filter by ICP fit and 6sense intent stage (e.g., 'Consideration' or 'Purchase').
2. **Waterfall Enrichment**: Execute Clay workflows to verify emails, LinkedIn profiles, and recent company news.
3. **Contextual Analysis**: Use Claygent to visit prospect websites and extract "strategic anchors" (e.g., specific mentions of AI initiatives or digital transformation).
4. **Sentiment Mapping**: Query Gong for recurring objection trends or feature requests in the target segment.
5. **Score Synthesis**: Combine Intent Score (6sense), Signal Freshness (Clay), and Sentiment Match (Gong) into a **Priority Score**.

## 10. Structured Findings
For each priority account:
- **Account**: [Domain]
- **Primary Signal**: [Evidence Path, e.g., 6sense Intent Surge on 2026-04-01]
- **Trigger**: [Extract from Claygent, e.g., New CEO appointment or Product Launch]
- **Messaging Angle**: [Personalized hook based on Gong call trends]
- **Confidence**: [High/Medium/Low based on data freshness]

## 11. Prioritization Logic
- **P0 (Action Now)**: 6sense 'Purchase' stage + Fresh Clay news (<48h) + Direct Gong pain point match.
- **P1 (Strategic Nurture)**: 6sense 'Consideration' stage + Strategic anchor match via Claygent.
- **P2 (Watchlist)**: ICP match + 6sense 'Awareness' stage + Recent job changes.

## 12. Pattern Detection
- **Systemic Shifts**: Identify if a specific competitor is losing ground based on Gong transcripts.
- **Vertical Surges**: Detect if a specific sub-industry is showing unified intent patterns (e.g., FinTech surging on 'Compliance' signal).

## 13. Recommendations
- **Sales Action**: Immediate outreach for P0 accounts with drafted "why now" hooks.
- **Marketing Action**: Target P1 accounts with intent-specific ad creative.
- **Product Signal**: Log recurring feature requests from Gong into specific product roadmap candidate bets.

## 14. Coverage Map
- **Deeply Analyzed**: Top 50 accounts by intent stage.
- **Partially Analyzed**: Remainder of ICP list (Contact enrichment only).
- **Not Analyzed**: Out-of-ICP accounts.

## 15. Limits and Unknowns
- **Data Freshness**: Apollo/ZoomInfo data may have a 5-10% bounce rate.
- **Intimacy Gap**: Automated synthesis cannot replace the nuance of a 1:1 discovery call.
- **Attribution**: 6sense "Dark Funnel" data is predictive and may occasionally produce false positives.

## 16. Workflow Rules
- Always build the Signal-Account Graph before making prioritization calls.
- Require at least TWO distinct signal sources before labeling an account as P0.
- Fallback to Apollo/ZoomInfo immediately if Clay enrichment fails.
- Never use hallucinated contact data; if a contact is not found, label clearly as "To Be Discovered".

## 17. Output Contract
- **File**: `knowledge/go-to-market-customer-signal-synthesis.md`
- **Constraint**: Do not modify existing core agent role documents.
- **Linkage**: Must be linked in the Execution Manifest (`orchestrator.md`).
