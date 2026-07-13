---
title: "Earnings Momentum"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [earnings, momentum, fundamental-analysis, PEAD, EPS-surprise, analyst-revisions]
aliases: ["Post-Earnings Announcement Drift", "PEAD Strategy", "Earnings Surprise Trading"]
strategy_type: fundamental
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[growth-investing-strategy]]", "[[news-trading]]", "[[event-driven-trading]]", "[[momentum]]", "[[relative-strength]]", "[[book-how-to-make-money-in-stocks]]", "[[book-one-up-on-wall-street]]"]
---

# Earnings Momentum

## Overview

Earnings Momentum exploits one of the most well-documented anomalies in academic finance: **Post-Earnings Announcement Drift (PEAD)**. When a company reports earnings that significantly beat or miss analyst estimates, the stock price does not instantly adjust to the new information. Instead, it continues drifting in the direction of the surprise for 30-60 days after the announcement. This violates the [[efficient-market-hypothesis]] and has persisted since first documented by Ball & Brown in 1968.

The strategy combines two signals: the **EPS surprise** (actual vs. consensus estimate) and **analyst revision momentum** (are estimates for future quarters being revised upward or downward?). O'Neil's CANSLIM system places current and annual earnings acceleration at the core of growth stock selection (Source: [[book-how-to-make-money-in-stocks]]). Stocks with positive surprises AND upward revisions have the strongest drift. The effect is strongest in small and mid-cap stocks where analyst coverage is thinner and information disseminates more slowly.

## Rules

### Entry
1. **Screen for EPS surprise:** After earnings release, identify stocks that beat consensus EPS estimates by at least 5-10%. Use data from providers like Estimize, Zacks, or Bloomberg.
2. **Confirm revision momentum:** Check that analyst estimates for the next 1-2 quarters are being revised upward. At least 2-3 analysts raising estimates is ideal.
3. **Enter within 1-3 days** of the earnings report. Buy on the first pullback or consolidation after the initial gap-up. Avoid chasing if the stock has already moved 15%+ from the pre-earnings close.
4. **Volume confirmation:** Earnings day [[volume]] should be at least 2x the 20-day average, signaling institutional participation.

### Exit
1. **Time-based exit:** Close the position 30-60 days after earnings. The PEAD effect weakens significantly beyond this window.
2. **Next earnings approach:** Exit at least 5-7 days before the next quarterly earnings to avoid binary event risk.
3. **Stop-loss:** Place a stop 7-10% below entry. If the drift reverses, the thesis is broken.
4. **Negative revision:** Exit immediately if analysts begin revising estimates downward.

### Position Sizing
Risk 1-2% of account per trade. Diversify across 5-10 names with recent positive surprises to reduce single-stock risk.

## Indicators Used
- EPS surprise percentage (actual vs. consensus)
- Analyst revision breadth (number of upward vs. downward revisions)
- [[volume]] surge on earnings day
- [[relative-strength]] vs. sector and market
- Revenue surprise (supplementary confirmation)

## Example Trade
**Asset:** NVDA after Q4 earnings report
1. NVDA reports EPS of $5.16 vs. consensus of $4.60 -- an 12.2% beat. Revenue also beats by 8%. The stock gaps up 9% on 4x average volume.
2. Over the next 2 days, NVDA pulls back 3% from the gap-up high. Enter long at $725. Stop-loss at $660 (9% risk).
3. Over the following 6 weeks, 14 analysts raise their forward estimates. The stock drifts steadily higher.
4. Exit at day 50 post-earnings at $815.
5. **Result:** +$90 per share (12.4% gain). The PEAD effect played out as expected with continuous upward drift supported by rising estimates.

## Performance Characteristics
- **Win Rate:** 55-65%. The drift is statistically significant but not guaranteed for every stock.
- **Profit Factor:** 1.8-2.5. Winners tend to drift steadily; losers are cut quickly by stops.
- **Best Market Conditions:** Bull markets with broad earnings growth. The effect is strongest in sectors with high analyst coverage dispersion.
- **Worst Market Conditions:** Bear markets or periods of macro uncertainty where systematic selling overwhelms individual earnings quality.
- **Annual Turnover:** High. Each earnings season (4x per year) generates a fresh batch of candidates.

## Advantages
- Backed by decades of academic research -- one of the most robust anomalies in finance. Lynch emphasized that earnings growth is ultimately what drives stock prices (Source: [[book-one-up-on-wall-street]])
- Clear, objective entry criteria based on quantifiable data (EPS surprise, revisions)
- Works across market caps, though the edge is larger in less-covered names
- Natural [[catalyst]]-driven approach: you know exactly why you are in the trade

## Disadvantages
- Requires access to real-time earnings data and analyst revision feeds, which can be expensive
- The initial gap-up after earnings can make the entry feel uncomfortable (buying after a big move)
- Some academic evidence suggests the PEAD effect has weakened as more participants exploit it
- Concentrated in the weeks around earnings season, leaving idle capital during off-periods
- Single-stock risk: even strong beats can sell off if forward guidance disappoints

## Sources

- [[book-how-to-make-money-in-stocks]] — O'Neil's CANSLIM system, which places earnings acceleration at the center of growth stock selection
- [[book-one-up-on-wall-street]] — Lynch's emphasis on earnings growth as the primary driver of stock prices

## See Also
- [[growth-investing-strategy]] -- longer-term approach that also values earnings growth
- [[news-trading]] -- broader event-driven trading that includes earnings
- [[event-driven-trading]] -- framework for trading around corporate catalysts
- [[momentum]] -- the broader concept underlying earnings drift
- [[relative-strength]] -- ranking stocks by price performance complements earnings signals
