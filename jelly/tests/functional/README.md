# Small functional test drivers

Four independent test Shortcuts; no production source changes. Each has a .jelly source and identical .txt copy for pasting into Jellycuts. Flush-left parenthesized If and positional Output follow the user-confirmed fixture; missing noResultBehaviour/response warnings may remain. These new drivers are Drafted, not compiled or run. Confirm installed names and inspect generated If inputs/output bodies. Do not infer successful tests from compilation alone.

| Installed name | Source | Input | Dependencies |
| --- | --- | --- | --- |
| TEST - Canonical Names | [test-canonical-names.jelly](test-canonical-names.jelly) | None | Naming 2.0 |
| TEST - Archive Reuse | [test-archive-reuse.jelly](test-archive-reuse.jelly) | Existing PDF/Library/config native context List | Archive 2.1 |
| TEST - Archive Config Error | [test-archive-config-error.jelly](test-archive-config-error.jelly) | Same context List, with invalid disposable config | Archive 2.1 |
| TEST - Choir Service | [test-choir-service.jelly](test-choir-service.jelly) | None | Completed Assembly 1.1 and dependencies |

## Minimal setup

Preserve the installed helpers with your native fixes. Import each test as its own new Shortcut; none replaces a helper. The canonical test's Lists contain literal fixture strings intentionally: they must be text, not variable names. All Run Shortcut inputs and results must be actual variable tokens. In Archive Reuse inspect the final name comparison: its right operand must reference secondName, not literal interpolation text. Get Type's Text result assumes your English action profile. A mismatched app signature or missing action is a test-driver failure to diagnose, not proof the helper is wrong.

For archive tests, duplicate your existing working manual archive test caller. Keep its PDF picker, folder selection, config picker/Get Dictionary from Input, and three-row native List unchanged. Change its Run Shortcut target to TEST - Archive Reuse or TEST - Archive Config Error; keep passing the List and showing the returned result. This avoids another generated native-object List. Do not run those two drivers directly without their context input. Use a disposable Library named Library with Responses/category folders matching your valid test config. No standalone Folder action is required.

## Checks and expected results

| Case | Steps | Expected | Actual |
| --- | --- | --- | --- |
| Canonical | Run TEST - Canonical Names directly | Expected transformations for two filenames and a custom prefix; then missing second argument returns no useful value. A validation alert may need dismissal. Final PASS appears only after all four checks. | Not run |
| Archive reuse | In caller select a disposable PDF, test Library and valid config; run TEST - Archive Reuse | Two archive calls return non-Text values with equal names. First call may offer category; second must not. Inspect Files: no extra numbered copy. Matching names alone are not identity/count verification. | Not run |
| Missing rule | Caller uses config-missing-prefix.json | Exact ERROR: Set prefixRegex in config.json. No save/category prompt. Inspect test Library. | Not run |
| Missing category | Caller uses config-missing-category.json, whose TEST-MISSING-CATEGORY folder must NOT exist | Use a new PDF absent from every test category, otherwise reuse bypasses this test. Choose TEST-MISSING-CATEGORY. Exact missing-folder ERROR; no save. Existing same-name archive would make this fixture invalid. | Not run |
| Service branches | Point Assembly CONF root to disposable Choir Music/config/Library; complete existing slots, then run TEST - Choir Service with one existing and one absent forScore score | Inspect reuse/import, metadata and requested order. Use Create new with an unused test name. Run again with Replace existing and select that same disposable setlist; order/count correct and underlying scores retained. Report is evidence to inspect, not an automatic PASS. | Not run |

Both invalid config fixtures are supplied here; copy them to a test location and select them with your existing config picker. They are not changes to your production config.json. The config-error driver accepts only the two exact expected errors; confirm its returned message matches the particular fixture you selected. Native action errors/cancellation can stop a run without a diagnostic. No driver deletes test artifacts or automatically cleans up duplicate PDFs. Keep assembly's other settings/native fixes; restore the normal root after your disposable service test if needed.

References: local List, Run Shortcut, Get Type, File Details and Match Text documentation; installed-app If/Output observations in ../compatibility/README.md. These tests exercise the installed helpers rather than duplicate their implementations.
