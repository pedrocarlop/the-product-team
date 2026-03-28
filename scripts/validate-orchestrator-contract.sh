#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

errors=0

fail() {
  printf 'ERROR: %s\n' "$1" >&2
  errors=$((errors + 1))
}

legacy_productin='\.pro'"ductin"
legacy_workflow_name='Product'"in workflow"
legacy_workflow_state='workflow-'"state\.md"
legacy_request='request-normal'"ized\.md"
legacy_may_advance='may_advance_'"stage"
legacy_may_update='may_update_workflow_'"state"
legacy_stage_requirement='when_'"stage_active"
legacy_stage_phrase='Advance workflow '"stages"
legacy_pattern="${legacy_productin}|${legacy_workflow_name}|${legacy_workflow_state}|${legacy_request}|${legacy_may_advance}|${legacy_may_update}|${legacy_stage_requirement}|${legacy_stage_phrase}"

if rg -n "$legacy_pattern" agents logs >/tmp/orchestrator-legacy-check.txt; then
  fail "Legacy workflow references remain in agents or logs."
  cat /tmp/orchestrator-legacy-check.txt >&2
fi

[[ -f logs/README.md ]] || fail "Missing logs/README.md."
[[ -f references/role-catalog.md ]] || fail "Missing references/role-catalog.md."
[[ -d logs/active ]] || fail "Missing logs/active directory."
[[ -d logs/archive ]] || fail "Missing logs/archive directory."

python3 scripts/render_role_catalog.py --check >/tmp/role-catalog-check.txt || {
  fail "Role catalog is missing or stale."
  cat /tmp/role-catalog-check.txt >&2
}

python3 scripts/render_skill_catalogs.py --check >/tmp/skill-catalog-check.txt || {
  fail "Skill catalogs are missing or stale."
  cat /tmp/skill-catalog-check.txt >&2
}

orchestrator_file="agents/orchestrator/orchestrator/orchestrator.toml"
[[ -f "$orchestrator_file" ]] || fail "Missing orchestrator role file."

if [[ -f "$orchestrator_file" ]]; then
  rg -q 'role_kind = "orchestrator"' "$orchestrator_file" || fail "Orchestrator role_kind must be orchestrator."
  rg -q '00_routing\.md' "$orchestrator_file" || fail "Orchestrator must own 00_routing.md."
  rg -q '03_unified-plan\.md' "$orchestrator_file" || fail "Orchestrator must own 03_unified-plan.md."
  rg -q '04_approval\.md' "$orchestrator_file" || fail "Orchestrator must own 04_approval.md."
fi

while IFS= read -r file; do
  role="$(basename "$file" .toml)"

  if [[ "$role" == "orchestrator" ]]; then
    continue
  fi

  if [[ "$role" == "reference" ]]; then
    rg -q 'role_kind = "reference"' "$file" || fail "Reference role must use role_kind = \"reference\": $file"
    rg -q 'artifact_paths = \[\]' "$file" || fail "Reference role must not own artifacts: $file"
    rg -q 'may_write_paths = \[\]' "$file" || fail "Reference role must not write logs or repo artifacts: $file"
    continue
  fi

  rg -q 'subagent_requirement = "required"' "$file" || fail "Specialist must require subagent execution: $file"
  rg -q 'handoff_to = \["orchestrator"\]' "$file" || fail "Specialist must hand off to orchestrator: $file"
  rg -q "logs/active/<project-slug>/plans/$role\\.md" "$file" || fail "Missing per-role plan path: $file"

  if rg -q 'role_kind = "reviewer"' "$file"; then
    rg -q "logs/active/<project-slug>/reviews/$role\\.md" "$file" || fail "Reviewer missing review artifact path: $file"
  else
    rg -q "logs/active/<project-slug>/deliverables/$role\\.md" "$file" || fail "Executor missing deliverable artifact path: $file"
  fi
done < <(python3 - <<'PY'
from pathlib import Path
import sys

root = Path.cwd()
sys.path.insert(0, str(root / "scripts"))
from lib.toml_utils import discover_toml_paths

for path in discover_toml_paths(root):
    print(path.as_posix())
PY
)

if (( errors > 0 )); then
  exit 1
fi

echo "Orchestrator contract validation passed."
