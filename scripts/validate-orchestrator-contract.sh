#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

errors=0
CHECK_DIR="$(mktemp -d)"
trap 'rm -rf "${CHECK_DIR}"' EXIT

fail() {
  printf 'ERROR: %s\n' "$1" >&2
  errors=$((errors + 1))
}

[[ -f logs/README.md ]] || fail "Missing logs/README.md."
[[ -f knowledge/README.md ]] || fail "Missing knowledge/README.md."
[[ -f references/role-catalog.md ]] || fail "Missing references/role-catalog.md."
[[ -d logs/active ]] || fail "Missing logs/active directory."
[[ -d logs/archive ]] || fail "Missing logs/archive directory."
[[ -d knowledge/assets ]] || fail "Missing knowledge/assets directory."
[[ -d knowledge/reviews ]] || fail "Missing knowledge/reviews directory."

python3 scripts/render_role_catalog.py --check >"${CHECK_DIR}/role-catalog-check.txt" || {
  fail "Role catalog is missing or stale."
  cat "${CHECK_DIR}/role-catalog-check.txt" >&2
}

python3 scripts/render_skill_catalogs.py --check >"${CHECK_DIR}/skill-catalog-check.txt" || {
  fail "Skill catalogs are missing or stale."
  cat "${CHECK_DIR}/skill-catalog-check.txt" >&2
}

python3 scripts/render_role_prompts.py --check >"${CHECK_DIR}/role-prompt-check.txt" || {
  fail "Role prompts are missing or stale."
  cat "${CHECK_DIR}/role-prompt-check.txt" >&2
}

python3 scripts/render_agents_md.py --check >"${CHECK_DIR}/agents-md-check.txt" || {
  fail "AGENTS.md agent roster is missing or stale."
  cat "${CHECK_DIR}/agents-md-check.txt" >&2
}

python3 scripts/check-orchestrator-scenarios.py >"${CHECK_DIR}/orchestrator-scenario-check.txt" || {
  fail "Orchestrator scenario checks failed."
  cat "${CHECK_DIR}/orchestrator-scenario-check.txt" >&2
}

while IFS= read -r file; do
  role="$(basename "$file" .toml)"
  grep -q 'model_reasoning_effort' "$file" || fail "Missing model_reasoning_effort: $file"

  if [[ "$role" == "orchestrator" ]]; then
    grep -q 'role_kind = "orchestrator"' "$file" || fail "Orchestrator role_kind must be orchestrator."
    grep -q 'repo_write_policy = "direct_only"' "$file" || fail "Orchestrator repo_write_policy must be direct_only."
    grep -q 'skill_paths' "$file" || fail "Orchestrator prompt must mention skill_paths."
    continue
  fi

  if [[ "$role" == "reference" ]]; then
    grep -q 'role_kind = "reference"' "$file" || fail "Reference role must use role_kind = \"reference\": $file"
    grep -q 'artifact_paths = \[\]' "$file" || fail "Reference role must not own artifacts: $file"
    grep -q 'may_write_paths = \[\]' "$file" || fail "Reference role must not write artifacts: $file"
    continue
  fi

  grep -q 'subagent_requirement = "required"' "$file" || fail "Specialist must require subagent execution: $file"
  grep -q 'handoff_to = \["orchestrator"\]' "$file" || fail "Specialist must hand off to orchestrator: $file"
  grep -q 'skill_paths' "$file" || fail "Specialist prompt must mention skill_paths: $file"
  grep -q 'evidence_mode' "$file" || fail "Specialist prompt must mention evidence_mode: $file"
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
