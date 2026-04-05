# Scenario: Platform Schema Migration

## Task
Plan a schema migration that adds multi-tenancy to an existing single-tenant PostgreSQL database. The application currently serves one customer with approximately 50 tables and 2M rows in the largest table. The migration must support tenant isolation while preserving existing data and maintaining service availability.

## Requirements
1. **Migration Steps**: Provide a numbered sequence of migration steps including adding tenant columns, creating indexes, updating constraints, and backfilling data. Each step must note whether it requires a lock and its estimated duration.
2. **Rollback Plan**: For each migration step, describe the rollback procedure. Identify which steps are reversible vs. one-way, and define the point-of-no-return.
3. **Data Migration Strategy**: Explain how existing data will be assigned to the initial tenant. Address foreign key relationships, orphaned records, and data validation checks.
4. **Zero-Downtime Approach**: Describe the strategy for running migrations without service interruption. Cover techniques like shadow columns, dual-write patterns, or phased cutover with feature flags.

## Output Contract
Produce a `migration-plan.md` artifact with ## sections for each requirement. Include SQL examples for critical migration steps and a risk assessment table.
