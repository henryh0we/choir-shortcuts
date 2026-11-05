# Pipeline tests and physical-iPad integration plan

Windows transport/evidence code is tested independently of the iPad. Device
evidence now includes a reported expected minimal-variable action sequence after
local folder copying; exact build linkage remains unconfirmed. Reports are recorded
separately from hash-linked feedback. No generated Shortcut or app output is fabricated.
Production sources and both G1A originals remain unchanged.

## Automated acceptance suite

From the repository root:

```powershell
python -B -m unittest discover -s jelly/tests/pipeline -v
```

The suite uses temporary directories, actual filesystem operations, real CLI
argument parsing and a subprocess. It checks byte-exact BOM/CRLF/Unicode source,
unique revisions, request/observation preservation, source and result hashes,
manual and incoming feedback, every evidence status, simulated-status isolation,
malformed JSON, Boolean types, incomplete generation, unavailable paths,
permissions, corruption, orphan/pending publications and path traversal.
The symlink escape test skips when the host denies symlink creation. No mock
compiler is used: these tests do not claim compilation at all. One mocked
PermissionError tests the error path without changing filesystem permissions.
Additional injected Windows sharing violations test bounded rename retries and
visible failure after retries are exhausted.

Recorded 5 November 2026: **Windows: 28 passed, 1 skipped** (symlink creation
not permitted); **WSL Ubuntu: 29 passed, none skipped**. A separate nine-command
subprocess smoke exercise prepared existing source, captured its matching stored
local report, listed/inspected builds, ingested and manually recorded explicitly
simulated observations, rejected mismatched/malformed feedback and verified the
exchange. Simulations left actual iPad status not-attempted. Its local transcript
is ignored under `jelly/build/pipeline-smoke/`; no device was contacted. Two clean
pending requests (Hello and minimal variables) were also prepared in the default
ignored exchange and verified without recording any device result.

## User-reported compilation observations, 5 November 2026

**Latest editor follow-up:** the user copied the same G1A source into Jellycuts,
compiled and built, and reports the exact same Calculate-box defect. They state
a screenshot would look identical; no additional screenshot was supplied. This
G1A generation failure is not specific to the compilation action. Earlier minimal
success does not establish full G1A support through either route. Next isolate
the header in the separate candidate described below; keep original failed outputs.

**Latest G1A result: malformed generation, not a pass.** After using the supplied
prepare command for the original g1a-presence.jelly and compiling with Compile
Jelly Text, the user supplied a screenshot showing the initial header Comments,
then a division/calculation action containing `Dependencies: None. Exact installed
targets must match source; export filenames do not set installed names.`, then
Stop this shortcut, then further header Comments. The original G1A has a single
line comment for Dependencies and no such calculation or unconditional stop.
The screenshot alone does not show all remaining actions or establish the cause.

Windows found one matching G1A request in the configured shared exchange:
`20261105T232511572676Z-a8d9428214e646b8a8cb603b6c1f83a6`, original/delivered hash
`9052558758e35e63d3928d3ae79bbe5fa0a2094da87c5c5169bcc87c1b86496c`, requested
method compile-jelly-text. This matches the supplied command/source and visible
original header; the consumed iPad bytes/hash were not independently observed.
Keep compiler errors/warnings, native repair requirements and runtime unknown
unless supplied. Classify as inconclusive with generated=true, inspected=true,
correct=false, not a successful validation. The proposed same-source editor
comparison has now been attempted and also failed by user report.
The pipeline appended manual observation
`20261105T233233864343Z-aa086373a56a40258bcf776675e6e891` to this shared request:
status inconclusive, generated=true, inspected=true, correct=false. Compiler
error reporting, repairs and installed name remain null/unknown; device_tested=false
means no generated-shortcut execution has been established. The receipt/source
hashes identify the request evidence, not independently measured iPad input bytes.

Earlier minimal-variable result: after copying the folder locally, the user ran the helper for
TEST - Pipeline Minimal Variable and reports the following generated actions:

```text
Nothing
Set variable currentValue to emptyValue
Show currentValue in Quick Look
```

The sequence matches M's expected generation. It supersedes the earlier
"local compilation untested" note for this narrow reported case. Exact build ID,
source hash/hash-check result, device versions, any native repairs and execution
of the generated shortcut were not supplied. The user subsequently confirmed the
correct variable token, so token correctness is no longer pending for that report. Local picker
versus Share Sheet launch was not specified. Do not infer a OneDrive fix or a
device-passed result, and do not attach this report to an assumed build ID.
Nothing remains intentionally empty in this fixture; an empty runtime preview
alone is not a generation failure. This success is limited to that small fixture
and does not supersede the subsequent G1A failure.

Transport follow-up: the user reports that all exchanged files appear as expected
in the iPad Files app. Windows inspection also finds the version-2 named minimal
request in the shared OneDrive exchange alongside the older version-1 Hello World
request. This is reported visibility, not confirmation of File-byte hashing,
compilation or iPad-to-Windows feedback. The [existing-helper upgrade guide](../../docs/ipad-pipeline-device.md#upgrade-test--jellycuts-compiler-step-by-step)
now walks through upgrading TEST -Jellycuts Compiler; that upgraded wiring has
not yet been device-tested.
The user's requested interaction is now **one Select Folder** for the long-ID
build folder, followed by automatic Get File from Folder retrieval of request.json
and source.txt. Add a device check that both files come from the selected OneDrive
folder without a second chooser; the provider/action behavior is not yet confirmed.
Follow-up: the user reports OneDrive and Jellycuts Exchange greyed out in the
shortcut's browser while usable in Files. Folder selection is blocked; the exact
cause is unresolved. The proposed next isolation test copies one complete request
folder to On My iPad and retries the same helper there. Local-folder selection,
hashing and compilation from that copy remain untested.
The next requested alternative is **Files → Share the build folder → TEST
-Jellycuts Compiler**, with Show in Share Sheet enabled and Folder input replacing
Select Folder. Native Folder delivery/child access are unverified; a OneDrive link
or archive is not a usable Folder. Inspect uncertain input with a separate View
Content Graph diagnostic before any compilation. A folder received via Share Sheet
must still pass manifest/source-hash checks. This is not yet a successful workaround.
The user subsequently reported folder Share unavailable/greyed out too. The local
copy/generation report above is the latest evidence; it does not establish which
local launch method worked.

Naming-enhancement checks: **Windows 33 passed, 1 symlink skip; WSL Ubuntu
34 passed**. These add filename defaults, overrides, same-path persistence,
renamed-source name reuse, actual-name mismatches, simulated-name isolation and
version-1 request/result/receipt compatibility. The original default exchange
verified successfully without modifying its eight existing request files. A new
version-2 minimal-variable request was prepared with intended name
`TEST - Pipeline Minimal Variable` for Compile Jelly Text; its device status is
still not-attempted.

These are separate attempts, not a single reliability pass. Build ID, exact source
hash, device versions, timing and screenshots were not supplied, so no immutable
request/result bundle has been attributed to either report.

| Observation | Reported evidence | Limits |
| --- | --- | --- |
| First Hello World attempt, Compile Jelly Text | Initial hang. | No confirmed completion/error, duration, recovery or generated output; inconclusive, not a compiler rejection. |
| Second Hello World attempt, Compile Jelly Text | Retry produced the expected Hello World shortcut. The installed name was `source`; the user configured the compilation action's naming input from the File name. | Supports this reported generation and configurable naming input. Exact build/source/action wiring and runtime were not captured; reliability still needs repeated tests. It does not prove the compiler inherently names all shortcuts from their source files. |

Change that helper's name input to request.shortcut_name, then record the actual
installed name. Do not silently rename existing installed dependencies. Once the
actual build ID/hash is confirmed, append separate inconclusive and generation
observations using record/ingest; retain unknown fields and do not infer execution.

## Exact integration inputs

All hashes are of current raw bytes, including final LF. The `.txt` fixtures
preserve the exact small reproductions without injected metadata comments.
Their intended installed names/contracts are specified here, not added to the
source under test. Submit these deliberately with `--allow-text-source`.

| Case | Exact input relative to jelly/ | SHA-256 |
| --- | --- | --- |
| H: Hello World | tests/compiler/hello-world.jelly | `047a8e5c1be1b02ce24af98730ef307988f683c945ee68dcb8498faa620e4b42` |
| M: minimal variables | tests/pipeline/fixtures/minimal-variable.txt | `02e6099570c2aa5af935e95c4055b9b5e7ddfa72875a1a4cfb150cb0793a3cd2` |
| G: original G1A Jelly | tests/ipad-investigation/g1a-presence.jelly | `9052558758e35e63d3928d3ae79bbe5fa0a2094da87c5c5169bcc87c1b86496c` |
| C: changed-header G1A Text | tests/ipad-investigation/g1a-presence.txt | `d5ba9a4ed11b56636d1169c8b397815942e846971a519699eb1f9ad3e9684a83` |
| I: intentionally invalid | tests/pipeline/fixtures/invalid-syntax.txt | `876d8a940530266109f873be12704bcb972ad5dea9ebdb857862e7e4a889e2a3` |

Expected delivered hash equals the input hash; no transformation is performed.
Stop and review if a request reports another hash. Future deliberate source
revisions require new expected hashes/build IDs; do not update these merely to
hide an unexpected change. Git core.autocrlf can change checkout bytes in another
checkout; diagnose that explicitly rather than silently comparing normalized text.

Minimal variable input M is exactly:

```jelly
import Shortcuts
nothing() >> emptyValue
var currentValue = emptyValue
quicklook(input: currentValue)
```

Its intended installed diagnostic name is **TEST - Pipeline Minimal Variable**.
Input: none consumed. Output: Quick Look of the current empty named variable;
there is no explicit return. No file/metadata writes or dependencies. The generation
assertion is Nothing → Set Variable → Quick Look, with correct references. An empty
preview or UI-specific preview failure must be recorded separately from generation.
Do not infer a successful runtime from the absence of a visible preview.

Invalid input I is exactly:

```text
import Shortcuts
text(text: "unterminated)
```

This is an intentionally invalid text submission, not an installable diagnostic.
Do not run any output it produces. Its purpose is measuring compiler rejection
and error visibility, including whether following actions still execute.

H has its existing source header/contract. G and C retain their original source
contracts and known local failure. C differs only in comments, including the
joined Result/Dependencies line. Neither variant is declared universally valid
for the app by this plan.

## Header isolation after both paths failed

New independent candidate: `tests/pipeline/fixtures/g1a-presence-no-header.txt`.
It removes exactly the eight leading // header-comment lines from the original
g1a-presence.jelly. An automated test checks that **every noncomment byte remains
identical**, including all executable statements, blank lines and If bodies.
Neither G1A original is modified. This is an intentional experimental source
variant, not a silent pipeline normalization or a proven production fix.

Candidate bytes: 533. SHA-256:
`109806e133539328882b27899d7fda5207cd2254dcb4d2f0491b968cfc0fbe3d`.

Intended installed diagnostic name: **TEST - G1A Presence No Header**. Input: none
consumed. Dependencies: none. Side effects: previews only. No explicit return.
Target: current iPad/Jellycuts versions must be recorded. Expected generation:
Nothing, currentValue assignment, four If blocks with their Text/Quick Look pairs,
and Alpha assignment. No header Comment, Calculate/Divide or unconditional Stop.
Expected runtime remains G1A EMPTY ABSENT then G1A FILLED PRESENT, without FAIL.
Native token connections and condition polarity must be inspected before execution.

First duplicate the editor test project and delete only its eight leading //
comment lines, so the first line is import Shortcuts; equivalently paste the exact
new candidate file. Compile/build through the editor with no other edits, under
the distinct test name, and inspect before repairs or runtime. A successful
header-free variant implicates header processing for this input, but does not
identify a particular comment/word or prove comments are universally broken.
If it also fails, header removal is insufficient. Preserve both observations.
After recording that editor result, compare the same candidate via Compile Jelly
Text. Current candidate device result: **Not run**.

To prepare a reproducible candidate request rather than editing an immutable build:

```powershell
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/pipeline/fixtures/g1a-presence-no-header.txt --allow-text-source --shortcut-name 'TEST - G1A Presence No Header' --method editor --exchange $exchangeRoot
```

The candidate is already a deliberate source variant; the pipeline still delivers
its submitted bytes unchanged. Do not delete comments from stored request files.
The Windows suite now passes 34 tests with one symlink skip; the additional test
establishes this candidate's noncomment-byte identity, not app compilation.

## Prepare a separate request per method and case

```powershell
$exchangeRoot = Join-Path $PWD 'jelly\build\ipad-exchange'
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/compiler/hello-world.jelly --shortcut-name 'TEST - Local Compiler Hello' --method editor --exchange $exchangeRoot
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/pipeline/fixtures/minimal-variable.txt --allow-text-source --shortcut-name 'TEST - Pipeline Minimal Variable' --method editor --exchange $exchangeRoot
# Repeat with --method compile-jelly-text, then --method compile-jelly-file.
# G uses .jelly normally; C and I require --allow-text-source.
```

For H/M/G/C, the source.txt and source.jelly aliases must match the same expected
hash. Do not compile one from the live repository and another from a stale Files
copy. Select/preview the published snapshot every time. Use [the device helper
instructions](../../docs/ipad-pipeline-device.md), including the anti-filename guard.

## Evidence and acceptance matrix

| Case | Paths | Expected generation / acceptance | Required evidence |
| --- | --- | --- | --- |
| H | Editor, Text action, File action, independently | Text "Hello from local Jellycore!" → Quick Look connected to that Text, plus source comments if generated. Actual run displays that literal. | Hash, full input preview, versions, compiler warnings, actions/connections, actual preview. |
| M | All three paths | Nothing named emptyValue → Set Variable currentValue from it → Quick Look of currentValue. Missing Nothing/Quick Look or dangling references fail generation even with no error. | Same source hash in every path, source/input type, three actions and their tokens, returned-output availability/type and any Quick Look behavior. |
| G | Editor first, then each action if safe | Four Ifs with absent/present polarity and current named variable. Runtime exactly G1A EMPTY ABSENT then G1A FILLED PRESENT, no FAIL marker. | All conditions/connections and actual preview order; classify any malformed output separately from runtime. |
| C | Same paths as G | Same executable intent as G. Compare header generation and malformed actions independently; no assertion that comments cannot affect this compiler. | Distinct C hash, complete header preview, any Calculate/Divide/Stop anomalies, and untouched generated sequence. |
| I | Each path independently | Compiler rejects input; exact diagnostics captured if exposed. No output, no messages or an abort are distinct observations. Any apparent success is inconclusive, never a pass. | Visible error, warning text, whether action aborts, availability of output and subsequent actions. Do not execute generated output. |
| N: filename guard | Text helper, before Jellycuts | Deliberately feed literal source.txt instead of source contents into sourceText in a duplicate helper. The import/contents guard stops before compilation. Then restore the sourceFile → Get Text connection and preview the real source. | Photograph/record actual Quick Look, guard stop and restored connection. No compile claim for the rejected input. |

Input hashes for N are the selected H/M/G/C request's hash. Its deliberately wrong
literal is never a valid delivered source and must not be recorded as that source
having compiled. Put this wiring failure in developer_notes/inconclusive evidence.

For each valid generated shortcut also inspect the actual installed name. It
should match request.shortcut_name after the naming-field connection or a recorded
manual Rename. Record installed_shortcut_name separately from action correctness.
Test distinct filenames and explicit overrides without modifying source bytes.

## Record each result

Use the request's generated feedback template outside requests, or Windows
`record`. Include actual method, device versions, the exact warnings/error text,
generated/inspected/correct fields, every native repair, tested input and observed
runtime. Preserve untouched malformed outputs. A repaired pass remains separate.

For no-error incomplete M output:

```powershell
python jelly/scripts/ipad_pipeline.py record $buildId --exchange $exchangeRoot --status inconclusive --method compile-jelly-text --generated yes --actions-inspected --actions-correct no --repairs-required yes --error-reported no --notes 'Only Set Variable; missing Nothing and Quick Look'
```

Use `actions-correct --repairs-required no` only after all generation checks pass;
use device-passed only after actual runtime checks too. Returned raw compiler
objects/errors are observations, not automatically trusted result-schema entries.

## Sync and repeat-revision acceptance

1. Publish H, confirm exact bytes on the iPad and return a note from its results
   folder. Confirm that note arrives on Windows intact. Windows verify must pass.
2. In a disposable copy of H (not the original fixture), change the greeting,
   prepare a second build, and inspect the new greeting before compilation.
   Original request/hash/observations must remain intact. Test both directions of
   sync before selecting Nextcloud as the normal exchange root.
3. If sync is unavailable, copy the complete request folder and returned note
   manually. A successful local prepare alone is only Windows transport evidence.

## Device results

| Case | Editor | Compile Jelly Text | Compile Jelly File | Runtime |
| --- | --- | --- | --- | --- |
| H | Not run | Not run | Not run | Not run |
| M | Not run in this loop | Expected three-action sequence reported via compiler helper after local copy; build/hash and exact path unconfirmed | No separate result | Not reported |
| G | Same Calculate-box defect reported after copying identical code; no second screenshot | Malformed generation shown: Dependencies division plus unexpected Stop; request association noted above | No separate result | Not reported; preserve malformed output |
| C | Not run | Not run | Not run | Not run |
| I | Not run | Not run | Not run | Must not run |
| N | Not applicable | Not run | Not applicable | Guard only |

These are build-linked results for the newly prepared pipeline experiments, not
an erasure of the unlinked Hello World reports above or the earlier successful
and failed user reports in the existing compatibility record.
