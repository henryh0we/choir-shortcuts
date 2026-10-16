# Pinned Jellycuts documentation

Upstream: https://github.com/Jellycuts/docs.jellycuts.com

Branch: `gh-pages`. Commit: `19306be1dd30c20e12058ebe144dd8342e64ca39`.

The [manifest](snapshot.json) records retrieval time, scope and SHA-256 hashes. `upstream/` contains 306 unmodified files: getting-started guides, language guides, native Shortcuts action pages and the upstream README. Website assets and third-party action libraries are excluded. HTML is reference source, not a locally hosted website.

`markdown/` is generated for searching and reading. It removes the sidebar and formatting markup, retaining document text, signatures and code examples. Consult original HTML if extraction looks suspicious. Upstream errors and older syntax are intentionally preserved; an example in this snapshot is not a passing compilation test.

No license declaration was found in upstream repository metadata or root at retrieval. These files remain attributed to their upstream authors; this snapshot grants no additional redistribution rights. Retain upstream notices. Review upstream licensing before publishing or redistributing the copied documentation.

Start with the [reference index](../../docs/jellycuts-docs-index.md) and [device compatibility record](../../tests/compatibility/README.md).

## Refresh

From the repository root, with Windows PowerShell 5.1 or PowerShell 7:

```powershell
# Rebuild Markdown and index without network, checking snapshot hashes.
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/update-jellycuts-docs.ps1 -Offline

# Fetch an explicitly selected full upstream commit SHA and regenerate references.
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/update-jellycuts-docs.ps1 -Commit <40-character-commit-sha>
```

The script defaults to the pinned commit, never a moving branch. It verifies existing recorded files before replacing a snapshot and removes recorded obsolete files during refresh. Project corrections belong in `jelly/docs/jellycuts-reference.md` or the compatibility record. Review the manifest, upstream and Markdown diff together. Update the commit in this README and the script default when deliberately adopting another revision. Check upstream licensing again at that revision.

A documentation refresh does not establish new app compatibility. Retest changed language/action forms under the installed app before adopting them in production.

## Repository validation, 16 October 2026

Initial integration checked all 306 recorded upstream hashes, all 305 generated pages and all 625 preformatted code blocks against their HTML originals (including indentation and enum spelling). The network refresh and offline rebuild both succeeded; the offline rebuild reproduced identical Markdown hashes. Local navigation links were checked. These checks validate the reference import, not Jelly compilation or iPad execution.
