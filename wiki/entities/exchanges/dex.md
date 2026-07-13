---
title: "DEX"
type: redirect
created: 2026-04-15
updated: 2026-07-13
status: good
tags: [exchange, crypto, defi]
aliases: ["Dex", "DEX", "Decentralized Exchange (redirect)"]
related: ["[[decentralized-exchanges]]", "[[uniswap]]", "[[hyperliquid]]", "[[cryptodataapi]]"]
---

See [[decentralized-exchanges]].

This page existed as an empty stub for "DEX" (decentralized exchange). The topic is covered in full at [[decentralized-exchanges]] (concept page, market-microstructure), with a shorter companion at [[decentralized-exchange]]. For specific venues see [[uniswap]], [[hyperliquid]], [[dydx]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].
