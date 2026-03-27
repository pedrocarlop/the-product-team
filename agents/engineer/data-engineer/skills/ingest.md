---
name: ingest
description: Design and operate reliable data ingestion from source systems into raw or landing zones with clear contracts, observability, and backfill safety.
activation_hints:
  - "Use when a task involves bringing new data into the warehouse, changing a connector, or fixing a broken extract/load path."
  - "Route here for source contracts, incremental syncs, backfills, load validation, or ingestion incident response."
  - "Do not use for transformation logic, marts, or downstream metric definitions."
---

# Ingest

## Purpose

Use this skill to move data from source systems into a trusted raw or landing layer with predictable timing, clear ownership, and enough observability to recover quickly when something breaks.

## When to Use

- When onboarding a new SaaS, database, file, API, or event source
- When a sync is failing, lagging, or missing records
- When you need to design incremental extraction, replay, or backfill behavior
- When ingestion contracts, auth, schema drift, or freshness SLAs need to be defined

## When Not to Use

- When the main work is modeling, joining, or reshaping data for analysis
- When the task is scheduling or coordinating downstream tasks rather than moving data
- When the issue is data governance policy rather than source loading mechanics

## Required Inputs

- Source system, owner, and access method
- Expected volume, cadence, and freshness requirement
- Destination layer and naming convention
- Schema or payload examples, including edge cases
- Backfill requirements and replay window
- Failure modes already observed or expected

## Workflow

1. Identify the source of truth and the exact contract the source already provides.
2. Choose the simplest reliable ingestion path, preferring managed connectors over custom code.
3. Decide whether the load should be full refresh, incremental, or event-driven based on source behavior and recovery cost.
4. Define idempotent load behavior so reruns do not duplicate or corrupt records.
5. Capture load metadata such as row counts, offsets, high-watermarks, and latency on every run.
6. Add validation and alerting that make missing, late, or malformed data visible quickly.
7. Document how to replay, backfill, and investigate the pipeline before shipping it.

## Design Principles / Evaluation Criteria

- Prefer managed connectors when they meet the need
- Capture raw data before applying business logic
- Make reruns safe and deterministic
- Preserve enough metadata to reconstruct failures
- Treat freshness and completeness as first-class requirements

## Output Contract

- Ingestion design or implementation plan
- Source contract and loading strategy
- Validation, retry, and alerting approach
- Backfill or replay procedure
- Short runbook for operational use

## Examples

### Example 1

Input:
- Source: Stripe API
- Problem: Daily sync misses late-arriving invoices
- Requirement: Keep raw data complete and replayable

Expected output:
- Recommendation: Incremental ingestion with a durable high-watermark, raw landing tables, and a replay path for the last N days
- Rationale: Preserves completeness while avoiding duplicate loads

## Guardrails

- Do not build custom extractors when a managed connector already solves the source reliably
- Do not mix source loading with transformation logic
- Do not rely on manual reruns as the recovery plan
- Do not ship ingestion without row-count, latency, and failure visibility

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Linear MCP
- Websites: [Apache Spark Docs](https://spark.apache.org/docs/latest/), [Apache Airflow Docs](https://airflow.apache.org/docs/), [dbt Docs](https://docs.getdbt.com/), [Snowflake Documentation](https://docs.snowflake.com/), [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- Source API docs or database schema
- Connector configuration and logs
- Warehouse landing-table conventions
- Incident history and replay requirements
