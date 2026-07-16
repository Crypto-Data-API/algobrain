---
title: "BOB (Build on Bitcoin)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, bitcoin, crypto, defi, ethereum]
aliases: ["BOB"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.gobob.xyz"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[data-availability]]", "[[ethereum]]", "[[layer-2]]", "[[optimism]]", "[[optimistic-rollup]]", "[[sequencer]]"]
---

# BOB (Build on Bitcoin)

**BOB ("Build on Bitcoin")** (BOB) is a **hybrid [[bitcoin|Bitcoin]] / [[ethereum|Ethereum]] [[layer-2|Layer 2]]** built on the **[[optimism|OP Stack]]** (an [[optimistic-rollup|optimistic rollup]]) with deep Bitcoin integration, positioning itself as a gateway for "BTCFi" — bringing BTC into DeFi. **Key architectural clarification:** despite the "Build on Bitcoin" branding, BOB is an **[[optimistic-rollup]] that settles to [[ethereum]]** (not to Bitcoin); it integrates BTC via [[bitcoin]] bridging (BitVM-based research) and Bitcoin "intents." It aims to fuse Bitcoin's liquidity with Ethereum-rollup smart-contract versatility. As of 2026-06-22 BOB trades at **$0.00535638**, ranked **#919** with a market capitalization of **~$16.2M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Crypto Fear & Greed Index: 21 (Extreme Fear).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BOB |
| **Market Cap Rank** | #919 |
| **Market Cap** | ~$16.18M |
| **Current Price** | $0.00535638 |
| **24h Change** | -0.33% |
| **7d Change** | -8.19% |
| **Architecture** | OP-Stack optimistic rollup settling to **Ethereum** + Bitcoin bridging (BitVM research) |
| **Categories** | Smart Contract Platform, Decentralized Finance (DeFi), Ethereum Ecosystem, Layer 2 (L2), Bitcoin Sidechains, BOB Network Ecosystem |
| **Website** | [https://www.gobob.xyz](https://www.gobob.xyz) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Crypto Fear & Greed Index: 21 (Extreme Fear).*

---

## Overview

BOB is a **hybrid [[layer-2|Layer 2]]**. Its execution and settlement layer is built on the **[[optimism|OP Stack]]**, making it an [[optimistic-rollup|optimistic rollup]] that posts data to [[ethereum|Ethereum]] [[layer-1|L1]] for [[data-availability|data availability]] and inherits Ethereum-rollup security (fraud-proof challenge windows, centralized [[sequencer|sequencer]] today). On top of this it layers **Bitcoin integration** so that BTC can be used natively in DeFi:

- **BitVM-based bridging** — BOB has been associated with BitVM/BitVM2 research, an approach aimed at more trust-minimized BTC bridging than traditional federated multisigs.
- **BOB Gateway / Bitcoin intents** — one-click flows to move BTC into assets or DeFi positions across many chains (using intents and cross-chain messaging such as LayerZero).
- **BTC vaults** — packaged, curated tokenized-BTC yield strategies.

The marketing framing ("Bank of Bitcoin", "BTCFi gateway") describes product ambition; the underlying chain is an Ethereum-settled OP-Stack rollup with Bitcoin bridges, not a rollup that settles to Bitcoin.

### Where BOB actually settles (the key distinction)

This is the most commonly misunderstood point about BOB. Many "Bitcoin L2s" (e.g. [[merlin-chain]]) are federated [[sidechain|sidechains]] that bridge BTC and claim Bitcoin alignment. **BOB takes a different path:** it is a standard OP-Stack [[optimistic-rollup]] whose **settlement and [[data-availability]] go to [[ethereum]]**, inheriting Ethereum-rollup security (fraud proofs, L1-posted data) — and *separately* bridges BTC in for DeFi. So BOB's base security is Ethereum's, not Bitcoin's; the "Bitcoin" in the name refers to the asset/ecosystem it serves, not the chain it settles to. This is arguably a more honest and more battle-tested security base than federated BTC sidechains, but it does mean BOB is not "secured by Bitcoin."

### Rollup stack

| Layer | BOB approach |
|---|---|
| **Settlement** | **[[ethereum]] L1** (OP Stack) — fraud-proof/dispute resolution and state commitments on Ethereum; ~7-day withdrawal window |
| **Data availability** | [[ethereum]] (blobs, post-[[eip-4844\|EIP-4844]]) for [[data-availability]] |
| **Execution** | EVM-compatible OP-Stack execution |
| **Sequencing** | **Centralized [[sequencer]]** (OP-Stack default) pending decentralization |
| **BTC integration** | BitVM/BitVM2-based bridging research + BOB Gateway / Bitcoin intents (cross-chain messaging, e.g. LayerZero) |
| **Gas token** | **ETH** (BOB is governance/incentive only) |

### BitVM and trust-minimized BTC bridging

BOB has been associated with **BitVM / BitVM2** research — a scheme for executing arbitrary computation verifiable on Bitcoin via fraud proofs and pre-signed transactions, aimed at building BTC bridges that are far less trust-dependent than the multisig/federated bridges used by sidechains like [[merlin-chain]]. BitVM is cutting-edge and still maturing; in practice today BTC integration still leans on bridges/cross-chain pathways that add attack surface, but the research direction distinguishes BOB's ambition from pure federated pegs.

---

## Comparison vs Bitcoin-aligned and Ethereum L2 peers

| Network | Settles to | Proof system | BTC bridge | Trust base |
|---|---|---|---|---|
| **BOB** | **[[ethereum]]** | [[optimistic-rollup\|Optimistic]] (OP Stack) | BitVM-style + cross-chain | **Ethereum-rollup** security + bridge risk |
| [[merlin-chain\|Merlin]] | Off-chain (not BTC-verified) | ZK-branded sidechain | Multisig/federated | Federated [[sidechain]] |
| [[optimism\|Optimism]] | [[ethereum]] | Optimistic (OP Stack) | n/a | Ethereum-rollup |
| [[base\|Base]] | [[ethereum]] | Optimistic (OP Stack) | n/a | Ethereum-rollup |
| Stacks (STX) | Bitcoin (PoX) | own consensus | sBTC | BTC-anchored own chain |

BOB's nearest *technical* relatives are other OP-Stack rollups ([[optimism]], [[base]], [[blast]]) — same settlement, DA, and centralized-sequencer profile — while its *thematic* relatives are BTCFi networks like [[merlin-chain]]. Understanding which group it actually belongs to (the OP-Stack rollups) is essential to assessing its risk.

---

## Token & What It Does

The **BOB** token (contracts on [[ethereum|Ethereum]], BNB Chain, and the BOB network) is the network's governance and ecosystem-incentive asset. Gas on the BOB chain is paid in ETH (OP-Stack default), so BOB functions as a governance/incentive token rather than the gas token. Total / max supply is 10B BOB with roughly 2.8B circulating, giving a low market-cap-to-FDV ratio (~0.28) and a significant future-unlock overhang.

---

## History

BOB launched its mainnet in 2024 as part of the BTCFi wave, distinguishing itself from pure "Bitcoin L2" sidechains by building on the OP Stack and emphasizing trust-minimized BTC bridging research (BitVM/BitVM2). The BOB token generation and distribution followed. Price action has been volatile and, like peers, sits well below its 2024-era highs in the current bear regime.

### Timeline

- **2024** — BOB mainnet launches on the [[optimism|OP Stack]] (settling to [[ethereum]]) during the BTCFi wave, positioning as a "BTCFi gateway" with BitVM-based BTC-bridging research.
- **2024-2025** — Rolls out BOB Gateway / Bitcoin intents (one-click BTC-into-DeFi flows) and curated **BTC vaults** (tokenized-BTC yield strategies).
- **2025-12** — All-time high ~$0.0293 (2025-12-04), notably later than the mid-2024 peaks of [[blast]]/[[taiko]]/[[merlin-chain]] (BOB's token distribution came later in the cycle).
- **2026-02** — All-time low $0.00506725 (2026-02-22).
- **2026** — Trading $0.00535638 as of 2026-06-22; down 8.19% on the week amid Extreme Fear (F&G 21).

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

### Governance

BOB is the network's governance and ecosystem-incentive token, deployed across [[ethereum]], BNB Chain, and the BOB network. Gas on the BOB chain is paid in ETH (OP-Stack default), so BOB is not the gas token; its role is governance over protocol parameters and direction of ecosystem incentives. As with the other OP-Stack L2 tokens, a large unvested allocation means circulating float and governance weight evolve with the unlock schedule.

---

## Risks

- **Bridge / peg risk** — BTC integration depends on bridging; even BitVM-style bridges are new and complex, and any cross-chain/LayerZero pathway adds attack surface. Bridge failure is the dominant risk for any BTC-DeFi product.
- **Sequencer centralization** — as an OP-Stack rollup, BOB runs a centralized [[sequencer]] today (single point of ordering/censorship) pending decentralized sequencing.
- **Rollup security assumptions** — optimistic-rollup safety depends on honest fraud-proof submission within the challenge window and on Ethereum data availability.
- **DeFi / vault risk** — curated BTC vaults and lending carry smart-contract, curator, and custodial counterparty risk on top of base-chain risk.
- **Token overhang & decay** — large unvested supply and post-distribution selling pressure are persistent headwinds.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.82B BOB |
| **Total Supply** | 10.00B BOB |
| **Max Supply** | 10.00B BOB |
| **Fully Diluted Valuation** | $74.09M |
| **Market Cap / FDV Ratio** | 0.28 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0293 (2025-12-04) |
| **Current vs ATH** | -74.72% |
| **All-Time Low** | $0.00506725 (2026-02-22) |
| **Current vs ATL** | +46.14% |
| **24h Change** | +5.30% |
| **7d Change** | +40.45% |
| **30d Change** | +20.35% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc9746f73cc33a36c2cd55b8aefd732586946cedd` |
| Binance Smart Chain | `0x52b5fb4b0f6572b8c44d0251cc224513ac5eb7e7` |
| Bob Network | `0xb0bd54846a92b214c04a63b26ad7dc5e19a60808` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | BOB/USD | N/A |
| KuCoin | BOB/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.gobob.xyz](https://www.gobob.xyz) |
| **Twitter** | [@build_on_bob](https://twitter.com/build_on_bob) |
| **Telegram** | [gobobxyz](https://t.me/gobobxyz) (19,697 members) |
| **Discord** | [https://discord.com/invite/gobob](https://discord.com/invite/gobob) |
| **GitHub** | [https://github.com/bob-collective](https://github.com/bob-collective) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.14M (2026-04-09 snapshot) |
| **Market Cap Rank** | #919 |
| **Price (2026-06-22)** | $0.00535638 |
| **24h Change (2026-06-22)** | -0.33% |
| **7d Change (2026-06-22)** | -8.19% |
| **24h Range (2026-04-09 snapshot)** | $0.00703299 — $0.00762221 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-06-22 |

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
- [[bitcoin]]
- [[layer-2]]
- [[optimistic-rollup]]
- [[optimism]]
- [[sequencer]]
- [[data-availability]]
- [[merlin-chain]]
- [[base]]
- [[blast]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko (Crypto Fear & Greed Index: 21, Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet for architecture/history claims.
