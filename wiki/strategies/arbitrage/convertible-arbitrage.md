---
title: "Convertible Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [arbitrage, convertible-bonds, hedge-fund, options, credit, equity-options]
strategy_type: quantitative
timeframe: position
markets: [stocks, bonds]
complexity: advanced
backtest_status: untested
related: ["[[statistical-arbitrage]]", "[[pairs-trading]]", "[[implied-volatility]]", "[[delta]]", "[[gamma-scalping]]"]
---

# Convertible Arbitrage

## Overview

Convertible Arbitrage is a classic hedge fund strategy that exploits the **embedded option** in a convertible bond. A convertible bond pays fixed coupons like a regular bond but can be converted into a fixed number of shares of the issuing company's stock. This conversion feature is essentially a [[call-option]] on the stock, and the strategy seeks to capture its value at a discount.

The core trade: **buy the convertible bond** (gaining the embedded call option plus credit income) and **short the underlying stock** to hedge away equity risk. The resulting position isolates the option component, the credit spread, and any mispricing between the bond and the stock. Profits come from the bond's coupon income, the option's [[gamma]] (profiting from stock volatility), and any convergence of the bond price to fair value.

## Setup

1. **Identify a convertible bond** trading cheap relative to its theoretical value (bond floor + embedded option value). Screen for bonds where [[implied-volatility]] of the embedded option is below realized [[volatility]].
2. **Buy the convertible bond** at market price.
3. **Short the underlying stock** in the correct [[delta]]-neutral ratio. If the bond's conversion ratio implies delta of 0.50, short 50 shares per bond.
4. **Hedge interest rate risk** with Treasury futures or [[interest-rate-swaps]] to isolate the equity and volatility components.
5. **Rebalance the delta hedge** as the stock moves -- this [[gamma-scalping]] generates additional P&L.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock rallies | Bond conversion value rises; short stock loses; net gain from [[gamma]] |
| Stock declines | Short stock profits; bond declines but bond floor provides cushion |
| Stock is volatile | Frequent delta rebalancing generates [[gamma-scalping]] profits |
| Stock is flat | Coupon income accrues; [[theta]] on embedded option slowly decays |
| Credit deterioration | Bond price drops below bond floor; potential loss |

**Profit sources:** Coupon income, gamma scalping from delta rebalancing, convergence to fair value. **Risk sources:** Credit risk, liquidity risk, interest rate risk, short squeeze on borrowed stock.

## When to Use

- The convertible bond market offers **mispricings** -- embedded options trading below fair [[implied-volatility]].
- You have access to bond markets, leverage, and stock borrowing at reasonable cost.
- [[volatility]] is expected to be **elevated** (more gamma-scalping opportunities).
- You can hedge interest rate exposure and monitor credit risk continuously.

## Advantages
- Multiple profit sources: coupon income, gamma, convergence, and credit spread
- Natural downside cushion from the bond floor (bond value without conversion)
- Delta-neutral positioning reduces directional equity risk
- One of the most proven and enduring hedge fund strategies (decades of track record)

## Disadvantages
- **Highly capital-intensive** and requires leverage for meaningful returns
- Credit risk: if the issuer's creditworthiness deteriorates, the bond can fall below its theoretical floor
- **Liquidity risk:** convertible bonds can become illiquid in stressed markets (2008 was devastating)
- Requires sophisticated systems for pricing embedded options and managing dynamic hedges
- Stock borrowing costs and availability can erode profitability or make the trade infeasible

## See Also
- [[statistical-arbitrage]] -- another market-neutral strategy profiting from mispricings
- [[gamma-scalping]] -- the rebalancing technique that generates profits from volatility
- [[implied-volatility]] -- key input for determining if the embedded option is cheap
