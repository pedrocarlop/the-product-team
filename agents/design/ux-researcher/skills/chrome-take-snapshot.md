---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture DOM snapshots as durable research evidence — documenting current product states, competitor patterns, and observed friction points.
---

# Chrome: Take Snapshot

Use this skill to capture the DOM of specific product states as durable evidence for the research synthesis. Snapshots create a reproducible record of observed product behavior that can be cited in research artifacts and handed to the design role as concrete evidence.

## When to Use

- When capturing the current state of a product feature that the new design will replace or modify
- When documenting a specific friction point or missing affordance as observable evidence
- When recording a competitive product's approach to a specific design challenge for analysis
- When capturing evidence of a pattern that is cited in the research synthesis

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the relevant page and state. Parse the returned DOM for:
- Visible content that reveals what information the product surfaces to users
- Structural patterns that indicate how the product organizes the user's task
- State indicators — loading, error, empty — that reveal how the product handles uncertainty
- Interactive element labels that reveal the product's conceptual model

## What to Extract

- Specific DOM evidence to cite in `research-and-rationale.md`
- Content patterns that reveal the product's information hierarchy and conceptual model
- State handling approaches — what the product does when data is missing, loading, or failed
- Labels and terminology that reveal the product's mental model (compare to user's actual mental model)

## Notes for UX Researcher

Snapshots are evidence, not findings. Translate each captured pattern into a specific research insight before including it in the synthesis. "The product shows [X DOM pattern] at step Y, which creates friction because users expect Z based on [research finding]" is an insight. A DOM dump is not.
