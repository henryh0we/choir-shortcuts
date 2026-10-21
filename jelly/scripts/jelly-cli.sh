#!/usr/bin/env bash
set -euo pipefail
# Swiftly's environment also supplies runtime library/toolchain paths.
if [[ -f "$HOME/.local/share/swiftly/env.sh" ]]; then
    source "$HOME/.local/share/swiftly/env.sh"
fi
exec "$HOME/.local/share/jelly-tools/Open-Jellycore/.build/release/jelly" "$@"
