---
title: "Immutable"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, nft]
aliases: ["IMX", "Immutable X"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://imx.community/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[layer-1]]", "[[gaming-tokens]]", "[[proof-of-stake]]", "[[hyperliquid]]"]
---

# Immutable

**Immutable** (ticker **IMX**) is a gaming-focused [[layer-2]] scaling ecosystem on [[ethereum|Ethereum]]. IMX is the native token of the Immutable X network — originally launched as the first zk-rollup for NFTs on Ethereum, and now expanded to **Immutable zkEVM**, a general-purpose zero-knowledge rollup for Web3 games.

Immutable provides gas-free NFT minting and trading, developer tooling, and a marketplace stack tailored to game studios, letting players own in-game assets as NFTs while abstracting away Ethereum's fees and complexity. IMX is used for staking, fees, and ecosystem incentives.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | IMX |
| **Current Price** | $0.141859 |
| **Market Cap** | $119,453,078 (~$119.5M) |
| **Market Cap Rank** | #235 |
| **24h Volume** | $6,851,699 (~$6.9M) |
| **24h Change** | +1.28% |
| **7d Change** | -0.97% |
| **Fully Diluted Valuation** | ~$283.7M |
| **Market Cap / FDV** | ~0.42 |
| **All-Time High** | $9.52 (2021-11-26), ~-98.5% |
| **All-Time Low** | $0.120425 (2026-06-06) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

IMX is modestly up over 24h (+1.3%) and broadly flat over the week (-1.0%) — relatively stable for this cohort — but trades roughly 98.5% below its November 2021 all-time high of $9.52, and sits just ~18% above the fresh cycle-low of $0.120425 printed on 2026-06-06. The backdrop remains extreme fear (crypto [[fear-and-greed-index|Fear & Greed Index]] ~23, an "Established Bear Market" regime with [[bitcoin]] dominance near 59% as of 2026-06-21).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~842.44M IMX |
| **Total Supply** | 2.00B IMX |
| **Max Supply** | 2.00B IMX (fixed cap) |
| **Fully Diluted Valuation** | ~$283.7M |
| **Market Cap / FDV** | ~0.42 |

IMX has a **fixed maximum supply of 2 billion** tokens. With ~842M circulating, the market-cap/FDV ratio of ~0.42 indicates roughly **58% of supply is not yet in circulation** — a substantial **dilution overhang** from team, investor, and ecosystem-development allocations that vest over time. At the current price the gap between the ~$119.5M circulating market cap and the ~$283.7M FDV is the single largest valuation risk on the page: each tranche of unlocked tokens is fresh sell-side supply unless absorbed by demand. IMX is used to pay protocol fees and can be staked, with a portion of marketplace fees flowing to stakers.

---

## Technology & Architecture

Immutable's stack has two generations of [[layer-2]] scaling, both anchored to [[ethereum|Ethereum]] for security:

- **Immutable X (StarkEx validium):** the original product — a zk-rollup/validium built on StarkWare's StarkEx engine — purpose-built for NFTs. It batches trades and mints off-chain and posts validity proofs to Ethereum, delivering **gas-free minting and trading** for users while inheriting Ethereum's settlement guarantees. Data availability is handled off-chain (validium model), trading lower cost for a weaker data-availability assumption than a pure rollup.
- **Immutable zkEVM:** a newer, general-purpose **zero-knowledge EVM rollup** built with [[polygon|Polygon]] technology, letting studios deploy standard Solidity contracts with full EVM compatibility while keeping the gaming-optimised UX. This broadens Immutable from an NFT-only venue to a full programmable game chain.

On top of the chains sit the **Immutable Passport** (non-custodial wallet / identity for players), an **orderbook/marketplace** stack, and developer SDKs. The economic model routes a share of protocol and marketplace fees to IMX stakers, tying token value to ecosystem throughput.

---

## How & Where It Trades

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| Binance | IMX/USDT |
| Kraken | IMX/USD |
| Upbit | IMX/KRW |
| Bitget | IMX/USDT |
| KuCoin | IMX/USDT |
| Crypto.com Exchange | IMX/USD |

### Derivatives & on-chain

| Venue | Instrument | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | IMX-PERP | Perpetual |
| Uniswap V3 ([[ethereum|Ethereum]]) | IMX/WETH | Spot |
| SushiSwap ([[ethereum|Ethereum]]) | IMX/WETH | Spot |

### Contract Address

| Chain | Address |
|---|---|
| Ethereum | `0xf57e7e7c23978c3caec3c3548e3d615c346e79ff` |

IMX is an established, well-distributed token with deep CEX liquidity (Binance, Upbit KRW) and a perpetual market on [[hyperliquid|Hyperliquid]] for leveraged exposure with on-chain funding and open-interest. As an ERC-20, it also trades on Ethereum DEXs including Uniswap V3 and SushiSwap.

---

## Use Case, Narrative & Category

Immutable is the leading **blockchain gaming / NFT [[layer-2]]** infrastructure play. CoinGecko tags include Gaming (GameFi), NFT, Play To Earn, Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK), Rollup, Gaming Blockchains, Immutable zkEVM Ecosystem, plus index inclusions (GMCI 30, Coinbase 50) and portfolios (Animoca Brands, Coinbase Ventures).

The narrative ties IMX to the GameFi cycle: if Web3 gaming achieves mainstream adoption, Immutable aims to be the default settlement and asset-ownership layer for studios, capturing fee flow from NFT minting and trading. As a ZK-rollup, it inherits Ethereum security while offering gas-free UX — positioning it among the more mature, institutionally-backed ([[ethereum|Ethereum]]-aligned) L2s in the gaming vertical. See [[gaming-tokens]] for the broader category.

---

## Valuation Framing (Qualitative)

- **vs. the gaming-L2 niche:** IMX is the largest pure-play **gaming/NFT [[layer-2]]** by market cap, but the entire category is depressed in an extreme-fear regime where speculative GameFi demand is near a cyclical low. The ~$119.5M cap reflects a "show me the users" market: the option value of being the gaming settlement layer is being priced cheaply.
- **MC/FDV discount:** the ~0.42 ratio means the FDV is more than double the circulating cap — any valuation that uses circulating market cap understates the eventual diluted base. A buyer is effectively paying ~$283.7M FDV for the franchise, not ~$119.5M.
- **Fee-capture optionality:** value accrual depends on real minting/trading throughput on Immutable X and zkEVM; in a bear market that throughput is thin, so today's price is largely a forward bet on the next GameFi cycle rather than current cash-flow capture.

---

## Peer Comparison

| Token | Category | Price | Market Cap | Rank | MC/FDV | Max Supply |
|---|---|---|---|---|---|---|
| **Immutable (IMX)** | Gaming/NFT [[layer-2]] | $0.1419 | ~$119.5M | #235 | ~0.42 | 2.00B (fixed) |
| [[zilliqa\|Zilliqa (ZIL)]] | Sharded [[layer-1]] | $0.00312 | ~$61.0M | #392 | ~0.93 | 21.0B |
| [[qtum\|Qtum (QTUM)]] | UTXO+EVM [[layer-1]] | $0.7239 | ~$76.8M | #326 | ~0.98 | Uncapped |
| [[bittorrent\|BitTorrent (BTT)]] | DePIN / [[tron]] satellite | $2.62e-7 | ~$258.7M | #140 | ~1.00 | 990T (fixed) |

*All figures from the 2026-06-21 snapshot. IMX carries by far the largest dilution overhang (lowest MC/FDV) of the cohort but the highest single-token market cap among the L1/L2 peers.*

---

## Notable History

- **All-time high:** $9.52 on 2021-11-26, at the peak of the previous NFT/GameFi mania.
- **All-time low:** $0.120425 on 2026-06-06 — a fresh cycle low set ~two weeks before this snapshot; IMX trades only ~18% above it.
- The ~98.5% drawdown from ATH reflects the multi-year unwind of the 2021 gaming/NFT bubble; IMX's recent price stability relative to peers is notable given the extreme-fear backdrop.

---

## Risks

- **GameFi adoption risk:** the thesis depends on Web3 gaming gaining real, sticky users; the sector has repeatedly over-promised, and a marquee hit game has been elusive.
- **Unlock overhang:** ~58% of supply not yet circulating (MC/FDV ~0.42) means scheduled unlocks can pressure price for years.
- **L2 competition:** the gaming-L2 niche faces competition from general-purpose rollups and rival gaming chains.
- **Bear-market beta:** with [[fear-and-greed-index|Fear & Greed]] at ~23 (extreme fear) and an established bear-market regime, demand for speculative gaming tokens is suppressed.
- **Volatility / liquidity:** ~$119.5M market cap and ~$6.9M daily volume make IMX a small-cap, volatile asset prone to sharp moves and slippage.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[layer-1]]
- [[gaming-tokens]]
- [[polygon]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
