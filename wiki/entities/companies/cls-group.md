---
title: "CLS Group"
type: entity
created: 2026-06-13
updated: 2026-06-13
status: good
tags: [forex, market-microstructure, risk-management]
entity_type: company
founded: 1997
headquarters: "Lucerne, Switzerland (parent: CLS Group Holdings AG); New York (operating bank: CLS Bank International)"
website: "https://www.cls-group.com"
aliases: ["CLS", "CLS Bank", "Continuous Linked Settlement", "CLSSettlement"]
related: ["[[forex]]", "[[bank-for-international-settlements]]", "[[settlement-risk]]", "[[last-look]]", "[[transaction-cost-modeling]]"]
---

CLS Group is the financial-market-infrastructure utility that settles the world's [[forex|foreign exchange]] trades on a payment-versus-payment (PvP) basis, eliminating the risk that one party to a currency trade pays out its leg without receiving the offsetting leg. Operating through its CLSSettlement service, CLS is owned by the world's largest FX dealing banks and is regulated as a systemically important financial-market utility. It went live in 2002 and has become the central settlement layer for institutional FX, processing on the order of several trillion US dollars of payment instructions every business day.

## Overview

CLS ("Continuous Linked Settlement") is a multi-currency cash settlement system that removes the central credit hazard of the FX market: that the two currency legs of a single trade settle at different times, in different time zones, across different national payment systems. Its flagship service, CLSSettlement, links to the real-time gross settlement (RTGS) systems of each eligible currency's central bank and settles both legs of an FX transaction *simultaneously* on its own books. If one leg cannot be funded, neither leg settles — the defining property of payment-versus-payment (PvP).

CLS is structured as a member-owned utility. It is owned by, and serves, the major global banks active in FX — on the order of 70-plus shareholder and direct settlement member institutions — making it closer to a market cooperative than a commercial vendor. Because so much of the interbank FX market clears through it, CLS is designated systemically important and is overseen by a cooperative arrangement of central banks led by the US Federal Reserve, reflecting the predominance of the US dollar in FX settlement.

## Herstatt / Settlement Risk

The risk CLS was built to neutralize is named after a single 1974 event. On 26 June 1974, the German regulator (Bundesaufsichtsamt) withdrew the banking licence of Bankhaus Herstatt and ordered it into liquidation during the German business day. Counterparties had already paid Deutsche Mark to Herstatt that morning; but because New York was several hours behind, Herstatt's correspondent stopped making the offsetting US dollar payments. Those counterparties had irrevocably delivered one currency and never received the other. This asynchronous, time-zone-driven loss became the textbook case of [[settlement-risk]], still widely called **Herstatt risk**.

[[settlement-risk|Settlement risk]] in FX is the risk that a party delivers the currency it sold but does not receive the currency it bought, because the two legs settle at different times and across different payment systems with no linkage between them. In a worst case it is principal risk: the full value of the trade can be lost, not merely a mark-to-market difference. CLS solves this by settling both legs of each trade simultaneously on a PvP basis — a payout in one currency happens only if and when the corresponding receipt in the other currency is funded. Either both legs settle or neither does, which structurally removes the Herstatt exposure for trades submitted to CLSSettlement.

## How CLSSettlement Works

CLSSettlement operates a daily settlement cycle with a defined funding-and-settlement window. Members submit matched payment instructions for their FX trades; CLS then calculates each member's net funding obligation per currency and settles the underlying trades gross on a PvP basis across linked accounts at the relevant central banks.

Two mechanisms make this efficient:

- **Multilateral netting of funding.** Although each individual trade settles gross and PvP, members only need to *fund* their net position in each currency. Across the system this collapses a very large gross value of instructions into a small net value to be paid in — CLS reports that this multilateral netting reduces the funding required to settle to roughly 4% of the underlying gross value, i.e. on the order of a **~96% reduction** in the liquidity members must move. This is the core liquidity benefit that makes the service economic.
- **A time-zone-overlapping settlement window.** Settlement and the associated pay-ins occur within a roughly **5-hour window** each morning (Central European Time), chosen because it is the period in which the RTGS systems of European, Asian-Pacific and American business hours overlap. That overlap is what makes simultaneous, real-time PvP settlement across multiple currencies operationally possible.

Members access CLSSettlement directly as settlement members, while a much larger population of banks, funds, corporates and other institutions participate indirectly as **third-party** users through a settlement member.

## Eligible Currencies

CLSSettlement currently settles **18** of the most actively traded currencies. These include the major reserve and trading currencies — the US dollar (USD), euro (EUR), Japanese yen (JPY), British pound (GBP), Swiss franc (CHF), Canadian dollar (CAD) and Australian dollar (AUD) — alongside other liquid currencies such as the New Zealand, Singapore, Hong Kong and Scandinavian currencies. A currency can only be added once its central bank's RTGS system can be linked into the PvP mechanism, which is why the eligible set is limited to currencies with robust, well-governed payment infrastructure.

## Scale

CLSSettlement is one of the largest value-processing systems in the world. It settles payment instructions on the order of **~$7-8 trillion per day** on average, with daily peaks materially higher. It serves **70-plus direct settlement members** (its owner banks and other large dealers — CLS reports over 75 member institutions) and, through them, tens of thousands of **third-party** users worldwide. Because the bulk of interbank spot, forward and FX-swap activity in the eligible currencies routes through it, CLS effectively sits at the centre of the global FX plumbing — a position reflected in its designation as systemically important.

## Relevance to Traders

For institutional FX participants, CLS is the answer to a question retail traders rarely think about: *what happens between trade execution and the moment cash actually changes hands?* Key implications:

- **Counterparty and settlement risk.** Without PvP, every cross-border FX trade carries principal [[settlement-risk]] for the hours between the two legs. Routing through CLSSettlement removes that exposure, which is why prime brokers, asset managers and corporates push institutional flow through it.
- **True transaction-cost accounting.** Settlement, netting and funding are real components of the cost of trading FX. Proper [[transaction-cost-modeling|transaction-cost modeling]] for institutional FX accounts for settlement and funding efficiency — the ~96% funding reduction from CLS netting is a genuine cost saving, not just a risk control.
- **Market microstructure.** The existence of a central PvP utility shapes how dealers manage credit lines, intraday liquidity and end-of-day positions. It interacts with execution-side practices such as [[last-look]] and with how spreads and credit terms are extended to clients.
- **Indirect exposure for retail and spot strategies.** Retail FX and spot strategies do not settle directly through CLS, but they sit downstream of an institutional market whose risk and cost structure is shaped by it. The settlement risk CLS removes at the interbank level is still borne — indirectly and in repackaged form — by participants whose brokers and liquidity providers are themselves CLS members or third-party users. Traders accounting honestly for counterparty risk should understand where, in the chain, that risk has and has not been neutralized.

## Related

- [[forex]]
- [[settlement-risk]] — also covers Herstatt risk
- [[bank-for-international-settlements]]
- [[last-look]]
- [[transaction-cost-modeling]]

## Sources

Compiled from CLS Group public documentation and the BIS Triennial Central Bank Survey (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md).
