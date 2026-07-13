---
title: Equity Index
type: concept
created: 2026-04-06
updated: 2026-06-17
status: excellent
domain: [portfolio-theory]
difficulty: beginner
tags:
  - stocks
  - indices
aliases:
  - stock-index
  - equity-indices
  - stock market index
related:
  - "[[s-and-p-500]]"
  - "[[dow-jones]]"
  - "[[nasdaq]]"
  - "[[euro-stoxx]]"
  - "[[stocks]]"
  - "[[stock-markets]]"
  - "[[stocks-overview]]"
  - "[[market-capitalization]]"
  - "[[index-options]]"
  - "[[index-funds]]"
  - "[[futures]]"
---

# Equity Index

An **equity index** (or stock market index) is a rules-based statistical measure that tracks the combined performance of a defined basket of stocks, expressed as a single number. It serves as a **benchmark** for a market, region, or sector. Major examples include the [[s-and-p-500]], [[dow-jones|Dow Jones Industrial Average]], and [[nasdaq|NASDAQ]].

This page covers **what an index is and how it is built**. For the underlying instrument, see [[stocks]]; for where its constituents trade, see [[stock-markets]]; for the section hub, see [[stocks-overview]].

## What Is an Index?

An index applies fixed selection rules (size, liquidity, sector, geography, listing) to choose a set of constituent stocks, then combines their prices into one figure using a **weighting scheme** and a **divisor** that keeps the level continuous through corporate actions. An index is *not directly investable* — it is a mathematical construct. Investors gain exposure through wrappers built to replicate it: [[index-funds]], ETFs, [[futures]], and [[index-options]].

A well-designed index aims to be **representative** (captures the intended market), **investable** (replicable at low cost), **transparent** (published rules), and **stable** (low turnover).

## Weighting Schemes

The weighting method is the single most important design choice — it determines what the index actually measures.

| Scheme | How weights are set | Used by | Bias / effect |
|---|---|---|---|
| **Price-weighted** | Proportional to **share price** | [[dow-jones\|Dow Jones]], Nikkei 225 | High-priced stocks dominate regardless of company size; distorted by splits |
| **Market-cap-weighted** | Proportional to **[[market-capitalization]]** | [[s-and-p-500]], [[nasdaq]], Russell, MSCI | Largest companies dominate; tilts toward megacaps and momentum |
| **Float-adjusted cap-weighted** | Cap, counting only **freely tradable shares** | Modern S&P, MSCI, FTSE | Excludes locked-up insider/government stakes; the current standard |
| **Equal-weighted** | Every constituent gets the **same weight** | S&P 500 Equal Weight (RSP) | Small/mid tilt; needs frequent rebalancing; higher turnover |
| **Fundamental-weighted** | By sales, earnings, book value, dividends | RAFI, many "smart beta" ETFs | Breaks the price-weight link; value tilt |

The dominant modern approach is **float-adjusted market-cap weighting**: it is self-rebalancing (a stock's weight rises and falls with its price, so no trading is needed to maintain weights) and reflects the actual investable opportunity set.

## Float Adjustment and Reconstitution

- **Float adjustment** — only shares available to public investors count toward a stock's weight. Closely held stakes (founders, governments, strategic holders) are excluded, so the index reflects what investors can actually buy.
- **Reconstitution** — periodic review (e.g., Russell's annual June reconstitution; the S&P's ongoing committee additions) where constituents are added or dropped to keep selection rules current. Because trillions of dollars track major indices, reconstitution forces [[index-funds|index funds]] to buy additions and sell deletions on the effective date, creating large, predictable flows.

## Major Global Indices

| Index | Region | Constituents | Weighting | Notes |
|---|---|---|---|---|
| **[[s-and-p-500]]** | US | ~500 large-cap | Float cap | The benchmark; ~80% of US market cap |
| **[[dow-jones\|DJIA]]** | US | 30 blue chips | **Price** | Oldest (1896); least representative |
| **[[nasdaq\|NASDAQ Composite]]** | US | 3,000+ NASDAQ-listed | Cap | Tech-heavy; NASDAQ-100 = top 100 non-financials |
| **Russell 2000** | US | 2,000 small-caps | Cap | The small-cap benchmark |
| **[[euro-stoxx\|EURO STOXX 50]]** | Eurozone | 50 blue chips | Cap | European S&P equivalent |
| **FTSE 100** | UK | 100 largest LSE | Cap | Energy, mining, financials heavy |
| **DAX 40** | Germany | 40 | Cap | Quoted as **total return** (unusual) |
| **Nikkei 225** | Japan | 225 | **Price** | Price-weighted like the Dow |
| **TOPIX** | Japan | ~2,000 | Cap | Broader than the Nikkei |
| **Hang Seng** | Hong Kong | ~80 | Cap | Proxy for Chinese large-cap sentiment |
| **MSCI World / ACWI** | Global | 1,400 / 3,000+ | Cap | Standard global benchmarks |

## Price Return vs Total Return

Most headline index levels are **price-return** — they ignore dividends. The **total-return** version reinvests [[dividend|dividends]] and is the correct benchmark for evaluating a fund manager. The gap compounds: over multi-decade horizons, roughly a third to a half of equity total return has come from reinvested dividends. (The DAX is the notable exception, published as a total-return index, which complicates cross-index comparison.)

## Uses of an Index

- **Benchmark and beta** — an index defines "the market" against which [[alpha]] is measured; a portfolio's [[beta]] is its sensitivity to it.
- **Passive investing** — [[index-funds]] and ETFs (SPY/VOO/IVV, QQQ, DIA, IWM, FEZ) replicate an index at minimal cost; passive now rivals active in assets.
- **Derivatives** — [[futures]] (E-mini S&P ES, Nasdaq NQ, Dow YM, EURO STOXX FESX) and [[index-options]] (cash-settled SPX/NDX, plus SPY/QQQ ETF options) allow capital-efficient, leveraged, or defined-risk exposure. The [[vix|VIX]] is derived from SPX option prices.
- **Hedging** — selling index futures or buying index puts hedges a diversified book cheaply without selling individual holdings.
- **Economic gauge** — indices are headline indicators of market health and sentiment.

## Index Effects

Because so much capital mechanically tracks indices, index *changes* move prices:

- **Inclusion/deletion effect** — a stock added to the [[s-and-p-500]] is bought by every tracking fund, often causing a pre-effective-date pop; deletions sell off. Front-running additions is a classic event-driven play (now decayed as it became widely known).
- **Rebalancing flows** — quarterly/annual reconstitution and weight changes concentrate forced trading on known dates (e.g., Russell reconstitution).
- **Breadth and rotation** — comparing a cap-weighted index to its **equal-weight** version (RSP vs SPY) reveals whether a rally is broad or megacap-driven, a key input for [[sector-rotation]] and breadth analysis.

## Limitations

- **Megacap concentration** — cap weighting can leave an index dominated by a handful of names, undermining the diversification it appears to offer.
- **Buy-high/sell-low tilt** — cap weighting mechanically over-weights what has risen and under-weights what has fallen.
- **Survivorship and reconstitution bias** — chronic underperformers are removed, flattering long-run index returns versus a static basket.
- **Price-weighting distortions** (Dow, Nikkei) — share price, not company size, drives weight; splits arbitrarily change influence.
- **Total-return vs price-return confusion** — comparing a price-return headline to a total-return strategy understates the true benchmark.

## Related

- [[stocks]] — the underlying instrument
- [[stock-markets]] — where constituents trade
- [[stocks-overview]] — the stocks section hub
- [[s-and-p-500]] · [[dow-jones]] · [[nasdaq]] · [[euro-stoxx]] — major indices
- [[market-capitalization]] — the basis of cap weighting
- [[index-funds]] — passive replication vehicles
- [[index-options]] · [[futures]] — derivative exposure
- [[sector-rotation]] — breadth and rotation analysis

## Sources

- S&P Dow Jones Indices and MSCI — index methodology and float-adjustment documentation
- STOXX Ltd. — EURO STOXX 50 methodology
- FTSE Russell — Russell reconstitution methodology
- General market knowledge; no specific wiki source ingested yet.
