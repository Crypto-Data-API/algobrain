---
title: "Core-Satellite Portfolio"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, meta-strategy, portfolio-construction, passive-investing, active-management, asset-allocation]
strategy_type: hybrid
timeframe: long-term core, varies for satellites
markets: [crypto, bonds]
complexity: intermediate
backtest_status: untested
related: ["[[index-investing]]", "[[covered-calls]]", "[[wheel-strategy]]", "[[dollar-cost-averaging]]", "[[momentum-investing]]", "[[crypto-allocation]]"]
---

# Core-Satellite Portfolio

## Overview

The core-satellite portfolio is the most practical combination strategy for the majority of investors. The concept: build a passive, low-cost core (60-80% of your portfolio) that captures broad market returns, then surround it with active satellite strategies (20-40%) that attempt to generate alpha. The core is your wealth-building engine. The satellites are your edge-seeking experiments.

This structure acknowledges two uncomfortable truths simultaneously: **most active strategies underperform the index over time** (so a passive core is rational), and **there are genuine edges available to disciplined traders** (so a satellite allocation is worthwhile). By combining both, you guarantee participation in market growth while giving yourself room to outperform.

## The Synergy

**Risk containment with upside optionality.** The passive core provides a floor. Even if every satellite strategy fails completely (returns zero), your 70% core allocation still compounds with the market. Over 20 years at historical average returns, that core alone builds significant wealth. The satellites cannot destroy the portfolio — they can only enhance it.

**Psychological stability.** One of the biggest reasons active traders fail is behavioral — they panic sell, they chase, they overtrade. When you know that the majority of your money is safely compounding in index funds, the emotional pressure on your active trades drops dramatically. You can afford to be patient, take calculated risks, and accept losses on satellite positions without existential portfolio anxiety.

**Diversification across strategy types.** The core captures beta (market return). Satellites can target alpha from completely different sources: [[options-selling]] income, [[crypto-allocation]] asymmetry, [[momentum-investing]] factor returns. These return streams have low correlation to each other and to the core, reducing overall portfolio volatility.

## Component Strategies

| Allocation | Component | Strategy | Role |
|------------|-----------|----------|------|
| 70% | Core | [[index-investing]] — SPY, VOO, VTI | Market beta, compounding, wealth building |
| 10% | Satellite 1 | [[options-selling]] — [[covered-calls]], [[wheel-strategy]] | Income generation, 1-2% monthly target |
| 10% | Satellite 2 | [[crypto-allocation]] — BTC/ETH [[dollar-cost-averaging]] | Asymmetric upside, portfolio diversification |
| 10% | Satellite 3 | Tactical — [[momentum-investing]], [[swing-trading]] picks | Active alpha, discretionary trades |

## Implementation

**Core Setup (70%)**

Buy and hold broad market index funds. The simplest and most effective approach:
- 50% in US total market (VTI or VOO for S&P 500)
- 10% in international developed (VXUS or EFA)
- 10% in bonds (BND or TLT depending on rate outlook)

Contribute regularly via [[dollar-cost-averaging]]. Rebalance annually. Do not touch this allocation based on market conditions, news, or fear. This is the "set and forget" engine. Over any 20-year period in US market history, this approach has been positive.

**Satellite 1: Options Income (10%)**

Deploy the [[wheel-strategy]] on high-quality stocks you want to own:
1. Sell cash-secured puts at strikes where you would happily buy the stock (typically 10-15% below current price, 30-45 DTE).
2. If assigned, sell [[covered-calls]] against the position at your target exit price.
3. Repeat. Target 1-2% monthly return on allocated capital.

This satellite generates income in sideways markets and acquires stocks at discounts in pullbacks. It pairs perfectly with the passive core because it thrives in the boring, range-bound periods when the index goes nowhere.

**Satellite 2: Crypto Allocation (10%)**

Systematic [[dollar-cost-averaging]] into [[bitcoin]] (60% of crypto allocation) and [[ethereum]] (40%). Buy weekly regardless of price. Hold through full market cycles (4+ years). This is a long-term asymmetric bet — crypto allocation provides exposure to a different return profile than equities. The 10% cap means even a total loss is survivable, but a 5-10x cycle gain meaningfully boosts overall portfolio returns.

**Satellite 3: Tactical Active (10%)**

This is your active trading allocation. Use it for:
- [[momentum-investing]] — buy the top-performing stocks from the last 6-12 months, rotate monthly
- [[swing-trading]] — trade technical setups on individual stocks (breakouts, pullbacks to support)
- Event-driven trades — pre-earnings positions, sector rotation plays

This satellite requires the most skill and time. Track results rigorously. If after 1-2 years this allocation underperforms the core, consider reallocating to the core. Intellectual honesty is critical.

**Rebalancing Rules**

- Rebalance the core annually (or when any allocation drifts more than 5% from target).
- Review satellite performance quarterly. If a satellite strategy loses more than 30% of its allocation in a quarter, pause and reassess before continuing.
- Profits from successful satellite trades can be swept into the core to compound.
- As total portfolio grows, the percentage in satellites can decrease — a $2M portfolio might run 85/15 core-satellite while a $100K portfolio might run 60/40.

## Example Setup

**$100,000 portfolio:**
- $70,000 in VTI ($50K), VXUS ($10K), BND ($10K) — monthly contributions of $1,000
- $10,000 in options account — selling 2-3 cash-secured puts per month on AAPL, MSFT, AMD at 10-15% OTM strikes
- $10,000 in crypto — weekly $125 BTC, $75 ETH purchases on Coinbase or Kraken
- $10,000 in active trading account — currently holding 3 momentum stocks (top sector leaders), rotated monthly based on relative strength

## When It Excels

- **Long-term wealth building** — this structure works over decades, not days. The core compounds regardless of what happens in satellites.
- **For investors who have a day job** — the core requires almost zero attention. Satellites can be managed in 2-5 hours per week.
- **All market conditions** — the core captures bull markets, options satellite earns in flat markets, crypto satellite provides upside in risk-on environments. Something is always working.
- **For investors transitioning from pure passive to active** — satellites let you test active strategies with limited risk while maintaining a wealth-building foundation.

## When It Fails

- **Aggressive bull markets** where 100% equity exposure would have been optimal. The bond allocation and defensive positioning of the core drag returns relative to going all-in.
- When the investor **treats the core as a piggy bank** — withdrawing from the core to fund failing satellite strategies destroys the compounding engine.
- If satellite strategies are **not tracked separately** — without clear accounting, it is impossible to know if satellites are adding value or just adding complexity and cost.
- **Very small portfolios** (under $10K) where splitting into 4 buckets creates positions too small to be meaningful or cost-efficient.

## Real-World Usage

**Institutional investors** almost universally use core-satellite. Pension funds, endowments, and sovereign wealth funds hold a large core of index exposure and then allocate a percentage to hedge funds, private equity, real estate, and other alternatives seeking alpha.

**Vanguard's founder Jack Bogle** advocated a version of this: the vast majority of your money in low-cost index funds, with a small "funny money" account for stock picks if you must scratch the itch. He found that formalizing the split prevented investors from going all-in on speculative positions.

**The "Bogleheads" community** has evolved the core-satellite concept into a philosophy: invest the core according to your investment policy statement, and only use satellite allocations that you have researched and backtested. The core is non-negotiable. The satellites are optional.

**See also:** [[index-investing]], [[asset-allocation]], [[wheel-strategy]], [[covered-calls]], [[dollar-cost-averaging]], [[portfolio-rebalancing]], [[crypto-allocation]]
