---
title: "Coinglass"
type: source
created: 2026-05-14
updated: 2026-07-19
status: good
tags: [data-provider, derivatives, perpetual-futures, funding-rate, liquidations, crypto]
aliases: ["Coinglass.com", "Bybt", "CoinGlass"]
source_type: data
source_url: "https://www.coinglass.com"
source_author: "Coinglass"
confidence: high
related: ["[[funding-rate]]", "[[perpetual-futures]]", "[[open-interest]]", "[[liquidation]]", "[[polymarket-as-crypto-leading-indicator]]", "[[cme-fedwatch]]", "[[information-arbitrage]]", "[[coingecko]]", "[[dex-screener]]", "[[liquidation-cascade-modeling]]", "[[auto-deleveraging]]", "[[2025-10-crypto-liquidation-cascade]]", "[[crypto-perp-backtesting-pitfalls]]"]
---

Coinglass (formerly Bybt, rebranded in 2022) is the de facto aggregator for crypto derivatives data. It pulls feeds from 25+ exchanges — [[binance]], OKX, [[bybit]], [[deribit]], BitMEX, dYdX, [[hyperliquid]], and others — and unifies funding rates, open interest, liquidations, long/short ratios, options metrics, and order-book heatmaps into a single browser dashboard and API surface. For any crypto trader running positioning-aware strategies, Coinglass is the practical first stop.

## Core product surface

- **Funding rates** — real-time across all perpetual venues; weighted aggregates; full historical series per instrument and per exchange. The single most-used view on the site.
- **Open interest** — total and per-venue, denominated both in USD and in coin terms (the coin-terms view matters during sharp price moves where USD-denominated OI can rise mechanically without new positioning).
- **Liquidations** — real-time tape and historical archives; split long vs short; aggregated across venues and broken down per exchange.
- **Long/short ratio** — top-trader positioning by exchange (Binance, OKX, [[bybit]] publish these); useful as a sentiment proxy but not a precise signal.
- **Options data** — heavily [[deribit]]-focused; put/call ratios, max-pain levels, gamma exposure, term structure.
- **Liquidation heatmaps** — projected liquidation clusters visualized as a heat overlay on the price chart. Widely-watched as candidate magnet levels.
- **Exchange balance** — BTC and ETH balances held on the major CEX hot/cold wallets; useful for spotting supply leaving (custody / cold storage) vs entering (potential sell pressure) the trading layer.

## Relevance to [[polymarket-as-crypto-leading-indicator]]

Coinglass is the natural counterpart to a Polymarket-leads-crypto thesis because it provides the derivative-market positioning signal that a PM odds shift should (or should not) be confirming.

- **Cross-signal validation** — if a Polymarket Fed-cut market shifts and BTC funding rate also moves in the consistent direction, the signals confirm each other. If PM moves but funding does not, that is either a PM-leads-crypto setup (tradeable) or a thin-market PM print (noise).
- **Crowding check** — extreme positive funding alongside bullish PM odds means consensus is already crowded; classic fade setup. Extreme negative funding alongside bearish PM odds is the symmetric long setup.
- **Liquidation-level overlay** — any PM position sized on a crypto-relevant catalyst (ETF approval, regulatory ruling, hack outcome) should account for liquidation clusters in the underlying — a clean PM thesis can still be wrecked by a stop-cascade leg in BTC/ETH.

## API and data access

- REST API with a free tier (rate-limited, often delayed by ~30 seconds on key endpoints) and paid tiers (commonly labelled Standard, Professional, Enterprise).
- Pricing (as of 2026 — verify current rates on the Coinglass site before committing): free tier suitable for casual research; paid plans typically in the ~$30–$300+/month range depending on rate limits and historical depth.
- WebSocket support for select endpoints (funding, liquidations).
- Python SDKs are community-maintained rather than official. Official docs live at coinglass.com/api.

## Use cases for a crypto trading app

- **Funding-rate divergence** — when the spread between two venues' funding rates exceeds a threshold, go long the negatively-funded venue and short the positively-funded venue against it.
- **Liquidation hunting** — visible liquidation clusters in the heatmap frequently act as magnets, particularly in low-liquidity sessions.
- **Sentiment regime** — sustained negative funding across all majors marks a fear regime; sustained extreme-positive funding marks euphoria. Both are mean-revertible.
- **PM signal corroboration** — when a Polymarket Fed-cut probability spikes intraday, check whether STIR proxies and BTC/ETH funding rates align before acting on PM as a lead.
- **Open-interest divergence** — price up + OI flat is a weak rally (mostly spot or short-covering); price up + OI up is a leveraged trend (more energy, but more fragile to liquidation cascades).

## Paid Tiers

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Full web access, basic features |
| Basic API | $59/mo | API access, historical data |
| Pro API | $199/mo | Higher limits, more endpoints |
| Enterprise | Custom | Full data access, dedicated support |

The free web version covers most trader needs. API plans are primarily for building automated systems that consume Coinglass data programmatically.

## API Details

- **Authentication**: API key (paid plans only)
- **Format**: JSON
- **Key endpoints**: `/api/futures/funding-rate`, `/api/futures/open-interest`, `/api/futures/liquidation`

```python
import requests
headers = {"coinglassSecret": "YOUR_API_KEY"}
# Get funding rates
funding = requests.get("https://open-api.coinglass.com/public/v2/funding",
                       headers=headers).json()
# Get open interest
oi = requests.get("https://open-api.coinglass.com/public/v2/open_interest",
                   headers=headers, params={"symbol": "BTC"}).json()
```

## Liquidation Cascade Data

Coinglass's most distinctive dataset is its **historical liquidation feed**, aggregated across the major centralized perp venues — Binance, Bybit, OKX, [[hyperliquid]], Bitget, dYdX — with per-trade granularity going back several years. For each forced close it captures: timestamp, exchange, symbol, side, size in USD, price, and (where exposed) the liquidation type (mark-price vs. ADL).

Sub-products built on this feed:

- **Liquidation heatmaps**: estimated cluster of stop and liquidation prices by leverage tier, derived from public OI distributions. Useful for identifying levels where a cascade is mechanically likely.
- **Funding-rate term-structure dashboards**: 8h, 1d, 7d, 30d annualised funding rates per exchange and per symbol, with cross-venue divergence views.
- **OI / funding heatmap composites**: overlay of open-interest concentration with funding extremes — flags the venues most exposed to a given crowding regime.
- **Long/Short ratio histories** per exchange and per account-class (top-trader, all-trader) — useful as a contrarian sentiment filter.
- **ETF flow reconciliation**: BTC/ETH ETF net-flow data alongside perp positioning, allowing cash-and-carry / basis backtests to use a single, time-aligned dataset.

For perp-strategy researchers this is the closest available public proxy for what a top-tier shop reconstructs from raw exchange feeds (Kaiko, Amberdata).

## Backtesting Use Cases

- **Stress-testing strategies against the Oct 10-11 2025 cascade**: replay the ~$20B liquidation event using the per-minute liquidation feed alongside mark-price data. See [[2025-10-crypto-liquidation-cascade]] and [[liquidation-cascade-modeling]].
- **Validating ADL exposure assumptions**: by cross-referencing the public liquidation feed with insurance-fund balance changes, a researcher can detect periods when [[auto-deleveraging|ADL]] events likely occurred. Most retail backtests assume liquidations only hit losing positions; ADL invalidates that assumption.
- **Modelling realistic liquidation triggers**: instead of using a fixed liquidation price, calibrate to the empirical distribution of per-symbol liquidation prices — capturing the real interaction between mark-price methodology, funding flows, and dynamic margin tiers.
- **Funding-rate regime detection**: feed funding-rate term-structure series into [[market-regime-detection-ml|regime classifiers]].
- **Capacity calibration**: compare 24h liquidation totals and OI per venue to estimate the ceiling at which a strategy starts to cause the cascades it tries to exploit.

## Comparison to alternatives

| Tool | Strength | Best for vs Coinglass |
|------|----------|------------------------|
| [[laevitas]] | Deeper [[deribit]] options analytics | Detailed options structure and skew |
| **Velo Data** | Cleaner institutional-grade API | Lower-latency systematic systems |
| [[the-block]] | Editorial and research overlay | Macro context, not raw data |
| Per-exchange APIs | Most accurate single-venue data | When you only need one venue |

## Limitations

- Aggregation methodology is not always transparent. Weighting schemes across exchanges can shift over time without obvious notice, which complicates long-horizon backtests.
- Some exchanges intermittently rate-limit Coinglass, causing visible gaps in the data feed.
- The free tier is delayed by roughly 30 seconds on many endpoints — useless for any HFT or fast-reactive strategy.
- Liquidation data is *reported* by the exchanges themselves and is subject to under-reporting. Binance famously throttled its liquidation feed in 2021, which made aggregate liquidation numbers across the space systematically understated for an extended period.

## Why this matters for [[polymarket-as-crypto-leading-indicator]]

Polymarket Fed-rate-cut probabilities should be tested against [[cme-fedwatch]] *and* against perpetual-futures funding rates on BTC/ETH around FOMC dates. Coinglass is the practical layer for the funding-rate side of that test. The structural question is timing:

- If PM odds shift several hours before BTC funding repositions, Polymarket is leading.
- If funding moves first, Polymarket is lagging.
- If both move simultaneously, neither leads — they are both reacting to a third signal (usually a CPI/jobs/FOMC tape or a large derivatives flow).

Without Coinglass (or an equivalent funding aggregator), the PM-leads-crypto thesis cannot be empirically tested.

## Related

- [[funding-rate]]
- [[perpetual-futures]]
- [[open-interest]]
- [[liquidation]]
- [[polymarket-as-crypto-leading-indicator]]
- [[cme-fedwatch]]
- [[information-arbitrage]]
- [[laevitas]]
- [[deribit]]

## Sources

- Coinglass own documentation and product pages at coinglass.com
- Cross-reference [[information-arbitrage]] §Crypto-specific stack
