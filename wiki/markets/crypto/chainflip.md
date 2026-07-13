---
title: "Chainflip"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi]
aliases: ["FLIP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://chainflip.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[cross-chain-bridge]]", "[[bitcoin]]", "[[slashing]]", "[[smart-contract-risk]]"]
---

# Chainflip

**Chainflip** (FLIP) is a decentralised, native [[cross-chain-bridge]] and cross-chain DEX. It lets users swap assets between major blockchains — including non-smart-contract chains like [[bitcoin]] — without wrapped tokens or traditional lock-and-mint bridging. Chainflip is its own application-specific blockchain (a Substrate-based state chain) whose ~150 validators collectively control multi-party **threshold-signature (TSS) vaults** on each connected chain; swaps are priced by a novel **Just-In-Time (JIT) AMM**. FLIP is the network's staking, security, and utility token.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, FLIP trades at **$0.295999**, ranked **#699** by market capitalization with a market cap of **~$26,382,199** (24h +3.29%, 7d +0.12%) — a rare green print in this cohort against an otherwise weak tape. The token is roughly 97% below its 2024 all-time high, consistent with the broader bear regime (BTC ~$64,390; Fear & Greed Index 21 — "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FLIP |
| **Market Cap Rank** | #699 |
| **Market Cap** | ~$26,382,199 |
| **Current Price** | $0.295999 |
| **24h / 7d Change** | +3.29% / +0.12% |
| **Categories** | Decentralized Finance (DeFi), Ethereum Ecosystem, Bridge Governance Tokens, Coinbase Ventures Portfolio, Pantera Capital Portfolio, Delphi Ventures Portfolio, Blockchain Capital Portfolio, CoinList Launchpad |
| **Website** | [https://chainflip.io/](https://chainflip.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Chainflip is a decentralised protocol for swapping cryptocurrency assets across blockchains without users losing custody mid-flight and without wrapped tokens or conventional bridging. It is fully generalised — it can integrate any chain and transaction type — and prices swaps with its **Just-In-Time (JIT) AMM**, where market makers provide liquidity precisely at the moment of execution to deliver tight pricing. The protocol is secured by a set of ~150 validators that stake the native **FLIP** token.

FLIP is primarily a utility/security token: validators must bond FLIP to participate and are rewarded in FLIP, with value returned indirectly through protocol fees. Additionally, swaps drive automatic buying and burning of FLIP via the liquidity-pool system, applying deflationary pressure as trading volume grows. See [[cross-chain-bridge]] for the general design space and [[bitcoin]]/[[ethereum]] for two of the chains Chainflip natively connects.

---

## How Chainflip Works

**Native cross-chain swaps via threshold-signature vaults:**

1. Chainflip runs its own **State Chain** (a Substrate-based blockchain) that coordinates the protocol. A set of ~150 validators is elected by FLIP stake.
2. On each connected external chain (Bitcoin, Ethereum, Solana, etc.), assets are held in **vaults controlled by threshold signatures (TSS)**. No single validator holds the keys; control is split across the active validator set via multi-party computation, so a swap never requires trusting one custodian or minting a wrapped asset.
3. A user deposits asset A on its native chain; the State Chain witnesses the deposit, the **JIT AMM** prices the swap (market makers quote just-in-time liquidity), and the validator set authorises a TSS-signed payout of asset B from the destination-chain vault to the user.
4. Validators rotate periodically; key shares are re-shared to the new set ("key rotation"), and misbehaving validators can be [[slashing|slashed]] — losing bonded FLIP — to enforce honest operation.

**Trust model:** Chainflip is effectively a *decentralised-custody* bridge. Security depends on (a) the honesty of the bonded validator supermajority controlling the TSS vaults and (b) the soundness of the MPC/threshold-signature scheme and key-rotation process. This is a different trust model from optimistic bridges like [[across-protocol]] or messaging bridges like [[stargate-finance]]/[[layerzero]] — but it shares the bridge category's elevated risk.

**What the FLIP token does:**

- **Validator staking & security** — Validators must bond FLIP; the bonded stake is the economic security backing the vaults and is subject to [[slashing]].
- **Rewards & fees** — Validators (and liquidity providers) earn from protocol activity; FLIP rewards plus fee value flow to participants.
- **Deflationary burn** — A portion of swap activity buys and burns FLIP, linking token economics to real trading volume.
- **Governance** — FLIP holders participate in protocol governance decisions.

**How yield/value is generated:** Value accrues from genuine swap fees and the buy-and-burn mechanism, both tied to bridging/trading volume. Low volume (the page's historical snapshot showed very thin 24h volume) directly weakens the fee/burn flywheel.

---

## Architecture Deep Dive

Chainflip is unusual among [[cross-chain-bridge|bridges]] because it is a *purpose-built application-specific blockchain* rather than a contract suite layered on existing chains. The components:

- **The State Chain.** A Substrate-based proof-of-stake blockchain that is the brain of the protocol. It witnesses deposits on external chains, runs the auction that elects validators, coordinates the [[#JIT AMM and pricing|JIT AMM]], and authorises payouts. User assets never live on the State Chain — only the *coordination logic* does.
- **Threshold-signature (TSS) vaults.** On each connected external chain ([[bitcoin]], [[ethereum]], Solana, Polkadot/Assethub, Arbitrum, and others), funds sit in a vault whose signing key is split across the active validator set via **multi-party computation (MPC)**. No single party — and no fixed multisig — ever holds a complete key. A payout requires a threshold of validators to cooperatively sign, which is why a malicious *supermajority* (not just a single key) would be needed to steal vault funds.
- **Validator auction & bonding.** ~150 validators are selected through a periodic on-chain auction; they must bond FLIP to win a slot. The bonded stake is the economic security backing the vaults and is exposed to [[slashing]] for misbehaviour or downtime.
- **Key rotation / re-sharing.** When the validator set rotates, the vault keys are *re-shared* to the new set without ever reconstructing the full key on any one machine. This rotation is a critical and complex safety operation — a bug here is one of the protocol's principal risk surfaces.
- **Witnessing.** Validators independently observe deposits on external chains and reach consensus on the State Chain that a deposit occurred, triggering the swap. This replaces a trusted oracle/relayer with the validator set itself.

### JIT AMM and pricing

Chainflip's **Just-In-Time (JIT) AMM** is its defining DEX innovation. Instead of passive constant-product pools, professional market makers post **range orders** and update quotes *at the moment a swap is executed*, competing block-by-block to fill the swap at the tightest price. This lets liquidity providers hedge on centralized venues and quote aggressively, narrowing spreads and reducing the slippage and toxic-flow problems of conventional [[automated-market-maker|AMMs]]. The trade-off is that pricing quality depends on active, sophisticated market makers being present — thin LP participation widens spreads.

---

## Comparison vs Competing Cross-Chain DEXs / Bridges

| Dimension | **Chainflip** | THORChain | [[stargate-finance\|Stargate]] | [[across-protocol\|Across]] | Wormhole / Portal |
|---|---|---|---|---|---|
| Architecture | App-chain (Substrate) + TSS vaults | App-chain (Cosmos) + TSS vaults | App on [[layerzero\|LayerZero]] | Optimistic ([[uma\|UMA]]) + relayers | Guardian-attested messaging |
| Native BTC support | **Yes** | **Yes** | No (via wrapped/OFT) | No | Wrapped |
| Pricing model | **JIT AMM (active MM quotes)** | Continuous-liquidity pools (RUNE-paired) | Unified stable pools | Relayer/intent fill | n/a (transfer) |
| Liquidity asset | Direct asset pools | RUNE-bonded pools | Per-asset pools | HubPool | n/a |
| Token security role | FLIP bonded by validators | RUNE bonded + economic peg | STG governance/ve | ACX governance | W governance |
| Burn/deflation | **Swap buy-and-burn of FLIP** | RUNE supply policy | Emissions | Emissions | Emissions |
| Key trust assumption | Honest validator supermajority + sound MPC | Honest node supermajority + bond economics | Honest DVN set | ≥1 honest disputer | Honest guardian quorum |

Chainflip's closest peer is **THORChain** — both are app-specific chains using bonded validators and TSS vaults to enable native, no-wrapped-token swaps including [[bitcoin]]. Chainflip differentiates on its **JIT AMM** (active professional market-making vs THORChain's passive continuous-liquidity pools) and a simpler validator-bonding model that does not require pairing every pool against a native token.

---

## Governance & Value Accrual

- **FLIP utility.** FLIP is fundamentally a **work/security token**: validators bond it to earn the right to operate vaults and collect rewards. Unlike a pure governance token, FLIP's value is tied to (a) the demand to validate (staking yield from emissions + fees) and (b) the **buy-and-burn** that converts swap volume into deflationary pressure on supply.
- **Buy-and-burn flywheel.** A portion of network fees is used to buy FLIP from the market and burn it, directly linking token supply to real swap volume. In a high-volume regime this can outweigh validator-reward emissions and make FLIP net-deflationary; in a low-volume regime emissions dominate and the flywheel stalls.
- **Governance.** FLIP holders govern protocol parameters (supported chains, fee levels, validator economics). Governance is deliberately constrained relative to fund-custody to limit the governance-attack surface.
- **No fixed max supply.** FLIP has an unlimited max supply governed by emission and burn policy, so the *net* inflation/deflation rate — not a hard cap — is the key tokenomics variable to watch.

---

## Notable History

- **CoinList launch & blue-chip backers.** Chainflip ran a public sale via CoinList and is backed by Coinbase Ventures, Pantera Capital, Delphi Ventures and Blockchain Capital — reflected in its CoinGecko category tags.
- **Mainnet & multi-chain rollout.** Chainflip launched its mainnet swapping product and progressively added native support for Bitcoin, Ethereum, Solana, Polkadot/Assethub and EVM L2s, establishing itself as one of the few protocols offering genuinely native BTC↔EVM↔SOL swaps without wrapped assets.
- **ATH and drawdown.** FLIP reached an all-time high near $9.48 in March 2024 before retracing ~97% in the broader market downturn — typical of small-cap infrastructure tokens whose price tracks both volume cycles and sector sentiment.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 90.65M FLIP |
| **Total Supply** | 92.03M FLIP |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $18.39M |
| **Market Cap / FDV Ratio** | 0.99 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $9.48 (2024-03-07) |
| **Current vs ATH** | -97.89% |
| **All-Time Low** | $0.1913 (2026-04-03) |
| **Current vs ATL** | +4.43% |
| **24h Change** | -2.44% |
| **7d Change** | -0.59% |
| **30d Change** | -24.46% |
| **1y Change** | -54.97% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x826180541412d574cf1336d22c0c0a287822678a` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | FLIP/USDT | N/A |
| Crypto.com Exchange | FLIP/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X826180541412D574CF1336D22C0C0A287822678A/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://chainflip.io/](https://chainflip.io/) |
| **Twitter** | [@chainflip](https://twitter.com/chainflip) |
| **Telegram** | [chainflip_io_chat](https://t.me/chainflip_io_chat) (7,144 members) |
| **Discord** | [https://discord.gg/chainflip-community](https://discord.gg/chainflip-community) |
| **GitHub** | [https://github.com/chainflip-io/](https://github.com/chainflip-io/) |
| **Whitepaper** | [https://chainflip.io/whitepaper.pdf](https://chainflip.io/whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $102,830.00 |
| **Market Cap Rank** | #649 |
| **24h Range** | $0.1997 — $0.2048 |
| **Last Updated** | 2026-04-09 |

---

## Risks

Native cross-chain swap protocols still carry the bridge category's elevated risk profile (bridges have lost billions to exploits — Ronin, Wormhole, Nomad and others):

- **Validator-set / TSS compromise** — The vaults are only as safe as the bonded validator supermajority and the threshold-signature scheme. If a malicious supermajority colludes, or the MPC/key-rotation implementation is exploited, vault funds across chains could be stolen. This is the central trust assumption.
- **[[slashing]] & liveness** — Validators are slashed for misbehavior, but a large coordinated outage or a buggy key-rotation could halt swaps or freeze funds; liveness depends on a sufficiently honest, online validator set.
- **[[smart-contract-risk]] / protocol-code risk** — The State Chain logic, vault contracts on each connected chain, and the JIT AMM are complex; bugs in any could endanger user funds or mispricing.
- **Liquidity & volume risk** — Pricing quality and the FLIP buy-and-burn both depend on active market makers and trading volume. Thin volume (as seen in earlier snapshots) widens spreads and weakens token economics.
- **Sector & token risk** — As a small-cap bridge token deep below its all-time high, FLIP is highly volatile and sensitive to security sentiment and volume cycles.

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
- [[cross-chain-bridge]]
- [[slashing]]
- [[smart-contract-risk]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical market-data snapshot
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear)
- General market knowledge; no specific narrative wiki source ingested yet for protocol mechanism.
