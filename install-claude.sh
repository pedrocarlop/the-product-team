#!/usr/bin/env bash
# Thin wrapper: installs Product Team for Claude Code.
# Equivalent to: ./install.sh --platform claude
set -euo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "${SELF_DIR}/install.sh" --platform claude "$@"
