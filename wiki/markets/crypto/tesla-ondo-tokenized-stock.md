---
title: "Tesla (Ondo Tokenized Stock)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, nasdaq, tokenization]
aliases: ["TSLAON", "TSLAon", "Tesla Ondo"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/tslaon"
related: ["[[real-world-assets]]", "[[tokenized-stocks]]", "[[ondo-finance]]", "[[tesla]]", "[[nasdaq]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# Tesla (Ondo Tokenized Stock)

**Tesla (Ondo Tokenized Stock)** (TSLAON) is a tokenized equity issued by **Ondo Global Markets** ([[ondo-finance|Ondo Finance]]) that tracks the shares of **Tesla, Inc.** listed on the [[nasdaq|Nasdaq]] as **NASDAQ: TSLA**. TSLAON is **not** the underlying stock itself: it is an on-chain wrapper whose value is designed to follow the off-chain TSLA share, backed by real shares custodied off-chain. It gives holders economic exposure comparable to holding TSLA, but **no** shareholder rights. It is a [[real-world-assets|real-world asset (RWA)]] token, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, TSLAON trades at **$400.51**, ranks **#837** by market capitalization with a market cap of **$19,773,521**, and is **-0.39%** over 24 hours and **-1.30%** over the trailing 7 days. The broader market context is risk-off: BTC sits near $64,180 and the Crypto Fear & Greed Index reads 22 (Extreme Fear). (Regime context only — at the 2026-06-22 macro snapshot the crypto tape remained in Extreme Fear, F&G 21, market-health 29/100; TSLAON's value is set by TSLA's US session, not the crypto cycle.)

---

## What TSLAON Actually Is

TSLAON is a **[[tokenization|tokenized]] single-name equity** issued under the **Ondo Global Markets** program — Ondo's framework for bringing tokenized U.S. equities and ETFs on-chain. Real TSLA shares are held in custody off-chain and the token is designed to track their value. The token *tracks* the share; it does not set it. Unlike the broad-index wrappers in the same lineup ([[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]], [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]]), TSLAON gives **concentrated, undiversified exposure to one company** — a directional bet rather than market beta. Two prices coexist:

- **The reference price** — what TSLA trades at on the Nasdaq during US market hours.
- **The token price** — what TSLAON trades at on crypto venues, which can drift from the reference when traditional markets are closed or liquidity is thin.

[[tesla|Tesla]] is among the most volatile large-cap US equities, so the tokenized wrapper inherits that volatility on top of the wrapper's own tracking and issuer risks.

### Architecture — how the wrapper works

- **Issuer & custody:** [[ondo-finance|Ondo Global Markets]] (the tokenized-securities arm of Ondo Finance) issues TSLAON; real TSLA shares are held off-chain by the issuer's custodial arrangements, with the token representing economic exposure to those shares.
- **Backing:** Each token is backed by real custodied TSLA shares; the token's fair value is the underlying TSLA price.
- **Mint / redeem & KYC gating:** Minting and redeeming are permissioned and KYC-gated to eligible, onboarded **non-US** users; the product is **not offered to US persons**. Ondo markets the ability to mint/redeem tokenized U.S. stocks 24/5 with access to traditional exchange liquidity.
- **Oracle / price feed:** Fair value is the TSLA reference price; integrators reference it via market-data and oracle feeds, with eligible participants arbitraging premiums/discounts on-chain.
- **24/7 token vs market-hours underlying:** TSLAON trades on crypto venues continuously while TSLA trades only in the US session — the source of weekend/overnight basis risk.
- **Distributions:** Tesla pays **no common dividend**, so dividend pass-through is not a live consideration; corporate actions, where applicable, are handled through the issuer.
- **Settlement chains:** Ethereum (canonical), BNB Smart Chain and Solana (see Contract Addresses).

---

## Comparison: TSLAON vs alternatives

| Dimension | **TSLAON** (Ondo single-name) | **[[nvidia-ondo-tokenized-stock\|NVDAon]]** (Ondo single-name) | **[[invesco-qqq-etf-ondo-tokenized-etf\|QQQon]]** (index) | **Holding real TSLA** (broker) |
|---|---|---|---|---|
| Underlying | One company (TSLA) | One company (NVDA) | ~100 names (Nasdaq-100) | One company (TSLA) |
| Issuer | [[ondo-finance\|Ondo Global Markets]] | Ondo Global Markets | Ondo Global Markets | Nasdaq-listed equity |
| Diversification | None (concentrated) | None (concentrated) | High (broad index) | None |
| Volatility | High (TSLA is volatile) | High | Moderate (basket) | High |
| Trading hours | 24/7 | 24/7 | 24/7 | US market hours |
| Shareholder rights | None | None | None | Full (voting) |
| US persons | Not offered | Not offered | Not offered | Available |
| Main extra risk | Issuer/custody + high single-name vol + weekend gap | Same | Issuer/custody, weekend gap | None beyond market |

TSLAON is a **directional single-name bet**: choose it over an index wrapper like [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]] only when you specifically want Tesla exposure rather than diversified beta. Versus a real broker TSLA position, you trade voting rights and full investor protections for 24/7 on-chain access and composability, at the cost of issuer/custody and tracking risk.

---

## Key Facts

| Field | Detail |
|---|---|
| **Token ticker** | TSLAON |
| **Underlying** | Tesla, Inc. (NASDAQ: TSLA) |
| **Issuer** | Ondo Global Markets ([[ondo-finance|Ondo Finance]]) |
| **Backing** | Real TSLA shares custodied off-chain |
| **Native chain** | Ethereum (also BNB Chain, Solana) |
| **Market cap rank** | #837 |
| **Market cap** | $19,773,521 |
| **Current price** | $400.51 |
| **24h change** | -0.39% |
| **7d change** | -1.30% |
| **Website** | [https://app.ondo.finance/assets/tslaon](https://app.ondo.finance/assets/tslaon) |

---

## Issuance, Custody and the Mint/Redeem Model

The Ondo Global Markets model is built around **KYC and transfer restrictions**:

- **Permissioned access.** Minting and redeeming are restricted to KYC-verified, eligible users. Ondo Global Markets is positioned for **non-US** retail and institutional users; it is **not offered to US persons**, and additional jurisdictional restrictions apply.
- **Off-chain custody.** Real TSLA shares are held off-chain by the issuer's custodial arrangements; the token represents economic exposure to those shares.
- **Mint/redeem during market windows.** Ondo markets the ability to mint and redeem tokenized U.S. stocks 24 hours a day, five days a week, with access to traditional exchange liquidity — but transfers and eligibility remain controlled.

### No shareholder rights

TSLAON conveys **economic exposure only**. Holders are **not** registered Tesla shareholders and have **no voting rights**. (Tesla pays no common dividend, so dividend pass-through is not a live consideration; corporate actions, where applicable, are handled through the issuer.)

---

## Tracking Mechanism

TSLAON tracks TSLA because eligible participants can mint and redeem against the off-chain shares, arbitraging premiums and discounts toward the reference price while the underlying market is open. Outside those windows — and given transfer restrictions that limit who can arbitrage — the token can deviate from the underlying.

---

## Platform & Chain Information

**Native chain: Ethereum (multi-chain issuance).**

| Chain | Address |
|---|---|
| Ethereum | `0xf6b1117ec07684d3958cad8beb1b302bfd21103f` |
| Binance Smart Chain | `0x2494b603319d4d9f9715c9f4496d9e0364b59d93` |
| Solana | `KeGv7bsfR4MheC1CkmnAVceoApjrkvBhHYjWb67ondo` |

---

## How & Where It Trades

| Venue | Type | Pair |
|---|---|---|
| Bitget | CEX | TSLAON/USDT |
| Uniswap V3 (Ethereum) | DEX | TSLAON / USDC |

TSLAON trades on the Ethereum-canonical Uniswap V3 market and on Bitget as a CEX route, with multi-chain representations on BNB Chain and Solana. Secondary liquidity is far thinner than the underlying TSLA on the Nasdaq; large orders move the token and spreads widen when the US market is closed. Because TSLA is itself a high-turnover, high-volatility stock, the on-chain wrapper can show wider swings and basis when the reference market is shut.

---

## Narrative & Catalysts

TSLAON brings one of the most actively traded US equities on-chain as a composable token — part of the **[[real-world-assets|RWA tokenization]]** wave and [[ondo-finance|Ondo Global Markets]]' single-name equity lineup (alongside [[nvidia-ondo-tokenized-stock|NVDAon]]).

- **On-chain single-name access:** Non-US wallets get directional Tesla exposure without a US broker, tradeable 24/7 and usable on-chain.
- **High-beta retail favourite:** Tesla is a magnet for directional and momentum traders; a tokenized wrapper extends that to crypto-native venues and after-hours windows.
- **RWA / tokenized-equity build-out (2024–2026):** Single-name wrappers complement the index products (SPYon, QQQon) as issuers race to bring liquid US equities on-chain.

### History / timeline

- **2026-04-09:** TSLAON captured in the wiki's CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21:** Market-data snapshot — $400.51, market cap $19.77M, rank #837.

> *Only dated, verifiable events are listed; exact product-launch dates beyond those captured in snapshots are not asserted absent a confirmed source.*

---

## Risks (structured)

- **Issuer / custodian counterparty risk.** Holders rely on [[ondo-finance|Ondo Global Markets]] and its custodians to hold real TSLA shares and honor redemptions — a counterparty/centralization risk absent from a brokerage position.
- **Redemption-gating / access risk.** Mint and redeem are KYC-gated and transfer-restricted; ordinary holders cannot redeem directly, and these restrictions also **limit who can arbitrage the peg**, so deviations can persist longer than for a freely redeemable instrument.
- **Liquidity risk.** With a market cap around $19.8M, spreads widen and large orders move the token price, especially outside US hours.
- **High underlying volatility.** Tesla shares are notably volatile; the token carries elevated price risk on top of wrapper risk — the dominant risk for a single-name wrapper.
- **Tracking-error / weekend-gap risk.** Crypto trades 24/7 but the Nasdaq does not; TSLAON can drift while TSLA is closed and snap back at the next US open.
- **Regulatory risk.** KYC-gated, transfer-restricted, and **not for US persons**; eligibility and legality vary by jurisdiction, and tokenized-securities rules are still evolving.
- **Smart-contract / bridge risk.** Multi-chain deployment adds contract and bridge attack surface.
- **No shareholder rights / no recourse.** No voting; holders are not registered owners of the underlying shares.

---

## Trading Playbook

- **Directional single-name bet:** Use TSLAON when you specifically want on-chain Tesla exposure — a concentrated, high-beta position, not market beta. For diversified exposure, prefer an index wrapper like [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]] or [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]].
- **Momentum / event trading:** Tesla's volatility and earnings/news sensitivity suit momentum and event-driven setups; the 24/7 token lets non-US, crypto-native traders express views outside US hours (with the caveat that the price can gap at the next open).
- **Size for volatility and thin books:** TSLAON combines high underlying volatility with thin on-chain liquidity; size conservatively and check DEX depth before entering.
- **Mind the weekend gap and arbitrage limits:** Restricted redemption means the peg can drift further than for a freely arbitraged instrument; do not assume tight NAV tracking when US markets are closed.

---

## See Also

- [[tesla]] — the underlying company (NASDAQ: TSLA)
- [[ondo-finance]] — the issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- [[nasdaq]] · [[crypto-markets]] · [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet for the Ondo Global Markets product mechanics.
