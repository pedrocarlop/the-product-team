---
name: position
description: Define ICP, category positioning, and channel-ready messaging so marketing campaigns target the right buyers with a sharp, consistent reason to engage.
---

# Position

## Purpose

Use this skill to turn a broad market opportunity into a campaign-ready position: who we target, what problem we lead with, why we are different, and how the message should flex across marketing channels.

## When to Use

- When the ICP needs to be narrowed or clarified before campaign planning begins
- When category positioning or homepage messaging is inconsistent across channels
- When a new offer, feature launch, or market shift requires a refreshed narrative
- When marketing needs a sharper lead message before producing content, ads, or landing pages

## When Not to Use

- When the audience and promise are already clear and the work is campaign execution
- When the task is building channel plans, attribution models, or measurement frameworks
- When the issue is solely visual design, copy polish, or launch logistics

## Required Inputs

- The product or offer being positioned
- The target market, buyer persona, and the trigger event or pain point that makes the message timely
- Known alternatives, competitors, and status quo substitutes the buyer considers
- Supporting proof points, differentiators, and customer evidence
- Brand voice, terminology constraints, and any legal or compliance requirements
- The channels the positioning must work across: website, paid ads, email, sales enablement

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: go-to-market
project: <slug>
deliverable: go-to-market.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Identify the most specific buyer and the trigger event that makes the product relevant now.
2. Separate the primary audience from adjacent audiences that should not dilute the lead message.
3. Name the problem in the buyer's language, not internal product vocabulary.
4. Write the positioning statement and supporting message pillars.
5. Stress-test the message against the top 2-3 alternatives to ensure the distinction is real.
6. Adapt the positioning into channel-appropriate formats: headline for ads, value prop for landing pages, one-liner for email subject lines.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Specificity beats broad appeal; a message for everyone persuades no one
- Buyer vocabulary beats internal jargon in every channel
- Differentiation must be believable and provable, not generic
- Positioning should be stable enough to work across web, paid, email, and sales without contradicting itself
- The message should be simple enough that a non-marketer can repeat it accurately

## Output Contract

- ICP definition with fit criteria, trigger events, and primary pain points
- Positioning statement and 2-4 supporting message pillars
- Channel-adapted message variants: headline, value prop, email one-liner, ad copy direction
- Short list of approved claims, proof points, and phrases
- Notes on exclusions, messaging risks, and terms to avoid

## Examples

### Example 1

Input:
- Product: Workflow platform for customer success teams
- Problem: Sales and CS are both being targeted with the same homepage message

Expected output:
- ICP: "Customer success leaders at B2B SaaS companies with churn pressure and manual renewal workflows"
- Positioning statement: "For CS teams that need to protect recurring revenue, the product is the customer success workflow platform that surfaces risk and automates renewal playbooks."
- Channel variants: Homepage headline focuses on renewal automation; ad copy leads with churn reduction; email subject line uses "stop manual renewals"
- Messaging note: Do not lead with generic collaboration language

## Guardrails

- Do not widen the ICP to make the addressable market look larger
- Do not claim differentiation the product cannot demonstrate with evidence
- Do not turn positioning work into a feature list or product spec
- Do not skip channel adaptation; positioning that only works on a strategy slide is not useful
- Do not position without explicit exclusions when a sharper message is needed

## Optional Tools / Resources

- Research notes, win/loss interviews, or customer quotes
- Website copy, pitch decks, or sales enablement material
- Competitive pages, ad copy, and analyst reports
- Brand or terminology guidelines

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Marketing Blog (hubspot.com)](https://blog.hubspot.com/marketing), [Ahrefs Blog (ahrefs.com)](https://ahrefs.com/blog/), [Google Ads Help (support.google.com)](https://support.google.com/google-ads/), [Think with Google (thinkwithgoogle.com)](https://www.thinkwithgoogle.com/), [Content Marketing Institute (contentmarketinginstitute.com)](https://contentmarketinginstitute.com/articles/)
