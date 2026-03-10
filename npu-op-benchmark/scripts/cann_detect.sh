#!/usr/bin/env bash
set -euo pipefail
TOOLKIT_PATH="${1:-/usr/local/Ascend/ascend-toolkit}"
echo "toolkit_path=${TOOLKIT_PATH}"
if [[ -f "${TOOLKIT_PATH}/set_env.sh" ]]; then
  echo "set_env_exists=true"
else
  echo "set_env_exists=false"
fi
if [[ -e "${TOOLKIT_PATH}/latest" ]]; then
  echo "latest_ll=$(ls -ld "${TOOLKIT_PATH}/latest")"
else
  echo "latest_ll=missing"
fi
find "${TOOLKIT_PATH}" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | sort | sed 's/^/version_dir=/' || true
