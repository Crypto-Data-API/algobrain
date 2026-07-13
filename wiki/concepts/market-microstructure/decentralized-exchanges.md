---
title: "Decentralized Exchanges (DEXs)"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, dex, defi, trading, amm]
aliases: ["decentralized-exchange", "Decentralized Exchange", "DEX", "DEXs"]
related: ["[[defi]]", "[[uniswap]]", "[[dydx]]", "[[gmx]]", "[[hyperliquid]]", "[[smart-contracts]]", "[[liquidity]]", "[[slippage]]"]
---

# Decentralized Exchanges (DEXs)

A **decentralized exchange (DEX)** is a [[crypto-markets|cryptocurrency]] trading platform that operates without a central intermediary, using [[smart-contracts]] to facilitate trades directly between users. DEXs are a cornerstone of [[defi]] and come in two primary designs: **automated market makers (AMMs)** and **on-chain order books**.

---

## DEX Architectures

### Automated Market Makers (AMMs)
Liquidity providers deposit token pairs into pools. Prices are set algorithmically (e.g., constant product formula x * y = k). Traders swap against the pool rather than matching with a counterparty. Examples: [[uniswap]], Curve, SushiSwap.

### On-Chain Order Books
Traditional limit order book matching executed on-chain or in a hybrid on/off-chain architecture (or via a decentralized sequencer). Enables familiar trading UX with limit orders, stop-losses, visible depth, and leverage, but requires higher-throughput blockchains to function efficiently. Examples: [[hyperliquid]], [[dydx]], Serum.

---

## Key Advantages and Trade-offs

DEXs offer **self-custody** (users never hand over private keys), **permissionless access** (no KYC or account approval), and **censorship resistance**. The trade-offs:

- **Lower [[liquidity]]** than centralized exchanges, especially for long-tail pairs
- **Higher transaction costs** (gas fees on Ethereum, network fees on other chains)
- **Impermanent loss** for AMM liquidity providers when pooled-asset prices diverge
- **Higher [[slippage]]** on large orders against thin pools
- **Smart-contract exploit risk** and front-running by MEV (maximal extractable value) bots

---

## Major DEXs

| Protocol | Type | Chain(s) | Specialty |
|---|---|---|---|
| [[uniswap]] | AMM | Ethereum, L2s | Largest spot DEX by volume |
| [[hyperliquid]] | Order book | Hyperliquid L1 | Perpetual futures, highest perps volume |
| [[dydx]] | Order book | dYdX Chain | Decentralized perps pioneer |
| [[gmx]] | AMM-hybrid | [[arbitrum]], Avalanche | Perps with GLP liquidity model |
| Curve | AMM | Ethereum, L2s | Stablecoin and LST swaps |

---

## Trading Relevance

- DEXs offer [[self-custody]] -- no risk of exchange insolvency or withdrawal freezes
- AMM slippage and liquidity depth are critical considerations for larger trades
- DEX vs CEX volume ratios serve as an indicator of decentralization adoption trends
- [[on-chain-analysis|On-chain]] DEX activity (new pair listings, volume spikes) often front-runs centralized exchange listings
- MEV (maximal extractable value) and sandwich attacks are DEX-specific risks that affect execution quality

---

## See Also

- [[defi]] -- The broader ecosystem DEXs operate within
- [[uniswap]] -- Largest AMM-style DEX
- [[hyperliquid]] -- Leading on-chain order book exchange
- [[smart-contracts]] -- The technology enabling trustless trading
- [[liquidity]], [[slippage]] -- key execution considerations on DEXs
- [[crypto-markets]] -- market context

## Sources

- Synthesised from DEX protocol documentation (Uniswap, dYdX, Curve, GMX, Hyperliquid) and general DeFi market-microstructure references.
