# Local build record ? generation groups

Recorded 4 November 2026. Comparison profile: Open-Jellycore
`e1ec31c2ee192c8721749f9eb3b50108e38891cf`, Swift 6.4.1 in WSL Ubuntu.
Each source was run through the repository build wrapper using explicit paths;
no production source, compiler implementation or validation policy was changed.

**10/16 accepted compiler + basic structural exports; 6 failed. All iPad results
are Not run.** Accepted means only the wrapper's documented checks passed. These
include plist/action shape, UUID references and text-attachment ranges, not all
Apple action schemas, If/Repeat fidelity or actual default fields.

## Results

| Source | Local wrapper | Interpretation |
| --- | --- | --- |
| [g1a-presence](g1a-presence.jelly) | Failed | Rejected export: dangling ActionOutput UUID; brace/core-node diagnostics. |
| [g1b-latest-value](g1b-latest-value.jelly) | Failed | Rejected export: dangling ActionOutput UUID; brace/core-node diagnostics. |
| [g1c-count-guards](g1c-count-guards.jelly) | Accepted | Basic structural pass with brace/core-node diagnostics. Control flow/types still need app inspection. |
| [g1d-file-assignment](g1d-file-assignment.jelly) | Accepted | Basic structural pass with brace/core-node diagnostics. Control flow/types still need app inspection. |
| [g2a-append-text](g2a-append-text.jelly) | Failed | Compiler rejected += candidate syntax. App support unknown; not an established app-profile mismatch. |
| [g2b-append-files](g2b-append-files.jelly) | Failed | Compiler rejected += candidate syntax. App support unknown; not an established app-profile mismatch. |
| [g2c-append-scores](g2c-append-scores.jelly) | Failed | Compiler rejected += candidate syntax. App support unknown; not an established app-profile mismatch. |
| [g3-exit-context](g3-exit-context.jelly) | Accepted | Basic structural pass; caller return semantics/native types not device-tested. |
| [g3-exit-echo](g3-exit-echo.jelly) | Accepted | Basic structural pass; caller return semantics/native types not device-tested. |
| [g3a-text-caller](g3a-text-caller.jelly) | Accepted | Basic structural pass; caller return semantics/native types not device-tested. |
| [g3b-file-caller](g3b-file-caller.jelly) | Accepted | Basic structural pass; caller return semantics/native types not device-tested. |
| [g3c-context-caller](g3c-context-caller.jelly) | Accepted | Basic structural pass with brace/core-node diagnostics. Control flow/types still need app inspection. |
| [g4a-default-direct](g4a-default-direct.jelly) | Accepted | Basic structural pass, BUT both Ask defaults omitted by local binding. Not a default-behaviour pass. |
| [g4b-default-interpolated](g4b-default-interpolated.jelly) | Accepted | Basic structural pass, BUT both Ask defaults omitted by local binding. Not a default-behaviour pass. |
| [g4c-default-controls](g4c-default-controls.jelly) | Accepted | Basic structural pass, BUT both Ask defaults omitted by local binding. Not a default-behaviour pass. |
| [g4d-date-name](g4d-date-name.jelly) | Failed | Rejected export: out-of-range interpolation attachment. |

## Important semantic inspection

The local exports for G4A, G4B and G4C each contain two Ask actions with no
`WFAskActionDefaultAnswer` field. Their local basic structural passes are NOT
successful default-generation tests. Even the literal Alpha control is omitted.
The pinned `Jelly_WFAskActionDefaultAnswer` maps an enum of input types rather
than resolving these candidate values. Inspect the iPad app's generated fields
independently; its bundled compiler is not established as this implementation.

G3 receivers contain native Exit actions followed by the deliberate failure
sentinels. Presence of Exit in a plist does not prove a caller receives its value.
G1D/G3C include emitted loop markers that still need app control-flow inspection.
No locally emitted `.shortcut` is signed or claimed import-ready.

The three += sources fail this pinned compiler. They follow the documented
variables syntax, but no successful app result is recorded. Preserve the failed
sources for comparison; do not silently replace += with native Add to Variable
and then count the repaired probe as generated success.

## Reproduce

From the repository root, pass these sixteen `g*.jelly` paths explicitly to
`python jelly/scripts/build.py`, ordered receivers before their callers for group 3.
The existing batch used filename order (G3 receivers sort before G3 callers).
The wrapper attempts every explicit source and reports an aggregate failure if
any fails. Do not use `--all`, which also compiles unrelated historical probes.

Reports/logs/artifacts are under `jelly/build/tests/ipad-investigation/`, using each
source stem with `.build.json`, `.stdout.log`, `.stderr.log`, and accepted unsigned
`.shortcut` or rejected artifact as applicable. The aggregate capture is
`jelly/build/generation-groups-build.log`. Build artifacts are ignored workspace
outputs; this tracked record summarises observed results without pretending to
embed or sign them. Detailed reports identify diagnostics and output hashes.

## Exact source hashes

These match the wrapper reports and byte-identical `.txt` copies at this build.

| Source stem | SHA-256 |
| --- | --- |
| g1a-presence | `9052558758e35e63d3928d3ae79bbe5fa0a2094da87c5c5169bcc87c1b86496c` |
| g1b-latest-value | `96cf85cd55ec5d320d6d60726a6918d4308e7df7ef9f89df47ee1eb44f67e282` |
| g1c-count-guards | `e712e60a6a725d8db5c92d90335067f864067caf3d5ad3297ac35fb8386a6c57` |
| g1d-file-assignment | `d199c41c7f344ab6786e1c22d9e676288116c802ac9be61b5914a3339a621400` |
| g2a-append-text | `d2dbb617a08ca1a59dce71f007ed3fc53832373d03f002d133fa92dacf1d43b2` |
| g2b-append-files | `30046d111c3e289817968af40f33b96c9198e83430b3ef02bd2022be89457b9d` |
| g2c-append-scores | `e111043ae7b5a4d9d9057a3ad2e78a265e3c79dfd16511e76b275b9bfa0d04fe` |
| g3-exit-context | `e9f2ff77e320690b58f9f13a6556bcd8ee5719a150f5136d97e58b77ef9930a6` |
| g3-exit-echo | `d32b68029185d69bba8568db5c51b39029cc1798c647f54145a2a30d4d0e02b0` |
| g3a-text-caller | `5b65df55d3d49d4aec3593f95988236e1f90963d5a01ac3ac2db8aaa4cf04f48` |
| g3b-file-caller | `e04ae99a39aef60e08398170b5eef433e3d4a4f1a383a8565fcd3ecdea8b77f3` |
| g3c-context-caller | `b3c356d808fae5aaf01aeb9ab919b4dfcd188f57647b40bb8f7e0b789e137df4` |
| g4a-default-direct | `58d78ca5bb4e87e8e05fd8f307236e870b8e9e1b2c082e543d927bc87aa2ed49` |
| g4b-default-interpolated | `4ec8e500f5851b77c18a53e9e4657e98eeb0e53fbbd353c74cd2e8d389477b4d` |
| g4c-default-controls | `c6bb7529757b6f32e83fac6837879afb6dcfaa9eb8ec70d4a958aa336c8add4d` |
| g4d-date-name | `b4bcdd329a7cc203bd61f79e35060ea253bdfd0051bf628864b515bcc96eeeb3` |

[Instructions and expected results](generation-groups.md).
