---
title: Margin
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [margin, leverage, risk-management, derivatives]
aliases: ["margin", "collateral", "margin requirement", "Margin Trading", "margin-trading", "trading on margin", "buying on margin"]
domain: [risk-management]
prerequisites: ["[[leverage]]"]
difficulty: beginner
related:
  - "[[leverage]]"
  - "[[liquidation]]"
  - "[[futures]]"
  - "[[short-selling]]"
  - "[[position-sizing]]"
  - "[[cross-margin-vs-isolated-margin]]"
  - "[[portfolio-margin]]"
---

# Margin

Margin is the collateral a trader deposits with a broker or exchange to open and maintain a leveraged position.

## Overview

When trading on margin, you borrow funds to control a position larger than your available capital. The margin you post acts as a security deposit -- if the trade moves against you, losses are deducted from this collateral. Margin enables [[leverage]] but introduces the risk of forced liquidation.

## Key Details

### Margin Types

- **Initial margin**: The minimum collateral required to open a position. Typically expressed as a percentage of the position's notional value (e.g., 10% for 10x leverage).
- **Maintenance margin**: The minimum collateral that must remain in the account to keep a position open. Falls below this and you receive a margin call.
- **Margin call**: A demand from the broker to deposit additional funds or have positions liquidated. In fast-moving markets, liquidation can occur without prior warning.

### Margin Modes

- **Isolated margin**: Only the margin allocated to a specific position is at risk. If liquidated, other account funds are unaffected.
- **Cross margin**: The entire account balance serves as collateral for all open positions. Lowers liquidation risk per position but puts the full account at stake.

### Margin Mechanics (Quick Reference)

```
Initial margin     = Notional / Leverage              (collateral to open)
Maintenance margin = maintenance_rate x Notional      (collateral to keep open)
Margin ratio       = Account Equity / Used Margin      (health metric; watch >1.0)
Margin call fires when:  Equity <= Maintenance margin
Free margin        = Equity - Used Margin              (buffer available for new trades / adverse moves)
```

Equity here is balance plus unrealized P&L. As a position moves against the trader, unrealized losses erode equity; once equity falls to the maintenance level, the broker issues a margin call or (on most crypto venues and in fast markets) liquidates immediately without warning. Crypto perpetuals add a wrinkle: ongoing [[funding-rate|funding]] payments are debited from equity, so a position can drift toward a margin call even with a flat price.

### Reg T vs Portfolio Margin

In US equities, **Reg T** sets initial margin at 50% (2x leverage) for marginable stocks with a 25% maintenance minimum. **[[portfolio-margin]]** accounts (for larger, qualified accounts) instead size margin off the net risk of the whole book under stress scenarios, often allowing far more leverage on hedged positions because offsetting risks net out. Futures and crypto venues use their own SPAN-style or fixed-tier margin schedules.

## Trading Relevance

Understanding margin mechanics is critical for managing leveraged risk. Traders should monitor their margin ratio (equity / used margin) and maintain a buffer above maintenance levels, especially during volatile conditions. The key discipline is keeping a large free-margin cushion so a single adverse spike does not trigger forced [[liquidation]] at the worst possible price. Many blowups stem from ignoring margin requirements or over-leveraging across correlated positions — in cross margin, one bad position can drag the entire account into liquidation. See [[cross-margin-vs-isolated-margin]] for the trade-off.

## Sources

- CME Group, "Margin: Know What's Needed" and SPAN methodology documentation
- FINRA Rule 4210 / Regulation T — margin requirements for US securities accounts
- (Source: [[book-when-genius-failed]]) -- LTCM's collapse illustrates how margin calls during a liquidity crisis force selling into a falling market

## Related

- [[leverage]] -- margin enables leveraged trading
- [[stop-loss]] -- prevents margin from being fully consumed
- [[position-sizing]] -- determines how much margin to allocate per trade
- [[cross-margin-vs-isolated-margin]] -- comparison of the two margin modes and their risk implications
