<#
.SYNOPSIS
    Restores AlgoBrain's canonical Obsidian graph colours.

.DESCRIPTION
    Obsidian holds graph settings in memory and rewrites .obsidian/graph.json
    whenever they change, silently discarding hand edits to the colour palette.
    This script restores the `colorGroups` array from .obsidian/graph.default.json
    while leaving transient view state (search query, zoom, scale, force settings)
    untouched, so restoring does not disturb whatever you were looking at.

    IMPORTANT: if Obsidian is running it may overwrite this again on its next
    settings save. Close Obsidian, or reload the vault (Ctrl+R) after running,
    for the change to take effect. The script warns if Obsidian looks active.

    NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads UTF-8 files
    without a BOM as ANSI, which corrupts non-ASCII characters and breaks parsing.

.PARAMETER All
    Restore every key present in graph.default.json, not just colorGroups.
    Overwrites view state too.

.PARAMETER Check
    Report whether graph.json matches the canonical palette; change nothing.
    Exit code 0 = in sync, 1 = drifted.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File tools/restore_obsidian_config.ps1
    powershell -ExecutionPolicy Bypass -File tools/restore_obsidian_config.ps1 -Check
#>
[CmdletBinding()]
param(
    [switch]$All,
    [switch]$Check
)

$ErrorActionPreference = 'Stop'

$repoRoot    = Split-Path -Parent $PSScriptRoot
$livePath    = Join-Path $repoRoot '.obsidian/graph.json'
$defaultPath = Join-Path $repoRoot '.obsidian/graph.default.json'

if (-not (Test-Path $defaultPath)) {
    Write-Error "Canonical config not found: $defaultPath"
    exit 2
}
if (-not (Test-Path $livePath)) {
    Write-Error "Live graph config not found: $livePath"
    exit 2
}

$default = Get-Content $defaultPath -Raw | ConvertFrom-Json
$live    = Get-Content $livePath    -Raw | ConvertFrom-Json

# Compare on normalised JSON so key order and whitespace do not cause false drift.
$canonicalGroups = $default.colorGroups | ConvertTo-Json -Depth 10 -Compress
$liveGroups      = $live.colorGroups    | ConvertTo-Json -Depth 10 -Compress
$inSync          = ($canonicalGroups -eq $liveGroups)

if ($Check) {
    if ($inSync) {
        Write-Host "graph.json colour palette is in sync with graph.default.json." -ForegroundColor Green
        exit 0
    }
    Write-Host "graph.json colour palette has DRIFTED from graph.default.json." -ForegroundColor Yellow
    Write-Host "Run tools/restore_obsidian_config.ps1 to restore it."
    exit 1
}

if ($inSync -and -not $All) {
    Write-Host "Already in sync - nothing to do." -ForegroundColor Green
    exit 0
}

if ($All) {
    foreach ($prop in $default.PSObject.Properties) {
        if ($prop.Name -eq '_comment') { continue }
        $live | Add-Member -NotePropertyName $prop.Name -NotePropertyValue $prop.Value -Force
    }
    $what = 'all canonical keys'
} else {
    $live | Add-Member -NotePropertyName 'colorGroups' -NotePropertyValue $default.colorGroups -Force
    $what = 'colorGroups'
}

$live | ConvertTo-Json -Depth 10 | Set-Content $livePath -Encoding utf8
Write-Host "Restored $what to .obsidian/graph.json" -ForegroundColor Green

# Obsidian will clobber this on its next settings write if it is running.
$obsidian = Get-Process -Name 'Obsidian' -ErrorAction SilentlyContinue
if ($obsidian) {
    Write-Host ""
    Write-Host "WARNING: Obsidian is running (PID $($obsidian[0].Id))." -ForegroundColor Yellow
    Write-Host "It may overwrite graph.json from memory on its next settings save." -ForegroundColor Yellow
    Write-Host "Reload the vault (Ctrl+R) to pick up these colours, or close Obsidian and re-run." -ForegroundColor Yellow
}
