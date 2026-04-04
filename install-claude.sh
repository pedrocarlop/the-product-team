#!/usr/bin/env bash
set -euo pipefail

SELF_DIR=""
if [[ -n "${BASH_SOURCE[0]-}" && -f "${BASH_SOURCE[0]}" ]]; then
  SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

if [[ -n "${SELF_DIR}" && -f "${SELF_DIR}/scripts/install-claude.py" ]]; then
  exec python3 "${SELF_DIR}/scripts/install-claude.py" "$@"
fi

REPO_OWNER="pedrocarlop"
REPO_NAME="the-product-team"
REPO_REF="${PRODUCT_TEAM_REF:-main}"
REPO_URL="${PRODUCT_TEAM_REPO_URL:-https://github.com/${REPO_OWNER}/${REPO_NAME}}"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

ARCHIVE_URL="${PRODUCT_TEAM_ARCHIVE_URL:-${REPO_URL}/archive/refs/heads/${REPO_REF}.tar.gz}"
curl -fsSL "${ARCHIVE_URL}" | tar -xzf - -C "${TMP_DIR}"
ARCHIVE_ROOT="$(find "${TMP_DIR}" -mindepth 1 -maxdepth 1 -type d | head -n 1)"

if [[ -z "${ARCHIVE_ROOT}" || ! -f "${ARCHIVE_ROOT}/scripts/install-claude.py" ]]; then
  printf 'Could not find scripts/install-claude.py in archive from %s\n' "${ARCHIVE_URL}" >&2
  exit 1
fi

exec python3 "${ARCHIVE_ROOT}/scripts/install-claude.py" \
  --source-repo-url "${REPO_URL}" \
  --source-ref "${REPO_REF}" \
  --source-archive-url "${ARCHIVE_URL}" \
  "$@"
