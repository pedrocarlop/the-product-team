---
name: chrome-list-network-requests
tool: mcp__chrome_devtools__list_network_requests
description: Inspect network traffic to verify that API calls, data loading, and error handling match the approved technical plan.
---

# Chrome: List Network Requests

Use this skill to observe the network requests made by the implemented feature and verify that API calls align with the approved `tech-plan.md` and the functional requirements in the PRD.

## When to Use

- When reviewing whether the implementation calls the correct endpoints with the correct payloads
- When verifying that error states are triggered by real API failures, not just simulated conditions
- When checking that loading states appear in response to actual async operations
- When the PRD includes specific data-fetching or API integration requirements

## How to Use

Call `mcp__chrome_devtools__list_network_requests` after navigating to and interacting with the implemented feature. Review the captured requests for:
- Endpoint URLs — do they match what `tech-plan.md` specifies?
- Request payloads — are the correct parameters sent?
- Response codes — are error states triggered appropriately by 4xx and 5xx responses?
- Request timing — are there redundant or unnecessary calls that indicate implementation issues?

## What to Extract

- Any API call that deviates from the approved spec (wrong endpoint, wrong method, unexpected payload)
- Missing API calls — states that should be server-driven but appear to be hardcoded
- Error response handling — verify 4xx/5xx responses trigger the error states designed in `task-flows.md`
- Redundant calls that suggest a caching, memoization, or state management issue

## Notes for Engineering Reviewer

Network request inspection is particularly important for validating loading, error, and empty states. If the implementation shows correct states but triggers them with hardcoded conditions instead of real API responses, flag it as a risk — the behavior will break in production.
