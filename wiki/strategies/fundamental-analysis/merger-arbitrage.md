---
title: "Merger Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [merger-arbitrage, M&A, event-driven, risk-arbitrage, deal-spread, hedging]
aliases: ["Risk Arbitrage", "M&A Arbitrage", "Deal Spread Trading"]
strategy_type: fundamental
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[event-driven-trading]]", "[[news-trading]]", "[[pairs-trading]]", "[[hedging]]", "[[options-strategies]]"]
---

# Merger Arbitrage

## Overview

Merger Arbitrage (also called **risk arbitrage**) profits from the spread between a target company's current stock price and the announced acquisition price. When Company A announces it will acquire Company B at $50/share, Company B's stock typically jumps to $47-49 -- not the full $50, because there is uncertainty about whether the deal will close. The merger arbitrageur buys Company B at $48, earning a $2 spread (4.2%) when the deal closes at $50, typically over 3-6 months. In stock-for-stock deals, the arb also shorts the acquirer's stock to hedge market risk.

This strategy was popularized by **Warren Buffett** early in his career and is a core strategy at hedge funds like **Citadel**, **Elliott Management**, and **Millennium**. The returns are modest (5-15% annualized) but exhibit low correlation to the broader market, making merger arb attractive as a diversifier. The primary risk is **deal break** -- if regulatory or financing obstacles kill the deal, the target stock can crash 20-40% back to its pre-announcement level.

## Rules

### Entry
1. **Identify announced deals.** Monitor M&A announcements via Bloomberg, SEC filings (SC 13D, DEFM14A), or services like Dealogic. Focus on definitive merger agreements, not rumors.
2. **Calculate the deal spread.** Spread = (Deal Price - Current Price) / Current Price. Annualize it: Annualized Spread = Spread / (Expected Days to Close / 365). Target annualized spreads above 5-8%.
3. **Assess deal risk.** Evaluate:
   - **Regulatory risk:** Antitrust review (DOJ, FTC, EU Commission). Deals in concentrated industries face higher scrutiny.
   - **Financing risk:** Is the acquirer's financing committed? Cash deals with committed bank financing are safest.
   - **Shareholder approval risk:** Does the deal need target/acquirer shareholder votes? Are there hostile shareholders?
   - **Material Adverse Change (MAC) risk:** Could a business deterioration give the acquirer an exit clause?
4. **Enter the position:**
   - **Cash deals:** Simply buy the target stock.
   - **Stock deals:** Buy the target and short the acquirer in the exchange ratio. If the deal offers 0.5 shares of acquirer per target share, short 0.5 shares of acquirer for every 1 share of target purchased.

### Exit
1. **Deal closes:** Position automatically resolves at the deal price. Target shares convert to cash or acquirer shares.
2. **Deal breaks:** Exit immediately if the deal is terminated. Do not wait for a potential sweetened offer -- the probability is low and the loss deepens quickly.
3. **Spread compression:** If the spread narrows to less than 1-2% (annualized below 3%), consider exiting early and redeploying capital into wider spreads.
4. **Timeline extension:** If regulatory review extends the timeline significantly (e.g., second request from DOJ), reassess whether the annualized return still justifies the capital commitment.

### Position Sizing
Diversify across 10-20 concurrent deals. No single deal should exceed 10% of the merger arb portfolio. Size inversely to deal risk: lower-risk deals (strategic, cash, no regulatory issues) get larger allocations.

## Indicators Used
- Deal spread (current price vs. announced deal price)
- Annualized spread (spread adjusted for expected time to close)
- Regulatory filing timeline (HSR Act waiting periods, EU Phase I/II)
- [[options-strategies|Options]] implied probability: option prices on the target can imply the market's probability of deal completion
- Acquirer's credit default swap (CDS) spread -- widening CDS signals financing risk
- Proxy filing analysis for shareholder vote risk

## Example Trade
**Deal:** Broadcom announces acquisition of VMware for $61.50/share in cash (plus 0.2520 shares of Broadcom)
1. VMware trades at $116 post-announcement. Based on deal terms (cash + stock), the effective deal value is $123 at current Broadcom prices. Spread: $7 (6.0%). Expected close: 12 months. Annualized: ~6%.
2. **Risk assessment:** Major regulatory risk (EU, China approvals needed for large semiconductor deal). Financing is committed. No shareholder approval issues.
3. Buy 1,000 shares VMW at $116. Short 252 shares AVGO at current price to hedge the stock component. Total capital deployed: ~$116,000.
4. After 14 months of regulatory review (longer than expected), the deal closes. VMW converts to $61.50 cash + 0.2520 AVGO shares per VMW share.
5. **Result:** Gross spread captured: ~$7,000 (6.0%). Annualized: ~5.1% (lower due to timeline extension). Short borrowing costs on AVGO reduced net return to ~4.2% annualized.

## Performance Characteristics
- **Win Rate:** 85-92%. Most announced deals close successfully. But the losses on broken deals are much larger than the gains on completed deals.
- **Profit Factor:** 1.5-2.5. The asymmetry is unfavorable (small gains, large losses), so high win rate is essential.
- **Best Market Conditions:** Active M&A markets with strategic deals, friendly regulatory environments, and low interest rates that encourage leveraged buyouts.
- **Worst Market Conditions:** Antitrust crackdowns, credit market freezes (deals lose financing), market crashes (acquirers invoke MAC clauses).
- **Annual Returns:** 5-15% with low volatility and low market correlation. Hedge funds leverage the strategy 2-4x to amplify returns to 12-25%.
- **Sharpe Ratio:** Typically 0.8-1.5, attractive on a risk-adjusted basis.

## Advantages
- Returns are largely independent of market direction -- the position profits as long as the deal closes
- Highly diversifiable across many concurrent deals, reducing single-deal risk
- Clear, binary outcome: the deal closes or it does not. This simplifies analysis compared to directional trading
- Academic and industry evidence supports a persistent positive risk premium for bearing deal risk
- Can be combined with [[options-strategies]] (selling puts on targets) to enhance returns

## Disadvantages
- **Asymmetric risk:** Gains are small and capped (the spread), while losses from broken deals can be 20-40%+ -- a single deal break can erase months of profits
- Requires deep expertise in securities law, antitrust regulation, and deal structure analysis
- Capital is locked up for months while the deal progresses through regulatory review
- Opportunity cost: in strong bull markets, 5-10% annualized returns underperform simple buy-and-hold
- Short selling the acquirer (in stock deals) involves borrowing costs and short squeeze risk
- Information disadvantage vs. dedicated M&A hedge funds with legal teams and regulatory contacts

## See Also
- [[event-driven-trading]] -- the broader category that includes merger arb alongside other special situations
- [[news-trading]] -- initial M&A announcement creates trading opportunity that precedes the arb
- [[pairs-trading]] -- structurally similar long/short approach, though driven by statistical rather than deal mechanics
- [[hedging]] -- the short leg in stock-for-stock deals is a form of hedging
- [[options-strategies]] -- selling target puts or buying deal-break protection via puts
