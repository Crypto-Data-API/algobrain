---
title: "MEMX (Members Exchange)"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [exchange, stocks, options, market-microstructure, regulation]
aliases: ["Members Exchange", "MEMX Options"]
entity_type: exchange
founded: 2019
headquarters: "Jersey City, NJ, USA"
website: "https://memx.com"
related: ["[[occ]]", "[[sec]]", "[[cboe]]", "[[cboe-global-markets]]", "[[nyse]]", "[[nasdaq]]", "[[options-disclosure-document]]", "[[regulation]]", "[[citadel-securities]]", "[[virtu-financial]]", "[[smart-order-routing]]", "[[payment-for-order-flow]]"]
---

# MEMX (Members Exchange)

Members Exchange (MEMX) is a US national securities exchange founded in **January 2019** by a coalition of major Wall Street market participants and launched its **equities market in September 2020**. It later launched **MEMX Options in 2023**, expanding from cash equities into the listed-options market. MEMX was created explicitly to challenge the incumbent exchange triad of [[nyse|NYSE]], [[nasdaq|Nasdaq]], and [[cboe-global-markets|Cboe]] by offering a member-owned cooperative structure with lower fees and simplified pricing.

## Overview

MEMX is registered with the [[sec|SEC]] as a national securities exchange under the Securities Exchange Act of 1934 and operates from Jersey City, NJ. It is structurally distinct from incumbent exchanges in that it is **owned and governed by its member firms** — the same firms that route orders to it — rather than by public shareholders chasing exchange-fee profit margins. The model echoes the original member-cooperative origins of US exchanges before their early-2000s demutualizations.

The MEMX name is intentional: "Members Exchange." The pitch is that an exchange owned by users will price more fairly, lobby less aggressively against user interests, and avoid the data-fee monetization that has characterized [[nyse|NYSE]] and [[nasdaq|Nasdaq]] over the past decade.

## History

### Founder Coalition (January 2019)

MEMX was launched as a joint venture among nine financial firms, with additional investors joining in subsequent funding rounds. The founder/early-investor list includes some of the largest Wall Street institutions:

- **Bank of America Merrill Lynch**
- **Charles Schwab** — see [[charles-schwab]]
- **Citadel Securities** — see [[citadel-securities]]
- **Citigroup**
- **E*TRADE** (later acquired by Morgan Stanley)
- **Fidelity Investments**
- **JPMorgan Chase**
- **Morgan Stanley**
- **TD Ameritrade** (later acquired by [[charles-schwab|Charles Schwab]])
- **UBS**
- **Virtu Financial** — see [[virtu-financial]]
- **BlackRock** (added in subsequent funding)
- **Goldman Sachs** (added in subsequent funding)
- **Wells Fargo** (added in subsequent funding)
- **Jane Street** (added in subsequent funding)

This investor list spans the major US **wholesale market makers** ([[citadel-securities|Citadel Securities]], [[virtu-financial|Virtu]], Jane Street), the largest **retail brokers** ([[charles-schwab|Schwab]], Fidelity, TD Ameritrade, E*TRADE), the largest **bulge-bracket banks** (JPMorgan, Goldman, Morgan Stanley), and major **buy-side asset managers** (BlackRock). The shared interest: lower exchange fees and reduced market data costs paid to incumbent exchanges.

### Equities Launch (September 2020)

MEMX received SEC approval as a national securities exchange in May 2020 and went live with its equities market on September 21, 2020. Trading is conducted on a single matching engine using a maker-taker pricing model.

### Options Launch (2023)

MEMX Options received SEC approval and launched its options market in 2023. It became the **17th US options exchange** and operates with the same member-friendly fee philosophy.

### Inclusion in Updated ODD (June 2024)

MEMX Options was added to the list of recognized options markets in the **June 2024 update of the [[options-disclosure-document|Options Disclosure Document (ODD)]]**, the OCC's required pre-trade disclosure delivered to retail customers. This update reflects MEMX's full integration into the OCC clearing ecosystem alongside [[cboe]], [[nyse]], [[nasdaq]], MIAX, and BOX.

## Equities and Options Markets

| Market | Launch | Description |
|--------|--------|-------------|
| **MEMX Equities** | September 2020 | National securities exchange for NMS-listed equities (stocks listed on [[nyse]] and [[nasdaq]]). Standard limit order book with maker-taker rebate structure. |
| **MEMX Options** | 2023 | Listed options exchange. Cleared through [[occ|OCC]]. Trades the same standardized contracts as other US options exchanges, ensuring fungibility. |

Both markets are accessible to broker-dealers via standard FIX connectivity and are routed to by retail and institutional [[smart-order-routing|smart order routers]] alongside other US lit venues.

## Pricing Model

MEMX's competitive thesis rests on **lower fees and simpler pricing** relative to incumbents:

- **Reduced market-data fees** — MEMX charges substantially less for proprietary depth-of-book data feeds than [[nyse|NYSE]] or [[nasdaq|Nasdaq]] charge for comparable products. This is a direct cost savings for member firms that consume real-time market data across all venues.
- **Simplified rebate structure** — Fewer fee tiers and pricing tables than the incumbent exchanges, which have evolved baroque tiered structures with dozens of rebate codes.
- **Maker-taker model** — Standard maker rebate / taker fee structure for equities, with rates adjusted to undercut incumbents.
- **No connectivity rent-seeking** — MEMX has positioned itself as charging cost-recovery rates for connectivity (port fees, cross-connects) rather than monopoly rents.

The economic logic: by pulling order flow toward MEMX with lower all-in costs, the founder firms reduce their aggregate spend on exchange and market-data fees, even if MEMX itself does not return a large profit dividend.

## Significance

MEMX's significance lies less in raw market share and more in its existence as a **structural threat** to the incumbent exchange duopoly/triopoly:

1. **Fee competition** — MEMX's lower fee schedule has been cited as a benchmark in industry comments to the SEC about excessive market-data fees, supporting broader rulemaking efforts (e.g., the SEC's market-data infrastructure rule).
2. **Member-owned governance** — Unlike public-shareholder-owned [[nasdaq|Nasdaq]] (NDAQ), [[nyse|NYSE]] (parent ICE), and [[cboe-global-markets|Cboe Global Markets]] (CBOE), MEMX has no fiduciary duty to maximize fee revenue.
3. **Conflict-of-interest inversion** — When [[citadel-securities|Citadel Securities]], [[virtu-financial|Virtu]], and Jane Street own a piece of an exchange they route flow to, the traditional conflict (exchange wants to charge them more, they want to pay less) is internalized into a single decision-making body. Critics argue this creates new conflicts; proponents argue it aligns incentives.
4. **Validation of the cooperative model** — MEMX is a successful proof-of-concept for member-owned market infrastructure, alongside other recent cooperative ventures.

## Recent Inclusion in ODD (June 2024)

The OCC updated the [[options-disclosure-document|Options Disclosure Document]] in June 2024 to reflect changes in the listed-options ecosystem, including:

- Recognition of **MEMX Options** as an approved options market
- Addition of newer MIAX exchanges (MIAX Sapphire)
- Updates to settlement procedures aligned with the May 2024 industry transition to **T+1 settlement** for equities and options exercise

For retail traders, the practical consequence is that broker order routers may now route options orders to MEMX Options as one of the available execution venues, and any [[occ|OCC]]-cleared option contract is fungible across MEMX Options and the other 16 options exchanges.

## Market Share Trajectory

In US equities, MEMX has grown from launch to a mid-single-digit percentage of consolidated tape volume during 2024, placing it in the same general size range as Cboe BZX, EDGX, and other secondary lit venues — well below [[nasdaq|Nasdaq]] and [[nyse|NYSE]] primary listings volume but materially above niche venues. Exact monthly market share numbers are published by the SEC's Market Information Data Analytics System (MIDAS) and on consolidated tape statistics.

In US options, MEMX Options is in an earlier growth phase post-2023 launch and has lower market share than the established Cboe and Nasdaq options complexes.

### 2025–2026 Update

MEMX's options business became its standout growth story (figures from MEMX's own market-structure reports):

- **Options** — MEMX Options reached **8.4% regular electronic market share in October 2025, ranking second among 18 US options exchanges**. In December 2025 it ranked second in penny-issue regular-electronic share (7.8%) and **first in non-penny issues (12.5%)**. Non-penny share continued climbing, from 8.9% in March 2025 to **17.1% in March 2026**
- **Equities** — MEMX equities held roughly **2.5% of total consolidated volume (≈4.7% of on-exchange volume) as of March 2026**, with notional traded hitting a record $21.6 billion/day at one point, up 93% year-over-year, helped by the retail-driven volume surge; retail limit-order ADV reached a record 154 million shares
- **Second medallion** — In **March 2025** MEMX received SEC approval for a second exchange license, **MX2**, following the industry pattern (Cboe's four medallions, Nasdaq's three) of running multiple fee/queue models under one operator
- MEMX has also publicly lobbied on market-structure issues, e.g. arguing the one-cent minimum tick hurts exchange competitiveness versus off-exchange venues

## Related

- [[occ]] — Clears all MEMX Options trades; MEMX is an OCC participant exchange
- [[sec]] — Approves MEMX rule filings and oversees its operations
- [[cboe]] — Competing options exchange
- [[cboe-global-markets]] — Parent of Cboe; primary competitor to MEMX in options
- [[nyse]] — Competing equities exchange
- [[nasdaq]] — Competing equities exchange
- [[options-disclosure-document]] — June 2024 update added MEMX Options
- [[regulation]] — MEMX operates under SEC Reg NMS framework
- [[citadel-securities]] — Founding investor and major routing counterparty
- [[virtu-financial]] — Founding investor
- [[smart-order-routing]] — How orders reach MEMX in practice
- [[payment-for-order-flow]] — Alternative execution model that bypasses lit exchanges like MEMX

## Sources

- MEMX Insights, "Kicking off 2025 with strong equity and options volume" — https://memx.com/insights/strong-volume-in-january-one-cent-tick-size-hurts-exchange-competitiveness
- MEMX Insights, "Volatility Boosts Exchange Share; Options Non-Penny Market Share Surges" (2026) — https://memx.com/insights/volatility-boosts-exchange-share-options-non-penny-market-share-surges
- MEMX Insights, "New Equity and Options Volume Records on MEMX Exchanges" — https://memx.com/insights/new-equity-and-options-volume-records-on-memx-exchanges
- MEMX Insights, "Year in Review: Retail-Driven Volume Surge" — https://memx.com/insights/year-in-review-retail-driven-volume-surge
- MarketsWiki, "Members Exchange (MEMX)" — https://marketswiki.com/wiki/Members_Exchange_(MEMX)
- MEMX SEC Form 1 application / approval orders (May 2020); OCC ODD update (June 2024)
- Verified via web search, 2026-06-10
