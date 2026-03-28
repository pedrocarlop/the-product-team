---
name: apply-patch
tool: apply_patch
description: Write and update the conversation design artifacts — dialogue flows, prompt patterns, and fallback paths.
---

# Apply Patch

Use this skill to write or revise the conversation design package artifacts. It is the primary output mechanism for producing `task-flows.md`, `ui-spec.md`, `research-and-rationale.md`, and `component-mapping.md`.

## When to Use

- After research and flow planning are complete and you are ready to author a design artifact
- When revising a conversation flow based on validation feedback
- When adding or correcting dialogue states, fallback paths, or escalation triggers

## How to Use

Invoke `apply_patch` with the target file path and the structured content to write. Always:
1. Start with the shared structured contract at the top of each file
2. Use the exact file paths defined in `[outputs]`
3. Write all dialogue states completely — do not leave states as stubs

## What to Produce

- **task-flows.md**: Full conversation trees with all branches — happy path, error recovery, escalation, and fallback
- **ui-spec.md**: Prompt templates, response patterns, tone guidelines, and character limits
- **research-and-rationale.md**: Rationale for dialogue choices, tone decisions, and fallback strategy
- **component-mapping.md**: Mapping of each dialogue surface to the `CMP-*` component or AI interface element

## Notes for Conversation Designer

Complete all conversation states before writing the artifact. A dialogue flow that only covers the happy path is incomplete. Every prompt needs a documented fallback. Every escalation path needs a defined trigger condition.
