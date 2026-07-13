---
title: "Total Return Swap (TRS)"
type: concept
created: 2026-04-26
updated: 2026-06-11
status: good
tags: [derivatives, otc, prime-broker, leverage, equity, credit]
aliases: ["TRS", "Total Return Swap", "Total-Rate-of-Return Swap", "Equity Total Return Swap"]
related: ["[[contract-for-difference]]", "[[prime-broker]]", "[[archegos-blowup-2021]]", "[[counterparty-risk]]"]
domain: [derivatives, market-microstructure]
prerequisites: ["[[derivatives]]", "[[otc-markets]]"]
difficulty: intermediate
---

# Total Return Swap (TRS)

A **Total Return Swap (TRS)** is an OTC bilateral derivative in which one party (the *receiver* / "synthetic long") receives the total economic return of a reference asset — price appreciation plus income — while the other party (the *payer* / dealer) holds the actual asset on its balance sheet and receives a financing rate (typically SOFR + spread) from the receiver. TRS can reference single equities, baskets, indices, bonds, loans, or commodities. Equity TRS is the dominant structure in synthetic prime brokerage and was the central instrument in the [[archegos-blowup-2021|Archegos blow-up]].

## Cash-Flow Mechanics

For a single-stock equity TRS on Stock X, notional $100M, 1-year tenor:

| Party | Pays | Receives |
|-------|------|----------|
| Receiver (Archegos / hedge fund) | Financing: SOFR + 50bp on $100M | Stock X total return (price Δ + dividends) |
| Payer (Credit Suisse / prime broker) | Stock X total return | Financing: SOFR + 50bp on $100M |

The payer **buys $100M of Stock X** in the cash market to hedge its exposure. The receiver posts only **initial margin** — typically 10-25% — making this a leveraged synthetic position.

If Stock X goes up 10% (and pays no dividend), the receiver gets $10M, pays ~$5.5M financing on the year, net ~$4.5M on a $10-25M margin = 18-45% return on capital.

If Stock X goes down 10%, the receiver pays $10M plus financing — wiping out the 10-25% margin. Variation margin is called.

## Why TRS Exists (Investor Side)

1. **Leverage.** 4-10x leverage with no securities-loan friction.
2. **Cross-border tax efficiency.** UK investor accessing US equity dividends via TRS receives a single OTC payment rather than dealing with US withholding tax + treaty mechanics.
3. **Disclosure avoidance.** TRS is a derivative — until the SEC's proposed Rule 10B-1 (2022, not yet finalized as of 2026), large TRS positions did *not* trigger 13D/13G filings, even when economic ownership exceeded the 5% threshold. This was a structural feature exploited by Hwang for ViacomCBS (~20% effective stake, zero public disclosure) and by bill-ackman for Herbalife earlier.
4. **Short-side TRS.** "Pay-fixed" TRS gives synthetic short exposure without locating borrow.

## Why TRS Exists (Bank Side)

1. **Financing margin.** SOFR + 50-150 bp on multi-billion notional.
2. **Cross-sell:** TRS clients also use bank for execution, custody, FX, securities lending.
3. **Balance-sheet rental.** Bank collects fee for committing balance sheet without taking directional risk (perfectly hedged).
4. **Information edge.** Bank sees client positioning and trading patterns.

## TRS in [[archegos-blowup-2021|Archegos]]

The Archegos case is the modern-textbook TRS disaster:

- **8+ prime brokers**, each writing TRS on overlapping single-name positions.
- **Initial margin as low as 10%** (Credit Suisse) on concentrated single-stock exposures — vs typical 25-50% post-LTCM norms.
- **No 13D/13G** filed by Archegos — its ~20% effective ViacomCBS position invisible to public markets.
- **Multi-bank fragmentation** — no single counterparty saw aggregate concentration.
- **Cross-default cascade** when ViacomCBS secondary triggered margin calls Hwang couldn't meet.

## Variation: Contract for Difference (CFD)

A [[contract-for-difference|CFD]] is functionally near-identical to TRS but historically retail-oriented (UK, EU, AUS) and subject to different regulatory treatment. Banned for retail in the US (CFTC). Both TRS and CFD share the disclosure-avoidance feature.

## Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Counterparty | Bank default leaves receiver holding nothing | ISDA collateralisation, multiple counterparties |
| Margin/wrong-way | Concentrated TRS book moves against receiver, margin breach | Robust IM sizing, daily VM |
| Disclosure | Use of TRS to manipulate underlying via hidden buying | SEC Rule 10B-1 (proposed 2022) |
| Liquidity | Underlying becomes illiquid when bank tries to hedge | Position limits per name |
| Concentration | Multiple TRS receivers all long same name | Cross-client concentration monitoring |
| Cross-counterparty fragmentation | One client at multiple banks | Industry-shared counterparty database (post-Archegos discussion) |

## Regulatory Landscape (post-Archegos)

- **SEC Rule 10B-1 (proposed Dec 2021):** Large security-based-swap positions (>$300M for single-name) would trigger public disclosure. Stalled in finalization as of 2026.
- **FSB Counterparty Credit Risk Guidance (2023):** Banks must size IM to concentrated tail risk, not just historical VaR.
- **Basel III FRTB:** Enhanced capital charges for TRS book risk-weighted assets.
- **ISDA Multi-Dealer Default Management Protocol (2022+):** Standardized cooperative-unwind framework to break the prisoner's-dilemma at default.

## Use Cases Across Asset Classes

| Underlying | Primary Use | Typical Receiver |
|-----------|-------------|------------------|
| Single equity | Synthetic prime brokerage | Hedge fund, family office |
| Equity basket | Long/short factor exposure | Quant fund |
| Loan / leveraged loan | Credit access without funding | Insurance, pension |
| Bond / sovereign | Yield enhancement | EM credit fund |
| Commodity | Cross-border price exposure | Commodity trading house |
| Crypto | Yield/exposure without custody | Crypto credit fund |

## Sources

- ISDA, *2002 ISDA Master Agreement* and definitions library.
- Paul Weiss, *Report on Archegos for Credit Suisse* (July 2021).
- SEC, *Proposed Rule 10B-1: Position Reporting of Large Security-Based Swap Positions* (December 2021).
- Federal Reserve, *Senior Credit Officer Opinion Survey* (quarterly TRS disclosures).
- BIS Quarterly Review, OTC derivatives statistics.

## Related

[[contract-for-difference]] · [[prime-broker]] · [[archegos-blowup-2021]] · [[bill-hwang]] · [[counterparty-risk]] · capital-structure-arbitrage · [[block-trade-flipping-arbitrage]] · [[prime-broker-cascade-trading]] · [[ltcm-collapse-1998]]
