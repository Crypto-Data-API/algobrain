---
title: "Nasdaq xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, nasdaq, etf, tokenization]
aliases: ["QQQX", "Nasdaq-100 xStock", "QQQ xStock"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://xstocks.com/"
related: ["[[real-world-assets]]", "[[tokenized-stocks]]", "[[backed-finance]]", "[[nasdaq]]", "[[etf]]", "[[crypto-markets]]", "[[arbitrum]]"]
---

# Nasdaq xStock

**Nasdaq xStock** (QQQX) is a tokenized exchange-traded fund ("xStock") issued by [[backed-finance|Backed Finance]] that tracks the **Invesco QQQ Trust**, the ETF that follows the **Nasdaq-100** index of the 100 largest non-financial companies on the [[nasdaq|Nasdaq]] exchange. QQQX is **not** the ETF itself: it is an on-chain wrapper whose value is designed to follow the off-chain QQQ share, backed 1:1 by real ETF shares held in custody by the issuer. It is a [[real-world-assets|real-world asset (RWA)]] token, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, QQQX trades at **$740.93**, ranks **#640** by market capitalization with a market cap of **$30,199,138**, and is **-0.31%** over 24 hours and **+2.60%** over the trailing 7 days. The broader market context is risk-off: BTC sits near $64,180 and the Crypto Fear & Greed Index reads 22 (Extreme Fear). (Regime context only — at the 2026-06-22 macro snapshot the crypto tape remained in Extreme Fear, F&G 21, market-health 29/100; QQQX's value is set by the US equity session, not the crypto cycle.)

---

## What QQQX Actually Is

QQQX is a **[[tokenization|tokenized]] [[etf|ETF]]** — a blockchain token engineered to mirror the economics of the Invesco QQQ Trust, which in turn tracks the [[nasdaq|Nasdaq-100]]. It belongs to the **xStock** product line operated by [[backed-finance|Backed Finance]], a Switzerland-based issuer of tokenized securities. For every QQQX token in circulation, Backed (via its custodial arrangements) holds a corresponding QQQ share off-chain. The token's price *tracks* the ETF's price; it does not set it. The exposure chains through two wrappers: **Nasdaq-100 index → QQQ ETF → QQQX token**.

Because the subject is a wrapper around a basket, holders effectively get broad, single-token exposure to the Nasdaq-100's largest technology and growth names without holding each constituent or the ETF directly. It is a **broad-index** instrument — not a single-name bet like [[tesla-ondo-tokenized-stock|TSLAon]] or [[nvidia-xstock|NVDAx]] — though the Nasdaq-100 is heavily concentrated in a handful of mega-cap tech names, so QQQX carries more single-sector risk than a total-market wrapper such as [[sp500-xstock|SPYX]]. Two prices coexist:

- **The reference price** — what QQQ trades at on the Nasdaq during US market hours.
- **The token price** — what QQQX trades at on crypto venues 24/7, which can drift from the reference when traditional markets are closed or when secondary-market liquidity is thin.

### Architecture — how the wrapper works (Backed Finance model)

- **Issuer & custody:** [[backed-finance|Backed Finance AG]] (Switzerland) issues QQQX under EU/Swiss tokenized-securities frameworks; the backing QQQ shares are held with a regulated third-party custodian. Backed publishes reserve attestations so on-chain supply can be reconciled against custodied shares (**proof of reserves**).
- **1:1 collateral:** Each QQQX is backed 1:1 by a real QQQ share (or depositary-receipt equivalent) held off-chain.
- **Mint / redeem & KYC gating:** The primary market (mint/redeem) is permissioned to KYC'd, whitelisted participants; the secondary market is permissionless.
- **Oracle / price feed:** Integrators reference the underlying QQQ / Nasdaq-100 price via market-data and oracle feeds; fair value is the underlying NAV, enforced by primary-participant arbitrage.
- **24/7 token vs market-hours underlying:** QQQX trades 24/7 while the Nasdaq trades only in the US session, producing weekend/overnight basis risk.
- **Distributions / expense handling:** Nasdaq-100 dividends and QQQ's expense ratio are reflected through the issuer's terms (an economic adjustment, not a cash payout).
- **Settlement chains:** Solana SPL natively, with ERC-20 representations on Ethereum, BNB Chain and [[arbitrum|Arbitrum One]].

---

## Tracking & Peg

QQQX's fair value is the QQQ share price (and thus the Nasdaq-100). The peg holds through **primary-market arbitrage**: at a premium, whitelisted participants mint and sell; at a discount, they buy and redeem.

- **Premium / discount:** Minor deviations are normal on thin secondary books and compress at the US open.
- **Weekend-gap risk:** The dominant structural basis risk — with no live QQQ reference when the Nasdaq is closed, QQQX drifts on crypto sentiment and re-rates at the next open.
- **Concentration:** Because the Nasdaq-100 is top-heavy (mega-cap tech), a gap in one or two names (e.g. an AI mega-cap earnings surprise) moves QQQX more than it would a total-market wrapper.

---

## Comparison: QQQX vs alternatives

| Dimension | **QQQX** (Backed xStock) | **[[invesco-qqq-etf-ondo-tokenized-etf\|QQQon]]** (Ondo) | **[[sp500-xstock\|SPYX]]** (broad market) | **Holding real QQQ** (broker) |
|---|---|---|---|---|
| Underlying | QQQ / Nasdaq-100 (~100 names) | QQQ / Nasdaq-100 | SPY / S&P 500 (500 names) | QQQ / Nasdaq-100 |
| Issuer | [[backed-finance\|Backed Finance]] | [[ondo-finance\|Ondo Global Markets]] | Backed Finance | Invesco (QQQ sponsor) |
| Form | SPL + ERC-20, on-chain | ERC-20 + multi-chain | SPL + ERC-20 | Brokerage security |
| Trading hours | 24/7 | 24/7 | 24/7 | US market hours |
| Concentration | High (tech-heavy) | High (tech-heavy) | Lower (broad) | High (tech-heavy) |
| Shareholder rights | None | None | None | Full (via ETF) |
| US persons | Not offered | Not offered | Not offered | Available |
| Main extra risk | Issuer/custody, weekend gap, tech concentration | Same | Issuer/custody, weekend gap | None beyond market |

QQQX vs QQQon is mainly an **issuer/venue/liquidity** choice for the same exposure. QQQX vs [[sp500-xstock|SPYX]] is a **concentration choice**: tech-growth tilt (QQQX) versus broad market (SPYX).

---

## Key Facts

| Field | Detail |
|---|---|
| **Token ticker** | QQQX |
| **Underlying** | Invesco QQQ Trust / Nasdaq-100 index |
| **Issuer** | [[backed-finance|Backed Finance]] (xStocks) |
| **Backing** | 1:1 real QQQ ETF shares held in custody |
| **Standard** | SPL (Solana) / ERC-20 (EVM chains) |
| **Market cap rank** | #640 |
| **Market cap** | $30,199,138 |
| **Current price** | $740.93 |
| **24h change** | -0.31% |
| **7d change** | +2.60% |
| **Website** | [https://xstocks.com/](https://xstocks.com/) |

---

## Issuance, Custody and the Mint/Redeem Model

The xStock model separates two markets:

- **Primary market (permissioned):** Only KYC'd, whitelisted institutional participants can **mint** new QQQX (by delivering QQQ shares into custody) or **redeem** QQQX (burning tokens to receive the underlying value). This gatekeeping keeps the token supply collateralized 1:1.
- **Secondary market (permissionless):** Once minted, QQQX trades freely on centralized exchanges (e.g., Kraken) and DeFi venues (e.g., Orca on Solana). Any wallet can buy, sell or hold the token on the secondary market; whitelisting is required only to mint or redeem.

### No shareholder / fund rights

Holding QQQX confers **economic exposure only**. Token holders are **not** registered ETF shareholders and have no voting or fund-governance rights. Distributions and corporate actions, where applicable, are handled through the issuer rather than passed through as direct shareholder entitlements.

---

## Tracking Mechanism

QQQX stays close to QQQ through **arbitrage by primary participants**. If the token trades at a premium to the underlying ETF, whitelisted parties can mint and sell; if at a discount, they can buy and redeem. This keeps the peg honest while the underlying market is open and primary participants are active. Outside those windows, the token can deviate from net asset value.

---

## Platform & Chain Information

**Multi-chain (xStocks are issued across several chains).**

| Chain | Address |
|---|---|
| Arbitrum One | `0xa753a7395cae905cd615da0b82a53e0560f250af` |
| Ethereum | `0xa753a7395cae905cd615da0b82a53e0560f250af` |
| Binance Smart Chain | `0xa753a7395cae905cd615da0b82a53e0560f250af` |
| Solana | `Xs8S1uUs1zvS2p7iwtsG3b6fkhpvmwz4GYU3gWAmWHZ` |

---

## How & Where It Trades

| Venue | Type | Pair |
|---|---|---|
| Kraken | CEX | QQQX/USD |
| Orca (Solana) | DEX | QQQX / USDC |

Secondary liquidity is concentrated on Solana (where QQQX is issued natively) via DEXs such as Orca, with Kraken offering a CEX route for the xStocks line. Books are far shallower than the underlying QQQ; large orders move the token price and spreads widen when the US market is closed. EVM/Arbitrum/BNB representations exist primarily for composability.

---

## Narrative & Catalysts

QQQX brings the **Nasdaq-100 / US mega-cap tech benchmark** on-chain as a composable token — a core product of the **[[real-world-assets|RWA tokenization]]** wave.

- **On-chain index access:** Non-US wallets get diversified US large-cap tech beta without a US broker, usable as DeFi collateral and tradeable 24/7.
- **AI / mega-cap tech narrative:** The Nasdaq-100's heavy weighting toward AI and mega-cap technology makes QQQX the on-chain proxy for the dominant equity-market theme of the cycle.
- **RWA growth (2024–2026):** Index wrappers (Nasdaq-100, S&P 500) are the flagship issues as [[backed-finance|Backed]] and [[ondo-finance|Ondo]] compete to wrap the most liquid TradFi instruments.

### History / timeline

- **2025:** Backed Finance launches the **xStocks** brand; QQQX (QQQ / Nasdaq-100) is among the flagship index wrappers, issued Solana-native with EVM representations.
- **2026-04-09:** QQQX captured in the wiki's CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21:** Market-data snapshot — $740.93, market cap $30.20M, rank #640.

> *Only dated, verifiable events are listed; exact launch dates beyond the year are not asserted absent a confirmed source.*

---

## Risks (structured)

- **Issuer / custodian counterparty risk.** Holders rely entirely on [[backed-finance|Backed Finance]] and its custodians to hold real QQQ shares 1:1 and honor redemptions — a counterparty/centralization risk absent from owning QQQ in a brokerage account, and contingent on proof-of-reserves holding up.
- **Redemption-gating / access risk.** Mint and redeem are permissioned and KYC-gated; ordinary holders cannot redeem directly. If primary participants step back, peg enforcement weakens.
- **Liquidity risk.** With a market cap around $30.2M, spreads widen and large orders can move the token price away from fair value, especially outside US hours.
- **Tracking-error / weekend-gap risk.** Crypto trades 24/7 but the Nasdaq does not. When QQQ is closed, QQQX can drift on sentiment and snap back at the next US open.
- **Concentration risk.** The Nasdaq-100 is heavily weighted to a handful of mega-cap tech names, so QQQX is more exposed to single-name shocks than a broad-market wrapper like [[sp500-xstock|SPYX]].
- **Regulatory risk.** xStocks are marketed to **non-US** users and positioned around EU rules; availability and legality vary by jurisdiction, and tokenized-securities regulation is still evolving.
- **Smart-contract / bridge risk.** Multi-chain deployment adds contract and bridge attack surface.
- **No shareholder rights / no recourse.** No voting or fund-governance rights; token holders are not the registered owners of the underlying ETF shares.

---

## Trading Playbook

- **On-chain tech-beta core:** Use QQQX for diversified US large-cap tech exposure on-chain — broader than a single AI name, more concentrated than [[sp500-xstock|SPYX]].
- **Index vs single-name:** Prefer QQQX over [[tesla-ondo-tokenized-stock|TSLAon]] / [[nvidia-xstock|NVDAx]] when you want the tech *theme* rather than a single-company bet, accepting that the Nasdaq-100's top-heaviness still concentrates risk.
- **Crypto-book diversifier:** Equity-driven returns can dampen a crypto-heavy portfolio's volatility, though equity/crypto correlation rises in broad risk-off regimes.
- **Mind the weekend gap:** Avoid large positions over US-market closures expecting NAV pricing; QQQX can drift on crypto sentiment and re-rate at the next open.
- **Liquidity-aware sizing:** Check Solana/Orca depth before sizing; thin books mean meaningful slippage on large orders.

---

## See Also

- [[nasdaq]] — the exchange / Nasdaq-100 index the underlying ETF tracks
- [[etf]] — exchange-traded funds
- [[backed-finance]] — the xStock issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- [[crypto-markets]] · [[arbitrum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet for the xStocks product mechanics.
