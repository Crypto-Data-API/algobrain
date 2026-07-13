---
title: "Momentum-Value Combination"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, meta-strategy, factor-investing, momentum, value, quantitative]
strategy_type: hybrid
timeframe: medium-term (monthly rebalancing)
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[momentum-investing]]", "[[factor-investing]]", "[[relative-strength]]"]
---

# Momentum-Value Combination

## Overview

Value and momentum are two of the most well-documented return factors in financial history. value-investing — buying cheap assets based on low price-to-earnings-ratio or price-to-book-ratio — has generated excess returns over nearly every multi-decade period studied, across virtually every market in the world. [[momentum-investing]] — buying recent winners and selling recent losers based on 6-12 month price performance — has done the same, with comparable magnitude.

Here is what makes combining them extraordinary: **value and momentum are negatively correlated.** When value has a terrible year, momentum often has a great one. When momentum crashes, value tends to hold up. This negative correlation is not occasional — it has been consistent across decades and geographies. Combining two independently profitable factors that hedge each other's drawdowns is as close to a free lunch as investing gets.

## The Synergy

**Drawdown offset.** Value investing's worst periods (late 1990s tech bubble, 2018-2020 growth dominance) coincided with momentum's best periods (momentum rode the tech winners higher). Conversely, momentum's worst events (sharp reversals like March 2009, November 2020 vaccine rotation) coincided with value's best periods (cheap stocks surged during these reversals). A 50/50 blend dramatically smooths the equity curve.

**Return enhancement through intersection.** The most powerful implementation is not a simple 50/50 split but a composite: buy stocks that are BOTH cheap (value) AND have strong recent performance (momentum). These "value stocks with momentum" outperform either factor alone because they represent a fundamentally cheap asset where the market has started to recognize the cheapness. You are buying what is cheap AND what is already moving in the right direction.

**Behavioral explanation.** Value works because investors overreact to bad news and sell quality companies too cheaply. Momentum works because investors underreact to good news and are slow to bid up improving companies. The combination captures both behavioral errors: you buy the stocks that were oversold (value) but where the overselling has stopped and reversal has begun (momentum).

## Component Strategies

| Component | Signal | What It Captures |
|-----------|--------|-----------------|
| value-investing | Low price-to-earnings-ratio, low price-to-book-ratio, high earnings-yield | Cheap stocks likely to mean-revert upward |
| [[momentum-investing]] | Strong 6-12 month [[relative-strength]], positive trend | Stocks with established upward trajectory |
| Composite rank | Value rank + Momentum rank | Cheap stocks that are also moving up |

## Implementation

**Approach 1: Composite Ranking (Quant Implementation)**

This is the purest form. Monthly process:

1. **Universe selection.** Start with the largest 1000 US stocks (or an equivalent universe). Exclude financial stocks and REITs if desired (their value metrics are distorted).

2. **Value rank.** For each stock, compute a composite value score from:
   - Enterprise value to EBITDA (lower is cheaper)
   Rank all stocks from 1 (cheapest) to 1000 (most expensive).

3. **Momentum rank.** For each stock, compute:
   - 12-month total return, excluding the most recent month (the standard academic momentum signal — the last month is excluded because of [[short-term-reversal]] effects)
   Rank all stocks from 1 (strongest momentum) to 1000 (weakest).

4. **Composite rank.** Average the value rank and momentum rank. Buy the top 50 stocks (top 5%) by composite score. Equal-weight the portfolio.

5. **Rebalance monthly.** Sell stocks that drop out of the top 100. Buy stocks that enter the top 50. This creates natural turnover that refreshes both factors.

**Approach 2: Factor ETF Blend (Simple Implementation)**

For investors who cannot run quantitative screens:

- 50% in a value ETF: VLUE (MSCI USA Value), VTV (Vanguard Value), or QVAL (quantitative value)
- 50% in a momentum ETF: MTUM (MSCI USA Momentum), QMOM (quantitative momentum)
- Rebalance semi-annually

This is simpler but less optimal — you hold cheap stocks without momentum and momentum stocks without value. The composite ranking approach is strictly superior because it requires both factors in every holding.

**Approach 3: Value Selection, Momentum Timing**

A hybrid for discretionary investors:

1. Screen for value: P/E below 15, P/B below 2, positive earnings, reasonable debt.
2. From the value list, only buy those where 6-month [[relative-strength]] is above 50th percentile (stock is outperforming at least half the market).
3. Entry: buy when the stock breaks above its 50-day [[moving-averages]] (confirms momentum is intact).
4. Exit: sell when 6-month relative strength drops below 30th percentile (momentum is dying).

## Example Setup

**Composite ranking example — January 2026 rebalance:**

Screen the Russell 1000. Compute value ranks (P/E, P/B, EV/EBITDA) and momentum ranks (11-month return ex last month).

Top composite picks might include:
- A healthcare stock trading at 11x earnings after a sector selloff, but up 28% over the past year as fundamentals improved
- An industrial company at 0.9x book value with 35% price gain driven by infrastructure spending tailwinds
- An energy stock at 7x earnings with strong momentum from rising commodity prices

Each of these is cheap (value) AND already working (momentum). The intersection is the sweet spot.

Equal-weight 50 such stocks at 2% each. Rebalance monthly.

## When It Excels

- **Normal market environments** where both factors are compensated over medium-term horizons. Historically, this is most of the time.
- **After major market dislocations** — value stocks that start showing momentum after a crash have been among the best-performing assets in recovery periods (March 2009, March 2020).
- **Across international markets** — the value-momentum combination has been documented in Europe, Japan, emerging markets, and even commodity futures. It is among the most globally robust factor combinations.
- **For systematic, rules-based investors** who can execute monthly rebalancing without emotional interference.

## When It Fails

- **Prolonged factor crashes.** While value and momentum are negatively correlated on average, there are brief periods where both underperform simultaneously (late 2008 saw both factors struggle). These periods are rare but painful.
- **When a single mega-trend dominates** — if the market is driven entirely by 5-7 mega-cap tech stocks (as in 2023-2024), factor strategies that diversify across 50 stocks may lag the cap-weighted index even while generating positive absolute returns.
- **High turnover costs.** Monthly rebalancing of 50 stocks generates significant transaction costs and short-term capital gains taxes. This is best implemented in tax-advantaged accounts or with tax-loss harvesting.
- **Crowding risk.** As factor investing has become mainstream, crowded trades in popular value and momentum stocks can reduce forward returns or cause sharper reversals.

## Real-World Usage

**Cliff Asness and AQR Capital Management** have published the most influential research on the value-momentum combination. Their 2013 paper "Value and Momentum Everywhere" demonstrated that combining these factors improved risk-adjusted returns in every asset class tested — US stocks, international stocks, bonds, currencies, and commodities. AQR runs billions of dollars using factor combination strategies.

**Dimensional Fund Advisors (DFA)** builds portfolios that tilt toward value, profitability, and size factors, with implementation that considers momentum for trade timing (they avoid buying value stocks with negative momentum, effectively incorporating the composite approach).

**Vanguard and BlackRock** factor ETFs allow retail investors to access these strategies cheaply, though the single-factor versions (VLUE, MTUM) are less powerful than the composite intersection.

**Academic foundation:** Fama and French documented the value factor. Jegadeesh and Titman documented momentum. Asness showed the combination. This is among the most researched and validated strategies in all of finance.

**See also:** [[factor-investing]], value-investing, [[momentum-investing]], [[relative-strength]], [[quantitative-strategies]], [[portfolio-rebalancing]]
