# File-based iPad compilation pipeline

Phase 1 implements Windows/Linux request preparation, inspection, manual feedback,
JSON ingestion and integrity verification. It uses Python's standard library.
No network connection, compiler invocation, subscription, Mac, server or database
is needed. Jellycuts Bridge is excluded entirely.

The physical iPad compilation/interface tests are **Not run**. This tooling does
not automate the device. The [device instructions](ipad-pipeline-device.md) and
[integration plan](../tests/pipeline/README.md) define the next manual experiments.
Existing local compilation remains available and unchanged.

## First local request

From the repository root in PowerShell:

```powershell
$exchangeRoot = Join-Path $PWD 'jelly\build\ipad-exchange'
$prepared = python jelly/scripts/ipad_pipeline.py prepare jelly/tests/compiler/hello-world.jelly --exchange $exchangeRoot | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Request preparation failed' }
$buildId = $prepared.request.build_id
$prepared.ipad_instruction
python jelly/scripts/ipad_pipeline.py list --exchange $exchangeRoot
python jelly/scripts/ipad_pipeline.py status $buildId --exchange $exchangeRoot
python jelly/scripts/ipad_pipeline.py verify --exchange $exchangeRoot
```

Every successful command prints JSON. Errors go to stderr with exit 1; usage
errors use exit 2. `list` and `verify` report every discovered integrity error and
exit 1 if any is present. `status` includes full accepted observation history.
No directory is created by list/status/verify. Prepare creates the exchange root
and request directory. A missing/unavailable exchange fails clearly.

The default is `jelly/build/ipad-exchange`, already covered by `.gitignore`.
An ordinary local directory is sufficient for tests but is **not accessible on
the iPad merely because preparation succeeded**. Manually copy the complete
request folder to a device-accessible location for the first experiment.

Use `--exchange` on each subcommand or set a task-specific environment variable:

```powershell
$env:JELLY_EXCHANGE_ROOT = 'D:\Your Shared Folder\Jellycuts-Exchange'
python jelly/scripts/ipad_pipeline.py list
```

That path is illustrative. Choose a real Nextcloud/iCloud/other folder only after
confirming Windows-to-iPad and iPad-to-Windows synchronization. No account setup,
credentials or cloud transport are configured by this script. Paths with spaces,
Unicode, apostrophes and shell punctuation are passed as path arguments.

## Published files and lifecycle

```text
<exchange>/
  requests/<build-id>/
    request.json
    source.txt
    source.jelly
    feedback-template.json
    local-validation.json             Only with --local-report
  results/<build-id>/
    result.json                       Optional mutable incoming feedback slot
    observations/<observation-id>/
      receipt.json
      result.json                     Immutable accepted observation
      diagnostics.txt
```

The request manifest's status is permanently `prepared`. Transfer never becomes
a compile result. Each preparation creates a new UTC/UUID build ID, even for
identical source. Changing the original later does not change the snapshot.
Do not edit request folders. Submit a new request instead. Publication writes a
complete staging folder and renames it into place; failures can leave `.pending-*`
folders, which verification flags. Nothing automatically deletes or archives
evidence. Cloud clients may synchronize the files in a different order; wait for
the whole bundle and confirm hashes before using it.
Windows sharing/access-denied errors during rename receive up to four short
retries (0.75 seconds total waiting); persistent errors remain failures, not
ready requests. Other permission failures are reported immediately.

Source must be nonempty strict UTF-8, optionally with a UTF-8 BOM, without NUL
characters. Source bytes are never normalized: comments, BOM and line endings
are preserved in **both** snapshots. Both original and delivered SHA-256 are
recorded and equal. `source.jelly` is an editor-opening candidate; `source.txt`
is for explicit text extraction/preview. Neither is an exported Apple Shortcut.
The source's original absolute path is recorded for traceability, so exchange
folders contain source code and potentially private path information. Use a
trusted shared location; hashes detect inconsistency, not malicious authorship.

The original G1A `.txt` and `.jelly` have different comments. Both remain
unchanged. To submit the historical text variant deliberately:

```powershell
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/ipad-investigation/g1a-presence.txt --allow-text-source --exchange $exchangeRoot
```

## Record real observations manually

After an actual device attempt, use only the status justified by observation:

```powershell
# A generated shortcut has appeared; its actions have not been inspected.
python jelly/scripts/ipad_pipeline.py record $buildId --exchange $exchangeRoot --status output-unverified --method compile-jelly-text --notes 'Generated output appeared; actions not yet inspected'

# No compiler error, but action inspection reveals incomplete generation.
python jelly/scripts/ipad_pipeline.py record $buildId --exchange $exchangeRoot --status inconclusive --method compile-jelly-text --generated yes --error-reported no --actions-inspected --actions-correct no --repairs-required yes --notes 'Only Set Variable; Nothing and Quick Look absent'

# Compiler error text, typed directly or imported from a UTF-8 file.
python jelly/scripts/ipad_pipeline.py record $buildId --exchange $exchangeRoot --status compilation-failed --error-text 'Paste the actual error here'
python jelly/scripts/ipad_pipeline.py record $buildId --exchange $exchangeRoot --status compilation-failed --diagnostics-file 'C:\path to\actual diagnostics.txt'

# Use only after correct action inspection and actual execution.
python jelly/scripts/ipad_pipeline.py record $buildId --exchange $exchangeRoot --status device-passed --repairs-required no --ipados-version '<observed>' --jellycuts-version '<observed>' --notes 'Record actual previews and inputs'
```

These examples are alternative observations, **not results already obtained**.
Each record appends a new observation. Previous evidence is never overwritten.
If a repaired shortcut passed, use `--repairs-required yes`; the summary labels
the validation scope `repaired`. It does not validate untouched source generation.

`actions-correct` and `device-passed` imply an attempted compilation, generated
shortcut, inspected correct actions and no reported compiler error. They also
require an explicit repairs assessment. `device-failed` implies actual execution
failed, without inventing whether action inspection happened. Other record flags
allow explicit true/false/unknown observations. `--help` lists them.

Use `--evidence simulated` only for a transport test. Simulated records remain
visible in history but **never advance `ipad_status` or its validation scope**.
The latest observation and latest actual reported device evidence are separate.
The program validates consistency; it cannot independently authenticate a human
or device report.

## Ingest feedback returned as JSON

Copy `feedback-template.json` to a writable result location, update all observations
and its UTC report timestamp, and keep the build ID/hashes unchanged. Do not edit
the template inside the immutable request. The [format contract](ipad-pipeline-format.md)
defines every field. JSON booleans/null must be actual JSON types, not strings.

```powershell
python jelly/scripts/ipad_pipeline.py ingest $buildId 'C:\Returned Files\result.json' --exchange $exchangeRoot
# Or, after a result has arrived at <exchange>/results/<build-id>/result.json:
python jelly/scripts/ipad_pipeline.py ingest $buildId --exchange $exchangeRoot
python jelly/scripts/ipad_pipeline.py status $buildId --exchange $exchangeRoot
python jelly/scripts/ipad_pipeline.py verify --exchange $exchangeRoot
```

Missing/malformed/mismatched feedback is rejected before publication. Ingestion
canonicalizes JSON and stores `compiler_messages` verbatim as UTF-8 diagnostics.
External file paths are not embedded as executable instructions or followed from
JSON. Incoming files are not automatically trusted, consumed, moved or deleted.
Until explicit ingestion, they never change the accepted iPad status. An already
accepted identical incoming result is labelled `already-ingested`. Re-ingestion
creates another receipt, preserving the previous evidence.

## Optional existing local compiler evidence

```powershell
python jelly/scripts/build.py jelly/tests/compiler/hello-world.jelly
# A local failure is not a reason to block submission to the authoritative app.
python jelly/scripts/ipad_pipeline.py prepare jelly/tests/compiler/hello-world.jelly --local-report jelly/build/tests/compiler/hello-world.build.json --exchange $exchangeRoot
```

`--local-report` copies an existing matching report into the immutable request.
The report's source hash must match exactly; `success: false` is accepted and
kept separate from iPad evidence. The pipeline does not invoke or modify the
compiler, its exports or its wrapper. Reports retain their diagnostics and
profile information. A stale/mismatched report can be omitted so submission still
proceeds; never relabel it as a passing check. Optional local source normalization
belongs to the existing compiler wrapper, not to the delivered iPad snapshot.

## Codex loop

1. Read the source and compatibility record, then make the requested source edit.
2. Run the existing local wrapper as required by AGENTS.md; retain mismatches.
3. Prepare a request, optionally attaching that exact-source local report.
4. Report the build ID, delivered hash and Files location. Wait for actual device
   action; do not infer completion from folders, file sync or no error message.
5. Record or ingest genuine feedback. Inspect warnings, action wiring, repairs
   and runtime separately. Use status and verify to check consistency.
6. Make a targeted source correction and prepare a new build. Keep earlier evidence.

## Automated tests

```powershell
python -B -m unittest discover -s jelly/tests/pipeline -v
```

Tests use temporary local directories, exercise real CLI parsing and a subprocess,
and require neither WSL nor Nextcloud nor an iPad. They include simulated feedback
explicitly labelled as such. See the integration plan for device acceptance.

## Deferred automation

Automatic diagnostic capture/export depends on the compilation action's measured
return contract. A one-tap queue needs a reliable compiler path and file-provider
behavior. HTTP transport and polling are not implemented; they would not solve
compiler generation defects. No unattended/background execution guarantee is made.
Copy/paste plus manual Windows recording remains the complete fallback when the
app cannot return output. Existing native forScore completion requirements remain;
transport does not eliminate them or round-trip repairs. Work on source generation
through the existing isolated probes rather than recreating working production
shortcuts on each trial.
