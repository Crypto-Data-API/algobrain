---
title: "Funding Rate Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: excellent
tags: [arbitrage, crypto, funding-rate, perpetual-futures, market-neutral, defi, quantitative, derivatives]
aliases: ["Funding Arb", "Perp Funding Trade", "Cash and Carry (Perps)", "Cash-and-Carry Perp", "Crypto Carry"]
strategy_type: quantitative
timeframe: position
markets: [crypto]
complexity: intermediate
backtest_status: live

# Edge characterization
edge_source: [structural, behavioral, risk-bearing]
edge_mechanism: "Leveraged retail and trend-chasing longs persistently bid perpetual futures above spot; the arb provides the hedge they need and is paid funding to bear basis-blowup, exchange-failure, and oracle risks they refuse to bear."

# Data and infrastructure requirements
data_required: [funding-rates, spot-price, perp-price, funding-history-7d, open-interest, mark-price]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: high

# Performance expectations (net of fees and rebalancing slippage)
expected_sharpe: 1.4
expected_max_drawdown: 0.08
breakeven_cost_bps: 12

# Decay history
decay_evidence: "BTC/ETH 8h funding averaged ~0.04% (40%+ APY) in 2021; compressed to ~0.011% (~11% APY) by 2024 and ~0.005% (~5% APY) in 2025 as Ethena USDe ($14.8B peak TVL Oct 2025), Resolv RLP, Pendle yield-tokens and other delta-neutral protocols industrialised the trade. Funding briefly went negative on 2025-10-10."

# Lifecycle (deployed)
deploy_date: 2026-03-15
capital_allocation: "AsterDEX funding_arb sleeve, max 25% per asset, max 3 concurrent"
kill_criteria: |
  - rolling 7d funding average turns negative
  - drawdown > 8% on the sleeve
  - AsterDEX index/oracle vs CEX spot divergence > 100 bps for > 30 minutes
  - exchange insurance fund socialised loss event
last_review: 2026-04-27
next_review: 2026-05-27

related: ["[[cash-and-carry]]", "[[basis-trading]]", "[[cross-exchange-arbitrage]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[delta-neutral]]", "[[basis]]", "[[ethena-usde]]", "[[hyperliquid]]", "[[asterdex]]", "[[binance]]", "[[ftx]]", "[[kelly-criterion]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[book-a-man-for-all-markets]]", "[[cryptodataapi]]"]
---

# Funding Rate Arbitrage

Funding rate arbitrage is a delta-neutral strategy that captures the periodic funding payments exchanged between long and short holders of [[perpetual-futures]]. The arbitrageur shorts the perp when funding is persistently positive and hedges with an equal-notional spot long, earning the funding cash-flow without taking directional exposure to the underlying. It is the crypto-native expression of the classic [[cash-and-carry]] trade studied by Edward Thorp (Source: [[book-a-man-for-all-markets]]) and formalised in BIS Working Paper 1087, *Crypto carry* (Schmeling, Schrimpf and Todorov, 2023), which documents an average carry above 10% annualised — far larger than equities, FX, or commodities.

## Edge source

Mapping to the six categories in [[edge-taxonomy]], funding-rate arbitrage is a hybrid:

- **Structural** — perpetual contracts have a hard-coded funding mechanism that *must* transfer cash from longs to shorts when the perp trades above the index. As long as that contract design exists and someone is overweight long, a short collects funding. The flow is contractual, not opinion-based.
- **Behavioural** — the *reason* funding is positive is that retail and trend-chasing speculators systematically prefer leveraged long perp exposure to spot ownership. They are willing to pay 10-50% APY for convex, leveraged bull exposure they could replicate more cheaply with spot plus a margin loan. BIS 1087 explicitly traces crypto carry to "demand from smaller, trend-chasing investors seeking leveraged exposure".
- **Risk-bearing** — the arbitrageur is *paid* to absorb risks the long-only speculator does not want: exchange insolvency (see [[ftx]]), oracle/mark-price divergence, basis blowup, sudden funding inversion, and stablecoin depeg. This is a real risk premium, not a free lunch. Periods of zero or negative carry are the price of bearing those risks (see *What kills this strategy* below).

The trade does **not** rely on informational, analytical, or latency edge. Anyone with a Coinglass screen can see the funding rate. The edge is in *having the operational capability to be on the short side at scale and survive the tail*.

## Why this edge exists

Three persistent biases keep paying the arbitrageur:

1. **Leverage preference of the marginal long.** Retail crypto traders overwhelmingly prefer perpetual futures to spot because (a) perps offer 5x-100x leverage on a single click, (b) no need to custody underlying, (c) USDT-margined contracts unify the unit of account. They tolerate paying 30%+ APY in funding because they expect 100%+ price upside. As long as that asymmetric expectation holds in aggregate, longs bid the perp above spot.
2. **Limited deployment of arbitrage capital.** BIS 1087 explicitly identifies "limited deployment of arbitrage capital due to regulatory and margin frictions" as the second pillar of crypto carry. US institutions cannot easily access offshore perp venues. KYC, accreditation, custody, and tax treatment all narrow the eligible arb pool. The unmet hedging supply leaves a structural premium.
3. **Flow imbalance from leveraged crypto narratives.** During treasury-buying mania (BTC ETF approval, MSTR-clones, AI agent tokens), perp longs surge first because they are the cheapest convexity. Spot demand follows but lags. The wider the lag, the higher the funding.

Empirical evidence is consistent. He, Manela, Xu and Yan (2022, *Fundamentals of Perpetual Futures*, Wharton/WashU) find mean absolute deviations between perp and index of 60–90% per year — orders of magnitude larger than traditional currency basis. Sharpe ratios for the carry trade have been measured at 1.8 for retail-cost arbitrageurs and up to 3.5 for market-maker-tier execution.

## Null hypothesis

Under a no-edge world, perp-spot basis is a martingale: the funding rate is just noise around zero with mean equal to the risk-free interest rate (~0.01% per 8h, ~10.95% APY, the Binance baseline). In that world:

- The 7-day moving average of funding rate would oscillate near zero with no persistence.
- Funding above 0.03% per 8h would mean-revert within one or two periods, not persist for days or weeks.
- A short-perp/long-spot trade would earn zero net carry after fees and would not generate excess Sharpe.
- Cross-exchange funding spreads would close instantly via algorithmic arb desks.

The empirical record falsifies all four predictions. From 2017 through Q3 2025, BTC perp funding averaged materially above the interest-rate baseline; persisted for weeks at a time during bull regimes; and exhibited large, exploitable cross-venue spreads. The 2025-10-10 funding crash (when funding compressed to zero and briefly went negative as $5.7B redeemed from [[ethena-usde|USDe]] in a single month) is the clearest example of *what the null hypothesis world looks like* — and the speed at which it reverted shows how regime-dependent the edge is.

If your live funding-arb sleeve produces returns indistinguishable from the null distribution for more than 60 days, the regime has changed and the trade should be paused.

## Rules

### General entry conditions

1. **Funding signal.** 8-hour funding rate is positive AND > 0.03% (annualised ≥ 33%). Cross-check on at least one other major venue ([[binance]], [[hyperliquid]], Bybit, OKX) to filter out venue-specific oracle anomalies.
2. **Persistence filter.** 7-day rolling average funding rate is positive and trending up or flat. Filters out one-off spikes that mean-revert before you can collect.
3. **Spot leg available.** Underlying must be borrowable or directly purchasable on a venue with adequate liquidity for the intended notional. For ETF-linked assets (BTC, ETH), spot ETF or self-custody both qualify.
4. **Open interest health.** Perp open interest is rising or stable (confirms a real long-side flow, not just an illiquid quote artefact). See [[open-interest]].
5. **Counterparty/oracle health.** No active insurance-fund draw-down, no oracle-vs-CEX deviation > 50 bps, no funding-mechanism parameter change announced in the last 7 days.

### Exit conditions

1. **Funding falls below 0.01% per 8h** (annualised ~11%) — the trade has compressed below the interest-rate baseline; redeploy elsewhere.
2. **7-day funding average turns negative** — regime has flipped (typical of [[liquidation]] cascades or capitulation).
3. **Basis vs index widens > 100 bps for > 30 minutes** — execution risk on the short leg dominates expected carry; close before liquidation risk materialises.
4. **Spot-leg counterparty event** — exchange withdrawal halt, ACH suspension, custody risk flag.
5. **Drawdown on the sleeve > 8%** — kill criterion triggered (see below).

### Position sizing (general)

- 1x leverage on the perp short (fully collateralised in the same instrument's margin currency). Higher leverage massively reduces capital requirement but introduces liquidation risk on the short leg during sharp upward moves; the cost is asymmetric.
- Per-asset cap so a single oracle/exchange event cannot wipe the book.
- Cap concurrent positions to bound operational complexity (rebalancing, monitoring, withdrawal scheduling).
- Kelly-fractional sizing: realistic Kelly fraction for funding arb in current regime is ~0.05–0.10 of book per asset (see [[kelly-criterion]]); the reference bot stays well below this.

### AsterDEX implementation

This is the canonical, deployed instance of the strategy in this wiki: the deployed `funding_arb` strategy on [[asterdex|AsterDEX]] (perp DEX), currently ON.

| Parameter | Value | Rationale |
|---|---|---|
| **Venue (perp leg)** | [[asterdex|AsterDEX]] Pro Mode | 0.005% maker / 0.040% taker — among the lowest in the space; hidden orders protect the short fill from MEV. |
| **Hedge venue (spot leg)** | External (CEX or self-custody) | Avoids concentrating both legs on the same chain/exchange. |
| **Entry signal** | 8h funding > 0.03% AND positive | ~33%+ annualised; comfortably above breakeven cost. |
| **Exit signal** | 8h funding < 0.01% OR 7d avg < 0 | First condition closes when carry compresses; second is the regime-flip guard. |
| **Hold horizon** | Hours to weeks | Funding regimes persist weeks during bull markets, hours during stress. |
| **Leverage (perp leg)** | 1x isolated | Isolated margin contains a single-asset blowup to that asset's collateral. |
| **Per-asset cap** | 25% of sleeve allocation | Protects against a single Aster oracle / index incident. |
| **Concurrent positions** | Max 3 | Limits operational surface; matches available monitoring bandwidth. |
| **Signal cadence** | ~7 signals / 24h | Matches AsterDEX 8h funding intervals plus cross-asset opportunities. |

The choice of AsterDEX matters for the cost overlay: Pro Mode taker is 0.040% (vs Binance perp taker 0.0500%, Hyperliquid ~0.045%). Round-trip taker on the perp leg is therefore ~8 bps; combined with ~10 bps spot leg, the bot's all-in entry+exit cost is ~18 bps — well below the breakeven cost budget of 12 bps *per funding period* (which applies to a held trade collecting multiple fundings). Hidden orders are critical: a public 25%-of-sleeve short notional would otherwise leak directional bias and invite front-running. See [[asterdex]] for the venue's full fee schedule and hidden-order mechanics.

## Implementation pseudocode

```python
# funding_arb.py — canonical decision loop matching the deployed AsterDEX bot
from dataclasses import dataclass

ENTRY_8H_THRESHOLD = 0.0003     # 0.03% per 8h => ~33% APY
EXIT_8H_THRESHOLD  = 0.0001     # 0.01% per 8h => ~11% APY  (interest-rate baseline)
MAX_PER_ASSET      = 0.25       # 25% of sleeve allocation
MAX_CONCURRENT     = 3
ORACLE_DIVERGENCE_BPS = 100     # 1.00% Aster index vs CEX spot kill
DRAWDOWN_KILL = 0.08            # 8% sleeve drawdown kill

@dataclass
class Signal:
    asset: str
    funding_8h: float        # current 8h funding rate
    funding_7d_avg: float    # rolling 7-day mean
    aster_index: float
    cex_spot: float
    open_interest_zscore: float

def decide(signal: Signal, book: dict) -> dict:
    # ---- kill switches first (override everything) ----
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    divergence_bps = abs(signal.aster_index - signal.cex_spot) / signal.cex_spot * 1e4
    if divergence_bps > ORACLE_DIVERGENCE_BPS:
        return {"action": "FLATTEN", "asset": signal.asset, "reason": "oracle divergence"}

    pos = book["positions"].get(signal.asset)

    # ---- exit logic ----
    if pos is not None:
        if signal.funding_8h < EXIT_8H_THRESHOLD:
            return {"action": "EXIT", "asset": signal.asset, "reason": "funding compressed"}
        if signal.funding_7d_avg < 0:
            return {"action": "EXIT", "asset": signal.asset, "reason": "7d avg flipped negative"}
        return {"action": "HOLD", "asset": signal.asset}

    # ---- entry logic ----
    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent positions"}
    if signal.funding_8h <= ENTRY_8H_THRESHOLD:
        return {"action": "WAIT", "reason": "funding below entry threshold"}
    if signal.funding_7d_avg <= 0:
        return {"action": "WAIT", "reason": "7d avg not yet positive"}
    if signal.open_interest_zscore < -1.0:
        return {"action": "WAIT", "reason": "OI collapsing — likely capitulation"}

    notional = MAX_PER_ASSET * book["sleeve_capital"]
    return {
        "action": "OPEN",
        "asset": signal.asset,
        "perp_short_notional": notional,    # AsterDEX, 1x isolated, hidden order
        "spot_long_notional":  notional,    # external CEX or self-custody
        "reason": f"funding {signal.funding_8h*100:.4f}% per 8h",
    }
```

The real bot wraps this with: AsterDEX REST/WebSocket plumbing (see the [native API](https://github.com/asterdex/api-docs) referenced on [[asterdex]]); hourly rebalancing of the spot leg if delta drifts > 2%; an audit trail; and a manual kill switch.

## Indicators / data used

- **[[funding-rate]] (8h)** — primary signal. Annualise as `rate × 3 × 365`.
- **Funding rate history** — 7-day, 30-day, 90-day rolling means and signs.
- **[[basis]]** — perp mark price vs index/spot price; used as oracle-divergence guard.
- **[[open-interest]]** — confirms the size and direction of speculative flow on the long side.
- **Funding rate cross-venue spread** — funding can differ 5-20 bps between [[asterdex|AsterDEX]], [[hyperliquid]], [[binance]], and Bybit, allowing venue selection.
- **Mark price / index price** — for oracle-divergence kill switch.
- **Withdrawal/deposit liveness** — operational data, not a market signal but critical to surviving an [[ftx]]-style event.
- **Aggregator sources** — [[coinglass|Coinglass]], Velo Data, Amberdata, Laevitas for cross-venue funding tables.

## Example trade

**Setup (2026-04-19, AsterDEX):**

- ETH spot: $3,200 on Binance.
- AsterDEX ETHUSDT-PERP funding 8h: +0.045% (annualised ~49%). 7-day average: +0.029% (positive, trending up). OI z-score: +0.6.
- Sleeve capital: $40,000. Per-asset cap: 25% → $10,000 notional.

**Entry:**

1. Buy 3.125 ETH spot on Binance for $10,000 (taker fee ~$1.00 at 0.10%; can be reduced via maker quoting).
2. Submit a hidden short on AsterDEX ETHUSDT-PERP for 3.125 ETH at $3,210 with $10,000 USDT isolated margin (1x). Pro Mode maker fee: 0.005% = $0.50. (If filled as taker: 0.040% = $4.00.)
3. Verify delta neutrality: spot long 3.125 ETH, perp short 3.125 ETH. Net delta ≈ 0.

**Hold (10 days, 30 funding periods):**

- Funding averages 0.038% per 8h over the period.
- Funding income per period: 0.038% × $10,000 = $3.80. × 30 periods = **$114.00**.
- ETH rallies from $3,200 to $3,420 (+6.9%). Spot leg gains $687.50. Perp short loses ~$687.50 (basis converges modestly: actual net P&L from price = -$2 to +$5 depending on funding-period mark snapshots).
- Cumulative pre-cost gain: ~$114 funding + ~$0 directional ≈ $114.

**Exit (day 11):**

- Funding falls to 0.008% per 8h, below the 0.01% exit threshold.
- Close perp short on AsterDEX (taker $4.00) and sell spot ETH on Binance (taker $10.27 at 0.10% on $10,272 sale).
- Total fees: ~$1.00 + $0.50 + $4.00 + $10.27 = ~$15.77 round trip.

**Net P&L: ~$98 on $10,000 deployed in 11 days = ~3.27% APY-equivalent on this trade alone** (0.98% over 11 days). Across ~7 such signals/day with portfolio-level overlap, the deployed sleeve targets **15-25% APY net of costs** in current regimes — down from the 30-50% achievable in the 2021 bull market before [[ethena-usde]] and Resolv compressed the trade.

## Performance characteristics

The realistic, cost-corrected performance picture (2024-2026 regime):

| Metric | Value | Note |
|---|---|---|
| Net APY on capital | 8-25% | Was 30-50% in 2021. Heavily regime-dependent. |
| Sharpe (target) | 1.4 | Higher in steady regimes; collapses to <0 during funding inversions. |
| Max drawdown (sleeve) | 5-8% | Driven by funding-flip episodes plus basis blowup, not directional moves. |
| Win rate (per 8h period) | 80-95% | Most periods are profitable; tail events dominate the loss distribution. |
| Profit factor | 2.0-4.0 in bull regimes; ~1.0 in chop; <1.0 in bear regimes |  |
| Breakeven cost budget | ~12 bps per held funding period | Includes spread, taker fees, gas, and rebalance slippage. |
| Capital efficiency | ~50% (1x perp + spot = 2x capital outlay) | Higher leverage trades efficiency for liquidation risk. |

**Cost overlay (AsterDEX-specific):**
- Perp round-trip on Pro Mode maker/taker mix: ~5-8 bps.
- Spot round-trip on Binance with maker quoting: ~4-8 bps.
- Funding-period rebalance: ~1-2 bps per day if delta drift > 2%.
- Withdrawal/network: variable (BTC/ETH gas at ~$1-5 per leg today).
- Slippage on $10k notional: typically <2 bps on BTC/ETH; 5-15 bps on smaller perps.

The He, Manela, Xu, Yan empirical paper (*Fundamentals of Perpetual Futures*) reports Sharpe of 1.8 at retail cost levels and 3.5 at MM cost levels, consistent with the 1.4 expected Sharpe used here as a conservative live target after slippage and operational drag.

## Capacity limits

The trade is high-capacity but not infinite. Empirically:

- **Per-asset on a single perp DEX**: ~$50-200M notional before short-side bid-stacking moves the funding rate against the arb itself.
- **Across major perp venues simultaneously**: ~$1-5B for top assets (BTC, ETH).
- **Aggregate global capacity**: bounded by the *long-side* willingness to pay funding. [[ethena-usde|Ethena's]] $14.8B peak TVL in October 2025 represents a real-world benchmark — at that scale, USDe's hedge inventory was so large that it materially compressed funding rates across BTC and ETH on every major venue.

For the AsterDEX `funding_arb` sleeve specifically, the capacity ceiling is set by:
1. AsterDEX OI depth on the asset (varies by token; tens of millions on majors).
2. Hidden-order fill quality at size — Pro Mode mitigates this but does not eliminate it for $10M+ tickets.
3. Withdrawal velocity from external spot venues (Binance/Bybit limit daily withdrawal).
4. Counterparty concentration risk — a single-venue blowup at $X position size implies $X tail loss.

A reasonable working capacity for an individual operator: **$100k-$5M** before the trade becomes self-defeating on AsterDEX's smaller perps, **$10-50M** on majors. Above that, you are Ethena.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Crowding (Failure Mode #4: The Edge Got Crowded Out).** This is the dominant secular risk. From 2021 to 2024, BTC/ETH funding averages compressed roughly 75% as Ethena, Resolv, Pendle's PT-USDe yield-tokens, and the `Sky/USDS` ecosystem industrialised the trade. *(Source: [[ethena-usde]]; CoinMetrics State of the Network Issue 335; AMBCrypto coverage of the 2025-10-10 unwind.)* The trade is not dead, but the average reward has compressed.
2. **Regime change (Failure Mode #5: The Regime Changed).** Funding goes negative in bear markets and capitulation events. 2025-10-10 is the canonical recent example: BTC/ETH funding compressed to zero or briefly negative within hours; $5.7B redeemed from USDe in October alone; sUSDe yield collapsed. A bot with no 7d-avg-flip exit will bleed for weeks.
3. **Counterparty failure (Failure Mode #7: Operational Collapse).** [[ftx]] is the textbook case. Capital sitting on a centralised perp venue is at risk of insolvency, withdrawal halt, or rehypothecation. AsterDEX is decentralised but introduces *bridge/router risk* across its four chains and *team-controlled risk parameters* (the team can adjust leverage/funding/margin in real time — see [[asterdex#Risks]]).
4. **Basis blowup / oracle divergence (Failure Mode #6: Tail Realised).** During a flash crash or oracle malfunction, the perp can mark wildly off the index for minutes. If the short leg gets liquidated while the spot leg cannot be sold instantly, the supposedly delta-neutral position takes a one-sided loss. The Aster XPL index misconfiguration incident is the in-venue precedent (AsterDEX reimbursed users that time — but reimbursement is a discretionary, not contractual, guarantee).
5. **Liquidation risk on the short leg.** Even at 1x isolated leverage, a violent +50%+ rip in spot with execution latency on the rebalance can chew into the margin buffer. If the bot cannot top up margin or close in time, the short can liquidate, breaking the hedge at the worst possible moment.
6. **Stablecoin depeg.** USDT or USDC depeg events make USDT-margined positions a hidden directional bet. Less acute since 2023, but never zero.
7. **Regulation.** US perp DEX access is legally ambiguous and has been further constrained in waves. A jurisdictional change in the bot operator's home country can force a forced unwind.

### Basis blowup risk during AsterDEX-specific events

AsterDEX deserves separate mention because its risk profile is meaningfully different from CEX perps:

- **Index oracle.** AsterDEX's mark price is computed from a basket of CEX oracles. If one component pulls the index away from the underlying CEX spot mid-event, the perp can liquidate the short while spot is unchanged. Kill switch: any > 100 bps Aster-index vs CEX-spot divergence held > 30 minutes.
- **Multi-chain bridge risk.** AsterDEX deploys on BNB Chain, Ethereum, Solana, and Arbitrum. Bridge/router compromise on any one chain can isolate collateral.
- **Team parameter changes.** The team retains the ability to adjust leverage, funding mechanics, and margin in real time. A funding-formula tweak can overnight invalidate the bot's edge calculation.
- **ASTER token incentive flow.** Funding may be partly subsidised by ASTER emissions. If emissions roll off or the points program ends, observed funding can drop without an underlying market change.
- **Volume-mining/wash-flow distortion.** Some perp DEXes have at times had volume-mining programs that distort observed funding. AsterDEX's history here should be checked before sizing up.

The general principle: **any time the perp leg lives on a venue whose pricing is not produced by the same matching engine as the spot leg, you are running a basis trade across two pricing systems and you can lose to a divergence event.**

## The 2021-2024 funding rate compression

The most important alpha-decay story in modern crypto. Three structural changes ate most of the trade:

1. **Ethena USDe (2024-2025).** [[ethena-usde|Ethena]] launched in early 2024 with the explicit thesis of tokenising the funding-arb trade. By mid-2025, [[ethena-usde|USDe]] supply exceeded $14.8B at peak, making Ethena the largest single short-perp/long-spot operator in crypto. sUSDe yield averaged ~19% APY through 2024, then compressed to ~5% in 2025 as Ethena's own scale crowded out the very edge it was harvesting. *(Source: CoinMetrics SOTN 335; Stablecoin Insider review.)*
2. **Resolv RLP (2024-2025).** [[resolv-rlp|Resolv]] deployed a similar synthetic-dollar architecture with a separate insurance tranche (RLP) absorbing basis risk in exchange for higher yield. Tens to low-hundreds of millions in TVL.
3. **Pendle yield-token markets.** [[pendle|Pendle]] tokenises future Ethena/Resolv yield, attracting structured-product capital that ultimately backstops the same funding-arb supply. This deepened liquidity but *also* pulled forward the rate at which yield compresses.

Quantitative snapshot:

| Period | BTC 8h funding (avg) | ETH 8h funding (avg) | Implied APY | Note |
|---|---|---|---|---|
| 2021 bull | ~0.04% | ~0.05% | ~44-55% | Pre-Ethena. Naive arb dominated. |
| 2022 bear | -0.005% | -0.01% | negative | FTX collapse, capitulation. |
| 2023 chop | ~0.012% | ~0.013% | ~13-14% | Recovery. |
| 2024 | ~0.011% | ~0.014% | ~12-15% | Ethena scaling. |
| 2025 | ~0.005% | ~0.006% | ~5-7% | Ethena at $14.8B TVL peak; rate compression. |
| 2025-10-10 | ~0% | briefly negative | 0% | USDe redemption cascade; carry zero. |

*(Funding rate aggregates above are illustrative averages reconstructed from BIS 1087, the He et al. 2022 paper, public exchange data, and Ethena disclosures. Exact figures vary by venue and snapshot.)*

The strategy is **not retired** — funding is still positive on average and structurally bid in bull regimes — but the expected reward has compressed. Operators who do not adjust their thresholds (e.g., still using 0.05% entry from 2021) will see signal frequency collapse and live performance lag the backtest.

## Kill criteria

The deployed sleeve is killed (paused, not retired) on any of:

1. **Sleeve drawdown > 8%** in any rolling 30-day window.
2. **7-day funding average < 0** on more than half of currently held positions.
3. **AsterDEX index vs CEX spot divergence > 100 bps** sustained for > 30 minutes (oracle/health flag).
4. **AsterDEX insurance-fund socialised loss event** (any size).
5. **Withdrawal halt or unscheduled maintenance** > 4 hours on any leg's venue.
6. **Aggregate global funding (Ethena + Resolv + Pendle PT-USDe yield) below interest-rate baseline for 60+ days** — regime confirmation that the trade has been arb'd out.

Re-deploy criteria (un-kill): all of the above clear, plus 14-day funding average back above 0.015% per 8h on at least three eligible assets.

See [[when-to-retire-a-strategy]] for the broader framework. Funding-arb is a *pause-able* strategy: the underlying mechanism (perp funding) does not go away, only the rate level does, so killing-but-not-retiring is appropriate.

## Advantages

- **Truly delta-neutral when properly hedged.** No directional view required — the only views are on funding persistence and counterparty solvency. This mirrors the Thorp doctrine (Source: [[book-a-man-for-all-markets]]): edge plus disciplined hedging plus Kelly sizing.
- **Predictable cash-flow.** Funding is paid every 8h (every 1h on [[hyperliquid]] and dYdX). Income visibility far exceeds most directional crypto strategies.
- **High historical and current Sharpe.** 1.8 retail / 3.5 MM Sharpe documented in academic work; 1.4 conservative live target in current regime.
- **Scalable up to $10s-$100s of millions** for major assets without crippling the trade.
- **Transparent.** Every input (funding, mark, index, OI) is publicly observable in real time; no information asymmetry to exploit you on.
- **AsterDEX-specific advantage**: hidden orders prevent execution leakage that would otherwise tip retail traders to the arb's positioning.

## Disadvantages

- **Capital-intensive.** Spot + perp margin = ~2x capital deployment per dollar of funding income. Higher perp leverage reduces this but introduces liquidation risk (see *What kills*).
- **Counterparty risk on every venue.** [[ftx]], Celsius, BlockFi, FCoin, Mt Gox — the list of perp/spot venues that have lost user funds is long. AsterDEX is decentralised but not risk-free.
- **Funding can flip negative quickly.** The 2025-10-10 episode flipped BTC/ETH funding to zero in hours.
- **Basis-blowup tail.** Rare but vicious; the entire year's carry can be wiped in a single oracle-divergence event.
- **Regulatory/jurisdictional risk.** US accessibility to perp DEXes is constrained and shifting.
- **Edge decay.** Documented and ongoing — Ethena, Resolv, Pendle, and the next generation of structured products are still absorbing the trade.
- **Operational complexity.** Two-venue execution, delta drift rebalancing, withdrawal management, and oracle monitoring are all required. A bug in any layer is a live-fire risk.
- **Tax complexity.** In many jurisdictions, funding payments, perp P&L, and spot P&L are classified differently; the headline net APY can be materially lower after tax.

## Sources

**Foundational / theoretical:**
- (Source: [[book-a-man-for-all-markets]]) — Thorp (2017): the foundational treatment of delta-neutral arbitrage, [[kelly-criterion|Kelly]] sizing, and convertible/warrant carry that funding-arb is the crypto-native analogue of. Thorp's Princeton Newport partnership delivered 19.8% annualised over 19 years with only 3 losing months using exactly this *hedge-then-collect-spread* template.

**Empirical / academic:**
- BIS Working Papers No 1087, *Crypto carry* — Maik Schmeling, Andreas Schrimpf, Karamfil Todorov (BIS, April 2023). Documents that crypto carry averages above 10% annually, sometimes exceeding 40%, far larger than carry in equities, FX, fixed income, or commodities. Traces the premium to (i) leveraged demand from trend-chasing retail and (ii) limited deployment of arbitrage capital. Available at https://www.bis.org/publ/work1087.pdf.
- He, Manela, Xu and Yan, *Fundamentals of Perpetual Futures* (2022, updated 2024), Wharton/WashU. Reports mean absolute perp-vs-index deviations of 60-90% per year and Sharpe of 1.8 for retail-cost arbitrageurs / 3.5 for market makers. arxiv.org/abs/2212.06888.
- Ackerer, Hugonnier, Jermann, *Perpetual Futures Pricing*, Wharton working paper / Mathematical Finance (2024). Theoretical pricing model for perp basis under funding mechanism; published version: doi.org/10.1111/mafi.70018.
- "Exploring Risk and Return Profiles of Funding Rate Arbitrage on CEX and DEX", *Finance Research* (2025). Empirical CEX-vs-DEX comparison; reports the trade can return up to 115.9% over six months with max drawdown ~1.92% in favourable regimes — but only 40% of "obvious" arbitrage spreads remain profitable after costs. sciencedirect.com/science/article/pii/S2096720925000818.
- "The Two-Tiered Structure of Cryptocurrency Funding Rate Markets", *Mathematics* MDPI (2025). Shows CEXes lead price discovery (61% higher integration) with one-way information flow CEX→DEX. mdpi.com/2227-7390/14/2/346.

**Industry / mechanics:**
- Binance funding-rate documentation: 8-hour funding interval; 0.01% interest-rate baseline; clamped premium component. (Public docs.)
- Hyperliquid funding-rate documentation: 1-hour funding interval; predictive-mid premium calculation. (Public docs; see also [[hyperliquid]].)
- AsterDEX docs and API repository — fee structure (Pro Mode 0.005% maker / 0.040% taker), hidden-order mechanics, isolated-margin behaviour. https://github.com/asterdex/api-docs (see [[asterdex]]).
- [[ethena-usde|Ethena USDe]] official documentation: synthetic-dollar architecture; delta-neutral hedge composition (BTC/ETH/SOL spot longs + equivalent short perps). docs.ethena.fi/solution-overview/usde-overview.
- CoinMetrics, *State of the Network* Issue 335, "Ethena and the Mechanics of USDe" — Tanay Ved (2024). Walk-through of how Ethena industrialises the funding-arb trade.
- Amberdata, *The Ultimate Guide to Funding Rate Arbitrage* (2024). Practitioner-level treatment of execution mechanics. blog.amberdata.io.

**Regime/event evidence:**
- AMBCrypto and DLNews coverage of the 2025-10-10 funding crash: USDe outflows of $5.7B in October 2025; TVL fell from $14.8B to $7.6B; sUSDe yield collapsed; ENA token down 62%. Concrete record of what funding-arb decay looks like during a regime flip.
- [[ftx|FTX]] collapse (November 2022) — canonical counterparty-risk event; funding-arb operators with capital on FTX lost the spot or perp leg outright.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

- [[funding-rate]] — the underlying instrument-level mechanism.
- [[perpetual-futures]] — the contract that makes the trade possible.
- [[basis]] / [[basis-trading]] / [[cash-and-carry]] — the broader basis-trade family.
- [[delta-neutral]] — the hedging principle.
- [[edge-taxonomy]] — where this strategy sits among the six edge categories.
- [[failure-modes]] — the catalog this strategy's kill criteria draw from.
- [[when-to-retire-a-strategy]] — framework for deciding pause vs retire.
- [[kelly-criterion]] — sizing rule.
- [[ethena-usde]] — the largest industrialised version of this trade; primary alpha-decay agent.
- [[resolv-rlp]] — second-generation synthetic-dollar arb.
- [[pendle]] — yield-token market that recursively prices funding-arb future yields.
- [[hyperliquid]] — alternative perp-DEX venue with hourly funding.
- [[asterdex]] — the deployed venue for this wiki's `funding_arb` bot.
- [[binance]] — primary spot-leg counterparty and benchmark for funding rates.
- [[bybit]] — alternative perp venue.
- [[cross-exchange-arbitrage]] — adjacent crypto market-neutral strategy.
- [[hyperliquid-hlp-basis-arbitrage]] — variant on Hyperliquid HLP.
- [[stablecoin-yield]] — broader DeFi yield context for the trade's compressed APY.
- [[ftx]] — the cautionary tale on counterparty risk.
- [[liquidation]] — what happens to the short leg if the hedge breaks.
- [[book-a-man-for-all-markets]] — the foundational source for delta-neutral arb thinking.
