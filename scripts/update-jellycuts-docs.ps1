param(
    [ValidatePattern('^[0-9a-f]{40}$')]
    [string]$Commit = '19306be1dd30c20e12058ebe144dd8342e64ca39',
    [switch]$Offline
)

# Run from any directory. Offline rebuilds Markdown from the recorded snapshot.
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
$vendorRoot = Join-Path $repoRoot 'jelly/vendor/jellycuts-docs'
$rawRoot = Join-Path $vendorRoot 'upstream'
$markdownRoot = Join-Path $vendorRoot 'markdown'
$utf8 = New-Object System.Text.UTF8Encoding($false)
function Write-Utf8([string]$Path, [string]$Value) {
    [IO.Directory]::CreateDirectory((Split-Path $Path -Parent)) | Out-Null
    [IO.File]::WriteAllText($Path, $Value.Replace("`r`n", "`n"), $utf8)
}
function Convert-Reference([string]$Html, [string]$PageUrl) {
    # Upstream pages contain a large sidebar. Keep only the document body.
    $body = [regex]::Match($Html, '(?is)<div\b[^>]*\bid="Main"[^>]*>(.*)</body>').Groups[1].Value
    if (!$body) { throw 'No document heading found; inspect upstream markup before updating.' }
    $body = [regex]::Replace($body, '(?is)<(script|style)\b.*?</\1>', '')
    $body = [regex]::Replace($body, '(?is)<h([1-6])\b[^>]*>(.*?)</h\1>', {
        param($m)
        "`n" + ('#' * [int]$m.Groups[1].Value) + ' ' + $m.Groups[2].Value + "`n"
    })
    $codeBlocks = New-Object 'System.Collections.Generic.List[string]'
    $body = [regex]::Replace($body, '(?is)<pre\b[^>]*>(.*?)</pre>', {
        param($m)
        # Avoid introducing whitespace into code or decoding entities twice.
        $code = [Net.WebUtility]::HtmlDecode([regex]::Replace($m.Groups[1].Value, '<[^>]+>', ''))
        $token = "JELLYCODEBLOCK$($codeBlocks.Count)END"
        $codeBlocks.Add("~~~~text`n" + $code.Trim("`r", "`n") + "`n~~~~")
        "`n$token`n"
    })
    $body = [regex]::Replace($body, '(?is)<code\b[^>]*>(.*?)</code>', '`$1`')
    $body = [regex]::Replace($body, '(?is)<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>', {
        param($m)
        $href = $m.Groups[1].Value
        if ($href -match '^javascript:') { return $m.Groups[2].Value }
        $href = [Net.WebUtility]::HtmlDecode($href)
        $href = ([Uri]::new([Uri]$PageUrl, $href)).AbsoluteUri
        '[' + $m.Groups[2].Value + '](' + $href + ')'
    })
    $body = [regex]::Replace($body, '(?is)<li\b[^>]*>', "`n- ")
    $body = [regex]::Replace($body, '(?is)<br\s*/?>|</(?:p|div|section|article|tr)>', "`n")
    $body = [regex]::Replace($body, '<[^>]+>', '')
    $body = [Net.WebUtility]::HtmlDecode($body)
    $body = [regex]::Replace($body, '\n[ \t]+', "`n")
    $body = ([regex]::Replace($body, '\n{3,}', "`n`n")).Trim()
    for ($i = 0; $i -lt $codeBlocks.Count; $i++) {
        $body = $body.Replace("JELLYCODEBLOCK$($i)END", $codeBlocks[$i])
    }
    return $body + "`n"
}

if ($Offline) {
    $manifest = Get-Content (Join-Path $vendorRoot 'snapshot.json') -Raw | ConvertFrom-Json
    $Commit = $manifest.commit
    foreach ($record in $manifest.files) {
        $recordPath = [IO.Path]::GetFullPath((Join-Path $rawRoot $record.path))
        if (!$recordPath.StartsWith($rawRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid manifest path.' }
        if (!(Test-Path $recordPath) -or (Get-FileHash $recordPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $record.sha256) { throw "Snapshot hash mismatch: $($record.path)" }
    }
} else {
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $archivePath = Join-Path ([IO.Path]::GetTempPath()) ('jellycuts-docs-' + [guid]::NewGuid() + '.zip')
    try {
        Invoke-WebRequest "https://codeload.github.com/Jellycuts/docs.jellycuts.com/zip/$Commit" -OutFile $archivePath -UseBasicParsing
        $archive = [IO.Compression.ZipFile]::OpenRead($archivePath)
        try {
            $entries = @($archive.Entries | Where-Object {
                $_.FullName -match '^[^/]+/((Language_Guide|Getting_Started|Documentation/Shortcuts)/[^/]+\.html|README\.md|[^/]*(LICENSE|COPYING|NOTICE)[^/]*)$'
            })
            if ($entries.Count -lt 100) { throw 'Unexpectedly small snapshot; inspect upstream layout.' }
            $oldFiles = @()
            if (Test-Path $rawRoot) {
                $oldManifest = Get-Content (Join-Path $vendorRoot 'snapshot.json') -Raw | ConvertFrom-Json
                $oldFiles = @($oldManifest.files)
                foreach ($oldFile in $oldFiles) {
                    $oldPath = [IO.Path]::GetFullPath((Join-Path $rawRoot $oldFile.path))
                    if (!$oldPath.StartsWith($rawRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid manifest path.' }
                    if (!(Test-Path $oldPath) -or (Get-FileHash $oldPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $oldFile.sha256) { throw "Locally modified snapshot: $($oldFile.path)" }
                }
            }
            $newPaths = @()
            foreach ($entry in $entries) {
                $relative = $entry.FullName.Substring($entry.FullName.IndexOf('/') + 1)
                $newPaths += $relative
                $destination = [IO.Path]::GetFullPath((Join-Path $rawRoot $relative))
                if (!$destination.StartsWith($rawRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid archive path.' }
                [IO.Directory]::CreateDirectory((Split-Path $destination -Parent)) | Out-Null
                [IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $destination, $true)
            }
            foreach ($oldFile in $oldFiles) {
                if ($oldFile.path -notin $newPaths) {
                    # Paths were validated above. Remove only recorded obsolete files.
                    Remove-Item -LiteralPath (Join-Path $rawRoot $oldFile.path)
                    $obsoleteMarkdown = Join-Path $markdownRoot ($oldFile.path -replace '\.html$', '.md')
                    if ($oldFile.path.EndsWith('.html') -and (Test-Path $obsoleteMarkdown)) { Remove-Item -LiteralPath $obsoleteMarkdown }
                }
            }
        } finally { $archive.Dispose() }
    } finally {
        if (Test-Path $archivePath) { Remove-Item -LiteralPath $archivePath }
    }
    $manifest = [ordered]@{
        repository = 'https://github.com/Jellycuts/docs.jellycuts.com'
        branch = 'gh-pages'
        commit = $Commit
        retrievedUtc = [DateTime]::UtcNow.ToString('o')
        scope = @('Language_Guide/*.html', 'Getting_Started/*.html', 'Documentation/Shortcuts/*.html', 'README.md', 'root license/notice files if present')
        license = 'No license declaration found in repository metadata or root at initial retrieval; no additional rights granted.'
        files = @()
    }
    $manifest.files = @(Get-ChildItem $rawRoot -File -Recurse | Sort-Object FullName | ForEach-Object {
        [ordered]@{ path = $_.FullName.Substring($rawRoot.Length + 1).Replace('\', '/'); sha256 = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant() }
    })
    Write-Utf8 (Join-Path $vendorRoot 'snapshot.json') ($manifest | ConvertTo-Json -Depth 6)
}

$index = @(
    '# Local Jellycuts documentation', '',
    "Pinned upstream commit: ``$Commit``. See [snapshot provenance](../vendor/jellycuts-docs/README.md).", '',
    'Read the relevant action or language page before editing Jelly source. Markdown is generated for search; original HTML is authoritative for extraction details. Documentation does not establish compatibility with the installed app.', '',
    'For device results and known conflicts, read [compatibility evidence](../tests/compatibility/README.md) and [project reference](jellycuts-reference.md).', '',
    '## Start here', '',
    '- Language: [basics](../vendor/jellycuts-docs/markdown/Language_Guide/basics.md), [variables](../vendor/jellycuts-docs/markdown/Language_Guide/variables.md), [globals](../vendor/jellycuts-docs/markdown/Language_Guide/global.md), [repeats](../vendor/jellycuts-docs/markdown/Language_Guide/repeat.md).',
    '- Reported errors: [file details](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/fileDetail.md), [list items](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getItemFromList.md), [output](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/output.md).',
    '- Composition: [Run Shortcut](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/runShortcut.md).', '',
    '## All pages', ''
)
foreach ($file in (Get-ChildItem $rawRoot -Filter '*.html' -Recurse | Sort-Object FullName)) {
    $relative = $file.FullName.Substring($rawRoot.Length + 1).Replace('\', '/')
    $expected = @($manifest.files | Where-Object { $_.path -eq $relative })
    if ($expected.Count -ne 1 -or (Get-FileHash $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expected[0].sha256) {
        throw "Snapshot hash mismatch: $relative"
    }
    $markdownPath = $relative -replace '\.html$', '.md'
    $content = Convert-Reference ([IO.File]::ReadAllText($file.FullName)) "https://docs.jellycuts.com/$relative"
    $source = "https://github.com/Jellycuts/docs.jellycuts.com/blob/$Commit/$relative"
    Write-Utf8 (Join-Path $markdownRoot $markdownPath) ("Source: $source`n`n" + $content)
    $index += "- [$($relative -replace '\.html$', '')](../vendor/jellycuts-docs/markdown/$markdownPath)"
}
Write-Utf8 (Join-Path $repoRoot 'jelly/docs/jellycuts-docs-index.md') ($index -join "`n")
Write-Output "Generated references from $Commit; $($manifest.files.Count) upstream files recorded."
