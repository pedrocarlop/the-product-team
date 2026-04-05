# `/app` — Code Outputs

`/app` contains code and website outputs when a project produces software. Only the explicit `repo_write_owner` may write here, governed by the orchestrator's assignment contract.

## Directory Layout

```text
app/
  web/                           # Website / frontend code
```

## Write Policy

- Only the agent named as `repo_write_owner` in the assignment contract may write to `app/`.
- The `repo_write_scope` field defines the exact subdirectory the agent may modify (e.g., `app/web/`).
- If a role is not the named `repo_write_owner`, it must return a mismatch note instead of writing code.
- Parallel repo writers are allowed only when `repo_write_scope` values are explicitly disjoint.
