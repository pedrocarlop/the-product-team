#!/usr/bin/env bash
set -euo pipefail
# Local Cron Trigger for Product Team Self-Improvement
# Usage: ./cron-trigger.sh <scenario> <role> <skill>

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"

SCENARIO="${1:-modern-saas-dashboard}"
ROLE="${2:-design/ui-designer}"
SKILL="${3:-ui-concept-direction}"

echo "Starting Product Team Self-Improvement Cycle..."
echo "Scenario: ${SCENARIO}"
echo "Role: ${ROLE}"
echo "Skill: ${SKILL}"

# 1. Run Benchmark
python3 "${REPO_ROOT}/assets/auto-improve/benchmark.py" "${SCENARIO}" "${ROLE}" "${SKILL}"

# 2. Run Meta-Optimizer
python3 "${REPO_ROOT}/assets/auto-improve/meta_optimizer.py" "${SCENARIO}" "${ROLE}" "${SKILL}"

# 3. Check for Changes and commit only agent/skill files
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Improvement found. Committing changes..."
  git add agents/ references/ assets/auto-improve/
  git commit -m "Auto-Improve: Refined ${SKILL} based on ${SCENARIO} benchmark"
  echo "Skill Refined Successfully."
else
  echo "No improvement to commit (hill-climbing logic reached local optimum)."
fi
