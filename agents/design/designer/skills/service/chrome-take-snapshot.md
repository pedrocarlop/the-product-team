---
name: chrome-take-snapshot
tool: mcp__chrome_devtools__take_snapshot
description: Capture live product touchpoints to document the current-state digital experience within the broader service context.
---

# Chrome: Take Snapshot

Use this skill to capture specific digital touchpoints in the live product — status pages, confirmation flows, notification surfaces, and handoff screens — to document the current-state experience and ground the service blueprint in reality.

## When to Use

- When mapping the current-state digital journey to identify gaps, friction, or broken handoffs
- When capturing evidence of a specific touchpoint that the service blueprint proposes to change or replace
- When verifying that a digital touchpoint triggers the correct backstage processes (by observing what the page shows after a user action)
- When documenting the current notification, confirmation, or status communication that the service relies on

## How to Use

Call `mcp__chrome_devtools__take_snapshot` on the specific touchpoint page. Inspect the DOM for:
- Status messages and confirmation copy that reveal what the system tells the user about the service state
- Loading or processing states that indicate a backstage process is in progress
- Error states that reveal where the current service breaks down
- Handoff indicators — "You will receive an email / call / notification" messages that trigger the next channel

## What to Extract

- Current digital touchpoint content to document in the current-state blueprint
- Evidence of existing handoff triggers (email, SMS, human callback initiation)
- Failure state copy that reveals where the current service fails users
- Waiting states that indicate latency in backstage processes

## Notes for Service Designer

Digital touchpoints are only one layer of the service. Use the snapshot to document what the customer sees at each touchpoint, then map what must be true in the backstage for that experience to be delivered correctly. A confirmation screen that says "Your order is being processed" implies a backstage process — document it.
