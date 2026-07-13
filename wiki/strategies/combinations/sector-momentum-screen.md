---
title: Sector Rotation + Momentum Stock Screening
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, meta-strategy, sector-rotation, momentum, stock-screening, relative-strength, CANSLIM]
strategy_type: hybrid
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: [risk-on-risk-off-framework, multi-strategy-portfolio, dca-technical-hybrid]
---

# Sector Rotation + Momentum Stock Screening

## Overview

This combination first uses [[sector-rotation]] to identify which sectors are currently in favor based on the macro cycle and [[relative-strength]], then applies [[momentum-screening]] within those sectors to select the best individual stocks. The two-layer approach ensures you are fishing in the right pond (sector) with the right bait (momentum stock selection). Buying momentum stocks in the wrong sector underperforms. Buying the right sector with random stock picks underperforms. Together: **right sector + strongest stock = systematic outperformance**.

## The Synergy

Academic research (Moskowitz and Grinblatt, 1999) demonstrated that a large portion of individual stock momentum is actually driven by industry momentum. A stock rising 40% in a sector rising 30% has only 10% of alpha -- the rest is sector beta. Conversely, the strongest stock in a weak sector often gets dragged down by sector headwinds.

The synergy works because sectors move in predictable cycles tied to the [[business-cycle]]. Technology and consumer discretionary lead in early expansion. Energy and materials lead in late expansion. Utilities and healthcare lead in contraction. By identifying the cycle phase first, you eliminate sectors swimming against the macro current, then pick the strongest swimmers within favorable sectors.

## Component Strategies

**[[sector-rotation]] provides:**
- Macro cycle identification using [[economic-indicators]]
- Ranking of 11 [[gics-sectors]] by 3-month [[relative-strength]]
- Elimination of sectors in structural downtrends
- Alignment with [[fed-policy]], [[yield-curve]], and [[ism-pmi]] signals

**[[momentum-screening]] provides:**
- Individual stock ranking by 6-month and 12-month price momentum
- [[earnings-revision]] momentum -- analyst upgrades as a catalyst filter
- [[relative-strength-rating]] vs the broader market (a la [[ibd]])
- Volume confirmation -- strong moves on expanding [[volume]]

## Implementation

**Step 1: Rank Sectors Monthly**

Rank all 11 GICS sectors by 3-month total return relative to the S&P 500. Use sector ETFs as proxies: XLK (Tech), XLV (Healthcare), XLF (Financials), XLY (Cons. Disc.), XLP (Cons. Staples), XLE (Energy), XLI (Industrials), XLB (Materials), XLRE (Real Estate), XLU (Utilities), XLC (Comms). Select the **top 3 sectors** by relative strength as your investable universe for the month.

**Step 2: Screen Stocks Within Top Sectors**

Within each of the 3 selected sectors, apply a momentum screen:

| Criterion | Threshold | Weight |
|-----------|----------|--------|
| 6-month price return | Top quartile in sector | 30% |
| 3-month [[earnings-revision]] | Positive net revisions | 25% |
| [[relative-strength]] vs sector | RS rating > 80 | 25% |
| Volume trend | 50-day avg volume rising | 10% |
| Above [[200-day-ma]] | Price > 200-day SMA | 10% (binary) |

Rank stocks by composite score. Select the **top 5 stocks per sector** (15 total positions).

**Step 3: Position Sizing and Entry**

Equal-weight within each sector tier. Top sector gets 40% of capital, second gets 35%, third gets 25%. Within each sector allocation, divide equally among 5 stocks.

Enter on the first trading day of the month. Use limit orders at the previous day's close to avoid overpaying on gap-ups.

**Step 4: Monthly Rebalance**

On the first Friday of each month:
- Re-rank sectors. If a sector drops out of the top 3, sell all positions in it
- Within retained sectors, re-rank stocks. Replace any that fall out of the top 5
- Add new sectors/stocks that have entered the top ranks
- Allow a **one-month grace period** before selling a position that just dropped out (avoids whipsawing on borderline names)

## Example Setup

**March 2026 sector rankings (hypothetical):**

Top 3 sectors: Technology (XLK +12% 3-mo RS), Financials (XLF +8%), Industrials (XLI +6%)

Technology picks (8% each, 40% total):
- NVDA, AVGO, MSFT, CRM, NOW

Financials picks (7% each, 35% total):
- GS, JPM, AXP, COIN, HOOD

Industrials picks (5% each, 25% total):
- GE, CAT, URI, PWR, EME

Total: 15 positions across 3 sectors, fully invested.

## When It Excels / When It Fails

**Excels when:**
- Clear sector leadership exists (as in 2023 tech or 2022 energy)
- The [[business-cycle]] is in a definable phase (early, mid, or late expansion)
- Momentum persists for multiple months within sectors
- Combined with a [[risk-on-risk-off-framework]] that reduces exposure in bear markets

**Fails when:**
- Sector leadership rotates rapidly (every 2-3 weeks) causing whipsaws
- Broad market sells off indiscriminately -- all sectors drop together
- Momentum reversal events (factor crashes like March 2020) punish the strategy
- Concentrated sector bets magnify drawdowns if the selected sector reverses sharply

## Real-World Usage

[[william-oneil]]'s [[canslim]] methodology is fundamentally this combination -- the "L" (Leader/Laggard) and "I" (Institutional Sponsorship) criteria map directly to sector rotation + momentum screening. [[ibd]] (Investor's Business Daily) industry group rankings have tracked sector and stock momentum since the 1960s.

Modern implementations include [[dorsey-wright]] relative strength ETF models used by financial advisors, and [[alpha-architect]]'s quantitative momentum funds. The [[fidelity-select]] sector fund family was originally designed for this rotational approach. Most [[quantitative-equity]] hedge funds run some variant of sector-aware momentum as a core signal, often combined with [[value-factors]] and [[quality-factors]] for a multi-factor approach.
