# Backward-compatible PowerShell wrapper for the cross-platform Python manager.
$ErrorActionPreference = "Stop"

$python = Get-Command py -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command python -ErrorAction Stop }
& $python.Source "$PSScriptRoot\manage_mcp.py" stop
exit $LASTEXITCODE
