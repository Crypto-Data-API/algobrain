---
title: "Corporate Action Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [arbitrage, corporate-action, spinoff, tender-offer, rights-offering, stub-trade, event-driven, value-investing]
aliases: ["Corporate Action Arb", "Spinoff Arbitrage", "Stub Trade Arbitrage"]
strategy_type: fundamental
timeframe: swing|position
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[event-driven-trading]]", "[[structural-forced-selling]]", "[[merger-arbitrage]]", "[[special-situations]]", "[[joel-greenblatt]]"]
---

# Corporate Action Arbitrage

## Overview

Corporate action arbitrage exploits temporary mispricings that arise from corporate events such as spinoffs, tender offers, rights offerings, and restructurings. These events create mechanical selling pressure and informational complexity that cause securities to trade below their intrinsic value. The strategy is a cornerstone of [[event-driven-trading]] and [[special-situations]] investing, famously championed by Joel Greenblatt, whose Gotham Capital returned 50% annualized over a decade primarily through spinoff and corporate action trades.

The core insight is that corporate actions create forced, non-economic sellers. When a company spins off a subsidiary, index funds that held the parent may be forced to sell the spinoff if it does not qualify for their index. Large institutions may dump the spinoff because it is too small for their portfolio, falls outside their mandate, or they simply do not want to research an unfamiliar company. This [[structural-forced-selling]] pushes the spinoff's price below intrinsic value, creating an opportunity for arbitrageurs who are willing to do the fundamental work.

## How It Works

**Spinoff arbitrage:** A parent company distributes shares of a subsidiary to existing shareholders. The combined value of parent + spinoff shares often exceeds the pre-spinoff parent price by 10-30% within 12 months, because:
- Index funds sell the spinoff mechanically (it is not in their index)
- Large institutions sell because the spinoff is too small or outside their mandate
- Analysts do not cover the new entity initially, so it is under-followed
- Management of the spinoff is often incentivized with stock options struck at the depressed post-spinoff price

**Tender offer arbitrage:** A company or acquirer offers to buy shares at a premium (e.g., $50 when the stock trades at $45). Buy at market ($45), tender at $50, capturing the $5 spread minus the risk of the deal failing.

**Rights offering arbitrage:** A company issues rights to existing shareholders to purchase new shares at a discount. If the rights are tradable, buy the rights below their theoretical value and exercise them. If shares purchased via rights are cheaper than market price, buy via rights and sell on the open market.

**Stub trading:** Value a parent company as the sum of its parts, then subtract the value of publicly traded subsidiaries. If the "stub" (remaining parent value) is negative or absurdly low, buy the parent and short the subsidiary.

## Entry/Exit Rules

### Entry
1. **Monitor corporate actions:** Track SEC filings (Form 10-12B for spinoffs, SC TO for tender offers, S-3 for rights offerings), press releases, and corporate event calendars.
2. **Analyze the event:** Read the full filing. Understand the terms, timeline, conditions, and any contingencies.
3. **Value both entities:** For spinoffs, independently value the parent and the spinoff using DCF, comparable companies, or sum-of-parts analysis.
4. **Identify the forced seller:** Determine which institutional holders will be forced to sell (index funds, mandate-constrained institutions) and estimate the selling pressure.
5. **Enter after the event:** For spinoffs, the best entry is typically 1-4 weeks after the distribution date, when [[structural-forced-selling]] peaks and the price is most depressed.

### Exit
1. **Fundamental re-rating:** Hold until the market recognizes the intrinsic value -- typically 6-18 months for spinoffs.
2. **Catalyst-driven exit:** Sell when analyst coverage initiates, index inclusion occurs, or an acquirer bids for the spinoff.
3. **Sum-of-parts convergence:** For stub trades, exit when the parent-subsidiary valuation gap closes.
4. **Stop loss:** If the fundamental thesis is invalidated (e.g., spinoff business deteriorates), exit regardless of price.

## Example Trade

**Event:** A large conglomerate (Parent Corp, $80B market cap) spins off its technology division (Tech Spin, $5B market cap). Tech Spin shares are distributed 1:5 to Parent Corp shareholders.

1. **Pre-spinoff:** Parent Corp trades at $200 per share.
2. **Post-spinoff distribution:** Parent Corp trades at $188 per share. Tech Spin trades at $8 per share. Combined value: $188 + ($8 x 0.2 shares per parent share) = $189.60.
3. **Forced selling:** Vanguard S&P 500 index fund holds 10M Parent Corp shares. Tech Spin is not in the S&P 500, so Vanguard receives 2M Tech Spin shares and must sell them. Other index funds similarly dump Tech Spin.
4. **Tech Spin drops to $6** in the first two weeks due to indiscriminate selling. Market cap: $3.75B. But DCF analysis suggests fair value is $12-15 per share.
5. **Buy 100,000 shares of Tech Spin** at $6 = $600,000.
6. **Month 3:** Two sell-side analysts initiate coverage with $13 price targets. Tech Spin rallies to $11.
7. **Month 6:** A private equity firm bids $14 per share for Tech Spin.
8. **Sell at $14.** Profit: ($14 - $6) x 100,000 = **$800,000** (133% return in 6 months).

## Risk Management

- **Business risk:** The spinoff may be a genuinely weak business that was spun off precisely because it was a drag on the parent. Not all spinoffs are undervalued.
- **Liquidity risk:** Spinoffs are often small-cap and thinly traded. Position sizing must account for limited [[liquidity]] and wide bid-ask spreads.
- **Timing risk:** The forced selling period may last longer than expected, and fundamental re-rating can take 12-18 months. Patience and capital reserves are required.
- **Deal risk (tender offers):** The tender offer may be withdrawn, the premium may be reduced, or regulatory approval may be denied. Size positions to survive deal breaks.
- **Leverage risk (stub trades):** Stub trades involve both a long and short leg. If the short leg rallies while the long leg falls, losses can be severe. Use strict stop losses.
- **Information complexity:** Corporate action documents can be hundreds of pages. Misunderstanding the terms of a spinoff or rights offering can lead to incorrect positioning.

## Advantages
- **Exploits structural inefficiency** -- forced selling creates genuine mispricings that are not explained by business fundamentals
- **High historical returns** -- academic studies show spinoffs outperform the market by 10-20% in the first 12 months on average
- **Low correlation** -- corporate action returns depend on company-specific events, not market direction
- **Repeatable** -- hundreds of spinoffs, tender offers, and rights offerings occur annually across global markets
- **Informational edge** -- most investors do not read 200-page Form 10-12B filings, creating an advantage for those who do

## Disadvantages
- **Research intensive** -- each situation requires deep fundamental analysis of unfamiliar companies
- **Long holding period** -- re-rating can take 6-18 months; capital is tied up
- **Small position sizes** -- many spinoffs are micro- or small-cap with limited [[liquidity]]
- **Business deterioration** -- the spinoff may underperform for fundamental reasons, not just forced selling
- **Concentrated risk** -- each position is a single company with idiosyncratic risk
- **Requires event monitoring infrastructure** -- staying on top of all corporate actions across the market requires dedicated screening tools

## Real-World Examples
- **Joel Greenblatt's Gotham Capital:** Averaged ~50% annual returns from 1985-1995, primarily through spinoff and corporate action arbitrage. His book *You Can Be a Stock Market Genius* details the strategy.
- **eBay/PayPal spinoff (2015):** PayPal was spun off from eBay. Post-spinoff, PayPal (the growth business) outperformed dramatically as it was re-rated from "eBay's payment subsidiary" to a standalone fintech leader, eventually reaching 5x its spinoff value.
- **Danaher/Fortive spinoff (2016):** Fortive was spun off from Danaher and initially traded down due to forced selling. It subsequently outperformed the S&P 500 by 40%+ over the next two years as the market recognized its stand-alone value.

## See Also
- [[event-driven-trading]] -- the broader strategy category, including [[merger-arbitrage]] and [[special-situations]]
- [[structural-forced-selling]] -- the mechanism that creates many corporate action opportunities
- [[joel-greenblatt]] -- the investor most associated with spinoff arbitrage
