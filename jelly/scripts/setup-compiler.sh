#!/usr/bin/env bash
# Run inside the chosen WSL distro, as the ordinary development user.
set -euo pipefail
revision=e1ec31c2ee192c8721749f9eb3b50108e38891cf
toolchain=6.4.1
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
tools_dir="$HOME/.local/share/jelly-tools"
checkout="$tools_dir/Open-Jellycore"
if [[ ! -f "$HOME/.local/share/swiftly/env.sh" ]]; then
    echo 'Install official Swiftly first; see jelly/docs/setup.md.' >&2
    exit 2
fi
source "$HOME/.local/share/swiftly/env.sh"
swiftly install "$toolchain" --assume-yes
swiftly link "$toolchain" --assume-yes
mkdir -p "$tools_dir"
if [[ ! -d "$checkout" ]]; then
    git clone https://github.com/OpenJelly/Open-Jellycore.git "$checkout"
fi
cd "$checkout"
if [[ "$(git rev-parse HEAD)" != "$revision" || -n "$(git status --porcelain)" ]]; then
    echo 'Existing compiler checkout differs from the pinned clean revision; inspect it before rebuilding.' >&2
    exit 2
fi
swiftly run swift build -c release --product jelly +"$toolchain"
mkdir -p "$HOME/.local/bin"
install -m 755 "$script_dir/jelly-cli.sh" "$HOME/.local/bin/jelly"
"$HOME/.local/bin/jelly" --help
printf '\nInstalled pinned Jellycore. Start a new login shell to refresh PATH.\n'
