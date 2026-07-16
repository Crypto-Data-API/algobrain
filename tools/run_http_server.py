#!/usr/bin/env python3
"""
HTTP launcher for the AlgoBrain wiki MCP server.

Runs the same server defined in mcp_server.py, but over the Streamable HTTP
transport instead of stdio so that any client on this PC can connect to it at
http://<host>:<port>/mcp (default http://127.0.0.1:8010/mcp).

Bind to 127.0.0.1 (default) to expose the server to every process on THIS PC
only. Pass --host 0.0.0.0 to expose it to other machines on the network.

Run:
    .venv/Scripts/python.exe tools/run_http_server.py
    .venv/Scripts/python.exe tools/run_http_server.py --host 127.0.0.1 --port 8010

Connect from Claude Code:
    claude mcp add --transport http algobrain http://127.0.0.1:8010/mcp
"""
import argparse

from mcp_server import server


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8010)
    args = parser.parse_args()

    server.settings.host = args.host
    server.settings.port = args.port
    print(f"algobrain MCP (HTTP) on http://{args.host}:{args.port}/mcp", flush=True)
    server.run("streamable-http")


if __name__ == "__main__":
    main()
