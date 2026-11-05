# Pipeline tests and physical-iPad integration plan

Windows transport/evidence code is tested independently of the iPad. Device
results below are **Not run**. No generated importable Shortcut or app output
is fabricated. Production sources and both G1A originals remain unchanged.

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

## Prepare a separate request per method and case

```powershell
$exchangeRoot = Join-Path $PWD 'jelly\build\ipad-exchange'
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/compiler/hello-world.jelly --method editor --exchange $exchangeRoot
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/pipeline/fixtures/minimal-variable.txt --allow-text-source --method editor --exchange $exchangeRoot
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
| M | Not run | Not run | Not run | Not run |
| G | Not run | Not run | Not run | Not run |
| C | Not run | Not run | Not run | Not run |
| I | Not run | Not run | Not run | Must not run |
| N | Not applicable | Not run | Not applicable | Guard only |

These are results for the newly prepared pipeline experiments, not an erasure of
the earlier successful and failed user reports in the existing compatibility record.
