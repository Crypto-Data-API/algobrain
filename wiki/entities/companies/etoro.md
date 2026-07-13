---
title: "eToro"
type: entity
created: 2026-05-07
updated: 2026-06-18
status: excellent
tags: [company, exchange, behavioral-finance, crypto, stocks]
aliases: ["eToro Group", "eToro Group Ltd.", "ETOR"]
entity_type: company
ticker: "ETOR"
exchange: "NASDAQ"
sector: "Financials"
founded: 2007
headquarters: "Bnei Brak, Israel; with subsidiaries in London, Cyprus, and the US"
website: "https://www.etoro.com"
related: ["[[esma]]", "[[robinhood]]", "[[interactive-brokers]]", "[[ig-markets]]", "[[cmc-markets]]", "[[itpm-trading-philosophy]]", "[[fees-and-friction]]", "[[professional-vs-retail-mindset]]", "[[copy-trading]]", "[[social-trading]]", "[[payment-for-order-flow]]", "[[crypto]]", "[[options]]", "[[behavioral-finance-overview]]"]
---

eToro is an Israeli-headquartered, multi-jurisdiction retail trading platform founded in 2007 by brothers Yoni and Ronen Assia together with David Ring. It pioneered the *social trading* category — most distinctively the **CopyTrader** product, which lets users mirror the live positions of other users in real time — and grew to become one of the largest retail CFD and multi-asset trading platforms in Europe, Australia, the UK, and parts of the US. eToro listed on Nasdaq in **May 2025 via a traditional IPO** (ticker **ETOR**, priced at $52/share, raising ~$620M at a ~$4.2B valuation — after an earlier 2021 SPAC attempt with FinTech Acquisition Corp V at a $10.4B valuation was scrapped in mid-2022). For the purposes of this wiki the company matters principally because its mandatory [[esma|ESMA]] retail-CFD loss disclosures are among the most-cited data points in trader-interview discussions of retail performance and the [[professional-vs-retail-mindset|professional-vs-retail]] gap.

## History

eToro was founded in **Tel Aviv in 2007** by Yoni Assia, Ronen Assia, and David Ring, originally under the name *RetailFX*. The early product was a graphical, visual forex platform aimed at making FX charts and execution intuitive for non-specialists — an explicit attempt to build the "iPhone of trading" before the iPhone existed in serious form. The core insight was that the binding constraint on retail FX was not data or execution but *user experience*; everything else followed from that.

Key milestones:

| Year | Event |
|---|---|
| 2007 | Founded as RetailFX in Tel Aviv |
| 2010 | Launches "OpenBook" — the social-trading network letting users see and discuss other users' trades |
| 2010 | Renamed eToro |
| 2011 | Launches CopyTrader, the auto-mirroring of selected traders' positions |
| 2013 | Adds CFD trading on equities |
| 2017 | Adds direct crypto trading (BTC, ETH and others) |
| 2018 | Hit by the [[esma|ESMA]] retail-CFD intervention; leverage caps and mandatory loss-disclosure go into effect |
| 2018-2019 | Launches in the US as eToro USA, initially crypto-only |
| 2020 | Launches commission-free US equity trading via eToro USA Securities |
| 2021 | First SPAC merger announcement (FinTech Acquisition Corp V) at $10.4B valuation |
| 2022 | First SPAC deal terminated due to market conditions |
| 2025 | Listed on Nasdaq via traditional IPO (May 2025, $52/share, ~$4.2B valuation, ticker ETOR) |
| 2024-2026 | Continued expansion into options, fractional shares, and ETF wrappers |

The company is regulated separately in each major jurisdiction: by [[esma|ESMA]] member regulators in the EU (notably CySEC in Cyprus, where eToro (Europe) Ltd is licensed), by the FCA in the UK (eToro UK Ltd), by ASIC in Australia, and by [[finra|FINRA]] / [[sec|SEC]] in the US (eToro USA Securities Inc.) The CFD product line is largely *not* offered in the US — eToro USA's product is closer to a [[robinhood|Robinhood]]-style commission-free equity and crypto broker than to its EU CFD shape.

## Products

| Product line | Geographic availability | Mechanism |
|---|---|---|
| **CFDs** on FX, indices, commodities, equities, crypto | EU, UK, Australia, ROW | Customer enters a contract-for-difference with eToro; eToro takes the other side and either internalises or hedges externally. P&L is cash-settled. Subject to ESMA leverage caps in the EU/UK |
| **Real (cash) equities** | EU, UK, Australia, US | Direct ownership (or beneficial ownership via custodian); fractional shares supported |
| **ETFs** | EU, UK, Australia, US | Cash-settled holdings |
| **Crypto** | EU, UK, Australia, US (via eToro USA / Paxos, varying state-by-state) | Direct holdings via custodial wallets; not always withdrawable to external addresses depending on jurisdiction |
| **Options** | US (introduced 2023-2024); rolling out in EU | Listed equity options on US underlyings |
| **CopyTrader** | EU, UK, Australia (limited US scope) | Auto-mirrors a selected user's positions in real time |
| **CopyPortfolios / Smart Portfolios** | Global | Themed baskets of assets, sometimes including allocations to top traders |
| **eToro Money** | UK, EU | Bank-like accounts and debit cards |
| **eToro Wallet** | Global | Self-custody-style crypto wallet for withdrawal of held positions |

## Business Model

eToro's revenue economics differ between geographies:

1. **CFD spreads and overnight financing (EU/UK/Australia)** — The dominant historical profit driver. eToro quotes a spread on top of the underlying market, takes the other side of customer trades, and charges overnight financing on leveraged positions. A large share of CFD revenue is *spread + financing*, with directional client P&L being a smaller, more volatile contributor (and in part hedged externally).
2. **Crypto spreads** — Wider than equity spreads, particularly on smaller-cap assets. Crypto has historically been a high-margin product line for eToro, especially during 2020-2021's retail-crypto boom.
3. **US equity commissions and PFOF (eToro USA)** — Commission-free, with order-routing revenue from market makers under [[payment-for-order-flow|PFOF]] — though eToro's PFOF take is smaller than [[robinhood]]'s.
4. **Currency conversion fees** — A consequential revenue line on a multi-currency platform, especially for small EU clients trading USD-denominated US equities.
5. **Withdrawal fees, inactivity fees** — Small but recurring; partially restricted under ESMA inducement rules.

This mix means eToro's revenue is highly correlated with retail trading activity, particularly in crypto. The 2021 boom drove revenue toward $1.2B; subsequent crypto winters compressed it materially. The Nasdaq listing has subjected this volatility to public-market scrutiny.

### Revenue mix at a glance

The economically meaningful top line for eToro is **net contribution** (revenue net of crypto pass-through and direct trading costs), *not* the gross "revenue" figure that crypto cost-of-sales inflates. The contribution stack:

| Revenue line | Geography | Driver | Cycle sensitivity |
|---|---|---|---|
| **CFD spreads + overnight financing** | EU, UK, Australia, ROW | Spread on the underlying + financing on leveraged positions; dominant historical profit driver | High — scales with active-trading volume and volatility |
| **Crypto spreads** | Global (jurisdiction-limited) | Wide spreads, especially small-cap assets; high-margin in bull tape | Very high — peaks in retail-crypto booms, collapses in crypto winters |
| **US equity commissions + [[payment-for-order-flow|PFOF]]** | US (eToro USA) | Commission-free with order-routing rebates; PFOF take smaller than [[robinhood]]'s | Medium — tied to US retail equity activity |
| **Currency-conversion fees** | All multi-currency books | FX margin on non-base-currency trades (e.g. EU clients buying USD equities) | Low–medium — recurring, volume-linked |
| **Withdrawal / inactivity / other fees** | All (ESMA-restricted in EU) | Small recurring ancillary fees | Low |

The dominance of CFD and crypto spreads is why eToro's net contribution is a **high-beta proxy for retail risk appetite and crypto sentiment** rather than a stable subscription stream.

## CopyTrader and Social Trading

CopyTrader is eToro's signature product and the feature most discussed in the social-trading literature. The mechanism:

1. A user designates one or more "Popular Investors" they wish to copy.
2. They allocate a portion of their account to the copy (e.g., $1,000 to copy trader X, $500 to copy trader Y).
3. Whenever the copied trader opens a new position, the user's account opens a *proportionally sized* position in the same instrument at the prevailing market price — within the user's allocation budget.
4. When the copied trader closes a position, the user's mirrored position closes simultaneously.
5. Popular Investors earn a payout from eToro tied to the Assets Under Copy (AUC) following them.

The Popular Investor program creates an explicit incentive structure: traders are rewarded for *attracting copiers*, which depends on visible public performance, frequency of trades, and engagement on the social feed. This is the structural source of CopyTrader's behavioural problems, discussed below.

### Why CopyTrader produces *worse* aggregate retail outcomes

There are three structural reasons CopyTrader, despite the intuitive appeal of "copy a successful trader," tends to produce worse outcomes than even the modal retail trader managing their own book:

1. **Concentration on hot recent winners.** The discovery surface highlights traders who have been winning *in the recent past*, which is precisely the cohort whose positions are most extended and most mean-reverting. A user who follows the feed and copies the visible winner is structurally entering positions late in their run.
2. **Survivorship bias in the visible cohort.** Traders who have blown up are no longer visible in the discovery surface. The visible distribution of "Popular Investors" is therefore the *survivor* slice of a much larger pool, many of whom blew up in the run-up phase. Aggregate outcomes for the followers of *all* historical Popular Investors look much worse than outcomes for followers of *currently visible* Popular Investors.
3. **Incentive misalignment for the copied trader.** A Popular Investor earning fees on AUC has incentive to (a) trade more frequently than is optimal for their own P&L (engagement boosts visibility), (b) take asymmetric risks that produce a long visible win streak followed by a single large loss (the "blow-up insurance" of someone else's capital), and (c) not de-size their book even when their edge has decayed, because the AUC payout depends on the AUC, not the edge.

Academic studies of CopyTrader and analogous social-trading platforms (Wharton 2014; multiple follow-ons) have generally found that copied portfolios underperform unconcentrated benchmarks net of fees and that the longer the copy relationship runs, the worse the aggregate outcome — partly because the recent-winner-concentration effect resolves into mean reversion, partly because the most visible traders run higher leverage than their followers realise.

For a trader thinking through the [[itpm-trading-philosophy|ITPM-style argument]] about retail performance, CopyTrader is a particularly clean case: it is a structural mechanism that *appears* to solve the retail-edge problem but in fact compounds it.

## The ESMA Loss Disclosure

Under the [[esma|ESMA]] 2018 retail-CFD intervention rules, eToro — like every other EU-licensed CFD broker — must prominently display, on its homepage and across all marketing material, the percentage of its retail CFD accounts that lost money over the prior 12 months. The phrasing is standardised:

> *"XX% of retail investor accounts lose money when trading CFDs with this provider. You should consider whether you understand how CFDs work and whether you can afford to take the high risk of losing your money."*

The eToro number has historically printed in the **lower half** of the EU broker range — typically **51% to 77%** depending on the period sampled, the asset mix, and the underlying tape. Recent post-bull-market windows have tended to print at the lower end (around 51-65%), while flatter or bear tape pushes the number toward 70-77%. The exact figure is updated periodically.

### Why eToro's number sits at the lower end of the EU range

Several structural factors explain why eToro's loss percentage tends to be lower than CFD-day-trade-focused brokers:

- **Multi-asset client base** — Many eToro clients are predominantly long-equity or long-crypto holders rather than active CFD speculators. A client buying real equity and holding it for years is unlikely to print a CFD loss in any given 12-month window because they are not in the CFD universe.
- **Lower-leverage default behaviour** — eToro's UI defaults and guardrails encourage modest leverage; the modal CFD position is well below the regulatory cap.
- **CopyTrader long-bias** — Most CopyTrader allocations follow long-biased traders, and over a positive-tape window the modal copied position prints small wins.
- **Crypto bias** — A material share of eToro's CFD volume is in crypto, and during bull-tape years long-crypto CFD accounts print wins despite the funding-cost drag.

It is critical to note: even at the favourable end of the disclosure range, **the majority of retail CFD accounts at eToro lose money** in most years. The platform is widely cited in trader-interview discussions specifically because its disclosure is the *favourable* example — and the favourable example is still a majority-loss outcome. This is the data point [[itpm-trading-philosophy|ITPM]], [[anton-kreil|Kreil]], and similar professional-trader educators reference when arguing that retail derivative trading is structurally hostile.

### What the disclosure does not say

- The disclosure is **binary** — accounts that lost money vs. those that did not — and does not show the P&L *distribution*. Retail return distributions are heavy-tailed: most losers lose modestly, a small number of survivors win substantially, and an even smaller number of accounts blow up entirely. The blow-up tail is hidden by the binary disclosure.
- It covers **active CFD accounts only**. Dormant accounts and accounts that closed before the window are typically excluded, which understates the failure rate of the universe of people who *opened* an eToro CFD account.
- It is not adjusted for time-in-market, deposit size, or strategy. A 1% loss and a 90% loss both count as "lost money" in the same way.
- It does not cover the cash-equity, ETF, or crypto-spot product lines, only CFDs.

## What eToro Is Good vs Bad For

In the spirit of the [[professional-vs-retail-mindset|professional vs retail]] framing, eToro fits a particular niche cleanly and other niches very poorly.

### Reasonable use cases

- **Long-only equity and ETF investing in the EU/UK/Australia** with fractional shares and currency conversion built in
- **Crypto exposure** in jurisdictions where direct exchange access is awkward (with the wallet allowing withdrawal to self-custody)
- **Smart Portfolios** as a thematic ETF-substitute for users who do not want to construct baskets themselves
- **Education and exposure to the social-trading concept**, with paper trading available

### Poor use cases

- **Active CFD trading** — Spreads and overnight financing compound against the trader; the leverage cap (lower than offshore) plus the wider-than-DMA spread means the cost stack is particularly hostile
- **Listed-options trading at scale** — eToro's listed options are limited and the fees, when present, are uncompetitive vs [[interactive-brokers|IBKR]] or [[tastytrade]]
- **Algorithmic trading or API-driven execution** — eToro is not built for this; its API surface is shallow and not aimed at retail algo users
- **Crypto trading at low cost** — Native crypto exchanges have materially tighter spreads
- **CopyTrader as a wealth-building strategy** — For the structural reasons above, CopyTrader allocations tend to underperform broad-market benchmarks net of fees

The platform is therefore best understood as a **mass-market UX-first multi-asset platform** with a strong social-feed component, rather than as a serious tool for an [[itpm-trading-philosophy|ITPM-style]] book. Professional-trader educators specifically cite eToro's loss disclosures (a) as evidence of how retail-side platforms perform on aggregate, and (b) as a cautionary case study of how social-trading mechanics can actively work against follower outcomes.

## Economic Moat & Competitive Position

eToro is a [[financials]]-sector retail brokerage whose [[economic-moat|moat]] is **narrow but genuine**, and unusually for a broker it rests substantially on [[network-effects]]:

- **Social-trading network effects.** eToro operates the largest copy-trading network in the world. The value of the platform to a *copier* rises with the number and quality of visible "Popular Investors"; the value to a Popular Investor rises with the pool of potential copiers and the **Assets Under Copy (AUC)** they can attract. This two-sided flywheel — more copiers attract more Popular Investors and vice versa — is a real network effect that a new entrant cannot replicate by simply cloning the UI. It is the single most defensible asset eToro owns, and it is structurally absent from execution-only peers like [[interactive-brokers]] or [[robinhood]].
- **Brand and acquisition scale.** Two decades of heavy marketing built a globally recognised retail brand, lowering customer-acquisition friction relative to challengers and creating mindshare in the "social investing" category it effectively defined.
- **Multi-jurisdiction licensing as a barrier.** Operating regulated entities across CySEC (EU), FCA (UK), ASIC (Australia), and FINRA/SEC (US) is slow and costly to assemble. This regulatory footprint is a moat against would-be global competitors and a barrier eToro has already paid to cross.
- **Modest [[switching-costs]].** Once a user has an active copy relationship, a populated watchlist, social following, and tax lots on-platform, moving is friction-laden — though far weaker lock-in than a custody/banking relationship.

The moat is **contestable**: copy-trading mechanics can be (and have been) imitated; execution-only costs are lower at IBKR; native crypto exchanges undercut eToro's crypto spreads; and the network effect is concentrated in a retail-promotional product whose long-run follower outcomes are poor (see CopyTrader above). The durable defence is the network and brand; the threat is fee compression and competitors copying the social layer.

## Competitors / Peer Set

| Company | Model | Geography | Social feature | Cost profile | Regulation |
|---|---|---|---|---|---|
| **eToro (ETOR)** | Multi-asset CFD + cash equities + crypto, social-trading | EU, UK, AU, US, ROW | **CopyTrader / social feed — the category leader** | Wide spreads + FX + financing | CySEC, FCA, ASIC, SEC/FINRA |
| [[robinhood]] (HOOD) | Commission-free US equities, options, crypto | US (expanding) | Limited (lists, not copy) | PFOF-funded, low explicit cost | SEC/FINRA |
| [[interactive-brokers]] (IBKR) | Professional multi-asset, DMA, deep API | Global | None | Lowest spreads/commissions | SEC/FINRA + global |
| [[ig-markets]] (IGG) | CFD / spread-betting, longer track record | UK, EU, AU, ROW | Limited | Competitive CFD spreads | FCA, ASIC + ESMA |
| [[cmc-markets]] (CMCX) | CFD / spread-betting | UK, EU, AU | Limited | Competitive CFD spreads | FCA, ASIC + ESMA |
| [[coinbase]] (COIN) | Crypto-native exchange | Global | Limited | Tighter crypto spreads at scale | State + SEC scrutiny |

eToro's distinctive position is the **social/copy layer on top of a multi-asset book** — no peer matches the breadth (CFD + cash equity + crypto + social) in a single mass-market app, but each peer beats eToro on a specific axis (IBKR on cost, Coinbase on crypto, Robinhood on US-equity simplicity).

## Growth Drivers & Catalysts

- **Funded-account growth** — the cleanest leading indicator of future net contribution; 4.02M funded accounts at Q1 2026 (+12% YoY).
- **Crypto-cycle leverage** — net contribution is geared to crypto trading volume and spot prices; a sustained crypto bull cycle is the largest single upside driver (and the symmetric downside).
- **Product expansion** — options (US, rolling out in EU), fractional shares, ETF/Smart-Portfolio wrappers, and eToro Money banking features broaden the revenue base beyond CFD/crypto spreads.
- **Geographic expansion** — deeper US penetration (eToro USA) and new-market licensing extend the addressable base.
- **Net-contribution growth and operating leverage** — as the platform scales on a largely fixed cost base, incremental contribution should drop through to profit (FY2025 was net-income positive at $215.7M).
- **Recurring catalysts** — quarterly funded-account + net-contribution prints, crypto-market regime shifts, new-product launches, and lock-up/secondary-sale events on the post-IPO float.

## Bull Case vs Bear Case

### Bull case
- **Genuine social-trading [[network-effects]] moat** plus a globally recognised brand — defensible assets competitors cannot quickly replicate.
- **Multi-asset breadth in one app** (CFD + cash equity + crypto + social) captures the full retail wallet and cushions any single-product downturn.
- **Already profitable** — FY2025 net income $215.7M (EPS $2.58); Q1 2026 GAAP net income $82M (+37%), adjusted EPS $0.91 — unlike many growth-stage retail-fintech peers.
- **Funded-account growth** (4.02M, +12% YoY) compounds the future net-contribution base.
- **Crypto-cycle optionality** — a renewed retail-crypto boom drives outsized contribution growth.

### Bear case
- **Cyclical, crypto-levered revenue** — net contribution swings hard with retail risk appetite and crypto spot; the 2021→crypto-winter compression is the template, and the stock is down ~40% over the trailing year as of June 2026.
- **Regulatory pressure on the core economics** — [[esma|ESMA]] CFD leverage caps and inducement rules, possible PFOF restrictions, and crypto enforcement (the 2023 SEC settlement) all chip at the most profitable lines.
- **CopyTrader reputational risk** — the documented behavioural failure mode (poor aggregate follower outcomes) is a regulatory and brand liability if scrutiny intensifies.
- **Competition and fee compression** — IBKR undercuts on cost, native exchanges undercut on crypto spreads, and the social layer is imitable.
- **Post-IPO overhangs** — lock-up expiries and pre-IPO secondary sales pressured the 2025 float.

## Key Risks

- **Cycle / crypto sensitivity** — net contribution is a high-beta function of retail trading volume and crypto spot prices; a crypto winter or retail risk-off compresses revenue sharply.
- **Regulatory exposure** — ESMA/FCA CFD rules (leverage caps, mandatory loss disclosure, inducement bans), potential PFOF restrictions in the US, and ongoing crypto enforcement directly target eToro's highest-margin lines.
- **Competitive / fee compression** — execution-only peers ([[interactive-brokers]], [[robinhood]]) and crypto-native exchanges ([[coinbase]]) pressure spreads and commissions; the social layer is replicable.
- **CopyTrader behavioural failure mode** — as documented above, copied portfolios tend to underperform net of fees; this is both a reputational and a regulatory risk.
- **Concentration and overhangs** — revenue concentrated in cyclical CFD/crypto spreads; post-IPO lock-up and secondary-sale supply weighed on the stock.

## Valuation & How the Stock Trades

eToro is a **cyclical, profitable retail-brokerage** whose valuation is best framed off **net contribution and net income — not the gross "revenue" figure (~$13.8B FY2025), which is inflated by crypto pass-through cost of sales.** The market values ETOR as a high-beta proxy for retail trading activity and crypto sentiment rather than as a steady compounder:

- **Right top line** — net contribution (revenue net of crypto/trading costs) is the economically meaningful figure; gross revenue is a misleading optical number because crypto cost-of-sales dominates it.
- **Earnings base** — FY2025 net income $215.7M (EPS $2.58); Q1 2026 net contribution $258M (+19% YoY), GAAP net income $82M (+37%), adjusted EPS $0.91 vs ~$0.69 consensus — so an earnings/contribution multiple, not EV/revenue, is the relevant lens.
- **High beta to retail + crypto** — the stock correlates with [[robinhood]] (HOOD), [[coinbase]] (COIN), and crypto spot; quarterly funded-account and net-contribution growth are the swing factors. It is not a low-beta defensive financial.
- **Post-IPO behaviour** — priced at $52 (May 2025, ~$620M raised, ~$4.2B valuation), popped on debut then faded; down ~40% over the trailing year as of June 2026, with lock-up expiries and pre-IPO secondary sales as 2025 overhangs.
- **Dividend / capital return** — eToro is a young public company reinvesting in growth; it is traded for funded-account and contribution growth, not yield. (No established dividend; treat capital-return as immaterial to the thesis.)

> Figures above are as last disclosed (FY2025 / Q1 2026); eToro's results are high-volatility and cycle-dependent, so treat point figures as indicative of scale rather than current precise values.

## Regulatory History

| Year | Event |
|---|---|
| 2018 | ESMA retail-CFD intervention forces leverage caps, negative-balance protection, and mandatory loss disclosure |
| 2020 | UK FCA confirms the ESMA-style rules permanently in UK law |
| 2021 | Multiple ASIC enforcement actions on Australian CFD providers; eToro adjusts Australia product to comply |
| 2023 | SEC settlement with eToro USA Securities over crypto-asset offerings; eToro restricts available crypto in the US to a smaller list (BTC, ETH, BCH and a few others) |
| 2025 | Nasdaq IPO (May 2025) brings eToro under continuous public-company disclosure |
| 2024-2026 | EU MiCA implementation; eToro registers as a Crypto-Asset Service Provider in the EU |

The 2023 SEC settlement is particularly notable: it was part of the broader US enforcement wave against retail crypto offerings (alongside the [[coinbase]] and [[binance]] cases) and has constrained the US crypto product range eToro can offer.

## As a Public Company (ETOR) — 2025–2026

eToro priced its Nasdaq IPO on 2025-05-14 at $52 per share (above the indicated range), raising roughly $620M split between primary and selling shareholders at a ~$4.2B valuation; the stock popped strongly on debut before fading. As of June 2026 the shares trade well below the post-IPO highs (down roughly 40% over the trailing year), making ETOR a high-beta proxy for retail trading activity and crypto sentiment.

Key public-company datapoints:

- **FY2025:** net income $215.7M (+12% YoY); EPS $2.58. Headline "revenue" (~$13.8B) is gross and dominated by crypto pass-through cost; **net contribution** is the economically meaningful top line.
- **Q1 2026 (reported 2026-05-12):** net contribution $258M (+19% YoY, helped by commodities trading activity); GAAP net income $82M (+37%); adjusted EPS $0.91 vs ~$0.69 consensus; funded accounts 4.02M (+12% YoY).
- **Trading profile:** correlates with [[robinhood]] (HOOD), Coinbase (COIN), and crypto spot prices; quarterly funded-account and net-contribution growth are the swing factors. Lock-up expiries and secondary sales from pre-IPO holders were 2025 overhangs.

## Limitations and Criticisms

- **CFD economics structurally hostile** — The combination of spread + overnight financing + leverage compounds aggressively against active CFD positions
- **CopyTrader behavioural failure mode** — As discussed above, the structural design produces worse follower outcomes than the surface narrative implies
- **Limited withdrawal options on some crypto** — Historical and ongoing restrictions on moving crypto off-platform in some jurisdictions
- **Currency conversion fees** — Material on multi-currency books, especially for non-USD users buying US equities
- **Customer service consistency** — Mixed reviews; large user base across many languages stretches support quality
- **Marketing aggression** — Heavy ad spend has historically produced criticism that eToro's marketing emphasises social-trading upside while the legally mandatory loss disclosure receives less prominence

## Related

- [[esma]] — Architect of the mandatory loss-disclosure regime that makes eToro's retail-loss data publicly available
- [[robinhood]] — US analogue: commission-free retail platform, similar gamification critiques, but no CFD product line
- [[interactive-brokers]] — Professional-leaning broker contrast; lower spreads, deeper API, no CopyTrader
- [[ig-markets]] — UK-headquartered CFD broker with longer track record and similar ESMA disclosure obligations
- [[cmc-markets]] — UK-headquartered CFD broker; another comparison point
- [[itpm-trading-philosophy]] — Cites eToro's ESMA disclosure data as part of the empirical floor under the 70-90%-lose claim
- [[fees-and-friction]] — The structural drag visible in eToro CFD outcomes
- [[professional-vs-retail-mindset]] — eToro is the canonical retail-side platform in this contrast
- [[copy-trading]] — The product category eToro pioneered
- [[social-trading]] — Broader category context
- [[payment-for-order-flow]] — Relevant to the eToro USA equity model; ESMA largely banned it in EU
- [[crypto]] — Material share of eToro's revenue and product line
- [[behavioral-finance-overview]] — Theoretical lens on the CopyTrader failure modes
- [[financials]] — Sector
- [[economic-moat]] — Framework for eToro's competitive position
- [[network-effects]] — The social-trading flywheel underpinning the moat
- [[switching-costs]] — Modest user lock-in via copy relationships and on-platform holdings
- [[coinbase]] — Crypto-native competitor and correlated name

## Sources

_Content based on eToro public filings (Nasdaq prospectus and follow-up disclosures), eToro's mandatory ESMA retail-CFD loss disclosures published on its homepage and in all EU/UK marketing material, public regulatory filings (SEC, FCA, ASIC, CySEC), academic literature on social trading and CopyTrader, and references in [[itpm-trading-philosophy]] and the [[anton-kreil|Kreil]] interview corpus. No raw sources currently ingested into the wiki._

- eToro Q1 2026 results (GlobeNewswire, 2026-05-12): https://www.globenewswire.com/news-release/2026/05/12/3292651/0/en/etoro-reports-first-quarter-2026-results.html
- eToro investor relations: https://investors.etoro.com/
- eToro FY2025 earnings/revenue summary (Simply Wall St): https://simplywall.st/stocks/us/diversified-financials/nasdaq-etor/etoro-group/past
- Verified via Perplexity (sonar) and web search, 2026-06-10
