---
title: "Intrabar Fill Modeling"
type: concept
created: 2026-06-02
updated: 2026-06-21
status: excellent
tags: [backtesting, methodology, market-microstructure, crypto, derivatives, algorithmic]
aliases: ["Intrabar Fills", "Intrabar Order Execution", "Event-Time Backtesting", "Tick Replay"]
domain: [backtesting, market-microstructure]
difficulty: advanced
related: ["[[execution-model-differences]]", "[[bar-resolution-selection]]", "[[microstructure-noise-low-timeframe]]", "[[slippage-modeling]]", "[[lookahead-bias]]", "[[crypto-perp-backtesting-pitfalls]]", "[[multiple-timeframe-analysis]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[scalping]]", "[[backtesting-pitfalls]]", "[[backtesting]]"]
---

# Intrabar Fill Modeling

An OHLCV candle collapses thousands of trades and book updates into four price numbers and one volume figure. At a 1-minute or 5-minute resolution the order in which the High and the Low were reached *inside* the bar is unknowable from the bar alone — and the assumption you silently make about that ordering can flip a backtest from comfortably profitable to clearly losing. For low-timeframe (LTF) crypto-perp strategies, intrabar fill modeling is **the single largest silent inflator of backtested Sharpe**, larger than fee and funding errors combined.

---

## What a Bar Hides

A 1-minute BTC perpetual bar on a venue like [[hyperliquid|Hyperliquid]] routinely contains **hundreds to several thousand** individual trades and an even larger number of order-book updates. Compressing that into `(open, high, low, close, volume)` discards three things that matter for fills:

- **Sequencing** — the chronological order in which prices printed inside the bar.
- **The path** — whether price went Open→High→Low→Close or Open→Low→High→Close, and how many times it oscillated between levels.
- **Available depth** — how much size rested at each price level at each instant, i.e. whether your order could actually have filled there without moving the market.

This is the deeper cousin of "bar magnification" described in [[execution-model-differences]]. That page frames the problem at the daily/heuristic level; here the concern is that at 1m/5m the ambiguity is not an occasional edge case — it is **present on a large fraction of bars**, because tight LTF stops and targets frequently both sit inside a single candle's range.

---

## The Four OHLC Fill Assumptions

Every bar-replay backtester silently encodes an assumption about *where inside the bar* an order fills. The four canonical choices, ordered from most optimistic to most conservative, are:

| Assumption | Fill price used | Bias direction | When (if ever) defensible |
|---|---|---|---|
| Fill at **best** of bar (High for sells, Low for buys) | Most favourable extreme | Wildly optimistic — pure lookahead | Never; this is a bug, not a model |
| Fill at **close** of signal bar | The bar's close | Optimistic — uses the close to act on the close | Never for signals derived from that same close ([[lookahead-bias]]) |
| Fill at **bar open** (next bar) | Open of the bar *after* the signal | Mildly conservative, realistic | Default for daily/swing systems; the standard "signal-on-close, fill-on-next-open" rule |
| Fill at **worst** of bar / stop-first | Most adverse extreme reachable | Conservative | Stress / pessimistic bracket; the floor of plausible outcomes |

The two ambiguous cases that dominate LTF P&L are the **stop-loss** and **take-profit** touches. When *only one* of them lies inside the bar's High–Low range, the fill is unambiguous. The trap is the bar that contains **both** — covered next.

### The OHLC path is unobservable

A single OHLC bar is consistent with two completely different intrabar paths: `O → H → L → C` and `O → L → H → C` (and infinitely many oscillating paths between). For a long position with a stop below and a target above, the first path hits the target first (a win) and the second hits the stop first (a loss) — **the same candle, opposite trade outcomes**. No amount of cleverness recovers the truth from the bar alone; you need higher-resolution data or an explicit assumption.

---

## The H-or-L-First Problem, Quantified

The core ambiguity: when both your stop-loss and your take-profit lie inside one bar's High–Low range, OHLC data cannot tell you which was touched first.

### How the error scales with resolution

The probability that a given bar straddles both your exit levels rises sharply as the timeframe drops, because the bar's range grows with timeframe while your bracket width is fixed by the strategy:

- **1m bars, tight scalp brackets (e.g. ±10–25 bps):** ambiguous *constantly* — a large share of exit bars contain both levels. Nearly every trade's P&L depends on an unobservable ordering.
- **5m bars:** less frequent but still material for sub-50-bps brackets.
- **15m+ bars:** the bar range typically exceeds the bracket, so a bar usually contains only one of the two levels; the ambiguity is comparatively rare.

This is one of the main reasons [[bar-resolution-selection]] is a first-order modeling decision, not a convenience: choosing 1m bars without sub-bar disambiguation builds the ambiguity into every result.

### Honest reporting: bracket both ways

The defensible method is not to pick one heuristic and hope. It is to **bracket** the result:

- **Pessimistic run (stop-first):** whenever a bar contains both levels, assume the stop filled first.
- **Optimistic run (TP-first):** assume the take-profit filled first.

Report both equity curves. The *spread* between them is a direct measure of how much of your edge is real versus an artifact of intrabar ambiguity. If the strategy is only profitable under the optimistic assumption, it has **no demonstrated edge** — the apparent profit lives entirely in the unknowable ordering. A robust LTF strategy should remain profitable, or close to it, under the pessimistic assumption.

### Worked example: the bracket spread as a confidence interval

> Numbers below are illustrative, chosen to show how the bracket exposes phantom edge — they are not the result of a specific backtest.

Consider a 1-minute BTC-perp scalper with a +20 bps target and a −15 bps stop. Over a backtest, 60% of its *exit* bars happen to contain both levels (the bar's range exceeded 35 bps, swallowing the whole bracket).

- **Optimistic run (TP-first on every ambiguous bar):** reported net Sharpe ≈ 1.8, win rate ≈ 64%.
- **Pessimistic run (stop-first on every ambiguous bar):** net Sharpe ≈ −0.4, win rate ≈ 38%.

The truth lies somewhere between, but the *spread* — from clearly profitable to clearly losing — is the headline finding: **the entire apparent edge sits inside the unobservable intrabar ordering.** A strategy with this profile has not been validated and must be re-run on sub-bar data (1s or tick) before any capital decision. Contrast a 15-minute swing system on the same instrument, where bracket width (say 1.5%) usually exceeds the bar range: few bars contain both levels, the optimistic and pessimistic curves nearly coincide, and the bracket spread is small — a sign the result is robust to the ambiguity. This asymmetry is precisely why [[bar-resolution-selection]] is a first-order decision.

---

## Stop/Limit Fill Realism on Perps

Naive backtesters treat every order type as a guaranteed fill the instant price touches the level. On a perp order book this is wrong in two opposite directions.

### Taker (market / stop) orders

Market orders and triggered stops execute by **walking the book**: they consume resting liquidity from best price outward, so the realized average price is worse than the trigger price by an amount that depends on order size relative to available depth. A 1 BTC market order on a thin 1m wick can fill several ticks through the touched price. This must be charged as [[slippage-modeling|slippage]], and it should be **depth-aware** (size-dependent), not a flat constant — a flat 2 bps assumption understates cost during exactly the volatile bars where stops trigger.

### Maker (limit) orders

A resting limit/maker order fills **only if both** of the following happen:

1. Price actually **trades through** your level (a one-tick touch of the wick is *not* the same as trading volume through your price), **and**
2. The **queue ahead of you clears** — every order resting at your price that arrived before yours must be filled first.

Naive backtests assume condition (1) alone and fill the full size immediately on touch. This **massively overstates maker fills**, inflating both fill rate and the favorable maker fee. Two forward concepts correct it:

- **Queue-position / queue-priority modeling:** track how much size sits ahead of you at your price and only fill once that queue has been consumed by trades. A limit that price merely touches but does not trade *through* may never fill at all.
- **Adverse selection:** the limits that *do* fill are disproportionately the ones that fill **right before price moves against you** — you get filled on the buy precisely as the market turns down. Modeling fills without adverse selection systematically over-credits maker strategies.

See [[microstructure-noise-low-timeframe]] for why these effects dominate at the 1m/5m scale.

---

## OHLCV vs Tick vs Event-Time

There are three fidelity levels for resolving what happened inside a bar, in increasing realism and cost:

| Fidelity level | Resolves H-or-L order? | Models queue / adverse selection? | Storage & compute | Typical use |
|---|---|---|---|---|
| (a) Bar replay (1m/5m candles) | No | No | Low | First-pass screening, with explicit bracketing |
| (b) Higher-frequency sub-bars (1s / tick on demand) | Yes | Partially (touch-through only) | Medium | Disambiguate the bars that contain both levels |
| (c) Full event-time (trade + L2 event stream) | Yes | Yes | High | Serious LTF maker / perp research |

A common, cost-efficient hybrid is **signal logic on 1m, fill resolution on 1s/tick** — only drop to higher fidelity for the ambiguous bars, not the whole history.

### (a) Bar replay

Run the backtest directly on 1m/5m candles. **Cheap and fast**, but inherits every ambiguity above. Acceptable only with explicit pessimistic/optimistic bracketing and conservative fill rules.

### (b) Higher-frequency sub-bars

When a 1m bar is ambiguous, **drop to 1s bars or raw ticks for that interval** to recover the actual H-or-L ordering and whether price truly traded through a limit level. This disambiguates the path without committing to a full event-driven engine. A common pattern: signal logic on 1m, fill resolution on 1s/tick. Storage and compute cost rise, but ambiguity collapses.

### (c) Full event-time backtesting

Drive the simulation off the **trade and order-book event stream** itself — process each trade print and book update in timestamp order — rather than off fixed-width candles. The clock advances by *events*, not by wall-clock candles, which matches the bursty, clustered nature of LTF microstructure (long quiet stretches punctuated by dense bursts). This is the only level at which queue position and adverse selection can be modeled faithfully. Per the gap-finder report, event-time replay is **increasingly the standard** for serious LTF perpetual research, with bar replay treated as a rough first pass only (Source: [[2026-04-22-gap-finder-hyperliquid-crypto-perpetual-exchange-lo]]).

---

## Hyperliquid Specifics

Hyperliquid is unusually well-suited to high-fidelity intrabar modeling because it exposes the underlying event stream rather than only candles:

- **L2 order-book snapshots** and a **trades/fills WebSocket** are available, alongside historical data, enabling true **event-time replay** and **queue modeling below the 1-minute scale** — you can reconstruct what depth rested where and what actually traded through (see https://hyperliquid.gitbook.io/hyperliquid-docs).
- Because the order book is **on-chain with deterministic matching**, the matching logic is in principle reconstructable: the same inputs produce the same fills, so a faithful replay can reproduce exchange behavior more closely than on venues with opaque internalization.
- **Funding accrues hourly** and must be applied **mid-hold**, not just netted at entry and exit. A position held across several funding stamps pays/receives at each one; charging funding only once understates cost (or overstates carry) for multi-hour holds. See [[hyperliquid-funding-rate-microstructure]] for the accrual mechanics and [[perpetual-futures]] for the general funding model.

These capabilities mean that on Hyperliquid there is little excuse for a maker-heavy LTF backtest to rely on naive touch-fills — the data to do it properly is published.

---

## Common Intrabar Modeling Errors

| Error | Why it inflates the backtest | Correction |
|---|---|---|
| Fill on the *signal bar's close* | Acts on information from the bar that triggered the signal — [[lookahead-bias]] | Fill no earlier than next bar's open |
| Always assume TP-first on ambiguous bars | Picks the favourable side of an unobservable coin flip | Bracket both ways; report the spread |
| Flat-bps slippage on takers | Understates cost on exactly the volatile bars where stops trigger | Depth-aware, size-dependent [[slippage-modeling\|slippage]] |
| Fill a maker order on a wick *touch* | Price touching ≠ trading *through*; queue may never clear | Require trade-through + queue model + non-fill probability |
| Ignore queue position | Over-credits maker fill rate and the favourable maker fee | Track size resting ahead at your price |
| Ignore adverse selection | The fills you get are the ones that go against you | Penalise filled maker orders that precede adverse moves |
| Net funding once at entry/exit | Misses mid-hold accrual on multi-hour perp positions | Apply funding at each stamp crossed |

---

## A Defensible LTF Fill Protocol

1. **Signals on close, fills on next-bar-open.** Any signal computed from a bar's close fills no earlier than the next bar's open, never at the close that generated it (the LTF version of the rule in [[execution-model-differences]]; guards against [[lookahead-bias]]).
2. **Bracket SL/TP both ways and report the spread.** Run pessimistic (stop-first) and optimistic (TP-first) and publish both curves; treat the gap as a confidence interval on the edge.
3. **Model maker fills with queue + non-fill probability.** Require price to trade *through* your level, account for queue ahead of you, and assign a nonzero probability that a touched limit simply does not fill.
4. **Apply depth-aware slippage to takers.** Charge market/stop orders a size-dependent cost that walks the book, widened on high-range bars.
5. **Resolve ambiguous bars with sub-bar data when the edge is small.** If the optimistic–pessimistic spread is comparable to the claimed edge, drop to 1s/tick or event-time before believing the result.
6. **Never fill a limit at a wick-only price.** A price that only one tick of the wick touched, with no volume trading through, is not a fill — disallow it.

Following all six typically *lowers* a naive LTF backtest's Sharpe substantially. That reduction is not pessimism; it is the removal of phantom edge that would not have survived live execution. See [[crypto-perp-backtesting-pitfalls]] for the broader checklist and [[multiple-timeframe-analysis]] for combining signal and fill timeframes.

---

## Sources

- (Source: [[execution-model-differences]]) — fill-at-close vs next-open, bar magnification, framework defaults, vectorized shift bugs.
- (Source: [[slippage-modeling]]) — depth-aware and size-based cost models.
- (Source: [[2026-04-22-gap-finder-hyperliquid-crypto-perpetual-exchange-lo]]) — event-time replay as emerging standard for LTF perp research; Hyperliquid data-availability gaps.
- Hyperliquid documentation — L2 snapshot feed, trades/fills WebSocket, historical data, on-chain deterministic matching, hourly funding: https://hyperliquid.gitbook.io/hyperliquid-docs

---

## Related

- [[execution-model-differences]]
- [[bar-resolution-selection]]
- [[microstructure-noise-low-timeframe]]
- [[slippage-modeling]]
- [[lookahead-bias]]
- [[backtesting]]
- [[backtesting-pitfalls]]
- [[crypto-perp-backtesting-pitfalls]]
- [[multiple-timeframe-analysis]]
- [[hyperliquid]]
- [[hyperliquid-funding-rate-microstructure]]
- [[perpetual-futures]]
- [[scalping]]
