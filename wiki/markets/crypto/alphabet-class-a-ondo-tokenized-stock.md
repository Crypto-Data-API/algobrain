---
title: "Alphabet Class A (Ondo Tokenized Stock)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, nasdaq, tokenization]
aliases: ["GOOGLON", "GOOGLon", "Alphabet Ondo"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/googlon"
related: ["[[real-world-assets]]", "[[tokenized-stocks]]", "[[ondo-finance]]", "[[alphabet-xstock]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# Alphabet Class A (Ondo Tokenized Stock)

**Alphabet Class A (Ondo Tokenized Stock)** (GOOGLON) is a tokenized equity issued by **Ondo Global Markets** ([[ondo-finance|Ondo Finance]]) that tracks the Class A shares of **Alphabet Inc.** — Google's parent — listed on the Nasdaq as **NASDAQ: GOOGL**. GOOGLON is **not** the underlying stock itself: it is an on-chain wrapper whose value is designed to follow the off-chain GOOGL share, **backed 1:1 by real shares custodied off-chain**. It gives holders economic exposure comparable to holding GOOGL (including the economic effect of any dividends), but **no** shareholder rights. It is a [[real-world-assets|real-world asset (RWA)]] token, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, GOOGLON trades at **$365.07**, ranks **#710** by market capitalization with a market cap of **$25,791,170**, and is **-0.77%** over 24 hours and **+0.71%** over the trailing 7 days. The broader market context is risk-off: BTC sits near $64,180 and the Crypto Fear & Greed Index reads 22 (Extreme Fear).

---

## What GOOGLON actually is

GOOGLON is a **[[tokenization|tokenized]] stock** issued under the **Ondo Global Markets** program — Ondo's framework for bringing tokenized U.S. equities and ETFs on-chain. It is one of two tokenized representations of Alphabet in this wiki; the other is [[alphabet-xstock|GOOGLX]], a [[backed-finance|Backed Finance]] xStock. Same underlying (Alphabet / GOOGL), different issuer and mechanics.

For GOOGLON, real GOOGL shares are held in custody off-chain and the token is designed to track their value. Two prices coexist:

- **The reference price** — what GOOGL trades at on the Nasdaq during US market hours.
- **The token price** — what GOOGLON trades at on crypto venues, which can drift from the reference when traditional markets are closed or liquidity is thin.

---

## Key facts

| Field | Detail |
|---|---|
| **Token ticker** | GOOGLON |
| **Underlying** | Alphabet Inc. Class A (NASDAQ: GOOGL) |
| **Issuer** | Ondo Global Markets ([[ondo-finance|Ondo Finance]]) |
| **Backing** | Real GOOGL shares custodied off-chain (1:1) |
| **Native chain** | Ethereum (also BNB Chain, Solana) |
| **Market cap rank** | #710 |
| **Market cap** | $25,791,170 |
| **Current price** | $365.07 |
| **24h change** | -0.77% |
| **7d change** | +0.71% |
| **Website** | [https://app.ondo.finance/assets/googlon](https://app.ondo.finance/assets/googlon) |

---

## Architecture: issuance, custody and the mint/redeem model

The Ondo Global Markets model is built around **off-chain share custody, 1:1 backing, and KYC / transfer restrictions**:

- **Permissioned access.** Minting and redeeming are restricted to **KYC-verified, eligible** users. Ondo Global Markets is positioned for **non-US** retail and institutional users; it is **not offered to US persons**, and additional jurisdictional restrictions apply.
- **Off-chain custody, 1:1 backing.** Real GOOGL shares are held off-chain by the issuer's custodial arrangements, with each GOOGLON token designed to be backed by one share's worth of economic exposure. The token represents a claim on those custodied shares' economics, not a direct registered shareholding.
- **Instant mint/redeem (during market windows).** Ondo markets the ability to mint and redeem tokenized U.S. stocks and ETFs around the clock on weekdays (24/5), with access to traditional exchange liquidity — but transfers and eligibility remain controlled. New tokens are minted when an eligible participant delivers value and the issuer acquires/allocates the underlying shares; redemption reverses this.
- **Oracle / pricing.** The token's fair value is anchored to the GOOGL reference price; pricing on-chain references the underlying equity, with deviations corrected by eligible-participant arbitrage when the equity market is open.

### 24/7 token vs market-hours underlying

Crypto venues trade GOOGLON continuously, but **GOOGL trades only during Nasdaq hours** (plus limited pre/post-market). When the underlying is closed — nights, weekends, holidays — GOOGLON can drift from the last reference price on sentiment or thin flow, because the arbitrage that realigns it (mint/redeem against real shares) generally requires the equity market to be open and is further limited by the KYC/transfer restrictions on who may arbitrage.

### No shareholder rights

GOOGLON conveys **economic exposure only**. Holders are **not** registered Alphabet shareholders and have **no voting rights**. The token is designed to reflect the economics of holding GOOGL — including the economic effect of dividends (Alphabet's dividend is small) — through the issuer, not via direct shareholder entitlement.

---

## Comparison: GOOGLON vs GOOGLX vs holding GOOGL

Both tokens give on-chain exposure to Alphabet, but differ by issuer and access model; holding the underlying share is the TradFi baseline:

| | GOOGLON (Ondo) | [[alphabet-xstock\|GOOGLX]] (Backed xStock) | GOOGL (underlying share) |
|---|---|---|---|
| **Issuer** | Ondo Global Markets | [[backed-finance\|Backed Finance]] | N/A (public equity) |
| **Backing** | 1:1 real shares, off-chain custody | 1:1 real shares, off-chain custody | The share itself |
| **Access** | KYC / transfer-restricted, non-US | Permissionless secondary trading | Brokerage account |
| **Native chain** | Ethereum (+ BNB, Solana) | Arbitrum (multi-chain) | None |
| **Hours** | Token 24/7; underlying 24/5 | Token 24/7; underlying 24/5 | Nasdaq hours |
| **Rights** | Economic only, no voting | Economic only, no voting | Full shareholder rights + voting |
| **Composability** | On-chain (gated) | On-chain (permissionless) | None |

The trade-off ladder: **GOOGL** gives full rights and the tightest pricing but no on-chain utility and TradFi access only; **GOOGLX** maximizes on-chain composability via permissionless trading; **GOOGLON** targets compliance-sensitive non-US institutions willing to accept KYC/transfer gating in exchange for an issuer-controlled, regulated-style wrapper. The gating that makes GOOGLON attractive to institutions is also what limits its arbitrage and liquidity.

---

## Platform & chain information

**Native chain: Ethereum (multi-chain issuance).**

| Chain | Address |
|---|---|
| Ethereum | `0xba47214edd2bb43099611b208f75e4b42fdcfedc` |
| Binance Smart Chain | `0x091fc7778e6932d4009b087b191d1ee3bac5729a` |
| Solana | `bbahNA5vT9WJeYft8tALrH1LXWffjwqVoUbqYa1ondo` |

---

## Exchange listings

| Venue | Type | Pair |
|---|---|---|
| Bitget | CEX | GOOGLON/USDT |
| Uniswap V3 (Ethereum) | DEX | GOOGLON / USDC |

---

## Narrative & catalysts

GOOGLON rides the **tokenized-equities / RWA** narrative — Ondo's push (alongside Backed's xStocks, and others) to put U.S. stocks and ETFs on-chain for non-US and institutional users seeking 24/5 access and on-chain settlement. Catalysts: growth of the Ondo Global Markets product suite and listings, deeper secondary liquidity, integrations that let tokenized stocks be used as on-chain collateral, and regulatory clarity for tokenized securities. The principal headwind is the same regulation: tokenized-securities rules are still evolving, and the not-for-US-persons posture constrains the addressable market. Note that as a wrapper on Alphabet's equity, GOOGLON's value is driven by **GOOGL's fundamentals and the US equity tape**, not crypto sentiment — the "Extreme Fear" crypto regime affects on-chain liquidity and spreads more than the token's fair value.

---

## History / timeline

- **Launch** — GOOGLON issued under Ondo Global Markets, Ondo's tokenized-US-equities/ETF framework, backed 1:1 by custodied GOOGL shares; deployed on Ethereum with BNB Chain and Solana issuance.
- **2026-06-21** — snapshot: $365.07, market cap $25,791,170, rank #710, -0.77% 24h / +0.71% 7d; listed on Bitget (CEX, GOOGLON/USDT) and Uniswap V3 (DEX, GOOGLON/USDC).

(Exact issuance dates are not in the source data and are therefore not asserted here.)

---

## Risks

- **Off-chain dependency.** GOOGLON is only as good as the off-chain GOOGL shares and the systems that price and custody them.
- **Issuer & custody / counterparty risk.** Holders rely on Ondo Global Markets and its custodians to hold real shares and honor redemptions — a counterparty/centralization risk with no FDIC/SIPC-style backstop.
- **NAV-gap / tracking error.** During weekends, after-hours, or thin liquidity, the token price can diverge from GOOGL's value; the gap only reliably closes when the equity market is open and eligible participants arbitrage it.
- **Redemption-gating / transfer restrictions.** KYC-gated, transfer-restricted, and **not for US persons**; eligibility and legality vary by jurisdiction. These restrictions also limit who can arbitrage the peg, structurally widening potential NAV gaps.
- **Liquidity risk.** With a market cap around $25.8M, spreads can widen and large orders can move the token price.
- **Regulatory risk.** Tokenized-securities rules are still evolving and could affect issuance, listings, or holder eligibility.
- **No shareholder rights / no recourse.** No voting; holders are not registered owners of the underlying shares.

---

## Trading / usage playbook

- **Treat it as GOOGL exposure, priced in crypto rails.** Value GOOGLON off the **GOOGL reference price**, not off off-hours token prints; weekend/after-hours quotes can gap and should not be taken as fair value.
- **Confirm eligibility first.** Primary mint/redeem requires KYC and is **not available to US persons**; non-eligible users are limited to whatever secondary liquidity exists and bear the full NAV-gap risk.
- **Size to the book.** ~$25.8M market cap means thin depth; large orders move price, and the DEX/CEX pairs are best used for modest clips.
- **Pick the wrapper for your constraint.** Choose **GOOGLON** if you need an Ondo-issued, compliance-gated wrapper; choose [[alphabet-xstock|GOOGLX]] for permissionless on-chain composability; hold **GOOGL** directly if you want voting rights and the tightest pricing.

---

## See Also

- [[alphabet-xstock]] — alternative GOOGL tokenization via Backed Finance / xStocks
- [[ondo-finance]] — the issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- nasdaq · [[crypto-markets]] · [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet for the Ondo Global Markets product mechanics.
