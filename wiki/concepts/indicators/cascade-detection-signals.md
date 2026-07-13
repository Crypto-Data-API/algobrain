---
title: "Cascade Detection Signals"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [crypto, indicators, liquidations, market-microstructure, cascade, signals, hyperliquid]
aliases: ["Liquidation Cascade Indicators", "Cascade Early Warning Signals"]
related: ["[[liquidation-cascade-fade]]", "[[liquidation-cascade-arbitrage]]", "[[hlp-cascade-alongside-playbook]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-oracle-mechanics]]", "[[order-flow-analysis]]", "[[cumulative-volume-delta]]", "[[funding-rate]]", "[[mark-price]]", "[[hypurrscan]]"]
domain: [indicators, market-microstructure]
prerequisites: ["[[perpetual-futures]]", "[[liquidation]]"]
difficulty: advanced
---

# Cascade Detection Signals

**Cascade detection** is the practice of identifying — in real time — when a perpetual-futures market is approaching, entering, or actively in a forced-liquidation cascade. The same primitives serve three different operators: a [[liquidation-cascade-arbitrage|keeper bot]] that wants to be first to call `liquidate()` once positions go underwater, a [[liquidation-cascade-fade|fade trader]] that wants to be the patient bid at the exhaustion point, and a [[hyperliquid-hlp-basis-arbitrage|HLP-aware passive operator]] that needs to know whether to leave deposits in the vault or pull them ahead of an in-progress flush. Detection is fundamentally a tradeoff between *recall* (don't miss the cascade) and *precision* (don't fire on every wiggle), and the right operating point depends entirely on what you do with the signal.

This page catalogs the data sources, the three-stage signal hierarchy (early warning → confirmation → exit), concrete numerical thresholds drawn from observed cascades on [[binance]], [[bybit]], OKX, [[hyperliquid]], [[gmx]], and dYdX, and a Python-sketch detector that emits `PRE-CASCADE / IMMINENT / IN-CASCADE` levels. It is designed to be implementation-faithful for someone running cascade-follower or HLP-aware strategies on [[hyperliquid]] (and adaptable to centralized venues).

## The Three-Stage Signal Hierarchy

Cascades do not appear from nowhere. The leveraged-long book accumulates over hours-to-days, becomes brittle, and then snaps in seconds-to-minutes when a trigger arrives. Detection signals divide cleanly into three temporal stages:

| Stage | Lookahead | Goal | False-positive cost | Signal density |
|-------|-----------|------|---------------------|----------------|
| **Pre-cascade** (early warning) | 30 min – 24 h | Reduce position, stage capital, raise alert level | Low — false positives just keep you alert | Several alerts per week in active markets |
| **Cascade-imminent** (confirmation) | 0 – 15 min | Pre-stage entry orders, keeper inventory, withdraw HLP if lockup permits | Medium — false positives waste prep work | A few per week |
| **In-cascade** (live) | Right now | Pull the trigger — long the perp, fire `liquidate()`, stop further deposits | High — false positives mean you're catching a trending knife | A handful per quarter |

Each stage has different data requirements and different latency budgets. A **passive HLP depositor** can poll every 30 seconds and only cares about pre-cascade and cascade-imminent. A **fade trader** needs sub-second cascade-imminent and in-cascade detection. A **keeper bot** needs sub-100ms tick-level detection because the bonus goes to whoever lands the transaction first.

The architecture below treats the three stages as a state machine: a signal at one level *arms* the detectors at the next level, with thresholds tightening as the cascade approaches.

### Master signal reference

Every signal in this page, with its computation, threshold, stage, and feed. Use it as the index; each row is detailed in the section named in the last column. Funding/OI/liquidation/mark feeds are available cross-venue through aggregators such as [[coinglass]] and cryptodataapi.com, but in-cascade and keeper consumers must use native exchange websockets for latency.

| Signal | Computed from | Threshold | Stage | Section |
|--------|---------------|-----------|-------|---------|
| Funding extreme | [[funding-rate]] sustained premium | > 0.05%/8h (CEX) / > 0.006%/h (HL), 24h | Pre-cascade | Funding Rate Extremes |
| OI at highs | [[open-interest]] percentile + growth | OI > 90d P95 + OI growth > 20%/7d | Pre-cascade | OI at Multi-Month Highs |
| Long/short skew | Exchange L/S ratio | > 1.7 (long-cascade) / < 0.6 (short) | Pre-cascade | Long/Short Ratio Extremes |
| Mark-oracle drift | `(mark − oracle)/oracle`, 1h mean | > 15 bp, gap widening | Pre-cascade | Mark-Oracle Deviation Drift |
| HLP per-pair exposure | HLP position on-chain | > $20M or > 30% HLP TVL on small pairs | Pre-cascade | HL-Specific: HLP Exposure |
| Leverage health composite | weighted blend (above) | > 70 fragile, > 85 imminent-given-trigger | Pre-cascade | Leverage Health Composite |
| Liquidation count spike | 1-min liq notional vs 24h percentile | > 24h P99 (1m) AND > P95 (5m) | Imminent | Liquidation Count Spike |
| Funding snap | Δ predicted funding | \|Δ\|/\|predicted\| > 0.5 in 5 min | Imminent | Funding Rate Snap |
| Spot-perp basis | `(perp − spot)/spot` | > 30 bp (majors) / > 75 bp (alts) | Imminent | Spot-Perp Basis Dislocation |
| CEX-DEX divergence | \|HL mark − Binance mark\| | > 30 bp for 60+ s | Imminent | CEX-DEX Price Divergence |
| Mark-oracle acute | deviation jump | > 20 bp with 1-min Δ > 10 bp | Imminent | Mark-Oracle Deviation Acute |
| Liq tape + price drop | 5-min liq vs 24h mean + 15-min return | ≥ 3.0× mean AND ≥ 2.0% drop | In-cascade | Liquidation Tape > 3× |
| CVD exhaustion | [[cumulative-volume-delta]] slope ratio | recent slope ≤ 0.3× prior slope | In-cascade | CVD Crossing Zero |
| Depth withdrawal / refill | top-of-book bid depth vs 1h median | collapse to 10-30%; refill > 50% | In-cascade | Spread Snapback / MM Refill |
| Mark-oracle (HL exhaustion) | deviation during cascade | > 50 bp (HL only) | In-cascade | Mark-Oracle Deviation > 50 bp |

## Pre-Cascade Signals (Early Warning, 30 min – 24 h Ahead)

Pre-cascade is about **book fragility** — measuring how much leveraged long inventory has accumulated and how much pain a small price move would inflict. None of these are real-time cascade triggers; they are conditions that *make* a cascade more likely if a trigger arrives.

### Funding Rate Extremes

[[funding-rate|Funding]] is the cleanest measure of leveraged-long pressure. When perps trade at a sustained premium to spot, longs pay shorts every funding interval, and the size of that payment compounds the cost of holding. Persistent positive funding means the marginal long is paying 30-100% APR equivalent for the leverage — a population that is by definition more fragile than a balanced book.

**Concrete thresholds:**

- **Binance / Bybit / OKX:** funding rate **> 0.05% per 8h** (≈ 0.15% per day, ≈ 55% APR) sustained for **24+ hours** on BTC or ETH perp.
- **Hyperliquid:** Hyperliquid uses 1-hour funding intervals. Equivalent threshold is **> 0.006% per hour** sustained for 24+ hours.
- **Memecoin / long-tail perps:** thresholds are 2-5× higher because base funding volatility is higher; flag when funding exceeds the trailing 30-day 95th percentile.

**Why it matters:** funding is a price for leverage. A market clearing at 55% APR for leverage is one where the marginal long is expecting >55% gross returns or is mispricing risk. Either way, a small adverse move clears them.

### Open Interest at Multi-Month Highs

[[open-interest]] measures total notional locked in perp positions. OI alone is not a signal — large markets have large OI — but **OI at a multi-month high while price is grinding up on low volume** is the textbook setup for a cascade.

**Threshold:** OI > trailing 90-day 95th percentile, with concurrent **volume-weighted OI growth > 20% in 7 days**. The combination of high OI plus rapid OI growth implies the new positions are *late-cycle* — entered into a strong-uptrend regime, with stops clustered just below recent support.

**Hyperliquid-specific:** Hyperliquid's [[hypurrscan]] dashboard exposes per-pair OI in real time. Watch the OI/volume ratio: when OI grows much faster than spot volume, you have leveraged positions accumulating without underlying demand to support them.

### Long/Short Ratio Extremes

The exchange-published long/short ratio (taker-side or position-side) is a coarse but useful tell. **Extreme one-sidedness is the precondition for a one-sided liquidation cascade.**

**Thresholds:**

- **Long-cascade risk:** long/short ratio > **1.7** sustained for several hours on top traders' positions.
- **Short-cascade risk:** long/short ratio < **0.6** sustained — rarer but produces violent up-cascades (see e.g. SHIB/PEPE squeeze events).

**Caveat:** the public long/short ratio is gameable and exchanges report it inconsistently. Cross-reference with funding and OI; do not act on long/short alone.

### Liquidation Clustering (Spatial — Where the Fuel Sits)

Distinct from the *temporal* liquidation-count spike (an imminent signal) is the *spatial* clustering of liquidation prices: **where** in price the forced-sell fuel is concentrated. Estimated liquidation levels, aggregated across leverage tiers, form a [[liquidation-heatmap|liquidation heatmap]]. A dense cluster just below current price is the precondition that turns an ordinary dip into a cascade — once price reaches the cluster, each liquidation pushes price into the next, a reflexive chain.

**Computation:** for each open position (or, where positions are not observable, for each leverage tier and entry-price bucket), the liquidation price is `entry × (1 − 1/leverage ± maintenance_margin)`. Summing notional by price bucket yields the cluster map.

- **CEXs:** positions are not individually visible; aggregators ([[coinglass]], cryptodataapi.com) estimate clusters from OI, leverage distribution, and price history.
- **[[hyperliquid]]:** the transparent CLOB and on-chain positions make clustering **directly computable** rather than estimated — every position's liquidation price is derivable. This is the structural reason the [[hyperliquid-perp-trading-map]] calls liquidation-heatmap front-running an HL-specific edge.

**Threshold (pre-cascade flag):** a single price bucket within 2-3% of spot holding > 5% of total pair OI in estimated liquidations. The denser and closer the cluster, the more inevitable the cascade once price approaches it. See [[stop-hunting-and-liquidity-sweeps]] for how this is weaponized.

### Mark-Oracle Deviation Drift

Modern liquidation engines trigger on **mark price**, not last-trade. See [[mark-price]] and [[hyperliquid-oracle-mechanics]]. The mark price is computed from a weighted oracle of multiple venues; when the perp price drifts above the oracle median, longs are temporarily *over-marked* — their positions look healthier than they are. When the gap closes (which it always does), the snap can trigger liquidations.

**Threshold:** rolling 1-hour mean of (perp mark − oracle index) **> 15 bps** with the gap *widening* on a 15-minute basis. This is mostly a Hyperliquid / on-chain signal because CEX mark and last are usually within 1-3 bps; on Hyperliquid where oracle updates lag fastest CEX prints, gaps of 20-50 bps appear during fast tape.

### HL-Specific: HLP Per-Pair Exposure

Hyperliquid's [[hyperliquid-hlp-basis-arbitrage|HLP vault]] is the protocol's automated market maker and liquidator. Its per-pair position is publicly observable via the Hyperliquid SDK and on [[hypurrscan]]. When HLP accumulates large directional exposure on a single pair — typically because it is absorbing one-sided retail flow — it becomes the *next* counterparty to liquidate if the move continues.

**Threshold:** **HLP exposure on a single pair > $20M** (or > 30% of HLP TVL on small pairs) flags as pre-cascade. The JELLYJELLY incident (March 2025) illustrated this precisely: HLP accumulated a forced ~$13M position because the pair was thin and one-sided, then a coordinated push tested its solvency.

### Leverage Health Composite

A useful pre-cascade summary is the **leverage health score** — a 0-100 index combining funding (40% weight), OI percentile (30%), long/short skew (20%), and HLP single-pair concentration (10%). Above 70, the book is fragile; above 85, expect a cascade within 24 hours given any trigger.

## Cascade-Imminent Signals (0 – 15 Minutes Ahead)

Cascade-imminent signals fire when the trigger has arrived and the engine is *about* to start firing — but the bulk of liquidations have not yet executed. This is the window where you stage entry orders, top up keeper gas, and decide whether to pull HLP deposits (lockup permitting).

### Liquidation Count Spike vs Trailing 24h Percentile

The single most reliable imminent signal is **a 1-minute liquidation count or notional > the trailing 24h 99th percentile**. The 24h percentile is critical: a static threshold (e.g. "10 liquidations per minute") is wrong for low-vol regimes (always firing) and wrong for high-vol regimes (never firing). Percentile-relative thresholds normalize across regimes.

**Operational rule:** flag when the trailing 1-minute liquidation notional **> trailing 24h P99**, *and* the prior 5-minute total **> trailing 24h P95**. The double threshold filters single-print anomalies (one $5M position liquidating doesn't make a cascade) from genuine cluster events.

**Per-venue feeds:**

- **Binance:** WebSocket `forceOrder@arr` channel — every executed liquidation in real time.
- **Bybit:** `liquidation` topic on the WebSocket v5 API.
- **OKX:** `liquidation-orders` channel.
- **Hyperliquid:** `userEvents` subscription returns liquidation events; also queryable via `info` HTTP API.
- **Aggregated:** Coinglass exposes a unified liquidation feed but with **30-90 second delay** — fine for pre-cascade monitoring, too slow for imminent / in-cascade decisions.

### Funding Rate Snap

Funding can change abruptly when an exchange's interval ticks during fast tape. A **sudden change in the predicted next-funding rate of > 50% relative** (e.g., predicted next funding moves from +0.012% to +0.020%) is a tell that perps are trading at a much wider premium than they were a few minutes ago.

**Threshold:** for Hyperliquid (1-hour intervals), watch the predicted-funding update each minute; flag when |Δ predicted| / |predicted| > 0.5 within 5 minutes.

### Spot-Perp Basis Dislocation

Healthy perps trade within ±5 bps of spot index. When the perp price diverges sharply from spot — perp running ahead in an up-move, perp dropping below in a down-move — the basis becomes a confirmation signal that derivative pricing is leading spot pricing, which is often the *start* of a cascade.

**Threshold:** instantaneous (perp mark − spot index) / spot index **> 30 bps** on BTC/ETH or **> 75 bps** on alts. On Hyperliquid this is enriched by checking against [[binance]] and [[coinbase]] spot indices simultaneously.

### CEX-DEX Price Divergence

For markets that trade both on CEX and on Hyperliquid / dYdX / [[gmx]], a divergence between the venues is itself an imminent signal. DEXs have thinner books and thinner cross-venue arb during fast tape; a 30-50 bps divergence between Hyperliquid mark and Binance index typically indicates either (a) Hyperliquid is leading the cascade, or (b) the arb desks have stepped away because volatility has spiked.

**Threshold:** |HL mark − Binance mark| > **30 bps** sustained for 60+ seconds.

### Mark-Oracle Deviation Acute

The pre-cascade *drift* signal becomes the imminent *acute* signal when deviation jumps. **Mark-oracle deviation > 20 bps with 1-minute Δ > 10 bps** indicates that the oracle is catching up to a fast price move — and the catch-up itself will trigger liquidations.

## In-Cascade Signals (Live, Entry Triggers for the Fade)

These are the triggers consumed by [[liquidation-cascade-fade]]. They confirm that a cascade is not just imminent but *currently executing*, and they identify the exhaustion point where the patient-bid trade enters.

### Liquidation Tape > 3× 24h Average AND Price Drop > 2% in 15 min

This is the canonical fade entry condition (see [[liquidation-cascade-fade]] frontmatter). Both clauses must hold:

1. Trailing 5-minute liquidation notional ≥ **3.0× trailing 24-hour rolling mean**, **AND**
2. Mark price has fallen ≥ **2.0%** in the trailing 15 minutes.

Either alone is insufficient. Liquidation spikes without price drops happen during venue-specific anomalies (one large position liquidating in isolation). Price drops without liquidation spikes are simple downtrends with no forced-supply overshoot — not a fade setup.

### Open-Interest / Price Divergence (Forced-Closing Signature)

The cleanest confirmation that a price drop is a *forced-liquidation* cascade (not ordinary selling) is **[[open-interest]] falling in lockstep with price**. When longs are force-closed, their positions are extinguished — OI drops. Ordinary bearish selling that opens new shorts *raises* OI. So the cascade signature is: **price down AND OI down simultaneously**.

**Computation:** track 5-minute Δprice and 5-minute ΔOI per pair. The forced-closing flag fires when both are negative and the OI drop is steep:

```
oi_drop_pct   = (oi[t-5m] - oi[t]) / oi[t-5m]
price_drop_pct = (px[t-5m] - px[t]) / px[t-5m]
forced_closing = (price_drop_pct > 0.01) and (oi_drop_pct > 0.02)
```

**Threshold:** OI drop > 2% in 5 minutes concurrent with price drop > 1% in 5 minutes. The **exhaustion** read is the inverse: when the OI-drop *rate* decelerates (Δ²OI flattens) while price is still soft, the forced-selling pool is draining — the cascade is approaching its low. This is the [[open-interest]]-based analog of the [[cumulative-volume-delta|CVD]]-flatten signal below, and is the primary exhaustion tell used in the [[hyperliquid-perp-trading-map]] stop-hunting playbook and [[stop-hunting-and-liquidity-sweeps]].

**Caveat:** OI prints lag liquidation prints on most venues by seconds-to-minutes; use it as confirmation of an in-progress cascade, not as the first trigger. On [[hyperliquid]], per-pair OI is observable in near-real-time via [[hypurrscan]] and the native SDK, making the divergence sharper than on CEXs.

### CVD Crossing Zero / Selling Exhaustion

[[cumulative-volume-delta|Cumulative Volume Delta]] is the running sum of taker-buy minus taker-sell volume. During a cascade, CVD plunges as aggressive selling dominates. The exhaustion signal is when **the slope of CVD flattens** — selling pressure decelerating — which mathematically precedes price recovery by seconds-to-minutes.

**Threshold:** the absolute slope of the most recent 30-second CVD window ≤ **0.3×** the absolute slope of the prior 30-second window. See [[order-flow-analysis]] for the underlying intuition.

A more aggressive variant: CVD *crosses zero* on a 5-minute basis (taker buys overtake taker sells) — this is the classical Wyckoff "selling climax → spring" archetype in modern microstructure terms.

### Depth Withdrawal and Spread Snapback / Market-Maker Refill

Order-book depth has two distinct cascade signatures, and both are computable from the same feed.

**Depth withdrawal (in-cascade confirmation).** As the cascade fires, market makers pull quotes and bid-side depth collapses. Compute bid depth within a fixed band (e.g. -10 bp from mid) and compare to its trailing 1-hour median:

```
bid_depth_ratio = bid_depth(-10bp, now) / median_1h(bid_depth(-10bp))
depth_withdrawn = bid_depth_ratio < 0.30
```

**Threshold:** bid-side depth at -10 bp **collapses to 10-30% of trailing 1-hour median** during the flush. Sudden simultaneous withdrawal of large resting limit orders (visible on [[hyperliquid]]'s transparent CLOB) is itself a *pre-cascade-to-imminent* tell — MMs stepping away ahead of a move they expect.

**Spread snapback / refill (exhaustion signal).** When MMs return — spread compresses and bid depth restores — the cascade is functionally over even if the tape is still volatile.

**Threshold:** top-of-book spread returns to within 2× its trailing 1-hour median, AND bid-side depth at -10 bps recovers to > 50% of trailing 1-hour median. The withdrawal→refill transition (depth_ratio crossing back above ~0.5) is one of the most reliable exhaustion confirmations, pairing well with the [[cumulative-volume-delta|CVD]] flatten and the [[open-interest]]-deceleration signals above.

### Mark-Oracle Deviation > 50 bps (Hyperliquid)

On Hyperliquid specifically, a mark-oracle deviation > 50 bps during a cascade is *the* signal that the oracle has stopped tracking the cascade — i.e., the engine has caught up and the next oracle tick will not trigger more liquidations. This is venue-specific to on-chain perps with discrete oracle updates; CEXs are not subject to this dynamic.

## Data Sources

Practical detection requires combining multiple feeds. The table below maps signal type to source and noting cost and latency.

| Source | Coverage | Latency | Cost | Best for |
|--------|----------|---------|------|----------|
| **Hyperliquid native API / WS** | Hyperliquid markets, orderbook, liquidations, HLP | 100-300ms (WS) | Free | All HL signals |
| **HypurrScan** | HL on-chain analytics, vault flows, whale tracking | 1-5s | Free / paid tiers | Pre-cascade, HLP exposure |
| **Binance WS** (`forceOrder`) | Binance perp liquidations | <100ms | Free (rate-limited) | CEX cascade-imminent and in-cascade |
| **Bybit WS** (`liquidation`) | Bybit perp liquidations | <100ms | Free | CEX confirmation |
| **OKX WS** (`liquidation-orders`) | OKX perp liquidations | <100ms | Free | CEX confirmation |
| **Coinglass aggregator API** | All major CEX liquidations, OI, funding | 30-90s | Free / paid | Pre-cascade context, backfill |
| **TheGraph subgraphs** | On-chain lending positions ([[aave]], [[compound]], MakerDAO) | Block-level (12s ETH) | Free / paid | Lending cascade (see [[liquidation-cascade-arbitrage]]) |
| **Chainlink / Pyth feed listeners** | Oracle price updates | Per-update | Free (RPC) | Pre-empt mark price moves |
| **Mempool subscriptions** (Flashbots, BloXroute) | Pending oracle updates, pending liquidations | <500ms | Paid | Keeper bot edge |
| **Direct exchange index price API** | CEX index price for basis calculation | 100-500ms | Free | Spot-perp dislocation |

A minimal viable detector for a fade trader needs: native exchange WS for liquidations + tick CVD, exchange mark/last/index, and a percentile tracker. Total cost: free, total infrastructure: one VPS, a few Python processes, and a Redis instance for the rolling windows.

A keeper-bot detector adds: mempool subscription, oracle update listener, position-graph subgraph, and ideally co-location with the validator/sequencer. Cost: $1k-$10k/month.

## Signal Latency Budget

Latency budget depends entirely on the consumer:

- **Keeper bot (calling `liquidate()`):** target end-to-end latency **< 100ms** — oracle update arrives, you have ~1-2 blocks (12-24s on ETH, 1-2s on Hyperliquid) to land the transaction before competitors. On L1s with sub-second blocks, this is sub-100ms or you lose. Co-location with sequencers is standard.
- **Fade trader (entering long perp):** target latency **< 1 second** from CVD-flatten signal to limit order. Budget: 200ms feed-to-detector, 200ms detector decision, 300ms order routing, 300ms slack. Above 1 second, you're catching the snapback after it's started.
- **HLP-aware passive (just monitoring):** **30-second polling fine**. The decision (pull deposits or not) takes longer than detection, and HLP withdrawal lockups dominate the latency budget anyway.
- **Risk dashboard / alerting:** 5-30 second polling sufficient. The signal is for human consumption.

Match infrastructure to consumer. Running a co-located keeper stack to drive a manual fade trade is wasteful; running 30-second polling for a keeper bot is fatal.

## False-Positive Management

Most "cascade-imminent" signals do not result in cascades. Empirically, on BTC perp aggregated across major venues:

- **Pre-cascade signals fire** ~5-15 times per week.
- **Cascade-imminent signals fire** ~1-3 times per week.
- **Genuine cascades** (>2% drop in 15 min with >3× liq spike) occur ~1-4 times per quarter.

This means cascade-imminent signal precision is roughly **5-20%** at typical thresholds — most of the time it fires, no cascade follows. Threshold tuning is a recall/precision tradeoff:

- **Tighter thresholds** (e.g., 4× liq spike instead of 3×) raise precision but miss small cascades. Acceptable for fade traders, who have other opportunities.
- **Looser thresholds** raise recall — never miss a cascade — but every cascade you trade pays for many false positives. Acceptable for keepers, where the cost of a false-positive alert is near zero (you check, find no underwater position, do nothing).

**Backtest discipline:** validate thresholds against historical cascades. The canonical events:

| Date | Event | Drop | Liquidations | Notes |
|------|-------|------|--------------|-------|
| 2020-03-12 | Black Thursday | BTC -50% in 24h | $1.4B | BitMEX engine simple; cascade extreme; see [[2020-03-12-black-thursday-crypto]] |
| 2021-05-19 | China ban | BTC -30% intraday | $8B | Binance went down |
| 2022-05-08 to 12 | LUNA / UST | BTC -20% over week | ~$10B | Cascade-fade *failure* case; see [[2022-05-terra-luna-depeg-arb]] |
| 2022-06-11 to 15 | stETH depeg, 3AC | ETH -25% | ~$2B | See [[2022-06-steth-depeg]] |
| 2024-03-12 | HL mass liquidations | varied | ~$300M HL alone | First major Hyperliquid cascade test |
| 2024-08-05 | Yen carry unwind | BTC -16% | $1.05B | Modal cascade; clean fade trade |
| 2025-02-03 | Trump tariff weekend | BTC -8% | ~$2B | Small fast cascade |
| 2025-10-10 | China 100% tariff | BTC <$90k | $19B over 36h, $3.21B in 60s | Largest-ever single-window flush |

A detector is worth deploying when its threshold combination correctly fires `IN-CASCADE` for ≥ 80% of these events within 60 seconds of the cascade start, while firing `IN-CASCADE` no more than ~5 times per quarter outside of cascades.

**Survivorship caveat:** this list is the cascades we know about. Detectors tuned on these events may overfit; out-of-sample cascades on new venues (Hyperliquid post-2024, future on-chain perp DEXs) may have different microstructure. Re-tune annually.

## Python Sketch — Three-Stage Cascade Detector

```python
# Cascade detector: emits PRE-CASCADE / IMMINENT / IN-CASCADE signals.
# Adapts the [[liquidation-cascade-fade]] entry logic into a state machine
# usable by keepers, fade traders, and HLP-aware operators.

from collections import deque
from enum import Enum
import numpy as np
import time

class Stage(Enum):
    QUIET       = 0
    PRE_CASCADE = 1
    IMMINENT    = 2
    IN_CASCADE  = 3

class CascadeDetector:
    # Pre-cascade thresholds
    FUNDING_HIGH_8H        = 0.0005    # 0.05% per 8h
    FUNDING_HIGH_HOURS     = 24
    OI_PERCENTILE          = 0.95
    LONG_SHORT_RATIO_HIGH  = 1.7
    HLP_EXPOSURE_USD       = 20_000_000
    MARK_ORACLE_DRIFT_BPS  = 15

    # Imminent thresholds
    LIQ_1MIN_PERCENTILE    = 0.99
    LIQ_5MIN_PERCENTILE    = 0.95
    BASIS_DISLOCATION_BPS  = 30
    CEX_DEX_DIVERGENCE_BPS = 30
    MARK_ORACLE_ACUTE_BPS  = 20

    # In-cascade thresholds (fade entry)
    LIQ_SPIKE_MULTIPLIER   = 3.0       # 5min liq vs 24h mean
    PRICE_DROP_PCT         = 0.02      # 2% in 15min
    CVD_FLATTEN_RATIO      = 0.3
    MARK_ORACLE_HL_BPS     = 50

    def __init__(self, symbol):
        self.symbol = symbol
        self.stage = Stage.QUIET
        # Rolling windows
        self.liq_1min = deque(maxlen=24 * 60)        # for percentile
        self.liq_5min = deque(maxlen=12 * 24)        # for percentile
        self.oi_history = deque(maxlen=90 * 24)       # 90d hourly
        self.prices_15m = deque(maxlen=15 * 60)       # 1s samples
        self.cvd_ticks = deque(maxlen=600)            # 30s @ 20Hz
        self.funding_history = deque(maxlen=24 * 3)   # 24h of 8h funding
        # Latest singletons
        self.long_short_ratio = 1.0
        self.hlp_exposure = 0.0
        self.mark_price = None
        self.oracle_price = None
        self.spot_index = None
        self.alt_venue_mark = None  # e.g. Binance index for HL detector

    # --- ingestion ---

    def on_liquidation(self, notional_usd, ts):
        # Bucket by minute
        bucket = ts // 60
        if not self.liq_1min or self.liq_1min[-1][0] != bucket:
            self.liq_1min.append([bucket, notional_usd])
        else:
            self.liq_1min[-1][1] += notional_usd

    def on_funding(self, rate_8h):
        self.funding_history.append(rate_8h)

    def on_oi(self, oi_usd):
        self.oi_history.append(oi_usd)

    def on_tick(self, mark, oracle, spot, signed_size):
        self.mark_price = mark
        self.oracle_price = oracle
        self.spot_index = spot
        cum = (self.cvd_ticks[-1][1] if self.cvd_ticks else 0) + signed_size
        self.cvd_ticks.append((mark, cum))
        self.prices_15m.append(mark)

    # --- signal evaluators ---

    def _pre_cascade_score(self):
        score = 0
        if len(self.funding_history) >= 3:
            recent_funding = list(self.funding_history)[-3:]
            if all(f > self.FUNDING_HIGH_8H for f in recent_funding):
                score += 40  # funding weight
        if len(self.oi_history) >= 24 * 30:
            oi_p = np.percentile(self.oi_history, self.OI_PERCENTILE * 100)
            if self.oi_history[-1] > oi_p:
                score += 30
        if self.long_short_ratio > self.LONG_SHORT_RATIO_HIGH:
            score += 20
        if self.hlp_exposure > self.HLP_EXPOSURE_USD:
            score += 10
        return score

    def _imminent_score(self):
        score = 0
        if len(self.liq_1min) >= 60 and self.liq_1min:
            notionals = [n for _, n in self.liq_1min]
            p99 = np.percentile(notionals, 99)
            if self.liq_1min[-1][1] > p99:
                score += 40
        if self.mark_price and self.spot_index:
            basis_bps = abs(self.mark_price - self.spot_index) / self.spot_index * 1e4
            if basis_bps > self.BASIS_DISLOCATION_BPS:
                score += 25
        if self.mark_price and self.alt_venue_mark:
            div_bps = abs(self.mark_price - self.alt_venue_mark) / self.alt_venue_mark * 1e4
            if div_bps > self.CEX_DEX_DIVERGENCE_BPS:
                score += 20
        if self.mark_price and self.oracle_price:
            dev_bps = abs(self.mark_price - self.oracle_price) / self.oracle_price * 1e4
            if dev_bps > self.MARK_ORACLE_ACUTE_BPS:
                score += 15
        return score

    def _in_cascade(self):
        if len(self.liq_1min) < 60 or len(self.prices_15m) < 60:
            return False
        # 5-min liq vs 24h mean
        recent_5m = sum(n for _, n in list(self.liq_1min)[-5:])
        mean_24h = np.mean([n for _, n in self.liq_1min]) or 1e-9
        liq_spike = recent_5m / mean_24h >= self.LIQ_SPIKE_MULTIPLIER
        # Price drop
        price_drop = (self.prices_15m[0] - self.prices_15m[-1]) / self.prices_15m[0]
        return liq_spike and price_drop >= self.PRICE_DROP_PCT

    def _cvd_exhausted(self):
        if len(self.cvd_ticks) < 600:
            return False
        cvd_arr = np.array([c for _, c in self.cvd_ticks])
        slope_now = np.polyfit(np.arange(300), cvd_arr[-300:], 1)[0]
        slope_prev = np.polyfit(np.arange(300), cvd_arr[-600:-300], 1)[0]
        return abs(slope_now) <= self.CVD_FLATTEN_RATIO * (abs(slope_prev) + 1e-9)

    # --- state machine ---

    def step(self):
        prev = self.stage
        if self._in_cascade():
            self.stage = Stage.IN_CASCADE
        elif self._imminent_score() >= 50:
            self.stage = Stage.IMMINENT
        elif self._pre_cascade_score() >= 70:
            self.stage = Stage.PRE_CASCADE
        else:
            self.stage = Stage.QUIET

        if self.stage != prev:
            self._emit_transition(prev, self.stage)
        return self.stage, self._cvd_exhausted()

    def _emit_transition(self, prev, curr):
        # Hook: alerting, position-management, keeper-arming, etc.
        print(f"[{self.symbol}] {prev.name} -> {curr.name} at {time.time()}")
```

The detector is intentionally event-driven — `step()` is called on every tick or on a schedule (e.g., every 100ms). The `_cvd_exhausted` flag returned alongside the stage is the actual entry signal for the [[liquidation-cascade-fade]] strategy: enter long when `stage == IN_CASCADE AND cvd_exhausted`.

## Hyperliquid-Specific Tooling

[[hyperliquid]]'s sub-second blocks and transparent CLOB make detection windows tighter than any CEX, but also expose more raw signal:

- **Sub-second block times** mean cascades execute in 5-15 blocks, not minutes. The window between *cascade-imminent* and *in-cascade* compresses; detectors must be tuned faster.
- **Transparent CLOB** means whale stop-loss clusters are *visible*. Resting stop-loss orders (where the venue exposes them) and large limit orders pulled simultaneously are pre-cascade tells unavailable on most CEXs.
- **HLP positions on-chain** mean you can see the protocol's automated counterparty drift toward fragility in real time. [[hypurrscan]] and the Hyperliquid SDK both expose HLP per-pair exposure.
- **Oracle price feed lags fastest CEX prints by 200-500ms** during fast tape. The mark-oracle gap is therefore a meaningful Hyperliquid-specific signal that doesn't exist on Binance (where mark and last are tightly coupled).
- **HLP withdrawal lockup** is currently 4 days. This means the imminent-stage signal is *actionable* for HLP depositors only if it arrives 4+ days before the cascade — which is rarely the case. In practice, HLP depositors must rely on pre-cascade signals (funding, OI, HLP exposure) and accept some cascades will hit them in lockup.

See [[hyperliquid-liquidation-engine]] for the engine internals and [[hyperliquid-oracle-mechanics]] for oracle update cadence.

## How Operators Chain the Signals

Different operators consume different stages of the hierarchy and act differently:

### Passive HLP Depositor

- **Inputs:** pre-cascade composite score, HLP per-pair exposure, current HLP APR.
- **Action on PRE-CASCADE:** initiate withdrawal request (4-day lockup means this is mostly future-protection, not current-cascade protection).
- **Action on IMMINENT:** verify exposure, log alert. Cannot act intra-cascade due to lockup.
- **Action on IN-CASCADE:** monitor only — withdrawal already in flight or impossible.
- **Latency tolerance:** 30-second polling.

### Cascade Fade Trader

- **Inputs:** imminent-stage signals to pre-stage capital, in-cascade + CVD exhaustion to pull trigger.
- **Action on PRE-CASCADE:** ensure margin available, raise alert level.
- **Action on IMMINENT:** stage limit orders below current price, ready execution stack.
- **Action on IN-CASCADE + CVD exhausted:** market-buy the perp at 3× leverage, 5% allocation. Stop at -3%, target at pre-cascade VWAP, time stop 4 hours. Per [[liquidation-cascade-fade]].
- **Latency tolerance:** sub-1-second.

### Lending-Protocol Keeper Bot

- **Inputs:** mempool oracle updates, on-chain position health factors, in-cascade flag.
- **Action on PRE-CASCADE:** index at-risk positions, pre-fund flash-loan capacity, top up gas.
- **Action on IMMINENT:** subscribe to high-priority RPCs, prepare liquidation transactions for top-N at-risk positions.
- **Action on IN-CASCADE:** spam liquidation candidates as oracle ticks confirm underwater status. Submit via private mempool ([[mev-strategies|Flashbots]] equivalent). Per [[liquidation-cascade-arbitrage]].
- **Latency tolerance:** sub-100ms.

### Hyperliquid HLP-Alongside Operator

- **Inputs:** HLP positions, per-pair exposure, predicted HLP losses if cascade extends.
- **Action on PRE-CASCADE:** review HLP exposure, optionally hedge externally on Binance/Bybit.
- **Action on IMMINENT:** if HLP is forced-long an asset that is now cascading, short the same asset on a CEX to hedge HLP's exposure pre-emptively. See [[hlp-cascade-alongside-playbook]].
- **Action on IN-CASCADE:** maintain hedge through the flush; unwind when HLP recovers.
- **Latency tolerance:** 1-5 seconds.

The same detector serves all four — only the action handlers differ.

## Common Pitfalls

- **Static thresholds.** "10 liquidations per minute" looks reasonable in calm regimes and trips constantly in volatile regimes. Always use trailing percentiles.
- **Aggregator latency.** Coinglass is excellent for backfill and pre-cascade context, useless for in-cascade triggering. Run direct WS feeds.
- **Last vs mark price confusion.** Single liquidation prints can spike last price by 1-2% on thin pairs without the mark price moving. Trigger on mark for cascade detection.
- **Single-venue detection.** A cascade on Binance alone is rare; cascades almost always span venues. Aggregate liquidations across at minimum the top 4 CEXs plus Hyperliquid for top pairs.
- **Ignoring the regime overlay.** All signals fire during *both* flash crashes and bear-leg-opening cascades. The detector cannot distinguish these — the operator must add macro/regime context (cross-asset correlation, funding persistence after cascade, basis collapse on stables). See "What Kills This Strategy" in [[liquidation-cascade-fade]].
- **Forgetting HLP lockup.** The "withdraw HLP on imminent" plan only works if you have time. Pre-cascade is the actionable horizon for HLP; imminent is too late.
- **Overfitting to historical events.** The 8 cascades listed above are a small sample. Detectors that perfectly fit them will produce many false negatives on novel cascade shapes. Prefer fewer, simpler thresholds calibrated to percentiles rather than absolute values.

## Related

- [[liquidation-cascade-fade]] — the contrarian long that consumes IN-CASCADE + CVD-exhaustion
- [[liquidation-cascade-arbitrage]] — the keeper bot that consumes IMMINENT + on-chain underwater status
- [[hyperliquid-hlp-basis-arbitrage]] — the HLP-aware passive operator that consumes PRE-CASCADE
- [[hlp-cascade-alongside-playbook]] — coordinated HLP-hedge during cascades
- [[hyperliquid-liquidation-engine]] — engine internals affecting cascade shape on HL
- [[hyperliquid-oracle-mechanics]] — oracle update cadence for mark-oracle deviation signals
- [[order-flow-analysis]], [[cumulative-volume-delta]] — CVD theory and computation
- [[funding-rate]], [[mark-price]] — primitive signals
- [[perpetual-futures]], [[liquidation]] — instrument and mechanic prerequisites
- [[hypurrscan]] — Hyperliquid analytics
- [[insurance-fund]] — exchange-side cascade absorption
- [[mev-strategies]] — keeper-bot infrastructure context

## Sources

- Binance API documentation, `forceOrder@arr` WebSocket channel.
- Bybit V5 API documentation, `liquidation` topic.
- OKX API documentation, `liquidation-orders` channel.
- Hyperliquid SDK and HTTP API, `userEvents` and `info` endpoints.
- Coinglass aggregated liquidation feed documentation and API reference.
- HypurrScan Hyperliquid analytics dashboard.
- Bookmap and ATAS documentation on cumulative volume delta methodology.
- Amberdata research, *"Liquidations in Crypto: How to Anticipate Volatile Market Moves"*, 2025.
- Z. Ali, *"Anatomy of the Oct 10–11, 2025 Crypto Liquidation Cascade,"* SSRN 5611392, 2025 — quantitative cascade microstructure analysis.
- BIS Bulletin No. 90, *"The market turbulence and carry trade unwind of August 2024"*, for the 2024-08-05 case study.
- IWH Discussion Paper, *"Bitcoin Flash Crash on May 19, 2021: What Did Really Happen on Binance?"*, for cross-venue cascade dynamics.
- [[liquidation-cascade-fade]] — implementation-faithful entry conditions reused above.
- [[liquidation-cascade-arbitrage]] — keeper-bot consumer context.
- [[hyperliquid-hlp-basis-arbitrage]] — HLP-aware operator context.
