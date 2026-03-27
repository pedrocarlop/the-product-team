---
name: frame
description: Turn a machine learning request into a justified problem framing with a baseline, success metric, and failure mode before any model work starts.
activation_hints:
  - "Use when a request could be solved by ML, rules, retrieval, or prompting and the right approach is not yet clear."
  - "Route here before data exploration, training, prompt design, or architecture decisions."
  - "Do not use once the objective, metric, and deployment context are already settled."
---

# Frame

## Purpose

Use this skill to decide whether the problem should use machine learning, what outcome it should move, and what success and failure look like before implementation starts.

## When to Use

- When the request is broad, ambiguous, or solution-first
- When it is unclear whether ML, rules, retrieval, or prompting is the right approach
- When the business outcome, operating constraints, or failure mode have not been made explicit

## When Not to Use

- When the target metric and system boundary are already defined
- When the task is mainly model comparison, training, serving, or monitoring
- When the work is a pure implementation change with no framing ambiguity

## Required Inputs

- The request in plain language
- The decision this work should support
- The business metric or product outcome that matters
- Latency, cost, safety, privacy, and operational constraints
- Known data sources, labels, or retrieval sources
- Any prior baseline, heuristic, or prototype

## Workflow

1. Restate the request as a decision-oriented ML question.
2. Decide whether a deterministic rule, retrieval pattern, or prompt is sufficient before reaching for a model.
3. Define the input, output, and operating context of the system.
4. Identify the success metric, target threshold, and acceptable tradeoff.
5. Write down the baseline and the failure modes, including who is affected when the system is wrong.
6. Call out missing data, bias risks, and open questions that must be resolved before evaluation starts.

## Design Principles / Evaluation Criteria

- Decision-first framing over model-first enthusiasm
- The simplest viable solution should win if it meets the target
- Success metrics must map to a business outcome, not just a technical score
- Failure modes and harm cases are part of the frame, not an afterthought
- Constraints should be explicit enough to prevent hidden scope creep

## Output Contract

- A framed ML problem statement
- The decision it supports and the intended user
- The success metric, target threshold, and baseline
- Constraints, assumptions, and exclusions
- Open questions that must be answered before evaluation or build work starts

## Examples

### Example 1

Input:
- Request: "Can we use AI to reduce support tickets?"
- Context: The team is unsure whether this should be classification, search, or automation

Expected output:
- Framed question: "Which support intents can be safely routed to a self-serve answer or deterministic flow, and where is a model actually needed?"
- Decision: Whether to automate, assist, or leave the workflow unchanged
- Baseline: Intent rules plus top FAQ retrieval

## Guardrails

- Do not jump into model choice before defining the business decision
- Do not assume ML is needed if rules or retrieval are enough
- Do not skip the baseline because the request is urgent
- Do not hide uncertainty about labels, data quality, or downstream harm

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Linear MCP, Sentry MCP
- Websites: [PyTorch Docs](https://pytorch.org/docs/stable/index.html), [TensorFlow Docs](https://www.tensorflow.org/api_docs), [Hugging Face Docs](https://huggingface.co/docs), [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html), [Weights & Biases Docs](https://docs.wandb.ai/)
- Product requirements and workflow state
- Prior experiments, dashboards, or support data
- Notion for recording the frame and baseline
- Data catalog or schema docs for source discovery
