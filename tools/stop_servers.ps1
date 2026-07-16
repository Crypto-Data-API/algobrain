# Stop the AlgoBrain wiki MCP server started by start_servers.ps1.
#
#   powershell -ExecutionPolicy Bypass -File tools/stop_servers.ps1
$ErrorActionPreference = "Stop"

$root    = Split-Path -Parent $PSScriptRoot
$pidFile = Join-Path $root ".mcp-http.pid"

if (-not (Test-Path $pidFile)) {
    Write-Output "No .mcp-http.pid found - AlgoBrain MCP does not appear to be running."
    exit 0
}

$serverPid = (Get-Content $pidFile -ErrorAction SilentlyContinue | Select-Object -First 1)
$proc = if ($serverPid) { Get-Process -Id $serverPid -ErrorAction SilentlyContinue } else { $null }
if ($proc) {
    Stop-Process -Id $serverPid -Force
    Write-Output "Stopped AlgoBrain MCP (PID $serverPid)."
} else {
    Write-Output "Process $serverPid not running; clearing stale pid file."
}
Remove-Item $pidFile -Force
