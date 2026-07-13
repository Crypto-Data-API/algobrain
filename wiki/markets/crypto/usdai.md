---
title: "USDai"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi, ai-trading]
aliases: ["USDAI", "USD.AI", "Permian Labs"]
entity_type: protocol
founded: 2024
headquarters: "Decentralized"
website: "https://usd.ai"
related: ["[[crypto-markets]]", "[[arbitrum]]", "[[stablecoins]]", "[[ethena]]", "[[nvidia]]", "[[real-world-assets]]", "[[synthetic-dollar]]"]
---

# USDai

**USDai** (ticker **USDAI**) is a yield-bearing [[synthetic-dollar|synthetic dollar]] issued by the **USD.AI** protocol (developed by **Permian Labs**), native to [[arbitrum|Arbitrum One]] and backed by loans collateralized with AI hardware — primarily [[nvidia|Nvidia]] GPUs — plus compute and DePIN assets. It targets 15–25% APR via its staked token **sUSDai** and functions like a tokenized high-yield credit index on income-generating AI infrastructure, making it the flagship of the "AI-collateral stablecoin" niche at the intersection of the [[stablecoins|stablecoin]], [[real-world-assets|RWA-credit]], and AI-infrastructure narratives.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | USDAI |
| **Current Price** | $0.998817 |
| **Market Cap** | $190.1M |
| **Market Cap Rank** | #183 |
| **24h Volume** | $103.5K |
| **24h Change** | -0.09% |
| **7d Change** | -0.08% |
| **Circulating Supply** | ~190.3M USDAI |
| **Total Supply** | ~190.3M USDAI (MC/FDV = 1.00) |
| **Max Supply** | Uncapped (mint/redeem against collateral) |
| **All-Time High** | $1.19 (2025-09-04), -15.88% from ATH |
| **All-Time Low** | $0.769779 (2025-09-26) |

USDai trades close to peg (~$0.999) on very thin secondary volume (~$0.10M/day) — exit liquidity is the dominant practical risk for size. Supply has contracted to ~$190M (down from $269M at the April 2026 snapshot, i.e. roughly $79M of redemptions/outflows over Q2 2026), consistent with yield compression or rotation out of synthetic-dollar products amid the **Established Bear Market** (Crypto [[fear-and-greed-index|Fear & Greed Index]] ≈ 23 / extreme fear, 2026-06-21).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDAI (yield-bearing version: sUSDai) |
| **Sector** | Yield-bearing stablecoin / synthetic dollar; AI-hardware credit |
| **Developer** | Permian Labs |
| **Native Chain** | Arbitrum One; also Ethereum, Base, Plasma; built on the M0 stablecoin platform |
| **Market Cap** | $190.1M, rank #183 (CoinGecko, 2026-06-21) |
| **Peg** | ~$0.99–1.00; ATH $1.19 (2025-09-04), ATL $0.7698 (2025-09-26) — peg has broken both ways |
| **Website** | [https://usd.ai](https://usd.ai) |

---

## Overview

USD.AI bridges the gap between amortizing AI hard assets and the financing needed to scale productive infrastructure. AI/DePIN companies that cannot access traditional credit borrow stablecoins against their GPU fleets; depositors who mint and stake USDai (receiving **sUSDai**) earn the loan interest. Arbitrage mechanisms exist to pull USDai back to peg.

**CALIBER framework**: Permian Labs' collateralization standard tokenizes GPU hardware as NFTs, which serve as loan collateral with defined loan-to-value ratios, insurance, and liquidation mechanics — effectively treating GPUs as on-chain mortgages. USD.AI claims loan approval times cut by more than 90% versus traditional lenders.

### 2025–2026 developments

- **Aug 2025** — $13M Series A led by Framework Ventures, with Dragonfly, Arbitrum and others participating; Coinbase Ventures also invested in Permian Labs. Protocol had ~$50M deposits in private beta.
- **Sep 2025** — Public launch period; token traded as high as $1.19 (Sep 4) and as low as $0.77 (Sep 26) — evidence of immature peg arbitrage during the launch/ICO window.
- **Oct 2025** — QumulusAI secured a **$500M blockchain-backed credit facility** via USD.AI to scale AI compute infrastructure (announced 2025-10-09) — the protocol's marquee deal.
- **2026** — CALIBER protocol launch initiative reported targeting a ~$300M valuation; supply contracted from ~$269M (April) to ~$198M (June), suggesting yield compression or rotation out of synthetic-dollar yield products.

---

## Mechanism & Backing

USDai is a **credit-backed synthetic dollar** — its backing is a loan book, not fiat reserves or a basis trade. This means it carries **credit and duration risk** rather than the peg/reserve risk of a fiat stablecoin or the funding risk of a delta-neutral synthetic dollar.

- **Collateral (CALIBER framework)** — Permian Labs' standard tokenizes GPU hardware (and compute/DePIN assets) as NFTs that serve as loan collateral with defined loan-to-value ratios, insurance, and liquidation mechanics — effectively on-chain mortgages on AI hardware. AI/DePIN firms that cannot access traditional credit borrow stablecoins against their GPU fleets.
- **Yield (sUSDai)** — depositors mint USDai and stake to receive **sUSDai**, which accrues the loan interest paid by borrowers (target 15–25% APR). Yield is income from real borrowers, so it depends on borrower performance and GPU-rental economics.
- **Peg maintenance** — arbitrage incentives pull USDai back toward $1; the immature launch-window peg (ATH $1.19, ATL $0.77 in Sep 2025) reflects thin early liquidity, not a reserve shortfall.
- **Redemption & custody** — mint/redeem against the protocol; collateral NFTs and loan servicing are managed under CALIBER. Built on the **M0** stablecoin platform for composability across Arbitrum, Ethereum, Base, and Plasma.

**Marquee deal.** In October 2025, **QumulusAI** secured a $500M blockchain-backed credit facility via USD.AI — the protocol's largest exposure and a concentration-risk flag.

---

## Peer Comparison — Exotic-Backed Synthetic Dollars

| Token | Backing | Risk type | Yield token | Target APR |
|---|---|---|---|---|
| **USDai** (this page) | AI-hardware / GPU credit | Credit + duration | sUSDai | 15–25% |
| [[ethena-usde|USDe]] | Delta-neutral crypto basis | Funding-rate | sUSDe | Variable (funding) |
| [[falcon-finance|USDf]] | Overcollateralized crypto + RWA | Collateral + funding | sUSDf | Variable |
| [[usdtb]] | Fiat + BUIDL T-bills | Reserve/custodial | — | None (payment coin) |

---

## Trading Relevance

- **Not a trading vehicle per se** — it is a yield instrument. The trade is the carry: mint/buy USDAI near or below $1, stake to sUSDai for the 15–25% target APR, monitor collateral health.
- **Venues**: DEX-only; deepest pair is USDAI/USDC on Fluid (Arbitrum). No major CEX listings as of June 2026. Thin 24h volume (~$0.4M) — exit liquidity is the main risk for size.
- **Key risks/signals**: peg deviations (history of ±20% moves in Sep 2025), GPU depreciation vs loan tenor (AI hardware amortizes fast), borrower concentration (e.g., QumulusAI facility), and the broader AI-capex cycle ([[ai-capex-vs-cash-flow-divergence]]). A sharp fall in GPU rental rates would impair collateral income across the book.
- **Narrative basket**: AI x DeFi / RWA-credit basket; comparable to [[ethena|Ethena]] in "synthetic dollar with exotic backing" but with credit risk instead of basis risk.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~190.3M USDAI (CoinGecko, 2026-06-21); 269.36M at April 2026 snapshot |
| **Max Supply** | Unlimited (mint/redeem against collateral) |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Risks

- **Credit / borrower-concentration risk** — backing is a loan book; the $500M QumulusAI facility is a large single exposure, and a borrower default impairs the book.
- **Collateral-depreciation risk** — AI hardware amortizes fast; if GPU resale or rental rates fall (a softening AI-capex cycle, see [[ai-capex-vs-cash-flow-divergence]]), collateral value and loan income both deteriorate.
- **Peg risk** — history of ±20% deviations during the Sept 2025 launch window; thin liquidity can amplify dislocations.
- **Liquidity risk** — DEX-only, ~$0.10M daily volume; large exits face heavy slippage.
- **Smart-contract / oracle risk** — CALIBER NFT collateralization, liquidation logic, and cross-chain (M0) deployment are an attack surface.
- **Yield-decay risk** — Q2 2026 supply contraction (~$190M from ~$269M) signals yield compression or rotation out of the niche.

---

## Platform & Chain Information

**Native Chain:** Arbitrum One

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0x0a1a1a107e45b7ced86833863f482bc5f4ed82ef` |
| Ethereum | `0x0b2b2b2076d95dda7817e785989fe353fe955ef9` |
| Plasma | `0x0a1a1a107e45b7ced86833863f482bc5f4ed82ef` |
| Base | `0x0a1a1a107e45b7ced86833863f482bc5f4ed82ef` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://usd.ai](https://usd.ai) |
| **Twitter** | [@USDai_Official](https://twitter.com/USDai_Official) |
| **Telegram** | ~4,500 members (Apr 2026) |
| **Docs** | [https://docs.usd.ai](https://docs.usd.ai) |

---

## Related

- [[crypto-markets]]
- [[arbitrum]]
- [[stablecoins]] / [[stablecoin]]
- [[synthetic-dollar]]
- [[stablecoin-yields]]
- [[real-world-assets]]
- [[ethena]] / [[ethena-usde]]
- [[falcon-finance]]
- [[usdtb]]
- [[nvidia]]
- [[ai-capex-vs-cash-flow-divergence]]

---

## Sources

- CoinDesk — "USD.AI Raises $13M to Expand GPU-Backed Stablecoin Lending" (2025-08-13): https://www.coindesk.com/business/2025/08/13/usd-ai-raises-usd13m-to-expand-gpu-backed-stablecoin-lending
- CoinDesk — "QumulusAI Secures $500M Blockchain-Backed Facility via USD.AI" (2025-10-09): https://www.coindesk.com/business/2025/10/09/qumulusai-secures-usd500m-blockchain-backed-facility-to-scale-ai-compute-infrastructure
- CoinDesk — "USD.AI Bridges DeFi and AI by Turning Stablecoins Into Loans for Nvidia GPUs" (2025-10-24): https://www.coindesk.com/markets/2025/10/24/usdai-bridges-defi-and-ai-by-turning-stablecoins-into-loans-for-nvidia-gpus
- Stablewatch — "GPU-Backed Credit: How USD.AI Channels Onchain Capital": https://www.stablewatch.io/blog/usd-ai-deep-dive
- M0 Research — "USDai uses M0's stablecoin platform": https://research.m0.org/research/usdai-uses-m0s-stablecoin-platform-to-launch-composable-synthetic-dollar
- CoinGecko — USDai: https://www.coingecko.com/en/coins/usdai (June 2026 market data; April 2026 snapshot from CoinGecko top-1000 export 2026-04-09)
- Perplexity verification attempted 2026-06-10 (sonar; details cross-checked via web search)
