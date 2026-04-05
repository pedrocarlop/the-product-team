#!/usr/bin/env bash
# Regenerate the three platform fragment files from the shared template.
# Usage: ./generate-fragments.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS_DIR="$(cd "${SCRIPT_DIR}/../assets" && pwd)"
TEMPLATE="${ASSETS_DIR}/product-team.fragment.template.md"

if [[ ! -f "${TEMPLATE}" ]]; then
  echo "ERROR: Template not found at ${TEMPLATE}" >&2
  exit 1
fi

COMMENT="<!-- Generated from product-team.fragment.template.md — edit the template, then run scripts/generate-fragments.sh -->"

for TUPLE in "AGENTS.fragment.md:Codex:.codex" "CLAUDE.fragment.md:Claude:.claude" "ANTIGRAVITY.fragment.md:Antigravity:.antigravity"; do
  FILE="${TUPLE%%:*}"
  REST="${TUPLE#*:}"
  PLATFORM="${REST%%:*}"
  PACKAGE_DIR="${REST#*:}"
  OUTPUT="${ASSETS_DIR}/${FILE}"
  { echo "${COMMENT}"; sed -e "s/{{PLATFORM}}/${PLATFORM}/g" -e "s|{{PACKAGE_DIR}}|${PACKAGE_DIR}|g" "${TEMPLATE}"; } > "${OUTPUT}"
  echo "Generated ${FILE} (platform: ${PLATFORM}, base_dir: ${PACKAGE_DIR})"
done

echo "Done. All fragment files are up to date."
