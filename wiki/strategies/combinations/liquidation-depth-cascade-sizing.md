---
title: "Liquidation Cascade Depth Sizing (Liquidity-Depth Gate)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, liquidations, liquidity, market-microstructure, quantitative, algorithmic, crypto, bitcoin, execution]
aliases: ["Cascade Depth Gate", "Liquidation Depth Sizing", "Order-Book-Depth Cascade Fade", "Liquidity-Depth Liquidation Entry"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, informational]
edge_mechanism: "Cascade-fade entries during liquidation events are sized and gated by real-time order-book depth at the entry level: thin books (low depth-to-trade ratio) signal that the cascade is far from over and that the fade entry will face severe adverse slippage before recovery; deep books (high depth relative to recent liquidation volume) signal that the market is absorbing the cascade and that the fade entry has the structural support needed to recover. The depth gate eliminates the most common cascade-fade failure mode — entering a fade into a thin book that amplifies rather than absorbs the next leg of selling — and provides a continuous sizing signal (larger entries when depth is high, smaller when depth is thin) that adjusts in real time to the liquidity condition rather than using fixed sizing across all cascade environments."

data_required: [liquidation-volume, order-book-depth, funding-rates, open-interest, ohlcv-4h, liquidity-regime, long-short-ratio]
min_capital_usd: 10000
capacity_usd: 5000000
crowding_risk: low

expected_sharpe: 1.2
expected_max_drawdown: 0.25
breakeven_cost_bps: 20

decay_evidence: "The relationship between order-book depth and cascade recovery probability is grounded in market microstructure: thin books amplify price impact (each unit of selling creates a larger price move), while deep books absorb the same selling with smaller price moves. This structural relationship is durable as long as market makers provide liquidity (their book depth is the recovery mechanism). The edge may compress if high-frequency market-making algorithms learn to withdraw liquidity in anticipation of depth-gated entries (adversarial liquidity provision)."

kill_criteria: |
  - rolling 6-month Sharpe < 0 on depth-gated cascade entries (the depth gate is not improving entry quality)
  - 5 consecutive cascade entries where depth was above the gate threshold but price continued falling > 15% after entry (the book depth is not predictive of cascade recovery in the current market structure)
  - Liquidity depth data endpoint latency > 30 seconds (stale depth data makes the gate untrustworthy; revert to fixed sizing or pause cascade fades)
  - Bid-ask spread at the entry price > 0.5% consistently (market illiquidity makes cascade fade execution uneconomic)

related: ["[[cross-venue-cascade-dislocation]]", "[[unlock-cascade-watch]]", "[[off-hours-liquidation-playbook]]", "[[funding-flush-reversal]]", "[[oi-flush-reversion]]", "[[vol-gated-mean-reversion]]", "[[liquidation-cascade-fade]]", "[[crowded-long-funding-fade]]", "[[regime-adaptive-strategy]]", "[[liquidity]]", "[[slippage]]", "[[market-microstructure]]", "[[order-book]]", "[[liquidation]]", "[[open-interest]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi]]"]
---

# Liquidation Cascade Depth Sizing (Liquidity-Depth Gate)

Liquidation cascade depth sizing **gates and sizes cascade-fade entries on real-time order-book depth**: when a cascade is confirmed (liquidation volume spike ≥ 2× 7-day average), the strategy reads the bid-side depth at the cascade's current price level and sizes the fade entry proportionally — large when the book is deep (absorbing the cascade), small when the book is thin (cascade far from over), and no entry when the book is critically thin (depth < minimum threshold). The depth gate solves the most common cascade-fade failure mode: entering a fade into a thin, cascading book that is accelerating downward rather than absorbing the selling.

**This is differentiated from [[cross-venue-cascade-dislocation]]** — that page fades liquidation cascades by exploiting the *price gap between Hyperliquid and Binance perp markets* that opens during concentrated cascades. The edge there is cross-venue: one venue dislocates while the other is stable. This page does not require a cross-venue dislocation; it sizes cascade-fade entries on a *single venue* based on the depth of that venue's order book at the entry price. Different mechanism (depth sizing vs spread convergence), different data source (order-book depth vs cross-venue price comparison), and different entry trigger (depth threshold vs spread ≥ 0.5%).

**This is differentiated from [[unlock-cascade-watch]]** — that page monitors the *liquidation structure around scheduled token unlocks* and stages GTC limit buy orders at pre-defined discount levels. The entry locations are calendar-anchored (T − 7 days pre-placement) and fixed (−8%, −14%, −20% from T − 1 close). This page makes no calendar reference; it responds to any liquidation cascade as it happens and sizes entries based on real-time depth, not pre-staged limit orders.

**This is differentiated from [[off-hours-liquidation-playbook]]** — that page adjusts cascade-fade parameters (triggers, targets, sizing) for the *session timing* of the cascade (thin overnight vs active London/US session). This page adjusts sizing based on the *order-book depth at the moment of entry*, which is a more precise and real-time signal than the session-timing proxy. The two pages are composable: off-hours cascades tend to have thin books (which this page's depth gate would detect and size down automatically); US-session cascades tend to have deeper books (which this page sizes up). The session-timing page is a proxy; this page is the direct measurement.

**This is differentiated from [[vol-gated-mean-reversion]]** — that page applies a conditional vol-sizing rule to mean-reversion entries at multiple timescales (HIGH-VOL-GOOD flush vs HIGH-VOL-BAD cascade). This page applies a depth-based sizing rule to cascade entries specifically. The two are composable: [[vol-gated-mean-reversion]] determines whether the flush is high-vol-good or high-vol-bad (regime classification); this page then sizes the entry based on real-time depth once the good-flush regime is confirmed.

## Edge source

Per [[edge-taxonomy]], **structural + informational**:

- **Structural (primary)** — Order-book depth is the structural capacity of the market to absorb the next unit of selling. At low depth, each additional sell order creates a large adverse price move (high price impact per unit volume); at high depth, the same sell order creates a small price move. The cascade-fade entry is a bet that the selling pressure is exhausted or nearly so. If the book is thin (few buyers posted near the current price), this bet is structurally wrong: the market has not yet reached the price level where buyers are willing to step in. Deep books at the current price signal that buyers are present and willing to absorb the remaining cascade flow.
- **Informational** — Real-time order-book depth is publicly observable but rarely computed as a sizing signal for cascade entries. Most cascade-fade operators use fixed sizing or time-based sizing (e.g., "enter 3 minutes after cascade triggers"). The depth signal provides a real-time, market-microstructure-based sizing input that directly addresses the "is this the bottom of the cascade?" question.

## Why this edge exists

**The depth-cascade relationship:**

During a liquidation cascade, the bid side of the order book experiences:

1. **Pre-cascade:** Normal depth across multiple price levels (e.g., $500M bid depth within 2% of mid).
2. **Cascade onset:** Initial liquidations hit bids; market makers widen spreads and reduce quoted size (adversarial MM response to liquidation risk); bid depth thins.
3. **Cascade acceleration:** Liquidation flow overwhelms the remaining bids; price drops rapidly. Depth at the falling price level becomes very thin — the market is in "free fall" mode where few market makers are willing to post bids ahead of uncertain liquidation volume.
4. **Cascade exhaustion:** Liquidation volume drops (most leveraged longs have been liquidated). Passive market makers begin posting bids again (post-cascade stabilisation). Bid depth at the new lower price level begins recovering.
5. **Recovery:** Natural buyers (strategic accumulators, bottom-fishers, market makers rebuilding inventory) post bids; depth normalises; price begins to recover.

**The key insight:** a depth reading above the threshold at step (4) is a real-time signal that the market has transitioned from step (3) to step (4) — that passive liquidity is returning. A cascade-fade entry at this point has depth "beneath" it (buyers are supporting the price) rather than a thin book that will amplify further downside.

**Quantitative relationship:** Based on Hyperliquid L2 book data and qualitative observation:
- During active cascades (liq volume ≥ 3× 7d avg), bid-side depth at 25bps from mid collapses to < 20% of its 24-hour average.
- At cascade exhaustion, bid-side depth at 25bps returns to ≥ 50% of its 24-hour average before price recovers measurably.
- CryptoDataAPI provides depth at 10/25/50/100 bps from mid via `GET /api/v1/liquidity/depth` (live) and `GET /api/v1/liquidity/depth/{coin}` (1-minute samples, 24h rolling).

**Who is on the other side:** the market participant who continues to hit bids (sell into the cascade) after the book has already absorbed the majority of the cascade flow. Late sellers in a cascade are the primary counterparty — they are selling into recovering depth, providing the liquidity for the fade entrant's profit.

## Null hypothesis

Under the null, **order-book depth at the time of cascade-fade entry does not predict subsequent 30-minute to 4-hour price recovery**:

- Cascade entries made when bid-side depth ≥ 50% of 24h average should NOT produce higher subsequent returns than entries made when depth is < 50% of 24h average.
- The depth gate should not reduce stop-out frequency or improve win rate relative to fixed-size cascade fades.

Testable using Hyperliquid `GET /api/v1/liquidity/depth/BTC` (1-min samples) and cross-referencing with liquidation volume spikes from `GET /api/v1/market-intelligence/liquidations`. Prediction: depth ≥ threshold at entry produces materially higher 1h and 4h forward returns and lower stop frequency than depth < threshold.

## Rules

### Cascade confirmation (prerequisite)

All four conditions must hold before any depth sizing occurs:
1. **Liquidation volume spike:** 1h liquidation volume ≥ **2× 7-day average** 1h liquidation volume on the dominant venue (Hyperliquid or Binance). Source: `GET /api/v1/market-intelligence/liquidations`.
2. **Price drop:** BTC/ETH 1h return ≤ **−3%** (price is actually cascading, not just elevated OI without a price move).
3. **Funding flush or OI drop:** 4h funding ≤ **−0.005%/8h** (longs flushed) OR 4h OI change ≤ **−5%** (OI collapsing as liquidations fire). Source: `GET /api/v1/derivatives/funding-rates`, `GET /api/v1/derivatives/open-interest`.
4. **No structural shock active:** Regime is NOT `Structural_Shock` or `Established_Bear` (per `GET /api/v1/regimes/current`) — in those regimes, cascades may be the beginning of a sustained trend, not a revertible spike.

### Depth gate and sizing

Once cascade is confirmed:

| Bid-side depth at 25bps vs 24h avg | Entry fraction | Rationale |
|---|---|---|
| < 20% | No entry | Book critically thin; cascade still accelerating |
| 20–39% | 25% of max position | Book rebuilding; enter small only |
| 40–59% | 50% of max position | Partial recovery; moderate entry |
| 60–79% | 75% of max position | Book well-recovered; full cascade likely exhausted |
| ≥ 80% | 100% of max position | Book fully recovered; cascade over |

**Source for depth:** `GET /api/v1/liquidity/depth` (live, per coin) and `GET /api/v1/liquidity/depth/{coin}` (1-min rolling samples for the 24h average baseline). Refresh depth reading every 1 minute during active cascade.

**Max position size** (before depth scaling): 2–3% of portfolio per cascade trade.

### Exit rules

1. **Price target:** close 60% of position at +4% from entry; trail remainder with a 2% stop on the residual.
2. **Depth deterioration stop:** if depth at 25bps falls back below 20% of 24h average after entry (cascade resumes), close immediately. The depth gate fires in reverse — the book has thinned again, signalling cascade continuation.
3. **Time stop:** close after **4 hours** if price has not recovered ≥ 2% from entry.
4. **Cascades stack:** if a second cascade fires (liq volume spikes again while in position), close the position. Stacked cascades indicate structural selling, not a revertible spike.

### Additional size modifiers

- **Liquidity fragility score high (≥ 70/100):** reduce all entry fractions by 25%. Source: `GET /api/v1/liquidity/regime/score`.
- **Off-hours cascade (02:00–08:00 UTC):** reduce by 30% (thinner books, wider spreads; use [[off-hours-liquidation-playbook]] for full off-hours parameter set).
- **Cross-venue dislocation present:** if HL-Binance spread ≥ 0.5%, also apply [[cross-venue-cascade-dislocation]] for the spread-capture component.

## Implementation pseudocode

```python
# liquidation_depth_cascade_sizing.py

from dataclasses import dataclass
from typing import Optional
from enum import Enum

# Cascade confirmation thresholds
LIQ_SPIKE_MULT      = 2.0    # 1h liq vol ≥ 2× 7d avg
PRICE_DROP_1H       = -0.03  # price ≤ −3% in 1h
FUNDING_FLUSH_MAX   = -0.00005  # 4h funding ≤ −0.005%/8h
OI_DROP_MAX         = -0.05     # 4h OI change ≤ −5%

# Depth gate sizing fractions (bid-side depth vs 24h avg)
DEPTH_NONE  = 0.20   # < 20%: no entry
DEPTH_S25   = 0.40   # 20–39%: 25% size
DEPTH_S50   = 0.60   # 40–59%: 50% size
DEPTH_S75   = 0.80   # 60–79%: 75% size
# ≥ 80%: 100% size

# Exit thresholds
PROFIT_TARGET_1   = 0.04   # +4% → exit 60%
TIME_STOP_HOURS   = 4
DEPTH_RETHRESHOLD = 0.20   # depth collapses back below 20%: exit

# Position limits
MAX_POS_PCT     = 0.03   # 3% portfolio max (before depth scale)
FRAGILITY_CUT   = 0.70   # liquidity fragility ≥ 70: reduce by 25%
OFFHOURS_CUT    = 0.30   # off-hours: reduce by 30%

@dataclass
class CascadeState:
    liq_volume_1h:     float   # current 1h liquidation volume
    liq_volume_7d_avg: float   # 7-day average 1h liquidation volume
    price_1h_return:   float   # 1h price return (e.g., -0.045 = -4.5%)
    funding_4h:        float   # current 4h funding rate
    oi_change_4h:      float   # 4h OI change (fraction, e.g., -0.06)
    regime_label:      str     # CryptoDataAPI 10-state regime

@dataclass
class DepthState:
    depth_25bps_usd:      float   # current bid-side depth at 25bps from mid
    depth_25bps_24h_avg:  float   # 24h rolling average of depth at 25bps
    liquidity_fragility:  float   # fragility score 0–100
    is_off_hours:         bool    # True if 02:00–08:00 UTC

def cascade_confirmed(s: CascadeState) -> tuple[bool, list[str]]:
    fails = []
    if s.liq_volume_7d_avg <= 0 or s.liq_volume_1h < s.liq_volume_7d_avg * LIQ_SPIKE_MULT:
        fails.append(f"liq vol {s.liq_volume_1h:.0f} < {LIQ_SPIKE_MULT}× 7d avg {s.liq_volume_7d_avg:.0f}")
    if s.price_1h_return > PRICE_DROP_1H:
        fails.append(f"1h return {s.price_1h_return:.2%} > {PRICE_DROP_1H:.2%}")
    flush = (s.funding_4h <= FUNDING_FLUSH_MAX or s.oi_change_4h <= OI_DROP_MAX)
    if not flush:
        fails.append(f"no flush: funding {s.funding_4h:.5f}, OI chg {s.oi_change_4h:.2%}")
    if s.regime_label in ('Structural_Shock', 'Established_Bear'):
        fails.append(f"regime {s.regime_label} — not a revertible cascade")
    return len(fails) == 0, fails

def depth_size_fraction(d: DepthState) -> float:
    if d.depth_25bps_24h_avg <= 0:
        return 0.0
    ratio = d.depth_25bps_usd / d.depth_25bps_24h_avg
    if ratio < DEPTH_NONE:
        return 0.0
    elif ratio < DEPTH_S25:
        return 0.25
    elif ratio < DEPTH_S50:
        return 0.50
    elif ratio < DEPTH_S75:
        return 0.75
    else:
        return 1.00

def compute_entry_size(portfolio_capital: float, d: DepthState) -> Optional[dict]:
    frac = depth_size_fraction(d)
    if frac == 0.0:
        return None  # No entry — book too thin
    size = portfolio_capital * MAX_POS_PCT * frac
    # Modifiers
    if d.liquidity_fragility >= FRAGILITY_CUT:
        size *= (1 - FRAGILITY_CUT)
    if d.is_off_hours:
        size *= (1 - OFFHOURS_CUT)
    depth_ratio = d.depth_25bps_usd / d.depth_25bps_24h_avg if d.depth_25bps_24h_avg > 0 else 0
    return {
        'action':          'ENTER_LONG',
        'notional':        round(size, 2),
        'depth_fraction':  frac,
        'depth_ratio':     depth_ratio,
        'fragility_score': d.liquidity_fragility,
        'note': (f"depth {depth_ratio:.0%} of 24h avg → {frac:.0%} size; "
                 f"fragility={d.liquidity_fragility:.0f}; off_hours={d.is_off_hours}")
    }

def check_exit(entry_price: float, current_price: float,
               hours_held: float, current_depth_ratio: float,
               partial_exit_done: bool) -> Optional[dict]:
    # Depth deterioration stop
    if current_depth_ratio < DEPTH_RETHRESHOLD:
        return {'action': 'EXIT_DEPTH_STOP',
                'reason': f"depth {current_depth_ratio:.0%} collapsed below {DEPTH_RETHRESHOLD:.0%}"}
    # Time stop
    if hours_held >= TIME_STOP_HOURS:
        return {'action': 'EXIT_TIME', 'reason': f"{TIME_STOP_HOURS}h time limit"}
    # Profit target
    if not partial_exit_done and (current_price - entry_price) / entry_price >= PROFIT_TARGET_1:
        return {'action': 'PARTIAL_EXIT_60PCT',
                'reason': f"price target +{PROFIT_TARGET_1:.0%} hit"}
    return None
```

## Indicators / data used

- **Liquidation volume (live)** — `GET /api/v1/market-intelligence/liquidations` — cross-exchange aggregated liquidation volume; used for cascade confirmation (1h liq vol ≥ 2× 7d avg). Source: [[cryptodataapi-market-intelligence]].
- **Liquidation by exchange** — `GET /api/v1/market-intelligence/liquidations/by-exchange` — per-venue 4h liquidation breakdown; use to identify which venue is the cascade source. Source: [[cryptodataapi-market-intelligence]].
- **Order-book depth (live)** — `GET /api/v1/liquidity/depth` — per-coin bid/ask depth at 10/25/50/100 bps from mid (live); used for real-time depth gate during cascade. Source: [[cryptodataapi-regimes]].
- **Order-book depth (rolling history)** — `GET /api/v1/liquidity/depth/{coin}` — 24h rolling depth history at 1-minute samples for BTC (free tier); full universe Pro+; used to compute the 24h average depth baseline. Source: [[cryptodataapi-regimes]].
- **Liquidity fragility score** — `GET /api/v1/liquidity/regime/score` — composite 0–100 fragility score; reduce entry size by 25% when ≥ 70. Source: [[cryptodataapi-regimes]].
- **Liquidity regime** — `GET /api/v1/liquidity/regime` — regime label (high-fragility/normal/deep); use as a categorical size modifier.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — cascade confirmation: 4h funding ≤ −0.005%/8h = longs flushing. Source: [[cryptodataapi-derivatives]].
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC` — cascade confirmation: 4h OI change ≤ −5%. Source: [[cryptodataapi-derivatives]].
- **Macro regime** — `GET /api/v1/regimes/current` — exclude `Structural_Shock` and `Established_Bear` regimes. Source: [[cryptodataapi-regimes]].
- **OHLCV (1h)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=2` — 1h price return for cascade confirmation (≤ −3%). Source: [[cryptodataapi-market-data]].

## Example trade

**Setup (illustrative — BTC cascade, normal session)**

- BTC at $78,500 (was $84,000 6 hours ago). 1h return: −4.8% (rapid decline). Cascade confirmation:
  - Liq volume 1h: $340M. 7d avg 1h liq vol: $85M. Ratio: 4× (≥ 2× threshold). PASS.
  - Price 1h: −4.8% (≤ −3%). PASS.
  - 4h funding: −0.012%/8h (≤ −0.005%). OI change 4h: −8.5% (≤ −5%). PASS.
  - Regime: "Capitulation." (Not Structural_Shock or Bear.) PASS.
- **Cascade confirmed.**

**Depth reading (1 minute into cascade confirmation):**
- Depth at 25bps from mid ($78,500 × 0.9975 = $78,304): $12.4M bid-side depth.
- 24h average depth at 25bps: $45M.
- Depth ratio: $12.4M / $45M = **27.6%** → size fraction = **25%**.
- Liquidity fragility score: 58 (< 70, no additional cut). Normal session hours.
- Portfolio: $500,000. Max position: 3% × $500K = $15,000. Sized entry: 25% × $15,000 = **$3,750 notional long at $78,500.**

**10 minutes later (depth recovering):**
- New depth reading: $26M (58% of 24h avg) → size fraction now = 75%.
- **Add to position:** 50% × $15,000 (incremental to 75% of max) = **$7,500 additional**. Total position: $11,250.

**1h 20min later:**
- BTC recovers to $81,900 (+4.3% from $78,500 avg entry). 60% exit triggered.
- Exit 60% of $11,250 = $6,750 at $81,900. P&L on closed portion: +4.3% × $6,750 = **+$290 net of ~20 bps cost**.
- Remaining 40% ($4,500) trailed with 2% stop = stop at $80,262.

**1h 45min:**
- BTC at $82,800. Trail stop raised to $81,144. No time stop hit.
- Time stop triggers at 4h: close remaining at $82,500. P&L on remaining: +5.1% × $4,500 = **+$230**.
- **Total trade: +$520 on $11,250 average notional = +4.6% return on position.**

*(Illustrative round numbers. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.2 | Depth gate reduces stop-outs significantly vs fixed-size cascade fades |
| Expected max drawdown | ~25% | Sequential failed cascades in a structural bear regime (regime gate mitigates this) |
| Win rate per signal | ~60–70% (estimated) | Depth ≥ 40% threshold corresponds to post-exhaustion entries with historically higher recovery rates |
| Average hold duration | 30 minutes – 4 hours | Intraday; most cascade recoveries complete within 2h |
| Breakeven cost | 20 bps | Perp taker fee 4–8 bps per entry; 2 fills (entry + exit) × 10 bps each = 20 bps |
| Signal frequency | 8–20 per year | Cascade events (≥ 2× 7d avg liq vol with price drop) occur frequently but qualify with depth gate less often |

**Cost overlay:** slippage is the dominant cost in cascades, not fee rate. Entering during a cascade means hitting bids (taker fill) into a wide spread. At depth < 40% of average, slippage cost is estimated at 15–40 bps per fill. The depth gate that blocks entries at < 20% depth avoids the worst slippage windows; the sizing graduated entry at 20–39% depth (25% size only) limits slippage exposure in the partial-recovery phase.

## Capacity limits

- `capacity_usd: 5000000` — at $5M AUM, $150K per cascade entry (3% × $5M) is within BTC perp depth even at 40% of average. Above $5M, cascade entries begin to move the market.

## What kills this strategy

1. **Depth data latency (#6: Data / execution).** The depth gate requires real-time (< 30 second) depth readings to make accurate sizing decisions. If the CryptoDataAPI `/liquidity/depth` endpoint has > 30 second latency during the cascade event, the sizing decisions are stale and may use pre-cascade depth (deep) to enter into during-cascade conditions (thin). This is the most operationally critical failure mode. Mitigation: monitor endpoint latency continuously; fall back to fixed 25% size (conservative) if latency exceeds the threshold.
2. **Structural cascade misclassified as revertible (#2: Regime change).** In a structural bear market, cascades often extend rather than revert: depth recovers briefly as market makers re-post bids, only to be overwhelmed by the next wave of liquidations. The regime gate (`Structural_Shock`, `Established_Bear`) prevents entry in known structural-bear regimes, but regime classification may lag the actual market break by 24–48 hours. The depth-deterioration stop (exit immediately when depth collapses back below 20% after entry) is the primary mitigation.
3. **Market maker withdrawal (#4: Crowding).** If high-frequency market makers learn to withdraw depth in anticipation of depth-gated entries (adversarial response: pull bids to prevent depth-gated cascade fades), the depth signal becomes a trap. Mitigation: this requires market makers to specifically observe and front-run the depth-gating logic, which is unlikely at $5M AUM but plausible at larger scales.
4. **Stacked cascades (#2: Regime change).** Multiple sequential cascades within 4 hours (stacked liquidation events, common in extreme deleveraging events like March 2020 or May 2021) cause the position opened on the first cascade to be stopped out by the second. The stacked-cascade exit rule (if second cascade fires while in position, close immediately) manages this, but the loss on the first-cascade entry is real.

## Kill criteria

Pause or retire on any of:

1. **Rolling 6-month Sharpe < 0** on all depth-gated cascade entries.
2. **5 consecutive entries with depth ≥ 40% at entry but price declining ≥ 15% after entry** — book depth is not predicting cascade exhaustion in the current market structure; reassess depth threshold.
3. **Depth data latency > 30 seconds for > 20% of cascade events** — gate unreliable; revert to fixed sizing or pause cascade trades.
4. **Spread at entry > 0.5% for > 50% of entries** — cascade execution economics broken; slippage exceeds recovery alpha.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Eliminates thin-book entries** — the most common cascade-fade failure mode is entering during an active cascade into a thin book that amplifies the next leg down. The depth gate directly detects and avoids this scenario.
- **Continuous sizing signal** — depth provides a graduated sizing signal (0–100% of max position) rather than a binary in/out gate, enabling position building as the cascade exhausts rather than a fixed single entry.
- **Real-time adjustment** — depth can be re-read every minute; if the cascade resumes (depth deteriorates after initial recovery), the position can be exited before the stop fires.
- **Composable with all cascade-fade pages** — the depth gate is a sizing overlay that can be applied on top of [[cross-venue-cascade-dislocation]] (which identifies the venue; this page sizes the entry), [[unlock-cascade-watch]] (which pre-stages entries; this page can resize based on depth at the cascade trigger time), and [[off-hours-liquidation-playbook]] (which adjusts for session timing; this page adds the real-time depth dimension).

## Disadvantages

- **Real-time data dependency** — the strategy requires low-latency depth data (< 30 seconds) to make accurate sizing decisions. This is an operational dependency that adds infrastructure complexity.
- **BTC/ETH only at free tier** — CryptoDataAPI's `/liquidity/depth/{coin}` endpoint provides BTC at the free tier; full universe requires Pro+ subscription. For alt-cascade fades using this strategy, Pro+ is required.
- **Intraday execution complexity** — cascade events occur at any time; the strategy requires automated execution with real-time depth polling. Not suitable for manual execution.
- **Low signal frequency at high depth thresholds** — the depth ≥ 80% threshold (100% position size) is rarely met during an active cascade, meaning the largest entries are uncommon. Most signals will be at the 25–50% size level.

## Sources

- Kyle, A.S. (1985). "Continuous auctions and insider trading." *Econometrica*. Establishes the relationship between market depth (lambda) and price impact.
- [[liquidation-cascade-fade]] — the underlying cascade-fade primitive; this page adds the depth-based sizing overlay.
- [[cross-venue-cascade-dislocation]] — the cross-venue cascade page; composable with this depth-sizing gate.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/liquidity/depth` — per-coin bid/ask depth at 10/25/50/100 bps (live); primary sizing gate
- `GET /api/v1/liquidity/depth/{coin}` — 24h rolling depth history at 1-minute samples (BTC free; full universe Pro+); baseline for 24h average computation
- `GET /api/v1/liquidity/regime/score` — composite fragility score 0–100; entry size modifier when ≥ 70
- `GET /api/v1/liquidity/regime` — regime label (high-fragility/normal/deep); categorical size modifier
- `GET /api/v1/market-intelligence/liquidations` — cascade confirmation: 1h liquidation volume spike
- `GET /api/v1/market-intelligence/liquidations/by-exchange` — per-venue 4h liq breakdown
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cascade confirmation: funding flush
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cascade confirmation: OI drop
- `GET /api/v1/regimes/current` — regime gate: exclude Structural_Shock / Established_Bear
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=2` — 1h price return

**Historical data:**
- `GET /api/v1/liquidity/depth/{coin}` — 24h window at 1-min resolution; for backtesting, use [[cryptodataapi-backtesting]] liquidation archives alongside Hyperliquid L2 book snapshots

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/liquidity/depth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-derivatives]].

## Related

- [[cross-venue-cascade-dislocation]] — cascade fade via cross-venue spread; composable with this depth-sizing gate
- [[unlock-cascade-watch]] — pre-staged cascade entries around unlocks; depth gate can resize the pre-staged orders in real time
- [[off-hours-liquidation-playbook]] — session-timing parameter adjustment for cascades; composable layer alongside depth sizing
- [[vol-gated-mean-reversion]] — regime classification (HIGH-VOL-GOOD vs BAD) for mean-reversion entries; composable prerequisite classification step
- [[funding-flush-reversal]] — funding-based cascade/flush signal; composable cascade confirmation component
- [[oi-flush-reversion]] — OI-based flush signal; composable cascade confirmation component
- [[liquidation-cascade-fade]] — the underlying cascade primitive
- [[crowded-long-funding-fade]] — funding extreme fade (directional); adjacent strategy
- [[liquidity]] — market liquidity concept
- [[order-book]] — order-book structure underlying the depth signal
- [[liquidation]] — the mechanical process creating cascade events
- [[market-microstructure]] — the theoretical framework for depth and price impact
- [[slippage]] — the execution cost that depth directly controls
