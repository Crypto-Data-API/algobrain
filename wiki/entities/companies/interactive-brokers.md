---
title: "Interactive Brokers"
type: entity
created: 2026-04-15
updated: 2026-06-18
status: excellent
tags: [company, exchange, stocks, options, algorithmic, margin]
entity_type: company
founded: 1978
headquarters: "Greenwich, Connecticut, USA"
website: "https://www.interactivebrokers.com"
ticker: "IBKR"
exchange: "NASDAQ"
sector: "Financials"
industry: "Investment Banking & Brokerage"
aliases: ["Interactive Brokers", "IBKR", "IB", "Interactive Brokers Group"]
related: ["[[options]]", "[[algorithmic-trading]]", "[[margin]]", "[[futures]]", "[[charles-schwab]]", "[[robinhood]]"]
---

Interactive Brokers (NASDAQ: IBKR) is one of the world's largest electronic brokerage firms, founded in 1978 by Thomas Peterffy, a Hungarian-born engineer and pioneer of electronic trading. The company provides access to over 150 markets in 33 countries from a single unified account, offering trading in stocks, [[options]], [[futures]], currencies, bonds, funds, and cryptocurrencies. It is widely regarded as the broker of choice for professional traders, quantitative funds, and cost-conscious institutional investors due to its industry-leading low costs, comprehensive API access, and deep market connectivity.

## Business Overview & Segments

Interactive Brokers is best understood not as a commission business but as a **net-interest-income machine wrapped around an ultra-low-cost execution platform**. The brokerage charges famously thin commissions and routes for best execution; the bulk of pre-tax profit comes from interest earned on customer cash and [[margin]] loan balances, plus securities lending. The legacy market-making arm (Timber Hill) — once the firm's profit core — has been almost entirely wound down to remove proprietary-trading risk and capital drag, leaving a cleaner, capital-light agency model.

| Profit / business line | What it is | Role in the franchise |
|---|---|---|
| **Commissions** | Per-share / per-contract fees on equities, [[options]], [[futures]], forex, bonds, crypto across 150+ markets | Low-margin by design; the customer-acquisition hook, kept cheap to win volume |
| **Net interest income (NII)** | Spread earned on idle client cash and on [[margin]] lending balances (IBKR lends at the industry's lowest rates yet keeps a wide spread over its own funding cost) | The real profit engine — the single largest driver of earnings and the key swing factor with the Fed rate path |
| **Securities lending** | Lending out fully-paid and margin shares to short sellers | High-margin ancillary revenue that scales with client equity |
| **Market making (Timber Hill, legacy)** | Automated options/equity market-making that originated the firm | Largely wound down; no longer a meaningful or strategic profit source |
| **Client segments** | IBKR Pro (active/professional, smart-routed) vs IBKR Lite (commission-free retail); individuals, hedge funds & prop firms, RIAs, and introducing brokers running on IBKR's white-label rails | Diversified, sticky, globally distributed; introducing-broker and institutional channels add scale without retail acquisition cost |

As of 2024–25 the platform served on the order of millions of accounts with hundreds of billions in client equity (see 2025-2026 Developments for the latest disclosed figures). The detailed product, platform, and fee mechanics follow below.

## Overview

Interactive Brokers grew out of Thomas Peterffy's early experiments with computerized options trading in the 1970s and 1980s. Peterffy was one of the first traders to use handheld computers on the floor of the American Stock Exchange, and he built automated market-making systems that became the foundation of Timber Hill, the market-making arm that preceded the brokerage business. Interactive Brokers launched its electronic brokerage platform in 1993, initially serving professional traders and institutions.

The company went public in 2007 via an IPO on NASDAQ. As of 2024, Interactive Brokers had approximately 2.6 million client accounts, over $400 billion in client equity, and executed roughly 3 million trades per day. Thomas Peterffy, who remains chairman, is one of the wealthiest people in the United States with an estimated net worth exceeding $25 billion, built almost entirely from the company he founded.

Interactive Brokers differentiates itself through technology and cost efficiency. The firm operates on extremely thin margins, passing savings to clients in the form of low commissions, tight spreads, and the lowest margin lending rates in the industry. This cost-focused approach has made it the dominant choice for active traders, options-heavy portfolios, and [[algorithmic-trading|algorithmic trading]] operations that require API-driven execution.

## Products and Services

### Account Types
- **IBKR Pro**: The flagship offering for active and professional traders. Features tiered or fixed commission structures, access to all markets and instruments, professional-grade tools, and the lowest margin rates.
- **IBKR Lite**: Introduced in 2019 to compete with commission-free brokerages. Offers $0 commission on U.S. stocks and ETFs, but with wider spreads (orders are routed to market makers via payment for order flow, unlike Pro which uses smart routing for best execution).

### Market Access
Interactive Brokers provides access to:
- **Equities**: 90+ stock exchanges worldwide including NYSE, NASDAQ, LSE, TSE, HKEX, and dozens of others
- **Options**: All major U.S. options exchanges plus international options markets
- **Futures**: CME, ICE, Eurex, HKFE, SGX, and many others
- **Forex**: Interbank forex with institutional-grade spreads; 23 currencies
- **Fixed income**: U.S. Treasuries, corporate bonds, municipal bonds
- **Mutual funds and ETFs**: Over 48,000 mutual funds (many no-transaction-fee) and global ETFs
- **Cryptocurrencies**: Bitcoin, Ethereum, and other major cryptos (via Paxos for U.S. clients)

### Margin Rates
Interactive Brokers consistently offers the lowest [[margin]] lending rates in the brokerage industry. As of early 2024, benchmark rates ranged from approximately 5.8-6.8% for standard balances, with rates as low as 5.3% for balances above $1 million -- significantly below competitors like Schwab, Fidelity, and TD Ameritrade, which typically charge 8-13%. For portfolio margin accounts (available to clients with $110,000+ equity), margin requirements are based on risk-based models that can provide 4-6x leverage on diversified portfolios.

## Trading Platforms

### Trader Workstation (TWS)
TWS is Interactive Brokers' flagship desktop trading platform, known for its comprehensive functionality and steep learning curve. It provides:
- Real-time streaming quotes and market data from 150+ markets
- Advanced order types: over 100 order types including adaptive, algorithmic, and conditional orders
- Options analysis tools: probability-based analysis, volatility surfaces, strategy builder
- Risk management: real-time portfolio risk metrics, stress testing, margin analysis
- Customizable layout with multiple monitors support

TWS is powerful but notorious for its dated user interface and complexity. New users often find it overwhelming compared to more modern platforms, though experienced traders value its depth of functionality.

### Client Portal
A web-based platform with a modern interface for account management, basic trading, and reporting. Designed for less active clients who find TWS too complex.

### IBKR Mobile
Mobile trading app for iOS and Android with most trading functionality available on the go.

### IBKR GlobalTrader
A simplified mobile app launched in 2022, targeting newer investors with an intuitive interface for stocks and ETFs.

## API and Algorithmic Trading

One of Interactive Brokers' most significant competitive advantages is its comprehensive API access, which has made it the de facto standard for retail and small-institutional [[algorithmic-trading]]:

- **TWS API**: Native API supporting Java, C++, C#, and Python. Provides full access to market data, order execution, account information, and portfolio management.
- **Client Portal API**: RESTful API for web-based integration.
- **FIX API**: FIX protocol connectivity for institutional clients.
- **Third-party integration**: Compatible with dozens of third-party platforms including QuantConnect, Zipline, backtrader, Sierra Chart, MultiCharts, and NinjaTrader.

The API supports complex order types, real-time and historical market data, options chain data, and multi-asset execution. Many quantitative researchers and hobbyist algorithmic traders use Interactive Brokers as their primary execution venue because of the combination of low costs, broad market access, and robust API functionality.

## Fee Structure

| Category | IBKR Pro | IBKR Lite |
|----------|----------|-----------|
| U.S. stocks | $0.005/share (min $1.00) or tiered | $0 |
| U.S. options | $0.65/contract (lower on tiered) | $0.65/contract |
| Futures | $0.85/contract (varies by exchange) | $0.85/contract |
| Forex | 0.08-0.20 bps x trade value | 0.08-0.20 bps |
| Market data | Varies; many feeds available for $1-10/month | Limited free data |

IBKR Pro's tiered pricing can reduce costs significantly for high-volume traders, with equity commissions dropping as low as $0.0015/share for very large volumes.

## Strengths and Reputation

Interactive Brokers consistently ranks at or near the top of brokerage rankings by Barron's, Investopedia, and StockBrokers.com for active traders, options traders, and international investors. Key reputation points:

- **Best for cost-conscious traders**: Lowest overall trading costs including commissions, margin rates, and forex spreads
- **Best for international trading**: Unmatched global market access from a single account
- **Best for options and futures**: Professional-grade tools, competitive per-contract pricing
- **Best for algorithmic trading**: Most comprehensive API among retail brokers
- **Regulatory strength**: Regulated by SEC, FINRA, FCA (UK), and other major regulators. SIPC-insured accounts with additional Lloyd's of London coverage up to $30 million

## Criticisms

- **Platform complexity**: TWS has a significant learning curve and an interface that many find dated
- **Customer service**: Frequently criticized for slow response times and limited phone support
- **Account minimums**: IBKR Pro historically required minimum account sizes (removed in recent years, but the perception persists)
- **Inactivity fees**: Previously charged $10/month for accounts generating less than $10 in commissions (eliminated for most accounts in 2021)
- **Restrictive during volatility**: During extreme market events (e.g., the GameStop short squeeze of January 2021), Interactive Brokers raised margin requirements and restricted trading in certain securities, drawing criticism from retail traders

## Economic Moat & Competitive Position

Interactive Brokers' [[economic-moat]] is built on **scale plus automation** rather than brand or distribution — a classic low-cost-producer moat in a commoditizing industry:

- **Lowest-cost operator** — decades of relentless automation give IBKR among the lowest cost-to-serve in the industry. It can profitably offer commissions, [[margin]] rates, and forex spreads that competitors cannot match without subsidizing them, and still run industry-leading pre-tax margins.
- **Highly automated, low-headcount model** — the firm runs an enormous, globally connected platform with a strikingly small employee base relative to client equity and trade volume. This operating leverage means incremental accounts drop disproportionately to the bottom line.
- **Global multi-asset connectivity** — direct membership/connectivity to 150+ markets in 33 countries from a single unified account is genuinely hard to replicate; it took decades of regulatory licensing and exchange integration.
- **API lock-in for algo traders** — the comprehensive TWS/FIX/REST API is the de-facto execution venue for retail and small-institutional [[algorithmic-trading]]. Once a quant has built strategies, data pipelines, and order routing against IBKR's API, [[switching-costs]] are high — code, integrations, and operational tooling must all be re-pointed.
- **Regulatory capital strength** — large excess regulatory capital and conservative risk management (the firm famously raises margin pre-emptively into volatility) underpin counterparty trust for professional and institutional clients.

The moat is **wide on cost and connectivity but narrower on the retail front-end**, where commission-free app brokers compete on user experience rather than price. IBKR's defense there is IBKR Lite and the GlobalTrader app; its core defensibility remains the professional, global, multi-asset, API-driven segment.

## Competitors / Peer Set

| Company | Primary battleground | Notes |
|---|---|---|
| [[charles-schwab]] | US retail + RIA custody, banking | Far larger US retail/advisor base; competes on scale and banking, not on global access or lowest cost |
| [[robinhood]] | US retail, mobile-first, options/crypto | Commission-free, gamified UX; PFOF-funded; overlaps IBKR Lite, not the pro/global franchise |
| [[tiger-brokers]] | Asia (China-diaspora) low-cost electronic broker | Direct analog of IBKR's model in Asia; multi-market, app-led; some clients clear through IBKR-style rails |
| [[futu-holdings|Futu]] | Asia retail (Moomoo/Futubull) | Fast-growing Asian electronic broker; competes for the same globally-minded retail trader |
| Fidelity (private) | US retail + workplace + custody | Huge, low-cost, privately held; competes on US retail breadth, not global multi-asset depth |
| [[tradestation|TradeStation]] / other pro platforms | Active US traders, futures/options | Niche pro-trader platforms; compete on tools but lack IBKR's global reach and cost base |

IBKR's positioning is distinct: **professional-grade, lowest-cost, globally connected, API-driven**, versus the retail-app simplicity of [[robinhood]]/[[futu-holdings|Futu]] and the scale-and-banking model of [[charles-schwab]]/Fidelity.

## Growth Drivers & Catalysts

- **International account growth** — the structural driver; IBKR's single-account global access is uniquely suited to non-US investors seeking US and cross-border markets, and account growth has compounded at high rates.
- **Rising client equity** — more equity means more idle cash, more [[margin]] lending, and more securities-lending inventory — directly feeding NII and ancillary revenue.
- **Net interest income on cash & [[margin]]** — the largest earnings lever; expands with both balances and the level of short-term rates.
- **[[options]] / [[futures]] volume** — derivatives are higher-commission and stickier; IBKR is a leading venue for active options and futures traders.
- **New products** — crypto (via Paxos for US clients), the GlobalTrader app for newer/international retail, expanded fixed income and fund access, and forecast/event products broaden the funnel.
- **Securities lending** — scales with client equity and short-interest cycles.
- **Recurring catalysts** — **monthly brokerage metrics** (DARTs, account adds, client equity, margin loan balances) published mid-month, quarterly earnings (NII and DARTs the watched lines), and the **Fed rate path**, which directly moves NII.

## Bull Case vs Bear Case

### Bull case
- Structural, secular **account and client-equity growth**, especially internationally, in a business with enormous operating leverage.
- **Lowest-cost moat** — automation keeps cost-to-serve below rivals, so incremental growth is highly profitable.
- Diversified revenue (commissions + NII + securities lending) and a fortress balance sheet with large excess regulatory capital.
- Optionality from new products (crypto, GlobalTrader, event contracts) and the introducing-broker/institutional channels.
- [[s-and-p-500]] inclusion (2025) broadens the index-fund ownership base.

### Bear case
- **NII rate sensitivity** — a large share of profit is interest on client cash and [[margin]]; as the Fed eases, net interest margin compresses and earnings can stall even as accounts grow.
- **Trading-volume cyclicality** — commissions and engagement fall in quiet/risk-off tapes.
- **Controlled float / Peterffy structure** — the public IBKR Group holds only a minority economic interest; founder Thomas Peterffy retains majority control via IBG Holdings, limiting public-shareholder governance influence and creating a small effective float.
- Valuation embeds continued growth; any growth or NII disappointment can de-rate the multiple quickly.

## Key Risks

- **Interest-rate sensitivity of NII** — the central risk: falling short rates compress the spread on client cash and margin balances, the dominant profit source.
- **Trading-volume cyclicality** — revenue from commissions and engagement is tied to market activity and volatility, which is inherently cyclical.
- **Regulatory & margin risk** — as a global broker IBKR is exposed to multiple regulators; during extreme events (e.g. the January 2021 GameStop short squeeze) it raised margin and restricted trading, drawing criticism and highlighting episodic franchise/headline risk.
- **Controlled ownership** — IBG Holdings / Peterffy majority control means public holders have limited governance leverage and the float is small relative to market cap.
- **Technology / operational risk** — a heavily automated, low-headcount, globally connected platform concentrates operational risk in systems; an outage or risk-model error could be costly.

## Valuation & How the Stock Trades

IBKR trades as a **growth-financial** within the [[financials]] sector — valued on a multiple that reflects above-peer account/equity growth and very high operating leverage rather than as a slow-growth broker. Mechanically:

- **Small effective float / Peterffy control** — the public entity holds a minority economic interest with founder majority control via IBG Holdings; the limited float can amplify moves and constrains index/active ownership relative to market cap.
- **Capital return** — a modest dividend supplemented by buybacks; the payout is small relative to retained earnings, with reinvestment in the platform and balance-sheet capital the priority (qualitative — see Sources for disclosed figures).
- **Rate-path correlation** — because NII drives profit, the stock trades with short-rate expectations: it tends to firm when the market prices higher-for-longer and softens on aggressive-easing expectations.
- **Beta / cyclicality** — a moderately high-beta financial whose engagement and commissions rise with market activity and volatility.
- **[[s-and-p-500]] inclusion (2025)** broadened index-fund ownership and improved liquidity.
- **Options** — liquid single-stock options around the mid-month metrics and quarterly earnings, where DARTs and NII commentary drive the print.

## 2025-2026 Developments

- **4-for-1 stock split (June 2025):** IBKR executed a four-for-one forward split — shareholders of record 16 June 2025 received three additional shares, with split-adjusted trading from 18 June 2025. The split lowered the per-share price to broaden retail accessibility.
- **Explosive account growth:** Customer accounts grew ~32% in 2025 to roughly 4.40 million by year-end (from ~3.62 million at Q1 2025), and customer equity rose ~37% to about $779.9 billion. Q1 2025 net revenues were $1,427M with diluted EPS of $1.94.
- **Rate sensitivity:** A large share of IBKR's profit is net interest income earned on customer cash and margin balances. As the Fed eased through 2025-2026, the market watched IBKR's net interest margin closely — falling rates compress NII, while elevated trading activity and account growth offset it.
- **S&P 500 inclusion:** IBKR was added to the [[s-and-p-500]] in 2025, broadening its index-fund ownership base.

## Notable History & Milestones

| Year | Milestone |
|---|---|
| 1977–78 | Thomas Peterffy founds the predecessor (T.P. & Co. / **Timber Hill**) and pioneers computerized, automated options market-making |
| 1980s | Among the first to bring handheld computers to the exchange floor; builds automated market-making systems |
| 1993 | Launches the **electronic brokerage** platform, initially for professionals and institutions |
| 2007 | **IPO on NASDAQ** (ticker IBKR); public entity holds a minority economic interest with Peterffy retaining control via IBG Holdings |
| 2019 | Introduces **IBKR Lite** ($0 commission on US stocks/ETFs) to counter commission-free retail brokers |
| 2021 | Eliminates inactivity fees for most accounts; raises margin/restricts trading during the GameStop squeeze |
| 2022 | Launches **GlobalTrader**, a simplified mobile app for newer/international investors |
| 2025 | Executes a **4-for-1 stock split** (June) and is added to the **[[s-and-p-500]]**; client accounts ~4.40M and client equity ~$779.9B at year-end |

## Trading Relevance

- **Ticker:** NASDAQ: IBKR (the publicly-traded entity is Interactive Brokers Group, which holds a minority economic interest; founder Thomas Peterffy retains majority control via IBG Holdings).
- **Index membership:** member of the [[s-and-p-500]] and NASDAQ-100-adjacent large-cap financials.
- **Catalysts:** quarterly earnings (NII, DARTs, account/equity growth), Fed rate path, market-volatility-driven trading volume, margin-loan balances.
- **Correlated names:** [[charles-schwab]], [[robinhood]], and other brokers; broadly tracks equity-market activity and short-rate expectations.

## Related

- [[options]] -- IBKR is a leading platform for options trading
- [[algorithmic-trading]] -- the broker of choice for retail algo traders
- [[margin]] -- IBKR offers the lowest margin rates in the industry
- [[futures]] -- comprehensive futures market access
- [[risk-management]] -- IBKR's portfolio margin and risk tools
- [[charles-schwab]]
- [[robinhood]]
- [[tiger-brokers]]
- [[futu-holdings]]
- [[s-and-p-500]]
- [[financials]]
- [[economic-moat]]
- [[switching-costs]]

## Sources

- IBKR 4Q2025 results — https://www.interactivebrokers.com/mkt/getFileNew.php?file=latestEarningsPR
- IBKR 1Q2025 results — https://www.businesswire.com/news/home/20250415584574/en/Interactive-Brokers-Group-Announces-1Q2025-Results
- 4-for-1 split coverage — https://www.nasdaq.com/articles/interactive-brokers-splitting-its-stock-it-time-buy-shares
- Verified via WebSearch, 2026-06-10
