# V3 service-creation walkthroughs

8 November 2026. These are examples of the **intended finished design**, not instructions to run the current filename preview and not recorded test results. The [v3 plan](../../nextcloud-forscore-plan-v3.md) governs behavior. Examples are independent unless explicitly described as a rerun.

Actual native target lookup, score identity, gap insertion, overwrite/readback and review navigation still require integrated iPad checks. Where an operation is unsupported, the shortcut reports pending work rather than silently changing the policy.

## Common flow

**Receive music -> choose date/service -> read target -> choose Add/Overwrite/Cancel if it exists -> review -> optionally edit Name/Date/Order -> refreshed review -> Proceed -> execute -> report.**

Weekly derives dates/services from its selected folder and offers one batch proposal instead. Essential first-import metadata review happens before the final Proceed; existing saved Scores and annotations are reused. Composer/Genre creation, archive saves, imports, metadata edits and setlist changes happen only after that confirmation. A mode choice or an edit alone does not start writes.

The edit menu has **Change Name**, **Change Date**, **Change Order**, and **Back** only. Membership additions/removals happen separately. Changing a date can resolve a different target; its previous Overwrite choice does not carry over. File-provider order is the received order, not a guarantee of tap order.

## 1. New individual service whose music needs reordering

**Starting point:** No target exists for Sunday 15 November Evensong. Four unnumbered PDFs are shared from Files/Nextcloud to **V3 - Create Service**. For this example, all four Scores already exist in forScore with usable metadata.

The provider delivers them as:

1. Anthem
2. Responses
3. Canticles
4. Psalm

You choose **15 November 2026** in the date picker and **Evensong** in the service chooser. No full setlist name needs typing. The shortcut finds no existing target and presents:

```text
2026-11-15 - Sun - Evensong
Target: New setlist
Proposed order: Anthem -> Responses -> Canticles -> Psalm
Scores: reuse 4 saved forScore Scores
Order basis: received provider order; no comparable file positions
Proceed / Edit proposal / Cancel
```

You choose **Edit proposal -> Change Order**. Using the supported native ordering interface, you arrange the same four occurrences as **Responses -> Psalm -> Canticles -> Anthem**. This example does not assume a drag-and-drop control exists; the exact native interaction will be established during construction.

You return automatically to the refreshed proposal. You can choose another Name/Date/Order edit, or **Proceed**. Nothing has been imported, renamed or written yet.

After Proceed, the shortcut creates the setlist with that approved order, using the saved Scores and their annotations. It reads back the actual entries and reports the result. An unchanged rerun through Add must create no unintended duplicate entries or Scores.

**Expected final contents:** Responses -> Psalm -> Canticles -> Anthem.

## 2. New individual service whose numbered files already give the right order

**Starting point:** Tuesday 10 November Evensong does not yet exist. You share:

- Tue5-Finzi-MyLovelyOne.pdf
- Tue1-Clucas-Responses.pdf
- Tue4-Dove-StJohn'sService.pdf
- Tue3-Ps119vv65-88.pdf

Even if received in that order, the proposed sequence is **1 -> 3 -> 4 -> 5**, because these are comparable positions from the same service. Position 2 is not automatically flagged as missing.

Choose the date and Evensong. The proposed name is **2026-11-10 - Tue - Evensong**. Review unfamiliar Title/Composer/Type suggestions before approval; preserve source qualifiers and saved metadata.

If the composer name is known and approved but absent from forScore, the proposal can state that a Composer item will be created. Only after Proceed does **V3 - Resolve Composer** look up/create and return the object for assignment. Genuinely unknown authorship stays unassigned with metadata pending. An existing matched Score is used even if the incoming source PDF differs.

No order edit is needed. Proceed creates the ordered service from available usable music. If an occurrence cannot be prepared, New mode may create a partial service and report the unresolved reference/position; it must not silently omit it.

## 3. Existing service: add a missing piece in its intended gap

**Starting point:** The target date/service resolves to a live setlist containing:

```text
Responses -> Canticles -> Anthem
```

Your current request is:

```text
Responses -> Psalm -> Canticles -> Anthem
```

After date/service selection, the shortcut displays the actual current entries and offers **Overwrite contents / Add to existing / Cancel**. You choose **Add to existing**.

The refreshed proposal shows:

```text
Mode: Add to existing
Existing: Responses -> Canticles -> Anthem
Insert: Psalm between Responses and Canticles
Result: Responses -> Psalm -> Canticles -> Anthem
Preserve: all existing entries, their relative order and saved Scores
Proceed / Edit proposal / Cancel
```

On Proceed, prepare/import only what is actually missing, then insert the missing occurrence in the supported gap. Read back the result. If insertion is unavailable or its anchors are ambiguous, leave that insertion pending and explain why; do not append it in the wrong place or clear/rebuild in Add mode. Separate manual insertion is the fallback for the user.

**Expected final contents when insertion is supported:** Responses -> Psalm -> Canticles -> Anthem.

## 4. Existing service: overwrite because its order is wrong

**Starting point:** The live setlist contains:

```text
Anthem -> Responses -> Canticles -> Psalm -> Extra piece
```

The requested complete sequence is:

```text
Responses -> Psalm -> Canticles -> Anthem
```

You select the date/service, inspect the current contents and choose **Overwrite contents**. The proposal shows both sequences and makes clear that Extra piece will leave this setlist and the requested entries will be rebuilt in the approved order. That Score is not deleted from forScore.

If needed, choose **Edit proposal -> Change Order**, then return to the refreshed proposal. The selection/membership remains the supplied four occurrences; no music removal/addition editor appears.

On Proceed, ensure the full requested sequence is available before touching the existing entries. Then overwrite only this setlist's contents and verify the result. All existing Scores, annotations and unrelated setlists remain intact.

If the requested Psalm cannot be prepared, **do not clear the old setlist**. Report Overwrite pending. You can correct the source or supply a different selection in a separate run.

**Expected final contents for a complete successful overwrite:** Responses -> Psalm -> Canticles -> Anthem.

In contrast, choosing Add with all requested pieces already present would preserve their existing relative order and Extra piece. An order edit is not permission for Add to reorder existing entries; select Overwrite in the normal target-choice flow when that is what you want.

## 5. Existing service: a manually deleted requested piece comes back

**Starting point:** A service previously held **A -> B -> C**. You manually removed B, leaving **A -> C**, but the current creation input still requests **A -> B -> C**.

Rerun the normal shortcut for that date/service and choose **Add to existing**. The proposal includes B as a missing requested occurrence. It does not ask whether the prior deletion was intentional or remember a permanent omission preference.

After Proceed, B is added back in its intended gap where supported. Reuse its existing forScore Score and annotations. If the Score itself was also deleted, import it again from available archive/source; this cannot restore annotations deleted with the old Score.

If B is no longer in the current request, Add does not invent that request from history. It preserves whatever live entries remain.

## 6. Interrupted overwrite: repair using an ordinary rerun

**Starting point:** You approved **A -> B -> C -> D** in Overwrite mode. The run was interrupted after the target was partially populated, so actual current contents are **A -> B**.

Rerun creation with the same intended inputs. Choose the same date/service. The shortcut reads and shows **A -> B**, not the previously expected complete list, then offers **Overwrite contents / Add to existing / Cancel**.

| Your choice | Intended result |
| --- | --- |
| Overwrite contents | After a fresh complete-sequence check and final Proceed, rebuild the target as A -> B -> C -> D. |
| Add to existing | After Proceed, add missing C and D without duplicating existing A/B, where matching/order are unambiguous and supported. |
| Cancel | Leave the partial live setlist unchanged. |

No separate recovery wizard, rollback engine or automatic replay is involved. A failed run must not be reported as complete. Scores/annotations remain the saved performance copies. Native failures may abort again; the design does not promise transactions or uninterrupted continuation after an action error.

If the partial setlist was deleted instead, it is retired and must not be resurrected from saved history. A later explicit creation request is treated as a new current target request, not restoration of the deleted object.

## 7. Change the proposed date and discover a different existing service

**Starting point:** You initially chose 15 November Evensong and selected Overwrite for its existing target. Before Proceed, you notice the intended date was 22 November.

Choose **Edit proposal -> Change Date -> 22 November 2026**. The shortcut derives **2026-11-22 - Sun - Evensong**, resolves that date/service and reads its actual contents if present. It does not change or delete the 15 November service.

The earlier Overwrite decision is reset. If the 22 November target exists, make the ordinary Overwrite/Add to/Cancel choice for that target; otherwise review a new-service proposal. Your requested order and metadata decisions remain available, but the comparison is rebuilt for the new target. Only the refreshed proposal can be approved.

Changing Name instead is a display-name override for the same date/slot identity and associated live target. It does not silently move the service to another date, select another service type or create a duplicate. Any proposed rename of an existing setlist must be shown before final approval.

## 8. Weekly folder: a mixture of new, existing and unchanged services

**Starting point:** Select **INov9-15** in **V3 - Weekly**. For this example the resolved dates are 9–15 November 2026, and the following live target state is assumed:

| Service | Existing state | Default proposal |
| --- | --- | --- |
| Tue 10 - Evensong | Some requested occurrences missing | Add missing occurrences |
| Thu 12 - Evensong | No live target | Create new |
| Fri 13 - Evensong | Requested occurrences already present | Unchanged |
| Sun 15 - Eucharist | No live target | Create new |
| Sun 15 - Mattins | No live target; matching music exists | Create new |
| Sun 15 - Evensong | No live target | Create new |

Monday's selected-folder files are reported skipped by configuration. No empty Saturday setlist is created when no matching Saturday music is present. The shortcut does not recurse into YouthChoir or NewMusic merely because those collections contain parsable filenames.

You receive one batch proposal with inferred dates/names, actual existing contents where relevant, proposed ordered results, new/reused music and unresolved metadata. Known metadata is reused; unfamiliar required metadata can be reviewed once per distinct piece before confirmation.

If Tuesday needs replacement rather than additions, select that service's target-review choice and explicitly choose Overwrite. If a proposed order is wrong, select that service and **Edit proposal -> Change Order**. Return to the regenerated batch proposal; no mandatory chain of per-service editing questions is imposed. Do not add an extra music-membership editor.

One final Proceed starts the approved batch. Friday remains unchanged; Tuesday uses its explicitly chosen mode; other services are created using their available approved music. New/Add targets may be partial with explicit unresolved positions. A service in Overwrite mode with unresolved music stays pending without clearing its old contents. Independent services continue where native runtime control permits; an aborting native error can still end the run, followed by the normal rerun flow.

The final report identifies created, updated, unchanged, partial, pending or unconfirmed services and lists unresolved music/metadata. No historical deleted setlist is recreated unless current explicit inputs request that service again. An unchanged Add rerun introduces no unintended duplicates.

## What these examples leave outside this flow

- Adding/removing selected music is done separately, then a new proposal is produced. The edit menu only changes Name/Date/Order.
- Correcting the actual saved score edition/file is a separate user-invoked repair/insertion workflow; ordinary creation always reuses a matched existing Score.
- Title/Composer/Genre corrections on a shared Score affect every setlist using it. Preflight must disclose that shared effect and apply only approved fields after Proceed.
- Date/ordering/metadata/setlist examples are design walkthroughs, not claims that the current read-only preview implements them. Quote-line display artifacts in current preview reports remain a separate known issue.
