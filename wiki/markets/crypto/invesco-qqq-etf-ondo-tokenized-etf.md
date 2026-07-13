---
title: "Invesco QQQ ETF (Ondo Tokenized ETF)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, nasdaq, tokenized-stocks]
aliases: ["QQQON", "QQQon", "Ondo QQQ"]
entity_type: protocol
headquarters: "Decentralized (issued by Ondo Global Markets)"
website: "https://app.ondo.finance/assets/qqqon"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[tokenization]]", "[[tokenized-stocks]]", "[[ondo-finance]]", "[[etf]]"]
---

# Invesco QQQ ETF (Ondo Tokenized ETF)

**Invesco QQQ ETF (Ondo Tokenized ETF)** (QQQON) is a tokenized [[real-world-assets|real-world asset]]: an on-chain wrapper issued by **[[ondo-finance|Ondo Global Markets]]** on [[ethereum|Ethereum]] (canonical, also BNB Chain and Solana) that tracks the **Invesco QQQ [[etf|ETF]]** — the ETF tracking the Nasdaq-100 index of the largest non-financial Nasdaq-listed companies. Each QQQON gives holders economic exposure similar to owning a QQQ share (with dividends reinvested), but it is **not the ETF share itself** — it is a tokenized claim whose price tracks QQQ, backed by real ETF shares held off-chain. The exposure chains through two wrappers: **Nasdaq-100 index → QQQ ETF → QQQON token**. As of 2026-06-21 it traded at **$740.36**, ranked **#544** by market capitalization with a market cap of **~$38.12M**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

> *Regime context only (2026-06-22 macro snapshot): the broad crypto tape was in Extreme Fear (F&G 21, market-health 29/100, BTC ≈ $64,568). QQQON's value is set by the US equity session, not the crypto cycle — the existing token data block above is preserved unchanged.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | QQQON |
| **Market Cap Rank** | #544 |
| **Market Cap** | $38,117,920 (~$38.12M) |
| **Current Price** | $740.36 |
| **24h Change** | -0.05% |
| **7d Change** | +2.15% |
| **Underlying asset** | Invesco QQQ ETF (QQQ) |
| **Issuer** | Ondo Global Markets |
| **Tracks** | QQQ share price / Nasdaq-100 index (dividends reinvested) |
| **Categories** | Tokenized Assets, BNB Chain Ecosystem, Solana Ecosystem, Ethereum Ecosystem, Real World Assets (RWA), Binance Alpha Spotlight, Tokenized Exchange-Traded Funds (ETFs), Ondo Tokenized Assets |
| **Website** | [https://app.ondo.finance/assets/qqqon](https://app.ondo.finance/assets/qqqon) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

QQQON is the [[ondo-finance|Ondo]]-tokenized version of the Invesco QQQ [[etf|ETF]], part of the **Ondo Global Markets** lineup of tokenized US equities and ETFs (alongside [[nvidia-ondo-tokenized-stock|NVDAon]] and [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]]). It gives holders Nasdaq-100 / large-cap tech exposure comparable to holding a QQQ share, with dividends reinvested into the token's value. Ondo's tokenized products are built so **non-US retail and institutional users** can mint and redeem 24/5, with the on-chain price kept in line with the underlying via traditional exchange liquidity. *Additional restrictions apply.*

The token is a **wrapper**: its on-chain price **tracks the off-chain QQQ price**, and its backing is real QQQ shares held off-chain in the Ondo structure. It therefore carries equity-market (Nasdaq-100) risk rather than the flat-NAV profile of the cash/T-bill RWAs in this cluster (note the +2.15% 7-day move, mirroring tech-heavy index action).

---

## How the token works

- **Underlying asset / backing:** Real shares of the Invesco QQQ ETF (QQQ) held off-chain within the Ondo Global Markets structure; each token represents economic exposure to one underlying ETF share.
- **Issuer:** **Ondo Global Markets** (the tokenized-securities arm of [[ondo-finance|Ondo Finance]]).
- **Price tracking:** The token tracks QQQ (and thus the Nasdaq-100 index). Dividends are reinvested into the token's economic value.
- **Mint / redeem (issuance & redemption):** Issuance and redemption are **permissioned and KYC-gated** for eligible, onboarded non-US users. Minting causes Ondo to acquire QQQ shares; redemption sells the shares and burns the token, keeping the token tethered to QQQ's price.
- **No shareholder rights:** Holders get **economic exposure only** — no fund/voting rights, no record-holder status in QQQ; they hold a claim against the issuer's structure.
- **Transfer restrictions:** Secondary transfers can be limited to whitelisted / KYC'd addresses; the product is **not offered to US persons**.
- **Oracle / price feed:** Fair value is the underlying QQQ/Nasdaq-100 NAV; integrators reference it via market-data and oracle feeds, with primary-participant arbitrage enforcing the link on-chain.
- **Distributions / expense handling:** Nasdaq-100 dividends are **reinvested into the token's economic value** (a total-return path), and QQQ's expense ratio is absorbed through the issuer's structure rather than billed to holders.
- **Settlement chains:** Multi-chain — [[ethereum|Ethereum]] (canonical), BNB Smart Chain, and Solana (see Contract Addresses below).

---

## Tracking & Peg

QQQON's fair value is the QQQ share price (and thus the Nasdaq-100). The peg is held by **primary-market arbitrage**: eligible, KYC'd participants mint QQQON when it trades rich to QQQ and redeem when it trades cheap, pulling the token back to NAV while US markets are open.

- **Premium / discount:** Small deviations are normal on thin secondary liquidity; they compress at the US open when arbitrageurs can act.
- **Tracking error:** Dividend reinvestment makes QQQON's path total-return-like rather than price-return — a structural (benign) difference from the headline QQQ price.
- **Weekend-gap risk:** With no live QQQ reference outside the US session, QQQON drifts on crypto sentiment overnight and on weekends, then re-rates at the next open.
- **Concentration:** The Nasdaq-100 is top-heavy (mega-cap tech), so a gap in one or two names moves QQQON more than it would a broad-market wrapper like [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]].

---

## Comparison: QQQON vs alternatives

| Dimension | **QQQON** (Ondo) | **[[nasdaq-xstock\|QQQX]]** (Backed xStock) | **[[spdr-s-p-500-etf-ondo-tokenized-etf\|SPYon]]** (broad market) | **Holding real QQQ** (broker) |
|---|---|---|---|---|
| Underlying | QQQ / Nasdaq-100 (~100 names) | QQQ / Nasdaq-100 | SPY / S&P 500 (500 names) | QQQ / Nasdaq-100 |
| Issuer | [[ondo-finance\|Ondo Global Markets]] | [[backed-finance\|Backed Finance]] | Ondo Global Markets | Invesco (QQQ sponsor) |
| Canonical chain | Ethereum (also BNB, Solana) | Solana (also ETH/BNB/Arbitrum) | Ethereum (also BNB, Solana) | n/a |
| Dividends | Reinvested into token | Reflected via issuer terms | Reinvested into token | Cash payout to holder |
| Trading hours | 24/7 | 24/7 | 24/7 | US market hours |
| Concentration | High (tech-heavy) | High (tech-heavy) | Lower (broad) | High (tech-heavy) |
| Shareholder rights | None | None | None | Full (via ETF) |
| US persons | Not offered | Not offered | Not offered | Available |
| Main extra risk | Issuer/custody, weekend gap, tech concentration | Same | Issuer/custody, weekend gap | None beyond market |

QQQON vs [[nasdaq-xstock|QQQX]] is mainly an **issuer/chain/liquidity** choice for the same Nasdaq-100 exposure (Ondo is Ethereum-canonical and reinvests dividends; Backed is Solana-native). QQQON vs [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]] is a **concentration choice**: tech-growth tilt versus broad market.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 45,896 QQQON |
| **Total Supply** | 45,896 QQQON |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $27.74M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $641.53 (2025-12-27) |
| **All-Time Low** | $556.67 (2026-03-31) |
| **24h Change** | -0.05% |
| **7d Change** | +2.15% |

Because the token tracks QQQ, its price history follows the Nasdaq-100 index rather than crypto-market cycles. The +2.15% 7-day move reflects tech-sector equity action.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x0e397938c1aa0680954093495b70a9f5e2249aba` |
| Binance Smart Chain | `0x0cde6936d305d5b34667fc46425e852efd73559a` |
| Solana | `HrYNm6jTQ71LoFphjVKBTdAE4uja7WsmLG8VxB8ondo` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X0E397938C1AA0680954093495B70A9F5E2249ABA/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.ondo.finance/assets/qqqon](https://app.ondo.finance/assets/qqqon) |
| **Twitter** | [@ondofinance](https://twitter.com/ondofinance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.46M |
| **Market Cap Rank** | #559 |
| **24h Range** | $603.48 — $610.46 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Off-chain dependency:** Value depends entirely on real QQQ shares and the Ondo structure holding them; on-chain settlement cannot enforce delivery of the ETF.
- **Issuer / custody risk:** Concentrated reliance on Ondo Global Markets and its broker/custody partners.
- **No shareholder rights:** Holders forgo ETF/voting rights and direct ownership; they hold an economic claim, not QQQ shares.
- **Regulatory & transfer restrictions:** Permissioned, KYC-gated, and **not available to US persons**; secondary transfers may be whitelist-restricted. Tokenized-securities regulation is unsettled.
- **Market-hours / tracking risk:** QQQ trades on US exchange hours while the token trades 24/7, so the token can deviate from QQQ's last price during closures; tracking relies on Ondo's arbitrage/market-maker mechanics.
- **Equity-market / concentration risk:** Full exposure to Nasdaq-100 volatility, which is heavily weighted toward a handful of mega-cap tech names.
- **Liquidity & smart-contract risk:** Secondary on-chain liquidity (e.g. Uniswap V3) can be thin; multi-chain deployment adds contract and bridge attack surface.

---

## Narrative & Catalysts

QQQON is [[ondo-finance|Ondo Global Markets]]' on-chain wrapper for the **Nasdaq-100 / US mega-cap tech** benchmark — a flagship product of the **[[real-world-assets|RWA tokenization]]** wave.

- **On-chain index access for non-US users:** QQQON offers diversified US large-cap tech beta to wallets that cannot access QQQ through a US broker, in a composable, 24/7 form usable as DeFi collateral.
- **AI / mega-cap tech narrative:** The Nasdaq-100's heavy AI and mega-cap-tech weighting makes QQQON the Ethereum-canonical on-chain proxy for the dominant equity theme of the cycle.
- **Ondo Global Markets build-out:** QQQON sits alongside [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]] and single names like [[tesla-ondo-tokenized-stock|TSLAon]] and [[nvidia-ondo-tokenized-stock|NVDAon]] in Ondo's tokenized-equities lineup.

### History / timeline

- **2025-12 / 2026-Q1:** Price-history extremes recorded — all-time high $641.53 (2025-12-27) and all-time low $556.67 (2026-03-31), reflecting the underlying QQQ/Nasdaq-100 path rather than a crypto cycle.
- **2026-04-09:** QQQON captured in the wiki's CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); listing data last updated 2026-04-09.
- **2026-06-21:** Market-data snapshot — $740.36, market cap ~$38.12M, rank #544.

> *Only dated, verifiable events are listed; exact product-launch dates beyond those captured in snapshots are not asserted absent a confirmed source.*

---

## Trading Playbook

- **On-chain tech-beta core:** Use QQQON for diversified US large-cap tech exposure on-chain — broader than a single AI name, more concentrated than [[spdr-s-p-500-etf-ondo-tokenized-etf|SPYon]].
- **Total-return holding:** Dividends reinvest into the token, so QQQON suits a buy-and-hold tech-beta sleeve without managing cash distributions.
- **Index vs single-name:** Prefer QQQON over [[tesla-ondo-tokenized-stock|TSLAon]] / [[nvidia-ondo-tokenized-stock|NVDAon]] when you want the tech *theme* rather than a single-company bet, accepting the Nasdaq-100's top-heaviness still concentrates risk.
- **Crypto-book diversifier:** Equity-driven returns can dampen a crypto-heavy book's volatility, though equity/crypto correlation rises in broad risk-off regimes.
- **Mind the weekend gap & liquidity:** Avoid large positions over US-market closures expecting NAV pricing; check Uniswap V3 / on-chain depth before sizing.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[real-world-assets]]
- [[tokenization]]
- [[tokenized-stocks]]
- [[ondo-finance]]
- [[etf]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original listing snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific Ondo source document ingested yet.
