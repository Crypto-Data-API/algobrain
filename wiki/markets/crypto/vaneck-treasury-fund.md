---
title: "VanEck Treasury Fund"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenized-treasuries]
aliases: ["VBILL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://securitize.io/primary-market/vaneck-vbill"
related: ["[[crypto-markets]]", "[[real-world-assets]]", "[[tokenized-treasuries]]", "[[ethereum]]", "[[ousg]]", "[[buidl]]"]
---

# VanEck Treasury Fund

**VanEck Treasury Fund** (ticker **VBILL**) is a [[tokenized-treasuries|tokenized Treasury / money-market]] fund issued by the global asset manager **VanEck** and tokenized through the **[[securitize|Securitize]]** platform. Each token is a regulated fund interest — an on-chain share of a fund that holds cash, U.S. Treasury bills, and Treasury-collateralized repurchase agreements. VBILL targets a **stable $1.00 NAV per token** and is a **rebasing** product: daily-accrued dividends are paid directly to investors' wallets as newly minted tokens, so the price stays pinned at $1.00 while supply grows. It is deployed multi-chain across [[ethereum|Ethereum]], Solana, Avalanche, and BNB Chain, and is one of VanEck's flagship entries into the on-chain [[real-world-assets|real-world-asset]] (RWA) market.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | VBILL |
| **Market Cap Rank** | #362 |
| **Current Price** | $1.00 |
| **Market Cap** | $67.1M |
| **24h Volume** | $0 (negligible secondary) |
| **24h Change** | 0.00% |
| **Circulating Supply** | 67.11M VBILL |
| **Total Supply** | 67.11M VBILL |
| **All-Time High** | $1.00 |
| **All-Time Low** | $1.00 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

VBILL is a **rebasing $1.00-NAV** product: rather than letting the token price drift upward, yield is distributed as additional tokens, so price stays pinned at $1.00 (ATH = ATL = $1.00) and supply grows. The effectively zero secondary volume reflects a permissioned product where all flow runs through primary subscription/redemption with Securitize rather than open-market trading. **The price quoted here is an administrative $1.00 NAV target, not a market-discovered price** — there is essentially no secondary order book, so the relevant disclaimer is NAV/peg integrity and redemption access, not price volatility.

---

## How It Works (Architecture Deep Dive)

VBILL is a tokenized share in a money-market-style fund, with VanEck as asset manager and Securitize as the tokenization, transfer-agent, and primary-market layer.

- **Fund structure & manager:** The underlying is a regulated fund managed by **VanEck**, a long-established global asset manager. Securitize wraps the fund interest as an on-chain token (a digital security) and acts as the transfer agent that maintains the legal register of holders.
- **Underlying assets:** Cash, U.S. Treasury obligations (backed by the full faith and credit of the U.S. government), and repurchase agreements collateralized by Treasuries. The portfolio holds securities with maturities of **397 days or less** and maintains a **weighted-average maturity of 60 days or less** — a classic money-market mandate that minimizes interest-rate and credit risk.
- **Custody:** Underlying Treasuries and cash are held by regulated off-chain custodians; the on-chain token mirrors that custodied position. Market cap equals fully diluted value (MC/FDV = 1.00), consistent with full backing.
- **Eligible-investor gating:** Subscription and redemption are gated through Securitize's primary market to KYC/AML-screened, accredited or qualified investors, under U.S. securities-law exemptions (typically Reg D for U.S. persons and Reg S for non-U.S. persons). Open retail secondary trading is restricted.
- **Mint / redeem flow & settlement:** Investors subscribe through the Securitize primary market; the fund issues tokens against contributed value. VanEck/Securitize have supported in-kind **stablecoin subscriptions (including via atomic swaps)** alongside USD, enabling near-instant on-chain settlement for whitelisted participants. Redemption is at $1.00 NAV through the same primary channel.
- **Yield source & distribution:** Yield comes from the T-bill / repo portfolio. It is distributed via a **rebase** — daily-accrued dividends arrive as newly minted tokens in the holder's wallet — keeping unit price at $1.00 and growing token count, in contrast to price-accretion designs where unit price climbs.
- **Oracle / NAV feed:** The fund is priced at a $1.00 NAV target maintained by the fund's daily accounting cycle; on-chain there is no continuous oracle-driven price discovery because the peg is enforced by primary mint/redeem at NAV.
- **Transfer restrictions / whitelist:** Tokens can only move among Securitize-whitelisted addresses; transfers to non-whitelisted wallets are blocked at the contract/transfer-agent level.

---

## Comparison vs Peer Tokenized Treasury / MMF Products

| Product | Issuer / Manager | Unit / NAV model | Yield distribution | Notable trait |
|---|---|---|---|---|
| **VBILL** | VanEck + Securitize | $1.00 NAV (rebasing) | New tokens (rebase) | Multi-chain; stablecoin in-kind subscriptions |
| **[[buidl]]** (BUIDL) | BlackRock + Securitize | $1.00 NAV (rebasing) | New tokens (rebase) | Largest tokenized-Treasury fund; deep ecosystem |
| **[[ousg]]** (OUSG) | Ondo Finance | Price-accruing (~$100+) | NAV price-accretion | Instant mint/redeem via USDC; BUIDL-backed |
| **[[hashnote-usyc]]** (USYC) | Hashnote / Circle | Price-accruing | NAV price-accretion | Repo-focused; Circle-integrated collateral |
| **USTB** | Superstate | Price-accruing | NAV price-accretion | Short-duration Treasuries, 40-Act-style fund |

VBILL competes most directly with BlackRock's BUIDL — both are Securitize-tokenized, rebasing, $1.00-NAV Treasury funds backed by a brand-name manager. The key differentiators are VanEck's multi-chain footprint and support for stablecoin/atomic-swap subscriptions.

---

## How & Where It Trades / Is Used

- **Primary market:** Subscribe/redeem with VanEck via [Securitize](https://securitize.io/primary-market/vaneck-vbill) — effectively the only meaningful venue (secondary volume ~$0).
- **Eligibility:** Only Securitize-whitelisted, KYC/AML-cleared accredited or qualified investors (U.S. via Reg D, non-U.S. via Reg S) can hold or transact. Not available to open retail.
- **Secondary market:** Multi-chain token transfers are technically possible among whitelisted holders, but on-chain secondary liquidity is negligible; holders rely on primary redemption at NAV.
- **DeFi composability:** As a permissioned RWA, broad DeFi use is constrained by the whitelist, but tokenized Treasury funds in this category are increasingly used as **collateral and cash-management instruments** within institutional and permissioned DeFi rails.
- **Hours:** Token transfers run 24/7 on-chain, but creation/redemption and the underlying Treasury market follow traditional banking/market hours; daily dividend accrual mirrors the fund's accounting cycle.
- **Tracking:** Pegged to $1.00 NAV with yield distributed as tokens. There is essentially no price discovery on secondary venues — the peg is maintained by primary mint/redeem at NAV.

---

## Narrative, Category & Catalysts

VBILL sits in the fast-growing **tokenized Treasuries / tokenized cash** segment of the RWA narrative, where regulated managers move money-market exposure on-chain to serve crypto-native treasuries, DAOs, and institutions seeking dollar-stable yield with blockchain settlement. Catalysts include:

- **Rates regime:** Demand for tokenized T-bill yield scales with the level of short-term U.S. rates — higher front-end yields make products like VBILL more attractive as on-chain cash.
- **Institutional adoption:** VanEck's brand and Securitize's regulated rails lower the trust barrier for institutions entering on-chain cash management.
- **RWA tokenization wave:** VBILL is part of a broader push (alongside [[buidl]], [[ousg]], and others) to bring trillions in real-world fixed-income on-chain.
- **Stablecoin integration:** Support for stablecoin/atomic-swap subscriptions positions VBILL as a yield-bearing alternative to idle stablecoin balances.

### History / Timeline

- **2025:** VanEck Treasury Fund (VBILL) launched as a tokenized Treasury fund via Securitize, with multi-chain deployment across Ethereum, Solana, Avalanche, and BNB Chain. (Specific launch date not independently verified here — do not infer one.)
- **2026-06-21:** Market snapshot — ~$67.1M market cap, $1.00 NAV, rank #362.

---

## Risks

- **Issuer / counterparty risk:** Reliance on VanEck (manager) and Securitize (tokenization/transfer agent), plus the fund's custodians. Issuer or administrator failure is the primary tail risk.
- **Custodial risk:** The token's value depends on the off-chain custody and legal enforceability of the claim on the underlying Treasuries.
- **Redemption-gating / liquidity risk:** With near-zero secondary volume, holders depend on the primary redemption channel; if redemptions are gated or paused, exits could be slow.
- **NAV-gap / "breaking the buck" risk:** The $1.00 target can break if the underlying portfolio takes losses (e.g., a repo counterparty default) — the same risk faced by traditional money-market funds.
- **Regulatory / securities-law risk:** As a tokenized security, VBILL is subject to securities regulation and transfer restrictions that can change and limit eligibility.
- **Smart-contract risk:** Multi-chain deployment broadens the contract and bridge attack surface.
- **Macro backdrop:** As of 2026-06-23 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **21 ("Extreme Fear")** and the long-horizon regime model reads bottoming/accumulation. Dollar-stable Treasury products like VBILL are a relative safe haven within crypto portfolios during risk-off regimes, but remain exposed to issuer and regulatory risk. **The token's value tracks fund NAV/yield, not the crypto cycle.**

---

## Trading / Usage Playbook

- **Who can hold it:** Only KYC/AML-cleared accredited or qualified investors whitelisted through Securitize (Reg D for U.S. persons, Reg S for non-U.S.). Not for open retail.
- **Primary use case:** On-chain **cash management** — parking dollars in a $1.00-NAV, T-bill-yielding token that settles on-chain, suitable for crypto treasuries, funds, and institutions.
- **Collateral use:** Within permissioned/institutional DeFi contexts, tokenized Treasury funds can serve as high-quality collateral; eligibility depends on each venue's whitelist.
- **Exit:** Redeem at $1.00 NAV through Securitize's primary market; do not rely on secondary liquidity.

---

## Platform & Chain Information

**Deployment:** Multi-chain ([[ethereum|Ethereum]], Solana, Avalanche, BNB Chain)

| Chain | Address |
|---|---|
| Ethereum | `0x2255718832bc9fd3be1caf75084f4803da14ff01` |
| BNB Chain | `0x14d72634328c4d03bba184a48081df65f1911279` |
| Solana | `34mJztT9am2jybSukvjNqRjgJBZqHJsHnivArx1P4xy1` |
| Avalanche | `0x7f4546ef315efc65336187fe3765ea779ac90183` |

---

## See Also

- [[real-world-assets]] / [[rwa]]
- [[tokenized-treasuries]]
- [[ousg]], [[buidl]], [[hashnote-usyc]] — peer tokenized Treasury / MMF products
- [[securitize]] — tokenization platform / transfer agent
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.
