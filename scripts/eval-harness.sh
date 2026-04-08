#!/usr/bin/env bash

# Product Team Eval Harness
# Inspired by everything-claude-code evals

set -e

echo "[Eval Harness] Starting quality and test evaluation..."

PROJECT_DIR=${1:-"."}

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: Directory $PROJECT_DIR not found"
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

EVAL_REPORT="logs/hooks/eval-report.json"
mkdir -p "$(dirname "$EVAL_REPORT")"

pass_count=0
fail_count=0
results=""

# Check if npm/pnpm project uses vitest/jest
if [ -f "package.json" ]; then
    echo "[Eval Harness] Detected Node.js project. Scanning for test scripts..."
    if grep -q '"test"' package.json; then
        echo "[Eval Harness] Running NPM tests..."
        if npm run test -- --passWithNoTests; then
            results="\"node_tests\": \"pass\""
            pass_count=$((pass_count+1))
        else
            results="\"node_tests\": \"fail\""
            fail_count=$((fail_count+1))
        fi
    else
        results="\"node_tests\": \"skipped\""
    fi
fi

# Check if python project uses pytest
if [ -f "pytest.ini" ] || [ -f "requirements.txt" ] && grep -q "pytest" requirements.txt; then
    echo "[Eval Harness] Detected Python project with Pytest. Running..."
    if pytest -q; then
        if [ -n "$results" ]; then results="$results, "; fi
        results="${results}\"python_tests\": \"pass\""
        pass_count=$((pass_count+1))
    else
        if [ -n "$results" ]; then results="$results, "; fi
        results="${results}\"python_tests\": \"fail\""
        fail_count=$((fail_count+1))
    fi
fi

echo "[Eval Harness] Writing evaluation report to $EVAL_REPORT"
cat <<EOF > "$EVAL_REPORT"
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "total_passed_suites": $pass_count,
  "total_failed_suites": $fail_count,
  "details": {
    $results
  }
}
EOF

if [ $fail_count -gt 0 ]; then
    echo "[Eval Harness] Evaluation FAILED. See $EVAL_REPORT for details."
    exit 1
else
    echo "[Eval Harness] Evaluation PASSED. Code is ready for shipping."
    exit 0
fi
