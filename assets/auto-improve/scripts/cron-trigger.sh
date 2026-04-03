#!/bin/bash
# Local Cron Trigger for Product Team Self-Improvement
# Usage: ./cron-trigger.sh <scenario> <role> <skill>

SCENARIO=${1:-modern-saas-dashboard}
ROLE=${2:-design/ui-designer}
SKILL=${3:-ui-concept-direction}

echo "Starting Product Team Self-Improvement Cycle..."
echo "Scenario: $SCENARIO"
echo "Role: $ROLE"
echo "Skill: $SKILL"

# 1. Run Benchmark
python3 .codex/product-team/auto-improve/benchmark.py "$SCENARIO" "$ROLE" "$SKILL"

# 2. Run Meta-Optimizer
python3 .codex/product-team/auto-improve/meta_optimizer.py "$SCENARIO" "$ROLE" "$SKILL"

# 3. Check for Changes
if [[ -n $(git status --porcelain) ]]; then
  echo "Improvement found. Committing changes..."
  git add .
  git commit -m "Auto-Improve: Refined $SKILL based on $SCENARIO benchmark"
  echo "Skill Refined Successfully."
else
  echo "No improvement to commit (hill-climbing logic reached local optimum)."
fi
