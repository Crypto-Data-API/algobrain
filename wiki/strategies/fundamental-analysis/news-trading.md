---
title: "News Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [news-trading, event-driven, NFP, CPI, FOMC, earnings, high-frequency, volatility]
aliases: ["News-Based Trading", "Economic Calendar Trading", "Headline Trading"]
strategy_type: hybrid
timeframe: intraday
markets: [stocks, forex, crypto]
complexity: advanced
backtest_status: untested
related: ["[[event-driven-trading]]", "[[earnings-momentum]]", "[[merger-arbitrage]]", "[[scalping]]", "[[volatility]]", "[[social-arbitrage]]", "[[sentiment-trading]]"]
---

# News Trading

## Overview

News Trading is a high-intensity strategy that capitalizes on the sharp price movements triggered by major news releases: **economic data** (Non-Farm Payrolls, CPI, GDP, retail sales), **central bank decisions** ([[fomc|FOMC]] rate announcements, ECB meetings), **corporate earnings**, and **geopolitical events**. The premise is that markets are not perfectly efficient in the seconds and minutes after new information arrives -- prices overshoot, undershoot, and whipsaw before settling into a new equilibrium.

There are two primary approaches: **momentum trading** (enter in the direction of the initial move and ride the continuation) and **fade trading** (wait for the overreaction and trade the reversal). The momentum approach requires lightning-fast execution and works best when data deviates significantly from consensus. The fade approach requires patience and works when the initial spike is disproportionate to the actual news impact. Both approaches demand strict [[risk-management]] because [[volatility]] during news releases can be 5-10x normal levels, spreads widen dramatically, and [[slippage]] can be severe.

## Rules

### Entry (Momentum Approach)
1. **Identify high-impact events** on the economic calendar (forexfactory.com, Bloomberg). Focus on events rated "red" or "high impact": NFP, CPI, FOMC, earnings for mega-cap stocks.
2. **Wait for the release.** Do not enter before the number hits. Within 1-5 seconds of the release, identify the direction of the surprise (actual vs. forecast).
3. **Enter in the direction of the surprise** if the deviation is significant (e.g., NFP misses by 100K+, CPI beats by 0.3%+). Use market orders for speed.
4. **Target the follow-through:** After the initial spike, there is typically a 15-60 minute follow-through move as algorithms and institutional traders reposition.

### Entry (Fade Approach)
1. **Let the initial spike complete.** Wait 5-15 minutes after the release for the first wave of volatility to subside.
2. **Enter against the spike** if the move is disproportionate to the data surprise. For example, a minor CPI beat causing a 2% equity sell-off may be an overreaction.
3. Use [[support-and-resistance]] levels from before the news event as targets for the fade.

### Exit
1. **Momentum exit:** Take profits within 30-90 minutes. Most news-driven moves exhaust within the first hour.
2. **Fade exit:** Target a 50-75% retracement of the initial spike. Exit within the same trading session.
3. **Stop-loss:** Tight stops are essential. Risk no more than 1% of account. For momentum trades, stop below the pre-news price. For fades, stop beyond the spike extreme.

### Position Sizing
Small positions (0.5-1% risk per trade) due to extreme [[volatility]] and [[slippage]] risk. Reduce size during the most volatile events (FOMC, NFP).

## Indicators Used
- Economic calendar with consensus estimates and prior readings
- [[volatility]] indicators: [[atr]], [[bollinger-bands]] to gauge normal vs. news-driven ranges
- [[volume]] profile -- massive volume spikes confirm institutional participation
- [[vwap]] -- intraday anchor for determining if the move is sustainable
- Bid-ask spread monitor -- wider spreads signal dangerous liquidity conditions
- [[support-and-resistance]] -- pre-news key levels for targets and stops

## Example Trade
**Event:** U.S. CPI release, consensus +0.2% m/m, actual +0.5% m/m (significant upside surprise)
1. At 8:30 AM ET, CPI prints +0.5% vs. +0.2% expected. Hot inflation = higher rates = bearish for equities, bullish for USD.
2. S&P 500 futures (ES) drop 30 points in 10 seconds from 5,200 to 5,170. EUR/USD drops 80 pips in the same period.
3. **Momentum trade:** Short ES at 5,175 (entering on the first micro-pullback). Stop at 5,205 (above pre-release). Target 5,120.
4. Over the next 45 minutes, ES continues to drift lower as bond yields spike. Hit target at 5,120.
5. **Result:** +55 points on ES ($2,750 per contract). Total time in trade: 45 minutes. Risk was 30 points ($1,500) for a 1.8:1 reward-to-risk ratio.

## Performance Characteristics
- **Win Rate:** 45-55% for momentum approach, 50-60% for fade approach (fades have higher win rate but smaller average wins).
- **Profit Factor:** 1.5-2.5. High variance -- some news events produce enormous moves, others fizzle.
- **Best Market Conditions:** When actual data deviates significantly from consensus. Low-[[volatility]] environments prior to the release (compressed positioning unwinds sharply).
- **Worst Market Conditions:** When the data matches consensus (no surprise = no move), or when conflicting signals emerge (e.g., hot headline CPI but cool core CPI). Also dangerous when liquidity is thin (holidays, after-hours).
- **Frequency:** 4-8 tradable events per month for major economic data. Daily opportunities if including individual stock earnings.

## Advantages
- Very short exposure time reduces overnight and multi-day risk
- Clear, objective triggers (the data either surprises or it does not)
- News-driven moves can be enormous, offering outsized reward potential
- Works across multiple asset classes simultaneously ([[forex]], [[futures]], [[crypto]])
- Does not require prediction -- you react to information, not forecast it

## Disadvantages
- **Execution risk is extreme:** Spreads widen, orders slip, and platforms can lag during high-impact releases
- Requires professional-grade infrastructure: low-latency feeds, fast broker, and possibly co-located servers to compete with algorithms
- **Whipsaws are common:** The initial spike often reverses within seconds, stopping out momentum traders before the "real" move begins
- Emotional intensity is very high -- decisions must be made in seconds with large sums at risk
- Many events produce no tradable move if data matches consensus, leading to wasted preparation time
- Impossible to backtest accurately due to extreme spread and [[slippage]] conditions during live events

## See Also
- [[event-driven-trading]] -- broader framework for trading catalysts beyond just news
- [[earnings-momentum]] -- earnings-specific news trading with longer holding periods
- [[scalping]] -- similar ultra-short-term approach used in normal market conditions
- [[volatility]] -- understanding volatility regimes is critical for news trading
- [[risk-management]] -- position sizing and stop-loss discipline is paramount
