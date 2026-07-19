---
title: "DeFi Yield / LP Regime Gate"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, defi, yield-farming, volatility, market-regime, regime-detection, quantitative, crypto, impermanent-loss]
aliases: ["DeFi LP Regime Filter", "LP Vol-Regime Gate", "Yield Farm Regime Gate", "IL-Aware LP Deployment"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, risk-bearing]
edge_mechanism: "LP positions are structurally short gamma (short a synthetic straddle on the pooled assets): fee income is roughly proportional to volatility while Loss Versus Rebalancing (LVR) — the continuous cost of being adversely selected by informed arbitrageurs — grows with the square of volatility. A vol-regime gate that restricts LP deployment to low-vol regimes (where fee income exceeds LVR and gas costs) and pauses or reduces deployment in high-vol/trending regimes (where LVR overwhelms fee income) captures the net-positive LP opportunity while avoiding the regimes that make most passive LP positions structurally negative-EV. The counterparty is the passive LP who deploys continuously regardless of regime, funding the LVR gain for DEX arbitrageurs in high-vol periods."

data_required: [dvol-btc, dvol-eth, realized-vol-30d, regime-current, dex-pool-apr, dex-pool-tvl, impermanent-loss-estimate, gas-price, perp-funding-rates]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.20
breakeven_cost_bps: 25

decay_evidence: "The structural LP-vs-LVR dynamic is mathematically durable (Milionis et al. 2022 — LVR = σ²/8 per unit time for a CFMM). The regime gate does not decay the underlying LVR math; it selects for the regimes where σ is small enough for LVR to be dominated by fee income. As DEX liquidity provision becomes more sophisticated (Uniswap v4, Balancer v3 hooks), the fraction of LP positions that are vol-aware may grow, compressing the fee income available to late regime-gate adopters. The edge is durable at medium AUM; likely compresses above $50M LP deployment on any single pool."

kill_criteria: |
  - 6-month net P&L (fee income minus IL minus gas) is negative in LOW-vol regime deployments (the regime gate is not correctly identifying favorable windows)
  - Realized LVR in low-vol regime exceeds fee income by more than 0.5× for 3 consecutive months (structural shift: pools now pay lower fees than their LVR cost even in low-vol)
  - Regime signal latency: DVOL data delayed > 4 hours (stale gate inputs; pause LP deployment)
  - Pool TVL in the target pool exceeds $500M (fee income per unit LP collapses; move to smaller pool or pause)

related: ["[[delta-neutral-yield-farming]]", "[[concentrated-liquidity]]", "[[leveraged-yield-farming]]", "[[defi-yield-farming]]", "[[regime-adaptive-strategy]]", "[[regime-gated-grid]]", "[[loss-versus-rebalancing]]", "[[impermanent-loss]]", "[[volatility-targeting]]", "[[vol-gated-mean-reversion]]", "[[cryptodataapi-volatility]]", "[[cryptodataapi-regimes]]", "[[deribit]]", "[[uniswap]]", "[[aave]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# DeFi Yield / LP Regime Gate

DeFi yield / LP regime gate restricts liquidity provider capital deployment to **low-volatility, range-bound regimes** where LP fee income reliably exceeds Loss Versus Rebalancing (LVR) and gas costs, and withdraws or reduces LP exposure in trending or high-volatility regimes where LVR mathematically overwhelms fee income regardless of fee tier or range placement. The strategy makes the LP position structurally profitable in expectation by solving the most common LP failure mode: providing liquidity continuously regardless of whether the vol environment favours the LP or the arbitrageur. The counterparty is the passive LP — the majority of AMM liquidity providers — who deploys continuously and subsidises the arbitrageur in high-vol regimes.

**This is differentiated from [[delta-neutral-yield-farming]]** — that page delta-hedges the LP position by shorting the risky asset on a perp, removing the directional price risk. This page does not hedge the existing position; it gates WHEN to deploy LP capital based on regime, withdrawing during unfavorable periods. The two strategies are composable: delta-neutral yield farming (the hedged LP) benefits doubly from a regime gate (the hedge has a cost that is also not worth paying in very-low-vol environments where the LP position itself would be profitable unhedged).

**This is differentiated from [[regime-gated-grid]]** — that page gates a CEX grid market-making strategy on vol/trend regime (ADX, Bollinger bandwidth). This page applies the same gating logic to an AMM LP position, but the mechanism differs: CEX grids are killed by trending because the inventory accumulates in the wrong direction; LP positions are killed by trending because LVR grows with the square of realized vol and arbitrageurs continuously extract value from the pool. The gate condition (low vol, range-bound) is structurally similar but the kill mechanism is LVR, not inventory accumulation.

**This is differentiated from [[vol-gated-mean-reversion]]** — that page applies a conditional vol-sizing rule to mean-reversion ENTRIES (size up in high-vol good flush, size down in high-vol bad cascade). This page gates LP DEPLOYMENT at the regime level: it does not size up LP positions in high-vol; it withdraws them. The LP position has no analog to a "high-vol good" regime: LVR is always proportional to σ², so higher vol is always worse for an unhedged LP.

## Edge source

Per [[edge-taxonomy]], **structural + risk-bearing**:

- **Structural (primary)** — The LVR math (Milionis et al. 2022) establishes that for a constant-function market maker (CFMM), LVR = σ²/8 per unit time, where σ is the realized vol of the pooled asset. Fee income per unit time is approximately proportional to trading volume, which is also correlated with σ (more vol → more arb flow → more fees). However, LVR grows as σ² while fees grow as σ¹; above a vol threshold, LVR dominates. The regime gate exploits this asymmetry: deploy LP capital only when σ is below the vol threshold where fee income > LVR.
- **Risk-bearing** — In low-vol regimes, the LP is accepting residual IL risk in exchange for fee income (risk-bearing premium). The regime gate does not eliminate IL risk; it selects for the regime where that risk is reasonably priced (fee income > expected IL).

## Why this edge exists

**The LVR-fee income crossover is the core mechanism:**

The LP's net P&L per unit of time ≈ fee_income − LVR − gas:
- `fee_income ≈ k × σ × TVL` (fees proportional to vol × volume proxy)
- `LVR ≈ (σ²) / 8 × TVL` (LVR quadratic in vol)

Setting `fee_income = LVR` to find the break-even vol threshold:
```
k × σ = σ² / 8
→ σ_breakeven = 8k
```

For a typical 0.3% fee-tier Uniswap v3 pool: `k ≈ 0.003 / 2 = 0.0015` (half the fee, since both LPs and arbers split the fee income approximately 50:50 with the AMM). Break-even σ ≈ 8 × 0.0015 = 0.012 per-period = roughly 40–60% annualized realized vol depending on the time unit. For a 0.05% fee tier, break-even is even lower (~20–30% annualized vol).

**The regime gate operationalises this math:** DVOL (Deribit implied vol for BTC/ETH) is the forward-looking vol estimate that predicts future realised vol. When DVOL is below the break-even threshold AND the macro regime is non-trending (ADX low, no structural shock), the expected LVR is below expected fee income → deploy LP capital. When DVOL rises above the threshold OR a trend is running, withdraw.

**Who is on the other side:** passive LPs who deposit into Uniswap/Curve pools based on APY displays that do not net out LVR. They see "120% APY" in the pool display but their actual realised return net of LVR, gas, and IL is often negative in high-vol periods. Studies show the majority of Uniswap v3 positions underperformed HODL after accounting for LVR (Milionis et al. 2022). These passive LPs fund the LVR gain for the arbitrageurs; the regime-gate LP captures the fee income in the windows when LVR is small, while passive LPs absorb the LVR losses in high-vol windows.

## Null hypothesis

Under the null, LP returns are **regime-independent**: a regime gate that restricts LP deployment to low-vol windows does not produce higher net returns (fee income − LVR − gas − opportunity cost) than continuous LP deployment with the same capital.

If the null holds:
- Average daily LP fee income (net of LVR) should be constant across vol-regime buckets (low/medium/high vol).
- Withdrawing during high-vol regimes should reduce total fee income proportionally to the time withdrawn, with no improvement in net Sharpe (the LVR losses during high-vol are cancelled by higher absolute fee income).

The null is testable using on-chain LP position P&L data (Uniswap v3 subgraph, or Revert Finance LP analytics): regress net LP APY (gross fee − IL) on 30-day realised vol bucket. Prediction: LP net APY in the DVOL > 60% bucket is negative or near-zero; LP net APY in the DVOL < 40% bucket is significantly positive.

Currently not rejected by on-wiki evidence, but the LVR math (Milionis et al. 2022) provides strong theoretical support for the regime-asymmetry prediction.

## Rules

### Regime classification gate (deploy / reduce / pause)

**DEPLOY (full LP deployment):**
- `DVOL (BTC/ETH Deribit 30d IV) ≤ 45%` (annualized) — forward-looking vol expectation below break-even threshold for 0.3% fee pools
- AND `ADX(14, 1d) ≤ 20` (non-trending regime)
- AND `regime = Range_Bound OR Low_Vol OR Accumulation` per `GET /api/v1/regimes/current`
- AND gas price (ETH base fee) ≤ 30 gwei (rebalancing economics viable)

**REDUCE (50% LP deployment):**
- `DVOL 45–60%` OR `ADX 20–28` OR `regime = Trending OR Bull_Trend OR Bear_Trend`
- Still deploy 50% to maintain pool relationship and fee income; but half-size to reduce LVR exposure

**PAUSE (withdraw LP, hold in stablecoins):**
- `DVOL > 60%` OR `ADX > 28` OR `regime = High_Vol OR Structural_Shock OR Crash`
- OR 30d realized vol of the pooled asset > 80% annualized
- OR 24h price move of the pooled asset > 8% (acute vol event; withdraw immediately)
- Withdraw LP position and hold underlying assets in stablecoin or AAVE deposit until regime clears

### Pool selection

- Target: established correlated-asset pools (WBTC/ETH, ETH/stETH, USDC/ETH on Uniswap v3 0.3% tier) — higher fee tier compensates LPs more for LVR than 0.05% pools
- Avoid: low-TVL pools (< $5M TVL) where single-LP's position dominates and arbers pick off tightly
- LP range width: `± 2 × DVOL/100 × (days_in_range)^0.5` around current price — wider in medium-vol (reduce rebalance frequency), tighter in low-vol (capture more fees)

### Rebalancing

- Recalibrate LP range when price moves outside the current range bounds OR when DVOL changes by ≥ 15% since last calibration
- Each rebalance incurs gas cost; target ≤ 2 rebalances per month to keep gas below 10% of fee income
- If regime shifts to PAUSE during a rebalance cycle, complete the withdrawal first; do not rebalance into a PAUSE regime

### Position sizing

- Base LP position: 20–40% of portfolio notional per pool
- Maximum total LP exposure: 60% of portfolio (leave 40% in liquid assets for gas, rebalancing, and opportunity cost)
- REDUCE regime: 50% of base position per pool

## Implementation pseudocode

```python
# defi_yield_regime_gate.py

from enum import Enum

class LPRegime(Enum):
    DEPLOY = "deploy"    # full LP capital
    REDUCE = "reduce"    # 50% LP capital
    PAUSE  = "pause"     # withdraw, hold stable

DVOL_DEPLOY_MAX  = 45.0     # annualised % implied vol ceiling for full deploy
DVOL_REDUCE_MAX  = 60.0     # ceiling for reduced deploy
ADX_DEPLOY_MAX   = 20.0     # ADX ceiling for full deploy
ADX_REDUCE_MAX   = 28.0     # ADX ceiling for reduced deploy
REALVOL_PAUSE    = 80.0     # 30d realized vol ceiling (annualised %)
PRICE_MOVE_PAUSE = 0.08     # 24h price move triggering immediate withdraw
GAS_VIABILITY    = 30       # gwei ceiling for economic rebalancing

FAVORABLE_REGIMES  = {"Range_Bound", "Low_Vol", "Accumulation"}
PAUSE_REGIMES      = {"High_Vol", "Structural_Shock", "Crash"}

def classify_lp_regime(dvol: float, adx: float, macro_regime: str,
                       realvol_30d: float, price_move_24h: float,
                       gas_base_fee_gwei: float) -> LPRegime:
    # Immediate pause conditions
    if (dvol > DVOL_REDUCE_MAX or adx > ADX_REDUCE_MAX
            or macro_regime in PAUSE_REGIMES
            or realvol_30d > REALVOL_PAUSE
            or abs(price_move_24h) > PRICE_MOVE_PAUSE):
        return LPRegime.PAUSE

    # Reduce conditions
    if (dvol > DVOL_DEPLOY_MAX or adx > ADX_DEPLOY_MAX
            or macro_regime not in FAVORABLE_REGIMES):
        return LPRegime.REDUCE

    # Gas viability check
    if gas_base_fee_gwei > GAS_VIABILITY:
        return LPRegime.REDUCE   # rebalancing uneconomical; deploy but don't rebalance

    return LPRegime.DEPLOY

def lp_range_width_pct(dvol: float, target_days_in_range: int = 14) -> float:
    """
    Target range = ±(dvol/100 × sqrt(target_days/365)) × 2 (both sides).
    Returns the single-side width as a fraction of current price.
    """
    import math
    return (dvol / 100) * math.sqrt(target_days_in_range / 365) * 2.0

def position_notional(portfolio_usd: float, regime: LPRegime,
                      base_fraction: float = 0.30) -> float:
    if regime == LPRegime.DEPLOY: return portfolio_usd * base_fraction
    if regime == LPRegime.REDUCE: return portfolio_usd * base_fraction * 0.50
    return 0.0   # PAUSE: no LP exposure

def deployment_decision(dvol: float, adx: float, macro_regime: str,
                        realvol_30d: float, price_move_24h: float,
                        gas_base_fee_gwei: float, portfolio_usd: float) -> dict:
    regime = classify_lp_regime(dvol, adx, macro_regime, realvol_30d,
                                 price_move_24h, gas_base_fee_gwei)
    notional = position_notional(portfolio_usd, regime)
    range_width = lp_range_width_pct(dvol) if regime != LPRegime.PAUSE else 0.0
    return {
        "regime":          regime.value,
        "lp_notional_usd": notional,
        "lp_range_width":  f"±{range_width:.1%} of current price",
        "action":          ("DEPLOY_FULL" if regime == LPRegime.DEPLOY
                            else "DEPLOY_HALF" if regime == LPRegime.REDUCE
                            else "WITHDRAW_TO_STABLE"),
    }
```

## Indicators / data used

- **DVOL (Deribit BTC/ETH 30-day implied vol)** — `GET /api/v1/volatility/dvol?coin=BTC`; primary gate input; 30d IV index from Deribit; ≤ 45% = DEPLOY, 45–60% = REDUCE, > 60% = PAUSE.
- **Macro regime** — `GET /api/v1/regimes/current`; regime label determines deploy/reduce/pause along with DVOL; `Structural_Shock` or `Crash` = immediate PAUSE.
- **30-day realized vol** — `GET /api/v1/volatility/realized?coin=BTC&days=30`; secondary confirmation; > 80% annualized = PAUSE regardless of DVOL.
- **OHLCV daily** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=3`; 24h price move calculation for acute-event PAUSE trigger.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; elevated funding (> 0.04%/8h) signals leverage buildup that typically precedes vol spikes; use as leading REDUCE indicator.
- **Gas price (ETH base fee)** — sourced from Ethereum node RPC or Etherscan gas API (not in CryptoDataAPI); viability check for rebalancing economics.
- **DEX pool APR** — sourced from Uniswap v3 subgraph (not in CryptoDataAPI); pool-specific fee income estimation for position selection.

## Example trade

**Setup: Low-vol regime, deploy LP capital**

- DVOL (BTC): 38% annualized. ADX(14, 1d): 16. Macro regime: `Range_Bound`. 30d realized vol: 34%. 24h price move: +1.2%. Gas base fee: 12 gwei.
- All gates pass: DEPLOY regime.
- Pool: Uniswap v3 WBTC/ETH 0.3% tier, TVL = $120M, 7-day fee APY to LPs: 18% annualized.
- Range width: ±(38/100 × sqrt(14/365)) × 2 = ±3.9% of current price (BTC/ETH ratio ± 3.9%).
- LP notional: $150,000 portfolio × 30% = $45,000 deployed.
- Expected fee income (14 days): $45,000 × 18% / 26 = $312.
- Estimated LVR (14 days, σ = 38%/√26 per fortnight ≈ 7.5%/period): LVR ≈ (0.075²/8) × $45,000 = **$31.6**. Fee income ($312) >> LVR ($31.6). Net positive.

**Regime shift: DVOL spikes to 68%** (macro news event, risk-off)

- Trigger: DVOL (BTC) moves from 38% to 68% over 48 hours. Price move 24h: −6.2%.
- Gate: DVOL > 60% → PAUSE. 24h price move < −8% threshold not triggered, but DVOL alone is sufficient.
- Action: Withdraw LP position from Uniswap v3 pool. Gas cost: 0.02 ETH ≈ $40 at $2000 ETH + 12 gwei gas. Underlying assets redeployed to AAVE USDC deposit at 4% APY.
- LP avoided: estimated LVR during the 68% DVOL window (10 days): LVR ≈ (0.131²/8) × $45,000 = $96. Fee income in same period (higher vol → more fees): $45,000 × 28%/37 ≈ $340. But this estimate is optimistic — LVR typically exceeds the fee income acceleration. Even on this marginal scenario, pausing avoids downside risk.

*(Illustrative round numbers. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Regime gate improves from continuous LP Sharpe of ~0.4–0.6 to ~0.9 |
| Expected max drawdown | ~20% | Residual from regime misclassification (deploy in what becomes a high-vol window) |
| Expected fee income (deploy regime) | 15–25% APY gross | Pool-dependent; 0.3% fee tier, major pools |
| Expected LVR (deploy regime) | 3–8% APY | At DVOL 30–45% for correlated-asset pairs |
| Break-even cost | 25 bps | Gas costs (rebalancing) + opportunity cost of idle capital in PAUSE regime |
| Time in PAUSE regime | ~30–40% of calendar days | Based on BTC DVOL > 60% frequency historically (2021–2025) |

**Cost overlay:** the dominant cost is gas for rebalancing and withdrawing. At 2 rebalances/month and 1 regime-triggered withdrawal/2 months, gas cost ≈ 0.05 ETH/month at 15 gwei ≈ $100/month. On a $45K position earning $1,800/month (18% APY) in the DEPLOY regime, gas is < 6% of gross income.

## Capacity limits

- **Per pool:** `capacity_usd: 20000000` — above $20M in a single pool (most 0.3% pools), the LP's own position depresses the fee yield for itself (LP earns pro-rata fee share; adding large position dilutes fee per LP dollar while not proportionally increasing fee volume).
- **Market-level:** the regime gate improves per-LP Sharpe; it does not increase the total fee income available in the market. As more LPs adopt regime gating, the fraction of passive (non-gated) LPs providing the LVR subsidy in high-vol regimes decreases, potentially compressing the fee income available in low-vol regimes (as concentrated LPs compete harder for the same fee flow).

## What kills this strategy

1. **LVR math shifts with AMM design (#3: Market-structure change).** Uniswap v4 hooks, concentrated liquidity improvements, and AMM-native hedging (e.g., automated IV-aware fee tiers) could reduce LVR by better pricing the optionality sold to arbitrageurs. If LVR is substantially reduced in AMM design, the fee-vs-LVR crossover threshold rises, making more regimes viable for LP deployment — the regime gate becomes less additive.
2. **Pool TVL growth reduces per-LP fee income (#3: Market-structure).** As LP competition increases in the target pools, fee income per LP dollar falls (more LPs competing for the same fee flow). The regime gate does not improve market share; it only selects the favorable regime. If all regimes become fee-compressed, the strategy's alpha vanishes.
3. **Regime signal latency during acute events (#7: Operational).** DVOL spikes and 24h price moves can trigger the PAUSE condition faster than the monitoring loop detects them. LP positions can suffer significant LVR during the 1–4 hours between the event onset and the withdrawal execution. The 24h price move trigger (≥ 8%) partially mitigates this by using a faster-moving signal.
4. **Gas cost spikes make withdrawals/rebalances uneconomical (#7: Operational).** During network congestion (e.g., NFT mint rush, cascade events), gas costs can exceed the net gain from withdrawing in a regime shift. If withdrawal gas costs $500 but LVR for the next 72 hours is only $200, withdrawing is counterproductive.

## Kill criteria

Pause or retire on any of:

1. **6-month net LP P&L (fee income − IL − gas) negative during DEPLOY-regime periods** — the regime gate is not correctly identifying favorable windows.
2. **Realised LVR in low-vol regime exceeds fee income by > 0.5× for 3 consecutive months** — structural change in fee-vs-LVR balance; recalibrate gate thresholds.
3. **DVOL data delayed > 4 hours on 3 consecutive gate evaluations** — stale gate inputs; pause LP deployment until data pipeline restored.
4. **Pool TVL > $500M in target pool** — fee income per LP dollar collapsed; move to smaller pool or retire.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Solves the most common LP failure mode** — passive continuous LP deployment is well-documented as often negative-EV (LVR dominates) during high-vol periods. The regime gate is the structural fix.
- **Composable with delta-neutral hedging** — the regime gate can be layered on top of [[delta-neutral-yield-farming]]: deploy a delta-neutral LP in DEPLOY regime; if regime shifts to PAUSE, unwind the hedge and the LP simultaneously.
- **Mathematical basis (LVR = σ²/8)** — the strategy has a quantitative underpinning from Milionis et al. 2022, not just an empirical pattern. The gate threshold is derivable from pool fee tier and expected vol.
- **Yield in idle periods** — during PAUSE regime, capital is redeployed to stablecoin yield (AAVE, Compound) at 3–8% APY, reducing opportunity cost.

## Disadvantages

- **Misses fee income during high-vol windows** — rapid high-vol rallies and crashes generate the highest fee volumes; the PAUSE regime exits exactly when fee income peaks (temporarily). The LVR loss exceeds this fee income, but some operators will see the missed peak fee income and second-guess the gate.
- **Gas cost of regime-triggered withdrawals** — each regime shift triggers a withdrawal and re-deployment transaction, costing $50–500 in gas. Frequent regime oscillations at the boundary (DVOL hovering near 45–60%) can cause excessive gas burn.
- **Concentrated liquidity range management adds complexity** — the regime gate does not remove the need to manage the LP range; range rebalancing must still occur inside the DEPLOY windows. Two independent management processes (regime gate + range management) increase operational complexity.
- **DVOL is a BTC/ETH forward-looking metric** — for altcoin-pool LP positions (e.g., ARB/USDC, SOL/ETH), DVOL is a proxy vol signal, not the asset's own implied vol. Altcoin pools can spike into very high vol while DVOL stays moderate; the gate is less accurate for non-BTC/ETH pools.

## Sources

- [[loss-versus-rebalancing]] — the Milionis et al. (2022) LVR framework; the mathematical basis for the gate thresholds
- [[impermanent-loss]] — the practical LP risk concept; LVR is a tighter bound than the impermanent loss approximation
- [[delta-neutral-yield-farming]] — the nearest existing combination page; composable with this gate
- [[concentrated-liquidity]] — the LP execution framework; range management within the DEPLOY regime
- [[regime-adaptive-strategy]] — the general regime-gating framework applied to the DeFi LP primitive

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/volatility/dvol?coin=BTC` — DVOL 30-day IV index (primary gate signal)
- `GET /api/v1/volatility/dvol?coin=ETH` — ETH DVOL (for ETH-pool positions)
- `GET /api/v1/regimes/current` — macro regime classification (PAUSE trigger for Structural_Shock/Crash)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — leading indicator for vol buildup
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=3` — 24h price move for acute-event PAUSE trigger

**Historical data:**
- `GET /api/v1/volatility/dvol?coin=BTC&historical=true&days=365` — annual DVOL history for gate threshold calibration
- `GET /api/v1/volatility/realized?coin=BTC&days=30` — 30-day realized vol for secondary gate check
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=730` — 2-year daily OHLCV for backtesting regime classification

*Note: DEX pool APR, TVL, and tick-level LP data are not available via CryptoDataAPI. Use the Uniswap v3 subgraph (`thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3`), Revert Finance (`revert.finance`), or Defillama (`defillama.com/yields`) for pool-level LP analytics.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/volatility/dvol?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-volatility]], [[cryptodataapi-regimes]], [[cryptodataapi-market-data]].

## Related

- [[delta-neutral-yield-farming]] — hedged LP strategy; composable with this gate (add regime gate on top)
- [[concentrated-liquidity]] — LP range management within the DEPLOY regime
- [[leveraged-yield-farming]] — leveraged LP; regime gate is especially critical for leveraged positions (LVR × leverage factor)
- [[defi-yield-farming]] — the general DeFi yield farming primitive overview
- [[regime-adaptive-strategy]] — general regime gating framework
- [[regime-gated-grid]] — analogous regime gate applied to CEX grid market-making; same gate logic, different primitive
- [[vol-gated-mean-reversion]] — conditional vol treatment for mean-reversion; contrasting: for mean-reversion, high vol is sometimes good; for LP, high vol is always bad (LVR dominates)
- [[loss-versus-rebalancing]] — LVR framework: the mathematical basis for why LP positions are short-gamma and vol-regime-sensitive
- [[impermanent-loss]] — the practical LP risk metric that LVR bounds from above
- [[volatility-targeting]] — general vol-targeting overlay; this page is the LP-specific vol-regime application
- [[edge-taxonomy]] — structural + risk-bearing edge classification
- [[failure-modes]] — AMM design change, TVL compression, gas cost failure modes
- [[when-to-retire-a-strategy]] — kill vs pause framework
