---
title: "Settlement Risk"
type: concept
created: 2026-06-13
updated: 2026-06-17
status: good
tags: [risk-management, forex, market-microstructure]
domain: [risk-management, market-microstructure]
difficulty: intermediate
aliases: ["Settlement Risk", "Herstatt Risk", "FX Settlement Risk", "Principal Risk"]
related: ["[[forex]]", "[[counterparty-risk]]", "[[cross-currency-basis-swap]]", "[[bank-for-international-settlements]]"]
---

Settlement risk is the risk that one party to a transaction delivers the asset or payment it owes but does not receive the counter-value it is due, because the two legs of the trade settle at different times. In foreign exchange it is also called **Herstatt risk**, after the bank failure that first made the danger concrete, and it is the largest single risk in the FX market by gross exposure.

## Overview

A spot FX trade exchanges one currency for another. Because the two currencies settle in different national payment systems operating in different time zones, there is usually a window in which one party has irrevocably paid away the currency it sold but has not yet received the currency it bought. If the counterparty fails during that window, the first party can lose the full **principal** amount, not merely the change in market value. This makes settlement risk a *principal risk*, distinct from the smaller **replacement-cost risk** captured by mark-to-market [[counterparty-risk]].

## The Herstatt Episode

On **26 June 1974**, German regulators withdrew the banking licence of Bankhaus Herstatt and ordered it into liquidation during the afternoon, Central European Time. Counterparties had already paid Deutsche Marks to Herstatt earlier that day, but because New York was several hours behind, the corresponding US dollar payments had not yet been made when the bank was shut. Those dollar legs were never paid. The episode gave the risk its name and, decades later, motivated the construction of CLS. Other failures — Drexel Burnham (1990), BCCI (1991), and Barings (1995) — reinforced the lesson.

## Settlement Cycles: T+1 and T+2

The exposure window is bounded by the settlement cycle — the lag between trade date (T) and the date value actually changes hands.

| Market | Cycle | Notes |
|---|---|---|
| Spot [[forex]] (most pairs) | **T+2** | Two business days; the standard for EUR/USD, GBP/USD, etc. |
| USD/CAD spot FX | **T+1** | Shorter because both legs share North American business hours |
| US equities & corporate bonds | **T+1** | Shortened from T+2 in **May 2024** (SEC rule) |
| US Treasuries | **T+1** | Long-standing |
| Chinese A-shares | **T+1** | No same-day round-trip (see shanghai-composite) |

Shortening the cycle narrows the window in which a counterparty can fail before delivering, which is one of the explicit motivations behind moves like the 2024 US shift to T+1. It does not eliminate the *principal* exposure, however — only a payment-versus-payment mechanism does that.

## Delivery-versus-Payment and Payment-versus-Payment

The structural cure for settlement risk is to make the two legs conditional on each other so neither can happen alone:

- **Delivery-versus-payment (DvP)** — used in securities settlement: the security transfers if and only if cash transfers. Central securities depositories (e.g., DTCC in the US, Euroclear/Clearstream in Europe) operate DvP.
- **Payment-versus-payment (PvP)** — the FX analogue: currency A pays if and only if currency B pays. CLS is the dominant PvP utility.

## Why It Persists

Settlement risk arises from **asynchronous settlement**: the absence of a mechanism guaranteeing that the receiving leg happens if and only if the paying leg happens. The longer the gap between paying and receiving — and the more time zones a currency pair straddles — the larger the exposure. BIS analysis has repeatedly found that a material share of FX turnover still settles without full protection, particularly in currencies and products outside centralized settlement.

## Mitigation

- **Payment-versus-payment (PvP)** — the structural fix: both legs settle simultaneously or not at all. CLS is the dominant PvP utility, settling 18 major currencies on a PvP basis.
- **Multilateral netting** — settling only net obligations per currency rather than every gross trade dramatically shrinks the payment values at risk (CLS reports funding reductions on the order of ~96%).
- **Bilateral netting agreements** — ISDA and CLS-style master agreements reduce gross exposures between two counterparties.
- **Continuous / shortened settlement cycles** — reducing the time between trade and final settlement narrows the window.
- **Credit limits and monitoring** — capping intraday exposure to any single counterparty.

## Crypto Atomic Settlement: A Contrast

Blockchain settlement reframes the problem. An **atomic swap** uses a hash time-locked contract (HTLC) or an on-chain DvP so that both legs execute in a single transaction or neither does — eliminating the asynchronous window that creates Herstatt risk by construction. On a single chain, an exchange of token A for token B can be made truly atomic. **Crypto's settlement risk migrates elsewhere**, however:

- **Settlement finality is probabilistic, not instant** — a Bitcoin transaction is conventionally treated as final after ~6 confirmations (~60 minutes); reorganizations can in principle reverse it.
- **Centralized exchanges reintroduce principal risk** — depositing assets on a custodial venue means trusting it to deliver, exactly the exposure that felled [[ftx|FTX]] in 2022. Atomic settlement only protects on-chain, not on a CEX's internal ledger.
- **Cross-chain bridges** recreate an asynchronous gap and have been a leading source of hacks.

Atomic, programmable settlement is the conceptual endpoint that proposals like tokenized-deposit and wholesale-CBDC PvP systems are trying to bring to traditional finance.

## Relevance to Traders

Settlement risk is mostly borne by banks, prime brokers, and institutional desks rather than retail traders, but it shapes the market every trader uses: it is a real component of [[transaction-cost-modeling|transaction costs]], it concentrates flow through PvP utilities, and it explains why counterparty selection and venue/settlement arrangements matter at scale. It is also a live consideration for emerging-market and exotic currency pairs that fall outside CLS-eligible settlement, and — in crypto — for anyone holding assets on a custodial exchange rather than self-custody.

## Related

- [[forex]] — where settlement risk is largest
- [[counterparty-risk]] — the broader category; settlement risk is its principal-loss extreme
- [[bank-for-international-settlements]] — author of the definitive surveys on FX settlement risk
- [[cross-currency-basis-swap]] — funding/settlement frictions also drive the cross-currency basis

## Sources

_Compiled from BIS publications on FX settlement risk and CLS Group documentation (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md)._
