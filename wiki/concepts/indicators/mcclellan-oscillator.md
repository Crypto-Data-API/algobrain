---
title: "McClellan Oscillator"
type: concept
created: 2026-04-20
updated: 2026-07-19
status: excellent
tags: [indicators, technical-analysis, market-breadth, market-internals]
aliases: ["McClellan", "McClellan Osc", "McClellan Oscillator", "NYMO"]
domain: [indicators]
prerequisites: ["[[market-breadth]]", "[[moving-averages]]"]
difficulty: intermediate
related: ["[[sherman-mcclellan]]", "[[market-breadth]]", "[[arms-index]]", "[[divergence]]", "[[trend]]", "[[mcclellan-summation-index]]", "[[advance-decline-line]]", "[[macd]]", "[[market-internals]]"]
---

# McClellan Oscillator

The McClellan Oscillator is a [[market-breadth]] momentum indicator created by [[sherman-mcclellan|Sherman and Marian McClellan]] in 1969. It measures the momentum of advancing versus declining issues on an exchange (classically the NYSE, where the reading is ticker-symboled **NYMO**), providing a gauge of the internal strength or weakness of the broad market that price-based indices alone do not reveal.

## Overview

Most index levels (S&P 500, Dow) are capitalization-weighted, so a handful of mega-cap stocks can keep an index rising even as the *majority* of stocks fall. [[market-breadth|Breadth]] indicators like the McClellan Oscillator look "under the hood" at how many stocks are actually participating. The oscillator distills the daily advance-decline data into a single momentum reading that oscillates around zero, making [[divergence|divergences]] between the broad market's internal health and its headline price easy to spot. It belongs to the broader family of [[market-internals]] tools alongside the [[arms-index|Arms Index (TRIN)]] and the [[advance-decline-line|Advance-Decline Line]].

## How It Works

The oscillator is built from **net advances** — the number of advancing issues minus the number of declining issues each day:

```
Net Advances           = Advancing issues − Declining issues

19-day EMA of Net Advances    (smoothing constant α = 0.10  →  "10% trend")
39-day EMA of Net Advances    (smoothing constant α = 0.05  →  "5% trend")

McClellan Oscillator   = (19-day EMA) − (39-day EMA) of Net Advances
```

The EMA smoothing constants follow the standard α = 2 / (N + 1): for N = 19, α ≈ 0.10; for N = 39, α ≈ 0.05 — which is why the McClellans called them the "10% trend" and "5% trend" of net advances.

It is, in effect, a [[macd|MACD]] applied to breadth data rather than to price (the MACD uses a 12/26 EMA difference of price; the McClellan uses a 19/39 EMA difference of net advances). The two exponential [[moving-averages]] act as fast and slow momentum measures; their difference is **positive** when short-term breadth momentum is accelerating (more stocks joining the advance) and **negative** when it is decelerating.

### Worked example (EMA seeding)

Suppose breadth has been flat (net advances ≈ 0) so both EMAs sit at 0. Today the market gaps up broadly: 2,200 issues advance, 800 decline → Net Advances = +1,400. The EMAs update by `EMAₜ = EMAₜ₋₁ + α × (Net Advancesₜ − EMAₜ₋₁)`:

```
19-EMA:  0 + 0.10 × (1400 − 0) = +140
39-EMA:  0 + 0.05 × (1400 − 0) = +70

McClellan Oscillator = 140 − 70 = +70   (breadth momentum swinging positive)
```

The faster 19-EMA reacts more to today's surge than the slower 39-EMA, so the oscillator jumps positive — a single strong breadth day pushes it up, and a string of them drives it to an extreme.

### Summation Index and ratio-adjustment

The **[[mcclellan-summation-index|McClellan Summation Index]]** is the running cumulative total of the oscillator and serves as a longer-term, less noisy breadth *trend* gauge (the oscillator is the momentum; the summation index is the position).

Many platforms **ratio-adjust** the net-advances input — `Net Advances Ratio = (Adv − Dec) / (Adv + Dec)`, then scale (commonly ×1000) — so the indicator stays comparable across decades as the number of listed issues has grown. Ratio-adjusted readings run on a different scale (extremes nearer ±150 to ±300) than the raw version (extremes nearer ±100).

## Key Signals

| Reading / pattern | Interpretation |
|-------------------|----------------|
| Crosses **above zero** | Breadth momentum turning positive — more stocks joining the advance |
| Crosses **below zero** | Breadth momentum turning negative — distribution spreading |
| **> +100** (or > +150 ratio-adjusted) | Short-term overbought; potential exhaustion / snap-back |
| **< −100** (or < −150 ratio-adjusted) | Short-term oversold; potential capitulation bounce |
| **Bullish [[divergence]]** (price lower low, oscillator higher low) | Selling pressure narrowing — possible washout bottom |
| **Bearish [[divergence]]** (price higher high, oscillator lower high) | Rally narrowing — fewer stocks driving the move (distribution warning) |

The divergence row is the highest-value signal: when a price index makes a new high but the oscillator makes a lower high, fewer stocks are driving the advance — a classic warning of a deteriorating, narrow rally (see [[divergence]]). The reverse can mark a washout bottom.

## How Traders Use It

The McClellan Oscillator is primarily used by index traders, market timers, and analysts assessing whether a rally or decline has broad participation. A rising index with a falling oscillator warns that the advance is narrowing and may be fragile, while a sharp negative extreme during a selloff can signal capitulation and a tradeable bounce. Concretely:

- **Confirmation of breakouts** — an index breakout backed by an oscillator pushing above zero (broadening participation) is more trustworthy than one where breadth lags.
- **Spotting narrow rallies** — late-cycle markets often grind to new index highs on shrinking breadth; a persistent bearish divergence here is one of the earliest warnings of a top, well before price breaks.
- **Capitulation timing** — a plunge to −150/−200 (ratio-adjusted) during heavy selling has historically coincided with short-term bottoms, used by mean-reversion timers for a bounce.
- **Regime read** — combined with the [[mcclellan-summation-index|Summation Index]] (trend) and [[arms-index|TRIN]] (intraday buying/selling intensity), it forms a quick dashboard of [[market-internals]].

Like all breadth tools it is a *confirming* and *context* indicator rather than a precise timing trigger.

## Pitfalls and Risks

- **Breadth can stay narrow for months.** A bearish divergence is a warning, not a sell signal — narrow rallies (a few mega-caps dragging the index) can persist far longer than a counter-trend trader can stay solvent.
- **Exchange-data quirks.** The raw oscillator is sensitive to the universe of issues counted: bond funds, ETFs, and preferreds listed on the NYSE inflate advance/decline counts. Many analysts prefer "common-stock-only" A/D data, which can give a materially different reading.
- **Scale confusion.** Raw vs ratio-adjusted versions have different extreme thresholds (≈±100 vs ≈±150–300). Comparing a chart from one source against thresholds quoted for the other produces wrong conclusions.
- **Not a standalone trigger.** It says *how many* stocks participate, not *which way to trade*. Best paired with price action, [[arms-index|TRIN]], and new-high/new-low data rather than traded in isolation.
- **Single-exchange blind spot.** NYMO is NYSE-only; broad-market reads increasingly require Nasdaq breadth (NAMO) as well, given where growth/tech listings sit.

## Sources

- Sherman & Marian McClellan, *Patterns for Profit* (1970) — the McClellans' own monograph introducing the oscillator and summation index.
- McClellan Financial Publications (mcoscillator.com) — the family's reference site documenting construction and interpretation.
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — covers breadth oscillators in the market-internals chapter.
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research).

## Getting the Data (CryptoDataAPI)

There is no exchange-published advance/decline feed for crypto, but the inputs are constructible from [[cryptodataapi|CryptoDataAPI]]'s universe snapshots:

**Live data:**
- `GET /api/v1/daily/prices` — ~2,500 Binance spot pairs in one call; count advancers vs decliners against the prior snapshot for daily net advances
- `GET /api/v1/market-health/altcoin-breadth?period=200` — pre-computed % of coins above an N-day MA, a related market-wide breadth read

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots` — full daily payload, point-in-time since 2026-03-02, for reconstructing historical net-advance series with the correct dated universe

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/daily/prices"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-health]].

**Live dashboards:** [market health](https://cryptodataapi.com/market)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — snapshot `GET /api/v1/daily/prices` once per day, tally net advances (advancers − decliners), then run the 19/39 EMA difference exactly as above; ratio-adjust by (Adv − Dec)/(Adv + Dec) since the listed-pair count changes as Binance lists and delists
- **Live proxy** — `GET /api/v1/market-health/altcoin-breadth` with a short `period` gives a fast participation read without maintaining your own counts (it measures % above an MA, not net advances — related but not identical)
- **Backtest** — reconstruct historical net advances from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02 only); the dated universe avoids survivorship in the advancer counts, but the window is short — treat crypto-McClellan thresholds as provisional
- **Tip** — crypto's universe is dominated by low-liquidity pairs that follow BTC mechanically; computing a second oscillator on a volume-filtered subset (e.g. top-200 by quote volume) separates genuine breadth from beta noise

## Related

- [[sherman-mcclellan]] -- co-creator
- [[market-breadth]] -- the broader category of participation indicators
- [[market-internals]] -- the dashboard of breadth/internal tools it belongs to
- [[mcclellan-summation-index]] -- the cumulative, longer-term companion to the oscillator
- [[advance-decline-line]] -- the cumulative net-advances series breadth analysis starts from
- [[arms-index]] -- complementary volume-weighted breadth indicator (TRIN)
- [[divergence]] -- the primary signal type for breadth oscillators
- [[macd]] -- analogous dual-EMA momentum construction applied to price
- [[moving-averages]] -- the EMA mechanics underlying the 19/39 construction
