---
description: Start the local, self-pacing daily AlgoBrain improvement loop (runs /improve-algobrain-loop every 24h by default)
argument-hint: "[interval, default 24h]"
allowed-tools: Skill
---
Start the recurring local AlgoBrain improvement loop.

Interval: use `$ARGUMENTS` if given (e.g. "6h", "12h"); otherwise default to `24h`.

Invoke the `loop` skill to run `/improve-algobrain-loop` on that interval — equivalent to
typing:

```
/loop 24h /improve-algobrain-loop
```

(substitute the resolved interval if `$ARGUMENTS` overrides the default).

## Why this is session-scoped, not a cloud routine

`/improve-algobrain-loop` uses the local wiki MCP server (`wiki_lint`, `wiki_search`,
`wiki_stats` at `http://127.0.0.1:8010/mcp`, started by `/start-servers`), which only
exists on this machine — a cloud-scheduled agent (the `schedule` skill / `CronCreate`)
cannot reach it. So this loop deliberately runs through the `loop` skill in this local
Claude Code session instead. Practical implications to tell the user if not already
obvious:

- The loop only keeps advancing while this local session/CLI process stays running.
  Closing the terminal breaks the chain; re-run `/start-loops` to resume.
- Before starting, confirm the local MCP server is up (`/start-servers` if not — check
  `.mcp-http.pid` / tail `.mcp-http.err.log`), since the first iteration will try to use it.
- Each firing runs exactly one bounded iteration of `/improve-algobrain-loop` (pick one
  area, ~60 minutes of sub-agent work, commit + push with a changelog entry) — the loop
  itself just handles the once-per-interval cadence, not the work sizing.
- To stop it, tell Claude to stop the loop during a running iteration.

If the user instead wants a loop that survives the local machine being off/asleep (at the
cost of losing access to the local MCP server), point them at the `schedule` skill
(`CronCreate`-backed cloud routine) as the alternative — don't switch to it silently.
