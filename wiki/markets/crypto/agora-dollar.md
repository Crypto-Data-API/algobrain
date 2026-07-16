---
title: "AUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["AUSD", "Agora Dollar", "Agora USD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://agora.finance/"
related: ["[[crypto-markets]]", "[[dai]]", "[[ethereum]]", "[[pyusd]]", "[[stablecoin]]", "[[stablecoins]]", "[[usdc]]", "[[usdt]]"]
---

# AUSD

**AUSD** (Agora Dollar) is a **fiat-collateralized US-dollar [[stablecoin]]** issued by **Agora**, minted 1:1 against USD fiat and pegged to 1 USD. Agora positions AUSD around **institutional-grade custody and oversight** — reserves safeguarded by a major global custodian bank, audited by a Big Four auditor, and managed by a top-tier fund manager — and emphasizes a **gas-optimized smart contract** for low-cost transfers. It is deployed across a wide range of chains including [[ethereum|Ethereum]], Solana, Sui, Base, Arbitrum, Avalanche, BNB Chain, and Polygon.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | AUSD |
| **Price** | $0.999874 |
| **Market cap** | $138.2M |
| **Market-cap rank** | #217 |
| **24h volume** | $20.53M |
| **24h change** | +0.02% |
| **Circulating supply** | 138.22M AUSD |
| **Total supply** | 138.22M AUSD |
| **All-time high** | $1.022 |
| **All-time low** | $0.950515 |

Circulating supply equals total supply (market-cap / FDV ≈ 1.00), consistent with a 1:1 fiat-backed mint-and-redeem model. AUSD held its peg tightly at the snapshot (~$0.9999) even against an Extreme-Fear tape (Fear & Greed 21; [[bitcoin|BTC]] ~$64,568).

> *Informational only, not investment advice. Fiat-backed stablecoins depend on the integrity and solvency of the issuer and its reserve partners.*

---

## Architecture — How It Works

AUSD is a **fiat-collateralized stablecoin** targeting a 1:1 USD peg, built on an **outsourced institutional reserve stack** rather than self-custody:

- **Issuance** — each AUSD is minted against USD fiat held in reserve. Agora's stated design relies on institutional infrastructure: reserves held at one of the world's largest **custodian banks**, audited by a **Big Four auditor**, and managed by a **top-tier fund manager**. Agora's role is the token/issuance front-end; the regulated reserve functions are delegated to those partners.
- **Backing** — reserves are intended to be **cash and cash-equivalents** (typically short-dated US [[treasuries|Treasuries]] / money-market-style instruments for fiat-backed issuers of this type), backing the full circulating supply 1:1. The reserve yield is the issuer's revenue model.
- **Redemption & peg mechanism** — authorized participants mint and redeem 1:1 with the issuer; **arbitrage** between the redemption price and the secondary-market price enforces the peg. If AUSD trades below $1, APs buy and redeem for $1; above $1, they mint and sell. (The historically wider ATL of $0.950515 vs a tighter recent band shows the secondary price has gapped from peg before, even with a 1:1 redemption backstop.)
- **Efficiency** — AUSD markets itself as cost-efficient to transact thanks to a **gas-optimized contract**, targeting traders and payments use cases; the wide multi-chain footprint supports settlement across ecosystems.

No specific named attestation document is included in the source data beyond the issuer's description of its auditor/custodian arrangement.

---

## Tokenomics & Supply

AUSD has **no fixed supply** — it expands and contracts with net mint/redeem demand, and circulating supply (138.22M) equals total supply (MC/FDV ≈ 1.00), each unit backed 1:1 by reserves. There is no separate governance or fee token; economics accrue to Agora via reserve yield on the cash-equivalents backing AUSD. Supply growth is a direct read on AUSD's adoption as a trading/settlement dollar across its ~18 supported ecosystems.

---

## Comparison vs Peer Fiat Dollars

| Stablecoin | Backing | Reserve oversight | Distribution edge | Notes |
|---|---|---|---|---|
| **AUSD** (this page) | Cash + cash-equivalents, 1:1 | Major custodian bank + Big Four auditor + top fund manager | Multi-chain (~18 chains), gas-optimized | Institutionally-positioned; mid-cap (~$138M) |
| **[[usdc]]** | Cash + short-dated Treasuries (Circle) | Regular attestations | Broad CEX/DeFi + Coinbase | Largest regulated fiat dollar; deep liquidity |
| **[[usdt]] (Tether)** | Mixed reserves (Tether) | Attestations (less granular) | Largest CEX footprint | Largest stablecoin by cap |
| **[[pyusd]] (PayPal USD)** | Fiat reserves (Paxos) | Regulated issuer (Paxos) | PayPal/Venmo rails | Consumer-brand fiat dollar peer |

AUSD competes directly with [[usdc]] and [[usdt]] on the **same fiat-reserve model**, differentiating on its explicitly institutional custody/audit framing and a broad, gas-optimized multi-chain footprint rather than on liquidity depth, where the incumbents dominate.

---

## How & Where It Trades / Is Used

AUSD has **comparatively healthy liquidity for its size** — ~$20.53M of 24h volume against a ~$138.2M cap, the highest volume-to-cap ratio of this stablecoin cohort. It trades on **centralized venues** (e.g. Kraken, AUSD/USD) and across **DEXs** (Uniswap V3 on Ethereum vs USDC, Orca on Solana). Its multi-chain footprint ([[ethereum|Ethereum]] contract `0x00000000efe302beaa2b3e6e1b18d08d69a9012a`, plus Solana, Sui, Base and others) supports use in **trading, lending, and payments** — Agora's intended positioning as a transactional/settlement dollar.

---

## Narrative, Category & Catalysts

- **Category:** institutionally-positioned, multi-chain fiat-backed stablecoin for trading, settlement, and payments.
- **Bull catalysts:** integrations adding AUSD as a quote/settlement asset on more venues; partnerships leveraging its institutional custody/audit story to win compliance-sensitive flow; multi-chain expansion deepening composability; reserve-yield-sharing arrangements with partners driving distribution.
- **Bear catalysts:** dominance of incumbent [[usdc]]/[[usdt]] liquidity; any lapse or delay in reserve attestations pressuring confidence; liquidity fragmentation across ~18 chains thinning individual-venue depth; tightening stablecoin reserve/disclosure regulation.

---

## History / Timeline

| Date | Event |
|---|---|
| (early trading) | All-time high **$1.022**; all-time low **$0.950515** — the secondary price has gapped several points below peg historically despite the 1:1 redemption model. |
| 2026-06-21 | Trades ~$0.999874, rank #217, ~$138.2M cap; tight peg, healthy ~$20.5M/24h volume. |

*Only events with on-page provenance are listed. The ATL of $0.950515 is a real recorded extreme; no precise dates for the ATH/ATL are in the wiki record, so they are described qualitatively.*

---

## Risks

- **De-peg risk** — generally tight, though the ATL of $0.950515 shows it has traded several points below peg historically; cross-chain representations add bridge risk on non-native chains.
- **Issuer / custodial risk** — backing depends on Agora and its custodian/auditor/fund-manager arrangements; holders rely on the integrity and solvency of those institutions and on timely redemption.
- **Reserve-transparency risk** — peg confidence hinges on ongoing, verifiable attestations; any gap or delay can pressure the secondary price.
- **Redemption-gating risk** — direct 1:1 redemption is available to authorized participants; retail holders depend on secondary liquidity, which can thin in stress.
- **Regulatory risk** — fiat-backed stablecoins face evolving reserve, disclosure, and licensing rules across jurisdictions.
- **Liquidity fragmentation** — supply spread across ~18 ecosystems can thin depth on individual venues despite solid aggregate volume.

In the current Extreme-Fear environment (Fear & Greed 21), institutionally-positioned fiat dollars like AUSD tend to be used as a settlement and risk-off asset.

---

## Trading / Usage Playbook

- **Use case:** AUSD works as a multi-chain trading/settlement dollar with an institutional reserve story; its solid volume-to-cap ratio makes it more usable for active trading than thinner small-cap stables in this cohort.
- **What to watch:** reserve-attestation cadence and any custodian/auditor changes; the AUSD secondary price vs $1 on each chain (bridge/de-peg signal); per-venue depth, since liquidity is fragmented across ~18 ecosystems; AUSD circulating supply as an adoption proxy.
- **Risk-off framing:** in Extreme Fear, AUSD's value is as a settlement/parking dollar — but verify which chain's representation you hold (native vs bridged) and prefer venues with the deepest AUSD depth to avoid slippage on size.

---

## Related

- [[stablecoin]] / [[stablecoins]] — category overview
- [[usdc]], [[usdt]] — fiat-backed peers
- [[pyusd]] — consumer-brand fiat-backed peer
- [[dai]] — decentralized, crypto-overcollateralized peer
- [[gusd|GUSD]], [[frax-usd|Frax USD]] — other USD stablecoin peers
- [[ethereum]], [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
