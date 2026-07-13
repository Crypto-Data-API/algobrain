---
title: "Slippage Modeling"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [backtesting, slippage, execution, transaction-costs]
aliases: ["Slippage", "Implementation Cost"]
domain: [backtesting, market-microstructure]
difficulty: intermediate
related: ["[[backtesting-overview]]", "[[transaction-cost-modeling]]", "[[market-impact-models]]", "[[execution-algorithms]]", "[[implementation-shortfall]]", "[[bid-ask-spread]]", "[[adverse-selection]]", "[[slippage]]", "[[deflated-sharpe-ratio]]", "[[overfitting]]"]
---

# Slippage Modeling

Slippage is the difference between the price you expected to get and the price you actually got, after accounting for spread and impact. It is the residual execution cost — the part that comes from latency, partial fills, adverse selection, and order routing decisions. Most retail backtests ignore it; most institutional backtests model it crudely. Both are mistakes.

## Sources of Slippage

### 1. Latency

The time between when your strategy decides to trade and when the order reaches the exchange. During this gap, the market moves. If it moves in your direction, you get an unfavorable fill (because the price you wanted is no longer available); if it moves against you, the order may not fill at all.

For strategies that send marketable orders, latency directly translates into adverse selection: the orders that fill are disproportionately the ones where the market moved away from you.

### 2. Partial Fills

You send a market order for 10,000 shares. The top of the book has 3,000 at $100, then 4,000 at $100.01, then 5,000 at $100.02. You get filled at three different prices, with an average above the price you saw when you decided. The "saw" price is your reference; the realized average is the slippage relative to it.

### 3. Order Book Churn

Between the time you saw the book and the time your order arrives, other participants have already taken or moved liquidity. The book you trade against is not the book you decided on.

### 4. Adverse Selection

A subtle one: the orders that fill are not a random sample. They are the orders where the market was *willing* to fill you — which usually means the counterparty had a reason to be on the other side. For market makers, this is the entire game: the spread compensates them for the adverse-selection risk of being filled by informed flow.

For takers (you, the strategy), adverse selection works the opposite way: your fills are disproportionately ones where you were on the wrong side.

### 5. Routing Decisions

Smart order routers make decisions about where to send each child order based on displayed prices, expected fill rates, and venue rebates. These decisions are imperfect — sometimes the router picks a venue that quotes a good price but doesn't have real depth.

### 6. Time-of-Day Effects

Open and close auctions, lunchtime liquidity droughts, news events — all change the slippage profile minute to minute. Strategies that trade across the day need a slippage model that varies with time.

## A Simple Model

For backtesting purposes, a defensible starting point:

```
slippage = max(half-spread, k × σ_minute × √(Q / V_minute))
```

Where:
- `half-spread` = half the displayed bid-ask
- `σ_minute` = volatility over the order's expected execution interval
- `Q` = order size
- `V_minute` = volume in the execution interval
- `k` ≈ 0.3-0.7

The first term captures the minimum: even a small order pays half the spread. The second term captures size-related slippage that scales with the local liquidity-to-volatility relationship.

This is *separate* from the impact model. Slippage and impact are conceptually distinct:
- **Impact** is the price movement you cause
- **Slippage** is the gap between the price you wanted and the price you got, after subtracting the impact

In practice they overlap and many backtests lump them together. The cleaner approach is to model them separately and add the costs.

## The Three Slippage Models in Backtests

Almost every backtest slippage assumption is one of three families, in increasing order of fidelity. Choosing the right one is a function of how much the strategy's own size and trade frequency matter.

| Model | Formula (per trade) | Inputs needed | Captures | Misses | Good for |
|---|---|---|---|---|---|
| **Fixed / per-trade** | `cost = c` (constant bps, e.g. 5 bps) | One number | A blunt friction floor | Size, vol, liquidity, direction | First-pass sanity check; low-turnover, small-size strategies |
| **Spread-based** | `cost = f × half_spread` | [[bid-ask-spread\|bid-ask]] history | Liquidity differences across names/time | Own-trade impact, adverse selection | Liquid single-name equity, daily-bar strategies |
| **Impact (size-aware)** | `cost = max(half_spread, k·σ·√(Q/V)) + impact` | Spread, σ, ADV, order size | Size scaling, the square-root impact law | Sub-second microstructure | Large size, intraday, anything where `Q/V` is non-trivial |

### 1. Fixed (constant) slippage
Add a flat `c` bps to every fill. Trivial to implement and a reasonable *floor* — but it lies about everything that varies. A constant cost can make a high-turnover strategy look profitable (the constant is too low for thousands of trades) while penalising a low-turnover one (the constant is too high for a handful of large, patient orders). Use it only to answer "does this survive *any* friction at all?"

### 2. Spread-based slippage
Charge a fraction of the prevailing [[bid-ask-spread]] — typically the full half-spread for a marketable order, less for a passive one. This is the right default for liquid equities traded on daily or hourly bars where your size is small relative to depth. It correctly makes illiquid names and stressed periods (wide spreads) more expensive. It still ignores the price you move yourself, so it understates cost for large orders.

### 3. Impact / size-aware slippage
Layer a [[market-impact-models|market-impact]] term on top of the spread term. The workhorse is the **square-root law**: impact scales with `√(Q/V)` — the order size as a fraction of interval volume — times local volatility. The model at the top of this page is exactly this form. This is mandatory once `Q` is an appreciable fraction of `V`, and it is the only family that correctly punishes a strategy for assuming it can trade unlimited size at the touch.

### How they relate
The three are nested, not competing: fixed ⊂ spread-based ⊂ impact-aware. A complete cost model is `spread cost + impact + slippage`, and the choice of family is really a choice of *which terms you can afford to set to a constant*. See [[transaction-cost-modeling]] for the full additive decomposition and [[market-impact-models]] for the impact term in detail.

## Realistic Slippage by Strategy Type

### Market-on-close orders (MOC)
Slippage is essentially zero relative to the closing price (you participate in the closing auction at the official close). The "cost" is being unable to trade at any other time.

### Limit orders
Slippage is *negative* — you sometimes get price improvement. But the cost is fill probability: many limit orders never fill, and the unfilled ones represent missed opportunities.

### Marketable limit orders
Slippage is roughly half-spread plus a small adverse-selection cost (1-3 bps for liquid stocks).

### Pure market orders
Slippage is the full spread plus impact. Often 2-3x more expensive than marketable limit orders.

### Algorithmic orders (TWAP, VWAP, IS)
Slippage depends on the algorithm and market conditions. A TWAP order in a high-vol environment can suffer severe slippage from price drift; the same order in a calm market can outperform the arrival price.

### HFT-style aggressive
Slippage varies with sub-second market dynamics. Modeling requires nanosecond-level data.

## Empirical Slippage Calibration

The right way to estimate slippage is from your own execution data:

1. For each historical trade, record:
   - Decision time and decision price (mid at the moment the strategy fired)
   - Order arrival time
   - Average fill price
2. Compute slippage = (fill - decision) × side
3. Group by trade size, time of day, volatility regime
4. Fit a model that predicts slippage from these features

The result is a calibrated, strategy-specific slippage estimator. Plug it into your backtest in place of the generic formula.

For new strategies without execution history, use a conservative generic estimate (5-10 bps for most equity strategies, 10-30 bps for crypto, 1-3 bps for liquid futures). Refine after the first paper-trading period.

## The Slippage-Impact Decomposition

A useful framework for distinguishing the two:

```
total execution cost = spread cost + impact + slippage

spread cost   = how much of the spread you crossed
impact        = how much you moved the price by your own trading
slippage      = everything else (latency, adverse selection, routing)
```

For a $1M trade in AAPL via market order:
- Spread cost ≈ 0.5 bps (half of a 1 bp spread)
- Impact ≈ 0.5 bps (small relative to AAPL's huge ADV)
- Slippage ≈ 1-2 bps (latency, adverse selection)
- **Total ≈ 2-3 bps**

For a $10M trade in a small-cap stock via TWAP over 30 minutes:
- Spread cost ≈ 5 bps
- Impact ≈ 15 bps
- Slippage ≈ 5 bps (drift over the execution window)
- **Total ≈ 25 bps**

The relative weights of spread, impact, and slippage shift with strategy and venue. A model that ignores any one of them will systematically misestimate cost.

## Common Modeling Mistakes

### 1. Constant slippage
Adding a flat 5 bps per trade ignores that slippage scales with size, volatility, and market conditions. Better than nothing but only by a hair.

### 2. No slippage at all
The default in many backtest libraries. Wildly optimistic. Any backtest claiming "fills at the close" with no slippage is overstating returns by 10-50 bps per round-trip depending on the strategy.

### 3. Slippage proportional to spread only
Ignores impact and adverse selection. Underestimates cost for large trades and high-frequency strategies.

### 4. Same slippage for buy and sell
Slippage is asymmetric in markets with directional flow imbalance (e.g., crypto in a bull market: buys slip more than sells).

### 5. No slippage on limit orders
Limit orders that "don't fill" are also a cost — the missed opportunity cost. A complete model accounts for fill probability.

## When Slippage Is the Dominant Cost

For HFT and intraday strategies with thousands of trades per day, slippage usually dominates spread and impact combined. A 1 bp slippage per round-trip × 5,000 round-trips per day = 5,000 bps per day = 1,250% per year of friction. The strategy's gross edge has to clear that bar before it makes any money.

Strategies with this profile cannot be researched without realistic slippage modeling. Anything else is fiction.

## Which Model for Which Strategy

| Strategy profile | Turnover | Size vs ADV | Recommended model | Conservative default if uncalibrated |
|---|---|---|---|---|
| Long-term value / buy-and-hold | Very low | Tiny | Fixed | 5 bps round-trip |
| Daily-rebalance equity factor | Medium | Small | Spread-based | 5-10 bps |
| Liquid futures trend | Low-medium | Tiny | Spread-based | 1-3 bps |
| Crypto swing | Medium | Variable | Spread-based + asymmetry | 10-30 bps |
| Large-AUM portfolio rebalance | Low | Large | Impact-aware (√-law) | 15-50 bps, size-dependent |
| Intraday / stat-arb | High | Small-medium | Impact-aware + time-of-day | Calibrate from fills |
| HFT / sub-second | Extreme | Small | Empirical, nanosecond data | Cannot proxy — measure directly |

The rule of thumb: the higher up the turnover or size column you sit, the further down the [model fidelity ladder](#the-three-slippage-models-in-backtests) you must go. A pennies-per-trade edge run thousands of times a day cannot be researched with a constant.

## Worked Example: Same Edge, Three Models

A daily mean-reversion strategy on mid-cap equities shows a gross Sharpe of 1.4 and ~250% annual turnover before costs. Watch what each slippage model does to it (numbers illustrative):

| Model | Assumed cost / round-trip | Annual cost drag | Net Sharpe | Verdict |
|---|---|---|---|---|
| No slippage | 0 bps | 0% | 1.4 | Fiction — looks great |
| Fixed | 5 bps | ~12% | ~0.9 | Survives, but optimistic |
| Spread-based | ~9 bps (wider in stressed months) | ~22% | ~0.5 | Marginal |
| Impact-aware | ~9 bps body, **30+ bps in stress** | ~30%+ | ~0.2 | Edge mostly eaten in the months that matter |

The strategy is *real* under the no-slippage and fixed models and *barely viable* under the realistic ones — and crucially, the impact-aware model concentrates the extra cost in exactly the volatile, wide-spread months when the signal also fires most. A backtest that passes under "no slippage" and fails under spread-based modelling was never a strategy; it was a measurement of the cost model. This is a primary channel of [[overfitting]] and a reason backtested Sharpes need to be [[deflated-sharpe-ratio|deflated]].

## Sources

- Perold (1988) "The Implementation Shortfall: Paper Versus Reality" — *Journal of Portfolio Management* (the foundational paper)
- [[book-trading-and-exchanges]] — Harris on slippage and adverse selection
- Almgren & Chriss (2001) on impact (overlaps with slippage in their treatment)

## Related

- [[backtesting-overview]]
- [[transaction-cost-modeling]]
- [[market-impact-models]]
- [[execution-algorithms]]
- [[implementation-shortfall]]
- [[bid-ask-spread]]
- [[adverse-selection]]
