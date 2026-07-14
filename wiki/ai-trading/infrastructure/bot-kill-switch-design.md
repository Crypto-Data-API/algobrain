---
title: "Bot Kill-Switch Design"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, trading-bots, risk-management, deployment, crypto]
aliases: ["Kill Switch", "Circuit Breaker (Bot)", "Trading Halt", "Global Flatten", "Emergency Stop"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[bot-architecture]]", "[[risk-management]]"]
difficulty: advanced
related:
  - "[[bot-architecture]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[position-reconciliation]]"
  - "[[paper-to-live-promotion]]"
  - "[[deployment]]"
  - "[[risk-management]]"
  - "[[liquidation]]"
  - "[[circuit-breakers]]"
---

# Bot Kill-Switch Design

A bot kill switch is a control path — independent of strategy logic — that can **halt trading and flatten or freeze positions** the instant a defined danger condition is met. It is the single most important piece of a live crypto trading system's safety machinery: strategies fail in ways their authors did not model, and the kill switch is what converts "unbounded runaway loss" into "bounded, contained incident." The canonical cautionary tale is Knight Capital (1 August 2012), whose runaway deployment lost about **$440M in ~45 minutes** with no effective automated stop — the crypto equivalents (a bot looping orders, a hedge leg silently unfilled, a venue feed frozen) happen continuously and 24/7, with no market close to save you.

> **This is a *bot* kill switch — distinct from an *exchange* circuit breaker.** See [Kill switch vs exchange circuit breaker](#kill-switch-vs-exchange-circuit-breaker) below. Your kill switch protects *your* capital; the exchange's protects *the market*, and you cannot rely on the latter to save you (many crypto venues have none).

## Design principles

1. **Independent of strategy code.** The kill path must not depend on the strategy loop being healthy — the most dangerous failures are exactly when the strategy is wedged, looping, or crashed. Run it as a separate supervisor/watchdog process (or thread) with its own connection to the venue.
2. **Fail-safe, not fail-open.** If the watchdog loses contact with the strategy, the market data feed, or the venue, the default action is to **stop and reduce**, never to keep trading blind.
3. **Reduce-only unwind.** When flattening, submit **reduce-only** orders so the unwind can never accidentally *open* new exposure (a plain market sell on a spot-margin or perp account can flip you short). See [Reduce-only unwind](#reduce-only-unwind).
4. **Idempotent and reconciled.** The kill action must be safe to fire twice, and it must confirm the resulting flat state against venue truth (see [[position-reconciliation]]) — "I sent the flatten" is not "I am flat."
5. **Observable and drilled.** Every trigger emits an alert with the reason; the whole path is tested in the [[paper-to-live-promotion|testnet/paper rung]] before any capital.

## Trigger taxonomy

A kill switch is only as good as its trigger set. The five families every crypto bot needs:

| Trigger family | Example condition | Why it matters | Typical action |
|---|---|---|---|
| **Drawdown / P&L** | Realized+unrealized loss > X% of sleeve in a rolling window; daily loss limit; per-position stop | The direct capital-protection trigger | Per-strategy halt → global flatten if severe |
| **Latency** | Order round-trip or signal→ack latency > threshold for K consecutive events | High latency means you are trading on stale state and cannot manage risk in time | Halt new orders; hold/flatten depending on exposure |
| **Data staleness** | No market-data tick / WebSocket heartbeat for > T seconds; timestamp drift | A frozen feed makes every decision blind — the bot thinks the last price is current | Halt immediately; do **not** trade on stale data |
| **Position drift** | Internal position vs venue truth diverges > ε; hedge leg delta drift > threshold | A silent unfilled leg turns "delta-neutral" into a directional bet (top cause of silent live loss) | Halt + reconcile; flatten if reconciliation cannot close the gap |
| **Venue / infra outage** | REST 5xx rate spike, withdrawal halt, exchange maintenance, RPC/builder failure, insurance-fund draw | You cannot manage or exit; counterparty risk is spiking | Freeze; escalate to manual; flatten hedge legs on healthy venues |

Secondary/regime triggers worth wiring in for crypto specifically: a **security/black-swan spike** (hack or depeg event on a held asset), a **funding inversion** for carry strategies, and an **oracle/index vs spot divergence** guard for perp-DEX positions (a basis-blowup kill, as in [[funding-rate-arbitrage]]).

## Scope of the halt: global vs per-strategy

Two levers, used together:

- **Per-strategy halt.** Stops one strategy sleeve and (optionally) flattens only its positions. Correct response to a *local* fault — one strategy's edge decayed, one hedge leg drifted, one venue it uses went down. Keeps the rest of the book running.
- **Global flatten.** Halts *every* strategy and reduces the entire book to flat (or to a defined safe state). Correct response to a *systemic* fault — account-level drawdown breach, a compromised API key, a data-infrastructure outage affecting all strategies, or a security event on a widely-held asset.

Design the switch as a **hierarchy**: a per-strategy trigger halts that strategy; N simultaneous per-strategy halts, or any account-level breach, escalates to global flatten. Make the global switch reachable *manually* by a human with one command (a CLI, a signed Telegram/Discord command, a dashboard button) as well as automatically.

## Auto vs manual

| | Automatic | Manual |
|---|---|---|
| **Best for** | Fast, well-defined, measurable conditions (latency, staleness, drawdown, drift) | Ambiguous or novel situations (a news event, a suspected exploit, "something feels wrong") |
| **Latency** | Milliseconds — the machine wins the race | Seconds-to-minutes — a human is in the loop |
| **Risk** | False positives halt a healthy bot; needs good thresholds/hysteresis | A human may freeze or be asleep — 24/7 crypto has no night shift by default |

Use **both, layered**: automatic triggers for the measurable dangers (they fire faster than any human), plus an always-available manual global switch for everything the trigger set did not anticipate. Add **hysteresis / debounce** to automatic triggers (require K consecutive breaches, not one spike) so a single noisy tick does not needlessly flatten the book — but keep the threshold for catastrophic conditions (data feed dead, key compromised) at a hair-trigger.

## Reduce-only unwind

When the switch flattens, *how* it exits matters as much as *that* it exits:

- **Use reduce-only order flags** so an unwind order can only shrink a position, never open or flip one. On perps (Binance, Bybit, [[hyperliquid]], OKX) this is a native order parameter; on spot, compute the exact sellable balance and never exceed it.
- **Unwind hedges together, not legs-first.** Flattening the spot leg of a delta-neutral pair while leaving the perp short open *creates* a directional position at the worst moment. Either flatten both legs atomically (bundle where possible) or unwind the risk-reducing leg first.
- **Prefer marketable-limit / IOC over naked market orders** in thin books to bound slippage — but in a true emergency (venue about to halt), immediacy beats price.
- **Cancel-all before flatten.** Pull all resting orders first so they cannot fill mid-unwind and re-open exposure.
- **Confirm flat via reconciliation.** Poll venue positions until confirmed flat (or timeout → escalate to manual). See [[position-reconciliation]].

## Kill switch vs exchange circuit breaker

These are routinely confused; they are different mechanisms at different layers:

| | Bot kill switch (this page) | Exchange circuit breaker |
|---|---|---|
| **Owner** | You, the operator | The venue / market |
| **Protects** | *Your* account from *your* bot and *your* risks | *The market* from disorderly moves |
| **Scope** | Your positions only | Every participant in that market |
| **Trigger** | Your drawdown, latency, staleness, drift, outage | Price moves beyond a band in a time window |
| **Action** | Halt your bot; flatten/freeze your positions | Halt or throttle trading; price bands; auction |
| **Crypto reality** | You must build it — no one else will | **Often absent.** Spot crypto has no market-wide halts; perp venues use price bands, funding caps, and auto-deleveraging (ADL) rather than true halts |

Traditional equities have market-wide circuit breakers (e.g., S&P-500 halts at 7% / 13% / 20%) and single-name limit-up/limit-down. Crypto spot has essentially **none** — BTC can fall 20% in an hour with markets fully open, as on 2020's "Black Thursday" (12 March 2020) and the 10 October 2025 cascade. Perp venues substitute price bands, funding-rate caps, and **auto-deleveraging** (forcibly closing profitable counterparties to cover a bankrupt one) — mechanisms that protect the *exchange's* solvency, sometimes at your expense. The lesson: **assume no venue safety net exists; your kill switch is the only circuit breaker you control.**

## Reference watchdog (pseudocode)

```python
# watchdog.py — supervisor independent of the strategy loop
import time

THRESH = {
    "drawdown_global": 0.10,      # 10% account drawdown -> global flatten
    "drawdown_sleeve": 0.05,      # 5% per-strategy -> halt that sleeve
    "data_stale_s":    5.0,       # no tick for 5s -> halt (blind)
    "latency_ms":      750,       # order RTT > 750ms for K events -> halt
    "drift_bps":       50,        # internal vs venue position drift -> halt+reconcile
    "latency_k":       3,         # debounce: consecutive breaches required
}

def watchdog_tick(state):
    now = time.time()

    # --- fail-safe: lost contact with strategy or feed => stop and reduce ---
    if now - state.last_strategy_heartbeat > 10 or now - state.last_md_tick > THRESH["data_stale_s"]:
        return fire("GLOBAL_FLATTEN", "strategy/feed heartbeat lost — trading blind")

    # --- account-level (global) triggers ---
    if state.account_drawdown > THRESH["drawdown_global"]:
        return fire("GLOBAL_FLATTEN", f"account drawdown {state.account_drawdown:.1%}")
    if state.api_key_compromise_flag or state.security_event_on_held_asset:
        return fire("GLOBAL_FLATTEN", "counterparty/security event")

    # --- per-strategy triggers ---
    for s in state.sleeves:
        if s.drawdown > THRESH["drawdown_sleeve"]:
            fire("HALT_SLEEVE", f"{s.name} drawdown {s.drawdown:.1%}", sleeve=s)
        if s.position_drift_bps > THRESH["drift_bps"]:
            fire("HALT_SLEEVE_RECONCILE", f"{s.name} position drift", sleeve=s)
        if s.consec_latency_breaches >= THRESH["latency_k"]:
            fire("HALT_SLEEVE", f"{s.name} latency degraded", sleeve=s)

    # --- escalation: many local halts => systemic => go global ---
    if sum(1 for s in state.sleeves if s.halted) >= state.escalation_count:
        return fire("GLOBAL_FLATTEN", "multiple simultaneous sleeve halts")

def fire(action, reason, sleeve=None):
    alert(reason)                              # emit to Telegram/PagerDuty with reason
    cancel_all_orders(scope=sleeve)            # pull resting orders first
    flatten(scope=sleeve, reduce_only=True)    # reduce-only unwind
    confirm_flat_or_escalate(scope=sleeve)     # reconcile vs venue truth; else page a human
    set_state(action, reason)                  # idempotent, logged
```

## Common mistakes

- **Kill logic inside the strategy loop** — dies exactly when you need it (the wedged/looping strategy cannot stop itself).
- **Flatten with plain market orders** — no reduce-only flag flips positions or over-sells; no cancel-all first lets resting orders re-open exposure.
- **"Sent" treated as "done"** — not reconciling the post-kill state leaves you thinking you are flat when a leg is still open.
- **No manual override** — automatic triggers cannot anticipate every event; a human needs a one-command global stop.
- **Never drilled** — a kill switch first exercised during a real incident is a kill switch you are debugging during a fire. Drill it in the [[paper-to-live-promotion|paper rung]].
- **Relying on the exchange** — assuming a venue halt will save you; most crypto venues have none.

## Getting the Data (CryptoDataAPI)

A watchdog's *data-staleness* and *venue-health* triggers can cross-check an independent feed's liveness, and its *security* trigger can consume a black-swan signal:

- `GET /api/v1/health` — basic liveness check (no auth); a dead upstream is a staleness corroborator
- `GET /api/v1/market-intelligence/status` — collector status + rate usage (independent feed-health signal)
- `GET /api/v1/security/regime` — recent hacks/depegs + Security Stress score (feeds a security/black-swan global-flatten trigger)
- `GET /api/v1/security/events` — filterable recent security events (10d lookback) for a held-asset check

```bash
curl "https://cryptodataapi.com/api/v1/health"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/security/regime"
```

Auth: `X-API-Key` header (the `/health` endpoint needs none). Catalogs: [[cryptodataapi-market-intelligence]], [[cryptodataapi-regimes]].

## Related

- [[bot-architecture]] — the kill switch is the risk-manager's hard backstop
- [[bot-risks-and-pitfalls]] — the runaway-bot and stale-data failures this prevents
- [[position-reconciliation]] — how a flatten is *confirmed* and how drift is detected
- [[paper-to-live-promotion]] — where the switch is drilled before capital
- [[deployment]] — production reliability context
- [[risk-management]] — pre-trade limits that complement the post-trade kill
- [[liquidation]] — what an unmanaged position runs into; ADL is the venue's version
- [[funding-rate-arbitrage]] — a strategy whose oracle-divergence and funding-flip kills are concrete instances of this design

## Sources

- Knight Capital Group trading incident, 1 August 2012 (~$440M loss, runaway deployment) — canonical kill-switch cautionary tale.
- General knowledge of production trading-system safety engineering; synthesized with this wiki's [[bot-risks-and-pitfalls]] and [[bot-architecture]] pages. No raw external source ingested yet.
