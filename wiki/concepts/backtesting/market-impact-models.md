---
title: "Market Impact Models"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [backtesting, market-impact, execution, market-microstructure, transaction-costs, slippage]
aliases: ["Market Impact", "Almgren-Chriss", "Square-Root Impact Law"]
domain: [backtesting, market-microstructure]
difficulty: advanced
related: ["[[backtesting-overview]]", "[[transaction-cost-modeling]]", "[[slippage-modeling]]", "[[slippage]]", "[[execution-algorithms]]", "[[implementation-shortfall]]", "[[bid-ask-spread]]", "[[strategy-capacity]]"]
---

# Market Impact Models

Models that estimate how much your own trade moves the market against you. Market impact is the dominant transaction cost for institutional sizes and the most important component to model in any backtest where the strategy might deploy meaningful capital.

## Two Components: Temporary and Permanent

Market impact is one component of the broader [[transaction-cost-modeling|transaction-cost stack]] and is, for institutional sizes, usually the largest. Where it sits relative to the other costs:

| Cost component | Scales with | Dominant for | Modeled in |
|---|---|---|---|
| Commissions / fees | Per-trade or per-share | All sizes | [[transaction-cost-modeling]] |
| [[bid-ask-spread\|Bid-ask spread]] | Liquidity, time of day | Small / fast trades | [[slippage-modeling]] |
| Market impact (this page) | √(size / ADV) × vol | Large trades, high turnover | This page |
| Timing / drift cost | Execution horizon × vol | Slow executions | [[implementation-shortfall]] |
| Opportunity cost | Unfilled portion | Aggressive limit orders | [[implementation-shortfall]] |

The sum of these realised against an arrival benchmark is the [[implementation-shortfall|implementation shortfall]]. Market impact decomposes further into temporary and permanent parts.

### Temporary impact
The portion of price movement that mean-reverts after the trade is finished. Caused by liquidity consumption — your trade exhausted the top of the order book, and once you're done, the book refills and price normalizes.

### Permanent impact
The portion that does *not* mean-revert. Caused by the *information* your trade conveyed to other participants. If you bought 5% of daily volume, the market infers that someone has positive information about the asset and adjusts its expectations.

A trade's total impact is the sum: `total impact = temporary + permanent`. For most equity strategies, temporary impact is 60-80% of total and permanent impact is 20-40%.

## The Square-Root Law

The dominant empirical regularity. For institutional-sized trades:

```
impact (bps) ≈ k × σ_daily × √(Q / V)
```

Where:
- `σ_daily` = daily volatility of the asset (in bps)
- `Q` = trade size
- `V` = average daily volume (ADV)
- `k` ≈ 0.5-1.5 (varies by asset class and execution style)

The square-root form is empirically robust across equity markets, FX, and futures. It says:

- Doubling trade size multiplies impact by ~1.41 (not 2)
- Trading 10% of ADV moves price by roughly 3x as much as trading 1% of ADV
- Impact scales linearly with volatility — high-vol assets are more expensive to trade

### Example

Trading 5% of ADV in a stock with 200 bps daily volatility, k = 0.7:

```
impact ≈ 0.7 × 200 × √0.05
       ≈ 0.7 × 200 × 0.224
       ≈ 31 bps round-trip (or ~16 bps per side)
```

For a strategy with 50 bps gross expected return per round trip, this trade leaves only ~19 bps net. For a strategy with 30 bps gross return per round trip, the trade is unprofitable after impact.

## Almgren-Chriss

The most widely-used parametric model. Decomposes impact into:

```
impact = γ × Q  +  η × (Q / T)
```

Where:
- `γ` (gamma) is the *permanent* impact coefficient — proportional to trade size
- `η` (eta) is the *temporary* impact coefficient — proportional to *trade rate* (size per unit time)
- `Q` = total trade size
- `T` = time over which the trade is executed

The optimal execution problem becomes: minimize `expected cost + risk aversion × variance of cost`, subject to the impact model. Almgren and Chriss derived the optimal trajectory: a frontloaded execution profile where the optimal slice size declines over time.

The key insight: there's a tradeoff between *impact* (faster trading is more expensive) and *risk* (slower trading exposes you to price drift before the trade is done). The optimal execution rate balances them.

### The efficient frontier of execution

Almgren-Chriss frames execution as a mean-variance problem identical in spirit to portfolio choice. Each trading trajectory produces an **expected cost** (mostly temporary impact, which falls as you slow down) and a **variance of cost** (price-drift risk, which rises as you slow down). Plotting all trajectories traces an *efficient frontier of execution*:

```
expected cost
   │   ●  aggressive (fast): high impact, low risk
   │    ╲
   │     ╲___ frontier of optimal trajectories
   │         ╲___
   │             ╲●  patient (slow): low impact, high risk
   └────────────────── variance of cost
```

The trader's risk-aversion parameter λ selects a point on the frontier:

- **λ → 0** (risk-neutral): minimise expected cost → trade slowly, accept drift risk. Converges toward a near-[[vwap|VWAP]] schedule.
- **λ → ∞** (risk-averse): minimise cost variance → trade immediately, accept impact. Converges toward a single block.
- **λ moderate**: a front-loaded exponential decay — trade more early (when remaining-position risk is highest), less later.

The closed-form optimal trajectory under the linear Almgren-Chriss model is an exponentially-decaying holdings path; the higher the risk aversion or the volatility, the steeper the front-loading. This is the theoretical backbone of the [[execution-algorithms|implementation-shortfall / arrival-price execution algorithms]] that brokers sell.

## Calibrating Impact Coefficients

Impact coefficients are asset-specific and venue-specific. Calibration requires real execution data:

1. Collect a dataset of your historical fills
2. For each fill, compute realized impact = (execution price − arrival price) / arrival price
3. Compute trade-size-to-volume ratio for each fill
4. Regress impact against `√(Q/V) × σ` to estimate `k`

For most institutional traders, k is in the 0.5-1.5 range for equities. Less liquid markets (small caps, illiquid options) can have k of 2-5. HFT venues with maker rebates and tight spreads can have negative effective impact (you're paid to provide liquidity).

If you don't have execution data, use Almgren et al. (2005) "Direct Estimation of Equity Market Impact" calibrations as a starting point.

## Linear vs. Square-Root vs. Concave Models

Different functional forms have different theoretical justifications:

- **Linear:** `impact ∝ Q`. Theoretically wrong (doesn't match data) but mathematically convenient. Predicts that doubling trade size doubles cost — too pessimistic.
- **Square-root:** `impact ∝ √Q`. Empirically supported. Used in most modern models.
- **Concave (general):** `impact ∝ Q^α` for some `α < 1`. Square-root is the special case with α = 0.5.

The empirical α is usually between 0.4 and 0.6, so square-root is a good default. Some markets (illiquid, HFT) deviate.

### Model comparison at a glance

| Model | Functional form | Captures | Best for | Key limitation |
|---|---|---|---|---|
| Fixed bps | constant | Nothing size-dependent | Small trades vs ADV | Wrong whenever size matters |
| Linear | `impact ∝ Q` | Permanent-only intuition | Quick conservatism | Too pessimistic at size |
| Square-root | `impact ∝ √(Q/V)·σ` | Empirical concavity | Most backtests | Breaks > ~25% ADV |
| Concave (general) | `impact ∝ (Q/V)^α`, α<1 | Tunable curvature | Calibrated desks | Needs fill data for α |
| Kyle (linear, info) | `Δp = λ·order flow` | Information / adverse selection | Theory, microstructure | Linear by assumption |
| [[#Almgren-Chriss\|Almgren-Chriss]] | permanent + temporary, time-resolved | Impact-vs-risk tradeoff | Optimal execution, capacity | Needs both coefficients calibrated |

[[kyle-lambda|Kyle's λ]] sits behind the *permanent* component: it is the price-impact-per-unit-order-flow coefficient that ties impact to the information content of the trade. The square-root law is the empirical *aggregate* regularity; Almgren-Chriss is the *operational* model that splits impact by time so an execution schedule can be optimised.

## Latent Liquidity and the Limits of the Square-Root Law

The square-root law breaks down at extremes:

- **Very small trades** (< 0.1% of ADV): impact is essentially the bid-ask spread plus a small temporary bump
- **Very large trades** (> 50% of ADV): impact grows faster than square-root because you exhaust the latent liquidity in the order book
- **Block trades** through dark pools or RFQ: bypass the LIT market and pay a different cost structure

For backtesting purposes, square-root is a reasonable assumption for trade sizes between 0.1% and 25% of ADV. Outside that range, more careful modeling is needed.

## Impact in Crypto

Crypto markets have several special features that affect impact modeling:

1. **Fragmented liquidity** — depth on Binance is not depth on Coinbase. Effective ADV for impact purposes depends on which venues you can route through.
2. **No regulated reporting** — much of crypto trading is wash, spoofed, or otherwise non-genuine. Reported volume overstates real liquidity.
3. **Cross-venue impact** — a large trade on one venue moves prices on others within seconds via arbitrage.
4. **Funding rate feedback** — large perp trades shift funding rates, which then induce flows from arbitrageurs.

For practical purposes, multiply your equity-style impact estimate by 1.5-2x for liquid crypto pairs, and by 5-10x for less liquid altcoins.

## Impact in Options

Options have additional impact channels:

1. **Vega impact** — large options trades move implied volatility, not just price
2. **Pin risk** — near-expiration trades concentrate impact on specific strikes
3. **Dealer hedging** — when dealers take the other side, they immediately delta-hedge in the underlying, generating *secondary* impact

A common simplification: model impact in vol-points rather than dollars, since options premium is more vol-sensitive than price-sensitive.

## How to Use in a Backtest

Three levels of sophistication:

### Level 1: Fixed bps per trade
Add a constant impact cost (e.g., 5 bps round-trip) regardless of trade size. Crude but better than nothing. Appropriate when trade sizes are small relative to ADV.

### Level 2: Square-root law
Compute impact per trade using `k × σ × √(Q/V)`. Appropriate for any strategy where size matters.

### Level 3: Almgren-Chriss with execution simulation
Model the trade as a multi-slice execution over time, with both temporary and permanent components, calibrated to actual venue depth. Required for realistic capacity estimation in serious institutional backtests.

For most strategies, Level 2 is sufficient. Strategies that are deliberately exploring capacity should use Level 3.

## Capacity Implications

The square-root law lets you compute strategy capacity:

```
breakeven Q* / V = (gross alpha per trade / k / σ)²
```

For a strategy with 50 bps gross alpha per round-trip, k = 0.7, and σ = 200 bps:

```
breakeven Q* / V = (50 / 0.7 / 200)² = (0.357)² ≈ 0.127
```

The strategy can trade up to ~13% of ADV before impact eats all the alpha. Beyond that point, additional capital reduces total profit.

This is *the* reason most retail-friendly strategies don't scale to institutional sizes. The square-root law is harsh at the high end. See [[strategy-capacity]] for how this breakeven feeds the capacity field on every [[strategies-overview|strategy page]].

## Common Pitfalls in Backtests

| Pitfall | What it does | Fix |
|---|---|---|
| Ignoring impact entirely | Inflates net returns, makes capacity look infinite | At minimum Level 1 fixed bps; Level 2 if size matters |
| Using full-period ADV | Overstates liquidity on the days you actually traded | Use trailing or same-day ADV |
| Modeling impact but not the spread | Double-counts liquidity savings | Add [[bid-ask-spread\|spread]] + impact + fees separately |
| Assuming you fill at the mid | Hides the cost of crossing | Fill at the touch or worse for marketable orders |
| Linear impact "to be safe" | Over-penalises, may kill a real edge | Square-root is the empirically correct default |
| Same `k` across regimes | Impact rises in stressed, thin markets | Stress `k` upward for crisis backtests |

A backtest that survives a Level 2 square-root overlay *and* a stressed-`k` sensitivity check is far more credible than one tuned on frictionless fills. See [[backtesting-overview]] and [[transaction-cost-modeling]].

## Sources

- Almgren & Chriss (2001) "Optimal Execution of Portfolio Transactions" — *Journal of Risk*
- Almgren, Thum, Hauptmann, Li (2005) "Direct Estimation of Equity Market Impact" — RiskMetrics
- Kyle (1985) "Continuous Auctions and Insider Trading" — *Econometrica*
- Tóth et al. (2011) "Anomalous Price Impact and the Critical Nature of Liquidity" — *Physical Review X*
- [[book-trading-and-exchanges]] — Harris on the microstructure foundations

## Related

- [[backtesting-overview]]
- [[transaction-cost-modeling]]
- [[slippage-modeling]]
- [[slippage]]
- [[execution-algorithms]]
- [[implementation-shortfall]]
- [[bid-ask-spread]]
- [[strategy-capacity]]
- [[kyle-lambda]]
- [[vwap]]
