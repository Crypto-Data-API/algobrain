#!/usr/bin/env python3
"""Cross-platform setup and process manager for the AlgoBrain MCP server."""

from __future__ import annotations

import argparse
import json
import os
import signal
import socket
import subprocess
import sys
import time
import venv
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS = ROOT / "tools" / "requirements.txt"
HTTP_SERVER = ROOT / "tools" / "run_http_server.py"
STDIO_SERVER = ROOT / "tools" / "mcp_server.py"
PID_FILE = ROOT / ".mcp-http.pid"
OUT_LOG = ROOT / ".mcp-http.log"
ERR_LOG = ROOT / ".mcp-http.err.log"
MINIMUM_PYTHON = (3, 10)


def venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def check_python_version() -> None:
    if sys.version_info < MINIMUM_PYTHON:
        required = ".".join(map(str, MINIMUM_PYTHON))
        current = f"{sys.version_info.major}.{sys.version_info.minor}"
        raise SystemExit(f"AlgoBrain requires Python {required}+; found {current}.")


def runtime_is_ready() -> bool:
    python = venv_python()
    if not python.is_file():
        return False
    check = subprocess.run(
        [str(python), "-c", "from mcp.server import MCPServer"],
        cwd=ROOT,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return check.returncode == 0


def setup() -> None:
    check_python_version()
    if not venv_python().is_file():
        print(f"Creating virtual environment at {VENV_DIR}")
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)

    print("Installing AlgoBrain MCP dependencies")
    subprocess.run(
        [str(venv_python()), "-m", "pip", "install", "-r", str(REQUIREMENTS)],
        cwd=ROOT,
        check=True,
    )
    if not runtime_is_ready():
        raise SystemExit("Setup completed, but the MCP runtime could not be imported.")
    print("AlgoBrain MCP setup complete.")


def ensure_runtime(auto_setup: bool) -> None:
    if runtime_is_ready():
        return
    if auto_setup:
        setup()
        return
    raise SystemExit(
        "MCP runtime is not installed. Run: <python> tools/manage_mcp.py setup "
        "(python3 on macOS/Linux, py on Windows)"
    )


def process_is_running(pid: int) -> bool:
    if os.name == "nt":
        import ctypes

        process_query_limited_information = 0x1000
        handle = ctypes.windll.kernel32.OpenProcess(
            process_query_limited_information, False, pid
        )
        if not handle:
            return False
        ctypes.windll.kernel32.CloseHandle(handle)
        return True
    try:
        os.kill(pid, 0)
    except (OSError, ProcessLookupError):
        return False
    return True


def read_state() -> dict[str, object] | None:
    if not PID_FILE.is_file():
        return None
    try:
        state = json.loads(PID_FILE.read_text(encoding="utf-8"))
        if not isinstance(state.get("pid"), int):
            raise ValueError
        return state
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def clear_stale_state() -> None:
    if PID_FILE.exists():
        PID_FILE.unlink()


def wait_for_port(host: str, port: int, process: subprocess.Popen[bytes]) -> None:
    probe_host = "127.0.0.1" if host in {"0.0.0.0", "::"} else host
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"server exited with status {process.returncode}; see {ERR_LOG}")
        try:
            with socket.create_connection((probe_host, port), timeout=0.25):
                pass
            # A different process may already own the port while this child is still
            # reporting its bind failure. Give the child a moment to prove it stayed up.
            time.sleep(0.2)
            if process.poll() is None:
                return
            raise RuntimeError(
                f"server exited with status {process.returncode}; see {ERR_LOG}"
            )
        except OSError:
            time.sleep(0.1)
    raise RuntimeError(f"server did not listen on {host}:{port} within 15 seconds")


def start(host: str, port: int) -> None:
    state = read_state()
    if state and process_is_running(int(state["pid"])):
        print(f"AlgoBrain MCP is already running (PID {state['pid']}) at {state['url']}")
        return
    clear_stale_state()
    ensure_runtime(auto_setup=True)

    command = [str(venv_python()), str(HTTP_SERVER), "--host", host, "--port", str(port)]
    popen_kwargs: dict[str, object] = {
        "cwd": ROOT,
        "stdin": subprocess.DEVNULL,
    }
    if os.name == "nt":
        popen_kwargs["creationflags"] = (
            subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS
        )
    else:
        popen_kwargs["start_new_session"] = True

    with OUT_LOG.open("ab") as stdout, ERR_LOG.open("ab") as stderr:
        process = subprocess.Popen(command, stdout=stdout, stderr=stderr, **popen_kwargs)

    try:
        wait_for_port(host, port, process)
    except Exception:
        if process.poll() is None:
            process.terminate()
        raise

    url = f"http://{host}:{port}/mcp"
    PID_FILE.write_text(
        json.dumps(
            {
                "pid": process.pid,
                "host": host,
                "port": port,
                "url": url,
                "started_at": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Started AlgoBrain MCP (PID {process.pid}) at {url}")
    print(f"Logs: {OUT_LOG} and {ERR_LOG}")


def stop() -> None:
    state = read_state()
    if not state:
        clear_stale_state()
        print("AlgoBrain MCP is not running.")
        return

    pid = int(state["pid"])
    if not process_is_running(pid):
        clear_stale_state()
        print(f"AlgoBrain MCP process {pid} is no longer running; cleared stale state.")
        return

    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    else:
        deadline = time.monotonic() + 5
        while process_is_running(pid) and time.monotonic() < deadline:
            time.sleep(0.1)
        if process_is_running(pid) and os.name != "nt":
            os.kill(pid, signal.SIGKILL)

    clear_stale_state()
    print(f"Stopped AlgoBrain MCP (PID {pid}).")


def status() -> int:
    state = read_state()
    if state and process_is_running(int(state["pid"])):
        print(f"AlgoBrain MCP is running (PID {state['pid']}) at {state['url']}")
        return 0
    clear_stale_state()
    print("AlgoBrain MCP is not running.")
    return 1


def replace_process(script: Path, arguments: list[str]) -> None:
    ensure_runtime(auto_setup=False)
    command = [str(venv_python()), str(script), *arguments]
    if os.name == "nt":
        raise SystemExit(subprocess.call(command, cwd=ROOT))
    os.execv(str(venv_python()), command)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("setup", help="create .venv and install dependencies")

    for command, help_text in (
        ("start", "start Streamable HTTP in the background"),
        ("run-http", "run Streamable HTTP in the foreground"),
    ):
        child = subparsers.add_parser(command, help=help_text)
        child.add_argument("--host", default="127.0.0.1")
        child.add_argument("--port", type=int, default=8010)

    subparsers.add_parser("run", help="run the STDIO server in the foreground")
    subparsers.add_parser("stop", help="stop the background HTTP server")
    subparsers.add_parser("status", help="show background HTTP server status")
    subparsers.add_parser("restart", help="restart the background HTTP server")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "setup":
            setup()
        elif args.command == "start":
            start(args.host, args.port)
        elif args.command == "run-http":
            replace_process(
                HTTP_SERVER,
                ["--host", args.host, "--port", str(args.port)],
            )
        elif args.command == "run":
            replace_process(STDIO_SERVER, [])
        elif args.command == "stop":
            stop()
        elif args.command == "status":
            return status()
        elif args.command == "restart":
            state = read_state() or {}
            host = str(state.get("host", "127.0.0.1"))
            port = int(state.get("port", 8010))
            stop()
            start(host, port)
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
