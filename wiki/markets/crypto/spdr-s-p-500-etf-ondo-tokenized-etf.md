---
title: "SPDR S&P 500 ETF (Ondo Tokenized ETF)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, sp500, tokenized-stocks]
aliases: ["SPYON", "SPYon", "Ondo SPY"]
entity_type: protocol
headquarters: "Decentralized (issued by Ondo Global Markets)"
website: "https://app.ondo.finance/assets/spyon"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[tokenization]]", "[[tokenized-stocks]]", "[[ondo-finance]]", "[[etf]]", "[[sp500]]"]
---

# SPDR S&P 500 ETF (Ondo Tokenized ETF)

**SPDR S&P 500 ETF (Ondo Tokenized ETF)** (SPYON) is a tokenized [[real-world-assets|real-world asset]]: an on-chain wrapper issued by **[[ondo-finance|Ondo Global Markets]]** on [[ethereum|Ethereum]] (canonical, also BNB Chain and Solana) that tracks the **SPDR S&P 500 ETF (SPY)** — the largest [[etf|ETF]] tracking the [[sp500|S&P 500]] index. Each SPYON gives holders economic exposure similar to owning a SPY share (with dividends reinvested), but it is **not the ETF share itself** — it is a tokenized claim whose price tracks SPY, backed by real ETF shares held off-chain. The exposure chains through two wrappers: **S&P 500 index → SPY ETF → SPYON token**. As of 2026-06-21 it traded at **$750.49**, ranked **#506** by market capitalization with a market cap of **~$41.92M**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

> *Regime context only (2026-06-22 macro snapshot): the broad crypto tape was in Extreme Fear (F&G 21, market-health 29/100, BTC ≈ $64,568). SPYON's value is set by the US equity session, not the crypto cycle — the existing token data block above is preserved unchanged.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SPYON |
| **Market Cap Rank** | #506 |
| **Market Cap** | $41,916,063 (~$41.92M) |
| **Current Price** | $750.49 |
| **24h Change** | +0.16% |
| **7d Change** | +0.80% |
| **Underlying asset** | SPDR S&P 500 ETF (SPY) |
| **Issuer** | Ondo Global Markets |
| **Tracks** | SPY share price / S&P 500 index (dividends reinvested) |
| **Categories** | Tokenized Assets, BNB Chain Ecosystem, Solana Ecosystem, Ethereum Ecosystem, Real World Assets (RWA), Tokenized Exchange-Traded Funds (ETFs), Ondo Tokenized Assets |
| **Website** | [https://app.ondo.finance/assets/spyon](https://app.ondo.finance/assets/spyon) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

SPYON is the [[ondo-finance|Ondo]]-tokenized version of the SPDR S&P 500 [[etf|ETF]], part of the **Ondo Global Markets** lineup of tokenized US equities and ETFs (alongside [[nvidia-ondo-tokenized-stock|NVDAon]] and [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]]). It gives holders broad [[sp500|S&P 500]] exposure comparable to holding a SPY share, with dividends reinvested into the token's value. Ondo's tokenized products are built so **non-US retail and institutional users** can mint and redeem 24/5, with the on-chain price kept in line with the underlying via traditional exchange liquidity. *Additional restrictions apply.*

The token is a **wrapper**: its on-chain price **tracks the off-chain SPY price**, and its backing is real SPY shares held off-chain in the Ondo structure. It therefore carries equity-market (index) risk rather than the flat-NAV profile of the cash/T-bill RWAs in this cluster.

---

## How the token works

- **Underlying asset / backing:** Real shares of the SPDR S&P 500 ETF (SPY) held off-chain within the Ondo Global Markets structure; each token represents economic exposure to one underlying ETF share.
- **Issuer:** **Ondo Global Markets** (the tokenized-securities arm of [[ondo-finance|Ondo Finance]]).
- **Price tracking:** The token tracks SPY (and thus the [[sp500|S&P 500]] index). Dividends are reinvested into the token's economic value.
- **Mint / redeem (issuance & redemption):** Issuance and redemption are **permissioned and KYC-gated** for eligible, onboarded non-US users. Minting causes Ondo to acquire SPY shares; redemption sells the shares and burns the token. This primary mint/redeem keeps the token tethered to SPY's price.
- **No shareholder rights:** Holders get **economic exposure only** — no fund/voting rights, no record-holder status in SPY; they hold a claim against the issuer's structure.
- **Transfer restrictions:** Secondary transfers can be limited to whitelisted / KYC'd addresses; the product is **not offered to US persons**.
- **Oracle / price feed:** Fair value is the underlying SPY/S&P 500 NAV; integrators reference it via market-data and oracle feeds, with primary-participant arbitrage enforcing the link on-chain.
- **Distributions / expense handling:** Unlike a cash-paying ETF position, S&P 500 dividends are **reinvested into the token's economic value**; SPY's expense ratio is absorbed through the issuer's structure rather than billed to holders.
- **Settlement chains:** Multi-chain — [[ethereum|Ethereum]] (canonical), BNB Smart Chain, and Solana (see Contract Addresses below).

---

## Tracking & Peg

SPYON's fair value is the SPY share price (and thus the [[sp500|S&P 500]]). The peg is held by **primary-market arbitrage**: eligible, KYC'd participants mint SPYON when it trades rich to SPY and redeem when it trades cheap, pulling the token back to NAV while US markets are open.

- **Premium / discount:** Small deviations are normal given thin secondary liquidity; they compress at the US open when arbitrageurs can act.
- **Tracking error:** Because dividends are reinvested into the token, SPYON's path is total-return-like rather than price-return — a structural (and benign) difference from the headline SPY price.
- **Weekend-gap risk:** With no live SPY reference outside the US session, SPYON can drift on crypto-market sentiment overnight and on weekends, then re-rate to the new SPY print at the next open.
- **Broad-index advantage:** As a 500-name basket, SPYON is far less exposed to single-stock gaps than single-name wrappers like [[tesla-ondo-tokenized-stock|TSLAon]], so tracking is generally cleaner.

---

## Comparison: SPYON vs alternatives

| Dimension | **SPYON** (Ondo) | **[[sp500-xstock\|SPYX]]** (Backed xStock) | **Holding real SPY** (broker) | **Single-name token** (e.g. [[tesla-ondo-tokenized-stock\|TSLAon]]) |
|---|---|---|---|---|
| Underlying | SPY / S&P 500 (500 names) | SPY / S&P 500 (500 names) | SPY / S&P 500 (500 names) | One company |
| Issuer | [[ondo-finance\|Ondo Global Markets]] | [[backed-finance\|Backed Finance]] | State Street (SPY sponsor) | Ondo / Backed |
| Canonical chain | Ethereum (also BNB, Solana) | Solana (also ETH/BNB/Arbitrum) | n/a | Ethereum / Solana |
| Dividends | Reinvested into token | Reflected via issuer terms | Cash payout to holder | n/a (TSLA pays none) |
| Trading hours | 24/7 | 24/7 | US market hours | 24/7 |
| Shareholder rights | None (economic claim) | None (economic claim) | Full (via ETF) | None |
| US persons | Not offered | Not offered | Available | Not offered |
| Diversification | High (broad index) | High (broad index) | High (broad index) | None (concentrated) |
| Main extra risk | Issuer/custody, weekend gap | Issuer/custody, weekend gap | None beyond market | Issuer + high single-name vol |

SPYON vs [[sp500-xstock|SPYX]] is essentially an **issuer/chain/liquidity** choice for the same SPY exposure — Ondo is Ethereum-canonical and reinvests dividends into the token, while Backed is Solana-native. Versus a real broker SPY position, the trade-off is on-chain composability and 24/7 access against added issuer, custody and tracking risk.

---

| Metric | Value |
|---|---|
| **Circulating Supply** | 52,527 SPYON |
| **Total Supply** | 52,527 SPYON |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $35.62M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $701.14 (2026-01-28) |
| **All-Time Low** | $632.87 (2026-03-30) |
| **24h Change** | +0.16% |
| **7d Change** | +0.80% |

Because the token tracks SPY, its price history follows the S&P 500 index rather than crypto-market cycles. The modest 7-day move reflects broad-market action.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xfedc5f4a6c38211c1338aa411018dfaf26612c08` |
| Binance Smart Chain | `0x6a708ead771238919d85930b5a0f10454e1c331a` |
| Solana | `k18WJUULWheRkSpSquYGdNNmtuE2Vbw1hpuUi92ondo` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XFEDC5F4A6C38211C1338AA411018DFAF26612C08/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.ondo.finance/assets/spyon](https://app.ondo.finance/assets/spyon) |
| **Twitter** | [@ondofinance](https://twitter.com/ondofinance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.49M |
| **Market Cap Rank** | #512 |
| **24h Range** | $676.72 — $681.67 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Off-chain dependency:** Value depends entirely on real SPY shares and the Ondo structure holding them; on-chain settlement cannot enforce delivery of the ETF.
- **Issuer / custody risk:** Concentrated reliance on Ondo Global Markets and its broker/custody partners.
- **No shareholder rights:** Holders forgo ETF/voting rights and direct ownership; they hold an economic claim, not SPY shares.
- **Regulatory & transfer restrictions:** Permissioned, KYC-gated, and **not available to US persons**; secondary transfers may be whitelist-restricted. Tokenized-securities regulation is unsettled.
- **Market-hours / tracking risk:** SPY trades on US exchange hours while the token trades 24/7, so the token can deviate from SPY's last price during closures; tracking relies on Ondo's arbitrage/market-maker mechanics.
- **Equity-market risk:** Full exposure to S&P 500 drawdowns and volatility.
- **Liquidity & smart-contract risk:** Secondary on-chain liquidity (e.g. Uniswap V3) can be thin; multi-chain deployment adds contract and bridge attack surface.

---

## Narrative & Catalysts

SPYON is [[ondo-finance|Ondo Global Markets]]' on-chain wrapper for the single most recognised US equity benchmark — a flagship product of the **[[real-world-assets|RWA tokenization]]** wave.

- **On-chain index access for non-US users:** SPYON offers broad US large-cap beta to wallets that cannot access SPY through a US broker, in a composable, 24/7 form usable as DeFi collateral.
- **Ondo Global Markets build-out:** SPYON sits in Ondo's tokenized-equities lineup alongside [[invesco-qqq-etf-ondo-tokenized-etf|QQQon]] and single names like [[tesla-ondo-tokenized-stock|TSLAon]] and [[nvidia-ondo-tokenized-stock|NVDAon]], extending Ondo's RWA franchise beyond cash/T-bill products into equity beta.
- **RWA growth (2024–2026):** Broad-index wrappers (S&P 500, Nasdaq-100) are the marquee issues as Ondo and [[backed-finance|Backed]] compete to wrap the most liquid TradFi instruments on-chain.

### History / timeline

- **2025-12 / 2026-Q1:** Price-history extremes recorded — all-time high $701.14 (2026-01-28) and all-time low $632.87 (2026-03-30), reflecting the underlying SPY/S&P 500 path rather than a crypto cycle.
- **2026-04-09:** SPYON captured in the wiki's CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); listing data last updated 2026-04-09.
- **2026-06-21:** Market-data snapshot — $750.49, market cap ~$41.92M, rank #506.

> *Only dated, verifiable events are listed; exact product-launch dates beyond those captured in snapshots are not asserted absent a confirmed source.*

---

## Trading Playbook

- **On-chain US-beta core:** Use SPYON as a broad-index, lower-volatility building block for non-US, on-chain portfolios — the Ethereum-canonical route to "owning the US market" without a broker.
- **Total-return holding:** Because dividends reinvest into the token, SPYON suits a buy-and-hold beta sleeve where you want compounding without managing cash distributions.
- **Index vs single-name:** Prefer SPYON over single-name tokens (e.g. [[tesla-ondo-tokenized-stock|TSLAon]]) when the goal is diversified beta rather than a directional company bet.
- **Crypto-book diversifier:** Equity-driven returns can dampen a crypto-heavy book's volatility, though equity/crypto correlation rises in broad risk-off regimes.
- **Mind the weekend gap & liquidity:** Avoid large positions over US-market closures expecting NAV pricing; check Uniswap V3 / on-chain depth before sizing, as thin books mean meaningful slippage.

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
- [[sp500]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original listing snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific Ondo source document ingested yet.
