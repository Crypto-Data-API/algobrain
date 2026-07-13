---
title: "Micron Technology (Ondo Tokenized Stock)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenized-stock, stocks]
aliases: ["MUON", "Micron Ondo Tokenized Stock"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/muon"
related: ["[[real-world-assets]]", "[[ondo-finance]]", "[[crypto-markets]]", "[[ethereum]]", "[[tokenization]]"]
---

# Micron Technology (Ondo Tokenized Stock)

**Micron Technology (Ondo Tokenized Stock)** (ticker **MUON**) is a [[tokenization|tokenized]] [[real-world-assets|tokenized equity]] issued by [[ondo-finance|Ondo Finance]] through its **Ondo Global Markets** product on [[ethereum|Ethereum]] (bridged to BNB Chain and Solana). Each token is designed to track the price of **Micron Technology's US-listed common stock (NASDAQ: MU)** — the memory and storage semiconductor maker (DRAM and NAND flash) — giving non-US holders economic exposure similar to owning MU, including reinvested dividends. Within the Ondo Global Markets line, MUON is a **single-stock, high-beta semiconductor expression** rather than a diversified beta building block.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | MUON |
| **Underlying equity** | Micron Technology (NASDAQ: MU) |
| **Issuer / wrapper** | Ondo Global Markets (Ondo Finance) |
| **Current price** | $1,132.78 |
| **Market cap** | $83.65M |
| **Market cap rank** | #302 |
| **24h volume** | $1,105,292 |
| **24h change** | +0.38% |
| **Circulating supply** | ~73,843 MUON |
| **Total supply** | ~73,843 MUON |
| **All-time high** | $1,157.13 (2026-06-18) |
| **All-time low** | $115.92 (2025-09-02) |
| **Chains** | Ethereum (native), BNB Chain, Solana |

> Note: the high MUON unit price reflects a tokenized claim whose value tracks the MU share price; per-token price and supply differ from a 1-share-per-token reading, but the economic exposure is to MU.

MUON's value is anchored to the MU US trading session, not the crypto cycle. As of 2026-06-23 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads 21 (Extreme Fear; bottoming/accumulation regime) with Bitcoin ~$64,568 and ETH ~$1,737, yet MUON printed a fresh all-time high on 2026-06-18 — underlying semiconductor strength, not crypto sentiment.

---

## Architecture: How the Wrapper Works

MUON is a **tokenized claim on the underlying MU equity** held within Ondo Global Markets. It is not a synthetic or derivative; each token corresponds to economic exposure to real Micron Technology shares custodied within the Ondo structure, with dividends reflected back to holders.

- **Issuer / wrapper:** [[ondo-finance|Ondo Finance]] via Ondo Global Markets structures and issues the token as a digital claim on a real MU share.
- **Underlying asset:** Micron Technology common stock (MU), a US-listed equity.
- **1:1 backing & custody:** Underlying shares are held within Ondo's regulated brokerage/custody arrangements for Ondo Global Markets; the on-chain token mirrors that custodied position, with proof-of-reserves / attestation as the integrity anchor.
- **Mint / redeem & KYC gating:** Eligible users can mint and redeem against the underlying, with primary market access running 24 hours a day, five days a week (aligned to US equity availability through Ondo's infrastructure). Access is **restricted to non-US persons** (retail and institutional) who pass Ondo's KYC/AML onboarding; US persons are excluded, and additional jurisdictional restrictions apply.
- **Oracle / price feed:** The token's reference value derives from MU's market price; on-chain price tracks that feed, anchored by mint/redeem arbitrage during US hours.
- **24/7 token vs. market-hours underlying:** MUON transfers 24/7 on-chain; MU trades only during US market hours, so tight tracking is strongest when the underlying market is open.
- **Distributions:** Micron pays a (small) dividend; distributions are reflected in the token's reference value rather than paid out separately.
- **Regulatory wrapper:** Offered through Ondo Global Markets under a non-US distribution framework; a tokenized representation of a regulated US security, not a US-registered offering to US investors.

See [[ondo-finance]] for the issuer, and [[real-world-assets]] for the asset class.

---

## Tracking & Peg

- **Tracking:** The on-chain price is designed to track MU's underlying equity price. Deviations can occur off-hours, in thin liquidity, or when arbitrage to the primary mint/redeem channel is constrained.
- **Weekend-gap risk:** MU does not trade on weekends or US holidays, so MUON's on-chain price is stale relative to news during those windows; a gap at Monday's open will gap MUON.
- **Single-name volatility:** Unlike the diversified ETF tokens in the Ondo set, MUON carries concentrated single-stock risk — Micron is a highly cyclical memory-chip maker whose share price swings with the DRAM/NAND pricing cycle and AI/datacenter demand. Note the all-time low of $115.92 (2025-09-02) versus the recent high near $1,157, illustrating the wide range.
- **No duration / rate risk:** As an equity, MUON has none of the interest-rate duration risk carried by the bond ETF tokens ([[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]], [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]]).

---

## Comparison vs. Alternatives

| Dimension | **MUON (Ondo)** | Holding real MU | CRCLON (Ondo) | IVVON (Ondo) |
|---|---|---|---|---|
| Underlying | Micron (memory chips) | Micron (memory chips) | Circle (stablecoin issuer) | S&P 500 index |
| Concentration | Single stock | Single stock | Single stock | 500 stocks (diversified) |
| Beta profile | High (cyclical semis) | High (cyclical semis) | High (fintech/newly public) | Market beta |
| Access | Non-US KYC, on-chain 24/7 | Global brokerage | Non-US KYC | Non-US KYC |
| Backing | Real MU shares, off-chain | Direct share ownership | Real CRCL shares | Real IVV shares |
| Role in book | Semis high-beta bet | Semis high-beta bet | Stablecoin-issuer bet | Diversified equity core |

MUON is the **high-beta semiconductor satellite** of the Ondo set: where [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]] is the diversified core, MUON is a concentrated cyclical bet on the memory-chip cycle and AI/datacenter demand. Versus holding MU directly, the trade-off is on-chain composability and non-US access against custodial counterparty and peg risk.

---

## How & Where It Trades

- **Primary market:** Mint/redeem via Ondo Global Markets for eligible users, gated to US equity hours.
- **Secondary market:** On-chain secondary liquidity across Ethereum, BNB Chain, and Solana. CoinGecko showed no deep secondary exchange pair at snapshot time; primary mint/redeem is the main path.
- **Liquidity:** Modest — large orders rely on the primary channel rather than DEX depth.
- **Hours:** Token trades on-chain 24/7, but tight tracking is strongest when the underlying market is open.

---

## Narrative & Catalysts

MUON's thesis is **on-chain access to a high-beta semiconductor name**: it lets non-US holders express a view on the memory-chip cycle and AI/datacenter-driven DRAM/HBM demand as a composable on-chain token. Catalysts include the broader RWA tokenization wave led by Ondo, the AI/HBM (high-bandwidth memory) demand cycle that drives Micron's earnings, and growing appetite for single-stock tokenized equities on-chain.

### History / Timeline

- **2026-04-09** — MUON captured in the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2025-09-02** — All-time low of $115.92.
- **2026-06-18** — Fresh all-time high of $1,157.13, consistent with strength in the underlying semiconductor name.
- **2026-06-21** — Market snapshot: $1,132.78, ~$83.65M market cap, rank #302.

---

## Risks

- **Issuer / custodian counterparty risk:** Holders depend on Ondo Global Markets and its custody of the underlying MU shares; backing is custodial, not trustless.
- **Equity / cyclical risk:** Micron is a highly cyclical memory-chip maker; the underlying equity is volatile (note the wide ATH/ATL range) and exposure flows straight through to the token.
- **Concentration risk:** Single-name exposure with no diversification, unlike the ETF tokens in the set.
- **Tracking / liquidity risk:** Thin on-chain liquidity can cause deviation from MU, especially outside US market hours.
- **Redemption-gating risk:** Mint/redeem is KYC-gated, non-US-only, and market-hours-bound; halted creations can break the peg arbitrage.
- **Regulatory risk:** Tokenized equities face an evolving global regulatory landscape; access restrictions (non-US only) can change.
- **Smart-contract / bridge risk:** Multi-chain deployment (Ethereum, BNB Chain, Solana) adds contract and bridge attack surface.

---

## Trading Playbook

- **Semis high-beta satellite:** Use MUON as a concentrated, high-beta semiconductor expression alongside a diversified core like [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]] — size it small relative to the core given single-name volatility.
- **Cycle view:** Hold MUON to express a constructive DRAM/NAND or AI-memory (HBM) demand thesis; exit on signs of memory oversupply or cycle rollover.
- **Hedge with ballast:** Pair high-beta MUON exposure with bond tokens ([[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]], [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]]) to dampen portfolio drawdowns.
- **Execute in US hours:** Transact size while mint/redeem arbitrage is live; avoid large weekend trades into a stale price.

---

## Macro Backdrop (2026-06-23)

The Crypto Fear & Greed Index reads **21 (Extreme Fear)** with market-health 29/100 (bearish, bottoming/accumulation), Bitcoin ~$64,568 and ETH ~$1,737. Even so, MUON's all-time high days earlier reflects underlying-equity strength rather than crypto-market sentiment — a reminder that tokenized single-stock products track their underlying first.

---

## See Also

- [[real-world-assets]]
- [[ondo-finance]]
- [[circle-internet-group-ondo-tokenized-stock]] — sibling single-stock token
- [[ishares-core-s-p-500-etf-ondo-tokenized-etf]] — diversified equity core
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko market snapshot, 2026-06-21
- General market knowledge; no specific wiki source ingested yet.
