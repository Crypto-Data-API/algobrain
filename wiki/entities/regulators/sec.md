---
title: "SEC (Securities and Exchange Commission)"
type: entity
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [regulators, government, stocks, regulation, crypto]
aliases: ["Securities and Exchange Commission"]
entity_type: regulator
founded: 1934
headquarters: "Washington, D.C., USA"
website: "https://www.sec.gov"
related: ["[[cftc]]", "[[federal-reserve]]", "[[market-structure]]", "[[short-selling]]", "[[robinhood]]", "[[citadel]]", "[[exchange-data-sources]]", "[[bitcoin]]", "[[ethereum]]", "[[hyperliquid]]", "[[binance]]", "[[coinbase]]"]
---

# SEC (Securities and Exchange Commission)

The U.S. Securities and Exchange Commission (SEC) is the primary federal regulator overseeing securities markets, protecting investors, maintaining fair and orderly markets, and facilitating capital formation. Established in 1934 following the [[1929-crash|1929 stock market crash]], the SEC is the single most important regulatory body for anyone trading U.S. stocks, [[options]], or [[securities-lending|securities]]. It is the US counterpart of the EU's [[esma|ESMA]], Australia's [[asic|ASIC]], and the UK's [[fca|FCA]], and shares crypto and derivatives turf with the [[cftc|CFTC]].

## At a Glance

| Field | Detail |
|-------|--------|
| **Full name** | U.S. Securities and Exchange Commission |
| **Type** | Independent federal regulatory agency |
| **Founded** | 1934 (Securities Exchange Act of 1934) |
| **Headquarters** | Washington, D.C., USA |
| **Jurisdiction** | US securities markets — equities, bonds, options, mutual funds, ETFs, public-company disclosure |
| **Structure** | 5 commissioners (Senate-confirmed, 5-year staggered terms); no more than 3 from one party; one designated Chair |
| **Current Chair** | Paul Atkins (confirmed April 2025) |
| **Approx. budget** | ~USD $2.2 billion |
| **Approx. staff** | ~5,000 |
| **Self-regulatory orgs** | Oversees FINRA (broker-dealers) and the exchanges' own SROs |
| **Founding statutes** | Securities Act of 1933; Securities Exchange Act of 1934 |
| **Key data system** | EDGAR (public-company filings) |
| **Website** | https://www.sec.gov |

## Mandate and Structure

The SEC has a three-part statutory mission: **protect investors; maintain fair, orderly, and efficient markets; and facilitate capital formation.** It is governed by five commissioners appointed by the President and confirmed by the Senate to staggered five-year terms; no more than three may belong to the same political party, and the President designates one as Chair. The Chair sets the agenda, which is why a change of Chair (Gensler → Atkins) can swing the agency's posture dramatically (see the crypto section below).

The agency is organized into operating divisions and offices, the most trader-relevant being:

| Division / Office | Responsibility |
|-------------------|----------------|
| **Division of Enforcement** | Investigates and litigates securities-law violations — insider trading, fraud, manipulation, unregistered offerings |
| **Division of Corporation Finance** | Oversees disclosure (10-K, 10-Q, 8-K, S-1) and reviews filings |
| **Division of Trading and Markets** | Regulates exchanges, broker-dealers, [[market-structure]], clearing agencies, and SROs like FINRA |
| **Division of Investment Management** | Regulates mutual funds, ETFs, and investment advisers |
| **Division of Economic and Risk Analysis (DERA)** | Quantitative/economic analysis and market-structure research |
| **Office of the Whistleblower** | Administers bounty program (10-30% of sanctions over $1M) |

Unlike [[asic|ASIC]] (which directly regulates brokers with no SRO layer), the SEC delegates front-line broker-dealer oversight to **FINRA**, a self-regulatory organization the SEC supervises — structurally closer to a layered model than ASIC's single-regulator design.

## Key Rules That Affect Traders

| Rule | What it does | Who it hits |
|------|--------------|-------------|
| **Regulation NMS** | National Market System — order protection (no trade-throughs), market-data consolidation, access rules | All US equity traders; shapes routing and [[payment-for-order-flow]] economics |
| **Pattern Day Trader (PDT) rule** | Accounts flagged as PDTs (4+ day trades in 5 business days in a margin account) must keep ≥ $25,000 equity | Active retail day traders |
| **Regulation SHO** | Short-sale rules — locate requirement, close-out, the alternative uptick (circuit-breaker) rule | [[short-selling]] traders |
| **Reg T (with the Fed)** | Initial margin (50%) on securities purchases | Margin traders |
| **Rule 10b-5** | Anti-fraud catch-all; basis for insider-trading and manipulation cases | Everyone |
| **Regulation FD** | Fair disclosure — material info must be released broadly, not selectively | Affects how news reaches markets |
| **Limit Up-Limit Down (LULD) / market-wide circuit breakers** | Volatility halts on individual names and the broad index | All traders during stress |

## Overview

The SEC enforces federal securities laws including the Securities Act of 1933 and the Securities Exchange Act of 1934. It oversees stock exchanges like the nasdaq and NYSE, broker-dealers like [[robinhood]], investment advisers, mutual funds, and public company disclosures. The SEC also regulates [[market-structure]], insider trading rules, and [[short-selling]] practices.

## Key Functions

- **Enforcement**: Investigates and prosecutes securities fraud, insider trading, market manipulation, and accounting fraud. Notable cases include actions against Enron, Bernie Madoff, and numerous crypto projects.
- **Disclosure Requirements**: Mandates public companies file quarterly (10-Q) and annual (10-K) reports, providing the transparency fundamental investors rely on.
- **Market Structure Oversight**: Regulates [[payment-for-order-flow]], dark pools, [[algorithmic-trading]], and exchange operations.
- **Rulemaking**: Proposes and implements rules governing markets, most recently addressing crypto asset classification and [[payment-for-order-flow]] reform.

## EDGAR Filing System

All US public company filings are submitted through EDGAR (Electronic Data Gathering, Analysis, and Retrieval). Companies listed on NYSE and NASDAQ must file:

| Filing | Description | Deadline |
|--------|-------------|----------|
| **10-K** | Annual report | 90 days after fiscal year end |
| **10-Q** | Quarterly report | 45 days after quarter end |
| **8-K** | Major events report | Promptly upon occurrence |

A typical US fiscal year ends December 31 (though many companies use other fiscal year-ends). Filing deadlines also vary by filer category: large accelerated filers (public float ≥ $700M) face a 60-day 10-K and 40-day 10-Q deadline, accelerated filers 75/40 days, and non-accelerated filers the 90/45 days shown above. Additional filings include proxy statements (DEF 14A), insider transactions (Forms 3/4/5), beneficial ownership disclosures (Schedules 13D/13G), and registration statements (S-1).

### EDGAR Data Access

| Resource | URL |
|----------|-----|
| EDGAR Data Docs | https://www.sec.gov/os/accessing-edgar-data |
| Company Tickers (CIK codes — JSON) | https://www.sec.gov/files/company_tickers.json |
| Company Search | https://www.sec.gov/edgar/browse/?CIK=0001018724 |
| SEC API (bulk ZIP downloads) | https://www.sec.gov/edgar/sec-api-documentation |
| Daily Archives (ZIP) | https://www.sec.gov/Archives/edgar/Feed/ |
| Full Indexes (ZIP) | https://www.sec.gov/Archives/edgar/full-index/ |
| Single Company Submissions (JSON) | https://data.sec.gov/submissions/CIK0001018724.json |
| Company Financial Facts (XBRL JSON) | https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json |
| SEC Forms List | https://www.sec.gov/forms |
| RSS Feeds | https://www.sec.gov/about/sec-rss |

For the full cross-exchange data source reference, see [[exchange-data-sources]].

## SEC and Crypto — Enforcement Era (2021-2024)

The SEC's approach to cryptocurrency regulation under Chair Gary Gensler (2021-2024) was defined by "regulation by enforcement" — using litigation rather than rulemaking to establish jurisdiction over digital assets. This period produced the most consequential regulatory actions in crypto history.

### The Howey Test and Token Classification

The SEC applies the **Howey Test** (from *SEC v. W.J. Howey Co.*, 1946) to determine if a digital asset is a security:

1. Investment of money
2. In a common enterprise
3. With an expectation of profits
4. Derived from the efforts of others

Under Gensler, the SEC argued that **most tokens** (excluding [[bitcoin]]) satisfy Howey and are therefore unregistered securities. This interpretation, if fully enforced, would require exchanges to register as securities exchanges and tokens to be registered as securities — fundamentally incompatible with how crypto markets operate.

### Major SEC Crypto Enforcement Actions

| Case | Date | Target | Outcome | Market Impact |
|------|------|--------|---------|--------------|
| **SEC v. Ripple (XRP)** | Dec 2020 – Jul 2023 | Ripple Labs | Partial victory for Ripple: Judge Torres ruled XRP sales on exchanges are NOT securities (programmatic sales); direct institutional sales ARE securities | XRP rallied ~75% on ruling day; established that secondary market token trading may not constitute securities transactions |
| **SEC v. Coinbase** | Jun 2023 | [[coinbase]] | Sued for operating as unregistered exchange, broker, and clearing agency; alleged 13 tokens are securities. **Dismissed with prejudice on Feb 21, 2025** under the new (Atkins-era) SEC — no fines, Coinbase kept its business model | COIN stock dropped ~12% on filing; rallied on the 2025 dismissal |
| **SEC v. Binance** | Jun 2023 | [[binance]], CZ | Charged with operating unregistered exchange, offering unregistered securities (BNB, BUSD), commingling customer funds. **SEC filed to dismiss the case on May 29, 2025** | BNB dropped ~8% on filing; CZ had separately pled guilty to BSA violations in a 2023 DOJ case ($4.3B combined settlement) |
| **Kraken staking** | Feb 2023 | Kraken | SEC sued over staking-as-a-service program | Kraken settled for $30M, shut US staking service; precedent for staking = security |
| **Terraform Labs** | Feb 2023 | Do Kwon, Terraform | Sued over UST/LUNA collapse | Terraform found liable; Do Kwon extradited |
| **Various token issuers** | 2021-2024 | Multiple ICOs, tokens | Wells notices and enforcement actions against dozens of projects | Created chilling effect on US-based token launches |

### SEC v. Ripple — Detailed Timeline and Trading Implications

The Ripple case is the most important crypto securities case because it partially defined the boundary between securities and non-securities:

| Date | Event | XRP Price Impact |
|------|-------|-----------------|
| Dec 2020 | SEC files lawsuit against Ripple | XRP -60% over following weeks; delisted from major US exchanges |
| 2021-2023 | Discovery phase, pre-trial motions | XRP traded as "litigation discount" — underperformed market |
| Jul 13, 2023 | **Judge Torres ruling**: Programmatic sales on exchanges ≠ securities; institutional sales = securities | XRP +75% in 24 hours; broader altcoin rally |
| Oct 2023 | SEC drops case against Ripple executives Garlinghouse and Larsen | XRP +5% |
| 2024 | SEC appeals certain aspects; case continues | Lingering uncertainty caps XRP upside |
| Mar–Aug 2025 | Under the Atkins-era SEC, both sides drop their appeals; the case is **fully resolved/dismissed by August 2025**, ending the four-year battle | XRP rallied into 2025 as the litigation discount evaporated |

**Trading lesson**: The Ripple ruling established that secondary market crypto trading may not constitute securities transactions — a precedent that weakens the SEC's case against exchanges like [[coinbase]] and [[binance]]. Tokens named in SEC enforcement actions often exhibit a pattern: sharp initial dump (10-30%) → extended litigation discount → rally on favorable ruling or settlement.

### Spot Bitcoin ETF Approval (January 2024)

After a decade of rejections, the SEC approved **11 spot [[bitcoin]] ETFs** on January 10, 2024. This was a watershed moment:

- **Approved issuers**: BlackRock (iShares), Fidelity, Invesco, ARK/21Shares, Bitwise, VanEck, Valkyrie, WisdomTree, Franklin Templeton, Hashdex, Grayscale (conversion)
- **BTC price impact**: Rallied from ~$44K to ~$73K over the following 2 months as institutional inflows materialized
- **Cumulative inflows**: Over $50B+ in net inflows within the first year
- **Trading implication**: ETF flows (tracked via daily creation/redemption data) became a leading indicator for BTC price direction; GBTC outflows initially offset new ETF inflows

### Ethereum ETF Status

Following the Bitcoin ETF approval, the SEC approved spot [[ethereum]] ETFs in May 2024:
- Initial inflows were more modest than BTC ETFs
- ETH ETFs did not include staking yield (SEC concern over staking = security)
- The approval signaled that ETH is treated more as a commodity than a security — significant for the broader Howey Test debate

### Gary Gensler Departure and the Atkins-Era Reversal (2025-2026)

Gary Gensler departed as SEC Chair in January 2025. **Paul Atkins** was confirmed as the new SEC Chair in April 2025, ushering in a sharply more accommodative posture toward crypto. The post-Gensler SEC has, through 2025-2026:
- **Dropped nearly all of its major crypto enforcement actions** — the cases against [[coinbase]] (dismissed with prejudice Feb 2025), [[binance]] (dismissal filed May 2025), and Ripple (fully resolved by August 2025) were all wound down, along with investigations into Kraken, Robinhood, OpenSea, and others
- Formed a dedicated **Crypto Task Force** (led initially by Commissioner Hester Peirce) for rulemaking rather than enforcement-first
- Began exploring frameworks for token registration and exemptions that don't require full securities compliance
- Put staking-as-a-service cases under reconsideration; issued staff guidance softening prior positions
- Coordinated with Congress's market-structure efforts (the **CLARITY Act**, which passed the House 294-134 on July 17, 2025) that would split crypto oversight with the [[cftc]]

This shift has broadly positive implications for crypto markets, though the durable statutory framework still depends on Senate passage of market-structure legislation as of mid-2026. (Verified via WebSearch, 2026-06-11.)

## Implications for Hyperliquid and DEX Perps

[[hyperliquid]] occupies a particularly complex regulatory position:

1. **No KYC**: Hyperliquid does not require identity verification, making it inaccessible to regulators through traditional exchange compliance channels
2. **TradFi perps**: Hyperliquid offers [[perpetual-futures]] on stocks (AAPL, TSLA) and commodities — these may fall under [[sec]] (stocks) or [[cftc]] (commodities/derivatives) jurisdiction
3. **Offshore operation**: Hyperliquid operates without a US entity, similar to early [[binance]] and BitMEX
4. **Enforcement precedent**: The SEC sued BitMEX (via DOJ) and obtained guilty pleas from founders despite offshore incorporation. Hyperliquid's team is more anonymous but not immune.
5. **DEX defense**: Hyperliquid could argue it is a decentralized protocol (not a company operating an exchange), but its L1 chain has identifiable validators and a development team

**Trading risk**: SEC or [[cftc]] enforcement action against Hyperliquid would likely cause a sharp [[hype-token|HYPE]] selloff (30-50%+) and potentially force platform changes (geoblocking US users, removing TradFi perps). This is a non-trivial tail risk for any HYPE position or large Hyperliquid exposure.

## Trading Relevance — SEC as Market Mover

SEC announcements consistently move crypto markets by 5-15%:

| Event Type | Typical Impact | Duration |
|-----------|---------------|----------|
| **New enforcement action** (against major exchange) | -8 to -15% on named token; -3 to -8% on BTC | Initial dump 1-4 hours; recovery over 1-4 weeks |
| **Favorable court ruling** (e.g., Ripple) | +10 to +30% on named token; +3-8% on alts broadly | Rally 1-3 days |
| **ETF approval/rejection** | +15 to +30% (approval) or -5 to -15% (rejection) | Sustained trend over weeks/months |
| **Chair/commissioner change** | +5 to +10% (crypto-friendly appointment) | Gradual repricing over weeks |
| **Wells notice** (pre-enforcement warning) | -10 to -20% on named token | Lingering discount until resolution |

**Pattern for traders**: SEC enforcement actions often create buying opportunities after the initial dump. The market tends to overreact to enforcement news (pricing in worst-case outcomes), then recover as legal proceedings reveal more nuance. The Ripple, Coinbase, and Binance cases all exhibited this pattern.

Traders must understand SEC regulations around pattern day trading (PDT rule), short sale restrictions (Reg SHO), insider trading prohibitions, and disclosure requirements. The SEC's enforcement actions and rulemaking directly impact [[market-structure]] and trading costs. Its involvement in the [[gamestop-short-squeeze]] investigation and ongoing crypto regulatory battles make it a constant presence in modern markets.

## Related

- [[cftc]] — Partner/rival regulator for derivatives and crypto
- [[esma]] — EU analogue (securities + markets) at the supranational layer
- [[asic]] — Australian analogue with a broader single-regulator mandate
- [[regulation]] — Overview of financial regulation and how it shapes trading
- [[bitcoin]] — Spot BTC ETF approval transformed institutional access
- [[bitcoin-etf]] — The 11 spot BTC ETFs the SEC approved in Jan 2024
- [[ethereum]] — ETH ETF approval and commodity vs. security debate
- [[hyperliquid]] — DEX perps platform with regulatory exposure
- [[hype-token]] — HYPE token risk includes SEC/CFTC enforcement
- [[binance]] — Subject of major SEC enforcement action
- [[coinbase]] — Subject of major SEC enforcement action
- [[risk-management]] — Regulatory/enforcement risk as a portfolio consideration
- [[counterparty-risk]] — Regulatory risk as component of platform assessment
- [[market-structure]] — SEC shapes US market structure rules

## Sources

- SEC official site and EDGAR documentation — https://www.sec.gov, https://www.sec.gov/os/accessing-edgar-data
- *SEC v. W.J. Howey Co.*, 328 U.S. 293 (1946) — the Howey Test
- Court documents and dockets: SEC v. Ripple Labs, SEC v. Coinbase, SEC v. Binance
- SEC press releases and Crypto Task Force statements (2025-2026)
- 2025 case dismissals (Coinbase, Binance, Ripple), Paul Atkins's confirmation as Chair, and CLARITY Act House passage verified via WebSearch, 2026-06-11.
