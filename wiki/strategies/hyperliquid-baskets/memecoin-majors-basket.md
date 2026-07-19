---
title: "Memecoin Majors Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, memecoins, altcoins, behavioral-finance, market-regime]
aliases: ["Meme Majors Basket", "Established Memecoin Basket", "Large-Cap Meme Basket", "Meme Blue Chip Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[meme-coin-cycle]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[alt-season-momentum-gate]]", "[[meme-speculative-regime]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]", "[[behavioral-finance]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral]
edge_mechanism: "Established memecoins (> 6 months of market history, > $500M peak market cap) retain social-contagion momentum through multiple cycles with higher liquidity and lower oracle-manipulation risk than micro-cap memes; the basket captures meme-season upside at reduced single-name wipeout risk compared to the micro-cap meme-coin-cycle basket."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data, social-volume]
min_capital_usd: 10000
capacity_usd: 25000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.50
breakeven_cost_bps: 40
kill_criteria: |
  - basket drawdown > 50% from peak on a rolling 6-month basis
  - meme-speculative regime not confirmed for > 30 consecutive days
  - rolling 6-month Sharpe < -0.2
---

# Memecoin Majors Basket (Hyperliquid Basket)

A basket of the largest, most established memecoins with active Hyperliquid perpetuals — tokens with ≥ 6 months of market history, ≥ $500M peak market cap, and demonstrated multi-cycle survival. Provides meme-season beta at higher liquidity and lower single-name wipeout risk than the [[meme-coin-cycle]] basket (which targets fresh micro-cap launches). Deployed during confirmed [[meme-speculative-regime|meme-speculative regimes]].

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral** (see [[edge-taxonomy]]). Established memecoins retain brand recognition and social-velocity that drives repeated retail FOMO cycles. Unlike micro-cap memes, these tokens survive bear markets and revive in each new meme season, making them repeatable behavioral-cycle trades rather than one-shot launches.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Dogecoin | DOGE | The original; highest market cap and liquidity; Elon-association narrative |
| Shiba Inu | SHIB | Second-largest memecoin; established ecosystem |
| Pepe | PEPE | 2023 emergence; large market cap; strong social identity |
| Bonk | BONK | Solana-native meme flagship; ecosystem narrative |
| Dogwifhat | WIF | Solana meme cycle leader; high liquidity HL perp |
| Floki | FLOKI | Elon-association meme; multi-chain |
| Brett | BRETT | Base-chain meme representative |

**Constituent count:** 7. All require ≥ $3M daily HL perp volume for inclusion.

## Selection Rule

Constituents must: (1) have ≥ 6 months of continuous trading history; (2) have reached ≥ $500M market cap at any historical peak; (3) have ≥ $3M daily HL perp volume; (4) have no fundamental utility claim — pure social/meme token (avoids blurring with AI tokens, gaming tokens, etc.).

## Weighting Scheme

**Equal-weight**. Optionally vol-weight to reduce DOGE dominance (DOGE often has lower volatility than smaller meme constituents; vol-weighting increases small-meme exposure and portfolio volatility — only apply in confirmed meme-speculative regimes with strong signals).

## Rebalance Cadence

Weekly. Out-of-cycle rebalance if any constituent posts ±50% in 7 days (common in meme-peak periods).

## Regime Character

Deployment ONLY in confirmed [[meme-speculative-regime]]: BTC dominance declining, meme total market cap rising, funding elevated but not extreme. Flat or short in bear markets and dominance-rising regimes. This basket differs from [[meme-coin-cycle]] in targeting established names (higher capacity, lower wipeout risk) rather than micro-cap launches.

## Strategies That Deploy This Basket

- [[meme-coin-cycle]] — the directional cycle strategy; this basket is its long-side vehicle for established memes
- [[momentum-rotation]] — long the meme sector when it ranks top momentum quintile
- [[cross-sectional-relative-value]] — long meme momentum winners vs. short laggards within the basket
- [[alt-season-momentum-gate]] — meme-majors basket activated when alt-season gate confirms

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=DOGE&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=DOGE`
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score for regime confirmation

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/meme/regime/score"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]], [[cryptodataapi-dex]].

## Related

[[hyperliquid-baskets-overview]] · [[meme-coin-cycle]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[alt-season-momentum-gate]] · [[meme-speculative-regime]] · [[behavioral-finance]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
