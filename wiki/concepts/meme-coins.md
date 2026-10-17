---
title: "Meme Coins"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: draft
tags: [crypto]
aliases: ["meme coins", "Memecoins", "memecoins", "Meme Tokens"]
domain: [crypto, behavioral-finance, market-microstructure]
prerequisites: ["[[altcoins]]", "[[narrative-trading]]"]
difficulty: intermediate
related: ["[[memecoin-mania]]", "[[meme-speculative-regime]]", "[[meme-coin-cycle]]", "[[memecoin-majors-basket]]", "[[memecoin-sniping]]", "[[pump-fun]]", "[[rug-pulls]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-dex]]"]
---

# Meme Coins

**Meme coins** are crypto tokens whose value rests on attention, community identity and internet culture rather than on cash flows, protocol usage or a technical roadmap. They range from decade-old, deeply liquid assets such as [[dogecoin|Dogecoin]] to tokens created minutes ago on a launchpad. Because nothing anchors their price except the next buyer, they are the purest expression of crypto's reflexive, sentiment-driven side — and one of the clearest risk-appetite gauges in the market.

## Overview

Meme coins have no claim on revenue and usually no utility beyond being held, traded and talked about. Price is set by attention against float: when a coin captures the timeline, a wall of retail demand meets thin order books and price goes vertical; when attention moves on, there is no fundamental floor. The narrative-level patterns (celebrity pumps, launch-day parabolas, "meme season" tops) are catalogued on [[memecoin-mania]]; this page covers the asset class itself.

Two broad tiers trade very differently:

- **Established memes** — DOGE, [[shiba-inu|SHIB]], [[pepe|PEPE]], [[bonk|BONK]], [[dogwifcoin|WIF]] and similar names with years of history, major-exchange listings and listed perpetuals. They behave like a high-beta sector of [[altcoins]]: they survive bear markets and revive in each new risk-on phase.
- **Launch tokens** — fresh contracts created on launchpads such as [[pump-fun|Pump.fun]] on [[solana|Solana]] or on [[base|Base]]. Most go to zero within days; the small fraction that catch on deliver very large returns to the earliest buyers.

## Lifecycle and History

- **Dogecoin (December 2013)** — created by Billy Markus and Jackson Palmer as a joke on Bitcoin, it became the template for the category. Its May 2021 run into Elon Musk's *Saturday Night Live* appearance (8 May 2021) is the canonical "sell the event" example.
- **Shiba Inu (August 2020)** — the "Dogecoin killer" that showed an Ethereum ERC-20 meme could reach a top-20 market cap during the 2021 cycle.
- **PEPE (April 2023) and BONK (December 2022)** — PEPE revived Ethereum meme trading in a bear-market lull; BONK's Solana airdrop became a symbol of Solana's post-FTX recovery.
- **The launchpad era (2024-2025)** — Pump.fun, which launched in early 2024, made creating a tradeable token a seconds-long, near-free action. Millions of tokens followed, and the [[2024-meme-coin-supercycle]] turned Solana into the dominant meme chain.
- **Political memes (January 2025)** — the [[official-trump|TRUMP]] token, launched days before the 2025 US presidential inauguration, showed how a single high-profile issuer can pull billions of dollars of attention (and liquidity) into one contract within hours.

Each wave follows the same arc: ignition on a few names, broad "meme season" as capital rotates down the market-cap curve, distribution by early holders, then a long bleed. CryptoDataAPI's meme regime classifier (below) uses that same arc — `ignition`, `euphoric`, `distribution`, `bleeding`, `dormant`.

## Market Structure

- **Venues.** Launch tokens trade first on DEX pools (bonding curves, then AMM pools after "graduation"); established memes trade on centralized exchanges and as [[perpetual-futures]], including Hyperliquid's thousand-unit contracts (kPEPE, kBONK, kSHIB).
- **Float and supply.** Most launch tokens have a fixed supply, but insiders, deployers and sniper bots often hold a large share of the float at launch. Concentrated holdings, retained mint or freeze authority, and unlocked liquidity are the main warning signs of [[rug-pulls]] (see the [[rug-detection-checklist]]).
- **Order flow.** Early flow is dominated by bots: [[memecoin-sniping]] bots buy within seconds of pool creation, and [[telegram|Telegram]] trading bots route much of the retail flow on Solana.
- **Leverage.** On listed perps, meme rallies push [[funding-rate|funding]] sharply positive; the unwinds are some of the largest liquidation events by percentage move in crypto.

## Trading Relevance

- **Regime gauge.** Broad meme strength is a late-cycle, risk-on signal. The [[meme-speculative-regime]] page defines how to detect it; peak meme euphoria has historically marked froth for the whole market (see [[memecoin-mania]]).
- **Basket strategies.** [[memecoin-majors-basket]] takes meme-season beta through the established names; [[meme-coin-cycle]] trades the rotation into higher-beta meme perps and the reversal out of it.
- **Launch trading.** [[memecoin-sniping]] and [[pump-fun-bonding-curve-sniping]] trade the first seconds to hours of a token's life. This is a latency and risk-control game with a high base rate of total loss on any single name.
- **Short side.** Exhausted meme rallies with crowded funding are candidates for [[crowded-long-funding-fade]] and [[distribution-post-peak-short-book]].
- **Narrative timing.** Meme rotations are a recurring entry in the [[narrative-trading]] playbook; position size must assume the coin can lose most of its value in a day.

## Risks

- **No fundamental floor** — drawdowns of 80-99% are normal, not exceptional.
- **Rug pulls and insider dumps** — the deployer or early wallets can drain liquidity or sell into the first wave of buyers.
- **Liquidity illusion** — quoted market caps are float × last price; real exit depth is often a small fraction of that.
- **Survivorship bias** — the famous winners hide millions of tokens that went to zero, which makes any backtest built on today's surviving tickers unreliable.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/meme/regime` — per-asset meme regime (`euphoric`, `distribution`, `ignition`, `bleeding`, `dormant`) across the curated meme universe, from trailing returns, volume spikes, realized-vol percentile, SMA-20 extension and live Hyperliquid funding
- `GET /api/v1/meme/regime/score` — market-wide meme-hype composite (0-100) with a `meme_season` flag
- `GET /api/v1/dex/new-pools` — newest DEX pools, for launch discovery
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug detection, honeypot check, risk scoring)

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme regime detail with 60 days of daily history (Pro+)
- `GET /api/v1/backtesting/klines` — historical OHLCV for listed meme pairs, for testing meme-season rules

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/meme/regime/score"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-regimes]] (meme regime) and [[cryptodataapi-dex]] (DEX pools and token security).

## Related

- [[memecoin-mania]] — narrative impact catalog for meme-coin events
- [[meme-speculative-regime]] — detecting a meme-driven market regime
- [[meme-coin-cycle]] and [[memecoin-majors-basket]] — Hyperliquid basket strategies
- [[memecoin-sniping]], [[pump-fun-bonding-curve-sniping]] — launch-phase strategies
- [[pump-fun]] — the dominant Solana launchpad
- [[rug-pulls]], [[rug-detection-checklist]] — the main failure mode and how to screen for it
- [[2024-meme-coin-supercycle]] — the launchpad-era boom
- [[dogecoin]], [[shiba-inu]], [[pepe]], [[bonk]], [[dogwifcoin]], [[official-trump]]
- [[altcoins]], [[narrative-trading]], [[low-cap-crypto-trading-map]]
