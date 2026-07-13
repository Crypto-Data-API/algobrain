---
title: "Covered Interest Rate Parity"
type: concept
created: 2026-06-13
updated: 2026-06-17
status: good
tags: [forex, derivatives, market-microstructure]
domain: [market-microstructure, derivatives]
prerequisites: ["[[forex]]"]
difficulty: advanced
aliases: ["Covered Interest Rate Parity", "CIP", "Covered Interest Parity"]
related: ["[[cross-currency-basis-swap]]", "[[carry-trade]]", "[[forex]]", "[[currency-hedging]]", "[[uncovered-interest-rate-parity]]", "[[arbitrage]]"]
---

Covered interest rate parity (CIP) is the no-arbitrage condition stating that the interest-rate differential between two currencies must equal the percentage difference between their forward and spot exchange rates. It is "covered" because the future exchange rate is locked in with a forward contract, removing currency risk. When CIP holds, borrowing domestically and borrowing abroad-then-hedging produce identical financing costs.

## The Relationship

For domestic rate $r_d$, foreign rate $r_f$, spot rate $S$ and forward rate $F$ (both quoted as domestic currency per unit of foreign currency), CIP requires:

```
F / S = (1 + r_d) / (1 + r_f)
```

Equivalently, the forward premium or discount on the foreign currency offsets the interest-rate gap. If this did not hold, an arbitrageur could borrow in the cheap currency, convert at spot, invest in the other currency, and sell the proceeds forward for a riskless profit.

## Worked Example

Suppose 1-year USD rate $r_d = 5\%$, 1-year EUR rate $r_f = 3\%$, and spot $S = 1.10$ USD per EUR. CIP says the fair 1-year forward is:

```
F = S × (1 + r_d) / (1 + r_f) = 1.10 × 1.05 / 1.03 ≈ 1.1214
```

The euro trades at a **forward premium** (1.1214 > 1.10) precisely because euro rates are lower — the forward compensates the holder for giving up the higher dollar yield. An investor who wants to hold euros risk-free earns the same 5% whether they keep dollars or convert, invest at 3%, and sell euros forward at 1.1214.

### The Arbitrage That Enforces It

If the actual 1-year forward were quoted *too cheap* (say 1.115), a desk could run a riskless [[arbitrage]]:

1. Borrow $1.00 at 5% → owe $1.05 in a year.
2. Convert to €0.909 at spot 1.10.
3. Invest at 3% → €0.9367 in a year.
4. Sell €0.9367 forward at the mispriced 1.115 → receive $1.0444... versus the $1.05 owed.

In this example the discrepancy direction would flip the profit, but the mechanism is symmetric: any deviation between the quoted forward and the CIP-implied forward is a textbook locked-in profit, which is why CIP held almost exactly before 2008.

## Covered vs Uncovered

- **Covered** parity uses the *forward* rate and is, in principle, a pure arbitrage condition — it should always hold absent frictions.
- **[[uncovered-interest-rate-parity|Uncovered]]** parity (UIP) replaces the forward with the *expected future spot* rate and is a much weaker, empirically violated proposition. The persistent failure of UIP is precisely what makes the [[carry-trade]] profitable on average.

## CIP Deviations and the Basis

In a frictionless market CIP holds exactly. In practice, since the 2008 financial crisis, persistent CIP **deviations** have appeared and the [[cross-currency-basis-swap|cross-currency basis]] — the spread that must be added to make the two financing routes equal — is the direct measure of that deviation. A non-zero basis (typically reflecting a premium to obtain US dollars synthetically) is attributed to:

- **Dollar funding demand** — scarcity of USD funding pushes up the cost of borrowing dollars via FX swaps.
- **Dealer balance-sheet and regulatory costs** — post-crisis [[bank-for-international-settlements|Basel]] capital and leverage rules make the arbitrage costly for banks, so it is not fully traded away.
- **Hedging supply and demand** — large, persistent currency-hedging flows from corporates, insurers, and asset managers move the basis.

These deviations widen sharply during funding stress (2008, the 2011–12 euro crisis, March 2020) and exhibit a recurring **quarter-end and year-end** pattern, when banks shrink balance sheets for regulatory reporting and the cost of providing the arbitrage spikes. Typical magnitudes are tens of basis points (e.g., the JPY and EUR bases versus USD running roughly −20 to −60 bps for much of the 2015–2020 period), wide enough to matter for hedgers but too narrow, after balance-sheet costs, to be worth arbitraging away.

### Why the Arbitrage Is Not Riskless Anymore

The pre-crisis assumption was that CIP arbitrage uses a bank's "free" balance sheet. Post-crisis it does not:

- **Leverage ratio** — the [[bank-for-international-settlements|Basel III]] leverage ratio charges capital against the gross size of the swap position regardless of its low risk, so even a near-riskless trade consumes a scarce, costly resource.
- **Counterparty and credit limits** — internal limits cap how much a desk can deploy.
- **Funding asymmetry** — the entity that *has* the dollars demands a premium because dollar funding is structurally scarce outside the US banking system.

The result is a market that is arbitraged *up to* the marginal balance-sheet cost and no further — a persistent, non-zero basis rather than a single fleeting mispricing.

## Relevance to Traders

CIP underpins the pricing of FX forwards, swaps, and [[currency-hedging|hedged]] international positions. Understanding it explains why hedging foreign assets is not free, why the [[cross-currency-basis-swap|basis]] is a useful funding-stress signal, and why the [[carry-trade]] is a bet against *uncovered* parity rather than the covered version.

## Related

- [[cross-currency-basis-swap]] — the instrument and spread that measure CIP deviations
- [[carry-trade]] — exploits the failure of uncovered (not covered) parity
- [[currency-hedging]] — its cost is governed by CIP and the basis
- [[uncovered-interest-rate-parity]] — the weaker, empirically violated counterpart
- [[forex]] — the market in which these relationships are priced

## Sources

_Compiled from BIS and academic literature on covered interest parity and the cross-currency basis (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md)._
