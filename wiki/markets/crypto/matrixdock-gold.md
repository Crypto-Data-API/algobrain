---
title: "Matrixdock Gold"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [commodities, crypto, gold, real-world-assets]
aliases: ["XAUM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.matrixdock.com/xaum"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[gold]]", "[[pax-gold]]", "[[real-world-assets]]", "[[tether-gold]]"]
---

# Matrixdock Gold

**Matrixdock Gold** (ticker **XAUm**) is a tokenized physical [[gold]] product: each token is backed **1:1 by one troy ounce of fine, high-grade, LBMA-certified gold** held in secure vaults. It is issued by **Matrixdock** (the RWA arm of **Matrixport**) and deployed as a multi-chain token (ERC-20 / BEP-20 and more) across [[ethereum|Ethereum]], BNB Chain, Sui, and Plume Network. XAUm is a [[real-world-assets|real-world asset]] (RWA) whose on-chain price tracks the **gold spot price per troy ounce** (spot XAU), giving 24/7 on-chain exposure to physical bullion. Note: XAUm is **not** [[tether-gold]] (XAUT) — it is a distinct issuer and product.

## Market Data

| Field | Value |
|---|---|
| **Ticker** | XAUm |
| **Market Cap Rank** | #383 |
| **Current Price** | $4,085.70 |
| **Market Cap** | $63.5M |
| **24h Volume** | $200,914 |
| **24h Change** | -0.10% |
| **Circulating Supply** | 15,367 XAUM |
| **Total Supply** | 15,367 XAUM |
| **All-Time High** | $5,574.96 |
| **All-Time Low** | $2,563.55 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The ~$4,086 token price corresponds to the **spot price of one troy ounce of gold** (each XAUm = 1 oz), so the token moves with the bullion market rather than crypto beta. The wide ATH ($5,575) to ATL ($2,564) range mirrors gold's own multi-year price swings. Circulating supply (~15,367 tokens) directly represents ~15,367 ounces of vaulted gold; supply equals total supply, matching backing.

---

## Mechanism & backing (how it works)

- **Underlying asset.** Physical gold — **one troy ounce** of fine-weight, high-grade, **LBMA-certified** bullion per token (gold bars produced by London Bullion Market Association "Good Delivery" refiners). Total token supply always matches the underlying vaulted gold holdings, so on-chain supply maps 1:1 to physical ounces.
- **Wrapper / issuer.** Matrixdock issues XAUm as a redeemable token representing direct ownership of **allocated** physical gold — i.e. specific, segregated bars rather than an unsecured claim on a pool, which limits commingling/rehypothecation risk.
- **Vaulting / custody.** Gold is held in reputable, high-security professional vaults under Matrixdock's custody arrangements; reserves are designed to be **auditable** so the chain supply can be reconciled against physical ounces.
- **Redemption.** Token holders can redeem XAUm for the underlying **physical gold** (subject to minimums, fees, and logistics) or sell on secondary markets. This physical redeemability is the arbitrage anchor that keeps the token tied to spot gold: if XAUm trades rich to spot, participants mint/sell; if cheap, they buy/redeem.
- **Mint / redeem & KYC gating.** Primary mint/redeem against physical gold and large-size transactions typically require **KYC/AML** through Matrixdock, though XAUm trades more openly on secondary venues than the fully permissioned tokenized-fund products in the RWA cohort.

### How tracking actually holds

XAUm is designed to track **spot XAU per ounce**. On-chain price can deviate slightly from spot due to liquidity, fees, and arbitrage friction — and, importantly, because crypto venues trade 24/7 while the LBMA/COMEX gold market closes, the token continues to print prices over weekends and holidays when there is no live spot reference. Redeemability for physical gold plus primary mint/redeem arbitrage is what pulls it back toward spot when the traditional market reopens.

---

## Comparison vs peer tokenized-gold products

| Token | Backing | Issuer | Unit | Redemption | Notes |
|---|---|---|---|---|---|
| **XAUm** | 1 troy oz LBMA gold, allocated | Matrixdock (Matrixport) | 1 token ≈ 1 oz | Physical redemption (KYC) | Multi-chain (ETH, BNB, Sui, Plume); CEX + DEX listed |
| [[pax-gold]] (PAXG) | 1 troy oz LBMA gold, allocated (Brink's, London) | Paxos (NYDFS-regulated) | 1 token ≈ 1 oz | Physical (allocated bars) + cash | Most established; regulated issuer; deep liquidity |
| [[tether-gold]] (XAUT) | 1 troy oz gold (Swiss vault) | TG Commodities (Tether) | 1 token ≈ 1 oz | Physical (Switzerland) | Large; less granular public attestation than PAXG |

All three are 1-ounce, allocated, LBMA-gold tokens, so they track the same underlying. The practical differentiators are **issuer/regulatory profile** (Paxos is NYDFS-regulated; Tether and Matrixport are offshore), **liquidity and venue depth** (PAXG is the most liquid), and **chain footprint** (XAUm is the most multi-chain of the three: ETH, BNB Chain, Sui, Plume). For a buyer, the choice is largely a trade-off between counterparty trust and where on-chain liquidity sits.

---

## How / where it trades

- **Primary market.** Mint/redeem with Matrixdock against physical gold for KYC'd participants.
- **Secondary market.** Centralized-exchange listing (e.g. **KuCoin** XAUM/USDT) plus on-chain DEX liquidity (e.g. a Uniswap V3 XAUM/USDT pool on [[ethereum|Ethereum]]). Secondary volume (~$0.2M/24h) is modest but more active than the permissioned fund tokens in the RWA cohort.
- **Hours.** The token transfers and trades **24/7** on-chain and on crypto exchanges, even when the traditional gold market (LBMA / COMEX) is closed — giving continuous price discovery against gold, with the caveat that off-hours prints can gap when spot reopens.
- **Composability.** As an ERC-20/BEP-20 across several chains, XAUm can serve as gold-denominated collateral or an LP asset on-chain — a use case physical bars and most ETFs cannot offer.

---

## Narrative & category

XAUm sits in the **tokenized-gold / RWA store-of-value** category — bringing the oldest macro hedge on-chain. The broader narrative is twofold: (1) **RWA tokenization** moving real assets (Treasuries, gold, credit) onto public chains, and (2) **gold as a macro hedge** in an era of fiscal and geopolitical stress. In the current backdrop, gold has been a strong macro hedge and tokenized-gold tracks spot XAU; the crypto market itself is in "Extreme Fear" (Fear & Greed 21 as of 2026-06-22, bottoming/accumulation), which is precisely the regime where a non-correlated, risk-off bullion proxy is most attractive inside a crypto portfolio. Catalysts: rising gold spot, growth of on-chain RWA rails, and integrations that let XAUm be used as collateral/settlement on its deployed chains.

---

## History / timeline

- **Issuance** — XAUm launched as Matrixdock's (Matrixport RWA arm) tokenized-gold product, each token backed by one troy ounce of LBMA-certified vaulted gold.
- **Multi-chain expansion** — deployed across [[ethereum|Ethereum]], BNB Chain, Sui, and Plume Network (addresses below), broadening on-chain reach.
- **All-time high $5,574.96 / all-time low $2,563.55** — the historical band reflects gold's own multi-year swing; the token tracks bullion, not crypto sentiment (exact dates not in the snapshot, so not asserted).
- **2026-06-21** — snapshot: ~$4,086 (≈ spot gold/oz), ~$63.5M market cap, ~15,367 oz backing, ~$0.2M/24h secondary volume, rank #383.

---

## Risks

- **Issuer / custodial risk.** Reliance on Matrixdock and its vaulting/custody arrangements. If the gold is not fully allocated, audited, or recoverable, the 1:1 backing is impaired — the central tail risk for any tokenized-gold product, and the main reason issuer trust/regulatory profile matters.
- **NAV-gap / tracking & liquidity risk.** Thin secondary liquidity can cause price gaps versus spot, particularly during volatile sessions, over weekends when the gold market is closed, or when crypto and gold markets diverge.
- **Redemption friction.** Converting tokens to physical bullion involves minimums, fees, KYC, and logistics; not all holders can practically redeem, which weakens the arbitrage anchor at small size.
- **Regulatory risk.** Tokenized commodities face evolving regulation across jurisdictions, which can affect issuance, custody, or who may hold the token.
- **Smart-contract / bridge risk.** Multi-chain deployment (Ethereum, BNB Chain, Sui, Plume) broadens the smart-contract and bridge attack surface.
- **Market risk (gold beta).** Full exposure to gold price moves — XAUm fell from a ~$5,575 ATH to ~$4,086, a roughly 27% drawdown tracking bullion's decline. Gold can and does fall.
- **Macro backdrop.** As of 2026-06-22 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads 21 ("Extreme Fear"). Tokenized gold is often used as a non-correlated, risk-off store of value within crypto portfolios, though its price is driven by the gold market, not crypto sentiment.

---

## Trading / usage playbook

- **Use it as a crypto-portfolio gold sleeve.** XAUm gives on-chain, 24/7 spot-gold exposure that can be held alongside crypto and used as collateral — a diversifier that does not move with crypto beta.
- **Mind weekend/after-hours gaps.** Because crypto trades when the gold market is closed, avoid treating off-hours XAUm prints as a live spot reference; expect convergence/gaps when LBMA/COMEX reopen.
- **Choose the venue/chain with liquidity.** Secondary depth is modest (~$0.2M/24h); for size, the KuCoin pair or primary mint/redeem is preferable to a thin DEX pool to limit slippage.
- **Counterparty-weigh against PAXG/XAUT.** If issuer/regulatory trust is the priority, [[pax-gold]] (regulated issuer, deepest liquidity) is the benchmark; pick XAUm where its multi-chain footprint or specific venue access is the deciding factor.

---

## Platform & chain information

**Deployment:** Multi-chain ([[ethereum|Ethereum]], BNB Chain, Sui, Plume Network)

| Chain | Address |
|---|---|
| Ethereum | `0x2103e845c5e135493bb6c2a4f0b8651956ea8682` |
| Plume Network | `0xa0c4f78a29ead4abf6b7f5b3f0d05c0f3eab8ddf` |
| Sui | `0x9d297676e7a4b771ab023291377b2adfaa4938fb9080b8d12430e4b108b836a9::xaum::XAUM` |
| BNB Chain | `0x23ae4fd8e7844cdbc97775496ebd0e8248656028` |

---

## See Also

- [[gold]] — underlying asset
- [[real-world-assets]] / [[rwa]]
- [[pax-gold]], [[tether-gold]] — peer tokenized-gold products
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

