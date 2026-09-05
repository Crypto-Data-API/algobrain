# Backward-compatible PowerShell wrapper for the cross-platform Python manager.
param(
    [string]$BindHost = "127.0.0.1",
    [int]$Port = 8010
)
$ErrorActionPreference = "Stop"

$python = Get-Command py -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command python -ErrorAction Stop }
& $python.Source "$PSScriptRoot\manage_mcp.py" start --host $BindHost --port $Port
exit $LASTEXITCODE
