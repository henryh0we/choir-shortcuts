# iPad exchange format, schema versions 1 and 2

This is the normative JSON contract validated by `scripts/ipad_pipeline.py`.
New requests/results use version 2. Version 1 remains readable without rewriting
old requests, templates, results or receipts. Fields marked v2 are required only
in version 2; other listed fields are required in both versions. Unknown fields
and duplicate keys are rejected. A v2 result can report on a v1 request; a v1
result remains accepted with its installed name unknown. Receipts remain version 1.
JSON is UTF-8 (an input JSON BOM is accepted); NaN/Infinity are rejected. A JSON
manifest/result must be at most 2 MB. Source text is strict UTF-8, with optional
BOM; there is no source-size limit imposed by this tool.

Hashes are lowercase 64-character SHA-256 hex strings. IDs have the form
`YYYYMMDDTHHMMSSffffffZ-<32 UUID hex characters>`. UTC timestamps are ISO 8601
strings ending in `Z`. Booleans are JSON true/false, never 0/1 or strings.
`null` means unknown, never an inferred false or success.

## request.json

| Field | Type / constraint |
| --- | --- |
| schema_version | Integer `1` or `2`; newly prepared requests use `2` |
| build_id | Unique ID, matching its request folder |
| created_at_utc | UTC timestamp |
| status | Literal `prepared`, permanently unchanged |
| target | Literal `ipad-jellycuts` |
| requested_method | `editor`, `compile-jelly-text`, `compile-jelly-file` |
| shortcut_name (v2) | Explicit intended Apple Shortcuts display name, independent of filename/build ID |
| name_from_build_id (v2) | Earlier request ID whose intended name was reused, or null for a filename default/explicit override; provenance only, not a runtime dependency |
| source | Object defined below |
| local_validation | Object defined below |
| artifacts | Filename → SHA-256 object |

`source` contains exactly:

| Field | Meaning |
| --- | --- |
| filename | Original source basename |
| original_path | Absolute originating path, metadata only; not read during verification |
| sha256 | Hash of original submitted bytes |
| delivered_sha256 | Equal to sha256 in both versions |
| bytes | Positive integer byte count |
| encoding | `utf-8` or `utf-8-bom`, checked against bytes |
| transformation | Literal `none` |

`local_validation` contains `status`, `success`, `stage`. Without a report these
are `not-provided`, null, null. With `--local-report` they are `captured`, the
report's Boolean success, and its text stage. Both passing and failing reports
are accepted if `source_sha256` matches. This is captured local evidence, not
fresh compiler execution or proof of app compatibility.

`artifacts` has exactly `source.txt`, `source.jelly`, `feedback-template.json`,
and optionally `local-validation.json`. Both source files contain identical
original bytes. Every artifact hash is checked. The feedback template is a valid
not-attempted result with the request identity prefilled. The template timestamp
starts at request creation; replace it in a result copy with the actual report time.

Shortcut names must be nonempty printable Text without surrounding whitespace.
They are never injected into source or treated as Jelly metadata. Source filename
remains `source.filename`; it is not duplicated or changed when the display name
changes. Default naming/persistence is documented in [the guide](ipad-pipeline.md).
Legacy requests have no stored intended name: summaries show null, not a guessed
historical name. A name reference need not be present in a copied exchange because
the new immutable request contains the actual intended name itself.

No source-name/path field controls a filesystem destination. Bundle filenames
are fixed by this schema. No manifest contents are executed.

## Feedback result.json

Start with the generated `feedback-template.json`, copied outside the request.

| Field | Type / meaning |
| --- | --- |
| schema_version | Integer `1` or `2`; new templates and manual records use `2` |
| build_id | Exact matching request ID |
| source_sha256 | Exact request original hash |
| delivered_sha256 | Exact request delivered hash |
| reported_at_utc | Actual UTC observation/report timestamp |
| compilation_method | Actual method: editor / compile-jelly-text / compile-jelly-file; may differ from requested |
| status | One of the eight statuses below |
| evidence_source | `manual`, `device-reported`, `simulated` |
| compilation_attempted | Boolean |
| error_reported | Boolean or null; distinct from warning text |
| compiler_messages | Text; errors/warnings verbatim where available, empty if unavailable |
| shortcut_generated | Boolean or null |
| actions_inspected | Boolean |
| action_sequence_correct | Boolean or null; evaluates the inspected shortcut, including repairs if declared |
| manual_repairs_required | Boolean or null; true prevents treating repaired behavior as untouched generation |
| device_tested | Boolean |
| execution_outcome | `not-run`, `passed`, `failed`, `inconclusive` |
| developer_notes | Text: identities, previews, discrepancies, exact native edits and evidence references |
| device | Object with exactly text ipados_version, jellycuts_version, forscore_version; empty strings mean not recorded |
| installed_shortcut_name (v2) | Observed actual installed name, or null if not known; never copied from intended name |

A non-null installed name requires compilation_attempted=true and
shortcut_generated=true. It may differ from shortcut_name; the summary reports
`name_matches=false` without hiding an otherwise valid generation observation.
Record names before/after a manual rename as separate observations. Simulated
names do not populate actual installed-name summaries. Matching names alone say
nothing about generated actions or execution.

## Status semantics

| Status | Required evidence |
| --- | --- |
| not-attempted | compilation_attempted=false; no claims of generation/error/inspection/execution |
| compilation-attempted | Attempted; generation/error outcome unknown; no inspection/execution |
| compilation-failed | Attempted and error_reported=true; no device execution or claim of correct generated actions |
| output-unverified | Attempted, generated=true; no inspection/execution; no reported compiler error |
| actions-correct | Attempted, generated=true, actions_inspected=true, correct=true, error_reported=false; explicit repairs yes/no; not executed |
| device-passed | Same inspected correctness requirements, plus device_tested=true and execution_outcome=passed |
| device-failed | Attempted, generated=true, device_tested=true, execution_outcome=failed |
| inconclusive | Describe ambiguous/incomplete observations; may be attempted or not, but basic field constraints still apply |

An inspection requires a generated shortcut. Correctness and repairs assessments
require inspection. A device run requires generation. `device_tested` is true
exactly when execution_outcome is not `not-run`. Actual device execution requires
a device status or `inconclusive`. Compilation warnings do not automatically mean
`error_reported=true`; record their text and the observed severity separately.

No-error incomplete output is `inconclusive` with generated=true, inspected=true,
correct=false. It cannot be actions-correct or device-passed. For a repaired pass,
set manual_repairs_required=true and describe what changed. The summary labels it
`repaired`; it does not claim untouched source generation succeeded.

The `record` command derives facts implied by the chosen status, then applies
explicit flags and validates the combination. For example `device-passed` asserts
actual execution and inspected correct actions; never choose it for a transfer
test. Use evidence_source=simulated for simulations. Simulations are retained but
excluded from the summary's `ipad_status` and `validation_scope`.

## Accepted observation bundles

`results/<build-id>/result.json` is only an incoming slot, not accepted evidence.
`ingest` copies a validated result to a new immutable observation directory.
`record` writes directly to a new observation directory. No command edits an old
observation or the request. Incoming results are not automatically archived/deleted.

Each observation has canonical `result.json`, UTF-8 `diagnostics.txt` equal to
compiler_messages, and `receipt.json` with exactly:

| Field | Meaning |
| --- | --- |
| schema_version | Integer 1 |
| observation_id | Unique ID matching observation folder |
| build_id | Matching request ID |
| received_at_utc | Windows/Linux ingestion timestamp |
| origin | `record` or `ingest` |
| request_sha256 | Hash of request.json when accepted |
| result_sha256 | Hash of stored canonical result.json |
| diagnostics_sha256 | Hash of stored diagnostics.txt |

Verification checks request files, stored observation hashes/semantics, request
manifest stability after acceptance, incoming result consistency, orphan result
folders and interrupted publications. Original source need not still exist or
match: the immutable snapshot defines the build. These hashes are integrity
checks, not signatures or authentication. Filesystems/cloud clients do not enforce
immutability; the CLI refuses overwrites and detects inconsistent stored evidence.

History is ordered by locally generated observation ID (receipt order), not the
device timestamp. The latest received actual report sets `ipad_status`, not the
highest status ever reported. An older report imported later can therefore become
current; inspect full history/timestamps. It remains a reported status, not a
device result independently measured by this tooling.
