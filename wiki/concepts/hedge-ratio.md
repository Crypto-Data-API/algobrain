---
title: "Hedge Ratio"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [risk-management, derivatives, options, pairs-trading, correlation]
aliases: ["Hedge Ratio", "Optimal Hedge Ratio", "Minimum Variance Hedge Ratio"]
related: ["[[hedging]]", "[[delta-hedging]]", "[[delta-neutral]]", "[[pairs-trading]]", "[[beta]]", "[[correlation]]", "[[statistical-arbitrage]]", "[[beta-hedging]]", "[[basis-risk]]", "[[futures]]", "[[gamma]]", "[[currency-hedging]]", "[[transaction-costs]]", "[[slippage]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[hedging]]", "[[correlation]]"]
difficulty: intermediate
---

The **hedge ratio** is the proportion of a position that is offset by a hedging instrument — the number of units of the hedge held per unit of the exposure being protected. Choosing it correctly is the central quantitative problem in [[hedging]]: too small a hedge leaves residual risk, too large a hedge over-corrects and introduces opposite exposure. The optimal hedge ratio minimises the variance of the combined position.

## Definitions

There are two common framings:

1. **Position hedge ratio** — the fraction of an exposure that is hedged. A portfolio with $1M of stock and $600K of offsetting index short has a 60% hedge ratio.
2. **Minimum-variance (optimal) hedge ratio** — the number of hedge units per exposure unit that minimises portfolio variance.

## The Minimum-Variance Formula

For an exposure with returns *S* hedged by an instrument with returns *F*, the variance-minimising hedge ratio is:

**h\* = ρ × (σ_S / σ_F) = Cov(S, F) / Var(F)**

where ρ is the [[correlation]] between the two return series, and σ_S and σ_F are their standard deviations. This is identical to the slope coefficient (β) of a regression of the exposure's returns on the hedge's returns — so **the optimal hedge ratio is the OLS [[beta]] of exposure-on-hedge**. The fraction of risk eliminated by the optimal hedge is **ρ²**; a hedge instrument correlated 0.9 with the exposure removes 81% of variance, leaving 19% as irreducible [[basis-risk|basis risk]].

### Worked example: minimum-variance hedge

A jet-fuel buyer wants to hedge with crude-oil [[futures]] (there is no liquid jet-fuel future, so this is a **cross-hedge** with basis risk). From historical data:

- σ_S (jet-fuel price change) = 4.0% (monthly)
- σ_F (crude-oil futures change) = 5.0% (monthly)
- ρ (correlation between the two) = 0.80

Then:

**h\* = 0.80 × (4.0 / 5.0) = 0.64**

So the buyer hedges **64%** of the dollar exposure with crude futures — not 100%, because crude is more volatile than jet fuel and imperfectly correlated. The hedge removes ρ² = 0.80² = **64% of the variance**, leaving 36% as basis risk. If the firm needs to cover 1,000,000 gallons and each futures contract covers 42,000 gallons (1,000 barrels), the **number of contracts** is:

contracts = h\* × (exposure value ÷ futures contract value)

If the exposure is worth $3.0M and one futures contract controls $80,000 of crude, then contracts = 0.64 × (3,000,000 ÷ 80,000) = 0.64 × 37.5 ≈ **24 contracts**.

## Hedge Ratio by Context

| Context | What the hedge ratio is | Rebalancing driver |
|---------|-------------------------|--------------------|
| **Options** | The option's [[delta-hedging\|delta]] — shares to short per long call to be locally [[delta-neutral]] | Delta changes with price ([[gamma]]) → rebalance continuously |
| **Futures / commodity** | h\* contracts to sell per unit of physical exposure, adjusted for contract size and basis | Volatilities and basis drift |
| **Equity / [[beta-hedging\|beta hedging]]** | Index futures notional = portfolio value × portfolio [[beta]] | Beta drifts; re-estimate periodically |
| **[[pairs-trading]] / [[statistical-arbitrage]]** | Cointegration coefficient / regression beta of stock B on stock A | Relationship breaks → re-estimate the spread |
| **[[currency-hedging\|Currency]]** | Fraction of foreign exposure hedged via forwards (often 0/50/100%) | Strategic, not tactical |

### Worked example: beta hedge

A portfolio manager holds **$10M** of stocks with a portfolio [[beta]] of **1.2** versus the S&P 500 and wants to neutralise market risk to isolate stock-specific alpha. The required short in index futures is:

notional to short = portfolio value × beta = $10M × 1.2 = **$12M**

If one E-mini S&P 500 futures contract controls, say, $250,000 of index exposure, the manager shorts $12M ÷ $250,000 ≈ **48 contracts**. This makes the book [[delta-neutral|market-neutral]] in beta terms; what remains is the manager's idiosyncratic stock selection (plus residual basis and any beta-estimation error).

## Estimation Pitfalls

The hedge ratio is estimated from historical data, so it inherits estimation error and is **non-stationary** — correlations and volatilities drift, and a ratio fitted in a calm regime can be badly wrong in a crisis when correlations converge toward 1. Practitioners re-estimate on rolling windows, shrink the estimate toward a prior, or use dynamic models (e.g., rolling-beta or GARCH-based conditional covariance). Over-fitting a precise ratio to a short sample is a common [[failure-modes|failure mode]].

## Trading Relevance

The hedge ratio is where risk management meets execution cost: a higher rebalancing frequency keeps the realised hedge ratio close to optimal but accumulates [[transaction-costs]] and [[slippage]], while a static ratio drifts off-target as relationships change. Every delta-hedging desk, pairs-trading book, and beta-neutral fund is implicitly running a continuous decision about how aggressively to track the moving optimal ratio versus how much trading cost to pay — the **gamma-versus-cost tradeoff**. Mis-estimating the ratio is one of the most common reasons "hedged" positions blow up in stress, because residual exposure and basis risk are largest exactly when correlations break.

## Common Pitfalls

- **Assuming a 1:1 hedge is "safe"** — full notional hedging is only optimal when ρ = 1 and σ_S = σ_F; otherwise it over- or under-hedges.
- **Stale estimates** — a hedge ratio from a calm sample understates the residual risk that appears when correlations spike toward 1 in a crisis.
- **Ignoring basis risk** — even a perfectly sized cross-hedge leaves (1 − ρ²) of variance; basis can move violently when the hedge and exposure decouple.
- **Over-rebalancing** — chasing the moving optimal ratio tick-by-tick can cost more in [[transaction-costs]] and [[slippage]] than the residual risk it removes.
- **Contract-size rounding** — you can only trade whole contracts; rounding leaves a small permanent mismatch, larger for small books.

## Related

- [[hedging]] — the broader practice the ratio parameterises
- [[delta-hedging]] — option delta is a hedge ratio
- [[delta-neutral]] — the target state a hedge ratio aims at
- [[beta-hedging]] — neutralising market risk with portfolio beta
- [[pairs-trading]] — hedge ratio as cointegration/regression coefficient
- [[beta]] — the optimal hedge ratio is a regression beta
- [[correlation]] — drives how much risk the hedge can remove (ρ²)
- [[basis-risk]] — the irreducible residual a cross-hedge leaves
- [[currency-hedging]] — hedge ratio applied to FX exposure
- [[statistical-arbitrage]] — uses estimated hedge ratios to build stationary spreads

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* — minimum-variance hedge ratio derivation and futures hedging (the jet-fuel/crude cross-hedge is the canonical Hull example).
- Sheldon Natenberg, *Option Volatility and Pricing* — delta as the option hedge ratio.
- Ernest Chan, *Algorithmic Trading* — hedge ratios via regression and cointegration in pairs/stat-arb.
