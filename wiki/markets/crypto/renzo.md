---
title: "Renzo"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["REZ", "ezETH", "Renzo Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.renzoprotocol.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[eigenlayer]]", "[[restaking]]", "[[liquid-restaking]]", "[[liquid-staking]]", "[[depeg]]", "[[smart-contract-risk]]", "[[slashing]]", "[[governance-token]]", "[[defi]]"]
---

# Renzo

**Renzo** (REZ) is a liquid [[restaking]] protocol built on top of [[eigenlayer]]. Users deposit ETH or ETH liquid-staking tokens and receive **ezETH**, a [[liquid-restaking]] token (LRT) that represents a position which is staked on [[ethereum]] *and* simultaneously restaked through EigenLayer to secure additional services (Actively Validated Services, or AVSs). Renzo abstracts away the complexity of choosing operators and AVSs, aiming to deliver staking yield plus restaking rewards in a single composable token.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, REZ trades at **$0.0032749**, ranked **#673** by market capitalization with a market cap of **$28,205,788** (24h -0.84%, 7d -1.81%). REZ has been one of the steadier movers in the cohort over the week, though it remains roughly 99% below its 2024 listing-era high amid the broader bear regime (BTC ~$64,508; Fear & Greed Index 21, "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | REZ |
| **Market Cap Rank** | #673 |
| **Market Cap** | $28,205,788 |
| **Current Price** | $0.0032749 |
| **24h / 7d Change** | -0.84% / -1.81% |
| **Categories** | Decentralized Finance (DeFi), Binance Launchpool, Ethereum Ecosystem, Base Ecosystem, Restaking, YZi Labs (Prev. Binance Labs) Portfolio, OKX Ventures Portfolio |
| **Website** | [https://www.renzoprotocol.com/](https://www.renzoprotocol.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Renzo is a liquid [[restaking]] platform offering staking, restaking, and yield strategies across crypto ecosystems. Its core product is the **ezETH** liquid-restaking token, which packages base Ethereum staking yield with EigenLayer restaking rewards into one transferable, DeFi-composable asset. By abstracting protocol-level complexity — operator selection, AVS delegation, reward accounting — Renzo lets both retail and institutional users access restaking yield without managing the underlying [[eigenlayer]] mechanics themselves.

The protocol presents a modular system spanning vaults, a staking/restaking suite, and enterprise tooling, each intended to maximize capital efficiency while keeping execution verifiable on-chain. Renzo grew rapidly during the 2024 restaking narrative and was an early, large LRT issuer on EigenLayer; the REZ token launched via Binance Launchpool in 2024.

---

## How Renzo Works

**The restaking stack:**

1. A user deposits ETH (or an LST such as stETH/wBETH) into Renzo.
2. The underlying ETH is staked on [[ethereum]] (directly or via existing [[liquid-staking]] tokens), earning base consensus + execution rewards.
3. That staked position is then **restaked** through [[eigenlayer]], where it is delegated to node operators who use the economic security to validate Actively Validated Services (AVSs) in exchange for additional rewards. See [[restaking]] for the general concept.
4. The user holds **ezETH**, a reward-bearing [[liquid-restaking]] token whose value reflects accumulated staking + restaking rewards. ezETH remains liquid and usable across DeFi (lending, LPs, leverage).

**What the REZ token does:**

- **Governance** — REZ is the protocol's governance token, used to vote on parameters, operator/AVS strategy, treasury, and risk settings.
- REZ is *distinct* from ezETH: ezETH is the yield-bearing restaking asset that carries user funds; REZ is the governance/coordination token. Confusing the two is a common error — REZ does not itself accrue staking yield.

**How yield is generated:** ezETH yield is the sum of (a) ordinary Ethereum staking rewards and (b) EigenLayer restaking rewards / AVS fees, minus protocol and operator fees. Restaking rewards depend on AVS adoption and fee generation, which are still maturing — so the *additional* restaking yield over plain staking can be modest and variable.

### Worked illustration: where ezETH yield comes from

Suppose ordinary Ethereum [[liquid-staking]] returns ~3.0% APR. A restaker hopes EigenLayer AVS rewards add another layer on top — but in practice, while AVS fee markets are immature, that increment may be only a fraction of a percent in actual cash yield (historically much of the "reward" arrived as points/airdrop expectations rather than realized fees). So an ezETH holder might earn ~3.0% base plus a small, variable AVS premium, *minus* Renzo's protocol fee and operator fees. The headline pitch — "staking yield plus restaking yield" — is real in structure but the second layer has frequently underdelivered in hard yield, which is central to the LRT investment debate. Importantly, ezETH's value can *also* fall if restaked positions are [[slashing|slashed]], so the holder is taking on more downside, not just more upside.

---

## Competitive Position

Renzo was one of the largest liquid-restaking token (LRT) issuers to emerge during the 2024 [[eigenlayer|EigenLayer]] restaking boom, competing primarily with other LRT protocols rather than with plain [[liquid-staking]] providers.

| Protocol | LRT | Base layer | Notable trait |
|---|---|---|---|
| **Renzo** | ezETH | [[eigenlayer\|EigenLayer]] (+ Symbiotic/others over time) | Binance Launchpool launch; large early TVL; April 2024 depeg |
| ether.fi | eETH / weETH | EigenLayer | Largest LRT by TVL; "DeFi neobank" expansion |
| Kelp DAO | rsETH | EigenLayer | Multi-LST inputs |
| Puffer Finance | pufETH | EigenLayer | Anti-slashing "Secure-Signer" tech; native restaking |
| Swell | rswETH | EigenLayer / own L2 | Integrated with Swellchain |

Renzo's edge was distribution (the Binance relationship and aggressive points campaigns drove rapid TVL growth); its disadvantages are the reputational scar of the April 2024 ezETH depeg and the generic LRT problem that the *extra* restaking yield has been thin relative to the *extra* risk being assumed.

---

## Governance

REZ is Renzo's [[governance-token]]. It is used to vote on protocol parameters, operator and AVS allocation strategy, fee settings, and treasury matters through Renzo governance. The token launched via **Binance Launchpool** in April 2024 with a 10 billion max supply, of which a large share was allocated to community/airdrop, investors, and the foundation/team subject to vesting — leaving meaningful unlock overhang (market-cap/FDV ≈ 0.83). As with most LRT governance tokens, REZ does **not** itself bear staking yield (that is ezETH); its value depends on the protocol's TVL, fee capture, and the DAO's willingness to route value to the token. A persistent investor critique of the whole LRT cohort is that governance-token value has decoupled from the (large) restaked TVL the protocols control.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 8.19B REZ |
| **Total Supply** | 9.81B REZ |
| **Max Supply** | 10.00B REZ |
| **Fully Diluted Valuation** | $35.17M |
| **Market Cap / FDV Ratio** | 0.83 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2782 (2024-04-30) |
| **Current vs ATH** | -98.71% |
| **All-Time Low** | $0.00265163 (2026-02-28) |
| **Current vs ATL** | +35.52% |
| **24h Change** | +0.23% |
| **7d Change** | +4.95% |
| **30d Change** | +10.74% |
| **1y Change** | -73.98% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3b50805453023a91a8bf641e279401a0b23fa6f9` |
| Base | `0xf757c9804cf2ee8d8ed64e0a8936293fe43a7252` |
| Solana | `3DK98MXPz8TRuim7rfQnebSLpA7VSoc79Bgiee1m4Zw5` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | REZ/USDT | N/A |
| Kraken | REZ/USD | N/A |
| Bitget | REZ/USDT | N/A |
| KuCoin | REZ/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | REZ-PERP | Perpetual |
| Orca | 3DK98MXPZ8TRUIM7RFQNEBSLPA7VSOC79BGIEE1M4ZW5/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.renzoprotocol.com/](https://www.renzoprotocol.com/) |
| **Twitter** | [@RenzoProtocol](https://twitter.com/RenzoProtocol) |
| **Telegram** | [RenzoProtocolChat](https://t.me/RenzoProtocolChat) (6,510 members) |
| **Discord** | [https://discord.gg/renzoprotocol](https://discord.gg/renzoprotocol) |
| **GitHub** | [https://github.com/Renzo-Protocol](https://github.com/Renzo-Protocol) |
| **Whitepaper** | [https://docs.renzoprotocol.com/docs/](https://docs.renzoprotocol.com/docs/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Market Cap Rank** | #673 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-06-22 |

---

## Risks

- **ezETH [[depeg]] risk** — This is the headline risk for any LRT and has materialised for Renzo before. In April 2024, ezETH temporarily lost its peg in secondary markets around the REZ airdrop/listing as some holders rushed to exit; thin on-chain liquidity caused a sharp, brief depeg that liquidated leveraged ezETH positions on lending markets. The episode is a textbook illustration of LRT liquidity/[[depeg]] fragility.
- **Layered [[smart-contract-risk]]** — Funds pass through Renzo contracts *and* [[eigenlayer]] contracts *and* (often) an underlying [[liquid-staking]] protocol. A bug in any layer endangers deposits; restaking stacks risk on top of staking risk.
- **[[restaking]] / [[slashing]] risk** — Restaked ETH secures multiple AVSs. New, more aggressive slashing conditions introduced as EigenLayer matures mean restaked capital can be penalised for operator misbehavior across services — a correlated, still-evolving tail risk.
- **AVS reward uncertainty** — The restaking yield premium depends on AVS demand and fees that remain immature; promised "extra" yield may underdeliver.
- **Concentration / governance** — Large LRT issuers concentrate Ethereum economic security and operator selection; governance and operator-set decisions carry systemic weight.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Notable Events

- **2023–early 2024** — Renzo launches as a liquid-restaking protocol on [[eigenlayer|EigenLayer]], issuing **ezETH**. It rides the explosive 2024 restaking narrative, accumulating large TVL on the back of EigenLayer points and its own "ezPoints" campaign.
- **24 April 2024 — REZ Binance Launchpool / airdrop and the ezETH depeg.** REZ launched via Binance Launchpool. Around the same window, controversy over the airdrop allocation combined with rushes to exit ezETH and **thin secondary on-chain liquidity** caused **ezETH to briefly depeg sharply** (on some DEXs it traded far below its ETH backing for a short period). Because ezETH was used as leveraged collateral on lending markets, the flash depeg triggered cascading liquidations of leveraged positions before the price recovered. The underlying ETH backing was never lost — this was a *liquidity/secondary-market* depeg, not an insolvency — but it became the canonical case study in LRT fragility. Renzo subsequently adjusted airdrop parameters in response to community backlash.
- **2024–2025** — Renzo expands multi-chain (Base, others), pursues additional restaking layers/AVS integrations, and broadens its product suite (vaults, enterprise tooling), while the broad LRT-yield thesis cools as AVS fee generation lags expectations.
- **2025–2026** — REZ trades ~99% below its listing-era high amid the wider altcoin/restaking drawdown; the protocol's relevance now hinges on sustained restaking demand and real AVS fee capture rather than points-driven TVL.

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[eigenlayer]]
- [[restaking]]
- [[liquid-restaking]]
- [[liquid-staking]]
- [[slashing]]
- [[smart-contract-risk]]
- [[governance-token]]
- [[defi]]
- [[depeg]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical market-data snapshot
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko)
- General market knowledge (publicly documented Renzo/ezETH mechanism, the April 2024 Binance Launchpool launch and ezETH depeg event); no specific narrative wiki source ingested yet for protocol mechanism.
