---
title: "Cross-Currency Basis Swap"
type: concept
created: 2026-06-13
updated: 2026-06-13
status: good
tags: [forex, derivatives, market-microstructure, liquidity]
domain: [market-microstructure, derivatives]
prerequisites: ["[[carry-trade]]", "[[currency-hedging]]"]
difficulty: advanced
aliases: ["Cross-Currency Basis Swap", "XCCY Basis", "Cross-Currency Basis", "Currency Basis"]
related: ["[[forex]]", "[[carry-trade]]", "[[currency-hedging]]", "[[basis]]", "[[basis-risk]]", "[[bank-for-international-settlements]]"]
---

A **cross-currency basis swap** (XCCY) is a derivative contract in which two parties exchange streams of principal and interest payments denominated in two different currencies, with principal exchanged at the prevailing spot rate at inception and re-exchanged at maturity. The **cross-currency basis** is the spread added to one leg of the swap that measures the deviation from [[covered-interest-rate-parity|covered interest rate parity]] (CIP) — in a frictionless market it would be zero, but in practice it is persistently non-zero and serves as a closely watched gauge of cross-border [[liquidity]] and dollar-funding conditions.

## Overview

A standard cross-currency basis swap works in three stages:

1. **Initial exchange of principal** — At inception, the two parties swap notional amounts in the two currencies at the current spot exchange rate. For example, one party delivers USD and receives EUR of equivalent value.
2. **Periodic interest payments** — Over the life of the swap, each party pays interest on the principal it received, typically referenced to a floating benchmark for that currency (e.g. [[sofr|SOFR]] for USD, [[estr|€STR]] for EUR, [[tona|TONA]] for JPY). One of the two floating legs carries an additional spread — the **cross-currency basis spread** — quoted in basis points. By convention the basis is usually quoted on the non-USD leg.
3. **Re-exchange of principal at maturity** — At the end of the contract, the original principal amounts are exchanged back at the **same** spot rate used at inception (not the maturity-date spot), so neither party bears outright FX translation risk on the notional.

The basis spread is the price that clears supply and demand for synthetic funding in one currency against another. A basis of, say, "−30 bp" on EUR/USD means the EUR-leg payer must accept a benchmark rate reduced by 30 bp — equivalently, dollars obtained synthetically via the swap cost 30 bp more than CIP would imply.

## Covered Interest Rate Parity and the Basis

**Covered interest rate parity** is the no-arbitrage condition stating that the return on a domestic money-market deposit should equal the return on a foreign deposit fully hedged back to the domestic currency using a forward (or FX swap). When CIP holds, the forward FX rate is pinned exactly by the interest-rate differential between the two currencies, and the cross-currency basis is zero.

The **cross-currency basis is the measured deviation from CIP.** In a frictionless world with unlimited, costless arbitrage, any non-zero basis would be instantly arbitraged away. In reality the basis is persistently non-zero — and, for many USD-funded pairs, persistently **negative** — because the arbitrage that should close it is neither free nor unlimited. The main frictions include:

- **USD funding demand** — Non-US banks, corporates, and investors with dollar liabilities or dollar-denominated assets to hedge create structural demand to borrow dollars synthetically, pushing the basis negative.
- **Balance-sheet and regulatory costs** — Post-2008 [[basel-iii|Basel]] rules (leverage ratio, capital and liquidity requirements) make it costly for dealer banks to expand their balance sheets to run the CIP arbitrage. The arbitrage consumes scarce balance-sheet capacity, so dealers demand compensation, and the basis no longer closes to zero.
- **Supply and demand for currency hedging** — Hedgers (e.g. a Japanese pension fund hedging US bond holdings, or a European corporate) are price-takers who pay the basis as a cost; their flows move it.

The key takeaway is that the basis is a **price of intermediation and funding**, not a pure interest-rate phenomenon. It widened structurally after the global financial crisis precisely because the previously near-costless arbitrage became balance-sheet-intensive.

## What the Basis Signals

Because the basis embeds the cost and scarcity of cross-border dollar funding, a **widening (more negative) basis indicates funding stress** — a scramble for dollars. Pronounced episodes of basis widening have historically coincided with broad liquidity events, including the 2008 global financial crisis, the 2011–12 European sovereign-debt crisis, and the March 2020 dash-for-cash at the onset of the COVID-19 shock. In each case the dollar basis blew out (became sharply more negative) as institutions worldwide competed for dollar liquidity.

This makes the cross-currency basis a useful **leading or coincident indicator of liquidity stress**: it often moves before or alongside other stress gauges as funding markets seize up. Central-bank USD swap lines (e.g. those extended by the Federal Reserve to other central banks) are deployed specifically to relieve this stress and compress the basis back toward normal. Monitoring the basis is therefore a way to read the plumbing of the global financial system. See [[basis-risk]] for the related risk that hedges and underlying positions move imperfectly together.

## Relevance to Hedging

For international portfolios, the cross-currency basis is not an abstraction — it is a **real cost or benefit embedded in every currency-hedged position.** An investor who hedges foreign-currency assets back to their home currency pays (or receives) the basis as part of the hedging cost. When the dollar basis is negative, non-US investors hedging USD assets back to their home currency effectively earn a pickup, while US investors hedging foreign assets back to dollars pay an extra cost — and vice versa.

This directly changes the economics of the [[carry-trade]] and of [[currency-hedging]] decisions: the headline interest-rate differential overstates the realisable carry once the basis is netted out, and the attractiveness of hedged-versus-unhedged allocations shifts as the basis moves. **Divergent central-bank policy regimes** — where one central bank tightens while another eases — tend to widen basis differentials by amplifying directional funding and hedging flows.

## Recent Context

The transition away from [[libor|LIBOR]] toward backward-looking, near-risk-free overnight rates reshaped how basis swaps are referenced and priced. Where legacy swaps quoted floating legs against IBOR fixings (e.g. 3-month USD LIBOR vs 3-month EURIBOR), modern contracts reference compounded risk-free rates — [[sofr|SOFR]] (USD), [[estr|€STR]] (EUR), [[sonia|SONIA]] (GBP), and [[tona|TONA]] (JPY). Because these new benchmarks are nearly credit-risk-free and backward-looking (compounded over the period rather than set in advance), the fixing conventions, the observation/payment lags, and the credit/term premium previously bundled into IBOR-based basis quotes had to be re-expressed. This affected both the level of quoted basis spreads and the mechanics of how cash flows are calculated.

## Relevance to Traders

- **Funding-stress monitoring** — The dollar basis is a real-time barometer of cross-border dollar liquidity; a sharp widening flags emerging stress and potential [[risk-off]] episodes.
- **Hedging-cost calculation** — Anyone running hedged international exposure must price the basis into the true cost or benefit of their currency hedge.
- **Relative-value opportunities** — Dislocations in the basis (across tenors, currency pairs, or against funding alternatives) create relative-value trades for desks with balance-sheet capacity to warehouse them.
- **Risk-off signal** — Because basis widening clusters with liquidity crises, it serves as a corroborating signal for de-risking and as input to systematic regime detection.

## Related

- [[forex]]
- [[carry-trade]]
- [[currency-hedging]]
- [[basis]]
- [[basis-risk]]
- [[covered-interest-rate-parity]]
- [[libor]]
- [[sofr]]
- [[bank-for-international-settlements]]

## Sources

Compiled from FX derivatives and funding-market literature and BIS material (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md).
