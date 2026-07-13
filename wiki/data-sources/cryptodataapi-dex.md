---
title: "CryptoDataAPI — DEX & Meme Coins"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, dex, memecoins, rug-detection, token-security, solana, on-chain]
aliases: ["CryptoDataAPI DEX", "CDA DEX", "CryptoDataAPI Meme Coins", "CryptoDataAPI Token Security"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-coins]]", "[[cryptodataapi-on-chain]]", "[[dex-screener]]", "[[memecoin-sniping]]", "[[rug-detection-checklist]]", "[[rug-pulls]]", "[[low-cap-crypto-trading-map]]"]
---

CryptoDataAPI's DEX & Meme Coins section covers the on-chain long tail: trending pools and newest launches across Solana, Ethereum, Base, BSC, and Arbitrum, per-token detail, and a security report for rug and honeypot detection. It also exposes a promoted-tokens feed that surfaces marketing spend as a tradeable signal — an API-first alternative to browsing [[dex-screener]].

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/dex/trending | Trending DEX pools | Solana/Ethereum/Base/BSC/Arbitrum | — |
| GET | /api/v1/dex/new-pools | Newest launches, multi-chain | — | — |
| GET | /api/v1/dex/token/{chain}/{address} | Token info + top pools | chain, address | — |
| GET | /api/v1/dex/promoted | Recently promoted tokens (marketing spend signal) | — | Pro |
| GET | /api/v1/dex/promoted/top | Top by promotion spend | — | Pro |
| GET | /api/v1/dex/security/{chain}/{address} | Token security report (rug/honeypot detection) | chain, address | — |

## Live Data

All six endpoints serve current state: `/dex/trending` and `/dex/new-pools` are rolling live feeds of what is moving and what just launched, `/dex/token/{chain}/{address}` and `/dex/security/{chain}/{address}` return on-demand snapshots for a specific contract, and the two `promoted` endpoints reflect recent marketing activity.

## Historical Data

This section is live-only — there are no dedicated history endpoints. To build launch or lifecycle history, poll `/dex/new-pools` and store results yourself, and use the [[cryptodataapi-regimes]] meme-regime endpoints (per-symbol 60d history, market-wide meme-hype score) for the historical view of meme-market conditions.

## Trading Applications

- **Launch sniping** — `/dex/new-pools` feeds [[memecoin-sniping]] pipelines with multi-chain launches the moment they appear
- **Automated rug screening** — run every candidate through `/dex/security/{chain}/{address}` as the API step of the [[rug-detection-checklist]] before risking capital on potential [[rug-pulls]]
- **Marketing-spend alpha** — the promoted feeds reveal which teams are paying for visibility, an early-attention signal for [[low-cap-crypto-trading-map]] plays
- **Momentum rotation** — `/dex/trending` per chain shows where retail flow is concentrating, replacing manual [[dex-screener]] monitoring
- **Regime gating** — only size up meme entries when the meme_season flag on [[cryptodataapi-regimes]] confirms a favourable backdrop

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

## Related

- [[cryptodataapi]] — provider hub (auth, tiers, category map)
- [[cryptodataapi-regimes]] — meme lifecycle regime + meme_season flag
- [[cryptodataapi-coins]] — profiles for established listed assets
- [[cryptodataapi-on-chain]] — exchange flows and whale signals
- [[dex-screener]] — browser-first counterpart
- [[memecoin-sniping]], [[rug-detection-checklist]], [[rug-pulls]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
