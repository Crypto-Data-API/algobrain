---
title: "Tokenised GBP"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, forex, real-world-assets, stablecoins, tokenization]
aliases: ["TGBP", "tGBP"]
entity_type: protocol
headquarters: "United Kingdom"
website: "https://www.tokenisedgbp.com"
related: ["[[british-pound]]", "[[crypto-markets]]", "[[depeg]]", "[[ethereum]]", "[[forex]]", "[[real-world-assets]]", "[[stablecoin]]", "[[tokenization]]", "[[treasuries]]"]
---

# Tokenised GBP

**Tokenised GBP** (TGBP) is a **British Pound Sterling–pegged [[stablecoin]]** issued by a UK FCA-registered firm. It maintains a 1:1 peg to GBP (1 TGBP ≈ £1.00) and is fully collateralised by fiat and short-term zero-coupon bonds issued by HM Treasury. TGBP is built for on-chain sterling payments, programmable transactions, and exposure to GBP-linked [[real-world-assets]] such as tokenized bonds.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, TGBP trades at **$1.32** with a market capitalization of **$31,213,514**, ranking **#628** by market cap. **The ~$1.32 USD quote is the GBP/USD foreign-exchange rate, NOT a de-peg** — TGBP is pegged to the British pound, and one pound was worth roughly 1.32 U.S. dollars on this date. Measured against its actual peg (sterling), TGBP is on-peg. The token was essentially flat over 24 hours (**+0.03%**) and down **-1.31%** over the trailing week; that weekly move reflects [[forex|GBP/USD currency movement]], not a loss of backing. The wider crypto market was in Extreme Fear (Fear & Greed 22, Bitcoin ~$64,180).

---

## Reading the Price Correctly

Because CoinGecko and most aggregators quote in USD, a GBP stablecoin will **always** display near the prevailing GBP/USD rate (historically ~$1.20–$1.40). A reading of $1.32 means **1 TGBP = £1.00 = ~$1.32**, which is the peg working as intended. A genuine [[depeg]] would show up as TGBP diverging from the GBP/USD rate — for example, trading materially below £1.00-equivalent. Do not interpret the USD figure as a 32% premium.

---

## What TGBP Is

- **Issuer:** A UK FCA-registered firm (the project markets itself as "the first and only British Pound–pegged stablecoin issued by a UK FCA-registered firm").
- **Peg:** 1:1 to GBP. The token is a sterling cash-equivalent on-chain.
- **Backing / collateral:** Fully collateralised by fiat cash and **short-term zero-coupon bonds issued by HM Treasury** (UK government debt) — i.e. high-quality, short-duration sterling reserves, analogous to how USD stablecoins hold [[treasuries|T-bills]].
- **Use cases:** On-chain GBP payments, programmable money, settlement, and access to GBP-denominated tokenized RWAs.

### Mint, Redeem, and Peg Mechanism

TGBP follows the standard fiat-backed [[stablecoin]] model: authorized users mint by depositing GBP and redeem 1:1 for GBP, with reserves held in cash and UK Treasury instruments. This reserve-backed redeemability is the primary peg-maintenance mechanism, supplemented by arbitrage against the GBP reference rate. Mint/redeem is typically KYC-gated and jurisdiction-restricted.

### Reserve & peg architecture (deep dive)

A fiat-backed sterling stablecoin holds its peg through a tight loop between **on-chain supply** and **off-chain reserves**:

1. **1:1 issuance against reserves.** Each TGBP in circulation is intended to be matched by £1.00 of high-quality, liquid reserves — **fiat cash plus short-term zero-coupon HM Treasury bonds** (UK government debt). Short-duration, sovereign-issued instruments minimize both credit risk and interest-rate/duration risk, which is the same reasoning USD issuers use when holding short-dated [[treasuries|T-bills]].
2. **Authorized mint/redeem ("primary market").** Whitelisted, KYC'd participants can mint TGBP by wiring GBP to the issuer and redeem TGBP for GBP at par. This **redeemability at £1.00** is the hard backstop for the peg.
3. **Arbitrage ("secondary market").** If TGBP trades below £1.00-equivalent on the open market, arbitrageurs buy the discount and redeem at par for a profit, lifting price back toward peg; if it trades above, they mint and sell. This arbitrage only works while the primary mint/redeem window is open, fully funded, and honored — which is why **frozen redemptions or reserve shortfalls are the canonical depeg trigger**.
4. **Reserve income.** The short-dated UK Treasuries in reserve earn yield (the GBP risk-free rate), which is the issuer's primary revenue model — analogous to how USD stablecoin issuers monetize T-bill interest. This aligns issuer incentives with growing float but also makes reserve transparency/attestation central to trust.

The economically meaningful question for a sterling holder is always **"is TGBP holding £1.00?"** — not what it prints in USD. A true [[depeg]] is TGBP diverging from the GBP reference rate, distinct from ordinary [[forex|GBP/USD]] movement.

---

## Settlement and Chains

TGBP is multi-chain, issued on **[[ethereum|Ethereum]]** with deployments across several EVM chains and Solana.

| Chain | Address |
|---|---|
| Ethereum | `0x27f6c8289550fce67f6b50bed1f519966afe5287` |
| Base | `0x27f6c8289550fce67f6b50bed1f519966afe5287` |
| BNB Smart Chain | `0x27f6c8289550fce67f6b50bed1f519966afe5287` |
| Polygon PoS | `0x27f6c8289550fce67f6b50bed1f519966afe5287` |
| Avalanche | `0x27f6c8289550fce67f6b50bed1f519966afe5287` |
| Solana | `2zMqyX4AYCk6mgy5UZ2S7zUaLxwERhK5WjqDzkPPbSpW` |

### Exchange Listings

| Venue | Pair | Type |
|---|---|---|
| Kraken | TGBP/USD | Centralized |
| Orca (Solana) | TGBP / USDC | Decentralized (spot) |

### How & where it trades / is used

- **Spot venues:** A **Kraken TGBP/USD** centralized pair and an **Orca TGBP/USDC** pool on Solana — modest, concentrated secondary liquidity typical of a non-USD stablecoin.
- **Liquidity profile:** Secondary depth is thin; large flows in or out generally route through the **issuer's primary mint/redeem window** rather than the open market. This is normal for a small GBP stablecoin but means on-screen liquidity understates the true redemption path.
- **Primary use:** On-chain sterling payments, programmable money/settlement, and access to GBP-denominated tokenized [[real-world-assets]] — i.e., it is built to be *used as money/settlement*, not actively traded.

---

## Comparison vs. other sterling & fiat stablecoins

| Stablecoin | Peg | Issuer / type | Backing | Notes |
|---|---|---|---|---|
| **TGBP** | GBP | UK FCA-registered firm | Fiat cash + short-term zero-coupon HM Treasury bonds | Markets itself as the first/only GBP stablecoin from a UK FCA-registered firm |
| **GBPT (Tether)** | GBP | Tether | Reserve-backed (per issuer) | A GBP-pegged issuance from the largest stablecoin operator |
| **USDC** | USD | Circle (regulated) | Cash + short [[treasuries\|T-bills]] | The reference template TGBP mirrors, but USD-denominated and far larger |
| **EURC** | EUR | Circle | Cash + short euro instruments | Same model in euros; illustrates the multi-currency fiat-stablecoin trend |

The key axis of comparison for a *GBP* stablecoin is **regulatory standing + reserve quality**, since the peg mechanics are broadly standardized. TGBP's pitch is its **UK FCA-registered issuer** and **HM Treasury-backed reserves**; against a sterling peer like Tether's GBPT, the differentiator is jurisdictional/regulatory positioning rather than the underlying 1:1 model. Versus USD/EUR incumbents, TGBP simply serves a different currency need (on-chain sterling) at much smaller scale.

## Narrative & catalysts

TGBP belongs to the **regulated fiat stablecoin / tokenization-of-money** narrative — the broadening of on-chain cash beyond the USD into other major currencies, paired with [[real-world-assets|RWA]] tokenization (here, GBP-denominated assets like tokenized bonds). Positive catalysts are regulatory and adoption-driven: a clearer UK stablecoin regime, growth in on-chain sterling demand, integrations with payment/RWA platforms, and broader exchange/DeFi listings that deepen liquidity. The negative path is any erosion of confidence in the issuer or reserves (a true depeg), or a UK/global regulatory shift that constrains the model.

## History / timeline

- **2026-04-09** — CoinGecko top-1000 snapshot ingested for this page.
- **2026-06-21** — Market snapshot: **$1.32** (= ~£1.00; GBP/USD FX, **on-peg**), ~$31.2M cap, rank #628; +0.03% / 24h, -1.31% / 7d (a GBP/USD currency move, not a loss of backing).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TGBP |
| **Peg** | 1:1 British Pound Sterling (GBP) |
| **Issuer** | UK FCA-registered firm |
| **Backing** | Fiat cash + short-term zero-coupon HM Treasury bonds |
| **Market Cap Rank** | #628 |
| **Market Cap** | $31,213,514 |
| **Current Price** | $1.32 (= ~£1.00; GBP/USD FX, on-peg) |
| **24h Change** | +0.03% |
| **7d Change** | -1.31% (GBP/USD FX move) |
| **Native Chain** | Ethereum (multi-chain) |
| **Categories** | Stablecoins, GBP Stablecoin, Fiat-backed Stablecoin |
| **Website** | [https://www.tokenisedgbp.com](https://www.tokenisedgbp.com) |

---

## Risks

- **FX / quote confusion:** The USD quote tracks GBP/USD; users unfamiliar with the FX peg may misread normal currency moves as instability. The economic risk for a sterling holder is whether TGBP holds £1.00, not $1.32.
- **Issuer / reserve risk:** Peg integrity depends on the issuer actually holding fully-backed, liquid GBP reserves and honoring 1:1 redemption. Reserve quality (cash + short UK Treasuries) is high but counterparty risk remains.
- **Depeg risk:** Loss of confidence, reserve shortfall, or frozen redemptions could cause TGBP to trade below its sterling peg — a true [[depeg]] (distinct from FX movement).
- **Liquidity risk:** Secondary liquidity is modest and concentrated (Kraken, Orca); large redemptions may rely on the issuer's primary window.
- **Regulatory risk:** UK and global stablecoin regulation is evolving; FCA registration helps but does not eliminate regulatory change risk.
- **Smart-contract / bridge risk:** Multi-chain deployment introduces bridge and contract risk across the supported networks.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

Context: as of 2026-06-23 the wider crypto market reads **Extreme Fear (F&G 21)** with a long-horizon **bottoming/accumulation** regime ([[bitcoin|BTC]] ~$64,568). A GBP stablecoin behaves very differently from the volatile microcaps elsewhere in this set:

- **Not a directional crypto bet.** TGBP is a sterling cash-equivalent; it should not rally or crash with BTC. Holding it is effectively a **GBP cash position on-chain**, so its USD "P&L" is just [[forex|GBP/USD]] currency exposure, not crypto beta. In Extreme-Fear risk-off, that makes it a *defensive/parking* instrument rather than a trade.
- **Watch the peg, not the USD quote.** The only TGBP-specific risk that matters is **depeg vs. £1.00** — driven by reserve quality, redemption availability, or issuer trust — distinct from ordinary GBP/USD moves. Monitor whether mint/redeem stays open and reserves stay attested.
- **Liquidity-aware use.** Thin secondary depth (Kraken, Orca) means large positions rely on the issuer's primary redemption window; do not assume deep open-market exit.
- **FX view, if any.** Any deliberate position is really a view on **sterling vs. the dollar**, plus the operational/regulatory soundness of the issuer — frame it as an FX + counterparty decision, not a crypto momentum play.

> *This is informational, not financial advice.*

---

## See Also

- [[stablecoin]]
- [[forex]]
- [[british-pound]]
- [[depeg]]
- [[real-world-assets]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on GBP-pegged stablecoins; no additional specific wiki source ingested yet.

