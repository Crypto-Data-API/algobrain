---
title: "Volatility Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [options, volatility, arbitrage, implied-volatility, realized-volatility, variance, vol-trading]
aliases: ["Vol Arb", "Volatility Trading", "IV vs RV Trading"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks, crypto]
complexity: advanced
backtest_status: untested
related: ["[[gamma-scalping]]", "[[straddle-strangle]]", "[[iron-condor]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[vix]]", "[[vega]]", "[[option-volatility-and-pricing]]"]
---

# Volatility Arbitrage

## Overview

Volatility arbitrage is the practice of trading the spread between [[implied-volatility]] (IV) -- what the options market predicts volatility will be -- and [[realized-volatility]] (RV) -- what actually occurs. The core observation driving this strategy is that implied volatility is systematically mispriced: it tends to overestimate future realized volatility (the [[volatility-risk-premium]]), creating a persistent edge for sellers, while occasionally underpricing it before extreme events, creating opportunities for buyers (Source: [[book-option-volatility-and-pricing]]).

Vol arb practitioners sell options (or [[variance-swap]]s) when IV is significantly higher than expected RV, and buy options when IV is unusually low relative to anticipated RV. The strategy is typically implemented as delta-neutral, isolating the pure volatility bet from directional exposure. This is the domain of hedge funds, prop desks, and sophisticated retail traders who treat volatility itself as a tradable asset class.

## Rules

### Entry
1. **Measure the IV-RV spread:** Compare current [[implied-volatility]] (e.g., 30-day ATM IV) to recent [[realized-volatility]] (e.g., 20-day historical vol). A spread of +5 vol points or more suggests options are expensive.
2. **Sell volatility when IV >> RV:** Sell [[straddle-strangle|straddles]], [[iron-condor]]s, or variance swaps. Delta-hedge to remain market-neutral.
3. **Buy volatility when IV << RV:** Buy straddles or strangles when options are cheap relative to actual market movement. This is rarer but occurs during complacent markets before shocks.
4. **Use IV rank/percentile:** Enter short vol trades when IV rank is above 50 (ideally above 70). Enter long vol trades when IV rank is below 20.
5. **Sector/asset selection:** Focus on liquid underlyings with well-understood vol dynamics -- SPY, QQQ, individual mega-caps, BTC, ETH.

### Exit
1. **Short vol trades:** Close when IV converges toward RV, or when 50-75% of premium is captured. Stop-loss if realized vol spikes above implied (the trade thesis is broken).
2. **Long vol trades:** Close quickly after the vol expansion event. Do not hold long options hoping for further moves -- [[theta]] decay is the enemy.
3. **Time-based exit:** Close positions at 50% of the DTE to avoid gamma risk near expiration.
4. **Hedge continuously:** Maintain delta-neutral positioning through the life of the trade. Use [[gamma-scalping]] techniques for long vol positions.

### Position Sizing
Allocate 1-3% of account risk per vol arb trade. Short volatility trades have tail risk -- size conservatively. Diversify across multiple underlyings and expirations to smooth the equity curve.

## Indicators Used
- [[implied-volatility]] (IV) -- the market's forecast of future vol, derived from option prices
- [[realized-volatility]] (RV) / historical volatility -- the actual observed volatility over a lookback period
- [[vix]] -- the market's "fear gauge," represents 30-day implied vol on the S&P 500
- IV rank / IV percentile -- contextualizes current IV relative to the past 52 weeks
- [[vega]] -- the position's sensitivity to changes in implied volatility
- Variance ratio -- IV^2 / RV^2 provides a cleaner signal than raw vol difference
- [[volatility-cone]] -- visualizes the term structure of realized vol to identify cheap/expensive expirations

## Example Trade
**Asset:** AMZN trading at $190. 30-day IV: 38%. 20-day realized vol: 25%. IV rank: 78th percentile.
1. **Thesis:** IV is 13 vol points above RV. Options are expensive. Sell volatility.
2. **Sell 1 AMZN $190 straddle**, 30 DTE, for $16.00 ($1,600). Delta-hedge to neutral by trading shares.
3. **Over the next 25 days:** AMZN moves within a $180-$198 range. Realized vol comes in at 27% -- below the 38% implied.
4. **Gamma scalping (in reverse):** As a short gamma position, hedging costs eat into profits, but the total hedging cost is less than the premium collected because RV < IV.
5. **Close at 5 DTE:** Buy back the straddle for $5.50. Net profit: $16.00 - $5.50 - $2.00 (hedging costs) = **$8.50 ($850 per straddle).**
6. The trade was profitable because realized volatility (27%) was below implied volatility (38%).

## Performance Characteristics
- **Win Rate:** 55-70% for systematic short vol strategies, due to the persistent [[volatility-risk-premium]].
- **Profit Factor:** 1.3-2.0 in normal environments. Catastrophic losses are possible in tail events (e.g., COVID crash, 2008 GFC) if not properly risk-managed.
- **Best Market Conditions:** Post-spike environments where IV is elevated but the shock has passed. Earnings season across a diversified basket.
- **Worst Market Conditions:** Black swan events, sustained volatility regimes, and markets where realized vol consistently exceeds implied (rare but devastating).

## Advantages
- **Exploits a proven risk premium:** The tendency of IV to exceed RV is one of the most documented anomalies in finance (Source: [[book-option-volatility-and-pricing]])
- **Market-neutral:** Profits do not depend on price direction, only on the IV-RV relationship
- **Scalable:** Can be applied across dozens of underlyings simultaneously for diversification
- **Systematic:** Lends itself to quantitative, rules-based implementation with clear entry/exit criteria

## Disadvantages
- **Tail risk on short vol:** Selling volatility is "picking up pennies in front of a steamroller" -- small consistent gains punctuated by rare but catastrophic losses
- **Requires sophisticated analytics:** Measuring IV, RV, forecasting vol, and managing Greeks demands advanced tools and knowledge
- **High transaction costs:** Continuous delta-hedging generates significant commissions and slippage
- **Model risk:** Vol forecasting models can be wrong, especially during regime changes
- **Capital-intensive:** Naked short options require substantial margin; defined-risk alternatives reduce margin but also reduce returns

## See Also
- [[gamma-scalping]] -- the hedging technique used to maintain delta neutrality in vol arb trades
- [[straddle-strangle]] -- the primary instrument for expressing long volatility bets
- [[iron-condor]] -- a defined-risk short volatility vehicle
- [[implied-volatility]] -- one side of the IV-RV spread
- [[realized-volatility]] -- the other side of the spread
- [[vix]] -- the benchmark index for S&P 500 implied volatility
- [[volatility-risk-premium]] -- the structural edge underpinning short vol strategies

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg's treatment of the implied vs. realized volatility relationship, the volatility risk premium, and delta-neutral volatility trading is the foundational reference for this strategy
