---
title: "Crypto Trading Sessions (Asia / London / New York)"
type: concept
created: 2026-05-16
updated: 2026-07-13
status: good
tags: [crypto, market-microstructure, liquidity, day-trading]
aliases: ["Crypto Sessions", "Asia London New York Crypto", "Crypto Intraday Sessions", "LNY Overlap"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[session-overlap-liquidity]]", "[[crypto-weekday-weekend-etf-era]]", "[[btc-weekend-effect]]", "[[overnight-vs-intraday]]", "[[funding-by-hour]]", "[[session-overlap-momentum]]", "[[kaiko]]", "[[coinglass]]", "[[cryptoquant]]", "[[crypto-perp-backtesting-pitfalls]]", "[[cryptodataapi]]"]
---

# Crypto Trading Sessions (Asia / London / New York)

Crypto markets trade 24/7, but liquidity, volume, and volatility are far from flat across the clock. Empirical and practitioner evidence shows that crypto inherits a regional "session" structure from the traditional financial system — Asia, London/Europe, and New York hours each have distinct character — because the humans and institutions providing liquidity still operate on regional workdays and because the macro and ETF flow anchors live in specific time zones. This page is the hub for that framework; it ties together session definitions, the empirical patterns observed in BTC/ETH intraday data, the ETF-era restructuring of weekday vs. weekend liquidity, and the strategy implications.

## Session Definitions

The standard mapping used by practitioners and the academic literature aligns crypto sessions with the major regional FX/equity sessions (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]):

| Session | UTC window | Typical character |
|---------|-----------|-------------------|
| Asia | ~00:00 – 07:00 UTC | Lower liquidity, tighter ranges, more false breakouts. Tokyo and Singapore desks set the tone; JPY pairs see their own activity peak here. |
| London / Europe | ~08:00 – 16:00 UTC | Marked pickup in volume and directional moves as European desks come online. The London open often initiates the day's first decisive break of the Asia range. |
| New York | ~13:00 – 21:00 UTC | Either extends or violently reverses the prevailing trend; ETF flows, US macro releases, and CME hedging anchor the action. |
| **London–New York (LNY) overlap** | ~13:00 – 16:00 UTC | The deepest liquidity window of the day and the dominant zone for price discovery (see [[session-overlap-liquidity]]). |

A secondary Asia–London handoff occurs roughly 07:00–09:00 UTC. It is thinner than LNY but still meaningfully tighter than late-Asia/early-Asia hours.

## Why Sessions Exist in a 24/7 Market

Several forces re-impose business-day structure on a nominally borderless market:

- **Institutional working hours** — proprietary trading desks, hedge funds, OTC desks, and market-making firms staff their books regionally. When a region's desks are off, their liquidity is off.
- **Regional retail flows** — Asian retail (Japan, Korea, China-adjacent) trades disproportionately in Asia hours; Western retail concentrates in London/NY hours.
- **CME and equity-market anchoring** — the NYSE and NASDAQ trade 09:30–16:00 ET on weekdays, and [[cme-bitcoin-futures]] runs on a Sunday–Friday CT schedule. These anchor institutional hedging and price discovery into US hours (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).
- **Stablecoin and banking fiat rails** — USD stablecoin issuance, redemption, and bank-rail on/off-ramps are tied to traditional money-market hours. When banks are closed, the fiat plumbing thins, and so does crypto liquidity that depends on it.

## Empirical Patterns

Tick-level Bitcoin studies covering 2017–2021 document an **inverted U-shape** in intraday activity for BTC/USD and BTC/EUR — volume, volatility, and liquidity all peak in the LNY overlap and decay toward Asia hours. BTC/JPY, by contrast, shows **dual peaks**: one in Asia hours and one in the LNY window, reflecting the bimodal trader base for that pair (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

Across all major pairs, the LNY overlap dominates intraday price discovery: spreads are tightest, top-of-book and L2 depth are deepest, and a disproportionate share of the day's information-driven price moves occur in this window. Practitioner content describes the typical day as Asia setting the range, London breaking it, and New York extending or reversing the move (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## ETF-Era Restructuring

Since the launch of US spot Bitcoin ETFs in 2024, the regional weighting has shifted further toward US weekday hours. Kaiko data shows that roughly half of BTC volume now occurs during US sessions, vs. a more even distribution in earlier cycles. Weekday BTC volumes are now roughly 2× weekend volumes, and the market has bifurcated into a deep weekday US session and a hollowed-out weekend/overnight regime (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

See [[crypto-weekday-weekend-etf-era]] for the full treatment of this restructuring and its risk implications.

## Implications for Strategy Design

Mapping strategy logic to the session structure is one of the highest-leverage adjustments an intraday crypto trader can make:

- **London open scalps and breakouts** — the Asia range is often broken in the first 60–90 minutes of London hours; breakout systems and momentum scalps tend to fire here.
- **Asia-range mean reversion** — when no fresh catalyst is live, prices tend to oscillate within the Asia range; mean-reversion logic that would fail during the London/NY trend phase often works here.
- **NY-close reversals** — late NY hours frequently see directional reversals or trend exhaustion as US desks square up before going offline.
- **Funding-cycle alignment** — 8-hour funding windows on CEX perps land at fixed UTC times and interact with session liquidity in systematic ways. See [[funding-by-hour]].
- **Liquidation cascade risk in thin sessions** — leverage clears unevenly across the clock. The same notional liquidation that gets absorbed in LNY can cascade catastrophically in late Asia or weekends because the book is shallower. Position sizing and stop placement should be session-aware.
- **Holding overnight (UTC) into thin sessions** — carrying full risk through a session handoff is materially different from carrying it across LNY. The implied volatility cost of overnight risk is not uniform.

A direct strategy that operationalizes the session framework is documented at [[session-overlap-momentum]].

## How to Measure

The empirical work above relies on a small set of institutional-grade data providers:

- [[kaiko]] — tick-level and L2 order-book feeds across exchanges, with the region and venue segmentation needed to build session curves (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).
- [[coinglass]] — funding-rate, open-interest, and liquidation dashboards that let you see how leverage clusters and clears by session.
- [[cryptoquant]] — exchange inflow/outflow analytics and the canonical [[spot-vs-derivatives-volume-ratio]] chart for diagnosing when derivatives are driving session price action.

For most retail-scale work, CoinGlass and CryptoQuant are the practical starting point; Kaiko is the institutional research backbone.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC history + 200D MA
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

## Related

- [[session-overlap-liquidity]] — focused treatment of the LNY overlap
- [[crypto-weekday-weekend-etf-era]] — ETF-era weekday/weekend split
- [[btc-weekend-effect]] — earlier weekend-anomaly framing
- [[overnight-vs-intraday]] — equity-side analog
- [[funding-by-hour]] — perp funding cycle and its session interaction
- [[session-overlap-momentum]] — strategy implementation
- [[crypto-perp-backtesting-pitfalls]] — why naive 24/7 backtests miss session structure
- [[liquidation]] — the cascade mechanic that punishes thin-session trading
- [[coinbase-prime]], [[cme-bitcoin-futures]] — institutional anchors that concentrate US-session flow
- [[whale-alert]], [[token-unlocks]] — flow/supply signals that read differently by session

## Sources

- [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]] — Perplexity deep-research synthesis of practitioner and academic sources on crypto intraday session structure
- Eross, A., McGroarty, F., Urquhart, A., Wolfe, S. (2019). "The intraday dynamics of bitcoin." *Research in International Business and Finance* — documents intraday volume/volatility seasonality in BTC
- Baur, D., Dimpfl, T. (2018). "Asymmetric volatility in cryptocurrencies." *Economics Letters* — intraday and session-level volatility patterns
- Kaiko Research, "Bitcoin Liquidity by Trading Session" reports (2024–2025) — ETF-era weekday/weekend volume restructuring
