---
title: "Altcoins"
type: concept
created: 2026-07-19
updated: 2026-08-20
status: draft
tags: [crypto, altcoins, market-microstructure]
aliases: ["Alt Season", "Alts", "Altcoin", "Altseason"]
domain: [crypto, market-microstructure]
prerequisites: ["[[bitcoin]]", "[[market-cap]]"]
difficulty: beginner
---

# Altcoins

**Altcoins** ("alternative coins") is the umbrella term for every crypto asset other than [[bitcoin|Bitcoin]] — in stricter trading usage, often excluding [[ethereum|Ethereum]] too, since ETH is liquid and large-cap enough to run its own regime rather than moving in lockstep with the broader "alt" complex. As a group, altcoins are higher-beta, lower-liquidity, and more narrative-driven than BTC, and what traders actually track is not their dollar price but their *relative* performance against BTC — the metric that defines "alt season."

## How It Works

**BTC dominance (BTC.D)** — BTC's share of total crypto market cap — is the anchor statistic. Falling BTC.D combined with a rising total market cap means capital is rotating out of BTC and into alts while the overall pie is still growing: the classic, healthy alt-season setup. Falling BTC.D with a flat or falling total cap is a weaker, more speculative signal — alts gaining share of a shrinking market rather than genuinely outperforming. The **ETH/BTC ratio** is the most-watched single bellwether, since Ethereum is usually the first mover of a rotation before it broadens into mid- and small-caps.

Altcoins behave like leveraged, high-beta versions of BTC: in bull markets they can outperform BTC by 2-5x or more; in bear markets they typically draw down harder and for longer, since liquidity thins out first in the long tail. This asymmetry is structural, not incidental — most altcoins have thinner order books, smaller free float relative to fully diluted supply, and less-diversified holder bases than BTC, so both buying and selling pressure move price more per dollar of flow. **Market-breadth** measures (the percentage of coins trading above a moving average, or the percentage outperforming BTC over a trailing window — the basis of the widely cited "Altcoin Season Index") quantify how broad a rotation is, distinguishing a genuine sector-wide alt season from a handful of large-caps carrying the tape.

Altcoins are commonly bucketed by liquidity tier and category: large-cap alts (ETH, SOL, BNB, XRP) that trade on every major venue with deep books; mid-caps with meaningful but shallower liquidity; and a long tail of micro-caps and [[meme-coins|memecoins]] where slippage and manipulation risk dominate. Categorically, the "altcoin" label spans [[layer-1|layer-1]] and [[layer-2|layer-2]] chains, [[defi|DeFi]] protocol tokens, infrastructure and oracle tokens, and speculative/narrative plays — each of which can rotate independently even within a single alt-season window.

## Concrete Examples

- **2017 ICO boom:** thousands of new ERC-20 tokens launched; many rose 10-50x during the year while BTC itself was "only" up roughly 13x, the archetypal broad-based alt mania.
- **2021, two distinct alt seasons:** a Q1 2021 wave tied to the DeFi-summer aftermath and early NFT speculation, and a Q4 2021 wave concentrated in layer-1 "Ethereum killers" (Solana, Avalanche, Terra/LUNA among them) as capital rotated into scaling narratives.
- **2022 bear market:** BTC fell roughly 77% peak-to-trough (from its November 2021 all-time high near $69,000 to under $16,000 by late 2022); most altcoins fell 90%+ over the same window, illustrating the drawdown asymmetry directly.
- **2024-2025 "no alt-season" debate:** BTC dominance trended higher through much of 2024 even as BTC itself made new all-time highs, as spot BTC ETF inflows concentrated demand in BTC specifically rather than broadening into the alt complex — a cycle traders widely discussed as breaking the historical pattern of alts eventually catching up.

## Trading Relevance

- **[[crypto-beta-rotation]]:** a strategy built directly on the BTC-vs-alt beta relationship — sizing alt exposure up when the market-wide risk backdrop favors higher beta, and rotating back to BTC when it doesn't.
- **[[momentum-rotation]]:** ranks and rotates into the strongest-momentum names within the alt universe, the natural strategy wrapper for chasing sector leadership once a rotation is underway.
- **[[bitcoin-dominance-rotation]]:** the AlgoBrain narrative-impact catalog entry documenting the BTC-dominance rotation pattern as a tradeable, recurring event.
- **[[btc-dominance]]:** the underlying market page for the dominance metric itself — the primary gauge for whether a rotation is starting, broadening, or reversing.
- **[[correlation-regime]]:** altcoins as a group carry high pairwise correlation, especially in drawdowns, which erodes the diversification benefit of holding a basket of "different" alt names during risk-off periods.
- **[[multi-strategy-crypto-portfolio]]:** altcoin exposure is typically sized as a distinct, higher-volatility sleeve rather than treated as interchangeable with a core BTC/ETH allocation, given the drawdown and liquidity differences documented above.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-health/altcoin-breadth` — percentage of coins trading above a chosen moving average (5-365 days, default 200) — the direct breadth signal for alt-season confirmation
- `GET /api/v1/coins/top?limit=100` — current altcoin universe ranked by market cap
- `GET /api/v1/daily/prices` — bulk snapshot of roughly 2,500 Binance spot pairs for cross-sectional altcoin screening

**Historical data:**
- `GET /api/v1/market-health/history?days=730` — up to two years of historical breadth and health scores for backtesting alt-season regimes
- `GET /api/v1/market-data/klines` — per-symbol OHLCV history for individual altcoin backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth?ma_period=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-health]], [[cryptodataapi-coins]].

## Related

- [[bitcoin]] — the reference asset altcoins are defined and measured against
- [[btc-dominance]] — the core rotation metric
- [[bitcoin-dominance-rotation]] — narrative-impact catalog entry for the rotation pattern
- [[crypto-beta-rotation]] — strategy trading the BTC-vs-alt beta relationship
- [[momentum-rotation]] — momentum-ranked rotation within the alt universe
- [[correlation-regime]] — pairwise correlation dynamics that shape alt-basket risk
- [[market-breadth]] — the breadth measure underlying alt-season confirmation
- [[market-cap]] — the sizing metric behind large/mid/micro-cap tiers
- [[multi-strategy-crypto-portfolio]] — portfolio context for sizing alt exposure

## Sources

- General crypto/market-structure knowledge; no specific wiki source ingested yet.
