---
title: "Pairs with Funding Differential"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, pairs-trading, arbitrage, funding-rate, perpetual-futures, quantitative, behavioral-finance, crypto]
aliases: ["Funding-Enhanced Pairs", "Perp-Expressed Pairs with Carry", "Funding Differential Spread"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Leveraged retail participants on the crowded leg of a relative-value spread persistently misprize the cost of holding that leg, creating a funding differential between the two perps that simultaneously agrees with the spread direction; the strategy earns both mean-reversion of the spread z-score and a structural funding carry for being on the less-crowded side, while the counterparty pays crowd-premium funding and bears the squeeze risk."

data_required: [ohlcv-4h, funding-rates, open-interest, mark-price, perpetual-futures-depth]
min_capital_usd: 20000
capacity_usd: 50000000
crowding_risk: medium

expected_sharpe: 1.1
expected_max_drawdown: 0.18
breakeven_cost_bps: 25

decay_evidence: "No published study on funding-differential-gated crypto pairs. The funding-carry basis for the overlay is supported by BIS Working Paper 1087 (Schmeling, Schrimpf, Todorov 2023). The pairs-trading primitive has well-documented slow decay since the 1990s but remains viable in crypto where correlation instability is higher and structural anchors (shared BTC beta, shared CEX liquidity) are robust."

kill_criteria: |
  - strategy drawdown > 18% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 15 completed pairs cycles
  - spread z-score and funding differential are anti-correlated for 45+ consecutive days (overlay provides no information or actively hurts)
  - cointegration p-value of primary pairs deteriorates beyond 0.15 on a 90-day rolling window (structural anchor has broken)

related: ["[[pairs-trading]]", "[[funding-rate-arbitrage]]", "[[hl-vs-cex-funding-divergence]]", "[[funding-filtered-momentum]]", "[[crowded-long-funding-fade]]", "[[crowded-short-funding-fade]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[stat-arb]]", "[[cointegration]]", "[[z-score]]", "[[spread-trading]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Pairs with Funding Differential

Pairs-with-funding-differential is a [[pairs-trading|stat-arb/pairs]] strategy expressed through crypto perpetuals where the **spread entry gate** requires not only that the spread z-score is at an extreme, but also that the funding differential between the two perp legs agrees with the spread direction — meaning the strategy collects carry while holding the spread. The primitive edge is spread mean-reversion (cointegrated assets converge); the overlay is a structural carry screen that selects only the subset of spread entries where you are paid to hold, not where you pay to hold.

This is differentiated from [[hl-vs-cex-funding-divergence]] — that page exploits the same asset priced differently across venues (Hyperliquid vs Binance), with the funding differential arising from a cross-venue arbitrage premium. This page operates within a single venue or consistently across venues, expressing a relative-value view between *different* assets whose spread is mean-reverting; the funding differential is between the two legs of the pairs trade, not between the same asset on two venues.

This is also differentiated from [[funding-filtered-momentum]] — that strategy gates directional momentum on single-asset funding state. This strategy requires a funding *differential between two assets* to agree with the direction of the pairs spread entry, creating a dual confirmation: statistical (z-score) and structural (carry).

## Edge source

Per [[edge-taxonomy]], this is a **behavioral + structural + risk-bearing** combination:

- **Behavioral (primary)** — retail participants on the crowded leg of the relative-value spread persistently overbid that perp, generating an anomalously high funding rate. The crowd is expressing a view (long Asset A vs short Asset B, or vice versa) via the perp with the most convenient leverage, creating a persistent funding premium that is independent of — and confirms — the pairs signal. The counterparty is the directional retail trader paying crowd-premium funding on the over-weighted leg.
- **Structural (secondary)** — perpetual funding is a contractual cost that runs regardless of price direction. Entering the spread only when the funding differential pays the spread carrier means the position has a positive carry floor even if the spread reverts slowly. This structural income improves the risk-adjusted cost of waiting for the mean reversion.
- **Risk-bearing (tertiary)** — the spread position absorbs correlation risk (the cointegrated relationship breaking down) and cross-asset liquidity risk. The funding differential compensates for this risk-bearing; when the differential is absent or adverse, the risk-bearing is under-compensated, and the signal correctly blocks the entry.

## Why this edge exists

Two mechanisms reinforce each other to create an additive edge beyond either component alone:

1. **Crowding asymmetry on paired assets.** In crypto, correlated assets (e.g., two Layer-1 tokens with shared BTC beta) often trade with divergent funding rates when a narrative favours one over the other. Retail piles into the "hot" token's perp; the relative underdog's funding stays flat. The hot token's spread vs the underdog widens (spread z-score moves negative from the hot token's side), AND the funding differential is positive for holding the spread in the correct direction (long underdog perp which earns flat-to-positive funding, short hot-token perp which earns the positive-funding receiver payment). Both the convergence thesis and the carry agree simultaneously.

2. **Mean reversion is faster in funded spreads.** When the funding differential is large (e.g., +0.06%/8h on the leg you are short), the pool of new participants willing to open the crowded position shrinks over time. The spread naturally mean-reverts as the funding cost bleeds the crowded side. The funding differential is not just a carry bonus — it is itself a mean-reversion force operating on the counterparty's position.

**Who is on the other side:** the directional retail participant on the crowded perp leg who pays an elevated funding rate while holding a position that is being mean-reverted against them; and the late-narrative trader who enters the "hot" asset's perp after the funding differential is already elevated.

## Null hypothesis

Under the null, the funding differential at spread entry carries zero marginal information beyond the spread z-score. Specifically:
- Spread trades entered when the funding differential agrees with the spread direction should show the same forward mean-reversion speed, win rate, and Sharpe as spread trades entered when the funding differential is zero or adverse.
- The carry income from a favorable funding differential should not offset the higher-frequency of false convergence signals that the filter blocks.

The null is currently not rejected in this wiki (`backtest_status: untested`). Testable prediction: sort historical spread entries by funding differential alignment (agrees vs disagrees); the aligned subset should show materially better net-of-cost Sharpe and faster convergence (fewer time-stop exits).

## Rules

### Universe selection

1. **Cointegrated pairs.** Screen for asset pairs where a rolling 90-day Engle-Granger test yields p ≤ 0.10. In practice, high-correlation pairs include: BTC/ETH, ETH/SOL, comparable Layer-1 tokens (SOL/AVAX, BNB/MATIC), comparable DeFi tokens sharing yield infrastructure, and comparable Layer-2 tokens.
2. **Both legs must have liquid perps.** Minimum $20M daily perp volume per leg; minimum $10M perp OI per leg. Illiquid perps introduce wide spreads that overwhelm the carry income.
3. **Funding rates must be available on both legs.** This strategy requires real-time 8h funding on both legs simultaneously.

### Entry conditions

1. **Spread z-score extreme.** The spread (log-price of Asset A minus log-price of Asset B, or their normalized ratio) has a z-score ≤ −2.0 or ≥ +2.0 on a rolling 20-day lookback. This is the pairs-trading primary signal.
2. **Funding differential agrees with spread direction.** Define `funding_diff = funding_A - funding_B`. For a z-score ≤ −2.0 (Asset A cheap vs B): enter long A / short B only if `funding_diff ≤ −0.01%/8h` — meaning Asset B's funding exceeds A's by at least 0.01%/8h, so the short-B leg receives and the long-A leg pays less. For a z-score ≥ +2.0 (Asset A expensive vs B): enter short A / long B only if `funding_diff ≥ +0.01%/8h` — meaning Asset A's funding exceeds B's, paying the short-A leg. The minimum threshold of 0.01%/8h (~11% APY) ensures the carry is economically meaningful and not noise.
3. **OI gate.** Neither leg should be experiencing a collapsing OI (> −10% 24h change). A collapsing OI on the "crowded" leg ahead of a spread entry may indicate a trend is forming, not a crowded overshoot.
4. **No concurrent event risk.** No major protocol-specific catalyst (upgrade, exploit, unlock) on either leg within 48h that could cause a structural break in cointegration.

### Exit conditions

1. **Spread z-score reverts to 0 ± 0.5.** Primary take-profit: convergence to near-zero. Close both legs simultaneously.
2. **Spread z-score widens beyond ±3.5.** Stop-loss: spread has continued to diverge beyond the entry z-score by 1.5 standard deviations — cointegration may be breaking. Close both legs.
3. **Funding differential reverses.** If the funding differential shifts to adverse (starts paying against the spread direction) by more than 0.02%/8h for 2 consecutive 8h periods — carry is now negative; trim or close.
4. **Time stop: 15 calendar days.** If spread has not converged to ±0.5 z-score within 15 days, close at market regardless of P&L.
5. **Cointegration break.** If the rolling 90-day p-value breaks above 0.15, immediately close the position — the structural anchor is lost.

### Position sizing

- Size both legs in notional dollars equally (delta-neutral at entry): if one leg has higher beta, scale the notional proportionally so both legs have equal dollar P&L sensitivity to a 1% BTC move.
- Total spread notional = min(7.5% of sleeve capital, $capacity per pair). Do not exceed 7.5% sleeve exposure per pair; run maximum 3 concurrent pairs.
- Never use more than 3× leverage on either individual leg; spread positions are already inherently hedged, limiting leverage is the key risk discipline.

## Implementation pseudocode

```python
# pairs_with_funding_differential.py — spread entry + carry gate

from dataclasses import dataclass
from typing import Optional
import numpy as np

# ---- thresholds ----
Z_ENTRY          = 2.0      # spread z-score extreme to enter
Z_EXIT           = 0.5      # spread z-score target to exit (convergence)
Z_STOP           = 3.5      # spread z-score stop (divergence)
FUND_MIN_DIFF    = 0.0001   # 0.01%/8h minimum funding differential to agree
FUND_FLIP_EXIT   = 0.0002   # 0.02%/8h adverse flip triggers trim/close
OI_MIN_CHANGE    = -0.10    # OI cannot be collapsing more than 10% per day
COINT_P_MAX      = 0.10     # max cointegration p-value for universe
COINT_BREAK_P    = 0.15     # p-value above which cointegration is "broken"
TIME_STOP_DAYS   = 15
MAX_LEVERAGE     = 3.0
MAX_PAIRS_PCT    = 0.075    # max notional per pair as fraction of sleeve
MAX_CONCURRENT   = 3
LOOKBACK_DAYS    = 20

@dataclass
class PairSnapshot:
    asset_a: str
    asset_b: str
    spread_z: float          # z-score of log-spread (asset_a - asset_b) over LOOKBACK
    funding_a: float         # 8h funding for asset A perp
    funding_b: float         # 8h funding for asset B perp
    oi_change_a: float       # 24h OI % change for asset A
    oi_change_b: float       # 24h OI % change for asset B
    coint_p: float           # rolling 90-day cointegration p-value
    event_risk_a: bool       # major catalyst within 48h on asset A
    event_risk_b: bool       # major catalyst within 48h on asset B

def funding_differential(snap: PairSnapshot) -> float:
    return snap.funding_a - snap.funding_b

def entry_signal(snap: PairSnapshot) -> Optional[str]:
    """Returns 'long_a_short_b', 'short_a_long_b', or None."""
    if snap.coint_p > COINT_P_MAX:
        return None
    if snap.event_risk_a or snap.event_risk_b:
        return None
    if min(snap.oi_change_a, snap.oi_change_b) < OI_MIN_CHANGE:
        return None

    fd = funding_differential(snap)

    if snap.spread_z <= -Z_ENTRY and fd <= -FUND_MIN_DIFF:
        # Asset A cheap, Asset B expensive; short B receives positive funding
        return "long_a_short_b"

    if snap.spread_z >= Z_ENTRY and fd >= FUND_MIN_DIFF:
        # Asset A expensive, Asset B cheap; short A receives positive funding
        return "short_a_long_b"

    return None

def manage_position(snap: PairSnapshot, pos: dict, days_held: int) -> dict:
    fd = funding_differential(snap)

    # --- stop conditions ---
    if abs(snap.spread_z) >= Z_STOP:
        return {"action": "CLOSE", "reason": f"spread z {snap.spread_z:.2f} beyond stop {Z_STOP}"}
    if snap.coint_p > COINT_BREAK_P:
        return {"action": "CLOSE", "reason": "cointegration break"}
    if days_held >= TIME_STOP_DAYS:
        return {"action": "CLOSE", "reason": "time stop"}

    # --- funding flip exit ---
    side = pos["side"]  # "long_a_short_b" or "short_a_long_b"
    if side == "long_a_short_b" and fd > FUND_FLIP_EXIT:
        return {"action": "TRIM", "reason": "funding differential flipped adverse"}
    if side == "short_a_long_b" and fd < -FUND_FLIP_EXIT:
        return {"action": "TRIM", "reason": "funding differential flipped adverse"}

    # --- take profit ---
    if abs(snap.spread_z) <= Z_EXIT:
        return {"action": "CLOSE", "reason": f"convergence: spread z {snap.spread_z:.2f}"}

    return {"action": "HOLD"}

def compute_notional(sleeve_capital: float) -> float:
    return min(MAX_PAIRS_PCT * sleeve_capital, 500_000)  # hard cap per pair
```

The production system adds: real-time cointegration re-estimation (rolling 90-day window updated daily); cross-pair correlation monitoring (exit if two active pairs become >0.9 correlated — they are effectively the same bet); and CryptoDataAPI funding polling at 8h intervals for carry recalculation.

## Indicators / data used

- **Spread z-score** — log(Price_A / Price_B) normalized over 20-day rolling mean/std. The primary entry signal.
- **[[cointegration]] test (p-value)** — rolling 90-day Engle-Granger; defines the universe and the structural break kill trigger.
- **[[funding-rate]] (8h) per leg** — the core overlay; both legs must be monitored simultaneously for the differential.
- **[[open-interest]] (24h change) per leg** — OI gate confirms neither leg is in a trending regime.
- **Event risk** — `/api/v1/event/regime/score` or manual calendar check for per-asset catalyst risk.

## Example trade

**Setup (illustrative, not a historical backtest):**

- Pair: ETH-PERP (long) vs SOL-PERP (short) on Hyperliquid, 4h chart.
- 90-day cointegration p-value: 0.04 — strongly cointegrated.
- Spread z-score (log ETH/SOL over 20-day): **−2.3** (ETH is cheap vs SOL on a relative basis).
- Funding ETH-PERP (8h): **+0.005%** (~5.5% APY) — relatively neutral.
- Funding SOL-PERP (8h): **+0.062%** (~68% APY) — SOL crowd is heavily long.
- Funding differential: 0.005% − 0.062% = **−0.057%/8h** — long ETH / short SOL earns 0.057%/8h net carry. Threshold: −0.01% → **PASS**.
- OI changes: ETH +1.2%, SOL +4.2% — neither collapsing → **PASS**.
- Sleeve capital: $100,000. Spread notional: 7.5% = $7,500 per leg.

**Entry (2026-05-12):** Long ETH-PERP at $2,880 ($7,500 notional = 2.6 ETH). Short SOL-PERP at $172 ($7,500 notional = 43.6 SOL). Net carry: 0.057%/8h × $7,500 ≈ $4.28 per 8h period = **+$12.83/day carry income**.

**Hold (11 days):** Spread z-score reverts from −2.3 to −0.4 as ETH outperforms SOL. Carry accrued: 11 × $12.83 = **$141.10** over the hold period.

**Exit (day 11):** Spread z-score = −0.4 → ≤ +0.5 convergence threshold met. ETH-PERP exit at $3,040 (+5.6%); SOL-PERP cover at $165 (+4.1% on short).

**Net P&L (rough):** ETH long gain: +$420. SOL short gain: +$308. Carry income: +$141. Fees (2 × 2 legs × 0.045% taker ≈ $13.50). Net: **+$856 on $7,500 deployed** (~11.4% in 11 days; illustrative exceptional result). Contrast with funding-indifferent entry: if SOL funding had been 0.005% (no differential), carry would have been near-zero and the trade would have yielded only the spread return (~9.7%) with no structural income floor.

*(Illustrative round-trip. Not a backtest. Actual results vary. Not investment advice.)*

## Performance characteristics

Cost-corrected picture — conservative, based on strategy design principles and analogous pairs work:

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Unfiltered crypto pairs Sharpe ~0.5-0.8; funding differential adds both selectivity and carry floor |
| Expected max drawdown | ~18% | Dominated by cointegration-break events (fundamental regime shifts) |
| Win rate (per pair cycle) | ~55-65% | Pairs mean-reversion win rates; filter removes the low-carry (weakest thesis) entries |
| Avg hold period | 5-15 days | Spread convergence is not guaranteed quickly |
| Carry income contribution | 5-30 bps/day net | When differential is 0.03%+ per 8h, carry is meaningful relative to typical spread P&L |
| Breakeven cost budget | 25 bps round-trip | Perp taker ~4.5 bps × 4 legs + slippage; entry must be at favorable z-score |

**Cost overlay (Hyperliquid):**
- Taker fees: 4 legs (enter and exit both perps) × 0.045% = ~18 bps total.
- Slippage: minimal on major perps; 5-20 bps on mid-caps.
- Funding carry received (if differential ≥ 0.03%/8h over 10 days): ~+90 bps gross carry — a material buffer against slippage.

**What the filter buys:** By requiring the funding differential to agree, the strategy avoids entering pairs where both legs have similar funding (no carry income) and — crucially — avoids entering into the crowded leg at a time when carry compounds against the position. In a bull market where SOL funding is perpetually 0.06%/8h and ETH is 0.005%, an ETH-long/SOL-short spread captures ~0.055%/8h carry; the same spread in a neutral funding environment earns only the convergence return.

## Capacity limits

- **Per pair on Hyperliquid majors (ETH/SOL, ETH/BNB)**: ~$10-20M combined notional before both legs see meaningful market impact.
- **Cross-pair universe of 5-8 pairs**: ~$50M combined.
- **Hard constraint**: as notional grows, the spread entries must use maker orders, increasing execution lag and the risk of partial fills.
- The strategy is moderate-capacity but lower than pure momentum due to the cointegration requirement (illiquid pairs cannot be included).

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Cointegration breakdown (#5: The Regime Changed).** The structural anchor between the two assets dissolves — e.g., a Layer-1 token undergoes a fundamental shift (ecosystem fork, exploit, ecosystem exodus) that permanently separates its price behavior from the paired asset. When the spread does not mean-revert, the z-score stop limits the loss, but the time-stop and cointegration-break kill ensure the strategy does not hold a broken pair.
2. **Funding differential crowding (#4: Strategy Crowded).** If enough capital enters funding-differential pairs strategies, the crowded-leg funding compresses as arbitrageurs short it, and the differential shrinks. The entry threshold (0.01%/8h minimum) becomes increasingly hard to satisfy, collapsing signal frequency.
3. **Simultaneous directional move (#5).** If both legs drop together (e.g., BTC-correlated risk-off), the hedge is imperfect (the spread is not correlated with absolute BTC price). The strategy has residual long-beta or short-beta exposure when the correlation of the pair is not exactly 1.0. Delta-neutral sizing mitigates but does not eliminate this.
4. **Funding data latency (#7: Operational).** 8h funding settlements mean stale funding rates for up to 8h between periods. The spread entry uses the *last settled* funding, not the *current predicted* funding — use `/api/v1/derivatives/funding-rates` for predicted funding where available.
5. **Thin mid-cap perp liquidity (#6).** The strategy's edge depends on clean execution on both legs simultaneously. In thin perps, one leg may fill at a materially worse price than the other, entering the spread already off-center.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 18%** in any rolling 30-day window.
2. **Rolling 6-month Sharpe < 0** on a minimum 15 completed pair cycles.
3. **Funding differential anti-correlation**: the funding differential and spread z-score are anti-correlated (funding differential disagrees with spread direction in > 60% of signals) for 45+ consecutive days — the overlay is providing no information or actively inverting the signal.
4. **Cointegration collapse**: the rolling 90-day p-value of the primary pair exceeds 0.15 for 20+ consecutive days — the structural anchor is broken.

See [[when-to-retire-a-strategy]] for the broader framework.

## Instrument Structures

Pairs with funding differential deploys on the **pair** structure, layering a funding-carry overlay on top of the standard z-score entry logic.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Pair** | The defining structure. Two perp legs, long/short, dollar-neutral by hedge ratio. The funding differential is the additional filter: the strategy requires that the funding rate on the shorted leg exceeds the funding rate on the longed leg (earning carry alongside the spread reversion). |
| Single-asset | Not deployed. The carry overlay does not change the market-neutral construction — both legs are always held simultaneously. |
| Basket | Not deployed. The funding differential check is computed at the individual perp level; basket construction would blur the per-leg funding signal. |
| Cross-venue | The funding-differential concept extends naturally to [[hl-vs-cex-funding-divergence]], which is a cross-venue pair that earns funding spread between Hyperliquid and a CEX on the same underlying. That is a related but distinct strategy. |

The key mechanical difference from standard [[pairs-trading]]: the entry z-score threshold is *relaxed* when funding agrees (to 2.0σ) and *tightened* when it disagrees (to 2.5σ), so the carry signal affects entry selectivity, not leg sizing or the market-neutral construction itself.

## Advantages

- **Double confirmation before entry**: both the statistical signal (z-score) and the structural signal (funding differential) must agree, materially reducing false entries relative to z-score alone.
- **Positive carry floor**: when the funding differential is substantial (> 0.03%/8h differential), the strategy earns carry while waiting for convergence — an income floor that pure pairs strategies lack.
- **Self-funding patience**: carry income lets the strategy hold the spread longer before the time-stop bites, giving convergence more time to work.
- **Identifies "momentum-vs-value" dislocations**: the combination typically fires when retail is chasing one leg via perps and the structural spread is at a mean-reversion extreme — a dual behavioral misfiring.
- **Compatible with directional strategies**: the spread is market-neutral (hedged BTC beta); it can run alongside directional momentum strategies in the same book without adding correlated risk.

## Disadvantages

- **Reduced signal frequency**: the funding differential requirement blocks a significant fraction of z-score extremes where carry is absent. In neutral funding environments, the strategy may produce very few entries.
- **Complexity of simultaneous execution**: two legs must be entered (and exited) nearly simultaneously; slippage asymmetry between legs can enter the spread off-center. Larger positions require careful leg-by-leg execution.
- **Cointegration instability in crypto**: crypto pairs cointegration is less stable than in equities; regime shifts (exchange listings, protocol changes) break pairs more often. The 90-day rolling test catches this, but there is inherent lag.
- **8h funding granularity**: the funding clock means the carry can change significantly every 8 hours; a large funding flip mid-hold can turn a positive-carry trade into a negative-carry hold quickly.
- **Does not generate alpha from either component alone**: if momentum (the z-score extreme) or carry (the funding differential) alone were sufficient, there would be no need for the combination. The combination only outperforms if the *joint* signal is better than either individually — this must be verified empirically before live deployment.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (BIS, 2023). Funding rates as crowding signals: carry is explained by leveraged retail demand and limited arb capital. https://www.bis.org/publ/work1087.pdf
- Gatev, E., Goetzmann, W., Rouwenhorst, G. (2006), *Pairs trading: Performance of a relative-value arbitrage rule*, Review of Financial Studies. Foundational pairs evidence; the strategy's z-score trigger follows this framework.
- Avellaneda, M. and Lee, J.H. (2010), *Statistical arbitrage in the US equities market*, Quantitative Finance. Co-integration framework and mean-reversion timing.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — 8h funding for each leg; compute the differential in real time
- `GET /api/v1/derivatives/open-interest?coin=SOL` — per-leg OI for the OI gate
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=ETHUSDT` — long/short ratio as a secondary crowding check on each leg
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=200` — OHLCV for spread z-score computation

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SOLUSDT&limit=500` — funding history per leg for backtest spread entry reconstruction
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI) for both legs
- `GET /api/v1/backtesting/funding` — deep funding archive (2020+) for multi-regime cointegration and carry backtests

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

- [[pairs-trading]] — the underlying stat-arb primitive; this page is the funding-differential extension
- [[funding-rate-arbitrage]] — the canonical funding carry primitive; shares the same data rail
- [[hl-vs-cex-funding-divergence]] — cross-venue funding arbitrage (same asset, two venues); the nearest neighbor
- [[funding-filtered-momentum]] — single-asset funding-filtered directional strategy; related overlay logic
- [[crowded-long-funding-fade]] — fades directional momentum at funding extremes; shares behavioral rationale
- [[funding-rate]] — the underlying contract mechanism and funding conventions
- [[open-interest]] — the OI gate and the structural anchor for position quality
- [[perpetual-futures]] — the instrument carrying both legs of the spread
- [[cointegration]] — the statistical framework for the pairs signal
- [[stat-arb]] — the broader statistical arbitrage family this strategy belongs to
- [[spread-trading]] — the general spread entry/exit framework
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — cointegration-break and crowding risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
