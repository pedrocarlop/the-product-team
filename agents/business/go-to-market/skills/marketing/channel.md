---
name: channel
description: Choose, shape, and improve marketing channels so each one has a clear role in demand generation and a realistic operating model.
---

# Channel

## Purpose

Use this skill to decide where marketing should show up, what each channel is for, and how the channel fits the audience, offer, and budget.

## When to Use

- When selecting between paid, owned, earned, or partner channels
- When a channel underperforms and needs a sharper strategy
- When an existing channel mix is too broad or unfocused
- When channel assumptions need to be tested before scaling spend

## When Not to Use

- When the main question is who to target or what to say
- When the task is campaign logistics or asset planning
- When the work is mainly attribution, reporting, or dashboarding

## Required Inputs

- The target audience and buying context
- The campaign objective or growth goal
- Available budget, team capacity, and time horizon
- Existing channel performance data or historical learnings
- Constraints on brand, compliance, or content production

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

1. Map the channel to the audience behavior and the stage of the buyer journey.
2. Decide whether the channel is for awareness, consideration, conversion, or retention.
3. Identify the minimum viable channel plan and what makes it worth testing.
4. Define the channel-specific message, format, cadence, and operating rhythm.
5. Check whether the channel has the audience scale and economics to support the goal.
6. Document what would cause the channel to be paused, refined, or expanded.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Channel choice should follow audience behavior, not habit
- Each channel needs a clear role in the funnel
- Economics must make sense before scale
- The channel plan should be focused enough to learn from
- Winning channels are usually the ones that match the audience's natural context

## Output Contract

- Channel recommendation with the reason it fits the goal
- Role of each channel in the funnel
- Channel-specific content or format requirements
- A short test, scale, or stop recommendation

## Examples

### Example 1

Input:
- Audience: Mid-market buyers researching alternatives
- Goal: Generate qualified demand for a new category page

Expected output:
- Channel plan that prioritizes search, retargeting, and sales-assisted distribution
- Clear channel role for each stage of the journey
- Recommendation to avoid channels that create reach without purchase intent

## Guardrails

- Do not choose channels by preference alone
- Do not scale a channel without a plausible audience and economics story
- Do not treat every channel as equally important
- Do not optimize a channel before its role is clear

## Optional Tools / Resources

- Channel performance dashboards
- Audience research and keyword data
- Budget trackers and historical spend records
- Content calendars or creative libraries

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Marketing Blog (hubspot.com)](https://blog.hubspot.com/marketing), [Ahrefs Blog (ahrefs.com)](https://ahrefs.com/blog/), [Google Ads Help (support.google.com)](https://support.google.com/google-ads/), [Think with Google (thinkwithgoogle.com)](https://www.thinkwithgoogle.com/), [Content Marketing Institute (contentmarketinginstitute.com)](https://contentmarketinginstitute.com/articles/)
