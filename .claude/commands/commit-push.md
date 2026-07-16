---
description: Stage all changes, commit, and push to the current branch's upstream
argument-hint: [optional commit message]
allowed-tools: Bash(git:*)
---
Commit and push all pending changes in this repository.

1. Run `git status --short` and `git diff --stat` (plus `git diff --stat --staged`) so you know exactly what will be committed.
2. Stage everything: `git add -A`.
3. Commit:
   - If `$ARGUMENTS` is non-empty, use it verbatim as the commit message.
   - Otherwise, write a concise, descriptive message summarizing the staged changes (imperative mood, e.g. "Update strategy pages and fix broken links").
   - End the commit message with this trailer:
     `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
4. Push to the current branch's upstream: `git push`.
5. Report the resulting commit hash and confirm the push succeeded (or surface any error).

Guardrails: never use `--force`/`--force-with-lease`, never `--no-verify`, and do not amend existing commits. If there is nothing to commit, say so and stop.
