---
title: "CryptoDataAPI — NFTs"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, nft, collections, volume]
aliases: ["CDA NFTs", "CryptoDataAPI NFTs", "cryptodataapi nft endpoints"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-coins]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-dex]]", "[[nft]]", "[[nft-floor-price]]", "[[nft-trading]]"]
---

The NFTs category of [[cryptodataapi]] covers the non-fungible side of the market: an overall market overview, collection listings and single-collection detail, supported chains and categories, volume data, and cross-collection correlations. It gives strategies a structured read on NFT market activity without scraping marketplaces.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/nfts/overview | NFT market overview | — | — |
| GET | /api/v1/nfts/collections | List NFT collections | — | — |
| GET | /api/v1/nfts/collections/{slug} | Single collection | slug | — |
| GET | /api/v1/nfts/chains | Supported chains | — | — |
| GET | /api/v1/nfts/categories | Categories | — | — |
| GET | /api/v1/nfts/volume | NFT volume data | — | — |
| GET | /api/v1/nfts/correlations | Collection correlations | — | — |

Tier "—" means the docs list no tier restriction for that endpoint.

## Live Data

All endpoints in this category serve **current state**: the market overview, today's collection list and per-collection detail (`/nfts/collections/{slug}`), the supported chain and category taxonomies, current volume data, and the latest collection-correlation matrix.

## Historical Data

The NFTs section exposes no dedicated history endpoints in the docs. Correlations and volume are derived from market activity but are served as current readings — build your own timeseries by sampling these endpoints on a schedule if you need history.

## Trading Applications

- **Collection screening** — `/nfts/collections` plus per-slug detail gives the universe and stats for [[nft-trading]] strategies, including [[nft-floor-price]]-driven entries
- **Risk-appetite gauge** — NFT volume expanding alongside broad crypto strength signals speculative appetite at the frothy end of the [[nft]] market; collapsing volume often precedes broader risk-off
- **Diversification within NFTs** — `/nfts/correlations` identifies which collections move together, so an NFT book isn't unintentionally one concentrated bet
- **Chain rotation** — `/nfts/chains` and per-chain activity show where NFT liquidity is migrating, informing which ecosystem tokens benefit
- **Cross-checking with market health** — pairing NFT volume with [[cryptodataapi-market-health]] scores helps separate NFT-specific manias from broad-market moves

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/nfts/overview"
```

## Related

- [[cryptodataapi]] — hub page with auth, tiers, and the full category map
- [[cryptodataapi-coins]] — fungible-asset universe and category taxonomy
- [[cryptodataapi-dex]] — the other speculative long-tail surface (DEX and memecoins)
- [[cryptodataapi-market-health]] — market-wide condition scores to contextualise NFT activity
- [[nft]], [[nft-floor-price]], [[nft-trading]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
