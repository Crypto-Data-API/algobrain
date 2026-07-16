# Start the AlgoBrain wiki MCP server over Streamable HTTP, in the background.
#
#   powershell -ExecutionPolicy Bypass -File tools/start_servers.ps1
#   powershell -ExecutionPolicy Bypass -File tools/start_servers.ps1 -Port 8010
#
# Serves the algobrain vault at http://127.0.0.1:<port>/mcp.
# PID -> .mcp-http.pid, logs -> .mcp-http.log / .mcp-http.err.log (all gitignored).
param(
    [string]$BindHost = "127.0.0.1",
    [int]$Port = 8010
)
$ErrorActionPreference = "Stop"

$root    = Split-Path -Parent $PSScriptRoot          # tools/ -> repo root
$py      = Join-Path $root ".venv\Scripts\python.exe"
$server  = Join-Path $root "tools\run_http_server.py"
$pidFile = Join-Path $root ".mcp-http.pid"
$outLog  = Join-Path $root ".mcp-http.log"
$errLog  = Join-Path $root ".mcp-http.err.log"
$url     = "http://$BindHost`:$Port/mcp"

# Already running?
if (Test-Path $pidFile) {
    $existingPid = (Get-Content $pidFile -ErrorAction SilentlyContinue | Select-Object -First 1)
    if ($existingPid -and (Get-Process -Id $existingPid -ErrorAction SilentlyContinue)) {
        Write-Output "AlgoBrain MCP already running (PID $existingPid) at $url"
        exit 0
    }
}

if (-not (Test-Path $py)) {
    throw "venv python not found at $py`nRun: python -m venv .venv; .\.venv\Scripts\python.exe -m pip install -r tools/requirements.txt"
}

$proc = Start-Process -FilePath $py `
    -ArgumentList @($server, "--host", $BindHost, "--port", "$Port") `
    -WorkingDirectory $root `
    -RedirectStandardOutput $outLog `
    -RedirectStandardError $errLog `
    -WindowStyle Hidden -PassThru

$proc.Id | Out-File -FilePath $pidFile -Encoding ascii
Write-Output "Started AlgoBrain MCP (PID $($proc.Id)) at $url"
Write-Output "Logs: $outLog / $errLog"
Write-Output "Register once with: claude mcp add --transport http algobrain $url"
