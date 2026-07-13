---
title: "SaucerSwap"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, automated-market-maker]
aliases: ["SAUCE", "SaucerSwap Labs"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.saucerswap.finance/"
related: ["[[crypto-markets]]", "[[hedera]]", "[[hbar]]", "[[decentralized-exchange]]", "[[automated-market-maker]]", "[[defi]]", "[[uniswap]]", "[[liquidity-pool]]", "[[impermanent-loss]]"]
---

# SaucerSwap

**SaucerSwap** (token **SAUCE**) is the leading [[decentralized-exchange|decentralized exchange]] and [[automated-market-maker|AMM]] on the [[hedera|Hedera]] network, implemented as a set of non-upgradable smart contracts focused on censorship resistance, security, and self-custody. SAUCE trades at **$0.01607204**, ranking **#969** by market capitalization (~**$14.57M** market cap), down **-0.88%** over 24h but up **+0.37%** over the past 7 days — relative stability in an Extreme-Fear, Established-Bear tape (BTC ~$64,211; Fear & Greed 21).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SAUCE |
| **Market Cap Rank** | #969 |
| **Market Cap** | $14,568,272 |
| **Current Price** | $0.01607204 |
| **24h Change** | -0.88% |
| **7d Change** | +0.37% |
| **Categories** | Decentralized Exchange (DEX), Decentralized Finance (DeFi), Hedera Ecosystem, Base Ecosystem, Made in USA |
| **Website** | [https://www.saucerswap.finance/](https://www.saucerswap.finance/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

SaucerSwap is the leading [[decentralized-exchange|DEX]] on the [[hedera|Hedera]] network, implemented as a set of non-upgradable smart contracts focused on censorship resistance, security, and self-custody.

SaucerSwap leverages the **Hedera Token Service (HTS)** for rapid throughput and a low-cost, U.S. dollar-denominated fee structure. Hedera's architecture provides fair transaction ordering (via its hashgraph consensus), which the protocol argues substantially mitigates the front-running and MEV (maximal extractable value) attacks common on [[ethereum|Ethereum]]-based [[automated-market-maker|AMMs]] like [[uniswap|Uniswap]].

The protocol has two iterations:

- **SaucerSwap V1** — a constant-product [[automated-market-maker|AMM]] (the classic `x*y=k` model).
- **SaucerSwap V2** — introduces **concentrated liquidity** (Uniswap V3-style), letting liquidity providers concentrate capital within chosen price ranges for greater capital efficiency.

---

## Architecture — How It Works

SaucerSwap is best understood as a Uniswap-lineage AMM ported to Hedera's unique execution environment:

- **Hedera Token Service (HTS) settlement.** Tokens on Hedera are native HTS assets rather than ERC-20 contracts, giving predictable, low, USD-denominated fees and fast finality. SaucerSwap's contracts interact with HTS for transfers and pool accounting.
- **Fair ordering via hashgraph consensus.** Hedera's aBFT hashgraph assigns a consensus timestamp to each transaction, which the protocol argues reduces the latency-game [[automated-market-maker|MEV]] (sandwiching, front-running) that plagues Ethereum AMMs. This is a structural pitch for traders sensitive to execution quality.
- **V1 constant-product pools.** Classic `x*y=k` curve; LPs supply paired liquidity and earn swap fees, bearing [[impermanent-loss]].
- **V2 concentrated liquidity.** LPs choose price ranges, concentrating capital where trades occur — far higher capital efficiency but more active management and amplified [[impermanent-loss|impermanent loss]] if price exits the range.
- **Non-upgradable contracts.** The core contracts cannot be changed by an admin key — strong against rug/admin risk, but bugs cannot be patched in place.
- **MasterChef emissions & xSAUCE staking.** A MasterChef-style contract distributes SAUCE emissions to incentivize liquidity; staking SAUCE mints **xSAUCE**, which accrues a share of fees, HBAR staking rewards, and emissions via an automated buyback.

### Token Role: SAUCE & Value Accrual

SAUCE, the native token of SaucerSwap, has multiple roles:

- **Governance** — SAUCE lets holders participate in the SaucerSwap DAO, voting on ecosystem proposals such as protocol upgrades and incentive alignment.
- **Liquidity incentives** — governed by the MasterChef smart contract, SAUCE is emitted to incentivize liquidity provision in V1 and V2 pools.
- **Staking (xSAUCE)** — SAUCE holders can stake (receiving **xSAUCE**) to earn a share of trading fees, HBAR staking rewards, and emissions through an automated buyback mechanism. This buyback-and-stake loop is the primary value-accrual channel, partly offsetting emission dilution.

For more information, see the official docs at https://docs.saucerswap.finance.

### Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 894.89M SAUCE |
| **Total Supply** | 1.00B SAUCE |
| **Max Supply** | 1.00B SAUCE |
| **Fully Diluted Valuation** | $20.57M |
| **Market Cap / FDV Ratio** | 0.89 |

With ~89% of supply already circulating, remaining emission overhang is modest relative to peers — most dilution is behind it.

---

## Competitive Position

SaucerSwap is the dominant DEX within the [[hedera|Hedera]] ecosystem, so its fortunes are closely tied to Hedera's overall adoption and on-chain activity. Compared with DEXs on larger chains, SaucerSwap's addressable market is smaller but it is the clear leader on its home chain, benefiting from Hedera's low, predictable fees and fast finality. Its V2 concentrated-liquidity upgrade keeps it feature-competitive with leading EVM AMMs. The principal strategic risk is ecosystem concentration: being the leading DEX on a niche chain caps upside to that chain's growth.

| DEX | Home chain | Model | Edge | Trade-off |
|---|---|---|---|---|
| **SaucerSwap** | Hedera | V1 `x*y=k` + V2 concentrated liquidity | MEV-resistant ordering, low USD fees, leader on Hedera | TAM capped by Hedera adoption; thin volume |
| **[[uniswap|Uniswap]]** | Ethereum / Base / L2s | V2/V3/V4 AMM | Deepest liquidity, largest ecosystem | Higher gas; MEV exposure |
| **PancakeSwap** | BNB Chain | AMM + concentrated liquidity | Large user base, BNB liquidity | EVM MEV; emissions-heavy |
| **Curve** | Ethereum / multi | Stableswap AMM | Best-in-class stable/pegged swaps | Specialized; lower for volatile pairs |

See [[automated-market-maker]], [[liquidity-pool]], and [[impermanent-loss]] for the underlying mechanics.

---

## How & Where It Trades

SAUCE's primary liquidity is on its own venue on [[hedera|Hedera]]; centralized listing is limited (Kraken). 24h volume is thin (~$180k at last snapshot), so the token is a low-liquidity microcap whose fee accrual depends on Hedera on-chain activity rather than CEX speculation.

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | SAUCE/USD | N/A |

---

## Narrative, Category & Catalysts

- **Category:** DEX / AMM and the **Hedera ecosystem** — a beta play on Hedera ([[hbar|HBAR]]) adoption, enterprise/RWA narratives, and HTS-native DeFi.
- **Bull catalysts:** Rising Hedera TVL and on-chain volume; enterprise/RWA tokenization on Hedera driving HTS asset swaps; growth in xSAUCE fee/buyback yield; expansion of V2 concentrated-liquidity pools.
- **Bear catalysts:** Stagnant Hedera adoption; thin volume weakening fee accrual; MasterChef emissions outpacing buybacks.
- In the current Extreme-Fear regime, SAUCE's relative 7-day stability reflects a tight, leader-on-its-chain position, but low liquidity means upside requires a Hedera-specific catalyst.

---

## History / Timeline

| Date | Event |
|---|---|
| 2023-06-10 | SAUCE all-time low of **$0.00997926**. |
| 2024-02-29 | SAUCE all-time high of **$0.2335**. |
| (V2 era) | SaucerSwap V2 launches concentrated-liquidity pools (Uniswap V3-style) on Hedera. |
| 2026-06-21 | Trades ~$0.0161, rank #969, ~$14.6M cap; ~-91% from ATH. |

*Only dated events with on-page provenance are listed; V1/V2 mechanics are described qualitatively from public SaucerSwap documentation.*

---

## Risks

- **Ecosystem concentration** — SaucerSwap's value is highly correlated with Hedera ([[hbar|HBAR]]) adoption; weak Hedera growth directly constrains the DEX.
- **Liquidity & volume risk** — thin trading volume relative to larger-chain DEXs means wider spreads and weaker fee accrual to SAUCE stakers.
- **Smart-contract risk** — although non-upgradable contracts reduce admin-key risk, they also mean bugs cannot be easily patched.
- **Token emissions/dilution** — ongoing MasterChef emissions are a structural supply headwind, partly offset by the buyback mechanism.
- **Market backdrop** — the 2026-06-21 environment is risk-off ([[bitcoin|BTC]] ~$64,180; Fear & Greed 22, "Extreme Fear"), though SAUCE's slightly positive 7-day move shows relative stability.

> *Informational only, not investment advice. Crypto assets are highly volatile.*

---

## Trading Playbook

- **Regime behavior:** SAUCE is a Hedera-ecosystem beta. It tends to track HBAR and overall Hedera on-chain activity; in broad risk-off tape it drifts with the chain, with relative stability when DEX usage holds up. Low float and thin liquidity make moves choppy in both directions.
- **What to watch:** Hedera TVL and DEX volume; xSAUCE staking yield (fees + HBAR rewards + buyback); SAUCE emissions vs buybacks; V2 concentrated-liquidity adoption; HBAR price as the primary correlation driver.
- **In this tape:** with Extreme Fear and BTC ~16% below its 200-day MA, microcap DEX tokens are pressured; SAUCE's edge is being the leader on its chain, so position it as a leveraged bet on Hedera adoption rather than a standalone trade. Size for thin liquidity.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 894.89M SAUCE |
| **Total Supply** | 1.00B SAUCE |
| **Max Supply** | 1.00B SAUCE |
| **Fully Diluted Valuation** | $20.57M |
| **Market Cap / FDV Ratio** | 0.89 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2335 (2024-02-29) |
| **Current vs ATH** | -91.19% |
| **All-Time Low** | $0.00997926 (2023-06-10) |
| **Current vs ATL** | +106.19% |
| **24h Change** | -2.15% |
| **7d Change** | +1.49% |
| **30d Change** | +1.40% |
| **1y Change** | -43.29% |

---

## Platform & Chain Information

**Native Chain:** Hedera Hashgraph

### Contract Addresses

| Chain | Address |
|---|---|
| Hedera Hashgraph | `0x00000000000000000000000000000000000b2ad5` |
| Base | `0xa4ff56ef7ef4a2cad03cfa130208c9bc1b45d293` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | SAUCE/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.saucerswap.finance/](https://www.saucerswap.finance/) |
| **Twitter** | [@SaucerSwapLabs](https://twitter.com/SaucerSwapLabs) |
| **Telegram** | [SaucerSwapLabs](https://t.me/SaucerSwapLabs) (2,359 members) |
| **Discord** | [https://discord.com/invite/PvgKSTTMbf](https://discord.com/invite/PvgKSTTMbf) |
| **GitHub** | [https://github.com/saucerswaplabs/saucerswaplabs-core](https://github.com/saucerswaplabs/saucerswaplabs-core) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 11 |
| **GitHub Forks** | 7 |
| **Pull Requests Merged** | 1 |
| **Contributors** | 1 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $179,962.00 |
| **Market Cap Rank** | #965 |
| **24h Range** | $0.0206 — $0.0216 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[hedera]]
- [[hbar]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[liquidity-pool]]
- [[impermanent-loss]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; protocol mechanics (HTS, V1/V2 AMM, xSAUCE staking) from public SaucerSwap documentation. No additional specific wiki source ingested yet.
