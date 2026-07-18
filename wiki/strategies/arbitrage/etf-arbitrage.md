---
title: "ETF Arbitrage"
type: reference
created: 2026-04-07
updated: 2026-07-14
status: good
tags: [arbitrage, etf, nav, authorized-participant, creation-redemption, market-neutral, spy, bonds]
aliases: ["ETF Arb", "Creation-Redemption Arbitrage", "NAV Arbitrage"]
strategy_type: algorithmic
timeframe: day
markets: [bonds]
complexity: advanced
backtest_status: untested
related: ["[[structural-forced-selling]]", "[[net-asset-value]]", "[[leveraged-etf-rebalancing]]"]
---

# ETF Arbitrage

## Overview

ETF arbitrage is the mechanism that keeps exchange-traded fund prices aligned with their [[net-asset-value]] (NAV). When an ETF's market price diverges from the aggregate value of its underlying holdings, Authorized Participants (APs) -- typically large broker-dealers like Goldman Sachs, JPMorgan, or Jane Street -- step in to exploit the discrepancy through the creation/redemption process. This in-kind mechanism is unique to ETFs and provides a structural arbitrage force that distinguishes ETFs from closed-end funds, which frequently trade at persistent premiums or discounts.

The ETF market has grown to over $10 trillion in assets, and the arbitrage mechanism is what makes it all work. However, the mechanism can break down under stress. During March 2020, fixed-income ETFs like LQD and HYG traded at 5-7% discounts to their reported NAV because the underlying corporate bonds were essentially illiquid -- the ETFs became the price discovery vehicle rather than tracking NAV. Additionally, [[leveraged-etf-rebalancing|leveraged and inverse ETFs]] create predictable end-of-day rebalancing flows that sophisticated traders exploit.

## How It Works

**Premium scenario (ETF price > NAV):**
1. AP observes that SPY is trading at $525.50 while the NAV of the S&P 500 basket is $525.00.
2. AP buys all 500 underlying stocks in their exact index weights on the open market.
3. AP delivers the stock basket to the ETF issuer (e.g., State Street for SPY).
4. ETF issuer creates new SPY shares and gives them to the AP.
5. AP sells the newly created SPY shares at the market price ($525.50).
6. **Profit:** $0.50 per share minus transaction costs. The creation of new shares increases supply, pushing the ETF price down toward NAV.

**Discount scenario (ETF price < NAV):**
1. AP buys SPY shares on the open market at the discounted price.
2. AP delivers SPY shares to the ETF issuer for redemption.
3. ETF issuer returns the underlying stock basket to the AP.
4. AP sells the individual stocks on the open market at their higher aggregate value.
5. The destruction of ETF shares reduces supply, pushing the ETF price up toward NAV.

## Entry/Exit Rules

### Entry
1. **Monitor premium/discount:** Track real-time ETF price vs. intraday indicative value (IIV) published every 15 seconds.
2. **Threshold exceeded:** When the premium or discount exceeds the cost of executing the creation/redemption (typically 5-20 bps for equity ETFs, 20-50 bps for bond ETFs), the arb is profitable.
3. **Initiate creation/redemption:** Submit a creation or redemption order to the ETF issuer (minimum creation unit is typically 25,000-50,000 shares).
4. **Hedge immediately:** While the creation/redemption processes overnight (T+1 or T+2), hedge the exposure to avoid directional risk.

### Exit
1. **Completion of process:** Once the creation/redemption settles, the arb is locked in. Sell the received shares or stocks.
2. **Intraday alternative:** Trade the ETF vs. underlying basket directly on the open market without formal creation/redemption, capturing spread within the trading day.

## Example Trade

**Setup:** iShares Investment Grade Corporate Bond ETF (LQD) trades at $108.50. Calculated NAV of underlying bonds is $110.00 -- a 1.36% discount.

1. **Buy 50,000 shares of LQD** at $108.50 = $5,425,000.
2. **Submit redemption order** to iShares for 1 creation unit (50,000 shares).
3. **Receive the underlying bond basket** valued at $5,500,000.
4. **Sell the bonds** in the OTC market (or hold, since they are valued higher).
5. **Gross profit:** $5,500,000 - $5,425,000 = **$75,000**.
6. **Transaction costs:** ETF commission (~$500), bond bid-ask spreads (~$15,000 for illiquid corporates), redemption fee (~$1,000). Total: ~$16,500.
7. **Net profit:** $75,000 - $16,500 = **$58,500**.
8. **Caveat:** In March 2020, selling the underlying bonds was the hard part -- the bonds were illiquid, and the reported NAV was stale. The ETF discount was arguably correct.

## Risk Management

- **Settlement risk:** Creation/redemption settles T+1 or T+2. Market conditions can change during settlement. Hedge with futures or options.
- **Underlying illiquidity:** For bond, commodity, or international ETFs, the underlying may be hard to trade. This is the primary risk and the reason discounts persist in stress periods.
- **Capital requirements:** Creation units are large (25,000-50,000 shares), requiring millions of dollars per trade.
- **Counterparty risk:** The AP relationship with the ETF issuer is contractual. In extreme scenarios, issuers can suspend creation/redemption.
- **Tracking error:** The ETF may hold a sampled subset of the index rather than all components, introducing basis risk in the arb.
- **Leveraged ETF risk:** Trading against [[leveraged-etf-rebalancing|leveraged ETF rebalancing]] flows involves directional market exposure during volatile periods.

## Advantages
- **Structural mechanism** -- creation/redemption is a built-in feature of ETFs, ensuring persistent opportunities
- **Near risk-free** for liquid equity ETFs where the underlying basket is easily tradable
- **Massive market** -- $10T+ in ETF assets means continuous flow of arbitrage opportunities
- **Benefits all investors** by keeping ETF prices fair and aligned with NAV
- **Tax efficient** -- in-kind redemptions avoid triggering capital gains for ETF holders

## Disadvantages
- **AP-only access** for formal creation/redemption -- retail traders cannot participate directly
- **Capital intensive** -- creation units require millions of dollars
- **Breaks under stress** -- when underlying assets are illiquid, the arb mechanism fails (March 2020 bonds, August 2015 flash crash)
- **Narrow margins** for liquid ETFs like SPY -- the spread between price and NAV is usually just a few basis points
- **Operational complexity** -- managing in-kind baskets of hundreds or thousands of securities
- **Regulatory burden** -- APs must maintain agreements with ETF issuers and meet regulatory requirements

## Real-World Examples
- **March 2020 bond ETF dislocation:** LQD, HYG, and other fixed-income ETFs traded at 5-7% discounts to NAV for days. APs could not efficiently arb because the underlying bonds were not trading. The ETF became the real-time price discovery mechanism.
- **August 24, 2015 flash crash:** Hundreds of ETFs were halted or traded at extreme discounts when market-wide circuit breakers triggered unevenly, disrupting the arb mechanism.
- **Leveraged ETF rebalancing:** 3x leveraged ETFs like TQQQ must rebalance daily to maintain their leverage ratio. After a +3% day, TQQQ must buy ~9% more exposure at the close -- creating a predictable, exploitable flow. See [[structural-forced-selling]].

## See Also
- [[structural-forced-selling]] -- forced rebalancing flows, including [[leveraged-etf-rebalancing]]
- [[net-asset-value]] -- the fundamental reference value for ETF pricing
- [[market-efficiency]] -- the economic principle that ETF arbitrage enforces
