---
title: "Basis Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [basis-trade, cash-and-carry, futures, arbitrage, convergence, crypto, treasury, quantitative]
aliases: ["Cash-and-Carry Trade", "Futures Basis Trade", "Spot-Futures Arbitrage"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, bonds, commodities]
complexity: intermediate
backtest_status: untested
related: ["[[merger-arbitrage]]", "[[pairs-trading]]", "[[dispersion-trading]]", "[[hedging]]", "[[futures]]"]
---

# Basis Trading

## Overview

Basis Trading exploits the price difference between a **spot (cash) asset** and its corresponding **futures contract** -- this difference is called the **basis**. In normal markets, futures trade at a premium to spot (called **contango**) to reflect the cost of carry (financing, storage, insurance). Occasionally, futures trade at a discount (called **backwardation**). The key insight is that regardless of which direction price moves, the basis must converge to zero at futures expiry. By buying the cheap leg and selling the expensive leg, the trader locks in the spread and profits from this guaranteed convergence.

The basis trade is one of the most important strategies in institutional finance. The **U.S. Treasury basis trade** -- buying cash Treasuries and selling Treasury futures -- has grown to over **$1 trillion** in notional and is a core strategy of relative-value hedge funds like Citadel, Millennium, and DE Shaw. In **crypto markets**, the basis trade (buying spot BTC/ETH and selling perpetual futures or dated futures) has become enormously popular because crypto futures frequently trade at 10-30% annualized premiums due to speculative demand, offering yield-like returns with limited directional risk.

## Rules

### Entry
1. **Identify the basis:** Calculate Basis = Futures Price - Spot Price. Annualize it: Annualized Basis = (Basis / Spot Price) x (365 / Days to Expiry) x 100%.
2. **Enter when the annualized basis exceeds your hurdle rate:**
   - **Treasuries:** Enter above 1-3% annualized (tight spreads, leveraged 10-50x).
   - **Crypto:** Enter above 10-15% annualized (wider spreads, lower leverage).
   - **Commodities:** Enter above 3-5% annualized.
3. **Positive basis (contango) trade:** Buy spot, sell futures. You profit as the futures premium decays toward zero at expiry.
4. **Negative basis (backwardation) trade:** Sell spot (or short), buy futures. Less common and harder to execute since shorting spot can be expensive.
5. **Crypto perpetual funding rate trade:** Buy spot BTC/ETH, short perpetual futures. Instead of expiry convergence, you collect the **funding rate** paid by longs to shorts every 8 hours when the rate is positive.

### Exit
1. **Hold to expiry:** The most common approach. The basis converges to zero mechanically as the futures contract settles against the cash price. No active trading required.
2. **Early exit on basis compression:** If the annualized basis narrows faster than expected (e.g., from 15% to 3%), close both legs and redeploy capital into a wider-basis opportunity.
3. **Roll the position:** Before expiry, close the near-month futures and sell the next-month futures to maintain exposure if the basis remains attractive.
4. **Stop-loss on margin:** If the short futures leg moves against you sharply (spot rallies, pushing futures even higher), you may face margin calls. Set a maximum margin usage threshold (e.g., 80% of available margin) as a hard exit trigger.

### Position Sizing
Size based on the margin requirements of the futures leg. For Treasuries, leverage of 10-20x is standard (highly leveraged). For crypto, use 2-5x leverage maximum. Never size so large that a temporary basis widening triggers a margin call before expiry convergence.

## Indicators Used
- Basis = Futures Price - Spot Price (absolute and annualized percentage)
- Cost of carry: financing rate + storage costs (for commodities) or borrow cost
- [[volume]] and open interest in the futures contract (ensures adequate liquidity for entry/exit)
- Funding rate (for crypto perpetual futures) -- 8-hourly rate determines carry return
- Implied repo rate (for Treasuries) -- the implied return from the basis trade
- Historical basis range to identify extreme dislocations

## Example Trade
**Market:** Bitcoin spot-futures basis trade
1. BTC spot trades at $65,000. The BTC quarterly futures (expiring in 90 days) trade at $68,250. Basis = $3,250 (5.0%). Annualized: 5.0% x (365/90) = 20.3%.
2. Buy 1 BTC spot at $65,000 on a crypto exchange. Simultaneously sell 1 BTC quarterly futures contract at $68,250 on the same exchange.
3. Net exposure: zero directional BTC risk. Whether BTC goes to $100K or $30K, the spot and futures positions offset. The only P&L driver is the basis converging.
4. Over 90 days, the futures premium decays: $3,250 -> $2,100 -> $800 -> $0 at settlement. Both legs close at the same price (settlement price).
5. **Result:** Profit = $3,250 (5.0% in 90 days, 20.3% annualized) on capital deployed equal to the margin for both positions (~$30,000 at 2x leverage). Effective return on capital: ~10.8% in 90 days.

## Performance Characteristics
- **Win Rate:** 90-95%. The trade is structurally near-arbitrage -- the basis must converge at expiry. Losses occur only from execution errors, exchange failures, or forced liquidation from margin calls.
- **Profit Factor:** 5.0-10.0. Very high because losses are rare and usually due to operational failures, not the strategy's logic.
- **Best Market Conditions:** High speculative demand (pushing futures premiums up), steep yield curves (making Treasury carry attractive), and high crypto funding rates. Bull markets in crypto produce enormous basis spreads.
- **Worst Market Conditions:** Market crashes that cause sudden backwardation (futures drop below spot), triggering mark-to-market losses on the short futures leg before expiry. Exchange counterparty risk in crypto (e.g., FTX collapse destroyed basis positions).
- **Annual Returns:** 5-15% in Treasuries (unlevered), 15-40% in crypto (depending on market conditions), 3-8% in commodities.
- **Risk Characteristics:** Low volatility, low market correlation, but exposed to liquidity crises and counterparty risk.

## Advantages
- Near-arbitrage: the convergence at expiry is a structural certainty, not a speculative bet
- Market-neutral: no directional exposure to the underlying asset
- Consistent, yield-like returns that are uncorrelated with traditional strategies
- Simple to understand and implement once exchange and margin infrastructure are in place
- Crypto basis trades offer some of the highest risk-adjusted returns available in digital assets
- Can be scaled significantly in liquid markets like Treasuries and major crypto pairs

## Disadvantages
- **Leverage risk:** Treasury basis trades use extreme leverage (10-50x), making them vulnerable to small basis widenings that trigger margin calls. The 2019 and 2020 Treasury market dislocations caused significant basis trade losses.
- **Counterparty risk:** In crypto, exchange insolvency (FTX, 2022) can result in total loss of both legs
- **Mark-to-market pain:** Even though the trade converges at expiry, the path to expiry can involve significant unrealized losses as the basis temporarily widens
- **Funding rate reversal:** In crypto perpetual funding rate trades, the rate can flip negative, causing losses instead of income
- **Regulatory and capital constraints:** Treasury basis trades face increasing regulatory scrutiny due to their systemic size ($1T+) and leverage
- **Opportunity cost:** Capital is locked for weeks or months earning modest returns when markets may offer better directional opportunities

## See Also
- [[merger-arbitrage]] -- another convergence-based strategy with defined timelines
- [[pairs-trading]] -- similar long/short structure, though driven by statistical rather than structural convergence
- [[dispersion-trading]] -- another relative-value strategy exploiting structural mispricings
- [[futures]] -- understanding futures pricing and cost of carry is essential
- [[hedging]] -- basis trading is structurally a hedged position
