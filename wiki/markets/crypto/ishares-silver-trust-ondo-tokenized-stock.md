---
title: "iShares Silver Trust (Ondo Tokenized Stock)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, commodities, etf, tokenization]
aliases: ["SLVON", "SLVon", "iShares Silver Trust Ondo"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/slvon"
related: ["[[real-world-assets]]", "[[tokenized-stocks]]", "[[ondo-finance]]", "[[etf]]", "[[gold]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# iShares Silver Trust (Ondo Tokenized Stock)

**iShares Silver Trust (Ondo Tokenized Stock)** (SLVON) is a tokenized exchange-traded fund issued by **Ondo Global Markets** ([[ondo-finance|Ondo Finance]]) that tracks the **iShares Silver Trust**, BlackRock's silver-backed ETF listed as **NYSEARCA: SLV**. SLVON is **not** the ETF itself: it is an on-chain wrapper whose value is designed to follow the off-chain SLV share, backed by real shares custodied off-chain. SLV in turn holds physical silver, so SLVON is effectively two layers of wrapping over the silver price. It gives holders economic exposure comparable to holding SLV, but **no** shareholder rights. It is a [[real-world-assets|real-world asset (RWA)]] token, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, SLVON trades at **$58.90**, ranks **#702** by market capitalization with a market cap of **$25,931,315**, and is **-0.15%** over 24 hours and **-3.68%** over the trailing 7 days. The broader market context is risk-off: BTC sits near $64,180 and the Crypto Fear & Greed Index reads 22 (Extreme Fear). (Regime context only — at the 2026-06-22 macro snapshot the crypto tape remained in Extreme Fear, F&G 21, market-health 29/100; SLVON's value is set by the silver price via SLV's US session, not the crypto cycle.)

---

## What SLVON Actually Is

SLVON is a **[[tokenization|tokenized]] [[etf|ETF]]** issued under the **Ondo Global Markets** program — Ondo's framework for bringing tokenized U.S. equities, ETFs and commodity vehicles on-chain. The chain of exposure runs through **two wrappers and a metal**: physical silver → iShares Silver Trust (SLV) → SLVON token. Real SLV shares are held in custody off-chain and the token is designed to track their value, giving on-chain holders single-token exposure to the silver price (a precious-metal commodity, comparable to how [[gold|gold]] is tracked by metal-backed ETFs). This makes SLVON the **commodity / macro-hedge** member of the Ondo tokenized lineup, distinct from the equity-beta wrappers ([[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]], [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]]) and single-name equities ([[tesla-ondo-tokenized-stock|TSLAon]]).

Two prices coexist:

- **The reference price** — what SLV trades at on NYSE Arca during US market hours.
- **The token price** — what SLVON trades at on crypto venues, which can drift from the reference when traditional markets are closed or liquidity is thin.

### Architecture — how the wrapper works

- **Issuer & custody:** [[ondo-finance|Ondo Global Markets]] issues SLVON; real SLV shares are held off-chain by the issuer's custodial arrangements, and SLV itself custodies the physical silver bullion that backs the trust.
- **Backing (two layers):** Each token is backed by real custodied SLV shares; SLV in turn is backed by allocated physical silver. The token's fair value is the underlying SLV/silver price.
- **Mint / redeem & KYC gating:** Minting and redeeming are permissioned and KYC-gated to eligible, onboarded **non-US** users; the product is **not offered to US persons**. Ondo markets the ability to mint/redeem tokenized U.S. ETFs 24/5 with access to traditional exchange liquidity.
- **Oracle / price feed:** Fair value is the SLV reference (and thus the silver spot price); integrators reference it via market-data and oracle feeds, with eligible participants arbitraging premiums/discounts on-chain.
- **24/7 token vs market-hours underlying:** SLVON trades on crypto venues continuously while SLV trades only on NYSE Arca's US session — the source of weekend/overnight basis risk.
- **Distributions:** SLV is a commodity trust that **pays no dividend** (and charges a sponsor's fee that gradually reduces silver-per-share); there is no cash distribution to pass through, and the fee drag is reflected through the underlying.
- **Settlement chains:** Ethereum (canonical), BNB Smart Chain and Solana (see Contract Addresses).

---

## Comparison: SLVON vs alternatives

| Dimension | **SLVON** (Ondo silver) | **Holding real SLV** (broker) | **Equity-beta wrapper** (e.g. [[spdr-s-p-500-etf-ondo-tokenized-etf\|SPYon]]) | **Crypto "digital gold"** (e.g. [[gold\|gold]] proxies / BTC) |
|---|---|---|---|---|
| Underlying | Physical silver via SLV | Physical silver via SLV | US equity index | Metal / store-of-value asset |
| Asset class | Commodity (precious metal) | Commodity | Equity | Commodity / crypto |
| Issuer | [[ondo-finance\|Ondo Global Markets]] | BlackRock (SLV sponsor) | Ondo Global Markets | varies |
| Wrapping layers | Two (SLVON → SLV → metal) | One (SLV → metal) | Two (token → ETF → index) | n/a / one |
| Trading hours | 24/7 | US market hours | 24/7 | 24/7 |
| Income | None (fee drag) | None (fee drag) | Dividends reinvested | None |
| Shareholder rights | None | Limited (trust units) | None | n/a |
| US persons | Not offered | Available | Not offered | Available |
| Role | Macro / inflation hedge | Macro hedge | Risk-on beta | Macro hedge |

SLVON is the on-chain way to hold a **precious-metal / inflation hedge** for non-US users, versus equity-beta wrappers that carry risk-on exposure. Versus a real broker SLV position it adds the second wrapping layer (issuer/custody, tracking, weekend gap) in exchange for 24/7 on-chain access and composability.

---

## Key Facts

| Field | Detail |
|---|---|
| **Token ticker** | SLVON |
| **Underlying** | iShares Silver Trust (NYSEARCA: SLV) — physical silver ETF |
| **Issuer** | Ondo Global Markets ([[ondo-finance|Ondo Finance]]) |
| **Backing** | Real SLV shares custodied off-chain (SLV holds physical silver) |
| **Native chain** | Ethereum (also BNB Chain, Solana) |
| **Market cap rank** | #702 |
| **Market cap** | $25,931,315 |
| **Current price** | $58.90 |
| **24h change** | -0.15% |
| **7d change** | -3.68% |
| **Website** | [https://app.ondo.finance/assets/slvon](https://app.ondo.finance/assets/slvon) |

---

## Issuance, Custody and the Mint/Redeem Model

The Ondo Global Markets model is built around **KYC and transfer restrictions**:

- **Permissioned access.** Minting and redeeming are restricted to KYC-verified, eligible users. Ondo Global Markets is positioned for **non-US** retail and institutional users; it is **not offered to US persons**, and additional jurisdictional restrictions apply.
- **Off-chain custody.** Real SLV shares are held off-chain by the issuer's custodial arrangements; SLV itself custodies the physical silver. The token represents economic exposure to those shares.
- **Mint/redeem during market windows.** Ondo markets the ability to mint and redeem tokenized U.S. ETFs 24 hours a day, five days a week, with access to traditional exchange liquidity — but transfers and eligibility remain controlled.

### No shareholder rights

SLVON conveys **economic exposure only**. Holders are **not** registered SLV unitholders and have **no fund-governance or voting rights**. SLV is a commodity trust that does not pay a dividend; corporate actions, where applicable, are handled through the issuer.

---

## Tracking Mechanism

SLVON tracks SLV (and therefore the silver price) because eligible participants can mint and redeem against the off-chain shares, arbitraging premiums and discounts toward the reference price while the underlying market is open. Outside those windows — and given transfer restrictions that limit who can arbitrage — the token can deviate from the underlying.

---

## Platform & Chain Information

**Native chain: Ethereum (multi-chain issuance).**

| Chain | Address |
|---|---|
| Ethereum | `0xf3e4872e6a4cf365888d93b6146a2baa7348f1a4` |
| Binance Smart Chain | `0x8b872732b07be325a8803cdb480d9d20b6f8d11b` |
| Solana | `iy11ytbSGcUnrjE6Lfv78TFqxKyUESfku1FugS9ondo` |

---

## How & Where It Trades

| Venue | Type | Pair |
|---|---|---|
| Uniswap V3 (Ethereum) | DEX | SLVON / USDT |
| Uniswap V2 (Ethereum) | DEX | SLVON / DAI |

Secondary liquidity is on Ethereum DEXs (Uniswap V2/V3), with multi-chain representations on BNB Chain and Solana. Books are far thinner than the underlying SLV on NYSE Arca; large orders move the token and spreads widen when the US market is closed. Because silver itself can be volatile, the wrapper can show meaningful basis when the reference market is shut.

---

## Narrative & Catalysts

SLVON brings a **physical-silver / precious-metal hedge** on-chain as a composable token — the commodity member of [[ondo-finance|Ondo Global Markets]]' tokenized lineup and part of the broader **[[real-world-assets|RWA tokenization]]** wave.

- **On-chain macro / inflation hedge:** SLVON lets non-US, crypto-native portfolios add precious-metal exposure (an inflation and macro-stress hedge) without a US broker, tradeable 24/7 and usable on-chain.
- **Diversifier vs equity beta and crypto:** Silver historically behaves differently from both US equity indices and crypto, so an on-chain silver token can diversify a book dominated by [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]]-type beta or crypto assets.
- **RWA / tokenized-commodity build-out (2024–2026):** Commodity-backed wrappers extend tokenization beyond equities and ETFs, broadening the on-chain RWA menu.

### History / timeline

- **2026-04-09:** SLVON captured in the wiki's CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21:** Market-data snapshot — $58.90, market cap $25.93M, rank #702; -3.68% over the trailing 7 days, reflecting the silver price rather than a crypto move.

> *Only dated, verifiable events are listed; exact product-launch dates beyond those captured in snapshots are not asserted absent a confirmed source.*

---

## Risks (structured)

- **Issuer / custodian counterparty risk (two layers).** SLVON depends on Ondo Global Markets and its custodians holding real SLV shares, which in turn depend on physical silver held by the trust. Either layer breaking impairs the peg — a deeper custody chain than a single-wrapper product.
- **Redemption-gating / access risk.** Mint and redeem are KYC-gated and transfer-restricted; ordinary holders cannot redeem directly, and these restrictions **limit who can arbitrage the peg**, so deviations can persist.
- **Liquidity risk.** With a market cap around $25.9M, spreads widen and large orders move the token price, especially outside US hours.
- **Commodity price risk.** Silver is a volatile precious metal (more volatile than gold); the token carries that price risk on top of wrapper risk.
- **Tracking-error / weekend-gap risk.** Crypto trades 24/7 but NYSE Arca does not; SLVON can drift while SLV is closed and snap back at the next US open.
- **Regulatory risk.** KYC-gated, transfer-restricted, and **not for US persons**; eligibility and legality vary by jurisdiction, and tokenized-securities rules are still evolving.
- **Smart-contract / bridge risk.** Multi-chain deployment adds contract and bridge attack surface.
- **No shareholder rights / no recourse.** No fund-governance rights; holders are not registered owners of the underlying shares.

---

## Trading Playbook

- **Macro / inflation hedge:** Use SLVON as an on-chain precious-metal hedge for a non-US portfolio — a diversifier against equity-beta wrappers ([[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]], [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]]) and crypto risk in stress regimes.
- **Silver vs gold framing:** Silver is more volatile and more industrially sensitive than [[gold|gold]]; size accordingly and treat SLVON as a higher-beta metal hedge, not a pure store-of-value.
- **Pair / hedge construction:** SLVON can offset equity drawdowns when silver acts as a safe-haven, but the relationship is regime-dependent and not guaranteed; combine with broad-index exposure rather than relying on it alone.
- **Mind the weekend gap and thin books:** Restricted redemption and thin on-chain liquidity mean the token can drift from NAV when NYSE Arca is closed; size conservatively and check DEX depth before entering.

---

## See Also

- [[etf]] — exchange-traded funds; SLV is a physical-silver ETF
- [[gold]] — the closest precious-metal analogue covered in the wiki
- [[ondo-finance]] — the issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- [[crypto-markets]] · [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet for the Ondo Global Markets product mechanics.
