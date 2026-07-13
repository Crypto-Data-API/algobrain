---
title: "Wash Sale Rule"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [risk-management, regulation, stocks]
aliases: ["Wash Sale", "Wash Sales", "Wash Sale Rule", "IRC 1091", "Section 1091"]
domain: [risk-management]
prerequisites: ["[[capital-gains]]"]
difficulty: beginner
related: ["[[capital-gains]]", "[[tax-loss-harvesting-australia]]", "[[section-1256-contracts]]", "[[transaction-costs]]", "[[regulation]]"]
---

The **wash sale rule** (US tax law, **IRC §1091**) disallows a capital loss when an investor sells a security at a loss and buys back a "substantially identical" security within a **61-day window** — 30 days before through 30 days after the loss sale. The loss is not erased; it is **deferred** by adding the disallowed amount to the cost basis of the replacement shares (and extending their holding period). The rule exists to stop investors from booking a tax loss while keeping essentially the same economic position. This is a tax-mechanics page, not tax advice — consult a qualified professional for your facts.

## How It Works

| Element | Detail |
|---|---|
| Statute | IRC §1091 (loss disallowance); §1091(d) (basis adjustment) |
| Window | 61 days total: 30 days before the loss sale + the sale day + 30 days after |
| Trigger | Acquiring a "substantially identical" security in the window |
| Applies to | Stocks, bonds, [[options-overview\|options]], ETFs, mutual funds — any "stock or securities" |
| Effect | Loss **disallowed now**, added to the basis of the replacement lot (deferred, not lost) |
| Holding period | The replacement lot inherits the original's holding period |

### Worked example

You buy 100 shares at \$50 and sell them at \$40 (a \$1,000 loss). If you buy 100 shares of the same stock back 10 days later at \$42, the \$1,000 loss is **disallowed** for now. Instead, your new lot's basis becomes \$4,200 + \$1,000 = \$5,200 (i.e. \$52/share). The benefit is recovered when you finally sell the replacement lot in a non-wash transaction.

## What Counts as "Substantially Identical"

- **Clearly triggers:** repurchasing the *same* stock or the same option series; selling stock and buying a call on it; buying in an IRA what you sold at a loss in a taxable account (the IRS treats spousal and IRA purchases as yours).
- **Generally does not:** rotating into a *different* company in the same sector, or swapping one broad index ETF for a *different-index* ETF (e.g. an S&P 500 fund for a total-market fund) — the standard tactic in tax-loss-harvesting.
- **Grey area:** two ETFs tracking the *same* index from different issuers. There is no bright-line IRS ruling, so conservative harvesters avoid same-index swaps.

## Why It Matters for Traders

- **It taxes active loss-taking.** Frequent in-and-out trading and "trade repair" (rolling losers) can pile up disallowed losses and basis adjustments, turning [[transaction-costs|trading costs]] into a tax-accounting burden. See wash-sale-rules-options for the options-specific mechanics.
- **It shapes tax-loss-harvesting.** Harvesters deliberately sell losers to bank losses, then must wait 31 days or buy a *non*-identical proxy to keep market exposure without tripping the rule.
- **Year-end danger zone.** A loss sale in late December with a repurchase in early January still falls inside the 61-day window, so the loss can be disallowed in the year you wanted it.
- **Key carve-out — [[section-1256-contracts|§1256 contracts]].** Broad-based index options (SPX, NDX, RUT) and most futures are marked to market at year end and are **not** subject to the wash sale rule, which is one reason active index traders prefer SPX to SPY.

## Jurisdiction Note

The wash sale rule as described is **US-specific**. Other countries have their own "bed-and-breakfasting" anti-avoidance rules with different windows — e.g. the UK's 30-day share-matching rule and Australia's ATO wash-sale anti-avoidance stance (see [[tax-loss-harvesting-australia]]). The economic intent is the same: deny a loss when the position is not genuinely closed.

## Related

- [[capital-gains]] — the broader tax framework
- [[section-1256-contracts]] — the index-options exemption

## Sources

No dedicated source summary yet — this page restates the statutory mechanics already documented in wash-sale-rules-options and referenced from [[capital-gains]] and tax-loss-harvesting. Add a source citation when a specific reference is ingested.
