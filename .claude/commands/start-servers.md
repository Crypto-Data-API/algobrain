---
description: Start the AlgoBrain wiki MCP server (Streamable HTTP) on 127.0.0.1:8010
allowed-tools: Bash(python tools/manage_mcp.py:*), Bash(python3 tools/manage_mcp.py:*), Bash(py tools/manage_mcp.py:*), Read
---
Start the local AlgoBrain MCP / API server for this vault.

Run the cross-platform launcher (it installs dependencies on first use and starts the
server as a background process):

Run `python3 tools/manage_mcp.py start` on macOS/Linux or
`py tools/manage_mcp.py start` on Windows.

The server exposes the AlgoBrain vault over Streamable HTTP at
**http://127.0.0.1:8010/mcp** (tools: `wiki_search`, `wiki_read`, `wiki_stats`,
`wiki_lint`, `wiki_ingest`). PID is written to `.mcp-http.pid`; logs go to
`.mcp-http.log` / `.mcp-http.err.log` (all gitignored).

After launching:
1. Confirm startup with `<python> tools/manage_mcp.py status`. If it reports an error
   (for example, because the port is already in use), inspect `.mcp-http.err.log` and
   report the cause.
2. Report the MCP URL. To use it from Claude Code (one-time registration):
   `claude mcp add --transport http algobrain http://127.0.0.1:8010/mcp`

To stop it later: `<python> tools/manage_mcp.py stop` (`python3` on macOS/Linux, `py` on
Windows).
