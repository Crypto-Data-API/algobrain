---
title: "Volatility Risk Premium"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [anomalies, volatility, options, risk-premium]
aliases: ["VRP", "Variance Risk Premium", "Variance Premium", "Implied vs Realized Vol", "Vol Risk Premium", "Volatility Risk Premium"]
domain: [anomalies, volatility]
difficulty: advanced
related: ["[[anomalies-overview]]", "[[volatility]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[vix]]", "[[vol-of-vol]]", "[[vvix]]", "[[volga]]", "[[carry-anomaly]]", "[[edge-taxonomy]]", "[[iron-condor]]", "[[short-strangle]]", "[[gamma-scalping]]"]
---

# Volatility Risk Premium

The empirical regularity that the *implied volatility* of options consistently exceeds the *realized volatility* of the underlying asset, on average and across market regimes. Equivalently: option sellers earn a positive expected return because the market overprices the cost of insurance against price moves. The single most-traded "anomaly" in the modern era — the basis of vol-selling strategies that have absorbed tens of billions in capital. Also one of the most catastrophic when it crashes.

## The Definition

The volatility risk premium (VRP) is:

```
VRP = E[Implied Vol] − E[Realized Vol]
```

Or, equivalently in variance terms:

```
Variance Risk Premium = E[IV²] − E[RV²]
```

Empirically, IV² > RV² on average across nearly all liquid options markets. The gap is positive in approximately 80-90% of months for SPX options, with the size of the gap roughly proportional to the level of vol.

### The two "spreads" that get conflated

Two distinct objects travel under the VRP banner, and confusing them causes most measurement errors:

| Object | Definition | What captures it |
|---|---|---|
| **Volatility risk premium** | E[IV] − E[RV], in vol points | Difference of standard deviations |
| **Variance risk premium** | E[IV²] − E[RV²], in variance units | The quantity a [[variance-swap]] pays |
| **Ex-ante VRP** | Today's IV minus a forecast of future RV | Forecasting model + current [[vix\|VIX]] |
| **Ex-post VRP** | Today's IV minus the RV that *actually* showed up | Realized after the fact |

The variance form is the cleaner theoretical object because a variance swap pays linearly in realized variance, so its fair strike *is* the risk-neutral expectation of RV². The vol form is what most discretionary traders eyeball off the [[vix\|VIX]]-minus-20-day-RV chart. They tell the same story directionally but differ in units and in how they weight the tail (variance over-weights large moves).

### IV-minus-RV harvesting in practice

The mechanical core of every VRP strategy is *harvesting the IV-RV gap*: sell an instrument priced off IV, then delta-hedge so that the position's P&L tracks (IV² − RV²) rather than the direction of the underlying. A delta-hedged short straddle, held to expiry and rehedged continuously, earns approximately:

```
P&L ≈ Σ ½ × Gamma_t × S_t² × (IV² − RV²_realized) × dt
```

— i.e. you collect the gap between the variance you *sold* (IV²) and the variance that *materialized* (RV²), weighted by dollar gamma each day. When realized stays below implied, the sum is positive; on a violent up-day in RV, a single term can swamp weeks of accumulated premium. This is the same convexity that [[gamma-scalping]] exploits from the *long* side. The seller is short gamma, short [[vol-of-vol]], and short the tail.

## The Original Finding

The VRP has been documented in multiple papers since the late 1990s:

- **Bakshi & Kapadia (2003)** — formalized the VRP for SPX
- **Carr & Wu (2009)** "Variance Risk Premiums" — *Review of Financial Studies* — comprehensive cross-asset documentation
- **Bollerslev, Tauchen, Zhou (2009)** — VRP as a return predictor for equity markets

The result: across S&P 500 and most major indices, average implied vol is approximately 3-5 percentage points higher than average realized vol. A short-vol position (sell options, hedge delta) has historically earned approximately **8-12% per year with Sharpe 0.5-0.8** before catastrophic events.

## What It Says

The market overprices insurance against volatility. Option buyers pay too much; option sellers earn the difference. The VRP exists for the same reasons all insurance markets have positive premiums for the seller: insurance provides utility beyond expected value, and people overpay for protection.

For trading strategies, this means systematic short-vol strategies have positive expected returns. The catch is the *crash risk*: when realized volatility spikes, short-vol strategies lose catastrophically.

## The Mechanism

Three theories, all partially correct:

### 1. Insurance Demand
Investors hold equity portfolios and want to hedge against crashes. They are willing to pay a premium for puts as crash insurance, just as homeowners pay above-fair-value for fire insurance. The premium reflects the *utility* of having insurance, not just expected payout.

### 2. Skewness Aversion
Investors prefer assets with positive skew and dislike negative skew. Stocks have negative skew (occasional crashes), and options magnify this. Selling puts means *adding* negative skew, which investors are reluctant to do; the VRP compensates the few who are willing.

### 3. Limits to Arbitrage
Selling options requires margin, has tail risk, and is psychologically uncomfortable. The set of investors willing to sell vol systematically is small. The VRP reflects the small effective supply.

In the [[edge-taxonomy]], VRP is **risk-bearing** — you earn the premium because you accept the tail risk.

## Replication Status

The VRP has been replicated extensively:
- **SPX options** — robust from the early 1990s onward
- **International equity indices** — DAX, FTSE, Nikkei, Euro Stoxx all show positive VRPs
- **Currency options** — EUR/USD, USD/JPY etc.
- **Commodity options** — oil, gold (smaller and noisier)
- **VIX itself** — selling VIX futures is a vol-of-vol VRP play

It is one of the most empirically robust patterns in derivatives markets.

## The Crash Profile

VRP strategies have a defining drawdown profile: years of smooth gains punctuated by catastrophic months. The return distribution is the textbook **negative skew, high kurtosis** shape — a left tail far fatter than a normal distribution, which is exactly what you would expect from selling insurance. Plotted as an equity curve it looks like "picking up nickels in front of a steamroller": a gentle, almost suspiciously smooth upward slope, then a vertical cliff.

The defining feature is the *asymmetry between the body and the tail*. A naive backtest that samples only the body (calm years) reports a Sharpe of 0.8-1.0 and a tiny max drawdown — and is dangerously misleading, because the strategy's true risk lives almost entirely in a handful of months that the backtest window may not even contain. This is the canonical example of an [[edge-taxonomy|risk-bearing]] edge whose Sharpe is overstated by any analysis that does not deliberately stress the tail. See [[deflated-sharpe-ratio]] and [[overfitting]] for why short-vol backtests flatter themselves.

**Famous VRP crashes:**
- **August 1998** — LTCM-related vol spike
- **September 2001** — 9/11 vol spike
- **May 2010** — flash crash
- **August 2011** — US debt downgrade
- **August 2015** — China devaluation
- **February 2018** — "Volmageddon" — XIV ETF wiped out overnight, many short-vol traders blew up
- **March 2020** — COVID crash, VIX hit 80+
- **April 2025** — vol spike

Each event produced single-month losses in the 30-100% range for naive short-vol strategies. The leveraged short-vol products (XIV, SVXY in their original form) lost essentially everything in February 2018.

The VRP literature universally agrees: the strategy *has* positive expected returns, *and* has crash risk that destroys naive implementations. Profitable VRP trading requires sizing for the tail, not the body, of the distribution.

### Drawdown profile at a glance

| Phase | Frequency | Typical contribution to P&L | What the naive backtest sees |
|---|---|---|---|
| **Body** (calm months) | ~85-90% of months | Small, steady positive | A smooth, attractive equity curve |
| **Mild stress** | ~8-12% of months | Small negative, quickly recovered | Minor dips |
| **Tail event** | A few months per decade | -30% to -100% in a single month | Often *absent* from a short backtest window |

The lesson encoded in this table: a VRP track record is only as informative as the number of *tail events* it contains. A five-year backtest with zero crashes tells you almost nothing about the strategy's risk.

## How to Capture the VRP Without Blowing Up

Several practical refinements:

### 1. Always Buy Tail Insurance
Sell ATM straddles or strangles, but *also* buy deep OTM wings. The wings cost a small fraction of the ATM premium but cap the maximum loss. This is the iron condor / iron butterfly approach. See [[iron-condor]], [[iron-butterfly]].

### 2. Size by Vol-of-Vol
Position size should be inversely proportional to current implied volatility (or [[vix\|VIX]] level), and ideally adjusted for [[vol-of-vol]] as well. When VIX is high, the strategy is risky — size down. When VIX is low, size up. This produces a natural reduction in exposure during stress. A more complete rule also watches [[vvix\|VVIX]]: when vol-of-vol is elevated, the *convexity* of the loss ([[volga]]) is larger for the same vega, so the seller should size down even if VIX itself looks ordinary. Selling vol when both VIX and VVIX are low is the cheapest-insurance regime to be *short*; selling when VVIX has already spiked is selling convexity that has already become expensive to be short.

### 3. Stop-Loss Rules
Pre-commit to closing positions when losses exceed some threshold (e.g., 2x the credit received). This caps individual trade losses and prevents the catastrophic single-trade blowup.

### 4. Term Structure Filtering
Sell vol only when the VIX term structure is in *contango* (longer-dated VIX > shorter-dated VIX). When the curve inverts to backwardation (panic regime), step aside. Backwardation periods are where VRP strategies historically lose the most.

### 5. Diversify Across Strikes and Expirations
Don't concentrate in a single trade. Run a portfolio of small positions across different strikes, expirations, and underlyings.

### 6. Vol-Targeting Overlay
Use a strategy-level volatility target. When realized volatility of the strategy itself exceeds the target, reduce size. This is a self-correcting mechanism.

### Capture-method decision table

| Implementation | Tail capped? | Premium per trade | Best regime | Worst-case failure |
|---|---|---|---|---|
| Naked short straddle/strangle | No | Highest | Calm, range-bound | Unbounded — single gap can wipe the book |
| [[iron-condor]] / [[iron-butterfly]] | Yes (wings) | Medium | Most regimes; the default "managed-risk" form | Max loss = width − credit, but realized often |
| Short [[vix]] futures (contango) | No | High + roll yield | Term structure in [[contango]] | Backwardation spikes — [[xiv-collapse\|XIV-style]] wipeout |
| Sell [[variance-swap]] | No (linear in variance) | Medium | Institutional, hedge-able | Variance over-weights the tail; brutal in a crash |
| dispersion-trading | Partially | Medium | When index IV >> single-name IV | [[implied-correlation]] spike (everything crashes together) |
| [[calendar-spread]] (sell front) | Partially | Low | Stable term structure | Curve inversion |

The vertical axis here *is* the risk-management spectrum: every move down the "tail capped" column trades premium for survivability. The historical graveyard (XIV, original SVXY) is populated entirely by the "No" rows run at leverage.

## Worked Example

A trader runs a defined-risk VRP program on SPX over a year, illustrating the body-vs-tail asymmetry. Numbers are illustrative.

- **Structure**: 30-DTE [[iron-condor]], short strikes at ~1σ, long wings ~30 points further out. Credit ≈ $2.00 per condor; max loss ≈ $8.00 (the $10 wing width minus credit).
- **Body**: In 10 of 12 months, SPX stays inside the short strikes. Each condor expires near full profit, ≈ +$1.80 net after the occasional adjustment. Ten winning months ≈ +$18 per condor.
- **One mild loser**: A choppy month forces an early close at −$3. Running total ≈ +$15.
- **The tail month**: A surprise [[cpi-release\|CPI]] print or a [[vix-august-2024-spike\|carry-unwind]]-style shock gaps SPX through the short strike. The condor realizes near max loss, −$7.50. Running total ≈ +$7.50 for the year.

The lesson: ten clean wins were *halved* by one tail month — and that is the *defined-risk* version. The naked-strangle version of the same year, with no wings, would have taken a loss many multiples of the annual premium in that single month. The wings cost roughly a third of the gross premium in calm months; that is the price of converting "unbounded" into "merely painful." See [[iron-condor]] for the structure mechanics.

## Variations

### Short Straddles / Strangles
The simplest implementation. Sell ATM or slightly OTM call and put on the same underlying. Profitable if the underlying stays range-bound. Catastrophic if it makes a large move.

### Iron Condors
Sell a put spread and a call spread on the same underlying. Limited maximum loss (the wings hedge), but smaller premium per trade. The most popular "managed-risk" VRP strategy. See [[iron-condor]].

### Variance Swaps / VIX Futures
Direct exposure to variance or VIX. Selling VIX futures (when curve is in contango) earns the vol risk premium plus the roll yield. Far more extreme tail risk than equity options.

### Dispersion Trading
Sell index volatility and buy single-stock volatilities. Captures the difference between index implied vol (which is over-priced due to crash hedging demand) and single-name vols (less affected). See dispersion-trading.

### Calendar Spreads
Sell short-dated options (which have higher IV per unit time) and buy long-dated options. Captures the term structure premium with less directional exposure.

### Vega-Theta Trading
Optimize for the ratio of theta (time decay) to vega (vol exposure). Higher theta-to-vega is more "income-like"; lower is more "vol-bet-like."

## Common Pitfalls

1. **Backtesting only the body.** A window with no crash (e.g. 2012-2017) shows a glorious Sharpe and a tiny drawdown. The strategy's real risk is the months *outside* the sample. Always include 2008, 2018, and 2020 — or assume the true tail is worse than anything in your data.
2. **Confusing the vol and variance premia.** Sizing a variance-swap book off a vol-points VRP chart misstates exposure because variance over-weights large moves. Match the metric to the instrument.
3. **Selling vol because it "looks high."** A high [[vix\|VIX]] is often *justified* by high realized vol to come — the VRP can be small or negative precisely when IV is elevated. The edge is the *gap*, not the level.
4. **Ignoring vol-of-vol.** Two positions with identical vega can have wildly different [[volga]] exposure; the high-[[vvix\|VVIX]] one loses far more convexly. Vega caps that ignore [[vol-of-vol]] systematically undersize the tail.
5. **Static sizing through regimes.** Selling the same notional in [[contango]] and [[backwardation]] is the classic error — backwardation is where VRP strategies historically lose the most.
6. **Correlation blindness.** In a crash *every* short-vol book loses at once. The drawdown is the *correlated* sum across positions, which is far worse than the sum of standalone max-losses. See [[implied-correlation]].
7. **Treating defined-risk as safe.** An [[iron-condor]] caps the per-trade loss but a clustered run of max-loss months can still be a deep drawdown. "Capped" is not "small."

## Current Viability

The VRP remains positive on average but the Sharpe is significantly compressed from earlier decades. After the 2018 Volmageddon, the more extreme leveraged products have died, but the underlying strategy continues. Realistic Sharpe for a well-managed VRP strategy is now 0.4-0.6 with strict tail management — down from historical 0.8-1.0.

The single biggest risk is *correlation surprise* during a crash: when vol spikes, *all* short-vol strategies lose simultaneously, and the strategy's drawdown is far worse than the historical body would suggest.

Recommended use: as one component of a larger portfolio, sized small enough that a 50% drawdown of the VRP allocation doesn't endanger the whole book. Combined with [[trend-plus-tail-hedge|trend or tail hedge]] for explicit crash protection.

## Strategies That Implement It

- [[short-straddle]]
- [[short-strangle]]
- [[iron-condor]]
- [[iron-butterfly]]
- [[options-selling]]
- [[wheel-strategy]]
- [[gamma-scalping]] (long side of VRP)
- [[vix-trading]]

## Sources

- Bakshi & Kapadia (2003) "Delta-Hedged Gains and the Negative Market Volatility Risk Premium" — *Review of Financial Studies*
- Carr & Wu (2009) "Variance Risk Premiums" — *Review of Financial Studies*
- Bollerslev, Tauchen, Zhou (2009) "Expected Stock Returns and Variance Risk Premia" — *Review of Financial Studies*
- [[book-options-volatility-and-pricing]] — Natenberg
- [[book-trading-volatility]] — Bennett

## Related

- [[anomalies-overview]]
- [[volatility]]
- [[implied-volatility]] — the price the seller collects
- [[realized-volatility]] — the variance that actually shows up
- [[vix]] — the standardized SPX IV gauge the VRP is read off
- [[vol-of-vol]] — governs the convexity of VRP losses
- [[vvix]] — implied vol-of-vol; the price of the seller's [[volga]] risk
- [[volga]] — the second-order Greek that prices the crash convexity
- [[carry-anomaly]] — sibling risk-bearing premium
- [[edge-taxonomy]] — VRP is the canonical risk-bearing edge
- [[gamma-scalping]] — the long side of the same trade
- [[iron-condor]] — the default defined-risk implementation
- [[deflated-sharpe-ratio]] — why short-vol backtests overstate Sharpe
- [[options-greeks]]
