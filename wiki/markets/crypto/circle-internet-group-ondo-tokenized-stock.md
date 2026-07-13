---
title: "Circle Internet Group (Ondo Tokenized Stock)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenized-stock, stocks]
aliases: ["CRCLON", "Circle Ondo Tokenized Stock"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/crclon"
related: ["[[real-world-assets]]", "[[ondo-finance]]", "[[circle]]", "[[crypto-markets]]", "[[ethereum]]", "[[usdc]]", "[[tokenization]]"]
---

# Circle Internet Group (Ondo Tokenized Stock)

**Circle Internet Group (Ondo Tokenized Stock)** (ticker **CRCLON**) is a [[tokenization|tokenized]] [[real-world-assets|tokenized equity]] issued by [[ondo-finance|Ondo Finance]] through its **Ondo Global Markets** product on [[ethereum|Ethereum]] (bridged to BNB Chain and Solana). Each token is designed to track the price of **Circle Internet Group's US-listed common stock (NYSE: CRCL)** — the company behind the [[usdc|USDC]] stablecoin — giving non-US holders economic exposure similar to owning CRCL, including reinvested dividends. Within the Ondo Global Markets line, CRCLON is a **single-stock, stablecoin-issuer-equity expression** rather than a diversified beta building block, and a notable case of on-chain exposure to the equity of a core crypto-infrastructure company.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | CRCLON |
| **Underlying equity** | Circle Internet Group (NYSE: CRCL) |
| **Issuer / wrapper** | Ondo Global Markets (Ondo Finance) |
| **Current price** | $80.62 |
| **Market cap** | $114.47M |
| **Market cap rank** | #247 |
| **24h volume** | $508,248 |
| **24h change** | +0.87% |
| **Circulating supply** | ~1.42M CRCLON |
| **Total supply** | ~1.42M CRCLON |
| **All-time high** | $158.37 (2025-10-10) |
| **All-time low** | $47.99 (2026-02-06) |
| **Chains** | Ethereum (native), BNB Chain, Solana |

CRCLON's value is anchored to the CRCL US trading session, not the crypto cycle, though Circle's business (USDC) makes the equity partly a crypto-infrastructure proxy. As of 2026-06-23 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads 21 (Extreme Fear; bottoming/accumulation) with Bitcoin ~$64,568 and ETH ~$1,737; CRCLON sits roughly 49% below its 2025-10-10 all-time high.

---

## Architecture: How the Wrapper Works

CRCLON is a **1:1 tokenized claim on the underlying CRCL share** held by Ondo Global Markets. The token is not a synthetic or derivative: each token corresponds to economic exposure to a real Circle Internet Group share custodied within the Ondo Global Markets structure, with dividends reflected back to holders (typically as additional economic value rather than separate cash payouts).

- **Issuer / wrapper:** [[ondo-finance|Ondo Finance]] via Ondo Global Markets structures and issues the token as a digital claim on a real CRCL share.
- **Underlying asset:** Circle Internet Group common stock (CRCL), a US-listed equity.
- **1:1 backing & custody:** Underlying shares are held within Ondo's regulated brokerage/custody arrangements for Ondo Global Markets; the on-chain token mirrors that custodied position, with proof-of-reserves / attestation as the integrity anchor.
- **Mint / redeem & KYC gating:** Eligible users can mint and redeem tokens against the underlying, with primary market access running 24 hours a day, five days a week (aligned to US equity trading availability through Ondo's infrastructure). Access is **restricted to non-US persons** (retail and institutional) who pass Ondo's KYC/AML onboarding; US persons are excluded, and additional jurisdictional restrictions apply.
- **Oracle / price feed:** The token's reference value derives from CRCL's market price; on-chain price tracks that feed, anchored by mint/redeem arbitrage during US hours.
- **24/7 token vs. market-hours underlying:** CRCLON transfers 24/7 on-chain; CRCL trades only during US market hours, so tight tracking is strongest when the underlying market is open and arbitrage is active.
- **Distributions:** Any CRCL dividends are reflected in the token's reference value rather than paid out separately.
- **Regulatory wrapper:** Offered through Ondo Global Markets under a non-US distribution framework; a tokenized representation of a regulated US security, not a US-registered offering to US investors.

See [[ondo-finance]] for the broader issuer context, and [[real-world-assets]] for the asset class.

---

## Tracking & Peg

- **Tracking:** The on-chain price is designed to track CRCL's underlying equity price. Deviations can occur off-hours, during low liquidity, or when arbitrage between the token and primary mint/redeem is constrained.
- **Weekend-gap risk:** CRCL does not trade on weekends or US holidays, so CRCLON's on-chain price is stale relative to news during those windows.
- **Single-name volatility:** As a single, relatively newly public equity, CRCL is volatile — CRCLON sits ~49% below its 2025-10-10 all-time high, and the ATH/ATL range ($47.99–$158.37) illustrates the swings. Because Circle's revenue is tied to USDC reserves and interest income, the equity is sensitive to both stablecoin-market growth and the interest-rate environment.
- **No duration / rate risk in the wrapper:** As an equity, CRCLON has none of the interest-rate duration risk carried by the bond ETF tokens — though Circle's earnings themselves are rate-sensitive.

---

## Comparison vs. Alternatives

| Dimension | **CRCLON (Ondo)** | Holding real CRCL | MUON (Ondo) | IVVON (Ondo) |
|---|---|---|---|---|
| Underlying | Circle (stablecoin issuer) | Circle (stablecoin issuer) | Micron (memory chips) | S&P 500 index |
| Concentration | Single stock | Single stock | Single stock | 500 stocks (diversified) |
| Beta profile | High (newly public fintech) | High (newly public fintech) | High (cyclical semis) | Market beta |
| Crypto linkage | High (USDC issuer) | High (USDC issuer) | Low | Low |
| Access | Non-US KYC, on-chain 24/7 | Global brokerage | Non-US KYC | Non-US KYC |
| Backing | Real CRCL shares, off-chain | Direct share ownership | Real MU shares | Real IVV shares |
| Role in book | Stablecoin-issuer equity bet | Stablecoin-issuer equity bet | Semis high-beta bet | Diversified equity core |

CRCLON is distinctive in the Ondo set as a **crypto-native equity expression**: it gives on-chain holders exposure to the listed equity of the [[usdc|USDC]] issuer — effectively a way to hold the "picks-and-shovels" stablecoin-infrastructure business as a token. Compare with [[circle-xstock]] (an xStock-style tokenized CRCL from a different issuer) — the practical differences are issuer, custody model, chains, and eligibility rules rather than the underlying stock.

---

## How & Where It Trades

- **Primary market:** Mint/redeem via Ondo Global Markets for eligible users, gated to US equity hours.
- **Secondary market:** On-chain secondary liquidity across Ethereum, BNB Chain, and Solana. CoinGecko data shows a Uniswap V3 (Ethereum) pool; secondary liquidity is thin (24h volume in the low hundreds of thousands of dollars).
- **Liquidity:** Modest relative to the underlying equity — large orders rely on the primary mint/redeem channel rather than DEX depth.
- **Hours:** Token trades on-chain 24/7, but tight tracking is strongest when the underlying market is open.

---

## Narrative & Catalysts

CRCLON's thesis is **on-chain access to stablecoin-issuer equity**: it lets non-US holders own the listed equity of Circle — the company behind USDC — as a composable on-chain token, turning the stablecoin-infrastructure business into a tradeable on-chain asset. Catalysts include the broader RWA tokenization wave led by Ondo, USDC supply growth and stablecoin adoption, regulatory clarity for stablecoins, and the interest-rate environment that drives Circle's reserve income.

### History / Timeline

- **2025-10-10** — All-time high of $158.37.
- **2026-02-06** — All-time low of $47.99.
- **2026-04-09** — CRCLON captured in the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21** — Market snapshot: $80.62, ~$114.47M market cap, rank #247, ~49% below ATH.

---

## Risks

- **Issuer / custodian counterparty risk:** Holders depend on Ondo Global Markets and its custody arrangements; token value is only as sound as the custody and redemption guarantee on the underlying CRCL shares.
- **Equity risk:** Exposure to a single, relatively newly public equity; CRCL itself is volatile, and its earnings are sensitive to stablecoin-market growth and interest rates.
- **Concentration risk:** Single-name exposure with no diversification, unlike the ETF tokens in the set.
- **Tracking / liquidity risk:** Thin on-chain liquidity can cause the token to deviate from CRCL, especially outside US market hours. Equity volatility flows directly through.
- **Redemption-gating risk:** Mint/redeem is KYC-gated, non-US-only, and market-hours-bound; halted creations can break the peg arbitrage.
- **Regulatory risk:** Tokenized equities face an evolving and uneven global regulatory landscape; access restrictions (non-US only) can change, and enforcement posture toward tokenized securities remains a live issue.
- **Smart-contract / bridge risk:** Multi-chain deployment (Ethereum, BNB Chain, Solana) introduces contract and bridge attack surface.

---

## Trading Playbook

- **Stablecoin-issuer equity bet:** Use CRCLON to express a constructive view on USDC growth and stablecoin adoption via Circle's listed equity — a crypto-native equity exposure inside an on-chain portfolio.
- **Satellite, not core:** Size it small relative to a diversified core like [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]] given single-name volatility (note the ~49% drawdown from ATH).
- **Pair vs. MUON:** Combine with [[micron-technology-ondo-tokenized-stock|MUON]] for a small basket of high-beta single-name tokens, or with bond tokens ([[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]], [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]]) for ballast.
- **Execute in US hours:** Transact size while mint/redeem arbitrage is live; avoid large weekend trades into a stale price.

---

## Macro Backdrop (2026-06-23)

The Crypto Fear & Greed Index reads **21 (Extreme Fear)** with market-health 29/100 (bearish, bottoming/accumulation), Bitcoin ~$64,568 and ETH ~$1,737. Tokenized single-stock products like CRCLON inherit both equity beta and crypto-market liquidity conditions, so secondary on-chain depth tends to thin out in such regimes; and because Circle is a crypto-infrastructure company, CRCL itself carries some sensitivity to the broader crypto backdrop.

---

## See Also

- [[real-world-assets]]
- [[ondo-finance]]
- [[circle]]
- [[usdc]]
- [[circle-xstock]] — xStock-style tokenized CRCL (alternative issuer)
- [[micron-technology-ondo-tokenized-stock]] — sibling single-stock token
- [[ishares-core-s-p-500-etf-ondo-tokenized-etf]] — diversified equity core
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko market snapshot, 2026-06-21
- General market knowledge; no specific wiki source ingested yet.
