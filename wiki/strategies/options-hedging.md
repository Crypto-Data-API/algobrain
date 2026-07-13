---
title: "Options Hedging"
type: index
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, risk-management, volatility, hedging]
aliases: ["Options Hedging", "Hedging with Options", "Option Overlays"]
related: ["[[hedging-strategies]]", "[[protective-puts]]", "[[delta-hedging]]", "[[risk-management]]", "[[options]]", "[[implied-volatility]]"]
---

**Options hedging** uses option contracts to reduce or reshape the risk of an existing position or portfolio. Unlike a static stop-loss, an option overlay caps downside while keeping upside, and its cost (the premium) is known in advance. This page is a hub indexing the wiki's option-based hedging techniques; it is not a single strategy. For non-option hedges (futures, pairs, inverse ETFs), see [[hedging-strategies]].

## How option hedges work

A long option is a one-sided insurance contract: a long put pays off when the underlying falls, a long call pays off when it rises. Because the most you can lose on a long option is the premium, options let you *truncate* a return distribution rather than merely scale it down. The trade-off is **negative carry** — premium decays via [[theta-decay]], so a permanently-on hedge bleeds money in calm markets. Effective hedging is therefore about *when*, *how much*, and *at what strike* to hedge, not whether to own protection forever.

The two structural decisions are:
- **Cost vs. coverage** — outright long puts give clean convexity but cost the most; spreads and collars cheapen the hedge by selling away tail or upside.
- **Single-name vs. index** — hedging the whole book with [[spx-puts|index puts]] is cheaper per unit of beta than hedging each name, but leaves idiosyncratic and basis risk.

## Catalog of option hedges

### Downside protection (long premium)
- [[protective-puts]] — buy a put against a long stock position; classic insurance, full convexity, highest carry.
- [[long-put]] — outright bearish/hedging put, the building block of most downside overlays.
- [[5-percent-otm-put-overlay]] — systematic out-of-the-money put overlay sized at ~5% below spot to cut cost while retaining crash protection.
- [[spx-puts]] — index puts to hedge a diversified equity book by beta rather than name-by-name.
- [[put-tree]] — a put ratio/tree structure that cheapens protection by financing it with extra short puts (introduces a sweet-spot and re-introduced tail risk).

### Cheaper, capped protection (spreads & collars)
- [[put-spread]] — bear put (debit) spread: buy a near put, sell a farther put; defined cost, capped payout, good for a bounded down-move view.
- **Collar** — combine [[protective-puts]] with selling an upside call ([[covered-calls]]) to finance the put; caps both tails, often near-zero cost.

### Volatility / tail hedges
- [[vix-calls]] — long VIX calls that spike in value during volatility shocks; convex but heavy negative carry.
- [[vix-call-spreads]] — VIX call spreads that cap the convexity to reduce carry.

### Dynamic hedging
- [[delta-hedging]] — continuously trade the underlying to neutralize an option book's directional exposure; the dealer/market-maker approach, also used to manage hedge cost dynamically.

### Income overlays that also reduce risk
- [[covered-calls]] — selling calls against stock lowers cost basis and cushions small declines (a partial, capped hedge, not true downside insurance).
- [[credit-spread]] — defined-risk premium selling that can offset book risk in range-bound regimes.

## When to use which

| Goal | Best fit |
|------|----------|
| Full crash insurance, willing to pay carry | [[protective-puts]], [[spx-puts]] |
| Bounded down-move, lower cost | [[put-spread]] |
| Hedge at near-zero cash cost, accept capped upside | Collar (puts + [[covered-calls]]) |
| Protect against a volatility spike, not just price | [[vix-calls]], [[vix-call-spreads]] |
| Cheapen protection, accept a tail "hole" | [[put-tree]], [[5-percent-otm-put-overlay]] |
| Neutralize an option book continuously | [[delta-hedging]] |

General guidance: hedge *before* implied volatility spikes (protection is cheapest when nobody wants it), size hedges to the beta-adjusted dollar exposure you actually need to protect, and prefer spreads/collars over outright long puts when carry would erode returns in calm regimes.

## Related
- [[hedging-strategies]] — broader (non-option) hedging hub
- [[risk-management]]
- [[options]] / [[options-pricing]]
- [[implied-volatility]] / [[volatility-risk-premium]]
- [[theta-decay]] / [[gamma-risk]]
- [[tail-risk-hedging]]

## Sources
- The Options Industry Council (OIC), "Strategies" — https://www.optionseducation.org/strategies
- CBOE, "VIX Index and Volatility Products" — https://www.cboe.com/tradable_products/vix/
- Hull, J. C., *Options, Futures, and Other Derivatives* — chapters on hedging with options and dynamic (delta) hedging.
