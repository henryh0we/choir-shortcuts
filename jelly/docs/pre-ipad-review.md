# forScore source review before iPad transfer

21 October 2026. Current sources: **Canonical 10 / Archive 14 / Assembly 12 /
Main 4**. Interfaces remain **2.0 / 2.1 / 1.1 / 1.0**, respectively. This review
supersedes older current-version/Exit-return instructions in the linked guides;
historical observations remain evidence for those older revisions.

## Fixes applied

| Source | Problem found | Change |
| --- | --- | --- |
| Canonical 10 | Still used indented If bodies and `exit(var: ...)`, despite recorded app failures of those forms | Flush-left bodies and positional Output; invalid input returns empty Text, success returns canonicalName Text. NAME01/NAME02 and manual receiving/output-token inspection remain required |
| Main 4 | Still used the old result/noResultBehavior/response Output signature | Uses positional Text Output, matching the user's isolated iPad probe. No-recipient behaviour is Do Nothing; direct display is not guaranteed |
| Assembly 12 | Collection slots could leave an incomplete order/preview or preparation list without preventing setlist writes | Checks orderedFiles/orderedNames counts before file writes, workingScore presence before metadata, and preparedScores count after the complete preparation loop and before any setlist creation/clearing/appending |
| Assembly 12 | Empty metadata/mode/target choices were not explicitly handled | Adds empty-result checks before using those choices; messages accurately acknowledge any earlier preparation or creation of an empty setlist |
| Assembly 12 | Readback count mismatch still flowed into the usual completion report | Returns a specific partial-write error on mismatch; equal counts still do not prove identity/order |
| Assembly header/inventory | Claimed Canonical required interface 2.1 | Corrected Canonical 2.0 versus Archive 2.1 |

The unchanged Archive 14 retains the user's reported manual save/reuse repair.
Do not regenerate/replace the working installed archive just for these changes.
Preserve it and confirm its native List input and File-success/Text-error contract
match the assembly caller. The source skeleton still cannot preserve the user's
installed native edits automatically.

The positional Output evidence establishes compilation and generated literal Text
for the isolated probe, not execution, interpolation or arbitrary native File
returns. The canonical/main dynamic Text outputs still require inspection on the
iPad; this review does not claim the full regenerated sources compile there.

## Native work still required by the current source workflow

- Keep the assembly's initial unconditional guard until CONF01-CONF02,
  COL01-COL03, SCORE01-SCORE02 and FS01-FS13 are complete. Archive CFG03/CFG04
  must return native File tokens, not the empty placeholders or file-path Text.
- In both naming-input Lists and archiveInput, inspect actual variable tokens.
  The user's archive previously passed literal variable names until repaired.
- Reconnect every consumer of replaced Nothing slots. New workingScore and
  targetSetlist checks must use the current named variable/actual choice output.
  Count actions must read the populated named collections, not empty initializers.
- COL01 now appends the current named orderedFile after it is assigned from
  chosenOrderedFile. This follows the existing named-variable workaround for
  conditions inside Repeat; inspect both the assignment and presence check.
- Preserve the user's existingCleanFile post-loop **has any value** repair;
  it fixed archive reuse. New exports do not prove that repair survives.
- Confirm score lookup still locates the intended score after title metadata
  changes, and inspect ambiguous matches before selecting the first score. The
  recorded evidence does not establish filename-versus-title lookup behaviour
  after rename; no guessed forScore identifier/API was introduced.
- Create new still relies on selecting the newly created setlist and using an
  unused name. The native action's duplicate-name behaviour is unverified. Use a
  disposable setlist first; equal counts do not prove correct target or order.

### Could a compiler change remove these repairs?

Assessment after inspecting the installed compiler source, 21 October 2026:

| Repair | Automation potential | Current blocker |
| --- | --- | --- |
| NAME/ARC/SCORE indexed selection | A local compiler can potentially generate the native selection and wire its output | The local binding exists, but the iPad rejected the tested Jelly enum forms. No replacement source form has been verified on the app |
| COL ordered collections | Potential local generation of native collection actions and references | Requires correct action serialization, scoped variables and native File/Score preservation, then device verification |
| Native return tokens and named-variable conditions | Good candidates for local compiler serialization fixes | Existing local interpolation/UUID defects and app-specific wiring defects must be isolated and tested; literal Output acceptance does not establish native File returns |
| Save destination CFG02 | Could be added to a local compiler binding | The inspected SaveFileParameter exposes input/ask/path/overwrite, with no native Folder destination field. A path string is not an equivalent replacement |
| CONF folder/config selection and receiving settings | Some metadata/wiring might be generated once the representation is verified | User-selected provider Folder references, permissions and actual app receiving behaviour still require device setup/checking |
| FS01-FS13 forScore actions | Potential with verified native action templates/bindings | No verified Jelly binding or complete machine-readable native action schema is available in the current setup; action display names alone are insufficient |

Editing the WSL Open-Jellycore checkout changes only locally generated exports;
it does not patch the compiler bundled inside Jellycuts on the iPad. The current
workflow transfers source and recompiles there. To benefit from a patched local
compiler, a separate route would need to generate the final Shortcut locally,
preserve/assemble native actions, and use a verified signing/import workflow.
Local files are currently unsigned and that import route has not been tested.

No further native repair slot was removed on the strength of local compiler access
alone. The supported source-side Output/indentation fixes above are already applied.
Developing and validating a local compiler/export route is feasible investigation,
but it is additional work, not functionality the present installation provides.

## Transfer and integrated checks

Preserve renamed working installed copies. Transfer Canonical 10, Assembly 12 and
Main 4 (`.jelly` or byte-identical `.txt` copies). Keep/reuse the completed archive
when its interface matches. Install/confirm exact names in dependency order:
Canonical, Archive, Assembly, Main. Reapply the new Canonical's NAME01/NAME02,
receiving type and final canonicalName output-token settings. In Assembly, retain
the guard while completing native slots and inspect every If/Repeat boundary.

| Check on disposable data | Expected result | Actual |
| --- | --- | --- |
| Naming valid/invalid | Existing functional naming driver returns expected stems; missing filename/rule stops and returns empty Text; actual generated Output token is canonicalName | Not run |
| Return propagation | Main returns the assembly's actual report/error Text, without literal parameter labels or guessed Respond settings | Not run |
| Missing COL01 / COL02 collection | In a guarded disposable copy, inspect/test each incomplete collection check; stops before saving/importing or setlist operations | Not run |
| Missing working Score / incomplete COL03 | Stops before that score's metadata use, or before all setlist mutations respectively; prior files/imports/metadata can remain | Not run |
| Empty choices | If a Choose action returns no value, the new check stops before consuming it; native cancellation may halt the action before the check | Not run |
| Two-piece success and repetition | Complete slots, select two PDFs; verify B,A and an intentional repeated-score order; counts match, native identities/order inspected | Not run |
| Readback mismatch | On a disposable setlist/modified test copy, mismatched readback returns an explicit error; inspect actual entries before retrying | Not run |
| Archive regression | Reuse the user's repaired archive twice; no new numbered copies and returned result remains a native File | Prior manual reuse repair reported; not rerun for this set |

## Local validation

Run from the repository root:

```powershell
python jelly/scripts/build.py jelly/shortcuts/reusable/util-canonical-choir-name.jelly jelly/shortcuts/reusable/util-archive-choir-pdf.jelly jelly/shortcuts/reusable/util-assemble-choir-service.jelly jelly/shortcuts/main/main-build-choir-service.jelly
```

The older CLI rejects the positional Output form as a known profile mismatch;
its additional control-flow/serialization limitations can obscure further errors.
Do not describe these attempts as a compiler pass or rewrite the supported app
form to silence them. Diagnostics are in per-source `build/...build.json` and
`build/forscore-review-summary.log`. The final local outcome is recorded in
[config integration tests](../tests/config-integration.md).

The wrapper/compiler is a supplementary check for this profile, not a substitute
for app compilation, native action/variable inspection or integrated device testing.
