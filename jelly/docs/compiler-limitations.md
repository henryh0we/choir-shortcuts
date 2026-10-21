# Local compiler limits and signing

The selected compiler is [official Open-Jellycore](https://github.com/OpenJelly/Open-Jellycore)
at `e1ec31c2ee192c8721749f9eb3b50108e38891cf` (16 May 2024).
Inspection on 21 October 2026 found the same upstream HEAD. The GitHub fork list
contained 15 entries; the two with newest push dates, Kris9403 and electrikmilk,
also had this exact default-branch HEAD. A newer push timestamp is not a compiler
update. No better maintained Jelly-compatible replacement was established.
[Cherri](https://cherrilang.org/getting-started.html) is an alternative Shortcuts
language, not a drop-in compiler for existing `.jelly` sources; migration would
require rewriting and separate validation. Keep the official pinned compiler here.

The upstream README advertises imports, comments, calls, conditions, repeats,
menus, magic variables, functions/macros and plist export. It lists Objects as
unsupported and does not offer full error handling. That feature table is an
upstream claim, not a record of all features passing local tests. Confirm unfamiliar
forms in the pinned grammar, bindings and actual exports.

This 2024 compiler is **not a confirmed match** for the user's Jellycuts 2026.6.4
app. Existing app evidence for flush-left bodies, positional output and line
comments must remain intact. A CLI error is not permission to rewrite a device-
verified form. See [the reference](jellycuts-reference.md) and
[device evidence](../tests/compatibility/README.md). forScore native actions and
existing assembly slots still require device work.

The CLI source hardcodes the compilation name `Function Tests`; an export basename
does not ensure an installed name. Function self-dispatch deserves particular
inspection. Its reported compiler errors can return exit status zero. Export is
UTF-8 property-list text and does not sign or execute the Shortcut. Parser success
alone does not establish action wiring, complete source consumption, device
compatibility or correct runtime behaviour.

## Defects reproduced locally

- CRLF source produces corrupted token offsets and misleading function names.
  The wrapper compiles an LF-normalized temporary copy without changing source.
- Text interpolation can produce an attachment indexed by its source-file offset
  instead of an offset within the exported string. A one-character text value
  had `{720, 1}`. The wrapper rejects such exports. The smoke test uses a native
  Quick Look variable binding as a supported alternative; this does not solve
  arbitrary interpolated text throughout the production sources.
- A teaching main produced a dangling ActionOutput UUID despite CLI success;
  the wrapper rejects references to absent action UUIDs.
- Current app positional Output calls, enum forms and several control-flow
  constructs fail this local compiler profile. See the
  [per-file audit](../tests/compiler/README.md). Do not rewrite device-tested
  sources merely to suppress these mismatches.

The [isolated positional Output comparison](../tests/compatibility/output-signature-comparison.md)
now has user-reported iPad confirmation: `output("...")` compiles with two
missing-setting warnings and generates the correct literal Stop and Output Text,
with no-recipient behaviour Do Nothing. Local CLI rejection of this exact form is
a confirmed profile incompatibility; it does not invalidate that app compilation.
Runtime return behaviour remains untested. Preserve the source form and record
the mismatch without suppressing the local failure or guessing replacement arguments.

Only 3 of 20 audited sources passed compilation plus the wrapper's structural
checks. Five compiled but had rejected exports; twelve reported compiler errors.
The installed compiler supports local iteration on its accepted subset. It cannot
currently replace validation of all existing project sources in the iPad app.

## Signing options

1. Apple's supported command is macOS `shortcuts sign`. Example, for a future Mac:

   ```sh
   shortcuts sign --mode anyone --input unsigned.shortcut --output signed.shortcut
   ```

   [Apple's command-line guide](https://support.apple.com/en-ng/guide/shortcuts-mac/-apd455c82f02/mac)
   documents signing modes and says Apple receives a copy for validation. No
   supported equivalent Windows/Linux command or public signing API was established.
2. A trusted Mac could eventually sign exports through an explicitly configured
   remote job. This is the preferred future automation if one becomes available;
   a Mac is not required for local compilation.
3. [shortcut-sign](https://github.com/0xilis/shortcut-sign) is an open-source
   Linux/macOS implementation. Its README requires private signing keys/auth data
   and describes device key extraction; it is not Apple's supported workflow and
   has not been installed or tested here. It is not recommended for this setup.
4. Cherri documents third-party HubSign/custom signing servers in its
   [signing guide](https://cherrilang.org/compiler/signing.html). This establishes
   an available approach, not verified reliability, privacy or compatibility with
   these exports. Do not upload sources or exports without explicit user permission.
5. The existing Jellycuts app remains the user's available export/import route;
   inspect its current workflow on the device. Local unsigned exports have not
   been imported through it in this setup.

Current Apple-platform sharing/import workflows require signed files; raw local
plist exports should not be described as import-ready. This is supported by the
Cherri signing documentation; direct import on the user's iPadOS build has not
been tested. No signing requests or third-party uploads are performed by this
workspace's build tools. Compilation, structural validation, signing, import and
actual iPhone/iPad execution are separate evidence stages.
