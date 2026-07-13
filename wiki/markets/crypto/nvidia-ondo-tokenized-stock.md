---
title: "NVIDIA (Ondo Tokenized Stock)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, tokenized-stocks]
aliases: ["NVDAON", "NVDAon", "Ondo NVIDIA"]
entity_type: protocol
headquarters: "Decentralized (issued by Ondo Global Markets)"
website: "https://app.ondo.finance/assets/nvdaon"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[tokenization]]", "[[tokenized-stocks]]", "[[ondo-finance]]", "[[nvidia]]", "[[nvidia-xstock]]"]
---

# NVIDIA (Ondo Tokenized Stock)

**NVIDIA (Ondo Tokenized Stock)** (ticker **NVDAON**) is a tokenized [[real-world-assets|real-world asset]]: an on-chain wrapper issued by **[[ondo-finance|Ondo Global Markets]]** that tracks the share price of **[[nvidia|NVIDIA]] (NASDAQ: NVDA)**. Each NVDAON gives holders economic exposure similar to owning an NVDA share (including reinvested dividends), but it is **not the underlying equity** — it is a tokenized claim whose price tracks NVDA, backed by real shares held off-chain within Ondo's structure. It is issued multi-chain with [[ethereum|Ethereum]] as the canonical chain (plus BNB Chain and Solana). As of 2026-06-21 it traded at **$208.74**, ranked **#446** by market capitalization with a market cap of **~$50.75M**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

NVDAON is the **Ondo-issued** alternative to the Backed-issued [[nvidia-xstock|NVIDIA xStock (NVDAX)]] — same underlying (NVDA), different issuer, custody, and access model.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NVDAON |
| **Market Cap Rank** | #446 |
| **Market Cap** | $50,750,581 (~$50.75M) |
| **Current Price** | $208.74 |
| **24h Change** | -0.07% |
| **7d Change** | +2.22% |
| **Underlying asset** | NVIDIA (NVDA) common stock |
| **Issuer** | Ondo Global Markets |
| **Tracks** | NVDA share price (economic exposure, dividends reinvested) |
| **Categories** | Tokenized Assets, BNB Chain Ecosystem, Solana Ecosystem, Tokenized Stock, Ethereum Ecosystem, Real World Assets (RWA), Binance Alpha Spotlight, Ondo Tokenized Assets |
| **Website** | [https://app.ondo.finance/assets/nvdaon](https://app.ondo.finance/assets/nvdaon) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

NVDAON is the [[ondo-finance|Ondo]]-tokenized version of [[nvidia|NVIDIA]] stock, part of the **Ondo Global Markets** lineup of tokenized US equities and ETFs (which also includes [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]] and [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]]). It gives holders economic exposure comparable to holding an NVDA share, with dividends **reinvested** into the token's value rather than paid out. Ondo's tokenized stocks are designed so **non-US retail and institutional users** can mint and redeem 24 hours a day, five days a week, with the on-chain price kept in line with the underlying via traditional exchange liquidity. *Additional restrictions apply.*

The token is a **wrapper**: its on-chain price **tracks the off-chain NVDA share price**, and its backing is real NVDA shares held by Ondo's structure off-chain. It is therefore exposed to equity-market moves (note the +2.22% 7-day move, mirroring NVDA), unlike the flat-NAV cash/T-bill RWAs in this cluster.

---

## Architecture: How the Wrapper Works

- **Underlying asset / backing:** Real shares of NVIDIA (NVDA) held off-chain within the Ondo Global Markets structure; each token represents economic exposure to one underlying share. Backing is custodied via Ondo's broker/custody partners rather than self-custodied on-chain.
- **Issuer:** **Ondo Global Markets** (the tokenized-securities arm of [[ondo-finance|Ondo Finance]]).
- **Price tracking & oracle:** The token price tracks NVDA's market price, maintained via Ondo's arbitrage/market-maker mechanics against traditional exchange liquidity. DeFi venues consuming an oracle price face staleness risk when the Nasdaq is closed.
- **Mint / redeem (issuance & redemption):** Issuance and redemption are **permissioned and KYC-gated** — available to eligible, onboarded non-US users, 24/5. When a user mints, Ondo (via its broker/market-maker arrangements) acquires the corresponding NVDA shares; on redemption the shares are sold and the token burned. This primary mint/redeem keeps the token tethered to NVDA's price.
- **Dividends / corporate actions:** Dividends are **reinvested** into the token's economic value rather than paid out separately. Corporate actions are handled within the issuer's structure.
- **24/7 trading vs market hours:** Secondary trading can occur 24/7 on-chain, while the underlying NVDA trades only in US session hours and mint/redeem runs 24/5. The token can deviate from NVDA's last print during closures and re-converge afterward.
- **Transfer restrictions:** Secondary transfers can be restricted to whitelisted / KYC'd addresses; the product is explicitly **not offered to US persons**.
- **Settlement chains:** Multi-chain — [[ethereum|Ethereum]] (canonical), BNB Smart Chain, and Solana (see Contract Addresses below).
- **No shareholder rights:** Holders get **economic exposure only** — no shareholder voting rights, not holders of record of NVDA, and they hold a claim against the issuer's structure rather than the equity itself. No US investor-protection (SIPC) coverage.

---

## Tracking & Peg

NVDAON tracks NVDA through Ondo's primary mint/redeem and market-maker arbitrage. Sources of premium/discount and depeg risk:

- **Weekend / after-hours gap risk.** With NVDA closed (and mint/redeem paused outside 24/5 windows), the token can drift from the stale last print and re-converge at the next US open.
- **Liquidity.** Secondary liquidity (Uniswap, Bitget) can be thin; size orders move price and widen spreads.
- **Redemption / KYC friction.** Permissioned, KYC-gated mint/redeem means peg arbitrage is limited to onboarded participants; if that channel slows, discounts can persist.
- **Oracle staleness.** DeFi venues pricing NVDAON off an oracle may misprice it during closures.

---

## Comparison: NVDAON vs Alternatives

| Dimension | **NVDAON (Ondo)** | **[[nvidia-xstock\|NVDAX]] (Backed xStock)** | **Real NVDA share (broker)** | **NVDA CFD** |
|---|---|---|---|---|
| **Issuer** | Ondo Global Markets | [[backed-finance\|Backed Finance]] | Exchange + broker | CFD broker |
| **Backing** | 1:1 NVDA share off-chain | 1:1 NVDA share in custody | Direct ownership | None (synthetic) |
| **Canonical chain** | Ethereum, multi-chain | Solana (SPL), multi-chain | n/a | n/a |
| **Secondary trading** | KYC / whitelist-restricted | Permissionless on-chain | Brokerage account | Broker platform |
| **Mint/redeem** | 24/5, KYC-gated | KYC'd APs | n/a | n/a |
| **Dividends** | Reinvested into token | Issuer economic adjustment | Paid to holder | Adjustment |
| **Rights** | Economic only, no voting | Economic only, no voting | Full (voting) | None |
| **US persons** | Excluded | Excluded | Allowed | Often restricted |

The key practical difference vs NVDAX: Ondo's secondary transfers are more tightly KYC/whitelist-gated, whereas Backed's xStock trades permissionlessly once minted. Choose based on which access/compliance model fits.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 129,669 NVDAON |
| **Total Supply** | 129,652 NVDAON |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $23.40M |
| **Market Cap / FDV Ratio** | 1.00 |

Supply is **elastic** — it expands on mint and contracts on redemption, tracking how many NVDA shares are tokenized. The MC/FDV ratio near 1.00 indicates essentially all supply is circulating (no large locked/vesting overhang), unlike typical token unlock schedules.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $211.50 (2025-10-29) |
| **All-Time Low** | $163.07 (2026-03-31) |
| **24h Change** | -0.07% |
| **7d Change** | +2.22% |

Because the token tracks NVDA, its price history mirrors the underlying equity's swings (unlike the flat cash/T-bill RWAs in this group). The +2.22% 7-day move reflects NVDA share-price action, not crypto sentiment.

---

## Platform & Chain Information

**Canonical Chain:** Ethereum (multi-chain issuance).

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x2d1f7226bd1f780af6b9a49dcc0ae00e8df4bdee` |
| Binance Smart Chain | `0xa9ee28c80f960b889dfbd1902055218cba016f75` |
| Solana | `gEGtLTPNQ7jcg25zTetkbmF7teoDLcrfTnQfmn2ondo` |

---

## How & Where It Trades

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Bitget | NVDAON/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | NVDAON / USDC | Spot |
| Uniswap V2 (Ethereum) | NVDAON / (paired token) | Spot |

Ethereum is the canonical liquidity venue. Liquidity concentrates during US trading hours when arbitrageurs are active; off-hours depth is shallow.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.ondo.finance/assets/nvdaon](https://app.ondo.finance/assets/nvdaon) |
| **Twitter** | [@ondofinance](https://twitter.com/ondofinance) |

---

## Narrative, Category & Catalysts

NVDAON sits in the **tokenized stocks / RWA** narrative, alongside the rest of the Ondo Global Markets lineup. Ondo is a leading RWA-tokenization protocol (also known for tokenized US-Treasury products), and its move into tokenized equities brings marquee US names like NVIDIA on-chain for non-US users. NVDAON's "Binance Alpha Spotlight" category tag reflects exchange-distribution attention for the Ondo tokenized-stock family.

**Catalysts:** broader on-chain-equities adoption, Ondo Global Markets expansion and new listings, DeFi integrations accepting tokenized stocks as collateral, issuer competition (Ondo vs Backed on the same names), and regulatory clarity on tokenized securities. Price catalysts are NVDA's own drivers — AI-datacenter demand, GPU supply, earnings, and the semiconductor cycle.

**Macro context (2026-06):** the broad crypto tape is risk-off — Fear & Greed at 21-22 (Extreme Fear) — though the long-horizon regime model has shifted toward **Bottoming / Accumulation**. NVDAON's price is driven mainly by NVDA, not crypto beta.

### History / timeline

- Recorded all-time high $211.50 (2025-10-29) and all-time low $163.07 (2026-03-31). The earliest market snapshot for this page in the wiki is the [[coingecko-top-1000-2026-04-09|CoinGecko listing snapshot of 2026-04-09]].

> *An earlier intra-snapshot reading (rank #438, 24h range $180.37–$184.95, last updated 2026-04-09) is retained for history only; current figures are the 2026-06-21 values above.*

*(Only verified dated events are asserted; additional history should be added via the ingestion workflow.)*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Off-chain dependency:** The token's value depends entirely on real NVDA shares and the Ondo structure holding them. On-chain settlement cannot enforce delivery of the equity.
- **Issuer / custody (counterparty) risk:** Concentrated reliance on Ondo Global Markets and its broker/custody partners. Failure or mismanagement could break the link to the underlying shares. No US investor-protection coverage.
- **Redemption-gating risk:** Permissioned, KYC-gated mint/redeem limits who can perform peg arbitrage; if that channel slows, discounts can persist.
- **No shareholder rights:** Holders forgo voting rights and direct ownership; they hold a derivative-like economic claim, not NVDA stock.
- **Regulatory & transfer restrictions:** Permissioned, KYC-gated, and **not available to US persons**; secondary transfers may be whitelist-restricted. Regulatory treatment of tokenized equities is unsettled and could force changes or restrict access.
- **Market-hours / tracking risk:** The underlying trades on US exchange hours; on-chain trading is 24/7, so the token can deviate from NVDA's last price during closures, and tracking depends on Ondo's arbitrage/market-maker mechanics.
- **Equity-market risk:** Full exposure to NVDA's volatility — semiconductor-cycle, AI-demand, and single-name concentration risk.
- **Liquidity & smart-contract risk:** Secondary liquidity (Uniswap, Bitget) can be thin; multi-chain deployment adds contract and bridge attack surface.

---

## Trading Playbook (for a crypto trader)

- **Use case:** On-chain, dollar-denominated exposure to the AI/semiconductor bellwether via the Ondo rails, with dividends auto-reinvested — convenient for non-US users already onboarded to Ondo.
- **Character of the underlying:** NVDA is a **high-beta, high-momentum** mega-cap — large gaps around earnings and AI-demand headlines. Expect equity-grade volatility.
- **NVDAON vs NVDAX:** Pick NVDAON if you want Ondo's KYC'd/whitelisted compliance model and dividend reinvestment; pick [[nvidia-xstock|NVDAX]] if you want permissionless secondary trading and DeFi composability. Same underlying exposure either way.
- **Mind the basis:** Treat weekend/holiday quotes with caution — the token can carry a premium/discount to the stale NVDA print that reverts at the next US open.
- **Execution:** Prefer US market hours for tightest spreads and active arbitrage; Ethereum is the canonical venue. Size to shallow on-chain depth and check the premium/discount before sending size.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[nvidia]] — the underlying company (NASDAQ: NVDA)
- [[nvidia-xstock]] — alternative NVDA tokenization via Backed Finance (xStocks)
- [[ondo-finance]] — the issuer (Ondo Global Markets)
- [[crypto-markets]] · [[ethereum]]
- [[real-world-assets]] · [[tokenization]] · [[tokenized-stocks]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original listing snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific Ondo source document ingested yet.
