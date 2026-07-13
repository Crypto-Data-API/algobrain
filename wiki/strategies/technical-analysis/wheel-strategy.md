---
title: "The Wheel Strategy"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [options, income, wheel, premium-selling, cash-secured-put, covered-call, assignment]
aliases: ["The Wheel", "Triple Income Strategy", "Options Wheel"]
strategy_type: hybrid
timeframe: swing|position
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[covered-call]]", "[[cash-secured-put]]", "[[iron-condor]]", "[[implied-volatility]]", "[[theta]]", "[[delta]]", "[[option-volatility-and-pricing]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[position-sizing]]"]
---

# The Wheel Strategy

## Overview

The Wheel is a systematic [[options]] income strategy that cycles between selling [[cash-secured-put]]s and [[covered-call]]s on stocks the trader is willing to own at a discount. The process begins by selling a cash-secured put on a quality stock. If the put expires worthless, the trader keeps the premium and sells another put. If the put is assigned, the trader takes delivery of the shares (at an effective cost basis reduced by the premium collected), then immediately begins selling [[covered-call]]s against those shares until they are called away. The cycle then repeats.

The Wheel works best on fundamentally strong stocks that the trader would be happy holding long-term. It transforms the typical buy-and-hold experience into a premium-collection engine, generating income in three ways: put premiums, call premiums, and dividends while holding shares (Source: [[book-option-volatility-and-pricing]]). The strategy requires patience, discipline, and enough capital to accept assignment -- it is inherently a cash-intensive, lower-return-but-consistent approach.

## Rules

### Entry (Phase 1 -- Sell Cash-Secured Puts)
1. **Select a quality stock** you genuinely want to own. Strong fundamentals, stable earnings, liquid options. Popular wheel stocks: AAPL, MSFT, AMD, SOFI, PLTR.
2. **Sell 1 OTM put** at a [[strike-price]] you consider a fair or discounted entry. Typical delta: 0.20-0.30.
3. **Expiration:** 30-45 DTE for optimal [[theta]] decay. Weeklies work but require more active management.
4. **Ensure full cash backing:** Hold enough cash to buy 100 shares at the strike price. No margin.

### Entry (Phase 2 -- Sell Covered Calls)
1. If assigned on the put, you now own 100 shares. Begin selling [[covered-call]]s.
2. **Sell 1 OTM call** at or above your cost basis (strike price minus premium collected). Delta: 0.25-0.35.
3. Continue selling calls each cycle until the shares are called away.
4. Collect dividends while holding shares for additional income.

### Exit
1. **Shares called away:** The stock rallies above your call strike. Shares are sold at a profit (strike above cost basis). Return to Phase 1 and sell puts again.
2. **Roll if necessary:** If the stock drops well below your cost basis, sell calls at your cost basis strike rather than below it, even if premiums are small. Avoid locking in a loss. See [[trade-repair-and-rolling]] for detailed rolling mechanics.
3. **Abandon the wheel:** If the fundamental thesis breaks (earnings collapse, sector rotation), close the position entirely rather than continuing to sell calls on a declining stock.

### Rolling and Adjustments

The wheel requires active rolling at both phases. The key adjustment scenarios:

**Phase 1 — Rolling a tested put:** When the stock drops toward the short put strike before expiration, roll down and out — buy back the current put and sell a lower-strike put at a later expiration, ideally for a net credit. This lowers the assignment price and collects additional premium. Only roll if the fundamental thesis is intact; if the thesis is broken, let the put expire or close it. (Source: [[recovering-losing-options-positions]])

**Phase 2 — Managing underwater shares:** The wheel's biggest risk is "bag-holding" — being assigned on the put and then watching the stock continue to fall. When this happens:
- **Sell calls at your cost basis strike**, not below it. Premiums will be small (the calls are far OTM), but this avoids locking in a loss if the stock rebounds.
- **Consider the stock repair strategy** (buy 1 ATM call, sell 2 OTM calls at cost basis) to lower breakeven at zero cost if you expect a partial recovery.
- **Do NOT sell calls below cost basis** unless you have deliberately decided to accept a smaller loss and exit the position.

**The 21-DTE rule:** Both put and call legs should be managed at ~21 DTE. At that point [[theta]] accelerates but [[gamma-risk|gamma risk]] spikes — the "gamma trap." Rolling at 21 DTE captures the majority of time decay while avoiding the zone where small price moves cause outsized P&L swings. (Source: [[recovering-losing-options-positions]])

### Position Sizing
Allocate no more than 15-20% of the portfolio to a single wheel position. Diversify across 3-5 different underlyings to reduce single-stock risk.

## Indicators Used
- [[implied-volatility]] / IV rank -- higher IV means richer premiums on both puts and calls
- [[delta]] -- guides strike selection for both phases (0.20-0.30 typical)
- [[theta]] -- the primary profit driver; daily time decay generates income
- [[support-and-resistance]] -- choose put strikes near strong support levels for better assignment prices

## Example Trade
**Asset:** AMD trading at $155
1. **Phase 1:** Sell 1 AMD $145 put, 35 DTE, for $3.50 ($350 credit). Cash reserved: $14,500.
2. AMD drops to $142. The put is assigned. You now own 100 shares at an effective cost basis of $145 - $3.50 = **$141.50**.
3. **Phase 2:** Sell 1 AMD $150 call, 30 DTE, for $4.00 ($400 credit). Adjusted cost basis: $141.50 - $4.00 = **$137.50**.
4. AMD rallies to $153. Shares are called away at $150. Total profit: ($150 - $141.50) + $4.00 = **$12.50 per share ($1,250)**.
5. **Return to Phase 1:** Sell another cash-secured put on AMD and repeat the cycle.
6. **Annualized return:** If each full cycle takes ~60-90 days and nets 5-8%, the annualized return is approximately 20-35% on deployed capital.

## Performance Characteristics
- **Win Rate:** 75-90% of individual option sales expire profitably (OTM).
- **Profit Factor:** 1.5-2.5. Consistent small gains with occasional drawdowns when holding assigned shares through pullbacks.
- **Best Market Conditions:** Sideways to moderately bullish. Elevated [[implied-volatility]] environments.
- **Worst Market Conditions:** Severe bear markets (assigned on puts, then shares continue falling; calls yield tiny premiums far below cost basis). Strong bull markets (puts never get assigned, missing the rally).

## Advantages
- **Triple income stream:** Put premiums, call premiums, and dividends while holding shares
- **Systematic and repeatable:** Clear rules eliminate emotional decision-making
- **Buys stocks at a discount:** The put premium reduces the effective purchase price
- **Works on quality stocks:** Aligns income generation with long-term equity ownership
- **Defined risk:** You always know the worst case -- owning shares of a stock you selected

## Disadvantages
- **Capital intensive:** Requires enough cash to buy 100 shares per position ($10,000-$50,000+ per stock)
- **Bag-holding risk:** If the stock drops 30-50%, you are stuck selling low-premium calls for months while sitting on large unrealized losses
- **Opportunity cost:** Capital is locked up in cash reserves or assigned shares, unable to deploy elsewhere
- **Not a hedge:** The strategy offers no protection against catastrophic stock declines
- **Requires patience:** Full cycles can take months, and returns are steady but not spectacular on a per-trade basis

## See Also
- [[covered-call]] — Phase 2 of the wheel in isolation
- [[cash-secured-put]] — Phase 1 of the wheel in isolation
- [[trade-repair-and-rolling]] — complete rolling and adjustment framework for both phases
- [[gamma-risk]] — the risk that drives the 21-DTE roll rule
- [[iron-condor]] — a defined-risk alternative that does not require owning shares
- [[theta]] — the Greek that powers the wheel's income generation
- [[position-sizing]] — sizing each wheel position (15-20% max per underlying)

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg covers the foundational mechanics of cash-secured puts, covered calls, and the premium-collection logic that underlies the wheel strategy
