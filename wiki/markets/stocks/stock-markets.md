---
title: "Stock Markets"
type: market
created: 2026-04-06
updated: 2026-06-17
status: excellent
tags: [stocks, markets, liquidity, market-microstructure]
aliases: ["Stock Markets", "Equity Markets", "Equity Exchanges"]
related: ["[[stocks]]", "[[equity-index]]", "[[stocks-overview]]", "[[market-microstructure]]", "[[order-types]]", "[[bond-market]]", "[[forex]]", "[[s-and-p-500]]", "[[gics-classification]]"]
---

# Stock Markets

**Stock markets** (equity markets) are the organized exchanges and electronic networks where shares of publicly traded companies are issued, bought, and sold. They perform three economic functions: **capital formation** (companies raise money by selling shares), **price discovery** (continuous trading establishes a fair-value price), and **liquidity provision** (investors can convert shares to cash quickly).

This page covers **market structure and mechanics** — how the plumbing works. For the instrument that trades here, see [[stocks]]; for benchmarks built from these shares, see [[equity-index]]; for the deeper theory of order flow and price formation, see [[market-microstructure]].

## Primary vs Secondary Market

- **Primary market** — where shares are *created and first sold* by the company itself, raising new capital. This includes the **IPO** (initial public offering), **direct listings**, **follow-on offerings**, and **secondary issuances**. Money flows to the company.
- **Secondary market** — where *existing* shares trade between investors. The company receives nothing; this is the day-to-day trading on exchanges that most people mean by "the stock market." Its liquidity is what makes the primary market viable — nobody would buy an IPO they could not later sell.

## Major Exchanges

| Exchange | Location | Notable Indices | Approx. listed mkt cap |
|---|---|---|---|
| **NYSE** | New York | [[dow-jones\|DJIA]], [[s-and-p-500\|S&P 500]] | Largest in the world |
| **NASDAQ** | New York | [[nasdaq\|NASDAQ Composite]], NASDAQ-100 | Tech-heavy, all-electronic |
| **LSE** | London | FTSE 100 | Largest in Europe |
| **JPX / TSE** | Tokyo | Nikkei 225, TOPIX | Largest in Asia (ex-China) |
| **SSE / SZSE** | Shanghai / Shenzhen | SSE Composite, CSI 300 | Largest in mainland China |
| **HKEX** | Hong Kong | Hang Seng | Gateway to Chinese listings |
| **Euronext** | Pan-European | Euro Stoxx 50, CAC 40, AEX | Multi-country platform |
| **NSE / BSE** | Mumbai | NIFTY 50, SENSEX | Largest in India |

The US (NYSE + NASDAQ) accounts for roughly **40%+ of global equity market capitalization**, making it the deepest and most liquid pool of stock in the world.

## Market Mechanics

Modern equity trading is almost entirely **electronic**, matched in a central limit **order book** that ranks resting orders by price then time (price–time priority).

### Trading sessions and the auction structure

A typical exchange day has three phases:

1. **Opening auction** — pre-market orders accumulate and are matched at a single price that maximizes executed volume. This sets the official open and is a major liquidity event.
2. **Continuous trading** — the main session, where buy and sell orders match in real time whenever prices cross.
3. **Closing auction** — orders concentrate into a single closing print. The close is the most important price of the day; index funds, ETFs, and benchmarks reference it, so it carries enormous volume.

### Order types

Traders interact with the book through [[order-types]]:

- **Market order** — execute immediately at the best available price (certainty of execution, not price).
- **Limit order** — execute only at a stated price or better (certainty of price, not execution); these are the resting orders that *provide* liquidity.
- **Stop / stop-limit** — becomes active only after a trigger price, used for risk control.
- **Marketable limit, IOC, FOK, pegged, iceberg** — finer-grained controls over how aggressively and visibly an order works.

### Liquidity providers

- **[[market-makers|Market makers]]** quote two-sided prices (a bid and an ask) and profit from the [[bid-ask-spread|spread]] while bearing inventory risk. On the NYSE, **Designated Market Makers (DMMs)** have specific obligations; NASDAQ uses competing electronic market makers.
- **High-frequency / electronic [[liquidity]] providers** now supply much of the displayed quote, competing on speed and spread (see [[market-microstructure]] and [[high-frequency-trading]]).

### Lit vs dark venues and PFOF

- **Lit markets** — exchanges that display quotes publicly, contributing to price discovery.
- **Dark pools** — private venues that do not display quotes pre-trade, letting large institutions trade big blocks without revealing intent and moving the price.
- **Payment for order flow (PFOF)** — retail brokers route customer orders to **wholesalers** (e.g., Citadel Securities, Virtu) who pay for the flow and execute it off-exchange. This funds "commission-free" retail trading but is controversial for its conflicts and effect on price discovery.

## Trading Hours and Sessions (US)

| Session | Hours (ET) | Notes |
|---|---|---|
| Pre-market | 4:00 AM – 9:30 AM | Thinner liquidity, wider spreads |
| **Regular session** | 9:30 AM – 4:00 PM | Opening + closing auctions bracket it |
| After-hours | 4:00 PM – 8:00 PM | Earnings reactions, low liquidity |

Outside-hours trading carries wider [[bid-ask-spread|spreads]], higher gap risk, and partial order-type support.

## Settlement and Clearing

When a trade executes, ownership and cash must actually change hands — **settlement**. The US moved to **T+1** settlement in **May 2024** (down from T+2): trades settle one business day after execution. Clearing is centralized through the **DTCC/NSCC**, which nets obligations and guarantees the trade, removing counterparty risk between brokers. Shorter settlement reduces systemic risk but tightens operational and funding timelines.

## Circuit Breakers and Trading Halts

To contain disorderly moves, exchanges impose automatic pauses:

- **Market-wide circuit breakers (MWCB)** on the [[s-and-p-500]]: **Level 1 (−7%)** and **Level 2 (−13%)** trigger 15-minute halts; **Level 3 (−20%)** halts trading for the rest of the day. (Triggered in March 2020.)
- **Single-stock limit-up/limit-down (LULD)** bands pause an individual name that moves too far, too fast.
- **Volatility and news halts** pause trading around pending material news or order imbalances.

## Market Participants

- **Retail investors** — individuals, increasingly via commission-free apps.
- **Institutional investors** — mutual funds, pensions, insurers, sovereign funds; the largest holders.
- **Hedge funds and prop traders** — active, often leveraged, strategy-driven.
- **[[market-makers|Market makers]] / wholesalers** — supply liquidity and absorb imbalances.
- **[[algorithmic-trading|Algorithmic]] and [[high-frequency-trading|HFT]] firms** — dominate intraday volume.
- **Index funds / ETF sponsors** — passive vehicles whose mechanical rebalancing creates predictable flows (see [[equity-index]]).

## GICS Sectors

The [[gics-classification|Global Industry Classification Standard (GICS)]] divides listed equities into 11 sectors: [[technology|Information Technology]], [[financials|Financials]], [[communication-services|Communication Services]], [[consumer-discretionary|Consumer Discretionary]], [[healthcare|Health Care]], [[industrials|Industrials]], [[consumer-staples|Consumer Staples]], [[energy|Energy]], [[utilities|Utilities]], [[materials|Materials]], and [[real-estate|Real Estate]]. [[sector-rotation|Sector rotation]] among these groups is a key macro signal. (Full sector weights and constituents are catalogued on [[stocks-overview]].)

## Why It Matters for Traders

Execution quality is decided by structure. Knowing how auctions, [[order-types]], liquidity provision, lit-vs-dark routing, and settlement work is what separates a fill at the [[bid-ask-spread|spread]] midpoint from one that leaks money on every trade. Structure also shapes when liquidity is deepest (the open and close) and when risk is highest (gaps, halts, thin sessions).

## Related

- [[stocks]] — what equities are and how they generate returns
- [[equity-index]] — benchmarks built from these shares
- [[stocks-overview]] — the stocks section hub
- [[market-microstructure]] — the theory of order flow and price formation
- [[order-types]] — the toolkit for interacting with the order book
- [[market-makers]] — liquidity provision and the spread
- [[s-and-p-500]] — the benchmark US index and circuit-breaker reference
- [[gics-classification]] — the 11-sector taxonomy
- [[bond-market]] · [[forex]] · [[commodities]] — adjacent markets

## Sources

- World Federation of Exchanges — global exchange listing and turnover statistics
- SEC / DTCC — T+1 settlement transition (effective May 2024) and market-wide circuit-breaker rules
- S&P Dow Jones Indices, MSCI — GICS sector framework
- General market knowledge; no specific wiki source ingested yet.
