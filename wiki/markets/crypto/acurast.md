---
title: "Acurast"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, defi, machine-learning]
aliases: ["ACU"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://acurast.com/"
related: ["[[crypto-markets]]", "[[depin]]", "[[decentralized-compute]]", "[[trusted-execution-environment]]"]
---

# Acurast

**Acurast** (ACU) is a [[depin|decentralized physical infrastructure network (DePIN)]] that turns idle smartphones into a permissionless [[decentralized-compute|serverless compute]] cloud. Phones enrolled as "processors" execute developer workloads inside the device's hardware [[trusted-execution-environment|Trusted Execution Environment (TEE)]], enabling confidential, verifiable off-chain computation without trusting a centralized cloud provider. As of 2026-06-22 ACU trades at **$0.083268**, ranked **#733** by market capitalization with a market cap of **~$24.9M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ACU |
| **Market Cap Rank** | #733 |
| **Market Cap** | ~$24.92M |
| **Current Price** | $0.083268 |
| **24h Change** | -5.14% |
| **7d Change** | +1.93% |
| **Categories** | Artificial Intelligence (AI), DePIN, Confidential Compute, BNB Chain / Ethereum / Base / Peaq Ecosystem, CoinList Launchpad |
| **Website** | [https://acurast.com/](https://acurast.com/) |

---

## Overview

Acurast positions itself as a [[depin|DePIN]]-based alternative to centralized "serverless" platforms such as AWS Lambda. Anyone with a compatible Android smartphone can register the device as an Acurast **processor**; the device then receives and runs developer-submitted jobs (oracle feeds, off-chain computation, API relays, automation tasks) inside its hardware-backed [[trusted-execution-environment|TEE]]. Because execution happens inside the TEE, the operator hosting the phone cannot read or tamper with the workload, and the result can be cryptographically attested — the core "confidential compute" value proposition.

Repurposing the large global stock of retired and idle smartphones is the supply-side thesis: phones are cheap, energy-efficient, ship with secure enclaves by default, and represent enormous latent compute. On the demand side, Acurast targets Web3 developers who need trust-minimized off-chain execution (oracles, keepers, cross-chain automation) and confidential AI/data workloads. ACU is deployed across multiple chains (Ethereum, Base, BNB Chain, Peaq) rather than a single L1, reflecting Acurast's multi-chain orchestration role.

---

## Architecture — How It Works

Acurast is a marketplace for **confidential serverless compute** matching developers ("consumers") with a permissionless pool of smartphone "processors":

1. **Processors (supply).** An owner enrolls a compatible Android smartphone using the Acurast app. The device joins the network and stands ready to execute developer jobs. The supply thesis is that the global stock of idle/retired smartphones is enormous, energy-efficient, and — critically — ships with a hardware secure enclave by default, so confidential compute is available at near-zero marginal hardware cost.
2. **Jobs (demand).** Developers submit workloads — oracle data feeds, off-chain computation, API relays, keepers/automation, cross-chain triggers, and confidential AI/data tasks. The orchestration layer matches each job to eligible processors and schedules execution.
3. **TEE execution + attestation (the trust mechanism).** Jobs run **inside the device's hardware [[trusted-execution-environment|Trusted Execution Environment (TEE)]]** — an isolated, encrypted region of the processor (e.g. Android's secure enclave / hardware-backed keystore). Because code and data are sealed inside the TEE, the phone's owner cannot read or tamper with the workload, and the hardware can produce a **remote attestation** — a cryptographic statement signed by the device's secure hardware proving that a genuine, unmodified TEE ran a specific piece of code. This is what lets a consumer trust a result from an anonymous, untrusted phone.

**Why TEE instead of ZK?** Acurast's trust model is **hardware-rooted** (attestation from the device's secure enclave) rather than **math-rooted** (zero-knowledge proofs, as used by [[space-and-time|Space and Time]]). TEE attestation is far cheaper and more general — it can run arbitrary code, including confidential workloads — but it shifts the trust assumption onto the integrity of the chip vendor's secure-enclave implementation, which is a different (and not zero) risk surface.

**Multi-chain orchestration.** Rather than living on one L1, Acurast deploys ACU and its coordination contracts across [[ethereum|Ethereum]], [[base|Base]], BNB Chain, and Peaq, positioning itself as a cross-chain compute/oracle layer that any of these ecosystems can call.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 240.49M ACU |
| **Total Supply** | 1.01B ACU |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $82.01M |
| **Market Cap / FDV Ratio** | 0.24 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3159 (2026-01-24) |
| **All-Time Low** | $0.0693 (2026-01-21) |
| **24h Change (to 2026-06-22)** | -5.14% |
| **7d Change (to 2026-06-22)** | +1.93% |

ACU has retraced heavily from its January 2026 launch-window high near $0.32 to the low-$0.08 range, a roughly 74% drawdown that is typical of recently listed DePIN tokens once initial listing demand fades. The token held flat over the trailing week (+1.93%) despite a broad risk-off backdrop — the overall market sat in **Extreme Fear** (Fear & Greed 21) on 2026-06-22 with [[bitcoin|BTC]] near $64,508.

---

## Token Role & Mechanism

ACU is the network's work-and-payment unit. Developers pay for compute jobs in ACU; processors (smartphone operators) earn ACU for correctly executing and attesting jobs. The design intends ACU demand to scale with *actual paid compute consumption* rather than pure speculation — the central question for any [[depin|DePIN]] token. The risk is the standard DePIN **demand-vs-emissions** problem: if processor rewards (token emissions and incentives) outpace real fee revenue from developers, sell pressure dominates and the token price decays even as the physical network grows. Acurast's edge thesis is that confidential TEE compute is a genuinely scarce capability that centralized clouds cannot easily offer trustlessly.

### Value Accrual & Governance

- **Fee throughput.** Every paid job routes ACU from consumer to processor — the core demand loop. Sustainable value accrual requires this fee revenue to grow faster than reward emissions.
- **Processor incentives.** ACU rewards bootstrap supply-side participation (more enrolled phones); the design challenge is transitioning from emission-funded to fee-funded rewards as the network matures.
- **Governance.** As the native asset, ACU is positioned to govern protocol parameters as the network decentralizes.

Note the supply structure: **max supply is uncirculated/unlimited** with ~240M of ~1.01B total circulating (MC/FDV ≈ 0.24), so emissions and unlocks are a material dilution consideration — the cleanest read on Acurast's health is whether *paid* job revenue is rising, not whether the physical processor count is.

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Peaq | `0x165bcb970836f83c15b22c3c1622279d97a20446` |
| Ethereum | `0x216b3643ff8b7bb30d8a48e9f1bd550126202add` |
| Base | `0xc5fed7c8ccc75d8a72b601a66dffd7a489073f0b` |
| Binance Smart Chain | `0x6ef2ffb38d64afe18ce782da280b300e358cfeaf` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | ACU/USD | N/A |
| KuCoin | ACU/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://acurast.com/](https://acurast.com/) |
| **Telegram** | [acurastnetwork](https://t.me/acurastnetwork) (29,178 members) |
| **Discord** | [https://discord.gg/wqgC6b6aKe](https://discord.gg/wqgC6b6aKe) |
| **GitHub** | [https://github.com/Acurast](https://github.com/Acurast) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.55M (2026-04-09 snapshot) |
| **Market Cap Rank** | #733 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-06-22 |

---

## Competitive Position

Acurast competes in the [[decentralized-compute]] / DePIN compute arena but differentiates on **confidential** compute via consumer-device TEEs rather than renting datacenter GPUs. Its niche is verifiable, privacy-preserving off-chain execution plus oracle/keeper services.

| Project | Token | Hardware / model | Trust mechanism | Best suited for |
|---|---|---|---|---|
| **Acurast** | ACU | Idle smartphones (TEE) | Hardware TEE remote attestation | Many small confidential jobs, oracles, keepers, automation |
| **[[akash-network\|Akash]]** | AKT | Datacenter GPU/CPU | Reputation / staking; not confidential by default | General GPU/CPU cloud, container workloads |
| **[[io\|io.net]]** | IO | Aggregated idle GPUs | Reputation / staking | ML training + inference clusters |
| **[[render-token\|Render]]** | RENDER | GPUs | Reputation / proof-of-render | GPU rendering + AI compute |
| **[[nosana\|Nosana]]** | NOS | GPUs ([[solana\|Solana]]) | Staking / reputation | AI inference endpoints |

The smartphone-supply model gives Acurast very low marginal hardware cost and a confidentiality property the GPU-renting peers lack, but per-node compute is modest — so the network is suited to **many small attested jobs** (oracles, keepers, light confidential tasks) rather than heavy ML training, which is where Akash/io.net/Render compete.

## How & Where It Trades

- **Spot venues.** ACU lists on Kraken (ACU/USD) and KuCoin (ACU/USDT) on the CEX side; it is deployed across [[ethereum|Ethereum]], [[base|Base]], BNB Chain, and Peaq, so liquidity is fragmented across chains. It launched via a **CoinList** launchpad sale.
- **Derivatives.** No liquid ACU perpetual market exists at this size; price discovery is spot-driven and the token cannot be readily hedged.
- **Float / unlock overhang.** With ~240M of ~1.01B total circulating (MC/FDV ≈ 0.24) and unlimited max supply, scheduled emissions/unlocks are a structural dilution headwind — the ~$25M cap versus ~$82M FDV prices in significant future supply, typical of a recently-launched DePIN token.

## Narrative, Category & Catalysts

ACU sits in the **DePIN** and **confidential-compute** narratives, with a secondary [[artificial-intelligence|AI]]-data angle (confidential AI/data workloads). Its differentiated story — repurposing idle smartphones for TEE-secured confidential compute — gives it a distinct pitch versus the GPU-rental crowd. Catalysts: demonstrable growth in *paid* job revenue, marquee developer integrations for oracles/keepers/confidential AI, and broad DePIN narrative rotations. The dominant de-rating risk is the standard one — the physical network growing while paid demand and fee revenue stay thin against emissions.

## History & Timeline

- **2026-01-21** — ACU all-time low of **$0.0693**, in its launch window.
- **2026-01-24** — ACU all-time high of **$0.3159**, during initial listing demand.
- **2026-06-22** — Trades ~$0.083 (~74% below the January 2026 launch-window high); -5.14% 24h / +1.93% 7d amid market-wide Extreme Fear (Fear & Greed 21, BTC ~$64,508).

---

## Risks

- **Narrative dependence** — valuation is tied to the broader DePIN / confidential-compute narrative; sentiment rotations hit the whole sector at once.
- **Emissions vs. real demand** — sustainability requires paid developer compute to exceed processor reward emissions; this is unproven for most DePIN tokens.
- **Low liquidity** — a sub-$25M cap with thin 24h volume means high slippage and vulnerability to sharp moves; not suitable for size.
- **TEE trust assumptions** — confidentiality rests on smartphone secure-enclave integrity; hardware-level vulnerabilities would undercut the core value proposition.
- **Multi-chain / smart-contract risk** — ACU is deployed across several chains, broadening the contract and bridge attack surface.

---

## Trading Playbook

> *Educational context, not financial advice. ACU is a thin, recently-launched, high-beta small-cap.*

- **Regime awareness.** In the current **Established Bear Market / Extreme Fear** tape (Fear & Greed 21, BTC ~16% below its 200-day MA as of 2026-06-22), DePIN small-caps are high-beta and trend hard in both directions. ACU's relative steadiness over the trailing week is not durable strength — these names amplify the broader risk cycle.
- **Post-launch supply.** As a January-2026 launch with ~0.24 MC/FDV and unlimited max supply, ACU carries a recurring unlock/emission overhang; track the emission schedule before sizing.
- **Liquidity discipline.** Sub-$25M cap with chain-fragmented, thin liquidity and no perp to hedge — expect wide spreads and slippage; size accordingly.
- **Watch fees, not phones.** The bull case is rising *paid* job revenue and confidential-compute adoption, not headline processor counts. Distinguish genuine demand from emission-funded supply growth.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[depin]]
- [[decentralized-compute]]
- [[trusted-execution-environment]]
- [[akash-network]]
- [[nosana]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). General market knowledge; no specific wiki source ingested yet for project mechanics.
