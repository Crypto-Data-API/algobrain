---
title: "DeFi Yield / LP × Sentiment-Extreme Filter"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, defi, yield-farming, sentiment, behavioral-finance, contrarian, liquidity, quantitative, crypto, impermanent-loss]
aliases: ["DeFi LP Sentiment Entry", "Panic LP Deploy", "Fear-Extreme LP Entry", "DeFi Yield Contrarian Deployment", "LP Capital-Flight Entry"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, risk-bearing]
edge_mechanism: "DeFi LP yields are richest immediately after fear-driven capital flight from liquidity pools — pool TVL collapses as retail LPs panic-withdraw, compressing pool depth and elevating per-unit fee income; simultaneously, asset prices are depressed, providing a better IL-reference entry price. At greed extremes (TVL crowded, yields compressed), the LP is the marginal entrant earning the lowest per-unit fee income and holding assets at cycle highs with maximum IL exposure if price falls. Deploying LP and farming capital at Fear & Greed ≤ 20 extremes (when TVL is thin and yields are mechanically elevated) and de-risking at greed extremes (≥ 75) captures the yield-richness cycle while reducing IL-reference-price risk at the extremes of sentiment. The counterparty is the retail LP who deploys at greed peaks (TVL crowded, yields compressed) and withdraws at fear troughs (TVL thin, yields rich)."

data_required: [fear-greed-index, dex-pool-tvl, dex-pool-apr, dvol-btc, dvol-eth, realized-vol-4h, funding-rates, on-chain-stablecoin-flows]
min_capital_usd: 10000
capacity_usd: 10000000
crowding_risk: low

expected_sharpe: 0.9
expected_max_drawdown: 0.20
breakeven_cost_bps: 25

decay_evidence: "The TVL-yield cycle that this strategy exploits is durable as long as retail LPs remain sentiment-driven (deploy into bull narratives, withdraw into panic). Academic evidence for sentiment-driven retail crypto behavior is robust (e.g., Gurdgiev & O'Loughlin 2020, Da et al. 2015 on attention-driven retail trading). The DeFi-specific manifestation — panic TVL withdrawal compressing pool depth and inflating per-unit yields — is a mechanical consequence of AMM design and retail behavior, not a statistical anomaly. Compression risk: if LPs become sufficiently sophisticated to counter-cyclically deploy at sentiment troughs, the entry bonus would narrow. Unlikely at scale given retail LP behavioral patterns observed 2020–2025."

kill_criteria: |
  - 6-month net P&L (fee income − IL − gas) is negative for fear-extreme LP entries (sentiment filter not improving outcomes relative to continuous deployment)
  - 3 consecutive fear-extreme LP entries where pool TVL expanded rather than contracted during the fear window (capital-flight mechanism not operating; reassess pool universe or fear threshold)
  - 3 consecutive greed-extreme de-risking signals where pool yields remained elevated post-de-risk (de-risk was premature; recalibrate greed threshold upward)
  - Stablecoin flow data (dry-powder gauge) becomes unavailable for 30+ days (key data source failure)

related: ["[[defi-yield-regime-gate]]", "[[defi-yield-event-calendar]]", "[[contrarian-extremes]]", "[[sentiment-positioning-divergence]]", "[[onchain-capitulation-confluence]]", "[[stablecoin-sentiment-depeg-entry]]", "[[delta-neutral-yield-farming]]", "[[concentrated-liquidity]]", "[[defi-yield-farming]]", "[[post-panic-vol-selling]]", "[[put-protected-dip-buying]]", "[[impermanent-loss]]", "[[loss-versus-rebalancing]]", "[[fear-and-greed-index]]", "[[uniswap]]", "[[aave]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi]]"]
---

# DeFi Yield / LP × Sentiment-Extreme Filter

DeFi yield / LP sentiment-extreme filter deploys LP and yield-farming capital **after fear extremes** — when capital has already fled liquidity pools, pool depths are thin, and fee income per unit of LP is mechanically elevated — and **de-risks at greed extremes** — when TVL is crowded, yields are compressed to their minimum, and the LP holds assets near cycle highs with maximum impermanent-loss exposure if prices correct. The sentiment filter gates LP capital allocation to the entry points where the risk/reward of being an LP is structurally most favourable: entry price at sentiment lows, yield rates at their highest, and the subsequent TVL expansion (fear to neutral) provides both yield income and an IL-neutral or IL-negative price recovery. The counterparty is the retail LP who deploys LP capital at greed peaks (TVL maximally crowded, yields minimally rich) and withdraws at fear troughs (TVL thin, yields maximally rich).

**This is differentiated from [[contrarian-extremes]]** — that page deploys directional *long positions in BTC/ETH perps or spot* at sentiment extremes, capturing the mean-reversion of price to fair value. This page deploys *LP/yield capital* at sentiment extremes, capturing elevated fee income in a thin pool while the price recovery reduces IL. The instrument is different (LP vs directional position); the mechanism is different (fee income richness vs price mean-reversion); and the risk profile is different (LVR vs stop-loss). The two strategies are complementary: [[contrarian-extremes]] takes the directional bet; this page takes the yield-farming bet on the same price recovery.

**This is differentiated from [[defi-yield-regime-gate]]** — that page gates LP deployment on the *vol regime* (DVOL level, ADX, realized vol): deploy in low-vol, withdraw in high-vol. It is a continuous, vol-state-based gate. This page is *sentiment-extreme based and contrarian*: it deploys LP capital DURING high-vol/fear periods (when DVOL is elevated and ADX may be high) specifically because the fear-driven TVL flight has created the highest per-unit fee income. The two pages are **partially in tension**: the regime gate would say "don't deploy LP when DVOL is high"; this page says "deploy LP when DVOL is high AND sentiment is at a fear extreme." The resolution: this page requires an additional condition — the fear extreme must be accompanied by a stabilisation signal (see Gate 3), ensuring the LP is not deployed into a continuing LVR cascade but into a bottoming/recovering vol environment. When both gates are satisfied, this page overrides the regime gate's vol caution with the sentiment entry signal.

**This is differentiated from [[onchain-capitulation-confluence]]** — that page requires BOTH on-chain capitulation (exchange inflows spike, MVRV extreme) AND a Fear & Greed extreme simultaneously, to time directional *perp or spot entries*. This page focuses on LP-specific entry criteria: the yield mechanism (thin TVL → rich fee income), the IL-reference-price advantage of entry at sentiment lows, and the TVL expansion recovery trajectory. Different signal composition (yield-richness vs on-chain capitulation), different instrument (LP vs directional), different time horizon (position-scale LP deployment vs swing directional entry).

**This is differentiated from [[post-panic-vol-selling]]** — that page sells Deribit options short-vol after panic stabilisation, harvesting the elevated IV premium. This page deploys DeFi LP capital after panic, harvesting elevated AMM fee income. Both are contrarian post-panic strategies but on completely different instruments with different risk profiles: short options vs LP position.

## Edge source

Per [[edge-taxonomy]], **behavioral + risk-bearing**:

- **Behavioral (primary)** — Retail DeFi LPs exhibit strong sentiment-driven behaviour: they deploy LP capital into high-profile pools during bull narratives (TVL peaks at greed extremes) and withdraw en masse during fear events (TVL troughs at fear extremes). This behaviour is mechanically observed across every major DeFi fear event (March 2020, May 2021, June 2022 Celsius/3AC, November 2022 FTX). The sentiment-contrarian LP enters precisely when retail is fleeing — capturing the yield-richness created by that flight — and exits when retail returns in force (greed extreme), removing capital before the yield compression makes LP unattractive.
- **Risk-bearing (secondary)** — At sentiment extremes, entering an LP position requires accepting non-zero IL risk during a period of elevated market volatility. The fee income at fear troughs compensates for this risk bearing. The risk-bearing premium is the yield above the LP's long-run average rate that accrues specifically because retail LPs are unwilling to bear the risk at sentiment extremes.

## Why this edge exists

**The TVL-yield feedback mechanism:**

Pool APR (fee income per unit TVL) = (trading volume × fee tier) / TVL

At fear extremes:
1. **TVL collapses** as retail LPs panic-withdraw (TVL denominator falls sharply)
2. **Trading volume remains elevated** (panic-selling creates DEX flow) or rises (arb vol)
3. **APR spikes** — sometimes to 3–10× the pre-panic level — because fewer LPs are earning from the same or higher trading volume

At greed extremes:
1. **TVL peaks** as yield-chasing retail floods into high-APR pools (TVL denominator expands)
2. **Trading volume plateaus** or grows more slowly than TVL
3. **APR compresses** — yields thin to their lowest levels as capital crowds in

**The IL-reference-price advantage:**

IL is path-dependent from the LP's entry price. Entering at sentiment troughs means:
- Entry price is at or near cycle lows; the IL-reference-price is maximally advantageous for a recovery scenario
- If price recovers from the fear trough, the LP incurs minimal IL (recovery means the two tokens in the pool converge back toward the entry ratio)
- If price continues declining, IL is real but the elevated fee income partially offsets it, and the position was sized to manage this risk

**Who is on the other side:** the retail LP who entered at greed extremes (high TVL, compressed yield, peak asset prices). They entered when fee income was lowest and IL exposure was highest (assets at cycle highs). When sentiment normalises from fear to neutral, their position faces falling TVL (others who entered at greed are also exiting as yields compressed) and potentially recovering asset prices that normalise their IL — but they have already missed the highest-yield window that the fear-extreme entrant captured.

## Null hypothesis

Under the null, LP APR net of IL and gas is **sentiment-independent**: fear-extreme LP entries do not produce higher per-unit fee income or better IL outcomes than entries made at neutral sentiment (Fear & Greed 40–60).

Testable on historical DeFi data (Uniswap v3, Curve, Aave) by:
- Binning all LP entry dates by Fear & Greed decile
- Computing 30-day, 60-day, and 90-day LP return (fee income − IL − gas) for each decile
- Testing whether decile 1 (Fear & Greed ≤ 20) produces materially higher mean returns than decile 5 (Fear & Greed 40–60)

Prediction: decile 1 entries have highest fee income per unit TVL (TVL-richness effect) and best IL outcomes for assets that recover (not all do). The null is not fully rejected for assets in terminal decline.

## Rules

### Entry gate (all three conditions must be simultaneously active)

**Gate 1: Fear extreme confirmed**
- Fear & Greed index ≤ **20** for ≥ **2 consecutive days** (sustained fear, not a one-day spike).
- Source: `GET /api/v1/sentiment/fear-greed`.
- *Rationale:* single-day fear extremes can occur during brief intraday shocks that self-correct within hours; 2-day confirmation requires a sustained sentiment trough where retail LP withdrawals have had time to materially thin pool TVL.

**Gate 2: Yield richness confirmed**
- Target pool APR (from DeFi yield aggregator — not CryptoDataAPI) ≥ **1.5× its 30-day rolling average APR**.
- AND pool TVL ≤ **70% of its 30-day rolling average TVL** (TVL has actually thinned, not just APR numerically elevated by token price changes).
- Source: DeFiLlama API or Uniswap v3 subgraph (not CryptoDataAPI — pool-level yield data is not available via CryptoDataAPI).
- *Rationale:* confirms the TVL-flight mechanism is operating for this specific pool; not just a market-wide fear signal.

**Gate 3: Stabilisation signal (prevents entry into continuing cascade)**
- 4h realised vol of the pool's underlying token is **flat or declining** over the last 24 hours (not still spiking).
- Source: `GET /api/v1/volatility/regime/{symbol}` — vol regime label is `mean_reverting` or `normal` (not `vol_shock` or `expanding`).
- *Rationale:* deploying LP capital during an active cascade is entering into maximum LVR. The stabilisation check prevents entry during the worst LVR window and restricts entry to the post-cascade stabilisation phase.

**Gate 4: Stablecoin dry powder rising (optional confirmation)**
- Stablecoin supply 14-day flow is **positive** (capital parked in stablecoins is growing, indicating future deployment capacity that will normalise yields) — from `GET /api/v1/sentiment/stablecoins`.
- *Optional:* this gate increases signal quality but significantly reduces signal frequency. Use when the fear extreme is near a macro bottom candidate (all three prior gates already satisfied).

### De-risk trigger

- Fear & Greed ≥ **75** for ≥ **2 consecutive days** AND pool APR ≤ **80% of its 30-day average** (TVL-crowding confirmed by compressed yield).
- Action: withdraw 60–80% of LP position; retain 20–40% as a "core" position earning compressed but still positive yield.
- Full exit: Fear & Greed ≥ **80** for ≥ **3 consecutive days** (extreme greed sustained = maximum TVL crowding = yield at minimum; the LP entry bonus has been fully captured).

### Position sizing

- **Entry size:** 4–6% of portfolio per deployment (LP positions have open-ended IL risk; larger size at confirmed sentiment troughs after a major market event like FTX/3AC-style events).
- **Maximum concurrent LP exposure via this strategy:** 15% of portfolio (3 simultaneous positions at most, given correlation across pools in a market-wide fear event).
- **Leverage:** none. DeFi LP positions inherently involve price-exposure risk; adding leverage amplifies both IL and LVR beyond manageable limits for this strategy.

## Implementation pseudocode

```python
# defi_yield_sentiment_entry.py

from dataclasses import dataclass
from typing import Optional

# Entry gate thresholds
FEAR_EXTREME_MAX       = 20    # Fear & Greed ≤ 20 = fear extreme
FEAR_CONSECUTIVE_DAYS  = 2     # sustained for 2 days
APR_RICHNESS_MULT      = 1.5   # pool APR ≥ 1.5× 30d avg
TVL_THINNING_THRESHOLD = 0.70  # pool TVL ≤ 70% of 30d avg
STABLE_FLOW_GATE       = True  # optional: require positive 14d stablecoin flow

# De-risk thresholds
GREED_EXTREME_MIN      = 75    # Fear & Greed ≥ 75 = greed extreme
GREED_CONSECUTIVE_DAYS = 2
APR_CROWDED_THRESHOLD  = 0.80  # pool APR ≤ 80% of 30d avg = TVL-crowded
PARTIAL_EXIT_FRACTION  = 0.70  # de-risk 70% at greed trigger
FULL_EXIT_FG           = 80    # Fear & Greed ≥ 80 for ≥ 3 days = full exit

@dataclass
class SentimentState:
    fear_greed:              float
    fear_greed_days_at_level: int     # consecutive days at current level
    stable_14d_flow_usd:     float    # stablecoin supply 14d change

@dataclass
class PoolState:
    apr_current:  float
    apr_30d_avg:  float
    tvl_current:  float
    tvl_30d_avg:  float
    vol_regime:   str    # 'compressed' | 'normal' | 'mean_reverting' | 'expanding' | 'vol_shock'

def gate_entry(sentiment: SentimentState, pool: PoolState,
               use_stable_gate: bool = False) -> tuple[bool, list[str]]:
    fails = []
    # Gate 1: fear extreme
    if sentiment.fear_greed > FEAR_EXTREME_MAX:
        fails.append(f"Fear & Greed {sentiment.fear_greed:.0f} > {FEAR_EXTREME_MAX}")
    if sentiment.fear_greed_days_at_level < FEAR_CONSECUTIVE_DAYS:
        fails.append(f"only {sentiment.fear_greed_days_at_level}d at extreme; need {FEAR_CONSECUTIVE_DAYS}")
    # Gate 2: yield richness
    if pool.apr_30d_avg > 0:
        apr_ratio = pool.apr_current / pool.apr_30d_avg
        if apr_ratio < APR_RICHNESS_MULT:
            fails.append(f"APR ratio {apr_ratio:.2f}× < {APR_RICHNESS_MULT}× (yield not rich enough)")
    tvl_ratio = pool.tvl_current / pool.tvl_30d_avg if pool.tvl_30d_avg > 0 else 1.0
    if tvl_ratio > TVL_THINNING_THRESHOLD:
        fails.append(f"TVL ratio {tvl_ratio:.2f} > {TVL_THINNING_THRESHOLD} (TVL not sufficiently thinned)")
    # Gate 3: vol stabilisation
    if pool.vol_regime in ('expanding', 'vol_shock'):
        fails.append(f"vol regime '{pool.vol_regime}' — not yet stabilised; wait for mean_reverting/normal")
    # Gate 4: optional stablecoin dry-powder gate
    if use_stable_gate and sentiment.stable_14d_flow_usd <= 0:
        fails.append(f"stablecoin 14d flow {sentiment.stable_14d_flow_usd/1e9:.2f}B ≤ 0 (dry powder not building)")
    return len(fails) == 0, fails

def should_derisk(sentiment: SentimentState, pool: PoolState,
                  greed_consecutive: int, position_fraction: float) -> Optional[dict]:
    # Partial de-risk at greed + yield compression
    if (sentiment.fear_greed >= GREED_EXTREME_MIN
            and greed_consecutive >= GREED_CONSECUTIVE_DAYS
            and pool.apr_30d_avg > 0
            and pool.apr_current / pool.apr_30d_avg <= APR_CROWDED_THRESHOLD
            and position_fraction > (1 - PARTIAL_EXIT_FRACTION)):
        return {
            'action': 'PARTIAL_EXIT',
            'exit_fraction': PARTIAL_EXIT_FRACTION,
            'reason': (f"greed={sentiment.fear_greed:.0f} for {greed_consecutive}d; "
                       f"APR ratio={pool.apr_current/pool.apr_30d_avg:.2f}× ≤ {APR_CROWDED_THRESHOLD}")
        }
    # Full exit at extreme sustained greed
    if sentiment.fear_greed >= FULL_EXIT_FG and greed_consecutive >= 3:
        return {
            'action': 'FULL_EXIT',
            'reason': f"extreme greed {sentiment.fear_greed:.0f} for {greed_consecutive}d"
        }
    return None
```

## Indicators / data used

- **Fear & Greed index** — `GET /api/v1/sentiment/fear-greed` — primary entry trigger; ≤ 20 for ≥ 2 days = Gate 1. Source: [[cryptodataapi-sentiment]].
- **Fear & Greed history** — `GET /api/v1/market-intelligence/fear-greed-history` — timeseries for backtesting signal frequency and threshold calibration. Source: [[cryptodataapi-market-intelligence]].
- **Stablecoin flows** — `GET /api/v1/sentiment/stablecoins` — 14d/90d stablecoin supply change; positive 14d flow = dry powder accumulating = future LP deployment capital incoming (Gate 4, optional). Source: [[cryptodataapi-sentiment]].
- **Vol regime per asset** — `GET /api/v1/volatility/regime/{symbol}` — stabilisation check (Gate 3); entry only when `mean_reverting` or `normal`, not `expanding` or `vol_shock`. Source: [[cryptodataapi-regimes]].
- **Vol-stress composite** — `GET /api/v1/volatility/regime/score` — market-wide 0–100 vol-stress score; secondary Gate 3 check (< 55 preferred at entry).
- **Pool APR and TVL** — *Not available via CryptoDataAPI.* Use DeFiLlama API (`https://yields.llama.fi/pools`) or Uniswap v3 subgraph (The Graph) for pool-specific APR and TVL data. This data is required for Gate 2 and cannot be substituted with CryptoDataAPI endpoints.
- **Market health composite** — `GET /api/v1/market-health/summary` — overall market health score; use as a secondary qualifier (deploy only when health score is recovering from its trough, not still declining).

## Example trade

**Setup (illustrative — June 2022 Celsius/3AC fear event, ETH/USDC Uniswap pool)**

- Fear & Greed: 6 (extreme fear for 4 consecutive days). Gate 1: PASS.
- ETH/USDC 0.3% Uniswap pool: TVL collapsed from $320M to $85M (27% of 30d avg). Gate 2 TVL check: PASS (0.27 < 0.70 threshold). Pool APR: 48% annualised (was 12% prior 30d avg = 4× richness). Gate 2 APR check: PASS (4× ≥ 1.5× threshold).
- Vol regime for ETH: `mean_reverting` (4h RV peaked and rolling over). Gate 3: PASS.
- Stablecoin 14d flow: +$8B (dry powder accumulating). Gate 4 (optional): PASS.
- All 4 gates pass. Portfolio $200,000. Entry: 5% × $200K = $10,000 into ETH/USDC pool.

**7-week outcome:**
- APR remained elevated (28% avg over 7 weeks) as TVL recovered slowly.
- Fee income: $10,000 × 28% × (7/52) = **$377**.
- ETH price recovered from $1,050 entry to $1,320 (+ 26%); IL = ~3.5% of position on the price recovery (IL = 2√(1.26) / (1 + 1.26) − 1 ≈ −3.5%).
- IL dollar cost: $10,000 × 3.5% = **$350 IL**.
- Net P&L: $377 fees − $350 IL − $20 gas = **+$7 net** (approximately break-even with no gas amplification due to IL).
- Compare to not deploying: $0 fee income, held in cash; missed fee income = −$377.

**De-risk trigger at T + 14 weeks:**
- Fear & Greed: 72 (recovering to near-greed). Pool APR: 9.5% (compressed below 80% of 30d avg of 14%). Greed gate partially triggered: partial de-risk of 70% of position.

*(Illustrative. The June 2022 example uses approximate historical prices. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Net of IL, gas, and opportunity cost of idle capital |
| Expected max drawdown | ~20% | Scenario where the underlying enters a structural bear (ETH post-LUNA, etc.) — IL exceeds elevated fee income |
| Signal frequency | 4–8 per year | Fear & Greed ≤ 20 for 2 days occurs roughly 4–8 times annually |
| Average hold duration | 4–12 weeks | From fear entry to greed de-risk trigger |
| Breakeven cost | 25 bps round-trip | Includes estimated pool gas (L2: < $30/round trip) and IL at entry/exit |
| APR richness at entry | 1.5–5× normal | Empirically observed at major fear events (May 2021, June 2022, November 2022) |

**Cost overlay:** The primary cost driver is IL, not gas (especially on L2). IL is positive when the pool's token price moves significantly after LP entry. The strategy is most favourable when the fear extreme coincides with a bottoming price level (minimal subsequent downside); if the underlying continues falling after entry, IL compounds. Gate 3 (stabilisation) mitigates but cannot fully prevent this risk.

## Capacity limits

- **Per pool:** `capacity_usd: 10000000` — above ~$10M per pool entry at a fear extreme, the LP's entry itself begins to lift pool TVL noticeably and reduces the yield-richness it is deploying into.
- **Cross-pool:** The strategy can run across multiple pools simultaneously (e.g., ETH/USDC, BTC/USDC, ETH/stETH) during market-wide fear events. Total concurrent LP via this strategy: 15% of portfolio.

## What kills this strategy

1. **Structural bear market beneath the fear extreme (#1: Primitive degradation).** If the fear extreme is not a sentiment trough but rather the beginning of a structural bear (LUNA-style algorithmic failure, FTX contagion spreading to all DeFi TVL), the recovery assumption fails. Gate 3 (stabilisation) provides partial protection but cannot detect multi-month structural bear trends. Mitigate: position sizing (5% max per entry), and use [[defi-yield-regime-gate]] as a parallel filter (if the regime gate also says "withdraw," do not enter even if sentiment is at a fear extreme).
2. **Pool death post-entry (#4: Crowding / data).** If a specific pool's token enters a death spiral (LUNA, UST), the pool TVL collapses to zero, fee income disappears, and IL goes to near-100%. Mitigate: pool diversification (no single pool > 5% of portfolio), avoid pools where the underlying has no redemption mechanism or sponsor.
3. **IL exceeds elevated fee income (#2: Regime change).** If the underlying asset continues falling 30–50% after LP entry (sustained bear, not a fear spike), IL grows faster than fee income accrues. At −40% price move from entry, IL is approximately 9% of position; at 48% APR, 3 weeks = only 2.8% fee income. IL dominates for large directional moves. Mitigate: the stabilisation gate (Gate 3) requires vol to be rolling over; enter only when the price move appears to be topping out.
4. **Gas cost amplification on Ethereum mainnet (#6: Data / execution).** At $400 gas per transaction on mainnet, two transactions = $800 overhead. For a $10,000 position, this is 8% round-trip cost — completely erases the fee income advantage. Mitigate: L2 deployment only at sub-$100K position sizes.

## Kill criteria

Pause or retire on any of:

1. **6-month net LP P&L (fee income − IL − gas) is negative for fear-extreme entries** — the sentiment filter is not correctly identifying recoverable fear troughs; reassess entry thresholds or pool universe.
2. **Three consecutive entries where vol regime was `mean_reverting` at entry but pool IL exceeded fee income by 2× over the next 30 days** — Gate 3 (stabilisation) is not sufficient protection against sustained downtrends; add an additional on-chain capitulation gate (per [[onchain-capitulation-confluence]]).
3. **Fear & Greed ≤ 20 occurs for more than 20% of calendar days** (chronic fear = bear market; threshold too commonly hit; raise threshold to ≤ 15).
4. **Pool-level data source (DeFiLlama/Uniswap subgraph) becomes unavailable for 30+ days** (Gate 2 cannot be evaluated; suspend new entries).

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Entry at the best risk/reward point** — deploying at TVL troughs captures the highest per-unit yield while entering at or near price lows minimises IL-reference-price exposure.
- **Behavioral mispricing is durable** — retail LPs consistently deploy at greed peaks and withdraw at fear troughs; this behaviour is observed across every major DeFi market event 2020–2025.
- **Complementary to [[defi-yield-regime-gate]]** — the regime gate handles continuous vol; this page adds the contrarian sentiment entry dimension. The two can be run together as a combined filter.
- **Low crowding risk** — contra-sentiment DeFi LP deployment is not a common institutional strategy; the signal frequency (4–8 times/year) and capital requirements mean few operators pursue it systematically.

## Disadvantages

- **Pool-level data not on CryptoDataAPI** — Gate 2 (yield richness + TVL thinning) requires DeFiLlama or Uniswap subgraph data, adding a second data dependency not covered by the canonical CryptoDataAPI stack.
- **IL risk is open-ended** — the LP position has no hard stop; price can continue falling after entry for months if the fear extreme is not a bottom. Position sizing discipline (5% max per entry) is the primary risk control.
- **Signal frequency limits capital deployment** — Fear & Greed ≤ 20 for 2 consecutive days occurs only 4–8 times per year; the strategy is inactive for most of the year, leaving capital idle or requiring a parallel deployment strategy.
- **Partially in tension with [[defi-yield-regime-gate]]** — the regime gate says "do not deploy LP when DVOL is high"; fear extremes almost always coincide with high DVOL. Operators must consciously override the regime gate's caution when the sentiment entry conditions are met.

## Sources

- [[defi-yield-regime-gate]] — the vol-regime gate that governs baseline LP deployment; this page adds the contrarian sentiment entry dimension
- [[contrarian-extremes]] — the directional analog of this strategy (perp/spot longs at fear extremes vs LP deployment at fear extremes)
- [[onchain-capitulation-confluence]] — complementary on-chain capitulation confirmation for the deepest fear-extreme entries
- Gurdgiev, C. & O'Loughlin, D. (2020). "Herding and anchoring in cryptocurrency markets: Investor reaction to fear and uncertainty." *Journal of Risk and Financial Management*.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — Gate 1: current Fear & Greed index (≤ 20 for 2 consecutive days = entry trigger)
- `GET /api/v1/sentiment/stablecoins` — Gate 4 (optional): 14d stablecoin supply flow (+ve = dry powder building)
- `GET /api/v1/volatility/regime/{symbol}` — Gate 3: per-asset vol regime (enter only when `mean_reverting` or `normal`)
- `GET /api/v1/volatility/regime/score` — Gate 3 secondary: market-wide vol-stress (< 55 preferred)
- `GET /api/v1/market-health/summary` — market health scores; use as recovery-trend confirmation

**Historical data:**
- `GET /api/v1/market-intelligence/fear-greed-history` — Fear & Greed timeseries for backtesting signal frequency
- `GET /api/v1/sentiment/stablecoins/remote-history?days=365` — annual stablecoin supply history for threshold calibration

*Note: Pool-specific APR and TVL data (Gate 2) are not available via CryptoDataAPI. Use DeFiLlama (`https://yields.llama.fi/pools`) or the Uniswap v3 subgraph (via The Graph) for pool-level analytics.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/sentiment/fear-greed"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]], [[cryptodataapi-regimes]].

## Related

- [[defi-yield-regime-gate]] — continuous vol-regime gate for LP deployment; composable baseline layer
- [[defi-yield-event-calendar]] — event-calendar-based withdrawal protocol; composable with this sentiment entry page
- [[contrarian-extremes]] — directional fear-extreme long (perp); conceptual parallel, different instrument
- [[sentiment-positioning-divergence]] — sentiment + derivative positioning divergence for directional entries; different instrument
- [[onchain-capitulation-confluence]] — on-chain + sentiment dual-confirmation for deepest bottoms; composable gate
- [[stablecoin-sentiment-depeg-entry]] — sentiment + stablecoin discount entry; structural parallel for stablecoin depeg trades
- [[post-panic-vol-selling]] — post-panic options vol selling; parallel contrarian strategy on a different instrument
- [[put-protected-dip-buying]] — post-capitulation dip-buy with tail hedge; directional analog with protective option
- [[delta-neutral-yield-farming]] — hedged LP; composable with this sentiment entry filter
- [[concentrated-liquidity]] — LP range management; use post-entry as the range placement tool
- [[fear-and-greed-index]] — the sentiment indicator underlying Gate 1
- [[impermanent-loss]] — the IL mechanism this strategy manages via entry timing
- [[loss-versus-rebalancing]] — the formal LVR framework
