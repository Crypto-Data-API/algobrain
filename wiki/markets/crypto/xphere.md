---
title: "Xphere"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["XP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.x-phere.com/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[proof-of-work]]"]
---

# Xphere

**Xphere** (ticker **XP**) is a [[layer-1]] blockchain using a dual-chain architecture: a **PBFT-based Main Chain** for fast transaction processing paired with a **PoW-based Proof Chain** for validator selection. The design targets the scalability/security/decentralization trilemma by separating execution (BFT) from validator security ([[proof-of-work]]). It is a small-cap, relatively obscure L1 with limited exchange depth.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | XP |
| **Market Cap Rank** | #409 |
| **Market Cap** | $57.11M |
| **Current Price** | $0.020469 |
| **24h Volume** | $952.8K |
| **24h Change** | -7.98% |
| **7d Change** | -21.72% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: backdrop is an **Established Bear Market** with the Crypto Fear & Greed Index at **22 (extreme fear)**. XP is the weakest performer in this cohort at the snapshot — **down ~8% on the day and ~22% on the week** — a sharp drawdown consistent with a thin small cap unwinding into a risk-off tape. (This supersedes the earlier draft's stale +41%/+83% figures.)

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.79B XP |
| **Total Supply** | ~2.79B XP |
| **Max Supply** | 5.50B XP |
| **Fully Diluted Valuation (FDV)** | $57.11M |
| **Market Cap / FDV** | 1.00 |

The **MC/FDV ratio of 1.00** looks reassuring at first glance — circulating equals total supply, so market cap equals FDV today. **However, the max supply is 5.50B XP versus ~2.79B circulating**, meaning only ~51% of the eventual cap has been minted. Future emissions (block rewards under the PoW Proof Chain) can roughly double the supply over time, so the "no dilution" read from MC/FDV is misleading — **dilution risk against max supply is material**. New issuance accrues to PoW miners/validators.

### Value accrual & governance

XP is the gas and security asset of the chain. Value accrues through **transaction fees** on the PBFT Main Chain and **block rewards** that pay PoW miners/validators on the Proof Chain. The critical nuance is that, unlike a fully-minted PoS token, XP's security budget is funded by *ongoing emission* toward the 5.5B cap — so holders face continuous dilution that is only offset if fee demand and price appreciation outpace new issuance. There is no large VC/team unlock cliff here (supply ≈ total today), but there is a steady inflationary drip via PoW rewards. Governance is not the headline feature; the design emphasis is on the consensus split rather than on-chain token governance.

---

## How & Where It Trades

**Spot venues:** liquidity is limited. The CoinGecko snapshot surfaced no major centralised-exchange pair as a primary market for XP; trading concentrates on smaller venues. Verify available pairs before trading.

**Derivatives:** No major perpetual/futures market is listed for XP — effectively **no perp**. This is a spot-only, low-depth asset.

**Liquidity read:** ~$953K of 24h volume against a ~$57M cap is a turnover near **1.7%** — low. Combined with the day's -8% move, slippage and gap risk are elevated.

---

## Technology & Consensus

Xphere uses a **dual-chain design**:

- **Main Chain (PBFT)** — a Practical Byzantine Fault Tolerant chain for fast, final transaction processing.
- **Proof Chain ([[proof-of-work]])** — secures validator selection via PoW, anchoring the BFT layer in computational security.

The stated goal is to balance throughput (from BFT) with decentralized, attack-resistant validator selection (from PoW), addressing the blockchain trilemma. CoinGecko categories: Layer 1 (L1), Proof of Work (PoW).

### Why split the chains?

The intuition behind the dual-chain design: classical **[[byzantine-fault-tolerance|PBFT]]** gives fast, deterministic finality but only works well with a *known, bounded* validator set — pick the wrong validators and you get either centralization or vulnerability to Sybil attacks. Pure **[[proof-of-work|PoW]]** is permissionless and Sybil-resistant but slow to finalize and energy-heavy. Xphere's answer is to use PoW *only to select/weight validators* (the Sybil-resistant, hard-to-fake part) while running actual transaction ordering and finality through fast PBFT on the Main Chain. In principle this captures BFT speed with PoW's open, attack-resistant membership. The trade-offs to verify in practice: how validators are rotated, how the two chains stay in sync, how much hashpower actually secures the Proof Chain (a thinly-mined PoW chain is cheap to 51%-attack), and how decentralized the BFT validator set really is.

---

## Comparison vs competitor chains

Xphere is a small-cap, general-purpose L1 competing on consensus design. Its peers are other throughput-focused or hybrid-consensus L1s.

| Chain | Consensus | Scale | Differentiator vs Xphere |
|---|---|---|---|
| **Xphere (XP)** | Dual-chain: PBFT main + PoW proof | Small-cap (~$57M) | PoW-for-validator-selection + BFT-for-finality hybrid; Korean-linked |
| **[[solana\|Solana]] (SOL)** | PoH + PoS (Tower BFT) | Mega-cap | Single high-throughput chain, huge ecosystem; no PoW |
| **[[bnb\|BNB Chain]]** | PoS (BFT-style) | Mega-cap | Massive liquidity/users; centralized validator set |
| **Kaspa (KAS)** | PoW (GHOSTDAG / blockDAG) | Large-cap | Pure-PoW high-throughput via DAG; different security/decentralization profile |

The honest read: Xphere's consensus story is genuinely differentiated, but consensus novelty alone rarely wins. It competes for the same general-purpose smart-contract demand as far larger, more liquid, more developed L1s, and must prove real ecosystem usage — which market data does not yet show.

---

## Use Case, Narrative & Category

The narrative is a **trilemma-solving hybrid L1** (BFT speed + PoW security) aimed at developers and enterprises seeking a general-purpose smart-contract platform. It competes in a crowded field of small-cap L1s and must demonstrate real ecosystem usage to differentiate. It carries an Asian (Korean-linked) project profile based on its community channels.

### Catalysts

Plausible **positive catalysts**: a major CEX listing (XP currently lacks deep CEX coverage), demonstrable ecosystem/dApp activity, Korean-market retail interest (a historically strong driver for Korean-linked tokens), or a broad rotation back into alt-L1 narratives. **Negative catalysts**: continued PoW emission diluting holders, persistent thin liquidity, failure to attract developers, and small-cap-L1 narrative fatigue.

---

## Notable History

- All-time high around **$0.069 (Mar 2025)**; XP now trades ~75–85% below that peak depending on the day.
- Sharp recent volatility: large positive prints earlier in 2026 have reversed into a steep -22% weekly drawdown at this snapshot — characteristic of a thin, momentum-driven small cap.

---

## Risks

- **Hidden dilution:** MC/FDV = 1.00 masks a max supply nearly **2x** the current circulating — substantial future PoW emissions.
- **Liquidity risk:** ~$953K/day volume, no derivatives, limited CEX depth — high slippage and gap risk.
- **Volatility:** -8% in a day and -22% in a week shows how fast XP can move against holders.
- **Adoption uncertainty:** the dual-chain trilemma pitch is shared by many L1s; real traction is unproven from market data.
- **Macro:** small-cap L1 into an Established Bear Market with extreme-fear sentiment (F&G 22).
- **51% / security-budget risk:** a thinly-mined PoW Proof Chain is cheaper to attack; the real cost of attacking validator selection should be weighed, not assumed safe.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

Context as of 2026-06-23: market-wide **Extreme Fear** (F&G 21), transitional **bottoming/accumulation** regime, BTC ~16% below its 200-day MA.

- **Character:** XP is the weakest performer in this cohort at the snapshot (-8% day, -22% week), spot-only, with low CEX depth and ~$1M/day turnover. This is a thin, momentum-driven micro-cap — the highest-slippage, highest-gap-risk profile in the group.
- **Default stance:** avoid chasing weakness *and* avoid catching the falling knife. With no perp to hedge and thin spot depth, position management is hard; capital preservation dominates.
- **If trading it:** treat as a small, speculative allocation only. Use limit orders, expect wide spreads, and assume you cannot exit size quickly. The steep -22% week shows how fast XP gaps against holders.
- **Invalidation / view change:** a broad regime flip out of Extreme Fear *plus* a liquidity catalyst (major CEX listing) and/or visible ecosystem traction. Absent improved liquidity, the structural illiquidity makes XP unattractive for anything but a tiny lottery-ticket size.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[proof-of-work]]
- [[byzantine-fault-tolerance]]
- [[solana]] · [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko bulk endpoints).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XP |
| **Market Cap Rank** | #435 |
| **Market Cap** | $49.99M |
| **Current Price** | $0.0176 |
| **Categories** | Layer 1 (L1), Proof of Work (PoW) |
| **Website** | [https://www.x-phere.com/](https://www.x-phere.com/) |

---

## Overview

Xphere revolutionizes blockchain technology by addressing the trilemma of scalability, security, and decentralization through an innovative dual-chain architecture. By combining a PBFT-based Main Chain for efficient and rapid transaction processing with a PoW-based Proof Chain for secure validator selection, Xphere achieves an optimized balance of trust, performance, and decentralization. This ecosystem fosters innovation, accessibility, and sustainability for individuals, developers, and enterprises worldwide.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.85B XP |
| **Total Supply** | 2.85B XP |
| **Max Supply** | 5.50B XP |
| **Fully Diluted Valuation** | $49.99M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0795 (2026-05-16) |
| **Current vs ATH** | -77.90% |
| **All-Time Low** | $0.00298093 (2025-12-26) |
| **Current vs ATL** | +489.51% |
| **24h Change** | -1.90% |
| **7d Change** | +29.38% |
| **30d Change** | -23.84% |
| **1y Change** | +20.36% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.x-phere.com/](https://www.x-phere.com/) |
| **Twitter** | [@Xphere_official](https://twitter.com/Xphere_official) |
| **Telegram** | [Xphere_official](https://t.me/Xphere_official) (43,141 members) |
| **Whitepaper** | [https://docs.x-phere.com/whitepaper/](https://docs.x-phere.com/whitepaper/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $499,963.00 |
| **Market Cap Rank** | #435 |
| **24h Range** | $0.0175 — $0.0179 |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
