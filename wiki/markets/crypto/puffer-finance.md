---
title: "Puffer Finance"
type: entity
created: 2026-04-10
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, lrt, lst, restaking, staking]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://www.puffer.fi"
aliases: ["PUFFER", "Puffer", "Puffer Finance", "Puffer-Finance", "pufETH"]
related: ["[[crypto-markets]]", "[[eigenlayer]]", "[[ethereum]]", "[[etherfi]]", "[[liquid-staking]]", "[[restaking]]"]
---

**Puffer Finance** (governance token **PUFFER**; flagship LRT **pufETH**) is a decentralized, native liquid [[restaking]] protocol on [[ethereum|Ethereum]] built on top of [[eigenlayer|EigenLayer]]. Its flagship token, **pufETH**, is a **liquid restaking token (LRT)** representing staked ETH that is also restaked through EigenLayer to earn additional rewards. Puffer's core differentiator is **anti-slashing technology** that lets it lower the collateral barrier for solo node operators, positioning the protocol as a decentralization-first alternative to LRT competitors like [[etherfi|EtherFi]] and [[renzo|Renzo]].

---

## Market Data

> *Puffer (PUFFER) is **outside the CoinGecko top 1000** in the 2026-06-21 snapshot, so no fresh authoritative market block is available. The protocol is verified and active; treat any cached price figures below as **stale** and confirm on CoinGecko / a live tracker before use.*

> *Market data unavailable as of 2026-06-21 (cryptodataapi.com / CoinGecko top-1000) — PUFFER not present in snapshot.*

| Field | Value |
|---|---|
| **Governance token** | PUFFER |
| **LRT** | pufETH (price tracks underlying ETH, less any liquidity discount) |
| **Chain** | [[ethereum\|Ethereum]] |
| **CoinGecko top-1000 status (2026-06-21)** | Not listed — outside top 1000 |
| **Macro backdrop** | [[fear-and-greed-index\|Fear & Greed]] = 23 ("Established Bear Market") |

Because PUFFER sits outside the top-1000 snapshot, its specific cap/price/volume cannot be refreshed from this loop's data. Qualitatively, low-float restaking governance tokens have been among the hardest-hit in the post-2024 LRT unwind, and the current extreme-fear regime pressures the entire restaking complex.

## Overview

Most [[liquid-staking]] and LRT protocols route deposits through a relatively small set of professional node operators. Puffer instead aims to onboard a long tail of **independent validators** without forcing each to lock the full **32 ETH** normally required to run an Ethereum validator. It achieves this by pairing **hardware-enforced signing safety** with on-chain economic backstops, so that the protocol — and pufETH holders — are protected even if an operator behaves badly.

## How Restaking Fits In

[[restaking|Restaking]] (pioneered by [[eigenlayer|EigenLayer]]) lets already-staked ETH be re-pledged to secure additional "Actively Validated Services" (AVSs) — oracles, bridges, data-availability layers — earning extra yield in exchange for taking on extra slashing conditions. A **liquid** restaking token like pufETH wraps that position so holders keep a tradable, [[defi|DeFi]]-composable asset while their ETH is busy securing both Ethereum and AVSs. The trade-off is **stacked slashing risk**: a fault can be penalized at the Ethereum layer and the AVS layer.

## Architecture

| Component | Function |
|-----------|----------|
| **Secure-Signer** | Hardware/enclave-based signing software that enforces Ethereum consensus rules and refuses to sign slashable messages (double-proposals, double-votes, surround votes), making slashing effectively unreachable at the software layer |
| **Slasher contract** | On-chain logic that penalizes operators if they somehow misbehave despite Secure-Signer |
| **Lower collateral / "NoOps"** | Solo restakers can participate with roughly **1–2 ETH** of their own bond instead of 32, with remaining collateral supplied from the pufETH deposit pool — pitched as an Ethereum decentralization mechanism |

By driving the per-validator bond well below 32 ETH, Puffer expands the pool of people who can run validators, which it frames as a counterweight to validator centralization among a few large staking providers.

## Products and Token

- **pufETH** — native LRT; accrues base [[staking]] rewards plus [[restaking]] rewards from [[eigenlayer|EigenLayer]] AVSs; designed to be used as collateral and liquidity across [[defi|DeFi]]. As a [[liquid-staking-derivative|liquid-staking/restaking derivative]], pufETH's market value tracks the ETH it represents plus accrued yield, less any secondary-market liquidity discount.
- **Points program** — used to bootstrap total value locked (TVL) ahead of the governance-token launch (the standard LRT go-to-market in the 2024 restaking wave).
- **PUFFER** — governance token coordinating AVS selection, fee parameters, and operator onboarding; the equity-like, speculative leg of the protocol (distinct from the ETH-pegged pufETH).
- **AVS partnerships** — Puffer integrates with EigenLayer's AVS ecosystem to route restaked ETH toward actively validated services.

## Tokenomics & Supply

Two distinct assets, two distinct token-economic profiles:

| Token | Peg / driver | Supply behaviour |
|---|---|---|
| **pufETH** | ~1:1 to ETH + restaking yield | Mint/burn against deposits; supply scales with TVL; aims to trade near ETH value |
| **PUFFER** | Governance/speculative | Fixed-cap governance token with team/investor/community allocations and vesting; subject to **unlock overhang** typical of 2024-era LRT launches |

The key dilution flag for **PUFFER specifically** is the standard LRT pattern: large insider/community allocations that vest over time, so circulating market cap can sit well below fully-diluted valuation, and emission/unlocks add structural sell pressure during a bear market. (Exact circulating/FDV figures are not in the 2026-06-21 top-1000 snapshot — verify on a live tracker.)

## Market Structure & Derivatives

- **pufETH liquidity** is concentrated in on-chain [[defi|DeFi]] pools (DEX LP, lending-market collateral) on [[ethereum|Ethereum]]; depth and the ETH discount/premium are the metrics that matter, mirroring the [[lido-finance|stETH]] discount dynamics seen in past deleveragings.
- **PUFFER** trades on CEX/DEX venues as a small-cap governance token; with the asset outside the top-1000 snapshot, spot liquidity is thin and slippage on size is a real risk.
- **Derivatives** — no deep, reliable perpetual-futures market is recorded for PUFFER on file; funding/open-interest are not stable data points. Treat exposure as primarily spot/on-chain.

## Narrative & Category

Puffer sits in the **liquid restaking ([[restaking|LRT]]) + Ethereum decentralization** narrative — the [[eigenlayer|EigenLayer]]-driven thesis that staked ETH can be re-pledged to secure additional services for extra yield. Within that crowded category, Puffer's specific pitch is **credibly-neutral, decentralization-first restaking**: anti-slashing hardware plus low-collateral solo operators as a counterweight to validator centralization, rather than the consumer-product breadth of EtherFi or the multi-chain land-grab of Renzo.

## Valuation Framing (qualitative)

- **Separate the two assets.** pufETH should be valued ≈ ETH (plus accrued yield, minus liquidity discount); the governance token PUFFER is the speculative leg whose value depends on protocol fee capture and restaking TVL.
- **TVL is the anchor.** For PUFFER, the relevant lens is restaking TVL and fee/AVS-reward capture versus fully-diluted valuation; LRT governance tokens generally trade on a TVL multiple plus narrative premium.
- **Post-unwind regime.** The 2024 restaking-points mania drove LRT TVL and token valuations to a peak that has since deflated; Puffer falling out of the top-1000 is consistent with the broad LRT de-rating. With [[fear-and-greed-index|Fear & Greed]] at 23, the category is at a sentiment trough.
- **Dilution discount.** Any "cheap" circulating-cap read must be checked against FDV given vesting unlocks.

## Peer Comparison

| Protocol | Token / LRT | Approx. positioning | Edge |
|---|---|---|---|
| **Puffer** | PUFFER / pufETH | Decentralization-first restaking | Anti-slashing (Secure-Signer), low-collateral solo operators |
| [[etherfi\|EtherFi]] | ETHFI / eETH | Largest LRT, consumer products | TVL scale, cash card, vaults, ease of use |
| [[renzo\|Renzo]] | REZ / ezETH | Aggressive multi-chain growth | Cross-chain restaking distribution |
| [[lido-finance\|Lido]] | LDO / stETH | Liquid **staking** (not restaking) benchmark | Deepest LSD liquidity; the discount Puffer's pufETH is measured against |

Puffer is a **mid-tier LRT by TVL** differentiated on security/decentralization rather than scale or distribution.

## Positioning and Risks

Compared with [[etherfi|EtherFi]]'s emphasis on ease-of-use and product breadth (cash card, vaults) and [[renzo|Renzo]]'s aggressive multi-chain growth, Puffer leans into **validator security, anti-slashing, and permissionless solo-operator participation** as its narrative.

Key risks for holders and traders:
- **Smart-contract risk** across Puffer, EigenLayer, and any integrated AVS.
- **Stacked slashing risk** from restaking multiple services simultaneously.
- **De-peg risk**: pufETH can trade at a discount to underlying ETH during stress or liquidity crunches, mirroring the stETH discount seen in past crypto deleveragings.
- **Reward concentration / AVS counterparty risk** if restaked collateral is routed to immature services.
- **Token-specific dilution / liquidity** — PUFFER carries vesting-unlock overhang and, being outside the top-1000, has thin spot liquidity.
- **Regime risk** — the LRT category de-rated sharply after the 2024 points mania; an extreme-fear backdrop ([[fear-and-greed-index|Fear & Greed]] = 23) pressures restaking tokens hardest.

## Related

- [[restaking]] — the mechanism pufETH is built on
- [[eigenlayer]] — the restaking layer Puffer operates atop
- [[liquid-staking]] — the broader category pufETH extends
- [[ethereum]] — the base network
- [[etherfi]] · [[renzo]] · [[lido-finance]] — competing/benchmark staking protocols
- [[defi]] · [[fear-and-greed-index]]

## Sources

- General market knowledge; no specific wiki source ingested yet.
- CoinGecko top-1000 snapshot, 2026-06-21: PUFFER not present (outside top 1000) — market block could not be refreshed.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PUFFER |
| **Market Cap Rank** | #1380 |
| **Market Cap** | $6.69M |
| **Current Price** | $0.0132 |
| **Categories** | Smart Contract Platform, Layer 2 (L2), Restaking, Liquid Restaking Governance Tokens, Rollup, Liquid Staking, Binance Alpha Spotlight, Made in USA |
| **Website** | [https://www.puffer.fi/](https://www.puffer.fi/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 506.59M PUFFER |
| **Total Supply** | 1.00B PUFFER |
| **Max Supply** | 1.00B PUFFER |
| **Fully Diluted Valuation** | $13.20M |
| **Market Cap / FDV Ratio** | 0.51 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.9908 (2024-12-07) |
| **Current vs ATH** | -98.66% |
| **All-Time Low** | $0.0131 (2026-07-14) |
| **Current vs ATL** | +1.40% |
| **24h Change** | -3.10% |
| **7d Change** | -3.42% |
| **30d Change** | -40.38% |
| **1y Change** | -93.28% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x4d1c297d39c5c1277964d0e3f8aa901493664530` |
| Binance Smart Chain | `0x87d00066cf131ff54b72b134a217d5401e5392b6` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | PUFFER/USD | N/A |
| Upbit | PUFFER/BTC | N/A |
| Bitget | PUFFER/USDT | N/A |
| KuCoin | PUFFER/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X4D1C297D39C5C1277964D0E3F8AA901493664530/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.puffer.fi/](https://www.puffer.fi/) |
| **Twitter** | [@puffer_finance](https://twitter.com/puffer_finance) |
| **Telegram** | [puffer_fi](https://t.me/puffer_fi) (28,351 members) |
| **Discord** | [https://discord.com/invite/pufferfi](https://discord.com/invite/pufferfi) |
| **Whitepaper** | [https://docs.puffer.fi/](https://docs.puffer.fi/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.91M |
| **Market Cap Rank** | #1380 |
| **24h Range** | $0.0132 — $0.0139 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
