#!/usr/bin/env python3
"""
HTTP launcher for the AlgoBrain wiki MCP server.

Runs the same server defined in mcp_server.py, but over the Streamable HTTP
transport instead of stdio so that any client on this PC can connect to it at
http://<host>:<port>/mcp (default http://127.0.0.1:8010/mcp).

Bind to 127.0.0.1 (default) to expose the server to every process on THIS PC
only. Pass --host 0.0.0.0 to expose it to other machines on the network.

Run:
    <python> tools/manage_mcp.py start
    <python> tools/manage_mcp.py run-http --host 127.0.0.1 --port 8010

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

    print(f"algobrain MCP (HTTP) on http://{args.host}:{args.port}/mcp", flush=True)
    server.run(
        transport="streamable-http",
        host=args.host,
        port=args.port,
        stateless_http=True,
        json_response=True,
    )


if __name__ == "__main__":
    main()
