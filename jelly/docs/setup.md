# Local compiler setup

Assessment on 21 October 2026, before installation:

| Component | Observed status | Action |
| --- | --- | --- |
| Windows | x64, build 26300, display version 26H2 (registry ProductName reports Windows 10 Pro) | Preserve system configuration |
| WSL2 | Installed; default version 2 | Reuse |
| Ubuntu | Existing `Ubuntu` distribution is Ubuntu 26.04 LTS, x86_64, WSL2 | Reuse; preserve docker-desktop distribution |
| Swift | No Swift/Swiftly found in Ubuntu or Swift on Windows PATH | Install official Swiftly and test a supported toolchain |
| Git | Windows 2.52.0; Ubuntu 2.53.0 | Reuse |
| Open-Jellycore | No compiler found | Build official pinned source inside Linux filesystem |
| VS Code | Windows installation and Jelly language extension present; WSL extension absent | Install Microsoft WSL extension; add build tasks |

WSL inspection needs execution outside Codex's restricted Windows sandbox: the
sandbox returns `Wsl/EnumerateDistros/Service/E_ACCESSDENIED`. This does not mean
WSL is broken. CIM inspection is also denied there; registry and architecture
checks supplied the Windows details above. No WSL installation or restart was needed.

The compiler checkout is `~/.local/share/jelly-tools/Open-Jellycore` in Ubuntu,
at `e1ec31c2ee192c8721749f9eb3b50108e38891cf`. Package.swift requires at least
Swift 5.7. The repository's resolved dependency versions are preserved.

Sources consulted:

- [Official repository and CLI](https://github.com/OpenJelly/Open-Jellycore)
- [Swift Linux installation](https://www.swift.org/install/linux/)
- [Ubuntu 26.04 toolchains](https://www.swift.org/install/linux/ubuntu/26_04/)
- [Swiftly automation options](https://docs.swift.org/latest/documentation/swiftlydocs/automated-install/)
- [Jellycuts Linux article](https://www.jellycuts.com/2024/05/creating-a-shortcut-for-ios-using-swift-on-a-raspberry-pi-with-openjelly/)

The article uses Docker; this workspace uses Swift directly inside WSL instead.
Do not follow the article's Docker removal or system upgrade steps for this setup.

## Installation performed

Swiftly 1.2.0 was downloaded from the official Swift Linux installer URL and
initialized with `--skip-install --assume-yes --quiet-shell-followup`. It writes
`~/.local/share/swiftly/env.sh` and updates the user's profile. Swift 6.4.1 was
installed explicitly, with Swiftly's default toolchain signature verification,
then linked with `swiftly link 6.4.1 --assume-yes`. This is a native Ubuntu 26.04
toolchain; Swift 5.7 is the package minimum, not a requirement to install precisely
5.7. Compatibility is determined by building the unchanged package, not by assuming
that the latest Swift is suitable.

These Ubuntu packages were installed (including their apt dependencies), without
an unrelated system upgrade:

```sh
sudo apt-get update
sudo apt-get install -y --no-install-recommends build-essential clang \
  libcurl4-openssl-dev libxml2-dev libicu-dev libedit-dev libsqlite3-dev \
  libncurses-dev zlib1g-dev pkg-config binutils-gold unzip zip gnupg2 \
  libpython3-dev libz3-dev
```

The second group was requested by Swiftly's post-install dependency check.
These commands require **Linux root/sudo**, not changes to Windows features.
During this session they ran via `wsl -d Ubuntu -u root -- ...`, with sandbox
escalation. Normal builds run as `henryhowe`, not root. Existing distributions,
Docker configuration and production sources are preserved.

A basic `swiftc` application was compiled and executed successfully; it printed
`Swift local compilation works`. Swift reports `6.4.1 (swift-6.4.1-RELEASE)` and
target `x86_64-unknown-linux-gnu`. Build log: `~/.cache/jelly-setup/build.log`.

Microsoft's VS Code WSL extension `ms-vscode-remote.remote-wsl` 0.104.4 was
installed using `code --install-extension ms-vscode-remote.remote-wsl`.

To reproduce the user installation in a compatible Ubuntu distro after installing
the packages above:

```sh
mkdir -p ~/.cache/jelly-setup
cd ~/.cache/jelly-setup
curl -fL https://download.swift.org/swiftly/linux/swiftly-x86_64.tar.gz -o swiftly.tar.gz
tar xzf swiftly.tar.gz
./swiftly init --skip-install --assume-yes --quiet-shell-followup
```

Then, inside this repository's `jelly/` folder in WSL:

```sh
bash scripts/setup-compiler.sh
source ~/.profile
jelly --help
python3 scripts/build.py tests/compiler/hello-world.jelly
```

The script reuses installed Swift, clones only when absent, refuses a dirty or
different compiler revision, and builds inside Linux. The Ubuntu 26.04/x86_64
toolchain was verified here; other distributions/architectures require checking
Swift availability before reproducing these commands. No dependency source was
patched. Compiler package/build cache stays outside the repository. Do not run
the user setup script as root.

## Filesystem choice

Keep this small Jelly source repository on Windows, as requested. Store Swift,
the compiler checkout, package downloads and Swift build products inside Linux;
this avoids expensive Swift builds on `/mnt/c` while retaining convenient Windows
Git access. The Windows workspace path contains spaces and is part of validation.

For larger Linux-heavy development, a repository in `~/projects/` opened through
**WSL: Connect to WSL using Distro** offers better Linux file performance and
permissions. Windows can browse that directory through `\\wsl.localhost\Ubuntu\home\henryhowe`.
Use one checkout per workflow; avoid concurrent Windows/Linux Git writes in the
same checkout. Both workspace locations can use the Python build entry point.
