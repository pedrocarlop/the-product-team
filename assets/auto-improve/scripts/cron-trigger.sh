#!/usr/bin/env bash
set -euo pipefail
# Local Cron Trigger for Product Team Self-Improvement
# Usage: ./cron-trigger.sh [--runner <dry-run|codex|claude>] [--dry-run] <scenario> <role> <skill>

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"

# Parse flags
RUNNER="dry-run"
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --runner)
      RUNNER="${2:?--runner requires a value (dry-run|codex|claude)}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    *)
      break
      ;;
  esac
done

SCENARIO="${1:-modern-saas-dashboard}"
ROLE="${2:-design/ui-designer}"
SKILL="${3:-ui-concept-direction}"

echo "=========================================="
echo "Product Team Self-Improvement Cycle"
echo "=========================================="
echo "Scenario : ${SCENARIO}"
echo "Role     : ${ROLE}"
echo "Skill    : ${SKILL}"
echo "Runner   : ${RUNNER}"
echo "Dry-run  : ${DRY_RUN}"
echo "=========================================="

if $DRY_RUN; then
  echo ""
  echo "[DRY-RUN] Would execute the following steps:"
  echo "  1. benchmark.py ${SCENARIO} ${ROLE} ${SKILL} --runner ${RUNNER}"
  echo "  2. judge.py <artifact> --type <inferred>"
  echo "  3. meta_optimizer.py ${SCENARIO} ${ROLE} ${SKILL}"
  echo "  4. git add + commit (if changes detected)"
  echo ""
  echo "No actions taken."
  exit 0
fi

# 1. Run Benchmark (prepare context + optionally execute via runner)
echo ""
echo "--- Step 1: Run Benchmark ---"
BENCHMARK_OUTPUT=$(python3 "${REPO_ROOT}/assets/auto-improve/benchmark.py" \
  "${SCENARIO}" "${ROLE}" "${SKILL}" --runner "${RUNNER}")
echo "${BENCHMARK_OUTPUT}"

# Extract the run_dir from benchmark output
RUN_DIR=$(echo "${BENCHMARK_OUTPUT}" | python3 -c "import sys, json; print(json.load(sys.stdin)['run_dir'])" 2>/dev/null || true)

if [[ -z "${RUN_DIR}" || ! -d "${RUN_DIR}" ]]; then
  echo "WARNING: Could not determine run directory from benchmark output."
  echo "Attempting to find latest run..."
  RUN_DIR=$(ls -td "${REPO_ROOT}/logs/benchmarks/${SCENARIO}_"* 2>/dev/null | head -1 || true)
fi

if [[ -z "${RUN_DIR}" || ! -d "${RUN_DIR}" ]]; then
  echo "ERROR: No run directory found. Aborting."
  exit 1
fi

# 2. Run Judge on the produced artifact
echo ""
echo "--- Step 2: Run Judge ---"
# Find the artifact (first file that isn't context.md or runner-error.log)
ARTIFACT=$(find "${RUN_DIR}" -maxdepth 1 -type f \
  ! -name "context.md" ! -name "runner-error.log" | head -1 || true)

if [[ -n "${ARTIFACT}" && -f "${ARTIFACT}" ]]; then
  # Infer scenario type
  SCENARIO_LOWER=$(echo "${SCENARIO}" | tr '[:upper:]' '[:lower:]')
  if echo "${SCENARIO_LOWER}" | grep -qE "(engineering|backend|api|platform|schema|frontend)"; then
    SCENARIO_TYPE="engineering"
  elif echo "${SCENARIO_LOWER}" | grep -qE "(business|prd|go-to-market|launch|qa|release)"; then
    SCENARIO_TYPE="business"
  else
    SCENARIO_TYPE="design"
  fi

  echo "Artifact : ${ARTIFACT}"
  echo "Type     : ${SCENARIO_TYPE}"

  JUDGE_OUTPUT=$(python3 "${REPO_ROOT}/assets/auto-improve/judge.py" \
    "${ARTIFACT}" --type "${SCENARIO_TYPE}" 2>&1)
  echo "${JUDGE_OUTPUT}"

  # Extract score for display
  SCORE=$(echo "${JUDGE_OUTPUT}" | python3 -c "import sys, json; print(json.load(sys.stdin)['score'])" 2>/dev/null || echo "?")
  PASSED=$(echo "${JUDGE_OUTPUT}" | python3 -c "import sys, json; print(json.load(sys.stdin)['passed'])" 2>/dev/null || echo "?")

  echo ""
  echo "=========================================="
  echo "SCORE  : ${SCORE} / 1.0"
  echo "PASSED : ${PASSED}"
  echo "=========================================="
else
  echo "No artifact found to judge (runner=${RUNNER} may not have produced output)."
  SCORE="N/A"
fi

# 3. Run Meta-Optimizer
echo ""
echo "--- Step 3: Run Meta-Optimizer ---"
python3 "${REPO_ROOT}/assets/auto-improve/meta_optimizer.py" \
  "${SCENARIO}" "${ROLE}" "${SKILL}"

# 4. Check for Changes and commit only agent/skill files
echo ""
echo "--- Step 4: Check for Changes ---"
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Improvement found. Committing changes..."
  git add agents/ references/ assets/auto-improve/
  git commit -m "Auto-Improve: Refined ${SKILL} based on ${SCENARIO} benchmark (score: ${SCORE})"
  echo "Skill Refined Successfully."
else
  echo "No improvement to commit (hill-climbing logic reached local optimum)."
fi
