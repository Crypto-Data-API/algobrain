---
title: "Over-the-Counter (OTC) Markets"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [stocks, market-microstructure, liquidity, regulation]
aliases: ["OTC", "OTC Markets", "Over-the-Counter", "Pink Sheets", "OTCQX", "OTCQB", "OTC Pink"]
related: ["[[primary-vs-secondary-market]]", "[[penny-stock]]", "[[american-depositary-receipt]]", "[[liquidity]]", "[[nyse]]", "[[nasdaq]]", "[[market-manipulation]]", "[[delisting]]", "[[bid-ask-spread]]"]
domain: [stocks, market-microstructure]
difficulty: beginner
---

**Over-the-counter (OTC) markets** are venues where securities trade directly through a network of broker-dealers rather than on a centralized, listed exchange such as the [[nyse|NYSE]] or [[nasdaq|Nasdaq]]. For equities, "OTC" in the US usually means the tiered marketplaces operated by **OTC Markets Group** — **OTCQX**, **OTCQB**, and **OTC Pink** (the old "**pink sheets**"). This page answers the ALFRED question *"this stock isn't on the NYSE or Nasdaq — where does it trade, and what does that mean?"* OTC listing is not inherently bad — many legitimate foreign companies and [[american-depositary-receipt|ADRs]] trade OTC — but the lower disclosure bar means the venue ranges from blue-chip-quality to outright shell companies.

## How OTC differs from an exchange

On a listed exchange, securities are *listed* under that exchange's rules and trade on a central order book. OTC securities are *quoted* by dealers who post bids and offers; trades are negotiated/matched through that dealer network. Key differences:

- **No exchange listing standards** to meet (minimum price, market cap, shareholder count, governance) — or far lighter ones.
- **Quote-driven, dealer-intermediated** rather than a single central limit order book.
- **Thinner [[liquidity]]** and wider [[bid-ask-spread|spreads]] on most names.
- **Variable disclosure** — from full SEC reporting down to almost none, depending on the tier.

OTC is still a [[primary-vs-secondary-market|secondary market]] — investors trade existing shares with each other via dealers; it is simply not a centralized exchange.

## The OTC Markets tiers

OTC Markets Group sorts securities into quality tiers by disclosure and eligibility:

| Tier | Disclosure / standard | Typical occupants |
|---|---|---|
| **OTCQX** (Best Market) | Highest OTC standard; audited financials, minimum bid price, no shells/bankrupt firms | Established foreign companies, large [[american-depositary-receipt|ADRs]], reputable mid/small caps |
| **OTCQB** (Venture Market) | Reporting, $0.01 minimum bid, annual verification; early-stage/developing firms | Small and emerging US and foreign companies |
| **OTC Pink** ("Pink Sheets") | Lowest bar; ranges from current-information to "no information" / shells | Distressed firms, shells, [[delisting|delisted]] companies, many [[penny-stock|penny stocks]] |

The name "pink sheets" comes from the literal pink-colored paper on which dealer quotes were historically printed before electronic quotation. Today, quotes are published electronically on **OTC Link ATS** (an alternative trading system operated by OTC Markets Group and regulated by FINRA/the SEC).

## Rule 15c2-11, the Expert Market, and the grey market

A 2020 SEC amendment to **Rule 15c2-11** (effective September 2021) reshaped the lowest OTC tier. To publicly quote a security, a broker-dealer must now have **current issuer information** on file. Companies that stopped disclosing — the old "no information" shells — can no longer be quoted publicly and were moved to the **Expert Market**, where quotes are visible only to sophisticated/professional investors and unsolicited orders; retail investors generally can only sell, not buy. The intent was to squeeze out the "dark," non-reporting names most associated with fraud.

- **Grey market.** Securities that are neither exchange-listed nor quoted on OTC Link at all. Trades can still be privately negotiated and reported to FINRA, but there are **no published bids/offers**, so pricing is opaque and execution is entirely dealer-dependent.
- **Form 211.** Historically the filing a broker-dealer submitted to FINRA to initiate public quoting of an OTC security; the 15c2-11 rules govern the underlying information requirements.

## Who legitimately trades OTC

OTC is not synonymous with fraud. Genuine reasons a real company trades OTC include:

- **Foreign companies and [[american-depositary-receipt|ADRs]]** — many large, blue-chip non-US firms list their US-traded shares OTC (often OTCQX) to avoid the cost and duplicate reporting of a full US exchange listing while still reaching US investors. Real examples of legitimate, profitable companies whose US shares trade OTC include **Nestlé (NSRGY), Roche (RHHBY), Tencent (TCEHY), Nintendo (NTDOY), Adidas (ADDYY), and Heineken (HEINY)** — household-name multinationals, not shells.
- **Companies too small for exchange listing** — early-stage firms that do not yet meet NYSE/Nasdaq thresholds.
- **[[delisting|Delisted]] companies** — firms that fell below an exchange's minimum price or filing requirements and dropped to OTC.
- **Banks and "dark" community companies** — small regional banks and closely held firms that never sought an exchange listing.

## What to watch for

- **Disclosure is the dividing line.** OTCQX/OTCQB names report regularly; many OTC Pink names disclose little or nothing. Treat "no information" / "shell" flags as a hard stop.
- **Liquidity and spreads.** Most OTC names trade thinly with wide [[bid-ask-spread|spreads]]; the round-trip cost can dwarf any expected edge, and large orders move the price.
- **Manipulation risk.** The lower OTC tiers are the natural habitat of [[market-manipulation|pump-and-dump]] schemes and many [[penny-stock|penny stocks]]; thin floats make them easy to ramp.
- **Quote vs. fill.** A displayed quote may not be executable in size; OTC fills can be far from the screen price.
- **Reporting status and tier matter more than the name.** The same ticker can carry very different risk depending on whether it sits on OTCQX or OTC Pink "no information."

## Hypothetical example

A fictional European consumer-goods firm, **Helvetia Foods AG**, is large and profitable but does not want the cost and reporting burden of a full [[nyse|NYSE]] listing. It sponsors a Level I [[american-depositary-receipt|ADR]] that trades on **OTCQX** in US dollars; US investors get a liquid, audited, regularly reporting security that simply happens to be OTC rather than exchange-listed — a perfectly reasonable holding. In contrast, a fictional shell, **Apex Holdings Inc.**, trades on **OTC Pink** with a "no information" flag, no audited financials, and a $0.03 price; it is the kind of OTC name where a promotional ramp can appear and vanish overnight. Same marketplace, opposite risk — which is the core lesson about OTC. (Both companies are illustrative, not real.)

## Related

- [[primary-vs-secondary-market]] — OTC is a dealer-based secondary market
- [[penny-stock]] — many penny stocks live on the lower OTC tiers
- [[american-depositary-receipt]] — foreign-company ADRs commonly trade OTC
- [[liquidity]] — the thin liquidity typical of OTC names
- [[bid-ask-spread]] — wider spreads are a core OTC cost
- [[market-manipulation]] — the lower OTC tiers attract pump-and-dump schemes
- [[delisting]] — exchange-delisted stocks often drop to OTC
- [[nyse-vs-nasdaq]] — the listed-exchange alternatives to OTC

## Sources

- OTC Markets Group, marketplace tier descriptions (OTCQX, OTCQB, Pink, Expert Market) and OTC Link ATS documentation.
- US Securities and Exchange Commission, investor-education materials on OTC and microcap securities; Rule 15c2-11 (2020 amendment, effective September 2021).
- General market knowledge; no specific wiki source ingested yet.
