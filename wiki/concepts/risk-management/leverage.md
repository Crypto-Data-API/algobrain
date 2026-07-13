---
title: Leverage
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [leverage, risk-management, derivatives, margin]
aliases: ["leverage", "gearing", "leverage ratio"]
domain: [risk-management]
prerequisites: ["[[margin]]"]
difficulty: beginner
related:
  - "[[margin]]"
  - "[[liquidation]]"
  - "[[futures]]"
  - "[[position-sizing]]"
  - "[[book-when-genius-failed]]"
  - "[[book-the-black-swan]]"
---

# Leverage

Leverage is the use of borrowed capital to amplify potential returns (and losses) on a trade or investment.

## Overview

Traders use leverage to control a position larger than their actual capital. A 10x leverage ratio means $1,000 of capital controls a $10,000 position. Leverage is available across asset classes -- from 2x in traditional equities margin accounts to 100x or more on some crypto derivatives exchanges.

## How It Works

- **Leverage ratio**: Expressed as a multiplier (2x, 5x, 10x, 100x). Higher ratios amplify both gains and losses proportionally.
- **Margin requirement**: The collateral you must deposit. At 10x leverage, you post 10% of the position's notional value as [[margin]].
- **Amplified P&L**: A 1% price move at 10x leverage produces a 10% gain or loss on your deposited capital.
- **Liquidation**: If unrealized losses approach your deposited margin, the exchange or broker forcibly closes your position to prevent the account from going negative. At 10x leverage, a roughly 10% adverse move triggers liquidation (minus fees and buffer).

## The Math

Leverage is the ratio of position notional to equity:

```
Leverage = Position Notional / Account Equity
Margin requirement = 1 / Leverage   (e.g. 10x => 10% initial margin)
Account P&L %      = Leverage x Underlying Move %
```

A position survives an adverse move only until equity is exhausted down to the maintenance buffer. The approximate liquidation distance for an isolated long is:

```
Liq move % ≈ (1 / Leverage) - maintenance_margin_rate
```

So at 10x with a 0.5% maintenance rate, a roughly 9.5% adverse move wipes the position. At 100x, well under 1% does. This is why effective leverage — not headline leverage — is what matters: a small posted margin against a large notional means the market only needs to twitch to liquidate you. Note that leverage cuts both ways on volatility drag too; a leveraged position that gains 10% then loses 10% ends below where it started, and the gap widens with leverage (the core problem for daily-rebalanced leveraged ETFs).

## Risk Amplification

Leverage magnifies risk in several critical ways:

1. **Faster drawdowns** -- losses accumulate at the leveraged rate
2. **Liquidation cascades** -- forced closures can accelerate price moves
3. **Funding costs** -- borrowing capital incurs interest or funding fees over time
4. **Gap risk** -- prices can jump past your liquidation level in volatile markets

The definitive case study in leverage risk is [[ltcm]], which operated at roughly 25:1 leverage (and far higher on a notional basis). When the Russian debt crisis of 1998 caused their convergence trades to diverge, the leverage transformed manageable losses into a $4.6 billion catastrophe that nearly triggered a systemic financial crisis (Source: [[book-when-genius-failed]]). [[nassim-taleb]] argues that leverage is particularly dangerous because it interacts with fat-tailed distributions -- extreme events occur more frequently than models predict, and leverage ensures those events are lethal rather than merely painful (Source: [[book-the-black-swan]]).

## Trading Relevance

Leverage is essential for capital-efficient trading but is the primary cause of account blowups. Professional traders combine leverage with strict [[stop-loss]] orders and disciplined [[position-sizing]] to manage the amplified risk. The general rule: the higher the leverage, the tighter your risk controls must be.

## Sources

- (Source: [[book-when-genius-failed]]) -- Lowenstein's account of LTCM's collapse is the canonical study of how leverage transforms manageable losses into existential ones
- (Source: [[book-the-black-swan]]) -- Taleb's argument that leverage combined with fat-tailed distributions creates catastrophic fragility
- Roger Lowenstein, *When Genius Failed: The Rise and Fall of Long-Term Capital Management* (Random House, 2000)
- CME Group, "Margin: Know What's Needed" — exchange documentation on initial vs. maintenance margin and leverage mechanics
- FINRA, "Investing with Borrowed Funds: No 'Margin' for Error" — regulator guidance on margin/leverage risk for retail accounts

## Related

- [[margin]] -- collateral required for leveraged positions
- [[futures]] -- commonly traded with leverage
- [[options]] -- built-in leverage through premium pricing
- [[stop-loss]] -- critical risk tool when using leverage
- [[cross-margin-vs-isolated-margin]] -- comparison of the two margin modes for leveraged trading
