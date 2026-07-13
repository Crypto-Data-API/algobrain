---
title: "ESMA (European Securities and Markets Authority)"
type: entity
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [regulation, stocks, options, derivatives, behavioral-finance]
aliases: ["European Securities and Markets Authority", "European Securities Markets Authority"]
entity_type: regulator
founded: 2011
headquarters: "Paris, France"
website: "https://www.esma.europa.eu"
related: ["[[finra]]", "[[sec]]", "[[itpm-trading-philosophy]]", "[[fees-and-friction]]", "[[professional-vs-retail-mindset]]", "[[options]]", "[[futures]]", "[[robinhood]]"]
---

The European Securities and Markets Authority (ESMA) is the European Union's pan-EU financial markets regulator, headquartered in Paris and established in January 2011. ESMA's mandate is threefold: investor protection, the orderly functioning of EU financial markets, and the safeguarding of EU-wide financial stability. For traders, ESMA matters most for two things: it is the architect of [[mifid-ii|MiFID II]] (the post-2018 transparency, best-execution, and reporting regime that governs EU equity, options, and derivatives trading), and it is the regulator behind the 2018 retail-CFD intervention whose mandatory loss-disclosures provide the cleanest publicly available evidence on how retail derivative traders actually perform. It is the EU peer of the US [[sec|SEC]], Australia's [[asic|ASIC]], and shares derivatives turf conceptually with the US [[cftc|CFTC]]; see [[regulation]] for the cross-jurisdiction map.

## At a Glance

| Field | Detail |
|-------|--------|
| **Full name** | European Securities and Markets Authority |
| **Type** | EU agency; one of three European Supervisory Authorities (ESAs) |
| **Founded** | 1 January 2011 (successor to CESR) |
| **Headquarters** | Paris, France |
| **Jurisdiction** | EU-wide securities and markets; sets the single rulebook, coordinates national regulators |
| **Chair** | Verena Ross (since November 2021) |
| **Front-line regulators** | National competent authorities — BaFin (DE), AMF (FR), CONSOB (IT), CySEC (CY), etc. |
| **Flagship frameworks** | [[mifid-ii\|MiFID II]]/MiFIR, MAR, EMIR, SFTR, CSDR, MiCA, Prospectus Regulation |
| **Direct intervention power** | MiFIR Article 40 — can bind product/practice restrictions EU-wide |
| **Signature retail rule** | 2018 CFD leverage caps + binary-option ban + mandatory loss disclosure |
| **US analogue** | SEC + parts of FINRA |
| **Website** | https://www.esma.europa.eu |

## Origins and Structure

ESMA was created on 1 January 2011 as part of the European System of Financial Supervision, replacing the earlier and much weaker Committee of European Securities Regulators (CESR). The post-[[2008-financial-crisis|2008-crisis]] reform package recognised that CESR — a non-binding coordinating committee — had been structurally incapable of enforcing pan-EU consistency, and that the EU needed a regulator with direct rulemaking, supervisory, and intervention powers analogous to (though narrower than) the US [[sec|SEC]].

ESMA is one of three European Supervisory Authorities (ESAs) sitting under the European Systemic Risk Board ([[esrb|ESRB]]):

| Authority | Sector | Equivalent in US terms |
|---|---|---|
| **ESMA** | Securities and markets | SEC + parts of FINRA |
| **EBA** | Banking | OCC + parts of the Fed |
| **EIOPA** | Insurance and pensions | State insurance regulators |

Member-state regulators (BaFin in Germany, AMF in France, FCA in the UK before Brexit, CONSOB in Italy, CySEC in Cyprus, etc.) remain the front-line supervisors of firms in their jurisdiction. ESMA's role is to set EU-wide standards, ensure consistent interpretation and enforcement across member states, and step in directly where investor protection or market integrity is at risk EU-wide. The UK's [[fca|FCA]] left ESMA's direct ambit on Brexit (2020) but historically inherited and largely retained ESMA's retail-protection rules.

## Core Mandate

ESMA pursues four operational objectives:

1. **Investor protection** — particularly retail investors trading complex products (CFDs, binary options, leveraged forex, structured notes).
2. **Orderly markets** — transparency, fair access, and integrity rules across equity, fixed income, and derivative markets.
3. **Financial stability** — monitoring systemic risk in market structure (CCPs, securities financing, short selling).
4. **Single rulebook enforcement** — ensuring the same EU rules apply consistently across member states, preventing regulatory arbitrage.

The legal toolkit is unusual by global standards: ESMA can issue **direct binding intervention measures** on products or practices (under MiFIR Article 40), bypassing member-state regulators when needed. This is the power it used to impose the 2018 CFD restrictions discussed below.

## MiFID II — The Big One

The Markets in Financial Instruments Directive II (MiFID II) and its companion regulation MiFIR took effect on **3 January 2018**, replacing the earlier 2007 MiFID I. It is the single most consequential piece of EU market structure regulation in the post-crisis era and the framework under which most EU-domiciled brokers, funds, and trading venues operate today.

### Key MiFID II provisions for traders

| Area | Rule | Practical effect |
|---|---|---|
| **Pre-trade transparency** | Bid/offer and depth disclosure required across more instrument classes | Tighter spreads on bonds and derivatives; shrinkage of dark trading |
| **Post-trade transparency** | Trade prints required for equities, ETFs, derivatives, bonds (with deferrals for large blocks) | Far better TCA data than under MiFID I |
| **Best execution** | Firms must publish RTS 27 and RTS 28 reports on execution venues and quality | Auditable evidence of where orders go and at what cost |
| **Research unbundling** | Research must be paid for separately from execution commissions | Massive contraction in sell-side equity research output post-2018 |
| **Position limits** | Hard limits on commodity-derivative positions (carried over from EMIR) | Constraints on commodity speculation |
| **Algorithmic trading controls** | Firms running algos must register, test, and have kill switches | Higher operational bar for retail-facing algo platforms |
| **Inducements ban** | No third-party payments to independent advisers; restrictions on portfolio managers | Functional ban on equity-research soft-dollaring in EU |
| **Reporting (RTS 22)** | Transaction reporting on roughly 65 fields per trade | The data backbone ESMA uses for surveillance |
| **Reg-NMS-style consolidated tape** | Authorised but slow to deploy | CTPs finally selected in 2025 (see below); no tape live yet as of mid-2026 |

The most felt second-order consequence has been the contraction of EU sell-side research after research unbundling, the migration of dark trading volume into Systematic Internalisers (SIs) and frequent batch auctions, and the structural disadvantage MiFID II places on EU brokers relative to US peers in cost-to-serve. Critics argue MiFID II overshot on retail protection at the cost of EU market depth; defenders point to the substantially improved transparency dataset for academic and TCA research.

## The 2018 Retail-CFD Intervention

In **March 2018**, ESMA used its MiFIR Article 40 powers for the first time to impose binding EU-wide restrictions on the marketing, distribution, and sale of contracts-for-difference (CFDs) and binary options to retail clients. The original measure was renewed every three months until **August 2019**, at which point individual national regulators (CySEC, BaFin, FCA, etc.) made the rules permanent under their own statutes. The measures remain in force across the EU and, post-Brexit, in the UK.

### What the intervention actually does

The CFD intervention bundles five rules:

| Rule | Detail |
|---|---|
| **Leverage caps** | Maximum leverage on CFDs against major FX pairs: **30:1**. Non-major FX, gold, major equity indices: **20:1**. Non-major equity indices, other commodities, gold-related products: **10:1**. Individual equities: **5:1**. Crypto-asset CFDs: **2:1** |
| **Margin close-out rule** | A 50%-of-initial-margin auto-liquidation rule per account: when account equity falls below 50% of the total initial margin posted, the broker must liquidate positions |
| **Negative-balance protection** | Retail clients cannot lose more than the funds in their CFD account. Brokers absorb the residual on adverse gaps |
| **Inducement ban** | No bonuses, no "free trading" promotions, no marketing perks tied to deposit or trading volume |
| **Loss-disclosure requirement** | Every CFD provider must prominently display, in all marketing material, the percentage of its retail CFD accounts that lost money over the prior 12 months — typically phrased: *"XX% of retail investor accounts lose money when trading CFDs with this provider."* |

Binary options to retail clients were **prohibited outright** in the same measure.

### Why this matters for the wiki

The retail-loss disclosure rule is the source of the 70-90% retail-loss statistic that appears across [[anton-kreil|Kreil]] interviews, the [[itpm-trading-philosophy|ITPM philosophy]], and most serious literature on retail derivative performance. Before 2018 the only such data came from leaked broker disclosures or academic studies of specific brokerages — neither continuous nor comparable. Post-2018, every regulated EU CFD broker must publish a continuously updated loss percentage, and the data has converged on a clear pattern:

- The single-broker numbers vary roughly **51% to 89%** depending on broker, year, and asset mix
- Broker-level numbers tend to cluster between **65% and 80%** in typical years
- Bull-market tape (2020-2021, 2024) compresses the loss percentage modestly because long-biased retail traders ride the trend
- Sideways and bear tape (2022) widens it back toward 80%+
- Brokers with more "professional" client mixes (higher minimum deposits, more options-aware clients) sit at the lower end; pure CFD-day-trader brokers sit at the higher end
- The sample includes only **active accounts** — dormant or zero-trade accounts are typically excluded — so the figures slightly understate the failure rate of the universe of *people who tried CFD trading*

The disclosure data is the cleanest publicly available evidence on retail derivative performance globally, because it is mandatory, continuous, comparable, broker-by-broker, and reflects realised P&L net of all costs. The [[sec|SEC]] / [[finra|FINRA]] equivalent in the US — broker [[payment-for-order-flow]] disclosures and the occasional FINRA retail study — is not nearly as complete or comparable.

## Other Major ESMA Files

| Regime | Subject | Trader-relevant content |
|---|---|---|
| **MAR** (Market Abuse Regulation, 2016) | Insider dealing, market manipulation, suspicious-transaction reporting | Pan-EU insider-dealing prohibition; cross-border surveillance; STOR filings by brokers |
| **EMIR** (European Market Infrastructure Regulation) | OTC derivatives, central clearing, trade repositories | Mandatory clearing for standardised OTC derivatives; trade-reporting backbone for derivatives surveillance |
| **SFTR** | Securities financing transactions | Repo and securities-lending reporting |
| **Short-Selling Regulation** | Short positions on EU equities and sovereign debt | Disclosure thresholds (0.1% notify, 0.5% public); locate rules; ESMA emergency restriction powers |
| **CRA Regulation** | Credit rating agencies | Direct ESMA supervision of S&P, Moody's, Fitch in EU |
| **CSDR** | Central securities depositories | Settlement discipline regime; mandatory buy-ins |
| **Prospectus Regulation** | Public offers of securities | Standardised EU prospectus rules |
| **MiCA** (Markets in Crypto-Assets, fully applicable Dec 2024) | Crypto-asset issuers and service providers | Pan-EU licensing for crypto exchanges; stablecoin reserve and disclosure rules |

## Developments 2024-2026

ESMA, chaired by **Verena Ross** (since November 2021), advanced several structurally significant files in 2024-2026:

- **MiCA went fully live (30 December 2024)** — Crypto-asset service providers now require pan-EU authorisation; 2025-2026 has been the transition/enforcement phase, with national regulators issuing CASP licences and ESMA coordinating supervision convergence.
- **EU consolidated tape finally moved from paper to procurement** — On **3 July 2025** ESMA selected **Ediphy (fairCT)** as the first Consolidated Tape Provider for **bonds**; on **19 December 2025** it selected **EuroCTP** (a venue-owned consortium) as the first CTP for **shares and ETFs**. A selection process for an **OTC derivatives** tape followed in 2026. The tapes are expected to go live progressively after authorisation — the EU's answer, two decades late, to the US consolidated tape.
- **EU move to T+1 settlement scheduled for 11 October 2027** — ESMA recommended the transition in late 2024 and is coordinating the EU switch alongside parallel UK and Switzerland moves, following the US T+1 shift of May 2024. Funding, securities-lending, and FX-cutoff workflows for anyone trading EU equities will change on that date.
- **Savings and Investment Union agenda** — ESMA has been pushing supervisory-convergence and retail-participation workstreams under the EU's 2025 Savings and Investment Union strategy, including proposals for more direct ESMA supervisory powers over systemic cross-border entities (CTPs, major CASPs).

## Trading-Relevant Implications

ESMA's rule set creates a structurally **different operating environment for EU retail traders** versus US retail traders. The most consequential differences:

1. **Lower CFD leverage in EU than offshore** — A retail trader in the EU who wants 100x leverage on a major FX pair cannot get it from an EU-licensed broker; the offshore alternatives (Vanuatu, Seychelles, Bahamas) carry counterparty and recovery risk that EU-licensed brokers do not.
2. **Negative-balance protection as a free option** — EU retail traders effectively have a free out-of-the-money put on their CFD account losses, courtesy of the broker's residual exposure on flash crashes and gap moves. US futures and FX traders have no such protection.
3. **Mandatory loss disclosure as a behavioural intervention** — The "XX% lose" warning shown on every CFD broker's homepage is an evidence-based behavioural nudge; surveys post-2018 found the disclosure modestly reduced retail account openings and shifted some demand toward [[options]] and equity products. The behavioural effect is small but real.
4. **No PFOF until recently** — EU MiFID II best-execution and inducement rules effectively banned [[payment-for-order-flow]] long before the [[sec|SEC]] began considering similar restrictions. An EU MiFID II Refit in 2024 codified the PFOF ban explicitly. EU retail traders therefore use brokers like interactive-brokers EU, ig-markets, cmc-markets, and Saxo whose order-routing economics differ from US PFOF-funded brokers like [[robinhood]].
5. **No US-style options market for retail** — EU equity options markets exist (Eurex) but retail access is far smaller and more expensive than US. EU retail derivative demand is therefore concentrated in CFDs and structured products rather than listed options.
6. **Tighter algorithmic-trading controls** — EU retail-facing platforms running algorithmic features must register and meet operational standards under MiFID II RTS 6, raising the bar versus the US where retail algo platforms operate with lighter oversight.

For a trader sitting in the EU, the most consequential single fact about ESMA is the **5:1 retail equity CFD cap** and the **2:1 retail crypto cap** — both of which can be circumvented by qualifying as a Professional Client (€500K+ portfolio, 10+ trades per quarter, financial-sector experience). The Professional uplift gives access to leverage closer to US institutional norms but removes negative-balance protection. This is the formal version of the [[professional-vs-retail-mindset|professional vs retail]] distinction: in the EU, professional status is a regulatory category with measurable thresholds and a paperwork uplift, not just a mindset.

## Why ESMA Data Matters for the ITPM-Style Argument

The [[itpm-trading-philosophy|ITPM philosophy]] argues that 70-90% of retail accounts lose money in any given 12-month window, even in bull markets, primarily because of the [[fees-and-friction|fees-and-friction stack]] and behavioural inversion versus professionals. The ESMA-mandated CFD broker disclosures are the **single best public dataset to test that claim**. They consistently show:

- Loss percentages in the **51%-89% range** depending on broker, year, and asset
- A **central tendency around 70-77%** in typical mixed-tape years across major EU CFD brokers
- The number does **not** improve materially in bull-market years — losing 65% in a year the index rallied 25% is itself an indictment of how retail allocate, not of the tape
- Brokers with the lowest leverage caps (and the most options-literate client bases) print the lowest numbers; high-leverage CFD-day-trade brokers print the highest

The data is widely cited by professional-trader educators precisely because it is mandatory, comparable, and uncomfortable. It is also why eToro's disclosure (which prints in the lower half of the range, near 51-77% depending on the period sampled) gets cited as the *favourable* example — even on the favourable end, the majority of retail accounts lose money.

## Limitations of ESMA Data

- **CFD universe only** — The disclosures cover CFDs, not spot equity, options, or crypto-spot trading. The numbers do not directly speak to a long-only retail equity book.
- **Active-account scope** — Dormant or near-zero-trade accounts are typically excluded; the failure rate of the universe of *people who tried* is somewhat higher.
- **Period sensitivity** — The 12-month window means results lag the regime; a 12-month window ending mid-bear can print a worse number than the underlying behaviour warrants.
- **Self-reporting** — Brokers report their own numbers under regulatory scrutiny but ESMA does not publish a centralised dataset; aggregation requires scraping individual broker disclosures.
- **No P&L distribution detail** — The disclosure is binary (lost money / did not), not P&L magnitude. The asymmetry of retail returns (a few large winners, many small losers) is not visible from the disclosure alone.

## Related

- [[finra]] — US analogue at the broker-dealer oversight layer
- [[sec]] — US analogue at the federal securities regulator layer
- [[asic]] — Australian analogue; near-identical retail CFD intervention
- [[cftc]] — US derivatives regulator (EMIR is the EU clearing analogue)
- [[regulation]] — Global financial-regulation overview
- [[risk-management]] — Leverage caps and negative-balance protection as survivorship tools
- [[robinhood]] — US contrast: PFOF model that ESMA effectively banned in EU
- [[itpm-trading-philosophy]] — Cites ESMA disclosure data as the empirical floor under the 70-90%-lose claim
- [[fees-and-friction]] — The structural drag the ESMA data ultimately measures
- [[professional-vs-retail-mindset]] — ESMA codifies a formal version of the distinction via Professional-Client status
- [[options]] — Listed-options access in the EU is structurally narrower than US, partly an ESMA / member-state outcome
- [[mifid-ii]] — The framework regulation
- [[emir]] — Derivatives clearing and reporting

## Sources

- ESMA official site: https://www.esma.europa.eu
- ESMA press release, "ESMA selects Ediphy (fairCT) to become the first Consolidated Tape Provider for bonds" (Jul 3, 2025): https://www.esma.europa.eu/press-news/esma-news/esma-selects-ediphy-fairct-become-first-consolidated-tape-provider-bonds
- ESMA press release, "ESMA selects EuroCTP to become the first Consolidated Tape Provider for shares and ETFs" (Dec 19, 2025): https://www.esma.europa.eu/press-news/esma-news/esma-selects-euroctp-become-first-consolidated-tape-provider-shares-and-etfs
- ESMA, Consolidated Tape Providers hub: https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/consolidated-tape-providers
- ESMA 2018 product-intervention decisions (CFD leverage caps, binary-option ban) and MiFID II / MiFIR / MAR / EMIR / MiCA official texts
- Individual EU broker mandatory loss disclosures referenced in [[itpm-trading-philosophy]] and across [[anton-kreil|Kreil]]'s public interviews
- 2025-2026 developments verified via Perplexity and web search, 2026-06-10
