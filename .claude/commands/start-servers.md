---
description: Start the AlgoBrain wiki MCP server (Streamable HTTP) on 127.0.0.1:8010
allowed-tools: Bash(powershell:*), Bash(pwsh:*), Read
---
Start the local AlgoBrain MCP / API server for this vault.

Run the launcher (starts the server as a hidden background process):

```
powershell -ExecutionPolicy Bypass -File tools/start_servers.ps1
```

The server exposes the ~3,500-page algobrain vault over Streamable HTTP at
**http://127.0.0.1:8010/mcp** (tools: `wiki_search`, `wiki_read`, `wiki_stats`,
`wiki_lint`, `wiki_ingest`). PID is written to `.mcp-http.pid`; logs go to
`.mcp-http.log` / `.mcp-http.err.log` (all gitignored).

After launching:
1. Confirm startup by reading the last lines of `.mcp-http.err.log` — a healthy
   start shows Uvicorn "Application startup complete" / "Uvicorn running on
   http://127.0.0.1:8010". If it shows an error (e.g. port already in use),
   report it.
2. Report the MCP URL. To use it from Claude Code (one-time registration):
   `claude mcp add --transport http algobrain http://127.0.0.1:8010/mcp`

To stop it later: `powershell -ExecutionPolicy Bypass -File tools/stop_servers.ps1`
