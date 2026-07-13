---
title: "THORChain"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi]
aliases: ["RUNE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://thorchain.org/"
related: ["[[crypto-markets]]", "[[bitcoin]]", "[[ethereum]]", "[[decentralized-exchange]]", "[[cross-chain]]", "[[cross-chain-bridges]]", "[[defi]]", "[[hyperliquid]]"]
---

# THORChain

**THORChain** (ticker **RUNE**) is an independent, Cosmos-SDK-based [[layer-1|Layer-1]] that operates a **[[cross-chain]] [[decentralized-exchange|DEX]]** — it lets users swap *native* assets across chains (e.g. native [[bitcoin|BTC]] for native [[ethereum|ETH]]) without wrapped tokens or centralized custodians. **RUNE** is the protocol's settlement and security asset: every liquidity pool is paired against RUNE, nodes bond RUNE to secure the network, and RUNE captures swap fees. It is a core **cross-chain / [[liquidity|liquidity]] / [[defi|DeFi]] infrastructure** name backed by Multicoin Capital and Delphi Ventures.

## Market Data

| Field | Value |
|---|---|
| **Market Cap Rank** | #220 |
| **Market Cap** | ~$134.48M |
| **Current Price** | $0.3972 |
| **24h Volume** | ~$6.26M |
| **24h Change** | -0.12% |
| **7d Change** | +0.82% |
| **Circulating Supply** | 338.37M RUNE |
| **Max Supply** | 354.21M RUNE |
| **All-Time High** | $20.87 (2021-05-19) — current ~-98.1% |
| **All-Time Low** | $0.00851264 (2019-09-28) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

RUNE is roughly flat over 24h (-0.12%) and the past week (+0.82%), but its ~$6.3M daily volume is notably thin, leaving it vulnerable to slippage on size. The setup is risk-off across crypto: [[crypto-fear-and-greed-index|Fear & Greed]] at **23 (extreme fear)** and an "Established Bear Market" long-horizon regime as of 2026-06-20. RUNE trades ~98% below its 2021 all-time high. See [[market-regime]].

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RUNE |
| **Market Cap Rank** | #220 |
| **Architecture** | Cosmos-SDK Layer 1, Proof of Stake (bonded nodes) |
| **Categories** | Decentralized Exchange (DEX), Infrastructure, Smart Contract Platform, Exchange-based Tokens, Decentralized Finance (DeFi), Layer 1 (L1), Bridge Governance Tokens, Multicoin Capital Portfolio, Proof of Stake (PoS), Delphi Ventures Portfolio |
| **Website** | [https://thorchain.org/](https://thorchain.org/) |

> *Live price/cap/volume figures are consolidated in the **Market Data** block above (2026-06-20). Tables below carry technical, supply, and historical detail.*

---

## Overview

THORChain is the first decentralized exchange (DEX) to swap Bitcoin, and other UTXO chains, with Ethereum, and other EVM chains.  All without using wrapped tokens.

THORChain currently supports swapping between 10 different blockchains.  Assets available to swap on THORChain include the following:

Bitcoin (BTC)
Ethereum (ETH)
Tether (USDT)
BNB (BNB)
XRPL (XRP)
USDC (USDC)
Tron (TRX)
Dogecoin (DOGE)
Bitcoin Cash (BCH)
Wrapped Bitcoin (WBTC)
Chainlink (LINK)
Litecoin (LTC)
Dai (DAI)
Avalanche (AVAX)
Aave (AAVE)
Cosmos (ATOM)

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 338.37M RUNE |
| **Total Supply** | 354.21M RUNE |
| **Max Supply** | 354.21M RUNE |
| **Implied FDV (at max supply)** | ~$140.7M |
| **Circulating / Max Supply** | ~96% |

> *The 2026-06-20 snapshot reports a max supply of ~354.21M RUNE (essentially equal to total supply). This differs from the originally launched 500M hard cap referenced in older documentation; the gap reflects RUNE that was never minted / removed from the schedule. The protocol now sits near full dilution (MC/FDV ~0.96), so supply-side overhang is small.*

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $20.87 (2021-05-19) |
| **Current vs ATH** | ~-98.1% |
| **All-Time Low** | $0.00851264 (2019-09-28) |
| **Current vs ATL** | ~+4570% |
| **24h Change** | -0.12% |
| **7d Change** | +0.82% |

---

## Platform & Chain Information

**Native Chain:** Thorchain

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RUNE/USDT | N/A |
| Kraken | RUNE/EUR | N/A |
| Bitget | RUNE/USDT | N/A |
| KuCoin | RUNE/USDT | N/A |
| Crypto.com Exchange | RUNE/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | RUNE-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://thorchain.org/](https://thorchain.org/) |
| **Twitter** | [@thorchain](https://twitter.com/thorchain) |
| **Reddit** | [https://www.reddit.com/r/THORChain/](https://www.reddit.com/r/THORChain/) |
| **Telegram** | [thorchain_org](https://t.me/thorchain_org) (11,706 members) |
| **Discord** | [https://discord.com/invite/thorchaincommunity](https://discord.com/invite/thorchaincommunity) |
| **GitHub** | [https://github.com/thorchain](https://github.com/thorchain) |
| **Whitepaper** | [https://docs.thorchain.org/](https://docs.thorchain.org/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$6.26M |
| **Market Cap Rank** | #220 |
| **CoinGecko Sentiment** | 67% positive |
| **Last Updated** | 2026-06-20 |

---

## Tokenomics & Supply

RUNE is **near full dilution** (~338M circulating, ~354M total/max; MC/FDV ~0.96 as of 2026-06-20). RUNE plays four roles, and its design deliberately ties protocol value to the token:

1. **Settlement asset** — every pool is `ASSET:RUNE`, so total RUNE demand scales with pooled liquidity (the protocol historically targeted a "deterministic value" of ~3x the value of non-RUNE assets bonded+pooled).
2. **Security bond** — node operators must **bond RUNE** (a large multiple of the assets they secure) to join; misbehavior is slashed, aligning validators with honest operation.
3. **Fee capture** — swap fees and a system income split flow to liquidity providers and bonded nodes.
4. **Incentive pendulum** — RUNE emissions/rewards are dynamically balanced between bonders and LPs to keep the network secure and liquid.

## Use Case, Narrative & Category

THORChain is a **cross-chain DEX / DeFi liquidity protocol** — its category peers are bridges and interoperability layers rather than metaverse tokens. Its differentiator is **native-asset swaps without wrapping**: a user can swap native BTC for native ETH in one transaction, with THORChain's network of vaults (managed by bonded nodes via threshold-signature / TSS multisig) holding the underlying assets. It currently connects ~10 chains, including [[bitcoin]], [[ethereum]], BNB Chain, XRP Ledger, Tron, Dogecoin, Bitcoin Cash, Litecoin, Avalanche, and Cosmos, and supports assets like USDT, USDC, WBTC, LINK, DAI, AAVE, and ATOM.

The investment narrative is **"the decentralized cross-chain liquidity layer"** — capturing swap volume that would otherwise route through centralized exchanges or custodial bridges. Demand for RUNE is meant to grow with total value locked and swap volume. The risk side of the narrative is that THORChain is **operationally complex and custodies real native assets**, which has made it a target.

## How & Where It Trades

- **Spot CEX**: [[binance|Binance]] (RUNE/USDT), Kraken (RUNE/EUR), Bitget, KuCoin, Crypto.com.
- **Native / DEX**: RUNE is the base asset of THORChain's own pools (THORSwap and other front-ends); it is also traded on EVM DEXs via bridged representations.
- **Derivatives**: RUNE has a perp on [[hyperliquid]] (RUNE-PERP) plus major CEX futures. As a thin-volume mid-cap, RUNE perps see [[funding-rate|funding]] and [[open-interest]] swing around protocol news (exploits, halts, restarts); thin spot depth (~$6.3M/24h) means basis and liquidation cascades can be violent. See [[perpetual-futures]] and [[cross-chain-arbitrage]].

## Valuation Framing (Qualitative)

Unlike most altcoins, RUNE has a **mechanically enforced relationship to protocol activity** — the "deterministic value" model historically targeted RUNE's pooled value at a multiple (~3x) of non-RUNE assets in pools, so RUNE demand is supposed to scale with total liquidity. That makes a few qualitative anchors usable:

- **Activity-linked, not pure narrative.** RUNE captures real swap fees and its value is tied (by design) to TVL and swap volume — closer to a productive infrastructure token than a meme. The flip side: when cross-chain swap volume falls, the model deflates RUNE alongside it.
- **Near full dilution = clean float.** With ~96% of supply circulating, there is minimal unlock overhang; the bull case is demand growth, not waiting out vesting.
- **Security is the discount factor.** RUNE's repeated exploit history (2021) and custody of real native assets mean the market applies a persistent **risk discount** versus non-custodial AMMs that hold only one chain's assets.
- **Mid-cap liquidity ceiling.** ~$6M daily volume caps realistic position size and makes RUNE prone to violent moves on protocol news.

## Peer Comparison

| Protocol | Category | Model | Custody of native assets? | Notes |
|---|---|---|---|---|
| **THORChain (RUNE)** | Cross-chain DEX | Native-asset AMM, RUNE-paired pools | Yes (node-bonded vaults / TSS) | ~10 chains; no wrapping; deep BTC↔ETH swaps |
| [[chainflip]] (FLIP) | Cross-chain DEX | JIT AMM, validator vaults | Yes | Direct competitor; native swaps via threshold sig |
| Across / Stargate | Bridge / messaging | Liquidity-network bridge | Wrapped/canonical | Faster but bridges representations, not native swaps |
| [[uniswap]] (UNI) | Single-chain DEX | Constant-product AMM | No | Deeper liquidity but no native cross-chain swaps |
| Maya Protocol | Cross-chain DEX | THORChain fork (CACAO) | Yes | Sister protocol; shares architecture |

THORChain's distinctive position is **native-asset, no-wrap cross-chain swaps**; the trade-off is the operational and custody complexity that pure single-chain AMMs avoid.

## Notable History

- **2019** — RUNE all-time low near **$0.0085** (2019-09-28) shortly after launch.
- **2021 (May)** — All-time high near **$20.87** during the DeFi/altcoin bull run.
- **2021 (Jul)** — Suffers **two major exploits** within weeks (totaling ~$8M+ across incidents), exposing the risk of holding native assets in node-controlled vaults; protocol pauses and patches.
- **2022-2024** — Recovers operationally, expands supported chains, and grows swap volume; introduces lending and savers products (some later wound down for risk reasons).
- **2026 (Jun)** — Trades around **$0.40** (rank ~#220), ~98% below ATH, roughly flat over 24h/7d on thin (~$6.3M) volume in an "Established Bear Market" with extreme-fear sentiment (Fear & Greed 23).

## Risks

- **Custody / smart-contract risk** — THORChain holds **real native assets** in node-managed vaults; it has a documented history of multimillion-dollar exploits, making security the central risk.
- **Complex incentive design** — the bond/pool "pendulum" and deterministic-value model are intricate; mispriced incentives or under-bonding can threaten network security.
- **Thin liquidity** — low spot volume ($4.3M/24h) means large swaps/exits face slippage, and the token is sensitive to forced selling.
- **Bear-market beta** — mid-cap DeFi infrastructure token; underperforms in extreme-fear regimes.
- **Regulatory** — non-custodial cross-chain swaps of native assets sit in an unsettled regulatory area (potential money-transmission / sanctions-screening scrutiny).

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[bitcoin]]
- [[ethereum]]
- [[decentralized-exchange]]
- [[cross-chain-bridges]]
- [[cross-chain-arbitrage]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original snapshot
- Market data as of 2026-06-20: `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko snapshot); market backdrop (Fear & Greed 23, "Established Bear Market") from `raw/data/crypto-loop/_digest.md`.
