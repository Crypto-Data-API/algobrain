---
title: "KernelDAO"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, altcoins]
aliases: ["KERNEL", "Kernel DAO", "KernelDAO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://kerneldao.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[restaking]]", "[[bnb-chain]]"]
---

# KernelDAO

**KernelDAO** (KERNEL) is a multi-product [[restaking]] ecosystem, best known for the **Kernel** restaking protocol on [[bnb-chain]], the **Kelp** liquid restaking protocol (issuer of the rsETH liquid restaking token), and **Gain**, a suite of automated yield vaults. **KERNEL** is the ecosystem's governance and utility token spanning all three products. It ranks **#995** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* KERNEL trades at **$0.04833114**, market cap **$13,915,571**, **-2.55% (24h)** and **-4.41% (7d)** — drifting lower in a fearful market (BTC $64,508; Fear & Greed 21 / Extreme Fear).

---

## What KernelDAO Is

KernelDAO is a suite of restaking and yield products under one token and governance umbrella:

- **Kelp** — a [[liquid-restaking]] protocol. Users restake [[ethereum]] (and LSTs) and receive **rsETH**, a liquid restaking token that stays usable across DeFi while earning restaking rewards. Kelp has reported multi-billion-dollar TVL, hundreds of thousands of ETH restaked, deployment across 10+ L2s, and integrations with Aave, Pendle, Fluid and others.
- **Kernel (Infrastructure)** — the restaking layer on **BNB Chain**, extending shared security and restaking to BNB-based assets and middleware, aiming to be the economic-security backbone for that ecosystem.
- **Gain** — automated vault products (e.g. Airdrop Gain Vault, High Growth Vault) that package restaking and DeFi strategies into one-click yield positions.

The thesis is to build an interconnected ecosystem bridging security, liquidity and rewards across Ethereum and BNB Chain.

## Mechanism: Restaking

Restaking lets assets already securing a base chain (or liquid staking tokens representing them) be re-pledged to secure additional services — Actively Validated Services / middleware — earning extra rewards in exchange for additional slashing risk. Liquid restaking (Kelp/rsETH) tokenizes that position so capital stays productive elsewhere in DeFi. KernelDAO applies this model on both Ethereum (via Kelp) and BNB Chain (via Kernel). See [[restaking]] and [[liquid-restaking]] for the general mechanics and risks.

### Why the BNB-Chain angle matters

KernelDAO's most differentiated piece is **Kernel on [[bnb-chain]]**. EigenLayer pioneered restaking on Ethereum and a crowd of LRT issuers (EtherFi, Renzo, Puffer, Swell) fight over that base. KernelDAO is unusual in extending the *shared-security / restaking* primitive to BNB Chain — restaking BNB and BNB-ecosystem assets to provide economic security to middleware and Actively Validated Services there. That makes Kernel less a "me-too Ethereum LRT" and more an attempt to be the restaking economic-security layer for a second major ecosystem, where it has fewer direct rivals. The flip side is dependence on BNB-Chain activity and on the assumption that demand for restaked security materializes outside Ethereum.

### Three products, one token — how they connect

1. **Kelp** is the demand-generation front end on Ethereum: deposits flow in, rsETH is minted, and that liquid position seeds DeFi integrations (Aave/Pendle/Fluid) which in turn deepen rsETH liquidity.
2. **Kernel (infrastructure)** is the security layer that takes restaked capital and rents it out to services, primarily on BNB Chain.
3. **Gain** packages restaking + DeFi strategies into one-click vaults (Airdrop Gain Vault, High Growth Vault), abstracting complexity for retail.
KERNEL is the governance/coordination token threaded across all three; the design intent is that growth in TVL and integrations compounds across products. The persistent open question (see Risks) is how strongly that protocol-level value flows back to the token.

## Token Role

KERNEL is the unifying governance and incentive token across Kelp, Kernel and Gain. It is used for protocol governance, reward/incentive programs, and ecosystem coordination. Tokenomics carry a notable overhang: circulating supply is ~286M of a 1B max, so **MC/FDV ≈ 0.29** — roughly 70% of supply is not yet circulating, meaning future unlocks/emissions are a structural dilution risk. KERNEL is issued on Ethereum, BNB Chain and Arbitrum and is broadly listed (Binance, Kraken, Upbit, Bitget, KuCoin, Crypto.com).

## Competitive Position

KernelDAO/Kelp is a meaningful player in liquid restaking, competing with EtherFi, Renzo, Puffer and others on Ethereum, while Kernel's BNB Chain restaking is a more differentiated niche. Its strengths are real TVL, broad integrations and a multichain footprint; its weaknesses are restaking-sector crowding, fee compression, and a token whose ~$14M market cap is small relative to the TVL it helps coordinate — value accrual from TVL to the KERNEL token is indirect.

### Comparison vs Restaking / Liquid-Restaking Peers

| Project | Token | LRT / product | Primary chain(s) | Differentiator vs KernelDAO |
|---|---|---|---|---|
| **KernelDAO** | KERNEL | rsETH (Kelp) + Kernel infra + Gain vaults | Ethereum + **BNB Chain** + Arbitrum | Multi-product; restaking extended to BNB Chain |
| **EtherFi** | ETHFI | eETH (largest LRT) | Ethereum | Market-share leader on Ethereum, cash/credit-card products |
| **Renzo** | REZ | ezETH | Ethereum + L2s | Pure LRT, aggressive multichain ezETH distribution |
| **Puffer Finance** | PUFER | pufETH | Ethereum | Anti-slashing tech (Secure-Signer), validator-centric |
| **EigenLayer** | EIGEN | (the restaking base layer itself) | Ethereum | The protocol KelpDAO and peers build *on top of* |

Takeaway: on Ethereum, KernelDAO/Kelp is a credible but not dominant LRT (EtherFi leads). Its real edge is **breadth** — being one of the few to ship a working restaking stack on BNB Chain plus packaged Gain vaults — rather than out-competing EtherFi on raw eETH/rsETH scale.

---

## How & Where KERNEL Trades

- **Broad Tier-1 CEX coverage.** Unusually well-listed for a sub-$15M cap, reflecting its 2025 launch with major-exchange support: **Binance (KERNEL/USDT)**, **Kraken**, **Upbit (KRW)**, **Bitget**, **KuCoin**, and **Crypto.com**. The Upbit KRW pair adds Korean-retail sensitivity.
- **DEX liquidity.** Native on Ethereum, BNB Chain, and Arbitrum, with Uniswap V3 (ETH) the main on-chain venue. Multichain issuance spreads — and fragments — liquidity.
- **Derivatives.** KERNEL has perpetual markets on major derivatives venues; given the small float and large supply overhang (MC/FDV ≈ 0.29), it is prone to violent leverage-driven moves — note the 24h range can span >30%.
- **Trading implications** — Good listings mask a thin true float: heavy CEX coverage plus a low circulating-vs-FDV ratio makes KERNEL a high-beta restaking proxy that overshoots in both directions. Funding and unlock schedules matter more here than for fully-circulating tokens.

---

## Narrative, Category & Catalysts

- **Category** — **Restaking / liquid restaking** governance token, a 2024–2025 DeFi narrative built on EigenLayer and its LRT ecosystem.
- **Catalysts** — Restaking-sector TVL inflows and a risk-on rotation back into DeFi yield; new AVS/middleware demand (especially on BNB Chain) that actually pays for restaked security; rsETH integration growth; and token-utility upgrades that route more protocol value to KERNEL.
- **Structural headwind — unlocks.** With ~70% of max supply still to circulate, scheduled emissions/unlocks are a recurring overhang; unlock dates are typically the single biggest idiosyncratic risk event for tokens with MC/FDV near 0.29.
- **Headwind — regime.** In an Established Bear with Fear & Greed at **21**, restaking yields compress and speculative DeFi tokens de-rate; KERNEL trades well below its 2025 ATH and remains pinned near its lows.

---

## History & Timeline

Only dated, verifiable milestones are listed.

| Date | Event |
|---|---|
| 2025-04-14 | KERNEL all-time high of **$0.4732** shortly after its 2025 token launch / listing wave |
| 2026-02-06 | KERNEL all-time low of **$0.0467** during the deepening bear market |
| 2026-06-22 | Trades ~$0.0483, ~83% below ATH, drifting lower in Extreme Fear (BTC $64,508; F&G 21) |

---

## Risks

- **Restaking-specific risk** — layered slashing and smart-contract risk across the base chain plus every restaked service; a failure cascades.
- **Large supply overhang** — MC/FDV ≈ 0.29 means heavy future unlocks can dilute holders and pressure price.
- **Token-vs-TVL value gap** — strong protocol TVL does not automatically flow to the KERNEL token.
- **Sector crowding & yield compression** — many liquid restaking protocols compete for the same deposits, eroding fees.
- **High volatility / drawdown** — KERNEL is well below its 2025 ATH (~$0.47) and trades thinly enough to swing sharply (note its 24h range can span >30%).
- **Multichain/bridge surface** — operating across Ethereum, BNB Chain and Arbitrum adds bridge and contract attack surface.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | KERNEL |
| **Market Cap Rank** | #995 |
| **Market Cap** | $13,915,571 |
| **Current Price** | $0.04833114 |
| **24h / 7d Change** | -2.55% / -4.41% |
| **Categories** | Restaking, Liquid Restaking Governance Tokens, Decentralized Finance (DeFi), BNB Chain Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem |
| **Website** | [https://kerneldao.com/](https://kerneldao.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Kernel is a suite of restaking products - Kelp LRT, Kernel Infrastructure, and Gain

Kelp is a liquid restaking protocol with $2B+ in TVL, 500K ETH restaked, live on 10+ L2s and integrated across Aave, Pendle, Fluid, and many more key platforms. 

Gain is a vault product designed for users to maximize their earning potential - via different vaults like Airdrop Gain Vault, and High Growth Vault among others

Kernel aims to redefine the restaking and decentralized finance landscape by building an interconnected ecosystem that seamlessly bridges security, liquidity, and rewards. By empowering stakers, developers, and protocols, Kernel strives to be the backbone of decentralized economic security on the BNB Chain and beyond

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 286.31M KERNEL |
| **Total Supply** | 1.00B KERNEL |
| **Max Supply** | 1.00B KERNEL |
| **Fully Diluted Valuation** | $81.84M |
| **Market Cap / FDV Ratio** | 0.29 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4732 (2025-04-14) |
| **Current vs ATH** | -82.73% |
| **All-Time Low** | $0.0467 (2026-02-06) |
| **Current vs ATL** | +75.02% |
| **24h Change** | -24.63% |
| **7d Change** | -26.27% |
| **30d Change** | -11.72% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3f80b1c54ae920be41a77f8b902259d48cf24ccf` |
| Binance Smart Chain | `0x9ecaf80c1303cca8791afbc0ad405c8a35e8d9f1` |
| Arbitrum One | `0x6e401189c8a68d05562c9bab7f674f910821eacf` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | KERNEL/USDT | N/A |
| Kraken | KERNEL/USD | N/A |
| Upbit | KERNEL/KRW | N/A |
| Bitget | KERNEL/USDT | N/A |
| KuCoin | KERNEL/USDT | N/A |
| Crypto.com Exchange | KERNEL/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X3F80B1C54AE920BE41A77F8B902259D48CF24CCF/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://kerneldao.com/](https://kerneldao.com/) |
| **Twitter** | [@kernel_dao](https://twitter.com/kernel_dao) |
| **Telegram** | [KelpDAOxyz](https://t.me/KelpDAOxyz) (26,992 members) |
| **Discord** | [https://discord.gg/khSpqCFvGq](https://discord.gg/khSpqCFvGq) |
| **GitHub** | [https://github.com/Kelp-DAO/kernel-smart-contracts-public](https://github.com/Kelp-DAO/kernel-smart-contracts-public) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 9 |
| **GitHub Forks** | 5 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $46.50M |
| **Market Cap Rank** | #986 |
| **24h Range** | $0.0810 — $0.1088 |
| **CoinGecko Sentiment** | 67% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Playbook (Bear / Extreme-Fear Regime)

> Educational framing only — not investment advice. KERNEL is a small-cap, high-overhang DeFi token.

- **Regime first.** In an Established Bear with Fear & Greed at 21, restaking yields compress and LRT governance tokens de-rate; the base case is range-bound-to-lower with sharp leverage-driven flushes.
- **Respect the unlock calendar.** The single most important idiosyncratic risk is supply: MC/FDV ≈ 0.29 means future unlocks can swamp organic demand. Map unlock dates before sizing; selling pressure tends to front-run them.
- **It's a high-beta restaking proxy.** KERNEL amplifies the restaking-sector beat — it rallies hard on DeFi risk-on and bleeds on risk-off. Pair-trade thinking (KERNEL vs ETHFI/REZ) can isolate the BNB-Chain-restaking thesis from generic sector beta.
- **Liquidity vs float.** Good CEX listings but a thin true float and active perps make it prone to overshoot; use limit orders and modest size, and watch funding for crowded-leverage signals.
- **Invalidation / risk control.** Watch the 2026-02 ATL ($0.0467) as structural support; a decisive break on volume signals continuation lower. Thesis improves only with a DeFi/restaking risk-on rotation plus evidence that real AVS demand (especially on BNB Chain) is paying for restaked security.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[restaking]]
- [[liquid-restaking]]
- [[bnb-chain]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.
