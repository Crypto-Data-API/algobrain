---
title: "Cross Margin vs Isolated Margin"
type: comparison
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [comparisons, margin, leverage, risk-management, crypto, market-microstructure, derivatives]
aliases: ["cross-margin", "isolated-margin", "cross-vs-isolated", "margin-mode"]
subjects: ["[[margin]]", "[[leverage]]"]
comparison_dimensions: [risk-sharing, liquidation, capital-efficiency, use-case, risk]
domain: [market-microstructure, risk-management]
prerequisites: ["[[maintenance-margin]]", "[[leverage]]", "[[liquidation]]"]
related: ["[[liquidation]]", "[[perpetual-futures]]", "[[position-sizing]]", "[[risk-management]]", "[[binance]]", "[[maintenance-margin]]", "[[mark-price]]", "[[liquidation-cascade]]", "[[crypto-perpetual-futures]]", "[[delta-neutral]]"]
---

## Overview

Cross margin and isolated margin are the two modes for managing collateral on crypto derivatives exchanges like [[binance]], [[hyperliquid]], and Bybit. The choice between them determines how your margin is allocated, when you get liquidated, and whether one bad trade can wipe your entire account. This is not a minor setting; it is one of the most important [[risk-management]] decisions a leveraged trader makes.

## Comparison Table

| Dimension | Cross Margin | Isolated Margin |
|---|---|---|
| **Collateral Sharing** | Entire account balance backs all positions | Each position has its own dedicated margin |
| **Liquidation Trigger** | Account-level: all positions liquidated together | Position-level: only that position is liquidated |
| **Max Loss per Position** | Entire account balance | Only the margin assigned to that position |
| **Capital Efficiency** | Higher: unused margin from one position helps another | Lower: margin is locked per position |
| **Liquidation Price** | Farther from entry (more buffer) | Closer to entry (less buffer) |
| **Adding Margin** | Automatic from account balance | Manual: must add margin explicitly |
| **Multiple Positions** | Profits from one offset losses on another | Positions are independent; no offset |
| **Risk Level** | Higher account risk; one bad trade can drain all | Contained risk; bad trade only loses its margin |
| **Best For** | Experienced traders running hedged portfolios | New traders; high-risk trades; portfolio isolation |
| **Default Setting** | Default on most exchanges | Must be selected per position |

## Practical Example

Consider a trader with $10,000 in their account who opens two positions:

**Position A:** Long BTC at $69,000 with 10x [[leverage]], $5,000 notional ($500 margin)
**Position B:** Long ETH at $2,100 with 10x [[leverage]], $5,000 notional ($500 margin)

**Under Cross Margin:**
- Both positions are backed by the full $10,000 account balance
- If ETH drops 20%, Position B is down $1,000 but is not liquidated because the $10,000 account absorbs the loss
- However, if both positions go badly, the entire $10,000 is at risk
- Liquidation price for each position is much farther away because $10,000 backs each trade

**Under Isolated Margin:**
- Position A is backed only by its $500 margin
- Position B is backed only by its $500 margin
- If ETH drops 10%, Position B hits [[liquidation]] and is closed for a ~$500 loss
- The remaining $9,500 is completely safe and untouched
- But Position B gets liquidated sooner because only $500 backs a $5,000 notional position

## Key Differences

**Cross margin prevents premature liquidation.** Because the entire account balance acts as collateral, positions have wider breathing room. A temporary wick that would liquidate an isolated position might be survived in cross margin. This is especially valuable during volatile moments where prices spike briefly before reverting.

**Isolated margin contains catastrophic risk.** The biggest danger in leveraged trading is the one trade that ruins everything. With isolated margin, each position can only lose its allocated margin. If you put $500 into an isolated 50x long on a speculative altcoin, the maximum loss is $500, no matter how far the price falls. In cross margin, that same trade going wrong could trigger cascading liquidations across your entire portfolio.

**Cross margin enables natural hedging.** If you are long BTC and short ETH (a relative value trade), cross margin allows profits on one leg to offset losses on the other. Under isolated margin, one leg might get liquidated even though the combined trade is profitable. Professional traders running multiple correlated positions almost always use cross margin.

**Isolated margin forces better [[position-sizing]].** Because you must explicitly allocate margin to each trade, isolated margin forces you to think about how much you are willing to lose. Cross margin can create a false sense of security, as the account looks healthy until a sudden market crash liquidates everything at once.

## When to Use Each

**Choose cross margin when:**
- You run hedged or correlated positions (long/short pairs)
- You are an experienced trader who monitors positions actively
- You want maximum capital efficiency and wider [[liquidation]] buffers
- You trade major pairs (BTC, ETH) with lower [[volatility]]
- You understand that your entire account is at risk

**Choose isolated margin when:**
- You are new to leveraged trading and want to limit downside
- You are taking high-[[leverage]] bets on volatile altcoins
- You want to risk only a specific dollar amount per trade
- You are testing a new strategy and want to contain losses
- You follow strict [[risk-management]] rules (e.g., risk 1-2% per trade)

## Auto-Deleveraging Interaction

When a liquidation cannot be filled in the market without further loss and the venue's insurance fund is insufficient, exchanges may use **auto-deleveraging (ADL)**: profitable opposing traders are forcibly partially closed at the bankruptcy price to absorb the shortfall. Margin mode interacts with this — large cross positions that blow through their entire account are a common source of ADL events, and traders running winning positions can be deleveraged through no fault of their own during a [[liquidation-cascade]].

## Risks and Pitfalls

- **Cross account wipeouts** — a single mismanaged position can liquidate everything, including unrelated winners
- **False security under isolated** — capped loss is comforting, but the position liquidates faster, so it is easier to get stopped out by noise
- **ADL surprises** — even a correct, profitable position can be auto-deleveraged during cascades
- **Mode-switch mistakes** — flipping modes mid-trade changes the liquidation price; do it deliberately, not in a panic

## Verdict

Neither mode is universally better; each serves a different risk philosophy. Isolated margin is safer for most traders because it enforces [[position-sizing]] discipline and prevents total account wipeouts. Cross margin is more capital-efficient and appropriate for experienced traders running multi-position portfolios with hedges. The worst mistake is using cross margin without understanding it: one bad trade in a volatile market can drain your entire balance before you can react. Start with isolated margin, graduate to cross margin only when you fully understand the [[liquidation]] mechanics and have proven [[risk-management]] discipline.
