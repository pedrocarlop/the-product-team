---
name: search-query
tool: search_query
description: Research service design patterns, cross-channel experience frameworks, and backstage process models before authoring blueprints.
---

# Search Query

Use this skill to research established service design frameworks, cross-channel experience patterns, and industry-specific service blueprinting conventions before committing to a service design approach.

## When to Use

- Before designing a new service blueprint when the domain or channel configuration is unfamiliar
- When researching how comparable services handle handoff moments, escalation, or failure recovery across channels
- When looking for industry-specific requirements (regulatory, compliance, or operational standards) that affect the service design
- When validating that a proposed backstage process structure aligns with established operational patterns

## How to Use

Call `search_query` with targeted queries focused on the service design challenge:
- `"customer onboarding service blueprint financial services"` — not `"onboarding design"`
- `"omnichannel returns process retail service design"` — not `"returns flow"`
- `"human-in-the-loop AI escalation patterns customer support"` — not `"AI support"`

## What to Extract

- Established service blueprinting frameworks relevant to the domain
- Cross-channel handoff patterns that reduce friction at ownership transitions
- Industry operational standards that constrain the backstage process design
- Anti-patterns to avoid — service breakdowns that occur at common handoff points

## Notes for Service Designer

Research service failure modes, not just success paths. The most valuable service design insight is usually found in documented cases of where services break down — at handoff moments, under peak load, and when backstage processes fail to trigger.
