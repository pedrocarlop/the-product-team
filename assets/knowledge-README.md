# `/knowledge` — Product Knowledge Base

This directory is the canonical source of truth for all product-related intelligence, research, strategies, and designs. It is the persistent memory of the Product Team.

## Directory Structure

- **`runs/`**: Snapshots of every deliverable at the moment of creation. Never overwrite files here; use it as a chronological version history.
- **`reviews/`**: Design and QA review readouts, feedback logs, and acceptance reports.
- **`entities/`**: Dedicated pages for cross-cutting concepts like Competitors, User Personas, Design Tokens, or Domain Models.
- **`assets/`**: Images, diagram source files, and other non-markdown attachments.
- **`index.md`**: The entry point for the knowledge base.
- **`changelog.md`**: A chronological record of every knowledge mutation.

## Rules for Agents

1.  **Lossless Snapshots**: When you create or update a deliverable, always write a copy to `knowledge/runs/<run-id>/` before updating the canonical version at the root of `knowledge/`.
2.  **Changelog Requirement**: Every meaningful change to the knowledge base must be appended to `knowledge/changelog.md`.
3.  **TL;DR Sections**: Every deliverable must include a `## TL;DR` section at the top for fast scanning.
4.  **Related Links**: Use the `related` field in the YAML header to cross-reference other deliverables.
5.  **Direct File Tools**: If the `knowledge` MCP is missing, use direct file-writing tools (like `write_to_file`) to maintain this structure.

## Rules for Humans

- Read `index.md` to navigate the latest state of the product.
- Use `changelog.md` to see what changed recently.
- Review `runs/` to understand the historical context of any decision.
