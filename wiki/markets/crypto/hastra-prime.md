---
title: "PRIME (Hastra)"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi, altcoins]
aliases: ["PRIME", "Hastra PRIME", "Hastra"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://hastra.io/"
related: ["[[crypto-markets]]", "[[solana]]", "[[figure-heloc]]", "[[real-world-assets]]", "[[rwa]]", "[[private-credit]]", "[[kamino]]", "[[chainlink]]", "[[stablecoin-yields]]"]
---

# PRIME (Hastra)

**PRIME** (ticker **PRIME**) is the yield-bearing liquid-staking token of **Hastra**, a [[solana|Solana]] [[real-world-assets|RWA]] protocol that channels yield from **Figure's (Nasdaq: FIGR) Democratized Prime HELOC lending pools** on-chain (see [[figure-heloc]]). Holders earn up to ~8% APY from real consumer-lending interest spreads — not token emissions — making PRIME one of the more credible "real yield from real-world assets" instruments on Solana and a building block of the 2025–2026 RWA narrative.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | PRIME |
| **Chain** | [[solana|Solana]] (via Provenance RWA framework) |
| **Current Price** | $1.043 (≈ $1 + accrued yield NAV) |
| **Market Cap** | $391,482,467 |
| **Market Cap Rank** | #119 |
| **Fully Diluted Valuation** | $391,482,467 |
| **24h Volume** | $1,527,931 |
| **24h Range** | $1.043 — $1.043 |
| **24h Change** | -0.01% |
| **7d Change** | +0.10% |
| **Categories** | Solana Ecosystem, Liquid Staking, [[real-world-assets|RWA]] |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

PRIME trades **flat at ~$1.04** — by design it tracks $1 plus accrued yield, so day-to-day price moves are near zero (24h range $1.043–$1.043). Market cap grew from ~$358M (April) to ~$391M (June), reflecting **net new deposits**. Macro backdrop: crypto [[fear-and-greed-index|Fear & Greed]] ~**23 (Extreme Fear)**, **Established Bear Market** — but a NAV-accruing yield token is largely insulated from sentiment; the relevant risk is credit, not beta.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PRIME |
| **Issuer / protocol** | Hastra (Solana RWA protocol) |
| **Yield** | Up to ~8% APY from tokenized HELOC interest spreads; no lock-up, non-rebasing |
| **Mechanism** | Swap USDC → wYLDS (wrapped Figure YLDS, an SEC-registered yield-bearing stablecoin) → stake to mint PRIME |
| **Underlying** | Figure Technology (Nasdaq: FIGR) — $17B+ cumulative loan originations, >$1B/month by Dec 2025 |
| **Chain** | Solana (via the Provenance Blockchain Foundation RWA framework) |
| **Categories** | Solana Ecosystem, Liquid Staking, RWA |
| **Website** | [https://hastra.io/](https://hastra.io/) |

---

## Mechanism & Backing

| Dimension | Detail |
|---|---|
| **Underlying asset** | Figure's **Democratized Prime HELOC lending pools** — tokenized US home-equity consumer loans (see [[figure-heloc]]). |
| **Yield source** | The interest spread on those HELOC pools — *real-world lending income*, not token emissions or trading rewards. Quoted up to ~8% APY (qualitative; rate is variable, not contractual). |
| **NAV / accrual** | Non-rebasing: PRIME's unit price accretes toward $1 + accrued yield rather than minting new units; secondary price should hug NAV. |
| **Minting path** | USDC → **wYLDS** (wrapped Figure **YLDS**, an SEC-registered yield-bearing stablecoin backed by treasury securities) → stake to mint PRIME. Burning PRIME unwinds the chain back to USDC. |
| **Custody / compliance** | Backed by Figure's audited, SEC-regulated lending operations with transparent collateral; wYLDS wraps a registered security. |
| **Composability / permissioning** | PRIME is freely composable across Solana DeFi ([[kamino|Kamino]], [[raydium|Raydium]], [[jupiter-exchange-solana|Jupiter]]); the entry ramp (wYLDS) involves a registered-security wrapper, so regulatory treatment is the open question. |
| **Regulatory wrapper** | Liquid-staking token over a registered-stablecoin/RWA stack; not itself marketed as a registered security, but its plumbing depends on one. |

> The ~8% APY is qualitative and variable — it is a function of HELOC spreads and is not a guaranteed rate. Do not treat it as fixed.

---

## Overview

Hastra is a decentralized protocol on Solana that bridges institutional-grade real-world assets (RWAs) with DeFi. The protocol tokenizes access to Figure's loan portfolio — a publicly-traded, SEC-regulated financial services company with over $17 billion in loan originations — enabling users to earn sustainable yields backed by real consumer lending operations.

The Hastra ecosystem features two primary yield-bearing tokens: **wYLDS**, a wrapped version of Figure's SEC-registered stablecoin backed by treasury securities, and **PRIME**, a liquid staking token that earns yield from Figure's Democratized Prime HELOC lending pools. Both tokens are fully composable across Solana DeFi protocols like [[kamino|Kamino]], [[raydium|Raydium]], and [[jupiter-exchange-solana|Jupiter]]. Unlike traditional DeFi yield that relies on token emissions or speculative trading, Hastra delivers real yields from audited, real-world lending operations with transparent underlying collateral and regulatory compliance.

---

## Major News & Events (2025–2026)

- **4 Dec 2025** — Figure and leading crypto partners launched an **RWA consortium for on-chain finance on Solana**, with PRIME as a flagship asset and **$19B+ of loans referenced on-chain** (Figure investor release).
- **Late 2025 / 2026** — Hastra integrated **[[chainlink|Chainlink]]** infrastructure to support its yield products, amid $19B+ equity backing from Figure.
- **2026** — PRIME listed/integrated on **Kamino**, Solana's main lending market, extending composability (collateralized borrowing against PRIME).
- **Q1 2026 price action** — ATH $1.50 (11 Mar 2026), ATL $0.9564 (17 Mar 2026): a sharp premium build-and-collapse within a week. As an accruing-yield token PRIME should trade near accrued NAV; the March spike was speculative.
- Figure's lending ops exceeded **$1B in monthly originations** as of December 2025.

---

## Market Structure

- **Where it trades**: Solana DEXs ([[raydium|Raydium]]/[[jupiter-exchange-solana|Jupiter]] routing) and within Hastra/[[kamino|Kamino]]; no major CEX listing as of the June 2026 snapshot. On-chain volume ~$1.5M/day (June 2026), down from ~$3.5M/day in April.
- **Who can hold it**: Solana wallet holders can hold/transfer PRIME freely; the *minting* ramp (USDC → wYLDS → PRIME) touches a registered-security wrapper and is the compliance-gated step.
- **Liquidity caveats**: as a NAV token, secondary liquidity is shallow and primarily exists to let holders enter/exit near NAV; large redemptions route through the wYLDS unwind, not a deep order book.

### What it is for traders
1. **Stablecoin-adjacent carry** — ~8% APY from HELOC spreads with daily liquidity ([[stablecoin-yields]] comp).
2. **RWA-narrative basket exposure tied to a listed equity (FIGR)** — an unusual crypto-equity linkage; Figure news moves the credibility of PRIME's yield.
3. **Collateral** in Solana money markets (Kamino integration).

---

## Category Context

PRIME is a **tokenized private-credit / liquid-staking** RWA token on Solana — the on-chain, retail-composable expression of the same Figure HELOC engine that backs the much larger [[figure-heloc]] registry. Narrative basket: RWA / tokenized [[private-credit]] (comps: Ondo, Maple, [[janus-henderson-anemoy-aaa-clo-fund|JAAA]]).

### Peer table — RWA yield tokens

| Token | Underlying | Yield source | Chain | Trades like |
|---|---|---|---|---|
| **PRIME (Hastra)** | Figure HELOC spreads | Consumer lending interest | Solana | NAV ~$1 + accrual |
| [[janus-henderson-anemoy-aaa-clo-fund\|JAAA]] | AAA [[clo\|CLO]] tranches | Floating credit yield | Multichain | NAV ~$1, near-zero vol |
| [[figure-heloc\|FIGR_HELOC]] | Tokenized HELOCs | Loan interest accrual | Provenance | Loan registry (not tradeable) |
| ONDO (USDY) | Treasuries/credit | T-bill + credit yield | Multichain | NAV ~$1 |

---

## Risks

- **NAV-premium episodes** — Mar 2026 showed ±40% swings around $1 (ATH $1.50, ATL $0.96 within a week); speculative spikes detach price from accrued NAV. Buy the premium and you lose it.
- **Credit risk** in the underlying HELOC pools — a US housing/consumer-credit downturn hits the yield and could impair principal.
- **Single-originator concentration** — *all* yield flows from Figure; idiosyncratic Figure risk is PRIME risk.
- **Regulatory** — treatment of the wrapped SEC-registered stablecoin (YLDS/wYLDS) and the liquid-staking wrapper is the key open question.
- **Liquidity** — shallow secondary depth; exits in stress route through the wYLDS unwind.

---

## Tokenomics

| Metric | Value (2026-06-21 snapshot) |
|---|---|
| **Circulating Supply** | 375.30M PRIME |
| **Total Supply** | 375.30M PRIME |
| **Max Supply** | Unlimited (minted/burned against wYLDS staking) |
| **Market Cap / FDV Ratio** | 1.00 |

Supply rose from ~348.35M (April) to ~375.30M (June), i.e. **net new deposits** of ~27M PRIME — the cleanest read on adoption of the product.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.50 (2026-03-11) |
| **All-Time Low** | $0.9564 (2026-03-17) |
| **Current vs ATH** | -30.46% (premium fully unwound; back to NAV) |
| **Current vs ATL** | +9.06% |
| **Behavior** | Tracks ~$1 + accrued yield; March 2026 showed a speculative premium spike and collapse — June 2026 sits at ~$1.04 NAV |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `3b8X44fLF9ooXaUm3hhSgjpmVs6rZZ3pPoGnGahc3Uu7` |

---

## Exchange Listings

On-chain only as of the April 2026 snapshot: Solana DEX routing (Raydium/Jupiter) and Kamino money-market integration. No major CEX listings in CoinGecko data.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hastra.io/](https://hastra.io/) |
| **Twitter** | [@HastraFi](https://twitter.com/HastraFi) |

---

## Related

- [[figure-heloc]] — the underlying lending machine
- [[solana]], [[kamino]], [[raydium]], [[jupiter-exchange-solana]]
- [[real-world-assets]], [[rwa]], [[private-credit]], [[stablecoin-yields]], [[chainlink]]
- [[janus-henderson-anemoy-aaa-clo-fund]] — peer RWA yield token
- [[crypto-markets]], [[defi]]

---

## Sources

- Market data: cryptodataapi.com / CoinGecko top-1000 snapshot, 2026-06-21
- CoinGecko market data snapshot, 2026-04-09 (CoinGecko top-1000 ingest)
- Hastra — https://hastra.io/
- Figure investor release, "Figure and Leading Crypto Partners Launch RWA Consortium for Onchain Finance on Solana" (2025-12-04) — https://investors.figure.com/news-releases/news-release-details/figure-and-leading-crypto-partners-launch-rwa-consortium-onchain
- StockTitan, "Figure (Nasdaq: FIGR) leads Solana RWA push with PRIME, $19 billion loans on-chain" — https://www.stocktitan.net/news/FIGR/figure-and-leading-crypto-partners-launch-rwa-consortium-for-onchain-x91xuyfunadt.html
- Phemex News, "PRIME RWA Asset Debuts on Solana's Kamino" — https://phemex.com/news/article/prime-rwa-asset-launches-on-solanas-kamino-platform-42393
- Cryptonews, "Hastra Taps Chainlink to Support Yield Products Amid $19B+ Equity Backing From Figure" — https://cryptonews.net/news/defi/32030810/
- Verified via web search, 2026-06-10: ~8% APY HELOC yield, wYLDS→PRIME staking mechanics, Figure $1B+/month originations Dec 2025, Kamino listing
