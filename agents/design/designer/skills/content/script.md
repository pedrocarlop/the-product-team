---
name: script
description: Draft and refine conversation scripts, dialogue trees, and turn-by-turn response sequences for AI-powered experiences.
---

# Script

## Purpose

Use this skill to turn conversation requirements into a clear turn-by-turn script that shows how the interaction actually unfolds.

## When to Use

- When designing a new chatbot or assistant flow
- When a flow needs to be expressed as actual dialogue before it is implemented
- When you need to compare alternate branches, entry points, or state transitions

## When Not to Use

- When the main problem is defining what the assistant should or should not handle
- When the task is primarily about recovery from errors or repeated failures
- When the conversation already exists and only tone or wording needs adjustment

## Required Inputs

- The user goal and the job the conversation must complete
- The channel or surface the script will run in
- Any known states, intents, or branch conditions
- Constraints such as latency, character limits, or handoff rules
- Existing product terminology, prompts, or surrounding UI context

## Workflow

1. Identify the conversation goal and the moment when the interaction begins.
2. Break the flow into distinct turns, including user inputs, system responses, and transition points.
3. Write the happy path first, then add alternate branches and exits.
4. Make every branch explicit so the script can be tested or implemented without guesswork.
5. Check that each response advances the task, requests the right next input, or closes the loop cleanly.
6. Verify that the sequence matches the product's real capabilities and constraints.

## Design Principles / Evaluation Criteria

- One conversation turn should do one clear job
- Branches should be explicit instead of implied
- The script should be easy to implement and easy to test
- Transitions should feel natural, not abrupt
- The flow should remain understandable when read without visual diagrams

## Output Contract

- A complete dialogue script with user and system turns
- Branch annotations for alternate paths, fallbacks, or handoffs
- Notes on unresolved assumptions or implementation dependencies

## Examples

### Example 1

Input:
- Goal: Help a user reset their password
- Constraints: Must support a locked-account branch

Expected output:
- A dialogue script covering the happy path, locked-account branch, and exit states
- A note indicating where human support should appear if self-service fails

## Guardrails

- Do not leave critical turns as placeholders
- Do not assume a branch exists unless the product can actually support it
- Do not collapse multi-turn interactions into a single generic prompt
- Do not hide state changes that affect the user experience

## Optional Tools / Resources

- Notion MCP, Figma MCP, and Chrome DevTools MCP for grounding the conversation in real UI and product context
- `chrome-take-snapshot` for grounding the script in the live UI
- `search-query` for precedents and interaction patterns
- `apply-patch` for writing the resulting conversation artifact
- [Conversation Design Institute](https://www.conversationdesigninstitute.com/)
- [Dialogflow Conversation Design Guide](https://conversation-design.web.app/)
- [Google Conversational Design resources](https://design.google/library)
- [Plain Language Guide](https://digital.gov/guides/plain-language/)
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
