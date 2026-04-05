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

declare -A PLATFORMS=(
  ["CLAUDE.fragment.md"]="Claude"
  ["AGENTS.fragment.md"]="Codex"
  ["ANTIGRAVITY.fragment.md"]="Antigravity"
)

for FILE in "${!PLATFORMS[@]}"; do
  PLATFORM="${PLATFORMS[$FILE]}"
  OUTPUT="${ASSETS_DIR}/${FILE}"
  sed "s/{{PLATFORM}}/${PLATFORM}/g" "${TEMPLATE}" > "${OUTPUT}"
  echo "Generated ${FILE} (platform: ${PLATFORM})"
done

echo "Done. All fragment files are up to date."
