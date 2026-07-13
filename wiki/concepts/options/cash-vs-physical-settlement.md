---
title: "Cash vs Physical Settlement"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [options, derivatives, market-microstructure]
aliases: ["Cash Settlement", "Physical Settlement", "Cash vs Physical", "Settlement Type"]
domain: [derivatives, options, market-microstructure]
difficulty: intermediate
related: ["[[spx-options]]", "[[spy-options]]", "[[xsp-options]]", "[[american-vs-european-options]]", "[[am-vs-pm-settlement]]", "[[assignment-and-exercise]]", "[[pin-risk]]", "[[options-portfolio-construction]]"]
---

**Cash settlement** and **physical settlement** describe what actually changes hands when an option is exercised at (or before) expiration. Cash-settled options pay out the intrinsic value in cash with no transfer of the underlying instrument; physical-settled options deliver the underlying shares (or commodity) at the strike price. The distinction is foundational: cash settlement eliminates [[pin-risk|pin risk]], removes assignment-driven margin shocks, and enables clean European-style mechanics on indices like SPX, NDX, and VIX. Physical settlement is the default for almost all US equity options — including [[spy-options|SPY]], QQQ, and individual stocks — and creates assignment-management workload that drives most of the operational complexity in active options trading.

## Overview

US options come in two settlement types:

| Type | What happens at exercise | Examples |
|---|---|---|
| **Cash settlement** | Intrinsic value paid in cash; no underlying changes hands | [[spx-options|SPX]], NDX, RUT, [[xsp-options|XSP]], [[vix|VIX]] |
| **Physical settlement** | Underlying shares delivered at strike (or short position created on a put) | [[spy-options|SPY]], QQQ, IWM, all single-stock equity options |

Settlement type often correlates with exercise style ([[american-vs-european-options]]) and underlying type:

- **Index options** → cash-settled, European exercise (no underlying shares exist to deliver).
- **Equity/ETF options** → physical-settled, American exercise.

But the correlation is not absolute — exceptions exist in international markets and in some specialty products.

## Mechanics of Each

### Cash Settlement

When a cash-settled option finishes in-the-money:

1. **Intrinsic value calculated** at the settlement reference value (SOQ for AM-settled, closing print for PM-settled — see [[am-vs-pm-settlement]]).
2. **Cash credit** posted to the long holder's account: (settlement value − strike) × multiplier for calls, or (strike − settlement value) × multiplier for puts.
3. **Cash debit** posted to the short writer's account by the same amount.
4. **No shares move.** No margin call from suddenly holding stock. No pin risk.

A long ITM SPX 5000 call when SPX settles at 5050 simply credits ($50 × $100 = $5,000) to the holder — no S&P 500 basket appears.

### Physical Settlement

When a physical-settled option finishes in-the-money:

1. **Auto-exercise** by OCC default if the option is $0.01 or more ITM at the close (unless a do-not-exercise is filed).
2. **Shares change hands.** A long ITM call → 100 shares delivered, debit at strike. A long ITM put → 100 shares short-sold (or existing long closed), credit at strike.
3. **Assignment is random** for short option holders — the OCC randomly selects accounts holding short positions in the assigned series.
4. **Resulting stock position** must then be margined, held, or liquidated, which can cascade into margin calls if the trader did not have enough capital to hold the resulting share position.

A short ITM SPY 500 call when SPY closes at 510 means the writer is short 100 SPY shares at $500 — they receive $50,000 cash but now have to either hold or buy back the short stock.

## Pros/Cons of Cash Settlement

**Pros:**

- **No pin risk.** The settlement value is a single computed number; there is no ambiguity about whether the option finished ITM.
- **No unwanted stock positions.** Sellers cannot be left holding a delta-1 share position they didn't size for.
- **No margin shocks.** A short option position never converts into a stock position needing different margin.
- **No early-assignment risk** (when paired with European exercise, as with index options).
- **Operational simplicity.** Settlement happens automatically; no trade-management decisions at expiration.
- **Capital efficient at scale.** Hedges pay cash exactly when needed without forcing share liquidation.

**Cons:**

- **Settlement-value ambiguity.** AM-settled cash options reference a derived SOQ that can differ from the prior close (see [[am-vs-pm-settlement]]).
- **Limited products.** Only available on broad-based indices and a few specialty contracts.
- **No share-level customization.** A trader using options to acquire stock at a target price (e.g., cash-secured puts on individual names) cannot use cash-settled products.

## Pros/Cons of Physical Settlement

**Pros:**

- **Direct share acquisition / disposition.** Strategies like [[wheel-strategy|the wheel]], [[cash-secured-put|cash-secured puts]], and [[covered-call|covered calls]] depend on physical settlement to actually move shares.
- **Predictable settlement reference.** The closing print of the underlying is the value — no SOQ machinery.
- **Available across all single-stock and ETF options** — far broader product set.

**Cons:**

- **Pin risk.** When the underlying closes very near a strike, sellers don't know with certainty whether they will be assigned overnight.
- **Assignment management workload** — checking ex-dividend dates, monitoring deep ITM positions, handling do-not-exercise.
- **Margin shocks.** Unexpected assignment can convert a small option position into a much larger share position, triggering margin calls.
- **Operational risk.** A long ITM call left untended at expiration becomes a stock position the trader may not have planned for (or have capital to support).
- **Tax interaction with [[ex-dividend-date|ex-dividend]]** — early exercise of ITM calls before ex-date is the most common cause of unexpected assignment on dividend-paying ETFs/stocks.

## Pin Risk Implications

Pin risk only applies to **physical-settled** options. The mechanics:

- An option closes very close to its strike (e.g., AAPL 200 call when AAPL closes at 200.02).
- The seller does not know whether the long counterparty will exercise — exercise is technically optional, and some traders submit do-not-exercise instructions on barely-ITM options.
- The seller cannot fully hedge overnight: hedging assuming exercise creates a wrong position if exercise doesn't happen, and vice versa.
- Monday's open can move the resulting stock position significantly before the seller can act.

For cash-settled options, there is no analog: the option settles to a calculated value, and any "pin" simply produces a small final P&L. The net Friday move is whatever it is, and the position is closed Friday.

This is one of the strongest practical arguments for [[spx-options|SPX]] over [[spy-options|SPY]] for active expiration-week strategies.

## ITPM Use (why we lean toward cash-settled for index hedges)

[[itpm|ITPM]]-style portfolios prefer cash-settled options for portfolio-level work because the pros map directly onto portfolio-management requirements:

- **Macro hedges need to pay in cash, not shares.** A long-short portfolio buying OTM SPX puts as catastrophe insurance wants cash on a crash, not a delivered short position to manage.
- **Premium-selling at scale must avoid assignment-driven margin shocks.** A short SPX strangle does not turn into a multi-million-dollar stock position overnight; a comparable SPY strangle could.
- **European-style exercise** (which usually accompanies cash settlement on index options) eliminates early-assignment surprise — see [[american-vs-european-options]].
- **Portfolio-level hedge sizing** is cleaner when each option is a self-contained P&L unit; physical settlement turns hedges into share positions that themselves need hedging.
- **Capital-efficient sizing.** Cash settlement means no stock margin requirement at expiration, which keeps the book's leverage profile predictable through expiration weeks.

For tactical or single-name positions where the trader actually wants the resulting share exposure (e.g., putting on a stock at a discount via a cash-secured put), physical settlement is the right tool.

## Related

- [[spx-options]] — primary cash-settled vehicle for index exposure
- [[spy-options]] — physically-settled S&P alternative
- [[xsp-options]] — cash-settled mini-SPX
- [[american-vs-european-options]] — exercise style usually correlates with settlement type
- [[am-vs-pm-settlement]] — within cash settlement, two timing variants
- [[assignment-and-exercise]] — physical-settlement mechanics
- [[pin-risk]] — only applies to physical settlement
- [[options-portfolio-construction]]
- [[options-position-sizing]]

## Sources

- OCC (Options Clearing Corporation) Settlement and Exercise rules
- Cboe product specifications (SPX, SPY-related, XSP)
- IRS Publication 550 and Form 6781 instructions (settlement-type interaction with tax treatment)
