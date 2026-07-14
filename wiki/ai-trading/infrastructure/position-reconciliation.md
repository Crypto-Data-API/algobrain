---
title: "Position Reconciliation"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, trading-bots, risk-management, deployment, crypto]
aliases: ["Reconciliation", "State Reconciliation", "Position Sync", "Ledger Reconciliation"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[bot-architecture]]", "[[broker-api]]"]
difficulty: advanced
related:
  - "[[bot-architecture]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[bot-kill-switch-design]]"
  - "[[paper-to-live-promotion]]"
  - "[[deployment]]"
  - "[[broker-api]]"
  - "[[funding-rate]]"
  - "[[exchange-api-key-security]]"
---

# Position Reconciliation

Position reconciliation is the continuous process of proving that a bot's **internal model of its state** (positions, orders, balances, P&L) matches the **exchange's authoritative truth**, and correcting any divergence before it can act on a false picture. In live crypto trading it is not housekeeping — it is a **top cause of silent losses**: a bot that believes it is delta-neutral while a hedge leg quietly went unfilled is running a directional bet it never chose, and it will keep doing so until reconciliation catches it or the market punishes it. The exchange is always the source of truth; internal state is a cache that drifts.

> Reconciliation is the audit layer under [[paper-to-live-promotion]] ("zero unexplained P&L") and the confirmation step for [[bot-kill-switch-design]] ("sent the flatten" ≠ "am flat"). It presumes secure, correctly-scoped venue access — see [[exchange-api-key-security]].

## Why internal state drifts

State divergence is the normal condition of a live bot, not an exception. The recurring causes:

| Cause | What happens | Why it silently loses money |
|---|---|---|
| **Partial fills** | An order for 10 ETH fills 6, then 4 later — or 6 and the rest cancels | Bot books the position it *sent*, not the size it *got*; sizing, hedging, and P&L are all wrong |
| **WebSocket gaps** | The fill/order stream drops a message or disconnects mid-event | Bot never sees a fill that happened (or sees a cancel that didn't); state and truth silently split |
| **Funding accruals** | Perp funding is debited/credited every 1h ([[hyperliquid]]) or 8h (Binance) | Balance changes with no order event; a bot that only tracks fills misreads its cash and margin |
| **Fee deductions** | Taker/maker fees, and fee-in-token (e.g., paid in BNB) | Realized P&L and available balance drift from the naive fill-price accounting |
| **Restart / crash recovery** | Bot restarts and rebuilds state from disk or from scratch | Orders/fills that occurred while down are missed; positions opened pre-crash are orphaned |
| **Rejects and post-only bounces** | An order the bot thinks is live was rejected or auto-cancelled | Bot waits on a fill that will never come, or re-sends and double-exposes |
| **Rounding / lot-size / dust** | Venue rounds to tick/lot; small residual balances ("dust") accumulate | Cumulative micro-drift eventually crosses a threshold and breaks a "flat" assumption |
| **Manual or cross-app interference** | A human, or another bot on the same account/sub-account, trades | Internal state has no record of the external action |

The insidious property is that **none of these throw an error**. The bot runs, places orders, reports P&L — all against a picture that is wrong. Losses accrue quietly until a reconciliation loop, a margin call, or a drawdown surprise exposes them.

## The reconciliation loop

The core design is a periodic (and event-triggered) loop that pulls authoritative state via REST and diffs it against the internal model:

```
every T seconds (and on: reconnect, restart, pre/post kill-switch, before sizing):
    truth   = venue REST snapshot (positions, open orders, balances, recent fills)
    internal = local state model
    diff = compare(truth, internal)   # position qty, order set, balance, realized P&L
    if diff within tolerance:
        heartbeat_ok()
    else:
        classify(diff)                # missed fill? funding? fee? phantom order? dust?
        if explainable and safe:
            correct_internal(truth)   # adopt venue truth as authoritative
        else:
            halt_and_alert(diff)      # unexplained -> possible bug/leak/compromise
```

Design points:

- **Venue truth wins, always.** On any conflict the internal model is corrected to match the exchange; the internal state is a cache, never the ledger.
- **Two cadences.** A fast **event-driven** path (reconcile on every reconnect, restart, and around any kill action) plus a slower **periodic** sweep (e.g., every 30–60s, and a full balance/P&L reconciliation each funding period and at least hourly — echoing the "reconcile at least every hour" rule in [[bot-risks-and-pitfalls]]).
- **Classify before correcting.** A drift that equals an expected funding debit or a known fee is *explained* — adopt it. A drift with no explanation is a **bug, a leak, or a compromised key** and must halt, not auto-correct (auto-correcting an unexplained gap hides the very incident you need to see).
- **Reconcile three ledgers, not one:** (1) **positions/quantities**, (2) **open-order set** (cancel phantoms, adopt unknown live orders), and (3) **balances/realized P&L** (the funding + fee ledger). Position-only reconciliation misses the funding/fee drift that quietly erodes carry strategies.

## Idempotency: the precondition for safe reconciliation

Reconciliation is only safe if re-sending is safe. Use **client order IDs** (`clientOrderId` / `cloid`) that are deterministic per intended order, so:

- A retry after an ambiguous timeout re-uses the same ID — the venue dedupes it, and you never double-send (a leading cause of accidental double exposure).
- After a restart, you can query by your own ID to learn the true fate of every order you *intended* to place, even if you never saw the ack.

Without idempotent IDs, crash recovery becomes a guessing game where re-submitting risks duplication and *not* re-submitting risks a missing leg — the reconciliation cannot be made safe.

## Restart / crash recovery

The hardest reconciliation moment is a cold start after a crash, because events happened while the bot was blind:

1. **Load persisted intent** — the last-known set of intended orders/positions and their client order IDs from disk/DB (persisted *before* each significant action, per [[bot-architecture]]).
2. **Pull venue truth** — current positions, all open orders, recent fills, and balances via REST.
3. **Reconcile by client order ID** — for each intended order, look up its real fate on the venue; adopt fills that occurred while down; cancel or account for the rest.
4. **Adopt orphans** — positions/orders on the venue with no internal record are adopted into state (and investigated — they may be a prior-session leg or cross-app interference).
5. **Recompute derived state** — delta, margin, exposure, P&L from the corrected truth *before* re-enabling the strategy.
6. **Only then re-arm trading.** A bot that starts trading before it has reconciled is trading blind against a phantom position — the single most common way restarts turn into losses.

## Detecting a WebSocket gap

Real-time fill/position streams drop messages. Defenses:

- **Sequence numbers / update IDs.** Track the venue's monotonic update ID; a gap means a missed message — trigger an immediate REST reconcile of the affected symbol.
- **Heartbeats.** No stream heartbeat within the interval → treat the feed as stale (a [[bot-kill-switch-design|data-staleness kill trigger]]) and reconcile before trusting anything.
- **Periodic full snapshots** regardless of stream health, so a silently-degraded stream cannot drift unbounded.
- **Reconcile on every reconnect.** Every WebSocket reconnection is a potential gap; always REST-reconcile immediately after.

## Worked example: the silent hedge break

A delta-neutral [[funding-rate-arbitrage|funding-arb]] sleeve intends spot-long 3.1 ETH + perp-short 3.1 ETH.

1. The spot buy fills fully (3.1 ETH). The perp short order is submitted; the ack WebSocket message is **dropped** during a brief disconnect. The venue actually filled only **1.6 ETH** (partial) before the rest was cancelled by a post-only bounce.
2. Internal state records perp-short **3.1 ETH** (what it sent). Truth is **1.6 ETH**. The book is now **+1.5 ETH net long** — a directional position no one chose.
3. Without reconciliation: the bot reports "delta-neutral," collects funding on 1.6 ETH, and eats the full P&L swing on 1.5 ETH of un-hedged ETH. A 6% ETH drop is a ~$300 loss on a position the dashboard says is flat.
4. With reconciliation: the 30-second sweep diffs perp position 1.6 (truth) vs 3.1 (internal), classifies it as an **un-filled leg** (not funding/fee), and — because a broken hedge is *not* a safe explainable drift — **halts the sleeve and alerts** (per [[bot-kill-switch-design]]), then either completes the missing 1.5 ETH short or flattens the spot leg reduce-only. The loss is bounded to seconds of exposure instead of hours.

This is the archetype of a "silent live loss": no error, a green dashboard, and money leaking from a position the bot does not know it has.

## Reconciliation health metrics

Track and alert on these so reconciliation itself is observable:

- **Time since last successful full reconcile** (staleness of the audit).
- **Count/size of unexplained diffs** per window (should be ~0; any non-zero is an incident).
- **Reconcile-induced corrections** (frequency of adopting venue truth — a rising trend signals a degrading feed or a bug).
- **Unexplained P&L** — the residual after attributing every balance change to a fill, funding, or fee. The [[paper-to-live-promotion|canary gate]] requires this to be zero.

## Getting the Data (CryptoDataAPI)

Reconciliation's authoritative source is *your own account* via the venue's private API — CryptoDataAPI does not hold your positions. But its market-wide funding and derivatives feeds are useful as an **independent cross-check** on the funding-accrual ledger (did the funding you were debited match the market rate?):

- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding to sanity-check perp funding accruals
- `GET /api/v1/hyperliquid/funding-rates?coin=BTC` — Hyperliquid 1h funding for per-hour accrual checks
- `GET /api/v1/backtesting/funding` — historical funding to reconstruct expected accruals over a window

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]]. For your *own* fills/positions/balances, use the exchange's private endpoints (see [[broker-api]], [[exchange-api-reference]]).

## Related

- [[bot-architecture]] — the portfolio tracker and state-persistence layer this depends on
- [[bot-risks-and-pitfalls]] — "incorrect position tracking" is the failure this closes
- [[bot-kill-switch-design]] — reconciliation confirms a flatten and detects position drift
- [[paper-to-live-promotion]] — the "zero unexplained P&L" gate is a reconciliation requirement
- [[deployment]] — end-of-day/periodic reconciliation as a production discipline
- [[broker-api]] — the private-API interface that provides venue truth
- [[funding-rate]] — a primary silent driver of balance drift
- [[exchange-api-key-security]] — an unexplained diff can be the first sign of a compromised key

## Sources

- General knowledge of production trading-system reconciliation practice; synthesized with this wiki's [[bot-architecture]] and [[bot-risks-and-pitfalls]] pages. No raw external source ingested yet.
