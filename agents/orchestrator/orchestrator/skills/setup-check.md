---
name: setup-check
description: Handle an hta_setup_required signal — pause execution, ask the prompter to configure the HTA or authorize fallback, then resume.
trigger: When a subagent returns hta_setup_required during coordinate.
primary_mcp: conversation context
fallback_tools: orchestrator/log
best_guess_output: A resolved HTA decision (configure or fallback) logged to context.md.
output_artifacts: logs/active/<project-slug>/deliverables/orchestrator.md
done_when: HTA is either configured and verified, or fallback is explicitly authorized by the prompter.
---

# Setup Check

## Purpose

Handle an `hta_setup_required` signal from a subagent. Pause execution, surface the missing configuration to the prompter, and resume only after the HTA is configured or fallback is explicitly authorized.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: orchestrator
project: <slug>
deliverable: orchestrator.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Identify the Block
From the subagent's `hta_setup_required` signal, extract:
- **Blocked role**: which subagent returned the signal.
- **Blocked MCP**: which tool or MCP server is not configured or accessible.
- **Blocked skill**: which assigned skill requires that MCP (from the skill's `primary_mcp` frontmatter).
- **Required config**: what the prompter would need to provide (e.g., API key, URL, credentials, endpoint) based on the role's `[capabilities].mcp_servers` declaration.

Record `hta_status: unresolved` for the blocked role in `context.md` if not already set.

### Step 3: Pause Execution
Do not launch or re-launch any subagent. Hold the coordinate workflow until this skill produces a resolution.

### Step 4: Present to the Prompter
Surface the block clearly with the following structure:

```
⚠ HTA Setup Required

Role blocked: <role name>
Required HTA: <MCP/tool name>
Needed by skill: <skill name>
Configuration needed: <API key / URL / credentials / endpoint — be specific>

Options:
  (a) Provide the configuration now to enable this HTA.
  (b) Skip configuration and authorize fallback for this execution only.
```

Wait for the prompter's response before proceeding.

### Step 5: Resolve Based on Prompter Decision

**If the prompter provides configuration:**
- Acknowledge the configuration (do not store secrets in logs).
- Record `hta_status: configured` for the blocked role in `context.md`.
- Note which MCP was resolved.
- Return control to `coordinate` to re-launch the subagent.

**If the prompter authorizes fallback:**
- Record `hta_status: fallback_authorized` for the blocked role in `context.md`.
- Note that the subagent must label its output `evidence_mode: fallback` or `inferred`.
- Return control to `coordinate` to re-launch the subagent with explicit fallback authorization.

### Step 6: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section:
- **What worked**: which path was taken and why.
- **What didn't**: any ambiguity in the config request or prompter response.
- **Next steps**: confirm the subagent was re-launched and the block is cleared.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/orchestrator.md`.
- Update `context.md` with `hta_status: configured` or `hta_status: fallback_authorized` for the resolved role.
- Ensure the work meets this done-when bar: HTA is either configured and verified, or fallback is explicitly authorized by the prompter.
