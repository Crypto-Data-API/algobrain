---
title: "Crypto Signal Library"
type: index
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [meta, crypto, quantitative, methodology, data-provider]
aliases: ["Signal Library", "Crypto Signal Menu", "Signal Primitives"]
related: ["[[feature-engineering-crypto]]", "[[information-coefficient]]", "[[signal-orthogonalization]]", "[[feature-selection-trading]]", "[[alpha-model]]", "[[edge-taxonomy]]", "[[cryptodataapi]]"]
---

> **Purpose.** A browsable ideation menu. Each row is a *reusable signal primitive*: a tradeable crypto signal you can pull from [[cryptodataapi|CryptoDataAPI]], transform, and drop into a strategy or basket. Use this page to shop for candidate signals, not as a set of finished strategies. Every primitive must clear [[information-coefficient|IC triage]] and [[signal-orthogonalization|orthogonalization]] before it earns capital. Tagged `#meta` so it is excluded from the default graph filter.

## How to read this table

| Column | Meaning |
|---|---|
| **Signal** | The raw primitive and its concept page |
| **CryptoDataAPI endpoint** | The verified path that serves it (auth: `X-API-Key`) |
| **Transform / normalization** | How to turn the raw series into a stationary feature (see [[feature-engineering-crypto]]) |
| **Predictive direction** | The hypothesized edge — who is on the other side ([[edge-taxonomy]]) |
| **Horizon & decay** | Where the [[information-coefficient|IC]] peaks and how fast it fades |
| **Consuming strategy / basket** | Where the primitive typically plugs in |

**The workflow for any primitive below:** pull → transform → measure [[information-coefficient|rank-IC]] and its decay curve → [[signal-orthogonalization|orthogonalize]] against BTC/ETH beta and existing signals → [[feature-selection-trading|prune redundancy]] → feed the surviving score into an [[alpha-model]]. Raw IC almost always overstates edge; the *orthogonalized, net-of-cost* IC is what counts.

## Master signal table

| Signal | CryptoDataAPI endpoint | Transform / normalization | Predictive direction | Horizon & decay | Consuming strategy / basket |
|---|---|---|---|---|---|
| **Perp funding** ([[funding-rates]]) | `/api/v1/derivatives/funding-rates?coin=BTC` | 30-90d rolling z-score; regime-conditional; keep carry vs. signal separate | Contrarian: extreme +ve (>0.05%/8h) → crowded longs, fade; deeply -ve → capitulation, buy | Peaks 8h-3d, **fast** decay | [[funding-rate-arbitrage]]; cross-sectional carry basket |
| **OI divergence** ([[open-interest]]) | `/api/v1/liquidity/oi-divergence` | Sign of ΔOI vs Δprice at 1h/4h/24h | Rising OI + rising price = new longs (continuation); rising OI + falling price = short buildup (squeeze risk) | 1h-24h, **fast** | Momentum / breakout; squeeze plays |
| **Exchange netflow** ([[exchange-netflow]]) | `/api/v1/on-chain/exchange-flows/{symbol}` | Trailing flow z-score; inflow vs outflow; spike-alerts for whales | Large CEX **inflow** → supply to sell (bearish); **outflow** → self-custody/accumulation (bullish) | 1-7d, **medium** | Swing accumulation basket |
| **MVRV / dormancy** ([[mvrv-z-score]]) | `/api/v1/on-chain/dormancy/btc` | Zone classification; MVRV-Z level | Low MVRV-Z (<0) → capitulation, accumulate; high (>7) → euphoria, distribute | Weeks-months, **slow** | BTC cycle-position overlay |
| **Whale-score** | `/api/v1/on-chain/whale-score/{symbol}` | Accumulation score; z-score per token | Whale accumulation → bullish; distribution → bearish | Days-weeks, **medium** | Smart-money follow basket |
| **Dry-powder z-score** | `/api/v1/on-chain/stablecoin-reserves/dry-powder` | Z-score of CEX stablecoin reserves (accumulating/neutral/depleting) | Rising dry powder → buying capacity building (bullish tailwind) | Weeks, **slow** | Market-wide risk-on gate |
| **Fear & Greed** ([[fear-and-greed-index]]) | `/api/v1/sentiment/fear-greed` | 0-100 index; contrarian bands | Extreme fear (<20) → buy; extreme greed (>80) → trim | Days, **medium** | Contrarian overlay / regime gate |
| **Taker buy/sell** | `/api/v1/market-intelligence/taker-buy-sell` | 4h ratio; z-score | Aggressive taker-buy dominance → short-term up; extreme → exhaustion | Minutes-hours, **very fast** | Intraday flow / execution timing |
| **Coinbase premium** ([[coinbase-premium]]) | `/api/v1/market-intelligence/coinbase-premium` | Premium index in bps | Positive → US-institutional net demand (bullish confirm) | Hours-days, **fast** | Spot-led trend confirmation |
| **ETF flows** | `/api/v1/market-intelligence/etf/{asset}/flows` | Daily net flow; z-score; multi-day sum | Sustained inflows → structural bid (bullish); outflows → distribution | Days-weeks, **slow** | BTC/ETH structural basket |
| **Liquidations** ([[liquidation-cascade]]) | `/api/v1/market-intelligence/liquidations` | Liq notional; OI-normalized; by-exchange | Long-liq cascade → forced selling exhaustion, local bottom; short-liq → local top | Minutes-hours, **very fast** | Reversal / mean-reversion |
| **Basis** ([[basis]]) | `/api/v1/derivatives/summary?coin=BTC` + `/api/v1/hyperliquid/summary?coin=BTC` | Perp-spot (and futures) basis, annualized bps | High +ve basis → leveraged-long crowding; harvest carry or fade | Hours-days, **medium** | [[basis-trading]]; carry basket |
| **Altcoin breadth** | `/api/v1/market-health/altcoin-breadth` | % of coins above MA (default 200d) | Rising breadth → broad bull (rotate to alts); narrowing → BTC-only risk-off | Days-weeks, **slow** | Regime gate; alt-rotation basket |

## Supporting / confirmation signals

Secondary primitives — usually gates or confirmations rather than standalone alpha:

| Signal | CryptoDataAPI endpoint | Transform | Use |
|---|---|---|---|
| **Long/short ratio** | `/api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` | Top-trader account ratio; z-score | Crowding confirmation for the funding fade |
| **HL whale positioning** | `/api/v1/quant/whales` | ≥$100k account net stance | Confirm whale-score with live perp positioning |
| **Gamma exposure (GEX)** | `/api/v1/quant/gex` | MM inventory + liquidation profile | Pin/anti-pin and squeeze-risk gate |
| **Hash ribbon** | `/api/v1/on-chain/miners/hash-ribbon` | 30d vs 60d hashrate MA state | BTC miner-capitulation bottom filter |
| **Options max-pain** | `/api/v1/market-intelligence/options` | OI, volume, max-pain strike | Expiry-pin bias near BTC option expiries |
| **Borrow interest** | `/api/v1/market-intelligence/borrow-interest` | Margin borrow rate, 4h | Leverage-cost / short-squeeze pressure |
| **Volatility regime** ([[volatility-regime]]) | `/api/v1/volatility/regime` | Compressed/expanding/shock label | Sizing and normalization regime for all signals above |

## Decay tiers (rebalance to the half-life)

Match rebalance frequency to each signal's [[information-coefficient|IC half-life]] — trading faster just pays cost, slower leaves alpha behind:

- **Very fast (minutes-hours):** taker buy/sell, liquidations, L2 imbalance. High Sharpe potential, cost-dominated, capacity-limited.
- **Fast (hours-days):** funding, OI divergence, coinbase premium, basis. The intraday-to-swing core.
- **Medium (days-week):** exchange netflow, whale-score, fear & greed.
- **Slow (weeks-months):** MVRV/dormancy, dry-powder, ETF flows, altcoin breadth. Low turnover, cheap, regime-level.

## Cautions before you trade any primitive

- **BTC-beta contamination.** Most of these co-move with BTC; a raw IC is usually inflated. Always recompute IC on the [[signal-orthogonalization|BTC/ETH-residualized]] signal.
- **Survivorship.** Build cross-sectional versions from a point-in-time universe (see [[feature-engineering-crypto]]); dead tokens inflate backtests.
- **Redundancy.** Funding, basis, OI, and long/short ratio all partly encode leverage — [[feature-selection-trading|prune or orthogonalize]] before stacking.
- **Cost overlay.** Fast signals must survive fees + funding + slippage; a high pre-cost IC can be net-negative.
- **Regime dependence.** Contrarian funding/fear-greed bands invert in strong trends; gate with [[volatility-regime]] / [[market-regime]].

## Example: composing primitives into a basket

A worked illustration of turning primitives into one [[alpha-model|alpha model]] score (not investment advice; numbers indicative):

1. **Pick complementary decay tiers** so bets are less correlated: funding-carry (fast), whale-score (medium), dry-powder (slow, as a market-wide gate).
2. **Transform** each to a cross-sectional rank-z-score per timestamp over the point-in-time perp universe.
3. **Orthogonalize** funding-carry and whale-score against BTC/ETH beta and against each other (both partly encode positioning) — see [[signal-orthogonalization]].
4. **Weight** by each signal's orthogonalized, net-of-cost [[information-coefficient|IC-IR]] rather than equal-weighting the raw signals.
5. **Gate** the whole basket to risk-on when dry-powder is accumulating and [[volatility-regime]] is not `vol_shock`.
6. **Rebalance** at the fastest surviving signal's half-life (here ~8h-1d for funding), sizing against a cost model.

The point of the library is that steps 1-6 are reusable: swap funding-carry for OI-divergence, or whale-score for coinbase-premium, and the same pipeline produces a different basket.

## Getting the Data (CryptoDataAPI)

Every row above is a live endpoint; historical/point-in-time equivalents live under the backtesting archive.

**Live:** see each row's path. **Historical / point-in-time:**
- `GET /api/v1/backtesting/klines` — OHLCV for forward-return labels
- `GET /api/v1/backtesting/funding` — funding archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — survivorship-free point-in-time snapshot
- `GET /api/v1/market-intelligence/fear-greed-history` and `/api/v1/market-intelligence/coinbase-premium` — historical sentiment/premium series

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Category hubs: [[cryptodataapi]] · [[cryptodataapi-derivatives]] · [[cryptodataapi-on-chain]] · [[cryptodataapi-market-intelligence]] · [[cryptodataapi-sentiment]] · [[cryptodataapi-backtesting]].

## Related

- [[feature-engineering-crypto]] — how to transform these raw primitives into features
- [[information-coefficient]] — triage each primitive's skill before building
- [[signal-orthogonalization]] — strip BTC-beta so primitives are independent bets
- [[feature-selection-trading]] — prune the redundant per-venue clones
- [[alpha-model]] — the combiner these primitives feed
- [[edge-taxonomy]] — the edge each primitive is supposed to express
- [[hyperliquid-perp-trading-map]] / [[low-cap-crypto-trading-map]] — venue-specific application maps

## Sources

- CryptoDataAPI endpoint catalog (verified 2026-07-13) — all endpoint paths above
- Grinold & Kahn, *Active Portfolio Management* — IC/breadth framing used in the triage workflow
