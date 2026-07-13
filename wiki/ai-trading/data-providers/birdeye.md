---
title: "Birdeye"
type: entity
created: 2026-05-04
updated: 2026-07-13
status: good
tags: [data-provider, crypto, defi, altcoins]
entity_type: company
website: https://birdeye.so
aliases: ["Birdeye.so"]
related:
  - "[[cryptodataapi]]"
  - "[[dex-screener]]"
  - "[[gmgn]]"
  - "[[solana]]"
  - "[[pump-fun]]"
  - "[[holder-concentration-analysis]]"
  - "[[rug-detection-checklist]]"
  - "[[memecoin-sniping]]"
---

# Birdeye

## Overview

**Birdeye** (birdeye.so) is a Solana-focused token analytics platform offering real-time price charts, holder analysis, whale wallet tracking, and Pump.fun-specific leaderboards. While it has expanded multi-chain coverage over time, its core strength remains [[solana]] memecoin and DeFi analytics, where its depth of holder-level data and freshness of new-token discovery make it a primary tool for sniping and short-term momentum trading.

For traders working in the low-cap and memecoin segments -- particularly tokens originating on [[pump-fun]] -- Birdeye sits alongside [[dex-screener]] and [[gmgn]] as a default daily-driver dashboard.

---

## Key Features

### Solana-First Token Analytics
- **Real-time charts:** Candlestick charts with on-chain trade data for any Solana SPL token, including very low-cap and newly launched tokens
- **Pump.fun integration:** Dedicated leaderboards and views for tokens currently on the Pump.fun bonding curve and recently graduated tokens
- **Multi-chain expansion:** Coverage has grown to include other chains (Ethereum, BNB Chain, Base, others), but Solana remains the deepest dataset

### Holder & Wallet Intelligence
- **Top-holder breakdown:** Lists the largest wallets in any token, surface concentrations that indicate bundling or insider stacking (key input for [[holder-concentration-analysis]])
- **Whale tracking:** Watch lists for large wallets, with notifications when they enter or exit positions
- **Wallet PnL views:** Per-wallet realized and unrealized profit/loss across their token portfolio, useful for identifying smart money to copy-trade

### Real-Time Alerts
- **Price alerts:** Configurable thresholds on price, market cap, and volume
- **New listing alerts:** Push notifications for newly created pairs that match user-defined filters (liquidity, holder count, age)
- **Movement alerts:** Sudden volume or holder spikes flagged in near-real-time

### Trader Leaderboards
- **Top traders by token:** Per-token ranking of wallets that generated the most realized PnL
- **Ecosystem-wide leaderboards:** Wallet rankings across recent timeframes, useful for sourcing new copy-trade targets

---

## Pricing & Access

- **Free tier:** The web interface is largely free for individual traders, including charts, holder lists, and basic alerts
- **Premium tier:** Paid subscription unlocks advanced filters, more alerts, deeper historical data, and higher API rate limits
- **API — Birdeye Data Services (BDS):** Birdeye's B2B data arm (bds.birdeye.so) offers 60+ REST APIs and 8 WebSocket stream types covering token metadata, OHLCV, holders, trades, and wallet data, with tiered free and paid packages. As of 2026 BDS markets coverage of data from 180+ decentralized exchanges (Jupiter, Uniswap, Orca, PancakeSwap, 1inch, Quickswap, etc.) across roughly 10 chains, including Solana, Ethereum, BNB Chain, Arbitrum, Optimism, Avalanche, Base, Polygon, and zkSync Era (per bds.birdeye.so and docs.birdeye.so, June 2026)
- **Wallet connection:** Connecting a Solana wallet enables portfolio tracking and personalized leaderboards but is optional for read-only research
- **Naming note:** "BDS" stands for Birdeye Data Services, the API product line — it is not a token. No Birdeye token launch could be verified as of June 2026. (Birdeye the crypto platform is also unrelated to the US SaaS reputation-management company of the same name)

Specific pricing changes frequently; check birdeye.so / bds.birdeye.so for current plans.

---

## Use Cases for Traders

- **Pre-trade due diligence:** Pull up a token's top holders to check for bundled allocations (e.g., 5 wallets holding 80%) -- a fast filter against rug pulls (see [[rug-detection-checklist]])
- **Pump.fun discovery:** Use Birdeye's bonding-curve leaderboards to surface tokens approaching graduation, a key entry signal for [[token-migration-sniping]]
- **Smart money copy-trading:** Identify wallets with consistent positive PnL on Solana memecoins and mirror their early entries
- **Liquidity / volume monitoring:** Track real-time volume and liquidity changes as confirmation signals for [[memecoin-sniping]] entries and exits
- **Market cap level trading:** Combine Birdeye's MC view with psychological MC thresholds ($100k, $500k, $1M) to time entries and exits on low-caps
- **Whale exit detection:** Set alerts on top holders of an active position so that a large dev or insider sell triggers immediate notification
- **Multi-tool workflow:** Pair with [[dex-screener]] for cross-chain pair discovery and [[gmgn]] for Telegram-based execution after Birdeye-driven research

---

## Limitations

- **Solana-centric:** Strongest on [[solana]]; multi-chain coverage exists but is shallower than [[dex-screener]] for some EVM ecosystems
- **Data lag on extreme launches:** During very high-throughput Solana events (mass memecoin launches), holder and PnL data can briefly lag the chain
- **Not a trade execution venue:** Birdeye is analytics-only -- execution still happens via wallet, aggregator, or sniper bot
- **Leaderboard gaming:** Wallet leaderboards can be gamed by wash-trading or by farming displays; verify with on-chain history before copy-trading
- **Free tier rate limits:** API rate limits on the free tier can be restrictive for systematic users; production sniping pipelines typically require paid plans
- **Memecoin survivorship bias:** "Top trader" leaderboards naturally over-represent winners on tokens that pumped; not a guaranteed forward-looking edge

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]])
- Birdeye platform — https://birdeye.so
- Birdeye Data Services (API products and pricing) — https://bds.birdeye.so
- Birdeye documentation, data coverage — https://docs.birdeye.so/docs/data-coverage
- CryptoAdventure, "Birdeye Review 2026: Solana Token Analytics, Wallet Tracking, and Trade Signals" — https://cryptoadventure.com/birdeye-review-2026-solana-token-analytics-wallet-tracking-and-trade-signals/
- Verified via web search, 2026-06-10

---

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

## Related

- [[dex-screener]] -- broader multi-chain DEX analytics; complementary
- [[gmgn]] -- Telegram-based Solana sniper / analytics tool, often paired with Birdeye
- [[solana]] -- the primary chain Birdeye covers
- [[pump-fun]] -- key data source feeding Birdeye's bonding-curve leaderboards
- [[holder-concentration-analysis]] -- one of Birdeye's primary use cases
- [[rug-detection-checklist]] -- Birdeye holder data is a core input
- [[memecoin-sniping]] -- the strategy family Birdeye most directly supports
