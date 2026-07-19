---
title: "Pendle PT/YT Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-07-19
status: excellent
tags: [arbitrage, defi, quantitative, derivatives, ethereum]
aliases: ["Pendle Principal Token Arb", "Yield Token Arbitrage", "Pendle Fixed-Yield Arb"]
related: ["[[pendle]]", "[[lst-depeg-arbitrage]]", "[[restaking-token-arbitrage]]", "[[funding-rate-arbitrage]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [analytical, structural]
edge_mechanism: "Pendle Finance splits yield-bearing assets (stETH, sUSDe, eETH) into Principal Tokens (PT) — entitled to underlying at maturity — and Yield Tokens (YT) — entitled to all yield until maturity. PT trades at discount to underlying; the discount equals expected yield. When market priced PT-implied-yield diverges from oracle/strategy expected yield, arb opens."
data_required: [pendle-pool-reserves, underlying-yield-rates, pt-yt-prices-by-maturity, points-multipliers]
min_capital_usd: 100000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 1.8
expected_max_drawdown: 0.1
breakeven_cost_bps: 30
decay_evidence: "Pendle TVL grew from $200M (2023) to $5B+ (2024) on restaking-LRT category. Strategy alive across markets but yields compressing as more institutional capital enters."
---

# Pendle PT/YT Arbitrage

Trading the **Principal Token (PT)** and **Yield Token (YT)** decomposition of yield-bearing assets on **[[pendle|Pendle Finance]]**. Pendle splits any yield-bearing token into two synthetic components: PT (zero-coupon claim on principal at maturity) and YT (claim on all yield from now until maturity). The two pieces re-combine to the original — but trade independently. [[arbitrage|Arbitrage]] opportunities arise when the implied-yield-from-PT diverges from realized or expected yield, when YT is mispriced relative to remaining yield runway, or when points/airdrop expectations distort YT.

This is, in effect, **fixed-income relative value applied to on-chain yield**: PT is a discount bond (zero-coupon), YT is the coupon strip, and the arb is the same implied-vs-realised-yield trade a rates desk runs — but on a protocol whose liquidity, oracle dependence, and points-driven flow make it far less efficient than a sovereign bond market. The strategy was niche pre-2023 but became one of the largest single arbitrage categories of 2024-2025 as Pendle integrated **restaking LRTs** ([[restaking-token-arbitrage|eETH, ezETH, rsETH]]), reaching **$5B+ TVL** by Q2 2024.

> **Concentration & smart-contract risk warning.** The entire strategy is exposed to a single protocol. Any Pendle core-contract exploit is **binary and terminal** regardless of position-level hedging — it is the dominant tail risk and is encoded directly in the kill criteria. The strategy also depends on continued Pendle growth and on accurately modelling points/airdrop value, which is inherently speculative.

## Edge Source

**Analytical** + **structural**.

- **Analytical:** Modeling expected yield over PT maturity (7 days to 12 months) requires understanding both base yield AND points/airdrop optionality.
- **Structural:** Most institutional capital deploys to PT (fixed yield) or YT (yield speculation) one-sided — relative-value spread is the arbitrage.

## Why This Edge Exists

Pendle's yield decomposition mathematics:
```
1 yield-bearing token = 1 PT + 1 YT
PT pays: 1 unit of underlying at maturity
YT pays: all yield until maturity
```

If underlying yields 5% APR and maturity is 1 year:
- PT trades at ~$0.952 (= $1 / (1 + 5%))
- YT trades at ~$0.048 (= present value of yield stream)

When markets misprice:
- PT trading at $0.92 implies 8.7% yield — if your expected yield is 5%, arbitrage by buying PT and locking in the 8.7% fixed return.
- YT trading at $0.06 implies higher yield — if your expected yield is 5%, sell YT.

In **2024 LRT mania**, YT prices were wildly inflated by points-farming optionality:
- eETH PT implied 30%+ yield on what was structurally a 4% Ethereum staking yield.
- Reason: YT holders received Ether.fi points + EigenLayer points + other rewards.
- Specialist arbs analyzed points-value vs YT premium.

Counterparty: yield-curious DeFi participants buying PT for "fixed yield" without modeling correctly; points farmers buying YT for airdrop exposure without comparing to direct LRT-holding.

### Risk decomposition of a PT/YT position

| Component | What you are exposed to | How it is usually managed |
|-----------|-------------------------|---------------------------|
| Long PT | Underlying yield realising below implied; underlying depeg | Hold to maturity; pick assets with stable yield |
| Short YT | Yield/points overshooting your model | Hedge with long spot underlying |
| Underlying asset | LST/LRT depeg (e.g. ezETH Apr 2024) | Diversify across protocols; size for depeg |
| Points / airdrop optionality | Mis-modelled points value; token launch reprices YT | The hardest leg to model; size conservatively |
| Pendle protocol | Smart-contract exploit | **Unhedgeable** — binary kill-criterion risk |
| Liquidity / maturity roll | Thin pool depth at roll; slippage | Cap size at pool TVL; stagger maturities |

The clean, model-able legs are the PT discount and the YT decay; the speculative leg is points value; the uninsurable leg is protocol risk.

## Null Hypothesis

Under efficient pricing, PT implied yield equals the market's unbiased expectation of underlying yield over each maturity window: `PT = 1 / (1 + E[y])^t`, `YT = 1 - PT` (plus correctly-priced points value), and no systematic spread exists between implied yield at entry and subsequently realized yield. The testable form: regress realized yield over each completed maturity against PT-implied yield at entry — under the null the slope is 1, the intercept 0, and a "buy PT when implied > model" rule earns exactly the underlying yield, nothing more. Empirically 2023-2025 rejects this: implied yields persistently **overshot** realized yield during points manias (eETH YT pricing 60-90% implied APR against ~4% realized base staking yield in Q1 2024) and modestly **undershot** on unfashionable long-dated PTs (stETH 12-month implying 5-7% vs ~4% realized). The systematic, sign-predictable residual — driven by one-sided points-farming flow — is the edge; if the regression residuals collapse toward zero, the market has matured and the strategy is done.

## Variants

| Variant | Description | Holding Period |
|---------|-------------|----------------|
| **Long PT (lock fixed yield)** | Buy PT at implied yield > model yield; hold to maturity | Days-months |
| **Short YT (sell yield speculation)** | Sell YT when implied yield > expected | Days-months |
| **PT/YT pair trade** | Long underpriced + short overpriced of the same maturity | Days-weeks |
| **Calendar PT spread** | PT 3-month vs PT 12-month — bet on yield curve | Months |
| **Cross-asset PT spread** | PT(stETH) vs PT(eETH) — same Ethereum yield, different protocol risk | Weeks-months |
| **Points-stripped YT analysis** | Decompose YT price into yield + points; trade based on points-value model | Weeks |
| **PT/YT vs underlying triangle** | When PT + YT ≠ 1.0 underlying (rare; arb closes within blocks) | Atomic |

## Rules

1. **Universe screening:** identify Pendle pools with significant TVL ($10M+).
2. **Yield modeling:** for each maturity, compute expected yield from underlying + projected points.
3. **PT/YT mispricing detection:** compute implied yield from PT price; compare to model.
4. **Position sizing:** typically 1-3% of fund per trade; lower for points-driven YT.
5. **Hold to maturity** for PT trades; or close if implied yield converges to model.
6. **Roll positions** at maturity; new PT/YT for next period.

## Implementation Pseudocode

```python
on tick:
    for pool in pendle_pools:
        underlying_apy = oracle.get_yield(pool.underlying)
        points_value = model.points_per_yt(pool)
        implied_yield_from_pt = (1 / pt_price - 1) * 365 / days_to_maturity
        implied_yield_from_yt = (yt_price + points_value) * 365 / days_to_maturity
        
        if implied_yield_from_pt > underlying_apy + 200bp:
            # PT cheap (high implied yield) — buy and lock
            buy(pool.pt, kelly_size(implied_yield_from_pt - underlying_apy))
        if implied_yield_from_yt > underlying_apy + 200bp:
            # YT rich — sell short
            short(pool.yt, kelly_size(implied_yield_from_yt - underlying_apy))
```

## Indicators / Data Used

- Pendle protocol API (PT/YT prices by maturity).
- Pendle SDK and AMM math libraries.
- Underlying yield oracle (Lido, Coinbase, Ether.fi, EigenLayer for LSTs/LRTs).
- Points-multiplier announcements.
- Maturity calendar (rolling Pendle pools every 3-12 months).

## Example Trades

**eETH PT/YT, Q1 2024.** Ether.fi launched eETH with point-farming hype. YT(eETH) priced implied 60-90% APR vs underlying ~4% Ethereum staking yield. Specialist arbs:
- Sold YT(eETH) maturity June 2024.
- Hedged via long eETH spot.
- Captured 50%+ on the YT decay over 3 months.
- Some funds reportedly extracted $50-150M from this trade alone.

**ezETH PT (April 2024 depeg).** When ezETH depegged from 1 ETH to 0.94 ETH on April 24, 2024 (Renzo airdrop disappointment), PT(ezETH) implied yield spiked to 25%+. Arbs bought PT at deep discount; convergence captured 6%+ in 3 weeks.

**sUSDe PT (Ethena's USDe).** Ethena's synthetic dollar yields 15-30% APR (funding rate harvest). PT(sUSDe) typically implied 10-15% fixed yield. Long PT for fixed-yield carry; conservative 8-12% APR on collateral.

**stETH PT 12-month maturities.** Long-dated PT(stETH) often implied 5-7% (vs 4% underlying yield) due to long-tail risk premia. Patient hold-to-maturity arb captured 1-3% spread.

**Eigenpie, Kelp KEP/RSETH.** Multiple LRT protocols with Pendle integrations. Pair trades across LRT-PTs (e.g., long eETH PT, short rsETH PT) captured relative-value differences.

## Performance Characteristics

Top dedicated Pendle desks reported 25-60% annualized returns 2024 (concentrated in the LRT-points era). These are **operator-reported figures, not an audited backtest**, and are heavily weighted to a one-off points mania that has largely passed. Sharpe 1.8-2.5. Returns compressing as the strategy matures and more capital deploys.

### Cost / friction overlay

| Cost / friction | Magnitude | Notes |
|-----------------|-----------|-------|
| Pendle AMM swap fees + slippage | Per entry/exit/roll | Charged on each PT/YT leg; worse on thin pools |
| Gas (Ethereum + L2s) | Per transaction | Entry, hedge, roll, exit each cost gas |
| Maturity-roll slippage | At every roll (3-12 months) | New PT/YT must be re-established |
| Hedge funding (if shorting YT vs long spot) | Borrow / funding | Carry cost on the spot hedge leg |
| Points-model error | Variable, can be large | The dominant *return* risk — mis-priced airdrop value |
| Breakeven cost | ~30 bp round-trip (frontmatter) | Below this the implied-vs-realised spread is consumed |

The honest read: the spectacular 2024 numbers were a points-farming regime, not a steady-state carry; as native tokens launched and points dried up, the residual edge is the modest, persistent PT-discount / yield-curve relative value — closer to a fixed-income RV book than to the 2024 LRT bonanza.

## Capacity Limits

Per-pool capacity bound by Pendle pool depth ($5-200M TVL typical). Strategy-level capacity ~$500M for top dedicated operators.

## What Kills This Strategy

- Points-farming era ends — most LRT protocols launched native tokens by Q2 2024, collapsing the YT premium that drove the biggest trades.
- Pendle protocol risk — a smart-contract exploit would be terminal and is unhedgeable (the binary tail risk; see warning in lead).
- LRT consolidation reduces the opportunity surface (fewer distinct PT/YT markets to run relative value across).
- Institutional yield-curve arbitrage capacity floods in, compressing the implied-vs-realised spread toward zero (classic [[limits-to-arbitrage]] dynamics in reverse — capital arrives and the edge decays).
- Underlying depeg cascade — a correlated LST/LRT depeg event hits multiple PT positions at once.

## Kill Criteria

- Average implied-yield mispricing across the screened pool universe < 100 bp for 60 consecutive days.
- Pendle TVL < $1B for 90 consecutive days (vs $5B+ peak).
- Any Pendle core-contract exploit, regardless of size — protocol concentration risk is binary.

## Advantages

- Highly profitable in 2024 LRT era.
- Decoupled from broad crypto beta.
- Decomposition allows fine-grained risk targeting.

## Disadvantages

- Smart contract concentration risk on Pendle.
- Strategy depends on Pendle continued growth.
- Yield modeling complexity.

## Sources

- Pendle Finance documentation and AMM math whitepaper.
- Pendle SDK (open source).
- Ether.fi, Renzo, Kelp protocol documentation.
- DefiLlama Pendle category tracking.
- **YouTube: "Pendle Explained" series by DeFi Dad (2024).**
- **YouTube: "Bankless" Pendle interview with TN Lee (founder, 2024).**
- **YouTube: "Wave Financial" / "Galaxy Digital" Pendle market commentary 2024.**

## Getting the Data (CryptoDataAPI)

PT/YT prices and pool state come from the Pendle API/SDK; [[cryptodataapi|CryptoDataAPI]] supplies the yield-model inputs for funding-derived underlyings (sUSDe — Ethena's yield *is* the funding harvest) and the depeg/tail overlay on LST/LRT underlyings.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — cross-exchange funding (the driver of USDe/sUSDe yield; feeds the expected-yield model for sUSDe PT/YT pools)
- `GET /api/v1/market-intelligence/funding-rates` — cross-exchange funding for top coins in one call
- `GET /api/v1/security/regime/score` — depeg/hack stress composite (the ezETH-Apr-2024-style tail on the underlying leg)
- `GET /api/v1/event/calendar` — forward catalysts incl. depeg-risk events on screened underlyings

**Historical data:**
- `GET /api/v1/backtesting/funding` — Hyperliquid hourly funding since 2023-05 (realized funding-yield series over past PT maturity windows)
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time market state for maturity-window studies (since 2026-03-02)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the yield-model half of this strategy (PT/YT quotes still come from Pendle):

- **Yield model (sUSDe pools)** — average `GET /api/v1/derivatives/funding-rates` across venues to project USDe's funding-harvest yield over the PT maturity, then compare to the Pendle-implied yield; a 200bp+ gap is the entry per the Rules.
- **Tail watch** — `GET /api/v1/security/regime/score` and `GET /api/v1/event/calendar` flag depeg/exploit stress on the underlying LST/LRT before it hits a held PT position.
- **Regime gate** — `GET /api/v1/quant/market`: sustained `strong_trend_bear` compresses funding toward negative, undermining sUSDe realized yield vs the fixed rate locked at PT entry — favour the long-PT (fixed-receiver) side in that state.
- **Backtest** — run the null-hypothesis regression (realized vs implied yield) using `GET /api/v1/backtesting/funding` (HL hourly since 2023-05) as the realized funding-yield series over each completed maturity; pair with `/api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid grading old entries with today's knowledge.
- **Tips** — points/airdrop optionality (the dominant model risk) has no API anywhere; keep it as an explicit uncertainty band rather than a point estimate, and size YT shorts to survive the band's top end.

## Related

[[arbitrage]] · [[pendle]] · [[limits-to-arbitrage]] · [[lst-depeg-arbitrage]] · [[restaking-token-arbitrage]] · [[funding-rate-arbitrage]] · [[2022-06-steth-depeg]] · [[airdrop-farming]]
