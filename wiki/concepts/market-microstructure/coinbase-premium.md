---
title: "Coinbase Premium"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [crypto, market-microstructure, on-chain, sentiment, indicators, bitcoin]
aliases: ["Coinbase Premium", "Coinbase Premium Index", "Coinbase Premium Gap"]
domain: [market-microstructure, on-chain]
prerequisites: ["[[spot-price]]", "[[bitcoin]]"]
difficulty: intermediate
related: ["[[exchange-netflow]]", "[[spot-etf-flows]]", "[[cvd]]", "[[stablecoin-supply]]", "[[fear-and-greed-index]]", "[[binance]]", "[[coinbase]]", "[[funding-rate]]"]
---

The **Coinbase Premium** is the price gap between Bitcoin on Coinbase (quoted in USD, dominated by US institutional and retail flow) and Bitcoin on Binance (quoted in USDT, dominated by offshore/retail flow). A **positive** premium — Coinbase trading above Binance — signals net US-side buying pressure; a **negative** premium (a "Coinbase discount") signals US-side selling. It is one of the most-watched proxies for *who* is driving a move, and is most informative at inflection points rather than as a standalone entry trigger.

## Definition

```
Coinbase Premium Gap = price(BTC-USD, Coinbase) − price(BTC-USDT, Binance)
Coinbase Premium Index = (gap / price_Binance) × 100   # in %
```

Because Binance quotes in USDT, part of the raw gap reflects the [[stablecoin-supply|USDT/USD]] peg deviation, not spot demand — during a USDT depeg the premium is contaminated and should be read against the stablecoin peg.

## Why it carries signal

- **Venue clientele differs.** Coinbase is the primary on-ramp for US institutions (and the custody venue behind several spot ETFs), so sustained Coinbase buying is a read on US institutional demand — the marginal buyer in the ETF era. Binance skews offshore/leveraged.
- **Leads at turns.** A rally that Binance leads while Coinbase lags (negative premium) is often leverage-driven and fragile; a rally confirmed by a positive Coinbase premium has spot/institutional support and tends to be more durable. The symmetric read applies to sell-offs.
- **ETF-flow corroboration.** The premium tends to move with net [[spot-etf-flows|spot-ETF flows]] and Coinbase-side [[exchange-netflow|exchange netflow]] — cross-confirming all three is stronger than any one alone.

## How to use it

- **Confirmation, not trigger.** Use the premium to grade the *quality* of a move (spot-led vs leverage-led), gating or sizing positions from other signals rather than firing entries off the premium itself.
- **Divergence.** Price making highs while the premium rolls over = US demand fading into strength (distribution risk). Price making lows while the premium turns up = US accumulation into weakness.
- **Regime context.** The premium is most reliable in trending/institutional regimes; in thin offshore-driven memecoin phases it carries little information. See [[crypto-market-regime-taxonomy]].

## Pitfalls

- **USDT peg contamination** (above) — always sanity-check against the peg.
- **Not a magnitude signal.** The sign and trend matter more than the absolute basis points; the raw gap is small and noisy intra-hour.
- **Fee/withdrawal frictions** keep the premium from arbing to zero, so a persistent small premium is normal, not a signal.

## Getting the Data (CryptoDataAPI)

**Live / recent:**
- `GET /api/v1/market-intelligence/coinbase-premium` — Coinbase premium index (Coinbase vs Binance BTC), historical series included

**Corroborating feeds:**
- `GET /api/v1/market-intelligence/etf/btc/aum` and `GET /api/v1/market-intelligence/etf/btc/flows` — US spot-ETF demand
- `GET /api/v1/on-chain/exchange-flows/BTC` — Coinbase-side inflow/outflow
- `GET /api/v1/sentiment/stablecoins` — USDT peg / supply, to de-contaminate the gap

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/coinbase-premium"
```

Auth: `X-API-Key` header. See [[cryptodataapi-market-intelligence]] for the full category.

## Related

- [[spot-etf-flows]] — the demand channel the premium proxies in the ETF era
- [[exchange-netflow]] — on-chain confirmation of exchange-side accumulation/distribution
- [[stablecoin-supply]] — USDT peg context that can distort the raw gap
- [[crypto-signal-library]] — where this sits among tradeable crypto signals

## Sources

- CryptoQuant / Coinglass Coinbase Premium Index documentation
- https://cryptodataapi.com/api/docs (market-intelligence/coinbase-premium)
