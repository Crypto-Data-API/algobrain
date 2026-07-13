---
title: "Hedging Strategies"
type: index
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [risk-management, options, derivatives, volatility]
aliases: ["Hedging Strategies", "Portfolio Hedging", "Risk Hedging"]
related: ["[[hedging]]", "[[risk-management-overview]]", "[[options-overview]]", "[[tail-risk-hedging]]", "[[protective-put]]", "[[collar]]"]
---

Hedging strategies are positions taken to offset, cap, or partially neutralize the risk of an existing exposure. Unlike a directional bet, a hedge is deliberately expected to lose money when the core position wins — its job is to reduce drawdown, smooth equity, and survive tail events, not to generate standalone alpha. This page is a hub that catalogs the hedging strategies documented elsewhere in the wiki and gives guidance on when each is appropriate. For the underlying concept, see [[hedging]]; for the broader framework, see [[risk-management-overview]].

## Core trade-off

Every hedge costs something: an explicit premium (buying [[put-option|puts]]), an opportunity cost (capping upside with a [[collar]]), basis risk (hedging one instrument with a correlated other), or carry/roll cost (rolling [[vix-call-spreads|VIX]] structures). The central decision is always *how much certainty you are willing to pay for, and against which scenario.* A hedge that is cheap usually has a flaw — a gap-risk window, basis mismatch, or a payoff that only triggers in a regime you do not actually fear.

## Options-based hedges (defined-risk, on a single book)

- [[protective-put]] — long stock plus a long put. The classic insurance trade: floors downside at the strike while keeping unlimited upside, at the cost of continuous premium drag. See also [[protective-puts]] and [[married-put]] (a protective put opened simultaneously with the stock).
- [[collar]] — protective put financed by selling an OTM call. Cheap or zero-cost protection in exchange for capped upside; the workhorse hedge for concentrated single-stock or low-basis holdings. See also [[collar-strategy]].
- [[covered-call]] — not a true hedge but a partial buffer: the call premium offsets a modest decline while capping upside. Useful as a yield-enhancing soft hedge in flat-to-mildly-bearish regimes.
- [[options-hedging]] — general options-based hedging techniques and Greeks-aware overlays.
- [[delta-hedging]] — dynamically trading the underlying to neutralize directional (delta) exposure of an options book; the foundation of market-making and structured-product risk management.

## Portfolio and tail-risk hedges (whole-book overlays)

- [[tail-risk-hedging]] — systematic far-OTM put or VIX-convexity overlay designed to pay off convexly in crashes; chronically negative carry, so sizing and financing discipline are everything.
- [[convex-tail-hedge-arbitrage]] — exploiting mispricing in the tail-hedge complex itself.
- [[cppi|CPPI]] — Constant Proportion Portfolio Insurance: a rules-based allocation that mechanically shifts between risky and safe assets to floor portfolio value without options.
- [[vix-call-spreads]] — defined-cost volatility hedges using VIX options; cheaper than outright VIX calls but with capped convexity.
- [[trend-plus-tail-hedge]] — pairing a [[trend-following-cta|trend]] sleeve (which tends to make money in sustained selloffs) with an explicit tail hedge for the gap risk trend-following misses.

## Relative-value and cross-asset hedges (offset risk with another position)

- [[pairs-trading]] — long one name, short a correlated peer, isolating the spread and hedging out shared (sector/market) risk.
- [[cross-chain-contagion-hedge]] — crypto-native cross-asset hedge against contagion across chains/protocols.

## When to use which

| Situation | Preferred hedge |
|-----------|-----------------|
| Concentrated single stock, want to keep it | [[collar]] or [[protective-put]] |
| Broad equity book, fear a crash, can tolerate carry | [[tail-risk-hedging]] / [[vix-call-spreads]] |
| Want protection with zero premium outlay | [[collar]] (zero-cost) or [[cppi|CPPI]] |
| Mildly bearish, want to keep harvesting yield | [[covered-call]] |
| Isolate stock-picking skill, remove market beta | long-short-equity / [[pairs-trading]] |
| Running an options book | [[delta-hedging]] |
| Trend sleeve already on, plug the gap-risk hole | [[trend-plus-tail-hedge]] |

## Key principles

1. **Hedge the scenario you fear, not the one that is easy to hedge.** Match the payoff (linear vs convex, slow grind vs gap) to the actual risk.
2. **Account for the full cost** — premium, opportunity cost, basis risk, and roll/carry. See [[breakeven-cost-bps]] thinking in each strategy page.
3. **Watch basis risk.** A correlated hedge (index puts on a single-stock book, BTC against an altcoin book) can fail exactly when correlations break.
4. **Size for the regime.** Tail hedges bleed in calm markets; over-hedging guarantees underperformance. See [[position-sizing]] and [[risk-budgeting]].
5. **Define an exit.** A hedge held forever is just a drag; decide in advance when to monetize, roll, or remove it.

## Related

- [[hedging]] — the underlying concept
- [[risk-management-overview]]
- [[options-overview]]
- [[correlation]], [[beta]] — what makes a hedge work or fail
- [[delta-hedging]], [[gamma-risk]], [[theta-decay]] — Greeks behind options hedges

## Sources

- Hull, John C. *Options, Futures, and Other Derivatives* (10th ed.) — chapters on hedging with options and dynamic hedging.
- Natenberg, Sheldon. *Option Volatility and Pricing* — protective puts, collars, and risk-defined structures.
- CBOE, "Hedging with Options" educational material (cboe.com).
