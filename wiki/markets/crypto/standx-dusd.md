---
title: "StandX DUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["DUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://standx.com/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[ethena-usde]]", "[[solana]]", "[[stablecoins]]", "[[usde]]"]
---

# StandX DUSD

**StandX DUSD** (ticker DUSD) is a yield-bearing dollar stablecoin issued by **StandX**, a decentralized perpetual-futures exchange, deployed on **[[bnb|BNB Chain]]** and **[[solana|Solana]]**. It targets a peg of **1 DUSD ≈ US$1**. DUSD is StandX's first product and is designed so that holders earn yield on idle balances and trading margin — **yield is auto-distributed to holders without a separate staking step**, making DUSD simultaneously a savings dollar and trading collateral on the StandX perp DEX.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | DUSD |
| **Price** | $0.997531 |
| **Peg target** | US$1.00 |
| **Market cap** | $100.38M |
| **Market-cap rank** | #269 |
| **24h volume** | $686,819 |
| **24h change** | -0.12% |
| **Circulating supply** | 100.64M DUSD |
| **Total supply** | 100.64M DUSD |
| **All-time high** | $1.039 (2025-11-21) |
| **All-time low** | $0.96504 (2025-11-21) |

DUSD held its peg closely at the snapshot (~$0.9975). Both ATH and ATL were recorded on 2025-11-21, indicating a volatile launch day followed by stabilization.

---

## Architecture & how it works

DUSD is described as a **fully collateralized, yield-bearing stablecoin** that **auto-distributes real yield to holders — no staking needed.** This rebasing/auto-distribution design differs from the stake-for-yield model used by peers like Aster's USDF (asUSDF) or Avant's savUSD: DUSD holders accrue yield simply by holding.

- **Collateral / reserve model:** StandX states DUSD is **fully collateralized.** As the native margin asset of a perp DEX, the collateral pool is deployed to generate returns while backing the token. The exact composition is set by StandX and not itemised in the CoinGecko snapshot, but for a perp-DEX margin dollar it is typically a mix of stablecoins and crypto deployed into market-neutral strategies.
- **Peg / stability mechanism:** Full collateralization plus mint/redeem against the collateral pool. Because yield auto-distributes, the token is designed to track $1 with returns accruing on top (via rebasing of balance rather than price drift) — though the CoinGecko price is quoted around $1.00, consistent with a balance-rebasing rather than price-appreciating design.
- **Mint / redeem & gating:** Handled through the **StandX protocol** against the collateral pool; secondary exit is via on-chain liquidity on BNB Chain and Solana. Primary redemption depends on StandX honouring redemptions at $1 from the collateral pool.
- **Yield source & distribution:** "Real yield" generated from the protocol's **deployment of collateral** — for a perp-DEX margin dollar this typically includes **funding-rate / basis income** and other market-neutral strategies, the same broad source as [[ethena-usde]] / [[usde]]. Yield is **auto-distributed to all holders**, including traders earning on their **margin balances** while positions are open.

---

## Tokenomics & supply

Circulating and total supply are essentially equal at ~**100.6M DUSD** — no meaningful locked overhang. Supply tracks the size of the StandX collateral pool (deposits as margin/savings). Because yield is auto-distributed, holders' balances grow over time even though the unit price stays near $1; supply figures therefore reflect both deposits and accrued distributions. No fixed max supply applies — issuance is elastic to deposits.

---

## Comparison vs peers

| Token | Issuer | Yield delivery | Backing | Primary use |
|---|---|---|---|---|
| **DUSD** | StandX (perp DEX) | **Auto-distributed (no staking)** | Fully collateralised, deployed | Margin + savings dollar |
| [[astherus-usdf\|asUSDF]] | Aster (perp DEX) | Stake-for-yield | Collateral-deployed | Margin + savings |
| [[usde\|USDe]] | Ethena | Stake (sUSDe) | Delta-neutral hedge | Yield dollar |
| [[usdc]] | Circle | None (base) | Fiat reserves | Settlement |

DUSD's differentiator versus its closest peer ([[astherus-usdf|asUSDF]]) is the **no-staking, auto-distribution** mechanic — holders and active traders earn without an extra step. The trade-off is that any backing shortfall is shared *immediately* across all holders rather than isolated to a staked tranche.

---

## How and where it trades & is used

DUSD is concentrated in the **StandX venue** and its host chains (BNB Chain, Solana); CoinGecko shows no major external centralized-exchange listings. Reported 24h volume of ~$687K against a ~$100M market cap is the **healthiest turnover of this peer set** but still modest, reflecting use mainly as **in-app margin and savings collateral** rather than cross-venue trading. The dual-chain deployment broadens reach but also splits liquidity.

Contract addresses:

| Chain | Address |
|---|---|
| BNB Chain | `0xaf44a1e76f56ee12adbb7ba8acd3cbd474888122` |
| Solana | `DUSDt4AeLZHWYmcXnVGYdgAzjtzU5mXUVnTMdnSzAttM` |

---

## Narrative, category & catalysts

DUSD belongs to the **perp-DEX yield-dollar** category — stablecoins issued by decentralized derivatives venues that monetise their collateral (alongside Aster's asUSDF and Ethena-adjacent designs). Catalysts: (1) growth of StandX trading volume, which drives funding-rate income and thus DUSD yield; (2) the auto-distribution UX attracting savings deposits; (3) cross-chain liquidity deepening. The narrative risk is that perp-DEX yield is procyclical — it shrinks (or turns negative) in low-volume, negative-funding regimes like the current Extreme-Fear backdrop.

---

## History / timeline

- **2025-11-21** — Launch day. Both the all-time high (**$1.039**) and all-time low (**$0.96504**) were recorded the same day — a ~±4% launch-day swing around peg before stabilising. This is a real, dated launch-day dislocation, not a later de-peg.
- **2026-06-21** — Snapshot: ~$0.9975, on peg, $100.38M cap, rank #269; ~$687K 24h volume (best turnover of the peer set).

---

## Risks

- **De-peg risk:** DUSD dipped to ~$0.965 on its launch day (2025-11-21); thin external liquidity and the current "Extreme Fear" backdrop (crypto Fear & Greed ~21) keep de-peg risk relevant.
- **Strategy / collateral risk:** "real yield" depends on the protocol's collateral-deployment strategies; losses there impair both yield and backing. Auto-distribution also means any backing shortfall is **shared across all holders immediately** rather than isolated to a staked tranche.
- **Yield-source / counterparty risk:** funding-rate / basis income from perp markets is procyclical and can turn negative in low-volume bear regimes; the yield (and the collateral generating it) is exposed to derivatives-venue counterparties.
- **Counterparty / venue risk:** as a perp-DEX margin dollar, DUSD is exposed to StandX platform and derivatives-venue risk; a problem at the exchange propagates directly to the token.
- **Redemption-gating risk:** redemption depends on StandX honouring $1 redemptions from the collateral pool across two chains; under stress this could gate or slow.
- **Issuer / smart-contract risk:** holders rely on StandX's contracts, custody, and accounting across two chains (BNB Chain + Solana), doubling the contract attack surface.
- **Regulatory risk:** auto-yielding dollar tokens issued by a perp DEX face evolving regulatory scrutiny.

---

## Trading / usage playbook

- **Earn while you trade.** DUSD's draw is auto-yield on idle *and* margin balances — useful as the default collateral on StandX rather than a CEX dollar.
- **Watch funding/volume.** Yield is procyclical; in a low-volume, negative-funding regime the "real yield" compresses and backing strategies are stressed.
- **Mind shared-loss design.** Because there is no staked tranche, a backing shortfall hits all holders at once — do not park size you cannot afford to mark down.
- **Plan exits per chain.** Liquidity is split across BNB Chain and Solana and is modest; size to the depth on the chain you hold.

---

## Related

- [[ethena-usde]], [[usde]] — synthetic / yield-bearing dollar peers
- [[astherus-usdf]] — peer yield-bearing dollar from a perp DEX
- [[stablecoins]] — landscape overview
- [[usdc]], [[usdt]], [[dai]] — peer dollars
- [[bnb]], [[solana]] — host chains
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- Protocol description and overview from StandX ([https://docs.standx.com/docs/stand-x-overview](https://docs.standx.com/docs/stand-x-overview)). General market knowledge; no specific wiki source ingested yet beyond the CoinGecko snapshot.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DUSD |
| **Market Cap Rank** | #253 |
| **Market Cap** | $105.61M |
| **Current Price** | $0.9980 |
| **Categories** | Stablecoins, USD Stablecoin |
| **Website** | [https://standx.com/](https://standx.com/) |

---

## Overview

StandX is a Perps DEX that enables users to trade with yield-earning margins. DUSD is StandX’s first product - a yield-bearing stablecoin. Through DUSD, StandX allows users to generate returns on their margin balances. 

DUSD is a yield-bearing stablecoin designed to deliver competitive returns. It is a fully collateralized, yield-bearing stablecoin that auto-distributes real yield to holders—no staking needed—offering secure, effortless returns with seamless DeFi integration.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 105.78M DUSD |
| **Total Supply** | 105.78M DUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $105.61M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.04 (2025-11-21) |
| **Current vs ATH** | -3.97% |
| **All-Time Low** | $0.9650 (2025-11-21) |
| **Current vs ATL** | +3.43% |
| **24h Change** | -0.04% |
| **7d Change** | -0.02% |
| **30d Change** | -0.08% |
| **1y Change** | -0.19% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xaf44a1e76f56ee12adbb7ba8acd3cbd474888122` |
| Solana | `DUSDt4AeLZHWYmcXnVGYdgAzjtzU5mXUVnTMdnSzAttM` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://standx.com/](https://standx.com/) |
| **Twitter** | [@StandX_Official](https://twitter.com/StandX_Official) |
| **Discord** | [https://discord.com/invite/standx](https://discord.com/invite/standx) |
| **Whitepaper** | [https://docs.standx.com/docs/stand-x-overview](https://docs.standx.com/docs/stand-x-overview) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $503,778.00 |
| **Market Cap Rank** | #253 |
| **24h Range** | $0.9967 — $1.00 |
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
- [[bnb]]

---
