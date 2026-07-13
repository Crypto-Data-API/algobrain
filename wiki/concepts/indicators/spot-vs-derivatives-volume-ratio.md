---
title: "Spot vs Derivatives Volume Ratio"
type: concept
created: 2026-05-16
updated: 2026-07-13
status: good
tags: [crypto, indicators, derivatives, market-microstructure, volatility]
aliases: ["Spot/Derivatives Ratio", "Spot vs Perp Ratio", "Derivatives Dominance"]
domain: [indicators, market-microstructure]
prerequisites: ["[[perpetual-futures]]", "[[volume]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[funding-rate]]"
  - "[[open-interest]]"
  - "[[crypto-weekday-weekend-etf-era]]"
  - "[[crypto-trading-sessions]]"
  - "[[cryptoquant]]"
  - "[[perpetual-futures]]"
---

# Spot vs Derivatives Volume Ratio

The **spot-to-derivatives volume ratio** (sometimes published as the inverse "derivatives-to-spot ratio" depending on vendor) is the ratio of spot-exchange trading volume to derivatives — primarily [[perpetual-futures]] — volume for a given asset over a chosen window. It is one of the cleanest single-number indicators of *what kind of market* a trader is operating in: a spot-led, real-flow regime, or a leverage-led, perp-dominated regime.

## What It Tells You

The intuition is mechanical. A spot trade moves real coins between balances; a perp trade moves a leveraged paper claim. When the **ratio is low** (derivatives dominate), price action is being set by leveraged speculation:

- Moves are more fragile and prone to mean reversion after [[liquidation]] flushes
- Funding rates run hotter as crowded perp positioning widens the perp-spot basis
- Wicks and squeezes are common because the marginal participant is leveraged

When the **ratio is high** (spot dominates), price action is being set by real flow — ETF creations/redemptions, treasury accumulation, large OTC tickets settling on-exchange, or genuine retail spot buying:

- Moves are stickier and follow-through is more reliable
- Funding tends to lag price rather than lead it
- Breakouts are more credible because the buyer is committing capital, not margin

Empirically, regimes dominated by perp volume have been associated with sharper [[liquidation]] cascades and more violent reversals; spot-led regimes have tended to produce more orderly trends (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## How to Compute

There is no canonical formula — the choice of constituents matters. Most published versions use one of:

- **Top-N spot vs top-N perp**: take the top 5 spot exchanges by reported BTC/ETH volume and top 5 perp venues; ratio is `sum(spot_vol) / sum(perp_vol)` over the window.
- **Single-asset, single-venue**: ratio of [[binance]] spot BTC/USDT volume to Binance USDⓈ-M perp BTC volume, normalised to the same units. Cleaner because both legs share market microstructure, but narrower.
- **Cross-asset aggregate**: total reported spot volume across tracked venues divided by total perp volume, USD-denominated. This is the format [[cryptoquant]] publishes as "Trading Volume Ratio (Spot vs Derivative)" (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

Rolling windows commonly used: 1h (intraday regime detection), 24h (day-over-day comparison), and 7d (regime trend). Wash-trading concerns historically distorted reported spot volume on lower-tier exchanges, so most serious users either restrict the spot leg to a small whitelist of venues with audited tape (Coinbase, Kraken, [[binance]], Bitstamp) or use a third party like Kaiko that normalises.

## Intraday Behavior

The ratio is not constant across [[crypto-trading-sessions]] (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]):

- **US trading hours (13:00–21:00 UTC) on weekdays**: ratio rises. ETF flow lands during NYSE hours, ETF creation/redemption traffic flows through [[coinbase-prime]] custody, and institutional desks transact on spot venues. This is the spot-led part of the day.
- **Asia session and overnight**: ratio falls. Retail-heavy perp flow on Bybit, OKX, [[binance]] dominates while spot books thin out and ETF activity sleeps.
- **Weekends**: ratio skews derivatives-heavy. ETF rails are closed, institutional spot desks are offline, and the marginal participant is a leveraged retail trader on a perp venue (see [[crypto-weekday-weekend-etf-era]]).
- **ETF flow days**: a large surge in net ETF inflows (or outflows) can drive a visible step up in the US-session spot share on the day of settlement.

This intraday cycle is one reason a single global daily ratio can be misleading: the same asset can be spot-led at 18:00 UTC and perp-led at 03:00 UTC of the next session.

## How Traders Use It

Practical uses fall into two buckets:

**Breakout filtering.** A breakout from a key level during a low-ratio (perp-dominated) window deserves more skepticism — derivatives-led wicks frequently reverse once funding extremes draw in arb flow. The same breakout during a high-ratio US-hours window with positive spot delta has a better chance of holding. Many systematic intraday strategies on BTC and ETH gate signals on a rolling ratio threshold.

**Regime detection for sizing and strategy selection.** Perp-dominated regimes favour mean-reversion and liquidation-cascade-fade plays (see [[liquidation-cascade-fade]]); spot-dominated regimes favour trend-following and breakout continuation. A persistent shift in the ratio — for example, the post-ETF era's structural increase in spot share during US hours (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]) — is a signal to recalibrate model parameters, not a trade in itself.

A common pairing is the ratio alongside [[funding-rate]] and [[open-interest]]: when the ratio is low, funding is extreme positive, and OI is climbing, the setup is a textbook crowded-long fragility. When the ratio is high, funding is neutral, and OI is rising, the trend has real backing.

## Data Source

[[cryptoquant]] is the canonical public provider, publishing the metric as "Trading Volume Ratio (Spot vs Derivative)" with daily and rolling views across BTC, ETH, and major alts (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]). Other providers (Kaiko, CoinGecko institutional tier, [[coinglass]]) expose the underlying volume components and let users compute custom ratios with their own exchange whitelist.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

- [[funding-rate]] — best read in conjunction with the ratio
- [[open-interest]] — completes the leverage-positioning picture
- [[crypto-weekday-weekend-etf-era]] — structural driver of the ratio's intraday rhythm
- [[crypto-trading-sessions]] — session framework that explains when the ratio shifts
- [[cryptoquant]] — canonical data provider
- [[perpetual-futures]] — the derivatives leg of the ratio

## Sources

- (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]])
