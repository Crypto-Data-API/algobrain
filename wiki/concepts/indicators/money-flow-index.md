---
title: "Money Flow Index"
type: concept
created: 2026-04-20
updated: 2026-07-19
status: excellent
tags: [indicators, technical-analysis, volume, momentum]
aliases: ["MFI", "Money Flow Index", "money-flow-index"]
domain: [indicators]
prerequisites: ["[[rsi]]", "[[volume]]"]
difficulty: intermediate
related: ["[[rsi]]", "[[relative-strength-index]]", "[[volume]]", "[[vwap]]", "[[chaikin-money-flow]]", "[[support-and-resistance]]"]
---

The Money Flow Index (MFI) is a volume-weighted momentum oscillator created by Gene Quong and Avrum Soudack in 1989. Often described as **"volume-weighted [[relative-strength-index|RSI]]"**, it combines price and [[volume]] data to identify overbought/oversold conditions with the added dimension of volume confirmation. Bounded between 0 and 100 with a default period of 14, MFI rises when money flows into an asset on up-days and falls when money flows out on down-days (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## The Calculation

MFI is built in four steps:

**Step 1 — Typical Price (TP)** for each period:
```
TP = (High + Low + Close) / 3
```

**Step 2 — Raw Money Flow (RMF)** = the dollar (or share) flow for that period:
```
Raw Money Flow = Typical Price × Volume
```

**Step 3 — Classify and sum over the lookback (default 14 periods):**
- If today's TP > yesterday's TP → the bar's RMF is **Positive Money Flow**
- If today's TP < yesterday's TP → the bar's RMF is **Negative Money Flow**
- If TP is unchanged → the bar is discarded (counts as neither)

Sum positive flows and negative flows separately over the 14-bar window.

**Step 4 — Money Ratio and the index:**
```
Money Flow Ratio = (14-period Positive Money Flow) / (14-period Negative Money Flow)

MFI = 100 − ( 100 / (1 + Money Flow Ratio) )
```

This is the identical mathematical form to [[relative-strength-index|RSI]], except RSI ranks *average price change* whereas MFI ranks *dollar volume on up-bars vs down-bars*. The volume term is what gives MFI its edge: it weights each move by how much capital backed it (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

### Worked Example

Take three consecutive days on a stock:

| Day | High | Low | Close | TP = (H+L+C)/3 | Volume | Raw MF = TP×Vol | Direction |
|---|---|---|---|---|---|---|---|
| 1 | 21.0 | 20.0 | 20.4 | 20.47 | 100k | 2.047M | — |
| 2 | 21.6 | 20.6 | 21.4 | 21.20 | 150k | 3.180M | TP up → Positive |
| 3 | 21.3 | 20.4 | 20.6 | 20.77 | 200k | 4.154M | TP down → Negative |

Over this tiny window: Positive Money Flow = 3.180M, Negative Money Flow = 4.154M.
Money Ratio = 3.180 / 4.154 = **0.766**.
MFI = 100 − (100 / (1 + 0.766)) = 100 − 56.6 = **43.4**.

A reading near 43 is mid-range / neutral. Notice that even though day 2's *price* rise was modest, the heavier volume on the day-3 decline (200k shares) dragged the index below 50 — exactly the volume-weighting effect MFI is designed to surface.

## Reading the Scale

| MFI reading | Condition | Typical interpretation |
|---|---|---|
| **> 90** | Extreme overbought | Strong reversal warning (rarer than RSI > 70) |
| **> 80** | Overbought | Potential selling pressure / mean-reversion zone |
| **20 – 80** | Neutral band | Trend-following territory; little signal |
| **< 20** | Oversold | Potential buying pressure |
| **< 10** | Extreme oversold | Strong reversal warning / capitulation |

Because MFI requires *both* price direction and volume to push it to an extreme, its 80/20 thresholds are typically reached less often than RSI's 70/30 — a high MFI reading therefore tends to carry more information.

## Key Signals

- **Overbought (>80)**: potential selling pressure
- **Oversold (<20)**: potential buying pressure
- **Divergences**: MFI diverging from price provides stronger signals than RSI divergences alone, because volume confirms the conviction behind price moves
- **Failure swings**: an MFI that fails to make a new high (or low) alongside price, then breaks its own prior swing level, is a classic non-confirmation that does not require a price reference at all

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## How Traders Use It

1. **Volume-confirmed reversals.** Take an MFI > 80 (overbought) signal only when price is also at [[support-and-resistance|resistance]] — the volume weighting means the extreme reflects real distribution, not just a price drift.
2. **Bearish divergence (distribution).** Price prints a fresh high while MFI rolls over below its prior peak → the rally is being made on thinning money flow; large participants are not supporting it.
3. **Bullish divergence (accumulation).** Price makes a lower low while MFI makes a higher low → selling is drying up; potential bottom.
4. **Trend filter.** In strong trends MFI can pin above 80 (or below 20) for extended runs, so traders avoid fading extremes during powerful moves and instead use MFI pullbacks toward 50 as trend-continuation entries.
5. **Confirmation overlay.** MFI is most valuable as a *confirmation* layer on top of price-structure or [[vwap]]-based setups, not as a standalone signal generator.

## Common Pitfalls

- **Fading every extreme.** MFI staying above 80 in an uptrend is normal, not a sell. Pinned readings confirm strength, they do not contradict it.
- **Garbage-in on bad volume data.** MFI is only as good as its volume input. In fragmented or OTC markets, or 24h [[crypto]] venues where reported volume can be inflated/washed, the signal degrades.
- **Treating it as identical to RSI.** They share a formula but diverge when volume and price disagree — the *disagreement* is the signal, so MFI and RSI giving different readings is the point, not a bug.
- **Short windows on illiquid names.** With few qualifying up/down bars, the money ratio becomes unstable; the default 14 is a sensible floor for thin instruments.

## Trading Relevance

MFI is used the same way as [[rsi|RSI]] but with a volume filter baked in, which makes it valued as a confirmation tool rather than a standalone signal generator. The highest-conviction setup is a **failure swing / divergence**: price prints a fresh high while MFI rolls over below its prior peak, indicating the rally is being made on thinning money flow (distribution). Because MFI weights each price move by traded volume, a divergence here implies that large participants are not supporting the move — a stronger tell than a bare RSI divergence. Traders typically pair MFI with [[support-and-resistance]] levels (take the overbought/oversold reading only when price is also at a structural level) and avoid acting on MFI extremes during strong trends, where the oscillator can pin above 80 (or below 20) for extended runs.

## MFI vs RSI

MFI incorporates volume, making it more sensitive to institutional activity. In liquid markets where volume data is reliable (equities, futures), MFI can provide earlier signals than RSI. In markets with unreliable volume data (forex spot), RSI may be preferred (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=100` — OHLCV bars supply every MFI input: high/low/close for typical price, plus per-bar volume
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=4h&limit=100` — the same computation on Hyperliquid perps
- `GET /api/v1/market-data/volume-history?days=90` — daily volume with buy ratio as a sanity check on the volume input

**Historical data:**
- `GET /api/v1/backtesting/klines` — full kline archive (Binance spot 1h/4h/1d back to 2017-08) for MFI threshold and divergence backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=100"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — from `GET /api/v1/market-data/klines`: typical price = (H+L+C)/3, raw money flow = TP × volume, then the 14-bar positive/negative flow ratio into the RSI-form index exactly as above
- **Signal** — flag divergences (price high with lower MFI peak) rather than raw 80/20 touches; in crypto trends MFI pins at extremes for long stretches, so extremes alone are continuation evidence, not fade signals
- **Backtest** — replay over `GET /api/v1/backtesting/klines` (1h/4h/1d back to 2017-08) and compare MFI-filtered entries against plain RSI entries — the volume term is only earning its keep if the two disagree profitably
- **Tip** — the page's wash-trading caveat is the crypto-specific failure mode: restrict MFI to major Binance pairs where volume is credible, and cross-check suspicious flow readings against `GET /api/v1/market-intelligence/taker-buy-sell` (aggressive buy/sell split by exchange)

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Quong, G. and Soudack, A. (1989), "Volume-Weighted RSI: Money Flow," *Technical Analysis of Stocks & Commodities* — original publication of the MFI
- Murphy, J. (1999), *Technical Analysis of the Financial Markets*, New York Institute of Finance — oscillator interpretation, overbought/oversold and divergence concepts

## Related

- [[rsi]]
- [[volume]]
- [[vwap]]
- [[chaikin-money-flow]]
