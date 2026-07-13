---
title: "Tiger Brokers"
type: entity
created: 2026-04-13
updated: 2026-06-18
status: excellent
tags: [company, exchange, stocks, options, futures, crypto, ai-trading, brokerage]
aliases: ["Tiger Brokers", "Tiger Trade", "Tiger Finance", "UP Fintech", "UP Fintech Holding", "TIGR"]
entity_type: company
founded: 2014
headquarters: "Singapore"
website: "https://www.tigerbrokers.com"
ticker: "TIGR"
exchange: "NASDAQ"
sector: "Financials"
industry: "Capital Markets / Online Brokerage"
related: ["[[hyperliquid-vs-asterdex-vs-tiger-brokers]]", "[[ai-trading-agents]]", "[[crypto-markets]]", "[[artificial-intelligence]]", "[[financials]]", "[[futu-holdings]]", "[[interactive-brokers]]", "[[robinhood]]", "[[charles-schwab]]", "[[economic-moat]]", "[[switching-costs]]", "[[network-effects]]"]
---

# Tiger Brokers

**Tiger Brokers** is the consumer brand of **UP Fintech Holding Limited** (NASDAQ: **TIGR**), a [[financials]]-sector online brokerage founded in 2014 by Wu Tianhua and headquartered in Singapore. It is a Chinese-founded, US-listed digital broker that built its early franchise serving globally-mobile Chinese investors and has since expanded across Singapore, Southeast Asia, Australia, the US, and other markets. It holds **81 licenses and qualifications globally** and has over **1 million users worldwide**. Unlike decentralized perp DEXs like [[hyperliquid|Hyperliquid]] and [[asterdex|AsterDEX]], Tiger Brokers is a **regulated, centralized brokerage** operating as a traditional financial intermediary. Its core product is the **Tiger Trade** app, which provides access to stocks, ETFs, futures, options, and cryptocurrencies in a single "Prime" account.

As an investable equity, TIGR is a **retail-brokerage business** whose earnings are geared to client trading activity, client-asset growth, and net interest income on customer cash — overlaid with a meaningful China/US regulatory and geopolitical overhang typical of US-listed Chinese ADRs. Tiger Brokers is best known for competitive fees, multi-market access, and increasingly AI-assisted trading tools. It is *not* primarily designed for automated high-frequency trading, but has expanded into AI-driven analysis and offers an open API for custom workflows.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: TIGR |
| **Founded** | 2014 |
| **Headquarters** | Singapore |
| **Users** | 1 million+ worldwide |
| **Licenses** | 81 global licenses and qualifications |
| **Products** | Stocks, ETFs, options, futures, crypto, bonds, treasuries |
| **Key App** | Tiger Trade |
| **AI Tool** | TigerGPT (DeepSeek-R1 powered) |
| **Crypto License** | Hong Kong SFC-licensed for virtual assets |
| **Exchange Access** | NYSE, NASDAQ, HKEX, SGX, ASX, A-shares (Stock Connect) |

---

## Business Overview & Segments

UP Fintech operates a digital, asset-light **retail-brokerage** model: it acquires self-directed investors through the Tiger Trade app, monetises their trading and balances, and layers on adjacent fee businesses. Revenue is not from a single product but from several reinforcing lines whose mix shifts with market activity and the rate cycle.

| Revenue line | What it is | Driver / sensitivity |
|---|---|---|
| **Commissions** | Per-trade fees on stocks, ETFs, options, futures | Geared to client trading volume / market activity; competitive-fee positioning compresses per-trade economics but drives volume |
| **Financing & interest income** | Net interest on customer cash balances, margin lending, securities lending | Geared to interest rates and client-asset levels — a major swing factor through a rate cycle |
| **Other / fee income** | IPO subscription & distribution, fund/ESOP (employee stock-plan) services, wealth-management, market-data and AI tooling | Diversifies away from pure transaction reliance; ESOP and IPO underwriting tie TIGR to primary-market activity in Asia |

The platform breadth — stocks, ETFs, options, futures, crypto, bonds, and treasuries in one "Prime" account — is the customer-acquisition hook; the **client-asset base** (balances and AUM) is the durable monetisation engine, because it compounds both interest income and recurring fee revenue independent of any single quarter's trading.

## Economic Moat & Competitive Position

Tiger Brokers has a **narrow** [[economic-moat|economic moat]] — real but contestable, of the kind typical for digital brokers:

- **Brand and trust among globally-mobile Chinese investors** — its original and still-core demographic; a regulated, NASDAQ-listed broker with a polished multi-asset app is differentiated versus local and offshore alternatives in that niche.
- **[[switching-costs]] of funded accounts** — once a client funds an account, holds positions, sets up tax/reporting and (for some) ESOP/IPO access, moving brokers is friction-heavy. Funded-account stickiness is the most reliable moat component for any broker.
- **Modest [[network-effects]]** — the social/community and content features (feeds, discussion, shared watchlists) create mild engagement loops, but these are weak compared with a true platform network effect; they aid retention more than they create a winner-take-all dynamic.
- **Multi-market license stack** — 81 global licenses/qualifications is a regulatory barrier that is slow and costly for a new entrant to replicate, especially the cross-jurisdiction breadth (HK SFC, Singapore, Australia, US).

The moat is **not wide**: brokerage is fundamentally a price- and feature-competitive business, client acquisition costs are high, and the closest peer [[futu-holdings]] competes for an overlapping customer base with a similar model and larger scale. The defensible core is *funded-account stickiness + license breadth*; the threat is fee compression and a better-capitalised competitor.

---

## Trading Capabilities

Tiger Trade's single Prime account supports:

- **US and HK stocks** (including fractional shares), ETFs, and funds
- **US options** with multi-leg strategies, options screeners, P&L analysis, and Greeks
- **Futures** on multiple global markets
- **Crypto** (BTC, ETH, and others) — licensed by the Hong Kong Securities and Futures Commission (SFC)
- **Bonds and US Treasuries**

### Global Exchange Access

| Exchange | Markets |
|----------|---------|
| NYSE / NASDAQ | US stocks, ETFs, options |
| HKEX | Hong Kong stocks |
| SGX | Singapore stocks |
| ASX | Australian stocks |
| A-shares | Via Stock Connect |

---

## Options Trading

Tiger Trade's options suite is among the more complete in the retail brokerage space:

- Call and put options on US markets
- **Multi-leg strategies** supported (verticals, iron condors, straddles, etc.)
- Real-time L1 quotes (L2 available for funded accounts)
- **Options screeners** and Greeks analytics
- **Demo trading mode** for paper trading options strategies

**Limitation:** options automation requires either the Open API with custom code or third-party integration — Tiger does not offer a native drag-and-drop options bot builder.

---

## AI & Automation Tools

Tiger Brokers is not a native "trading bot" platform, but has introduced several AI-driven tools:

### TigerGPT

An AI-powered analysis assistant upgraded with **DeepSeek-R1** in March 2025. TigerGPT synthesizes real-time stock prices, filings, analyst reports, technical patterns, and sentiment into actionable insights. It passed SFC review for use in Hong Kong.

**Important:** TigerGPT provides market insights and analysis but **does not execute trades automatically**. It is a research/analysis tool, not an autonomous trading agent.

### Auto-Invest

Dollar-cost averaging tool for scheduled investments in stocks and ETFs, starting from $2. Suitable for long-term passive investing but lacks the dynamic risk management needed for active trading.

### Open API

Available for developers to build custom automated strategies and risk management systems. For sophisticated options or multi-asset automation, the Open API needs to be paired with a custom execution layer.

### Limitations

Compared to [[hyperliquid|Hyperliquid]] and [[asterdex|AsterDEX]], Tiger Brokers **lacks built-in trading bots**. The Auto-invest feature is low-risk for long-term investors. For active automated trading, developers must build on the Open API — the platform offers no native grid, DCA, or signal bots.

---

## Fee Structure

Tiger Brokers is known for **competitive and transparent fees**, though specific rates vary by market:

- No hidden fees beyond handling fees for crypto
- Free fund withdrawals (banks may charge their own fees)
- Commission-competitive vs peers for US stocks and options
- Detailed fee schedules available on the Tiger Trade platform

---

## Competitors / Peer Set

| Company | Relationship to TIGR | Notes |
|---|---|---|
| [[futu-holdings]] (FUTU) | **Closest comparable** | Also a US-listed, Chinese-founded online broker (Moomoo / Futubull); larger scale and the primary head-to-head; TIGR and FUTU trade as a paired China-broker theme |
| [[interactive-brokers]] (IBKR) | Global multi-asset peer | Deeper professional/API tooling, lower financing costs, broader instrument range; the benchmark for serious multi-asset traders |
| [[robinhood]] (HOOD) | US retail peer | Commission-free, gamified, US-centric; overlaps on retail mindshare and crypto, less multi-market breadth |
| [[charles-schwab]] (SCHW) | Incumbent US broker | Vastly larger, full-service; relevant as the scale/cost-of-capital benchmark rather than a direct demographic competitor |

TIGR's distinctive position is the **multi-market, multi-asset app aimed at globally-mobile Chinese and Asian investors**, sitting between IBKR's professional breadth and HOOD's consumer simplicity. Its sharpest competitive pressure is from [[futu-holdings]], which targets a heavily overlapping base.

## Growth Drivers & Catalysts

- **Funded-account growth** — the headline operating metric; net new funded accounts each quarter are the leading indicator of future revenue.
- **Client-asset / AUM growth** — rising balances compound both interest income and recurring fee revenue; the most durable growth lever.
- **Geographic expansion** — diversification beyond the original Chinese-investor base into Singapore/SEA, Australia, the US, and other licensed markets reduces single-jurisdiction risk.
- **Interest-income leverage to rates** — net interest on customer cash is a powerful tailwind in a higher-rate environment and a headwind as rates fall.
- **Crypto + AI tooling** — Hong Kong SFC-licensed virtual-asset trading and the TigerGPT (DeepSeek-R1) assistant differentiate the product and may lift engagement/retention.
- **Adjacent fee businesses** — IPO distribution, ESOP/employee-stock-plan services, and wealth management diversify revenue beyond transaction commissions.
- **Recurring catalysts** — quarterly results (funded accounts, client assets, net income), regulatory/license announcements, and broad China-ADR sentiment swings.

## Bull Case vs Bear Case

### Bull case
- Sustained funded-account and client-asset growth in an under-penetrated, globally-mobile Asian investor base.
- Multi-asset, multi-market breadth in one regulated app is a genuine differentiator and raises [[switching-costs]].
- Competitive, transparent fees drive volume; net interest income provides a high-margin, rate-geared earnings layer.
- License-stack breadth (81 qualifications) is a slow-to-replicate regulatory moat enabling further geographic expansion.
- AI tooling (TigerGPT) and crypto access keep the product current and aid retention.

### Bear case
- **China regulatory overhang** — cross-border online brokerage of mainland Chinese clients has drawn regulatory scrutiny; rule changes can directly constrain client acquisition.
- **Competition from [[futu-holdings]]** — a larger, well-capitalised peer fighting for the same customers compresses margins and acquisition economics.
- **Rate-cycle sensitivity** — a large slice of earnings is net interest income; falling rates erode a high-margin revenue line.
- **Geopolitical / delisting tail risk** — as a US-listed Chinese-founded ADR, TIGR carries the HFCAA-style audit/delisting and US-China tension tail risk common to the cohort.
- **Cyclicality** — brokerage revenue is geared to trading activity and market sentiment; a risk-off retail environment hits volumes and balances simultaneously.

## Valuation & How the Stock Trades

TIGR trades as a **growth-brokerage equity** whose earnings are doubly geared — to client **trading activity** and to **net interest income** on customer cash — so the multiple expands and compresses with both market-volume sentiment and the rate outlook. Mechanically (qualitatively only — no current figures are ingested in this wiki):

- **High-beta China-ADR sentiment proxy** — the stock moves with the broader US-listed Chinese-ADR risk appetite and with retail-trading sentiment; idiosyncratic broker news is often swamped by macro China/US headlines.
- **Pairs behaviour with [[futu-holdings]]** — TIGR and FUTU frequently trade as a paired theme; relative results (funded accounts, client assets) drive relative performance, making FUTU the key read-across name.
- **Earnings drivers** — funded-account adds, client-asset growth, trading volume, and net interest income are the swing variables each print; commission-rate compression is a structural watch-item.
- **Capital return / beta** — as a growth-stage broker, capital is largely reinvested rather than returned; dividend (if any) is not the story. Beta is high relative to a diversified index given the China-ADR and retail-trading sensitivities. *Treat all valuation/beta characterisation as qualitative; no precise figures are sourced here.*

---

## Security & Regulation

- **NASDAQ-listed** (TIGR) — publicly accountable with SEC reporting requirements
- **81 global licenses** and qualifications
- **SFC-licensed** in Hong Kong for virtual assets
- **Custodial model** — funds held by the broker, not self-custody
- Well-established data security practices for a regulated brokerage
- **KYC required** — standard identity verification for all accounts

---

## Key Risks

**Company / equity risks**

- **Regulatory (China & US)**: Cross-border online brokerage of mainland Chinese clients has faced regulatory scrutiny; rule changes can directly throttle client acquisition. As a US-listed Chinese-founded ADR, TIGR also carries HFCAA-style audit/delisting and US-China-tension tail risk.
- **Competition**: [[futu-holdings]] is a larger, well-capitalised peer competing for an overlapping base; fee compression across the brokerage industry pressures per-trade economics.
- **Rate sensitivity**: A meaningful share of earnings is net interest income on customer cash — a tailwind in high-rate environments and a headwind as rates fall.
- **Cyclicality**: Revenue is geared to trading activity and client-asset levels; a risk-off retail environment compresses both at once.
- **Custodial / counterparty risk**: Funds are held by the broker (not self-custody) — standard brokerage counterparty exposure.

**Product / usability risks**

- **Limited automation**: No native trading bots; auto-execution requires developer work via Open API.
- **Sparse education resources**: Flagged as a weakness for less experienced users.
- **No MetaTrader support**: Traders accustomed to MT4/MT5 ecosystems will need to adapt.
- **Not suited for high-frequency crypto trading**: Optimised for traditional multi-asset brokerage, not crypto-native automation.

---

## Ideal For

Retail investors and traders who want a **unified account** for stocks, options, futures, and crypto under a regulated umbrella. Particularly suited for:

- **Options traders** wanting a full-featured, low-fee broker with AI-assisted research
- **Multi-asset portfolio managers** who need stocks + crypto + bonds in one account
- **Long-term investors** using Auto-invest DCA strategies
- **Developers** who can build on the Open API for custom automation

**Not suited for:** high-frequency algorithmic trading, automated crypto perpetuals trading, or traders who want native bot infrastructure.

---

## Notable History & Milestones

| Year | Milestone |
|---|---|
| 2014 | Founded by Wu Tianhua; UP Fintech / Tiger Brokers launches, initially serving globally-mobile Chinese investors |
| 2015-2018 | Tiger Trade app scales; multi-market access (US, HK) and margin/financing build out the brokerage model |
| 2019 | **NASDAQ IPO under ticker TIGR** — UP Fintech Holding becomes a publicly-listed online broker |
| 2019-2023 | Geographic expansion (Singapore HQ, Australia, Southeast Asia); license stack grows toward 81 qualifications; adds options, futures, bonds, ESOP and IPO-distribution businesses |
| 2023-2024 | Hong Kong SFC virtual-asset (crypto) licensing; crypto added to the Prime account |
| Mar 2025 | **TigerGPT upgraded with DeepSeek-R1**; passes SFC review for use in Hong Kong |
| 2025-2026 | Continued funded-account and client-asset growth; AI tooling and multi-market expansion as the strategic focus |

---

## Related

- [[financials]] — sector
- [[futu-holdings]] — closest comparable; US-listed Chinese-founded online broker
- [[interactive-brokers]] — global multi-asset professional peer
- [[robinhood]] — US commission-free retail peer
- [[charles-schwab]] — incumbent full-service broker / scale benchmark
- [[economic-moat]] — moat framing (narrow, funded-account stickiness)
- [[switching-costs]] — the core retention mechanism for brokers
- [[network-effects]] — modest social/community engagement loops
- [[hyperliquid-vs-asterdex-vs-tiger-brokers]] — Platform comparison
- [[hyperliquid]] — Leading decentralized perp DEX
- [[asterdex|AsterDEX]] — Second-largest perp DEX
- [[ai-trading-agents]] — AI agent trading architectures
- [[crypto-markets]]

## Sources

- Tiger Brokers corporate documentation and product pages
- Platform comparison reviews (Bitsgap, broker comparison sites)
- TigerGPT product announcements
- General market knowledge; no specific wiki source ingested yet for the equity/financials.
