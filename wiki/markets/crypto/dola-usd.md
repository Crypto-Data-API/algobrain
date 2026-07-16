---
title: "DOLA"
type: market
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["DOLA", "DOLA USD", "Inverse Finance DOLA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.inverse.finance/"
related: ["[[collateralization]]", "[[crvusd]]", "[[crypto-markets]]", "[[curve]]", "[[dai]]", "[[defi]]", "[[ethereum]]", "[[stablecoin]]", "[[tether]]", "[[usdc]]"]
---

# DOLA

**DOLA** (native on [[ethereum|Ethereum]]) is a decentralized, **debt-backed (crypto-collateralized)** [[stablecoin]] soft-pegged to the U.S. dollar, issued by the **Inverse Finance** [[defi|DeFi]] protocol. Unlike fiat-reserve stablecoins such as [[usdc|USDC]] or [[paxos-standard|USDP]], DOLA is created as protocol debt: it is borrowed into existence against crypto collateral via Inverse Finance's lending system (**FiRM**) rather than minted 1:1 against bank-held dollars. Its closest design peers are [[dai|DAI]] and Curve's [[crvusd|crvUSD]] — collateralized debt positions (CDPs), not custodial reserves.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, DOLA trades at **$0.995358**, holds market-cap rank **#451**, and carries a market capitalization of **$50,213,602** (**24h −0.08%**, **7d −0.07%**). The small discount to $1 is typical for a crypto-collateralized stablecoin, which trades at a soft peg rather than a hard redemption peg.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DOLA |
| **Price (2026-06-21)** | $0.995358 |
| **Market Cap Rank** | #451 |
| **Market Cap** | $50,213,602 |
| **24h Change** | −0.08% |
| **7d Change** | −0.07% |
| **Peg target** | Soft peg, 1 DOLA ≈ 1 USD |
| **Backing model** | Crypto / debt-backed (CDP-style via FiRM) |
| **Issuer** | Inverse Finance (decentralized protocol) |
| **Native chain** | [[ethereum\|Ethereum]]; bridged to Base, Arbitrum, Optimism, BSC, Fantom |
| **Website** | [https://www.inverse.finance/](https://www.inverse.finance/) |

---

## Architecture: Issuer & Mechanism

DOLA is issued by **Inverse Finance**, a decentralized, DAO-governed protocol with no central fiat custodian. There is no bank reserve and no 1:1 cash redemption; DOLA's value is defended by **over-collateralization, supply control, and DEX arbitrage**. DOLA enters circulation in two main ways:

### 1. FiRM borrowing (the CDP layer)
**FiRM (Fixed Rate Market)** is Inverse Finance's isolated-collateral lending market. Users deposit crypto collateral into a **Personal Collateral Escrow** (per-user, per-market isolation that contains contagion) and borrow DOLA against it, subject to a per-market collateral factor. The cost of borrowing is governed by the **DBR (DOLA Borrowing Right)** token: holding/spending 1 DBR entitles the holder to borrow 1 DOLA for one year. DBR effectively pre-pays and fixes the borrow rate, decoupling it from volatile spot interest rates — the protocol's signature design. This is conceptually a **collateralized debt position (CDP)** model, like [[dai|DAI]]'s vaults or [[crvusd|crvUSD]]'s LLAMMA, but with the fixed-rate DBR twist and isolated escrows.

### 2. DOLA Feds (the supply-control layer)
Protocol-controlled smart contracts called **"Feds"** mint or burn DOLA directly into liquidity venues (e.g. [[curve|Curve]] pools) to add or remove supply. A **Fed expansion** mints DOLA into a pool to deepen liquidity; a **contraction** burns DOLA to tighten supply and support the peg. This is an open-market-operations-style mechanism that lets the DAO actively manage where DOLA's price sits relative to $1.

### Peg maintenance
Because DOLA is debt-backed rather than fiat-redeemable, its peg is **soft**: defended by collateralization, by arbitrage in DOLA/[[usdc|USDC]]/[[tether|USDT]] liquidity pools, and by Fed expansion/contraction — **not** by a 1:1 cash redemption guarantee. The small discount ($0.9954) is the expected behavior of a soft-pegged CDP stablecoin. See [[collateralization]].

---

## Tokenomics & Supply

DOLA supply is **demand-driven and elastic**: it grows as users borrow against collateral (FiRM) and as Feds expand into pools, and shrinks on repayment, liquidation, and Fed contraction. There is no fixed max supply. Solvency rests on **over-collateralization** — borrowers post more crypto value than the DOLA they mint — plus the DAO's active supply management. Two governance tokens orbit DOLA: **INV** (the Inverse Finance governance token) and **DBR** (the borrowing-right token that prices fixed-rate loans). At ~$50M market cap, DOLA is a mid-small DeFi stablecoin whose stability is tightly coupled to the depth of its Curve/Balancer liquidity.

---

## Comparison vs Competitor Stablecoins

| Stablecoin | Issuer | Backing | Peg type | Rate mechanism |
|---|---|---|---|---|
| **DOLA** | Inverse Finance | Crypto collateral via FiRM (isolated escrows) | Soft (CDP) | Fixed-rate via DBR |
| [[dai\|DAI]] | MakerDAO/Sky | Crypto + RWA collateral | Soft (CDP), PSM-assisted | Variable stability fee |
| [[crvusd\|crvUSD]] | Curve | Crypto collateral (LLAMMA soft-liquidation) | Soft (CDP) | Dynamic PegKeeper |
| [[usdc\|USDC]] | Circle | Cash + T-bills | Hard (redeemable) | n/a (fiat) |
| [[paxos-standard\|USDP]] | Paxos | Cash + T-bills | Hard (redeemable) | n/a (fiat) |

DOLA's distinguishing features are **fixed-rate borrowing (DBR)** and **isolated Personal Collateral Escrows**; its tradeoff versus DAI/crvUSD is smaller scale, thinner liquidity, and a more eventful security history (below).

---

## How & Where It Trades / Is Used

DOLA liquidity is concentrated in [[defi|DeFi]] venues — notably [[curve|Curve]] and Balancer pools pairing DOLA with [[usdc|USDC]] and other stablecoins — across [[ethereum|Ethereum]] and L2s (Base, Arbitrum, Optimism) plus BSC and Fantom. Primary use cases are as a fixed-rate borrowing asset (borrow DOLA cheaply against collateral, deploy elsewhere), as a stable unit in DeFi, and as a yield source via DOLA-paired LP positions. Its ~$50M market cap makes it a mid-small stablecoin whose peg depends heavily on the depth of those pools.

---

## Narrative, Category & Catalysts

DOLA sits in the **decentralized, crypto-backed stablecoin** category, with a niche identity around **fixed-rate DeFi borrowing**. Catalysts: growth of FiRM collateral types and TVL, DBR demand (which prices the protocol's core product), expansion of DOLA liquidity to new chains/pools, and broader DeFi appetite for non-custodial dollars amid stablecoin-regulation pressure on fiat issuers. Counter-trends: DOLA competes for the same soft-peg demand as much larger [[dai|DAI]] and [[crvusd|crvUSD]], and its exploit history weighs on trust. In the current **Extreme Fear / bottoming-accumulation** regime (Fear & Greed 21), crypto-collateralized stablecoins face the dual pressure of soft-peg discounts widening when collateral falls and DeFi liquidity thinning.

---

## History / Depeg & Risk Timeline

Inverse Finance has a documented history of security incidents that bear directly on DOLA holders:

- **April 2022** — An **oracle-manipulation attack** on Inverse Finance's money market drained substantial value.
- **June 2022** — A **second money-market/oracle incident** caused further losses. Together these 2022 exploits drove the redesign toward the more conservative, isolated-collateral **FiRM** architecture with Personal Collateral Escrows and the DBR fixed-rate model.
- **All-time-low print (~$0.088)** — DOLA's record low in the historical data reflects an **extreme low-liquidity print**, not a sustained trading level; the working price has generally stayed in a narrow band around $1, currently $0.995358.

These episodes are why DOLA carries materially higher protocol/smart-contract risk than fiat-backed peers, and why its peg should be read as a **managed soft peg**.

---

## Risks

- **Smart-contract / oracle risk (realized)** — Inverse Finance has been exploited before (2022); oracle manipulation is a documented attack vector against this protocol specifically.
- **Collateral risk** — As a crypto-backed stablecoin, DOLA's solvency depends on the value and orderly liquidation of volatile collateral; sharp collateral drawdowns can stress the peg.
- **Soft-peg / liquidity risk** — No 1:1 cash redemption; the peg relies on DEX liquidity and Fed operations, so thin liquidity can produce visible discounts (as seen at $0.9954).
- **Fixed-rate / DBR risk** — The DBR mechanism can leave borrowers under-provisioned if DBR runs out, forcing accruing debt and liquidation pressure.
- **Governance risk** — DAO decisions on collateral parameters, DBR pricing, and Fed mint/burn directly affect peg stability and solvency.

See [[stablecoin]], [[depeg]], and [[collateralization]] for the general framework.

---

## Trading Playbook

- **Treat the peg as soft** — a few-tens-of-bps discount is normal; reserve "depeg" judgments for sustained, widening discounts tied to collateral or liquidity stress.
- **Borrowing angle** — DOLA is most interesting as a fixed-rate borrow via FiRM/DBR; model DBR cost before assuming a "cheap" rate.
- **Liquidity discipline** — size trades to Curve/Balancer pool depth; DOLA is far thinner than DAI/crvUSD.
- **Risk-off caution** — in a bottoming regime with falling collateral values, crypto-backed stablecoins carry more tail risk than fiat-reserve dollars; prefer redeemable coins for pure parking.

---

## Related

- [[stablecoin]]
- [[defi]]
- [[collateralization]]
- [[depeg]]
- [[dai]]
- [[crvusd]]
- [[usdc]]
- [[tether]]
- [[curve]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge (Inverse Finance FiRM/DBR mechanism, 2022 exploits); no specific wiki source ingested yet.

## Overview

DOLA is the asset and debt backed decentralized stablecoin of Inverse Finance

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 45.48M DOLA |
| **Total Supply** | 100.89M DOLA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $100.46M |
| **Market Cap / FDV Ratio** | 0.45 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.87 (2021-11-13) |
| **Current vs ATH** | -46.82% |
| **All-Time Low** | $0.0884 (2024-02-10) |
| **Current vs ATL** | +1026.18% |
| **24h Change** | +0.00% |
| **7d Change** | +0.11% |
| **30d Change** | -0.07% |
| **1y Change** | -0.34% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x865377367054516e17014ccded1e7d814edc9ce4` |
| Fantom | `0x3129662808bec728a27ab6a6b9afd3cbaca8a43c` |
| Base | `0x4621b7a9c75199271f773ebd9a499dbd165c3191` |
| Binance Smart Chain | `0x2f29bc0ffaf9bff337b31cbe6cb5fb3bf12e5840` |
| Arbitrum One | `0x6a7661795c374c0bfc635934efaddff3a7ee23b6` |
| Optimistic Ethereum | `0x8ae125e8653821e851f12a49f7765db9a9ce7384` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X865377367054516E17014CCDED1E7D814EDC9CE4/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Sushiswap | 0X865377367054516E17014CCDED1E7D814EDC9CE4/0X41D5D79431A913C4AE7D69A668ECDFE5FF9DFB68 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.inverse.finance/](https://www.inverse.finance/) |
| **Twitter** | [@InverseFinance](https://twitter.com/InverseFinance) |
| **Telegram** | [InverseFinance](https://t.me/InverseFinance) (1,550 members) |
| **Discord** | [https://discord.com/invite/YpYJC7R5nv](https://discord.com/invite/YpYJC7R5nv) |
| **GitHub** | [https://github.com/InverseFinance](https://github.com/InverseFinance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $645,249.00 |
| **Market Cap Rank** | #458 |
| **24h Range** | $0.9941 — $0.9964 |
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
