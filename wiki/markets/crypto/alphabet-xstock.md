---
title: "Alphabet xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, nasdaq, tokenization]
aliases: ["GOOGLX", "Alphabet Tokenized Stock"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://xstocks.com/"
related: ["[[real-world-assets]]", "[[tokenized-stocks]]", "[[backed-finance]]", "[[alphabet-class-a-ondo-tokenized-stock]]", "[[crypto-markets]]", "[[arbitrum]]", "[[tokenization]]"]
---

# Alphabet xStock

**Alphabet xStock** (ticker **GOOGLX**) is a tokenized equity ("xStock") issued by [[backed-finance|Backed Finance]] that tracks the shares of **Alphabet Inc.** — Google's parent — listed on the Nasdaq as **NASDAQ: GOOGL**. GOOGLX is **not** the underlying stock itself: it is an on-chain wrapper whose value is designed to follow the off-chain GOOGL share, backed 1:1 by real shares held in custody by the issuer. Issued as an SPL token on [[solana]] with bridged ERC-20 deployments (Arbitrum, Ethereum, BNB Chain, Mantle, TON), it is a [[real-world-assets|real-world asset (RWA)]] token, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, GOOGLX trades at **$364.91**, ranks **#717** by market capitalization with a market cap of **$25,328,045**, and is **-0.65%** over 24 hours and **+0.72%** over the trailing 7 days. The broader market context is risk-off: BTC sits near $64,180 and the Crypto Fear & Greed Index reads 22 (Extreme Fear).

---

## What GOOGLX Actually Is

GOOGLX is a **[[tokenization|tokenized]] stock** — a blockchain token engineered to mirror the economics of a single underlying equity, Alphabet (GOOGL). It belongs to the **xStock** product line operated by [[backed-finance|Backed Finance]], a Switzerland-based issuer of tokenized securities. For every GOOGLX token in circulation, Backed (via its custodial arrangements) holds a corresponding GOOGL share off-chain. The token's price *tracks* the share; it does not set it.

GOOGLX is one of two tokenized representations of Alphabet in this wiki; the other is [[alphabet-class-a-ondo-tokenized-stock|GOOGLON]], issued by Ondo Global Markets. Same underlying, different issuer and access model. Two prices coexist:

- **The reference price** — what GOOGL trades at on the Nasdaq during US market hours.
- **The token price** — what GOOGLX trades at on crypto venues 24/7, which can drift when traditional markets are closed or liquidity is thin.

---

## Architecture: How the Wrapper Works

### Issuer, custody and collateral

- **Issuer:** [[backed-finance|Backed Finance AG]], a Switzerland-based issuer of tokenized securities under EU/Swiss frameworks. xStocks target **non-US users** and are not offered to US persons.
- **1:1 backing:** For every GOOGLX token, Backed holds one corresponding GOOGL share with a regulated third-party custodian, segregated from its own balance sheet, with published proof-of-reserves / collateral attestations.
- **Bankruptcy-remoteness:** The structure is designed to give holders a claim on the collateral even in issuer default — a contractual/legal claim, not the SIPC-protected brokerage ownership a US investor holding GOOGL would have.

### Mint / redeem and access gating

- **Primary market (permissioned):** Only KYC'd, whitelisted institutional participants can **mint** new GOOGLX (by delivering GOOGL shares into custody) or **redeem** GOOGLX (burning tokens for the underlying value). This gatekeeping keeps supply collateralized 1:1.
- **Secondary market (permissionless):** Once minted, GOOGLX trades freely on centralized exchanges (e.g., Kraken) and DeFi venues (e.g., Orca on Solana). Any wallet can buy, sell or hold; whitelisting is required only to mint or redeem.
- **Jurisdiction gating:** Geofenced to non-US/eligible jurisdictions; US persons excluded.

### Oracle, trading hours, corporate actions, settlement

- **Tracking & oracle:** GOOGLX tracks GOOGL through primary-participant arbitrage. DeFi protocols consuming an oracle price for GOOGLX face staleness risk when the Nasdaq is closed.
- **24/7 vs market hours:** GOOGLX trades 24/7; GOOGL trades only in US session hours. The token can drift while GOOGL is closed and snap back at the next US open.
- **Dividends / corporate actions:** Alphabet pays a modest dividend; dividend and corporate-action treatment is handled by the issuer and typically reflected as an economic adjustment rather than a cash payout or direct shareholder entitlement.
- **Settlement chains:** Native SPL on Solana; bridged ERC-20 on Arbitrum, Ethereum, BNB Chain, Mantle, and TON.

### No shareholder rights

Holding GOOGLX confers **economic exposure only**. Token holders are **not** registered Alphabet shareholders and have **no voting rights**. The token reflects the economics of holding GOOGL — including the economic effect of dividends — through the issuer rather than via direct shareholder entitlement.

---

## Tracking & Peg

GOOGLX stays close to GOOGL through **arbitrage by primary participants**: mint-and-sell when the token is at a premium, buy-and-redeem when at a discount. This keeps the peg honest while the underlying market is open and primary participants are active. Sources of premium/discount and depeg risk:

- **Weekend / after-hours gap risk.** With GOOGL closed, the token can move on sentiment or thin depth, opening a basis to the stale last print that reverts at the next US open.
- **Liquidity.** With a market cap around $25.3M, spreads widen and large orders move the price.
- **Redemption friction.** If the AP/redemption channel slows under stress, discounts can persist.
- **Oracle staleness.** DeFi venues pricing GOOGLX off an oracle may misprice it during closures.

---

## Comparison: GOOGLX vs Alternatives

| Dimension | **GOOGLX (Backed xStock)** | **[[alphabet-class-a-ondo-tokenized-stock\|GOOGLON]] (Ondo)** | **Real GOOGL share (broker)** | **GOOGL CFD** |
|---|---|---|---|---|
| **Issuer** | [[backed-finance\|Backed Finance]] | Ondo Global Markets | Exchange + broker | CFD broker |
| **Backing** | 1:1 GOOGL share in custody | 1:1 GOOGL share off-chain | Direct ownership | None (synthetic) |
| **Native chain** | Solana (SPL), multi-chain | Ethereum, multi-chain | n/a | n/a |
| **Secondary trading** | Permissionless on-chain | KYC / transfer-restricted | Brokerage account | Broker platform |
| **Hours** | 24/7 | 24/7 mint/redeem (5d/wk) | US market hours | Broker hours |
| **Dividends** | Issuer economic adjustment | Reinvested into token | Paid to holder | Adjustment |
| **Rights** | Economic only, no voting | Economic only, no voting | Full (voting) | None |
| **US persons** | Excluded | Excluded | Allowed | Often restricted |

---

## How & Where It Trades

| Venue | Type | Pair |
|---|---|---|
| Kraken | CEX | GOOGLX/USD |
| Orca (Solana) | DEX | GOOGLX / USDC |

Solana is the deepest venue; liquidity concentrates during US trading hours when arbitrageurs are active. Off-hours depth is shallow, so size trades incur slippage.

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0xe92f673ca36c5e2efd2de7628f815f84807e803f` |
| Ethereum | `0xe92f673ca36c5e2efd2de7628f815f84807e803f` |
| Binance Smart Chain | `0xe92f673ca36c5e2efd2de7628f815f84807e803f` |
| Solana | `XsCPL9dNWBMvFtTmwcCA5v3xWPSMEBCszbQdiLLq6aN` |
| The Open Network (TON) | `EQALwJzXnxFjckNsurCi9O2kVg_0b1KdtjOSfvOedlY37iZc` |
| Mantle | `0xe92f673ca36c5e2efd2de7628f815f84807e803f` |

---

## Narrative, Category & Catalysts

GOOGLX sits in the **tokenized stocks / RWA** narrative — bringing US equities on-chain for non-US users who want 24/7 access, DeFi composability, and fractional, borderless exposure. The xStocks lineup spans 50+ US stocks and ETFs; Alphabet is a marquee mega-cap in that set. This was one of the most actively built corners of [[real-world-assets|RWA]] in 2025-2026.

**Catalysts:** broader on-chain-equities adoption, DeFi integrations accepting tokenized stocks as collateral, issuer competition (Backed vs Ondo on the same name), and regulatory clarity. Price catalysts are GOOGL's own drivers — search/ad revenue, Google Cloud growth, AI (Gemini) competitiveness, antitrust newsflow, and earnings.

**Macro context (2026-06):** the broad crypto tape is risk-off — Fear & Greed at 21-22 (Extreme Fear) — though the long-horizon regime model has shifted toward **Bottoming / Accumulation**. GOOGLX's price is driven mainly by GOOGL, not crypto beta.

### History / timeline

- GOOGLX is published by Backed Finance under the xStocks brand. The earliest market snapshot for this page in the wiki is the [[coingecko-top-1000-2026-04-09|CoinGecko listing snapshot of 2026-04-09]].

*(Only verified dated events are asserted; additional history should be added via the ingestion workflow.)*

---

## Risks

- **Off-chain dependency.** GOOGLX is only as good as the off-chain GOOGL shares and the systems that price and custody them.
- **Issuer & custody risk.** Holders rely on [[backed-finance|Backed Finance]] and its custodians to hold real shares 1:1 and honor redemptions — a counterparty/centralization risk absent from owning GOOGL in a brokerage account, and without US investor-protection coverage.
- **Redemption-gating risk.** Only whitelisted APs can mint/redeem; if that channel slows under stress, peg arbitrage weakens.
- **Regulatory / securities-law risk.** xStocks are marketed to **non-US** users and positioned around EU rules; availability and legality vary by jurisdiction, and tokenized-securities rules are still evolving.
- **Weekend / after-hours tracking gaps.** Crypto trades 24/7 but the Nasdaq does not; GOOGLX can drift while GOOGL is closed and snap back at the next US open.
- **Liquidity risk.** With a market cap around $25.3M, spreads can widen and large orders can move the token price.
- **No shareholder rights / no recourse.** No voting; holders are not the registered owners of the underlying shares.

---

## Trading Playbook (for a crypto trader)

- **Use case:** On-chain dollar exposure to a mega-cap tech/AI name without a US brokerage account; usable as DeFi collateral or as a lower-beta core sleeve (vs NVDA/TSLA) in an on-chain book.
- **Character of the underlying:** GOOGL is a profitable mega-cap with more moderate volatility than NVDA/TSLA, but still gaps on earnings, antitrust rulings, and AI-competitive headlines.
- **Mind the basis:** Weekend/holiday quotes can carry a premium/discount to the stale GOOGL print that reverts at the next US open.
- **Execution:** Prefer US market hours for tightest spreads and active AP arbitrage; check the premium/discount and size to shallow on-chain depth.
- **Alternatives:** Want direct ownership and dividends without wrapper risk? Hold the real share (KYC + US hours). Want the same on-chain exposure with a different access model? Compare GOOGLON.

---

## See Also

- [[alphabet-class-a-ondo-tokenized-stock]] — alternative GOOGL tokenization via Ondo Finance
- [[backed-finance]] — the xStock issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- nasdaq · [[crypto-markets]] · [[arbitrum]] · [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet for the xStocks product mechanics.
