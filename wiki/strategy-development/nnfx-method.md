---
title: "NNFX Method (No Nonsense Forex Algorithm)"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [strategy-development, methodology, risk-management, position-sizing, trend-following, indicators, backtesting, forex, crypto]
aliases: ["NNFX", "No Nonsense Forex", "NNFX Algorithm", "NNFX Way", "Baseline C1 C2 Volume Exit"]
related: ["[[stonehill-forex]]", "[[stonehill-forex-nnfx]]", "[[nnfx-crypto-daily-system]]", "[[atr]]", "[[atr-position-sizing]]", "[[atr-trailing-stop]]", "[[trend-following]]", "[[position-sizing]]", "[[mcginley-dynamic]]", "[[schaff-trend-cycle]]", "[[vortex-indicator]]", "[[waddah-attar-explosion]]", "[[choppiness-index]]", "[[repainting]]", "[[overfitting-detection]]", "[[hypothesis-to-backtest-workflow]]", "[[external-strategy-sources]]"]
domain: [strategy-development, risk-management]
prerequisites: ["[[atr]]", "[[moving-averages]]", "[[position-sizing]]", "[[trend-following]]"]
difficulty: intermediate
---

The **NNFX method** ("No Nonsense Forex") is a modular, rules-only template for building a daily-timeframe trend-following system out of interchangeable indicators, each filling a fixed **role**: an [[atr|ATR]] for trade management, a **baseline** for trend direction, two **confirmation** indicators (C1, C2), a **volume/volatility** filter, and an **exit** indicator. It pairs that stack with a fixed money-management scheme — 2% risk split across two orders, a 1.5 x ATR stop, half taken off at 1 x ATR and the rest run to an exit signal. Popularised by the NNFX YouTube channel ("VP") and documented in depth by [[stonehill-forex|Stonehill Forex]], its most transferable idea for crypto is methodological: **test each indicator in isolation, in its role, before assembling the stack** (Source: [[stonehill-forex-nnfx]]).

## Overview

NNFX is less a strategy than a *strategy-assembly protocol*. It assumes (a) no single indicator is reliable, (b) disagreement between indicators of *different types* filters out low-quality signals, and (c) consistent risk per trade plus asymmetric trade management (bank half, run half) does more for survival than entry cleverness. The canonical market is spot FX on the daily chart, with trades placed shortly before the daily close so every decision uses a completed or nearly completed candle. Every component is swappable, which invites optimisation — the method's biggest hazard (see [[#Pitfalls]]).

## The algorithm stack

| Slot | Role | Question it answers | Typical candidates (Stonehill library) |
|---|---|---|---|
| **ATR** | Trade management | How far is "normal" movement? Sets stop, target, size, and the 1 x ATR entry band | [[atr]] (14) |
| **Baseline** | Trend direction + entry band | Which side of the market are we allowed to trade? | [[mcginley-dynamic]], [[kama]], [[hull-moving-average]], [[alma]], [[jurik-moving-average]], [[frama]], [[supersmoother-filter]] |
| **C1** (main confirmation) | Primary entry trigger | Has directional momentum just turned? | [[schaff-trend-cycle]], [[vortex-indicator]], [[aroon]], Fisher transform, zero-lag [[macd]], [[ssl-channel]] (Stonehill profile, 2024), [[qqe]] |
| **C2** (second confirmation) | Agreement filter | Does a *different-type* indicator agree? | Any C1 candidate of a different construction than C1 |
| **Volume / volatility** | "Is there fuel?" filter | Is the market moving enough to follow through, or is it chop? | [[waddah-attar-explosion]], [[choppiness-index]], [[adx]], Williams VIX Fix |
| **Exit** | Close the runner early | Has momentum faded before the baseline breaks? | Fast oscillator, [[chandelier-exit]]-style trail; default = C1 flip |
| Continuation (optional) | Re-entry trigger | Can we re-join an existing trend? | Defaults to C1 |

The "volume" slot rarely uses literal volume in FX (spot FX has no consolidated volume); it is a **volatility / trendiness filter**. In crypto, real exchange volume exists and can be used, but the filter's job is the same.

## Entry rules

All rules are evaluated on **completed daily candles**. "Agrees" means the indicator is currently in the trade's direction; "signals" means it flipped on this candle.

| Entry type | Trigger | Must also hold | Special rule |
|---|---|---|---|
| **Standard** | C1 signals | Baseline agrees, price within 1 x ATR of baseline, C2 agrees, volume agrees | One-candle rule |
| **Baseline cross** | Close crosses the baseline | C1 agrees, within 1 x ATR, C2 agrees, volume agrees | 7-candle rule |
| **Pullback** | Baseline signalled but price closed *beyond* 1 x ATR | Next candle closes back within 1 x ATR with baseline, C1, C2, volume agreeing | Enter on the next candle only |
| **Continuation** | New C1 signal after a prior entry | Baseline has not been crossed since the original entry, baseline agrees, C2 agrees | Ignores 1 x ATR, one-candle rule and volume |

### The 1 x ATR rule

Do not enter when the close is more than one ATR from the baseline — price has already run and the stop (1.5 x ATR) would be stranded far from the structural invalidation point. The pullback entry exists to recover such signals if price comes back.

### The one-candle rule

On standard and baseline-cross entries, the *filters* (C2, volume) may lag the trigger by at most one candle. If they agree on the next candle and price has retraced rather than extended, enter then; otherwise the signal is dead.

### The 7-candle rule ("a bridge too far")

On a baseline-cross entry, C1 must have given its own signal **fewer than 7 candles earlier**. If C1 has been "agreeing" for a week or more, the trend is mature and the baseline cross is late — skip it.

### Continuation trades

Once in a trend (baseline not crossed since the original entry), each new C1 signal in the trend direction is a fresh, fully sized trade even if price is far from the baseline. This is how NNFX pyramids *across* signals rather than adding to a single position.

## Money management and trade management

- **Risk**: 2% of equity per signal, split into **two 1% orders**. Size = `(0.01 x equity) / (1.5 x ATR)` per order ([[atr-position-sizing]]).
- **Stop**: both orders at **1.5 x ATR** from entry.
- **Order 1**: take profit at **1 x ATR** ("half off at TP1").
- **Order 2**: no target. When order 1 fills, move order 2's stop to **breakeven**; common variant trails order 2 at 1.5 x ATR once it is 2 x ATR in profit, ratcheting every further 0.5 x ATR ([[atr-trailing-stop]]).
- **Exit (order 2)**: exit-indicator signal, close across the baseline, or C1 (or C2) flip — whichever comes first. A stop hit closes both.

The arithmetic: a full loss costs 2%; a TP1-then-breakeven trade nets about +0.67% (1 ATR on a 1% order sized for 1.5 ATR); the edge is supposed to come from the minority of runners that travel several ATR. Win-rate therefore overstates quality — Stonehill excludes breakeven "chalk" trades when reporting it (Source: [[stonehill-forex-nnfx]]).

## Trading at the daily close

Decisions are made once a day, just before the daily roll (FX: ~5 pm New York; the NNFX flow chart cites 23:40 broker time). This removes intraday noise and screen time, and makes backtests honest if — and only if — the signal uses the candle *as it will close*. Evaluating at 23:40 on a candle that is not yet final is a small [[lookahead-bias|lookahead]]; a stricter implementation waits for the close and enters on the first minutes of the new candle.

## Exposure and news rules

Two risk rules circulate in NNFX practice (medium confidence; they come from the NNFX community rather than Stonehill's published pages):

- **Correlated-exposure cap** — do not stack the same currency in the same direction (e.g. long EUR/USD and long EUR/JPY both add EUR-long risk); total risk per currency is capped, typically at one trade's 2%.
- **News avoidance** — avoid opening, and in some versions hold, positions through scheduled top-tier releases (central-bank decisions, payrolls) for the affected currency, because gap risk makes the 1.5 x ATR stop meaningless. See [[economic-calendar]].

## Testing an indicator in isolation

The NNFX research loop, as practised by Stonehill, tests **one role at a time** against a fixed harness, so each component's contribution is measurable (Source: [[stonehill-forex-nnfx]]):

1. **Fix the harness** — ATR(14), 2% risk split into two orders, 1.5 x ATR stop (Stonehill uses 1.25–1.5 x per asset), 1 x ATR TP on order 1, daily bars, entry at open of the next period.
2. **Test the C1 alone** — every C1 signal is a trade; exit on the opposite C1 signal or stop. This is the core screen: does the trigger have any edge?
3. **Test the baseline alone** — trade every close across the baseline; exit on the opposite cross.
4. **Test volume / C2 as filters** — add them to a *fixed* C1 and measure whether they improve expectancy by removing more losers than winners. A filter that only reduces trade count is worthless.
5. **Test exits** — hold the entry stack fixed and compare exit indicators by average runner size and giveback.
6. **Use a diverse basket, multi-year** — Stonehill's older baseline was five FX pairs chosen for different behaviour (EUR/USD, AUD/NZD, EUR/GBP, AUD/CAD, CHF/JPY) over several years; the current protocol is 3 years on EUR/USD, BTC/USD, XAU/USD and SPX500.
7. **Default settings first** — report the indicator's un-optimised result before any parameter search.

For crypto, replace the FX basket with a **behaviourally diverse crypto basket** — e.g. BTC (trend leader), ETH (high-beta major), SOL (high-vol L1), a large-cap laggard such as XRP or BNB, and one mid-cap that spent long periods ranging — and use at least one full bull/bear cycle (2020-2026 is available from the backtesting archive). Hold out the most recent 12 months as untouched out-of-sample and apply [[walk-forward-analysis]] to any parameter choice.

## Crypto adaptation

| NNFX (FX) assumption | Crypto adjustment |
|---|---|
| Daily roll at 5 pm New York | Use the **00:00 UTC** daily close (Binance and most perp venues); act on the closed candle, not a forming one |
| Spot FX with swap/rollover | Trade **perpetual futures**; model **funding** as a daily carry cost/credit on every open day ([[funding-rate]], [[crypto-perp-backtesting-pitfalls]]) |
| Weekend gap on Sunday open | **24/7** market — no weekend gap, but weekend candles are thinner; keep them (dropping them breaks ATR and indicator continuity) and be aware of the [[weekend-effect]] |
| 1.5 x ATR stop sized for FX volatility | ATR already scales for volatility, but crypto has fatter tails and deeper intraday wicks: test **2.0 x ATR** stops with 1.0–1.5 x ATR TP1, and cut per-signal risk to **1–1.5%** |
| Currency exposure (don't double up on EUR) | **BTC beta exposure** — most alts have 60-day beta to BTC of ~1.0–1.8; convert each open position's risk to BTC-beta-equivalent risk and cap the same-side total ([[beta]], [[correlation]]) |
| News avoidance (NFP, FOMC) | Avoid entries into FOMC/CPI days, token unlocks, and exchange/regulatory catalysts; use the event calendar and news tape |
| Leverage 20–50:1 | Use modest leverage; liquidation price must sit well beyond the 2 x ATR stop |

**Correlated-exposure rule (crypto).** Compute each position's rolling 60-day beta to BTC. Beta-adjusted risk = `risk_pct x beta`. Cap the sum of beta-adjusted risk on the same side at roughly **3%** (about 1.5 full trades) and total open risk at **6%**. BTC and ETH longs together already consume most of the budget; a third long in an alt only fits if it is sized down.

## Pseudocode

```python
# NNFX decision loop, run once per closed daily candle (00:00 UTC for crypto)
def on_daily_close(sym, bars, book):
    atr   = ATR(bars, 14)[-1]
    base  = BASELINE(bars)              # e.g. McGinley Dynamic
    c1    = C1(bars)                    # returns +1/-1 state series
    c2    = C2(bars)
    vol   = VOLUME_FILTER(bars)         # True if enough "fuel"
    close = bars.close[-1]
    side_base = sign(close - base[-1])
    dist_atr  = abs(close - base[-1]) / atr

    # --- manage open trades first ---
    for t in book.open(sym):
        if exit_signal(bars) or crossed(bars.close, base, against=t.side) \
           or c1[-1] == -t.side or c2[-1] == -t.side:
            book.close(t)                # closes runner (and TP1 order if still open)
        elif t.tp1_filled:
            t.runner_stop = max_favourable(t.runner_stop, t.entry, trail=1.5 * atr,
                                           arm_after=2.0 * atr, step=0.5 * atr)

    if blocked_by_news(sym) or book.has_position(sym):
        return
    side = None
    c1_flip   = c1[-1] != c1[-2]
    base_flip = side_base != sign(bars.close[-2] - base[-2])

    if c1_flip and c1[-1] == side_base and dist_atr <= 1.0:           # standard
        side = c1[-1]
    elif base_flip and c1[-1] == side_base and dist_atr <= 1.0 \
         and bars_since_flip(c1) < 7:                                    # baseline cross + 7-candle rule
        side = side_base
    elif pending_pullback(sym) and dist_atr <= 1.0:                       # pullback, next candle only
        side = side_base
    elif c1_flip and in_trend_since_last_entry(sym, base) and c1[-1] == side_base:
        side = c1[-1]; continuation = True                               # continuation: skips ATR + volume

    if side and c2[-1] == side and (vol or continuation):
        # one-candle rule: if C2/vol fail today, queue a 1-bar retry instead of discarding
        risk_each = 0.01 * book.equity
        if book.beta_adjusted_risk(side) + 2 * risk_each * beta_to_btc(sym) > 0.03 * book.equity:
            return
        qty = risk_each / (1.5 * atr)
        book.open(sym, side, qty, stop=1.5 * atr, tp=1.0 * atr, tag="TP1")
        book.open(sym, side, qty, stop=1.5 * atr, tp=None,     tag="RUNNER")
```

## Pitfalls

- **Combinatorial overfitting** — with 20+ baselines, 50+ confirmations and a dozen volume tools, the search space is enormous; a stack "found" by trying many combinations on the same data is almost certainly curve-fit ([[overfitting-detection]], [[data-snooping-and-p-hacking]], [[curve-fitting]]).
- **Redundant confirmations** — C1 and C2 built from the same input (two MACD variants) add no information; C2 should differ in construction.
- **Repainting indicators** — many library indicators (some ZigZag-, Heikin-Ashi- or centred-window-based) change history; Stonehill's register exists for this reason ([[repainting]]).
- **Short test windows** — 1–3 years on a handful of instruments is far too little to separate skill from regime luck.
- **Cost blindness** — FX tests ignore spread/swap; crypto must add fees, slippage and funding.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — closed daily candles (00:00 UTC) to compute ATR, baseline, C1, C2 and the volatility filter
- `GET /api/v1/market-data/volume-history` — up to 90 days of daily volume and buy ratio for a literal-volume filter
- `GET /api/v1/derivatives/funding-rates` — current perp funding, the carry cost of holding NNFX runners
- `GET /api/v1/volatility/regime/{symbol}` — volatility state as an independent cross-check on the volume/volatility slot
- `GET /api/v1/event/calendar` — scheduled catalysts for the news-avoidance rule

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for multi-year, per-role indicator tests
- `GET /api/v1/backtesting/funding` — historical funding to charge runners realistically
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time universe for survivorship-free baskets

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]], [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the NNFX role-testing loop end to end:

- **Screen one role at a time** — pull `/api/v1/backtesting/klines` daily bars for a 5-asset basket, run each candidate C1 in the fixed harness (1.5–2.0 x ATR stop, two orders), and rank by expectancy *net of fees and funding* from `/api/v1/backtesting/funding`, not by win rate.
- **Hold out and deflate** — reserve the last 12 months, and report how many candidates were tried so the winner's Sharpe can be deflated before promotion.
- **Gate the daily decision** — at 00:00 UTC fetch `/api/v1/market-data/klines` (closed bar only), compute the stack, and veto entries when `/api/v1/event/calendar` shows a high-impact event within 24h.
- **Enforce the beta cap** — before sizing, compute 60-day beta to BTC from the same klines and refuse any order that pushes same-side beta-adjusted risk above the cap.
- **Charge carry on runners** — poll `/api/v1/derivatives/funding-rates` daily for open positions; flag runners whose accrued funding exceeds 0.5 x ATR of profit.

## Related

- [[nnfx-crypto-daily-system]] — one fully specified crypto NNFX configuration
- [[stonehill-forex]] · [[stonehill-forex-nnfx]] — indicator library and testing protocol
- [[atr]] · [[atr-position-sizing]] · [[atr-trailing-stop]] · [[position-sizing]] · [[risk-of-ruin]]
- Baselines: [[mcginley-dynamic]] · [[kama]] · [[hull-moving-average]] · [[alma]] · [[jurik-moving-average]] · [[frama]]
- Confirmations: [[schaff-trend-cycle]] · [[vortex-indicator]] · [[aroon]] · [[macd]]
- Volume/volatility: [[waddah-attar-explosion]] · [[choppiness-index]] · [[adx]]
- Exits: [[chandelier-exit]] · [[trailing-stop]]
- Method: [[hypothesis-to-backtest-workflow]] · [[research-checklist]] · [[overfitting-detection]] · [[walk-forward-analysis]] · [[repainting]] · [[external-strategy-sources]]
- [[triple-screen-system]] · [[turtle-trading]] — other rule-complete trend templates

## Sources

- [[stonehill-forex-nnfx]] — Stonehill Forex indicator library, testing settings and profiles; NNFX flow chart (Rui Silva / nnfxalgotester.com), fetched 2026-09-28
- Crypto adaptation (00:00 UTC close, funding, beta cap, 2.0 x ATR stop) is this wiki's synthesis, not a Stonehill claim, and is untested.
