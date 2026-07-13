---
title: "Volatility Carry"
type: strategy
created: 2026-05-06
updated: 2026-06-20
status: excellent
tags: [quantitative, options, volatility, derivatives, sp500]
aliases: ["Vol Carry", "VRP Harvesting", "Short Vol Carry", "Volatility Risk Premium Strategy"]
strategy_type: quantitative
timeframe: position
markets: [stocks, options]
complexity: advanced
edge_source: [behavioral, structural]
edge_mechanism: "Hedgers and asset owners systematically pay a premium for downside insurance and convexity; carry sellers underwrite that insurance, collecting the spread between implied and realized volatility (the variance risk premium)."
data_required: [options-chain, vix-history, realized-vol-calc, futures-curve]
min_capital_usd: 25000
capacity_usd: 5000000000
crowding_risk: high
expected_sharpe: 1.0
expected_max_drawdown: 0.40
breakeven_cost_bps: 30
backtest_status: walk-forward-validated
related: ["[[variance-risk-premium]]", "[[options-premium-selling]]", "[[short-straddle]]", "[[short-strangle]]", "[[cboe-put-putwrite-index]]", "[[cboe-bxm-buywrite-index]]", "[[delta-hedging]]", "[[gamma-scalping]]", "[[vix-trading]]", "[[skew-trading]]", "[[tail-risk-hedging]]", "[[section-1256-contracts]]", "[[options-portfolio-construction]]"]
---

# Volatility Carry

**Volatility carry** is the systematic sale of options or variance contracts when implied volatility (IV) trades persistently above subsequent realized volatility (RV) — capturing the **variance risk premium** (VRP). The most common implementations are short ATM straddles or strangles delta-hedged daily, cash-secured short puts, covered calls, and (institutionally) variance and volatility swaps. The "carry" is the spread between the IV embedded in the sold option and the RV that subsequently delivers; over long horizons on the S&P 500, this spread averages **3-5 volatility points** annualized. The trade has long-run Sharpe near 1.0 in academic studies and is supported by indices like the **CBOE PUT** (PutWrite) and **CBOE BXM** (BuyWrite). The vulnerability is asymmetric and well-documented: vol-spike events (Feb 5, 2018 "Volmageddon"; Mar 2020 COVID) can wipe out years of carry in days.

This page covers the **canonical short-vol carry trade on broad equity indices**. Single-name, FX, commodity, and rates VRP harvesting share the same mechanics but face different liquidity, capacity, and tail profiles.

## Edge Source

**Primary**: Behavioral + Structural (per [[edge-taxonomy]]).

The **demand side** of the option market is structurally lopsided:

- **Asset owners and pension funds** systematically buy puts as portfolio insurance, with mandate-driven inelastic demand
- **Mutual funds, ETFs, and tail-risk funds** roll long volatility positions to hedge equity exposure
- **Retail investors** disproportionately buy lottery-ticket calls and protective puts; structurally net-long convexity
- **Dealers** delta-hedge their long-vol books by trading the underlying, generating mechanical flow that reinforces the premium

The **supply side** is concentrated in a smaller set of professional vol sellers (volatility funds, market makers' net inventory, structured product issuers, retail PutWrite/BuyWrite ETFs). The clearing price for risk transfer is therefore biased upward — IV systematically prices in **more** future realized volatility than actually arrives.

This is **not** a behavioral mispricing in the "irrational" sense — it is a **risk premium**. Buyers are paying for **negatively-correlated convex protection** that pays off precisely when the rest of their portfolio is hurting. Sellers earn the premium **because** they bear the asymmetric tail risk that buyers want to offload.

## Why This Edge Exists

The variance risk premium is one of the most well-documented persistent premia in financial markets. Three reinforcing mechanisms keep it alive:

### 1. Insurance Demand Asymmetry

Equity returns are negatively skewed and fat-tailed; investors are loss-averse with concave utility (especially institutional investors with drawdown-based mandates). They will **rationally pay more than fair actuarial value** for insurance that pays in down states. The VRP is the equilibrium price of that insurance.

### 2. Funding and Capital Constraints

Vol selling requires capital (margin) and balance sheet to absorb losses during spikes. The set of agents with sufficient capital, risk tolerance, and operational capability to sell volatility through a Volmageddon is small. Their required return for bearing that risk is high. The premium is the compensation for that **limited risk-bearing capacity**.

### 3. Dealer Hedging Reinforces Flow

When dealers are net long volatility from customer flow, their gamma hedging stabilizes spot. When customers buy more puts, dealers buy more puts from the supply side (vol sellers), bidding up IV. The premium widens precisely when carry sellers most want to underwrite, and compresses after risk-off resolves — generating a mean-reverting dynamic that disciplined sellers can exploit.

**Who keeps losing:** End-buyers of crash insurance over long horizons. They lose **most of the time** (small premium decay every month) and "win" only in tail events. Their loss is the carry seller's edge — and is **rational**, because the buyers value the negatively-correlated payoff. The trade is not "free money"; it is paid risk-bearing.

## Null Hypothesis

Under no-edge conditions: **IV ≈ RV in expectation**, so expected gross return on a delta-hedged short straddle is ~zero. After bid-ask, slippage on delta hedges, and assignment/exercise costs, expected net return is **modestly negative**. A vol carry strategy that does not produce statistically significant outperformance over the [[cboe-put-putwrite-index|PUT]] or [[cboe-bxm-buywrite-index|BXM]] benchmarks (which are themselves the simplest possible vol carry implementations) provides no evidence of skill — it would be consistent with the null.

A meaningful test for skill on top of the structural premium requires:

1. Net-of-costs Sharpe materially higher than PUT/BXM (~0.5-0.7 over 25+ years)
2. Drawdown profile no worse than benchmark in stress periods
3. Some evidence of timing — vol allocation responds to regime in a way that reduces tail without sacrificing carry

Most "vol arb" funds that purport to add skill do so through (a) cross-asset relative value, (b) skew/term-structure trades, or (c) dynamic sizing — not by improving the spot premium capture itself.

## Rules

The canonical short-vol carry trade on SPX:

### Entry

- **Underlying**: SPX (preferred — [[section-1256-contracts]] tax treatment, deep liquidity, no [[wash-sale-rules-options|wash sale]] friction). Alternatively SPY, ES futures options, or NDX/RUT for diversification.
- **Structure**: Short ATM straddle, ~30-delta strangle, or 25-delta cash-secured put. Strangles are the most common professional choice for risk balance.
- **Tenor**: 30-45 days to expiration (DTE) at entry. This is the [[theta]]-rich zone where time decay accelerates without holding excessive [[gamma]] risk.
- **Cadence**: New position every 1-2 weeks, laddered across expiries (avoids concentrating exposure in a single roll cycle). See [[expiration-laddering]].
- **IV regime filter** (optional but standard): Open positions only when **VIX or IV rank ≥ 30th percentile**. Below that, the premium is too thin to compensate for tail risk; sit out.
- **VRP filter** (advanced): Open only when **(VIX − 1-month trailing RV) > 2 vol points**. Confirms the premium is positive.

### Sizing

- **Notional cap**: vega exposure ≤ 1% of NAV per 1 vol point (i.e., a 5-vol spike costs ≤ 5% of NAV).
- **VAR cap**: position-level [[expected-shortfall|95% ES]] ≤ 3% of NAV.
- **Concentration**: total short vega ≤ 3-5% of NAV per 1 vol point across all positions.
- **Margin utilization**: ≤ 30% of [[portfolio-margin]] requirement at entry to leave headroom for spike-driven margin expansion.

### Exit

Each position has **three exit triggers**, whichever fires first:

1. **Profit target**: Close at **50% of maximum credit** (industry-standard rule from tastytrade research; balances hit rate against duration risk).
2. **Time stop**: Close at **21 DTE** regardless of P&L. Gamma risk accelerates inside 21 DTE without proportional theta benefit; the risk/reward turns unfavorable.
3. **Vol-spike kill**: Close immediately if **VIX rises by 50% in a single session** OR position [[delta]] exceeds 2× initial delta. This is the explicit tail-risk circuit breaker.

### Delta Hedging (advanced variant)

For pure VRP capture, delta-hedge the position daily (or intraday on vol-spike days):

- Compute net portfolio delta at close
- Trade ES or SPY shares to neutralize delta
- Track [[gamma-scalping]] P&L vs. theta as a diagnostic — if gamma scalping is consistently positive, IV was underpriced (rare in indexes)

For most retail/PM-account traders, **un-hedged short strangles are simpler** and capture most of the premium. Delta hedging adds cost and is most valuable for dispersion or single-name books.

### Implementation Variants Compared

| Vehicle | Purity of VRP capture | Operational complexity | Tail profile | Tax (US) | Typical user |
|---|---|---|---|---|---|
| Short ATM straddle (delta-hedged) | Highest (pure variance) | High (daily hedge) | Symmetric-ish gamma | [[section-1256-contracts\|§1256]] if SPX | Vol fund / PM |
| Short ~25-delta strangle | High | Moderate | Wider safe band, fatter tail | §1256 if SPX | Professional default |
| Cash-secured short put (25-delta) | Directional-tilted | Low | One-sided downside | §1256 if index | [[cboe-put-putwrite-index\|PUT]]-style |
| Covered call | Capped-upside variant | Low | Long-equity + short call | varies | [[cboe-bxm-buywrite-index\|BXM]]-style |
| [[variance-swap]] (OTC) | Pure, path-independent | Low to trade, ISDA overhead | Convex; cap basis | OTC | Institutional |
| Short [[vix-futures]] / inverse ETP | Term-structure carry, **not** realised VRP | Low | Catastrophic (XIV precedent) | varies | (Historically) retail — high blow-up risk |

The variance swap is the *cleanest* expression (no path-dependence, no roll), but it is OTC and institutional-only; for the instrument mechanics see [[variance-swap]] and [[variance-risk-premium]]. The inverse-ETP route looks easy but carries the [[volmageddon|February 2018]] blow-up risk and tracks the [[vix-futures]] curve rather than realised variance.

## Implementation Pseudocode

```python
def vol_carry_strategy(account, market_data, positions, today):
    # --- 1. Manage existing positions ---
    for pos in positions:
        # Profit target
        if pos.pnl >= 0.5 * pos.max_credit:
            close(pos, reason="50_pct_profit")
            continue
        # Time stop
        if pos.dte <= 21:
            close(pos, reason="21_dte")
            continue
        # Vol-spike kill
        if market_data.vix_change_pct >= 0.50 or abs(pos.delta) >= 2 * pos.entry_delta:
            close(pos, reason="vol_spike_kill")
            continue
        # Delta hedge (if hedged variant)
        if STRATEGY.delta_hedged:
            hedge_delta(pos, market_data)

    # --- 2. Open new positions if conditions met ---
    if can_open_new(account, positions):
        vix = market_data.vix
        rv = realized_vol(market_data.spx_returns, lookback=21)
        vrp = vix - rv
        iv_rank = percentile_rank(vix, lookback_days=252)

        if vix >= MIN_VIX and iv_rank >= 0.30 and vrp >= 2.0:
            # Find 30-45 DTE expiry
            expiry = select_expiry(market_data.spx_chain, target_dte=35)
            # 25-delta strangle: short put at 25-delta, short call at 25-delta
            short_put = find_strike(expiry, target_delta=-0.25)
            short_call = find_strike(expiry, target_delta=0.25)

            # Size by vega budget
            position_vega = short_put.vega + short_call.vega  # absolute
            max_contracts = account.nav * 0.01 / position_vega
            contracts = min(max_contracts, account.margin_capacity / margin_per_contract)

            sell_strangle(short_put, short_call, contracts)

def can_open_new(account, positions):
    total_short_vega = sum(p.vega for p in positions)
    return (
        total_short_vega < 0.05 * account.nav
        and account.margin_used / account.nav < 0.30
        and ladder_has_room(positions)  # avoid stacking same expiry
    )
```

## Indicators / Data Used

| Input | Purpose | Source |
|---|---|---|
| **VIX index** | Forward 30-day IV reference; entry filter | CBOE |
| **VVIX index** | Vol-of-vol; tail-regime monitor | CBOE |
| **SPX options chain** (full surface) | Strike selection, delta/vega/theta computation | OPRA / broker |
| **Realized volatility** (5/10/21/63 day) | VRP computation | Computed from SPX returns |
| **VIX term structure** (VX1-VX9) | Contango vs. backwardation regime detection | CBOE / CFE |
| **CBOE PUT / BXM indices** | Benchmark and historical reference | CBOE |
| **Skew (SKEW index, 25-delta skew)** | Tail pricing context | CBOE |
| **Greek aggregations** (portfolio Δ, Γ, Vega, Θ) | Risk monitoring | Broker analytics or computed |

The single most important real-time variable is the **VRP itself**: `IV − RV`. When VRP is positive and rising, the trade is paid; when VRP is negative (RV exceeding IV — a "stressed" regime), short vol is mathematically losing money in expectation.

## Example Trade

**Setup**: September 2024. SPX at 5,700. VIX at 18 (60th percentile). 21-day RV at 12. VRP = 6 vol points — a healthy entry.

**Trade**:
- Sell 1× SPX 35-DTE 25-delta strangle
  - Short 5,500 put @ $14.00
  - Short 5,900 call @ $11.00
  - Total credit: $25.00 × 100 = **$2,500 per contract**
- Buying power requirement (portfolio margin): ~$30,000

**Path A — base case (most common, ~75% historical probability of hitting 50% profit)**:
- Day 14: SPX at 5,720, VIX at 16. Strangle now worth $11.50.
- P&L = ($25.00 − $11.50) × 100 = +$1,350 (54% of max credit)
- **Close**: realized **$1,350 on $30k buying power = ~4.5% in 14 days**

**Path B — moderate vol spike (~20% historical probability)**:
- Day 7: news event, VIX jumps to 24, SPX -2%. Strangle worth $32.
- P&L = ($25 − $32) × 100 = −$700
- VIX up 33% — below 50% kill threshold; hold.
- Day 21: vol resolves, SPX recovers, VIX back to 18. Strangle worth $13.
- Close at 21 DTE: P&L = ($25 − $13) × 100 = +$1,200

**Path C — Volmageddon-style spike (~5% historical probability)**:
- Day 5: SPX gaps -4% overnight, VIX from 18 to 38 (+111%).
- Strangle worth $85.
- **Vol-spike kill triggers**: close at $85 → P&L = ($25 − $85) × 100 = **−$6,000 per contract**
- Loss of ~20% on buying power in one position; hits drawdown bands.

The expected value across these paths is positive — but path C dominates the **risk** calculation. Sizing must be such that even multiple simultaneous Path Cs do not threaten the book.

## Performance Characteristics

| Metric | Long-term estimate | Source / Caveat |
|---|---|---|
| **Gross annualized return** | 5-9% on capital allocated | Bondarenko (2014); Hill et al. (2006); BXM/PUT indices |
| **Net Sharpe (delta-hedged short variance)** | 0.8 - 1.2 | Carr & Wu (2009); Bakshi & Kapadia (2003) |
| **Max drawdown (post-cost, realistic)** | 30-40% | XIV blow-up (Feb 2018, −96% in one day, but XIV was levered ETP — comparable strategies showed 25-40% DDs); Mar 2020 |
| **Worst single day** | -10% to -25% | Volmageddon, Aug 2015, Mar 2020 |
| **Hit rate per trade (50% profit target)** | 70-80% | tastytrade 25-delta strangle research |
| **Skewness of returns** | Strongly negative | Defining feature; cannot be eliminated |
| **Kurtosis** | Very high (fat tails) | Required for risk modeling |
| **Correlation to S&P 500** | Slightly positive (0.2-0.4) in normal times; near +1 in crashes | The "wrong-way" correlation is the source of the premium |

The **CBOE PUT index** (cash-secured ATM put writes on SPX) has delivered **~9.5% annualized** since 1986 with **lower volatility** than the S&P 500 — but with comparable or worse drawdowns in crisis periods (2008: −32%; 2020: −24%; comparable to or slightly better than S&P 500 in those windows).

**Realistic cost overlay** (20-30 bps round-trip on each strangle, modest delta-hedge slippage): subtracts approximately 100-150 bps annualized from gross returns.

### Cost-Aware Return Waterfall (illustrative)

The following waterfall is **illustrative, not a backtest** — it shows how a gross premium is whittled down to a net figure by realistic frictions. Numbers are qualitative orders of magnitude, not promised returns:

| Step | Effect on annualized return | Notes |
|---|---|---|
| Gross VRP captured (IV − RV spread) | + (mid-single-digit %) | The structural premium; varies with regime |
| Bid-ask on entry/exit (20-30 bps round-trip) | − (~50-80 bps) | Wider on strangles than single legs |
| Delta-hedge slippage (hedged variant) | − (~30-70 bps) | Zero for un-hedged strangles |
| Roll/assignment friction, pin risk | − (small) | Mitigated by [[section-1256-contracts]] cash settlement |
| Tail-hedge drag (OTM put spread / VIX call overlay) | − (varies) | Insurance cost that caps Path-C losses |
| **Net** | **= modest positive in calm/normal regimes** | Goes **negative** in stressed (RV > IV) regimes |

The defining feature is that **the net is positive most of the time and sharply negative in the tail** — the cost overlay does not change the *shape* of the distribution, only shifts its mean down. See [[transaction-cost-modeling]].

### Regime and Term-Structure Sensitivity

Vol carry is not a constant-return strategy; its expectancy is conditional on the VRP regime and the [[vix-futures|VIX term structure]]:

| Regime | VRP (IV − RV) | VIX term structure | Carry expectancy | Action |
|---|---|---|---|---|
| Calm / contango | Positive, moderate | Upward (contango) | Positive, paid roll | Standard sizing |
| Elevated-but-stable | Large positive | Steep contango | Best risk/reward | Lean in (within sizing caps) |
| Compressed | Near zero / negative | Flat | Thin to negative | Sit out (IV-rank filter) |
| Stressed / spike | Negative (RV > IV) | Inverted (backwardation) | Negative; roll loses money | Suspend; tail hedge active |

Backwardation (front VX > back VX) is the single clearest tape-level warning that short vol is structurally unprofitable — rolling shorts in backwardation pays *negative* roll yield. See the kill criteria below and [[vix-trading]].

## Capacity Limits

| Implementation | Approximate capacity | Limit |
|---|---|---|
| **SPX index strangles** | $5-10B | Open interest / depth on listed strikes; market impact on rolls |
| **SPY equivalent** | $3-5B | Slightly thinner per strike; no §1256 advantage |
| **Single-name vol carry (e.g., AAPL)** | $50-200M per name | Liquidity drops sharply outside top 20 names |
| **Variance swaps (institutional)** | $1-5B+ | OTC dealer balance sheets; bilateral counterparty risk |
| **Volatility ETPs (XIV-style — retired)** | Was ~$2B at peak before Feb 2018 blow-up | Feedback loops created instability |

Index VRP capacity is large — multi-billion at the level of a single fund — but **systemic capacity** (the total amount of vol carry that can be sold to long-vol buyers at the prevailing VRP) is what shapes the premium itself. When too much capital chases short vol, **VRP compresses** and **tail risk concentrates** in the same hands. This is a **crowding trade** ([[crowding-risk]]: high) — the more popular the strategy, the smaller the premium and the larger the unwind when it goes wrong.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Vol-of-vol expansion / Volmageddon-style spike**. A sudden jump in IV from a low base, where IV moves multiple standard deviations in hours. Volmageddon (Feb 5, 2018): VIX from 17 to 37 in one session; XIV (an inverse vol ETP) lost ~96% in a day, blowing up the entire short-vol-ETP complex.
2. **Gap risk**. Overnight gap larger than the option's delta-implied move; daily delta hedging cannot react. Common around CPI, FOMC, geopolitical shocks.
3. **Regime change in VRP**. Persistent inversion (RV > IV) for weeks or months — happened in Q1 2020, Q4 2008. The strategy bleeds throughout the regime.
4. **Term-structure inversion** (backwardation). Front-month VX > back-month VX signals stressed vol; rolling shorts in backwardation is structurally unprofitable (negative roll yield on vol).
5. **Crowding-driven liquidity collapse**. When too many sellers all need to cover at once, bid-ask spreads explode and exits become impossible at modeled prices.
6. **Margin spiral**. A vol spike doubles or triples portfolio margin requirements — forced liquidations are executed at the worst prices.
7. **Pin / assignment risk** ([[pin-risk]], [[assignment]]) on cash-secured puts at expiration if not §1256-cash-settled.

Resilient implementations use:
- Hard vol-spike kill triggers
- Tail hedges (small long OTM put spread or VIX call overlay)
- Conservative sizing (3-5x lower than naive Kelly)
- Position laddering across expirations
- Index (§1256, cash-settled) rather than ETF or single-name

## Kill Criteria

Numerical thresholds at which the strategy should be paused or retired (see [[when-to-retire-a-strategy]]):

- **Drawdown > 25%** of allocated capital → pause for 30 days; review parameters
- **Drawdown > 40%** → retire and recapitalize from zero
- **Rolling 12-month Sharpe < 0** for 3 consecutive months → pause
- **VRP regime test**: if `mean(VIX − 21d RV)` over trailing 6 months falls below **0** → suspended carry; the structural premium has temporarily disappeared
- **VVIX > 150** sustained → vol-of-vol environment incompatible with carry; pause
- **Crowding indicator**: if dedicated short-vol AUM (CFTC vol-of-vol-related positioning, ETP balances) reaches prior peaks → reduce sizing 50%
- **Repeated stop-outs** (3+ vol-spike kills in a quarter) → pause for review

## Advantages

- **Persistent, well-documented premium** — VRP has been studied for 30+ years and survives across every major paper that has tested it
- **Positive expectancy with defined edge mechanism** (insurance pricing, not behavioral arbitrage)
- **Index implementation enjoys §1256 tax treatment** — 60/40 blended rate, no [[wash-sale-rules-options|wash sale]] complications
- **Capacity is large** at the index level — institutional-scale strategy
- **Benchmarkable** — direct comparison to [[cboe-put-putwrite-index|CBOE PUT]] and [[cboe-bxm-buywrite-index|BXM]] indices; transparency on whether the implementation adds value
- **High hit rate** at the trade level (70-80% with 50% profit targets) gives smooth-looking equity curves, supporting psychological discipline
- **Non-directional** — does not require directional view on equities; complements directional/momentum books
- **Funding-friendly** — naked short premium can be done in a [[portfolio-margin]] account at meaningful leverage

## Disadvantages

- **Catastrophic tail risk** — a single vol spike can wipe out years of carry. The strategy is **not** suited for capital you cannot afford to lose 30-40% of.
- **Negative skew** — wins look like losses in distribution shape; psychologically very hard to size and stay with
- **Crowded** — large pools of capital chase the same trade; VRP compresses in calm regimes, then unwinds violently
- **Path dependent** — entering during compressed VRP regimes has materially worse expected return than at elevated VRP
- **Margin sensitivity** — portfolio margin requirements expand exactly when capacity is most needed; broker-driven forced liquidations during stress are a documented failure mode
- **Operational complexity** — daily Greek aggregation, delta hedging, expiry management
- **Regulatory / counterparty risk** — variance swaps and OTC structures introduce dealer counterparty exposure; ETP-based implementations historically have collapsed (XIV)
- **Behavioral risk** — many traders cannot size correctly; returns to 50% leverage Kelly under typical assumptions are far smaller than the math suggests because realized tails are fatter than modeled

## Sources

- Bakshi, G., & Kapadia, N. (2003). "Delta-Hedged Gains and the Negative Market Volatility Risk Premium." *Review of Financial Studies*.
- Carr, P., & Wu, L. (2009). "Variance Risk Premiums." *Review of Financial Studies*.
- Bondarenko, O. (2014). "Why Are Put Options So Expensive?" *Quarterly Journal of Finance*.
- Hill, J., Balasubramanian, V., Gregory, K., & Tierens, I. (2006). "Finding Alpha via Covered Index Writing." *Financial Analysts Journal*.
- CBOE PUT and BXM index methodologies and historical data (cboe.com)
- tastytrade research: 25-delta strangle, 50% profit target, 21 DTE management studies
- Coval, J., & Shumway, T. (2001). "Expected Option Returns." *Journal of Finance*.
- Volmageddon post-mortems: Feb 5, 2018 XIV termination event analyses

## Related

- [[variance-risk-premium]] — the underlying premium being harvested
- [[options-premium-selling]] — broader category
- [[short-straddle]] — common implementation
- [[short-strangle]] — preferred professional implementation
- [[cboe-put-putwrite-index]] — benchmark index for cash-secured put writing
- [[cboe-bxm-buywrite-index]] — benchmark index for covered calls (alternative VRP harvest)
- [[delta-hedging]] — required for pure variance capture
- [[gamma-scalping]] — diagnostic and the long-vol counterpart
- [[vix-trading]] — related vol product complex
- [[skew-trading]] — adjacent vol surface trade
- [[tail-risk-hedging]] — the buy-side counterpart that pays the VRP
- [[section-1256-contracts]] — index option tax treatment
- [[options-portfolio-construction]]
- [[options-stress-testing]]
- [[crowding-risk]]
- [[itpm-playbook]]
- [[variance-swap]] — the cleanest (institutional, OTC) VRP-capture instrument
- [[expiration-laddering]] — the portfolio-construction layer that makes carry survivable
- [[volmageddon]] — the canonical short-vol blow-up event (Feb 5, 2018)
- [[transaction-cost-modeling]] — turning gross VRP into a realistic net figure
