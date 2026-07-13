---
title: "Tesla xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stocks, derivatives, sp500]
aliases: ["TSLAX", "TSLAx"]
entity_type: protocol
headquarters: "Switzerland (Backed Finance issuer)"
website: "https://xstocks.com/"
related: ["[[crypto-markets]]", "[[real-world-assets]]", "[[solana]]", "[[arbitrum]]", "[[ethereum]]", "[[bnb]]", "[[backed-finance]]", "[[tokenized-stocks]]", "[[tokenization]]"]
---

# Tesla xStock

**Tesla xStock** (ticker **TSLAX**, also written TSLAx) is a tokenized-equity product issued by [[backed-finance|Backed Finance]] under its **xStocks** brand. Each token is a blockchain wrapper engineered to track the price of a single **Tesla, Inc. (NASDAQ: TSLA)** common share, with the issuer holding the underlying equity (or an equivalent 1:1 claim) as collateral in custody. It is a [[real-world-assets|real-world asset]] (RWA) token deployed across multiple chains — [[solana]], [[ethereum]], BNB Chain, [[arbitrum]], Mantle and TON — rather than a standalone cryptocurrency. Its price therefore moves with the underlying TSLA share, not with crypto-native supply/demand.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Ticker** | TSLAX |
| **Price** | $401.08 (tracks the underlying TSLA share price via the issuer) |
| **Market-cap rank** | #413 |
| **Market cap** | ~$56.6M |
| **Fully diluted valuation** | ~$211.9M |
| **24h volume** | ~$5.72M |
| **24h change** | +0.42% |
| **7d change** | -1.22% |
| **Circulating supply** | ~141,220 TSLAX |
| **Total supply** | ~528,271 TSLAX |
| **Max supply** | Uncapped (mint/burn tracks issuance) |
| **All-time high** | $496.55 (2025-12-22), now -19.2% |
| **All-time low** | $292.26 (2025-07-07), now +37.3% |

**Note on price:** TSLAX is not a free-floating crypto asset. Its quoted price reflects the value of one TSLA share; deviations from the underlying are arbitraged away by authorized participants who can mint/redeem against the collateral. Treat its "price change" lines as a proxy for TSLA equity moves, not for crypto sentiment.

**Supply / valuation note:** Market cap (~$56.6M) is well below FDV (~$211.9M) because circulating supply (~141k) is roughly one-quarter of total supply (~528k). The gap reflects tokens minted/held by the issuer that are not yet circulating rather than a fixed vesting unlock — supply expands and contracts as shares are tokenized or redeemed. The MC/FDV ratio (~0.27) should not be read like a typical token unlock schedule.

---

## Architecture: How the Wrapper Works

TSLAX is a **tokenized-equity wrapper**, not a synthetic or derivative position. The mechanics that matter:

### Issuer, custody and collateral

- **Issuer & custody.** Backed Finance (Switzerland-based) holds the underlying TSLA shares — or a 1:1 legal claim to them — with a regulated third-party custodian, segregated from Backed's balance sheet. Each token is intended to be fully collateralized by real equity, and Backed publishes proof-of-reserves / collateral attestations for its xStocks line. Holders' claim is contractual/legal against the issuer's structure, not the SIPC-protected brokerage ownership a US investor would have.
- **Bankruptcy-remoteness.** Backed's framework is designed so holders retain a claim on the underlying collateral even if the issuer defaults — but this is a legal claim, not direct registered share ownership.

### Mint / redeem, KYC and jurisdiction gating

- **Mint / redemption.** Authorized participants (KYC'd institutions) mint new tokens by delivering the underlying shares into custody and redeem tokens for the underlying value. This primary-market arbitrage is what keeps the token pegged to TSLA.
- **KYC / permissioning.** Primary issuance and redemption are restricted to verified, non-US-eligible participants; xStocks markets itself as compliant with EU regulations and explicitly **not** available to US persons. Secondary trading of the token on-chain is permissionless once minted — any wallet can hold or trade without KYC.

### Oracle, trading hours, corporate actions, settlement

- **Trading hours vs 24/7.** The underlying TSLA share trades only during US market hours (plus pre/post-market), but the TSLAX token trades **24/7** on crypto venues. On weekends and overnight, the token can move on liquidity and expectations while the reference equity is closed, then re-converge at the next US open. DeFi protocols pricing TSLAX off an oracle can show staleness during closures.
- **Dividends / corporate actions.** Tesla pays no common dividend, so dividend pass-through is not a live consideration. Splits and other corporate actions are reflected by the issuer via token adjustment rather than direct shareholder entitlement.
- **Multi-chain settlement.** Issued on Solana, Ethereum, BNB Chain, Arbitrum, Mantle and TON, with the Solana deployment as the primary liquidity hub.

See [[real-world-assets]] and [[tokenization]] for the broader category.

---

## Tracking & Peg

TSLAX stays near the TSLA reference price through **primary-market arbitrage**: APs mint-and-sell when the token is at a premium, buy-and-redeem when at a discount. Peg integrity holds best while the US market is open and APs are active. Sources of premium/discount and depeg risk:

- **Weekend / after-hours gap risk.** With TSLA closed, the token can trade away from the stale last print on sentiment or thin depth, opening a basis that mean-reverts at the next US open.
- **Liquidity.** Thin on-chain markets mean slippage on size and wider spreads off-hours.
- **Redemption friction.** If the AP/redemption channel slows under stress, discounts can persist.
- **Oracle staleness.** DeFi venues consuming an oracle price may misprice TSLAX during closures.

---

## Comparison: Ways to Get Tesla Exposure

| Dimension | **TSLAX (Backed xStock)** | **Real TSLA share (broker)** | **TSLA CFD** | **TSLA perp / synthetic** |
|---|---|---|---|---|
| **Issuer / venue** | Backed Finance AG | Exchange + broker | CFD broker | Derivatives venue |
| **Backing** | 1:1 TSLA share in custody | Direct ownership | None (synthetic) | None (margin) |
| **Secondary trading** | Permissionless on-chain | Brokerage account | Broker platform | Derivatives venue |
| **Hours** | 24/7 | US market hours | Broker hours | 24/7 |
| **Leverage** | Spot (none inherent) | Margin via broker | Built-in leverage | Built-in leverage |
| **Shareholder rights** | None | Full (voting) | None | None |
| **US persons** | Excluded | Allowed | Often restricted | Often restricted |
| **Key risk** | Issuer/custody, peg | Counterparty minimal | Broker counterparty, leverage | Funding, liquidation |

For most non-US crypto users the practical choice is TSLAX (spot, composable, no leverage) vs a CFD/perp (leverage, no real backing). Holding the real share avoids wrapper/issuer risk entirely but requires a brokerage account and US-hours trading.

---

## Tokenomics & Supply

There is no fixed tokenomics schedule in the crypto sense. Supply is **elastic** and driven entirely by issuance:

- Circulating supply (~141k) grows when participants tokenize more TSLA shares and shrinks on redemption.
- Total supply (~528k) includes issuer-held inventory not yet in circulation.
- No max supply, no emissions, no staking rewards, no governance token mechanics — the only "value accrual" is the underlying equity's price and any corporate actions the issuer passes through.

---

## How & Where It Trades

- **Centralized:** Listed on Kraken (TSLAX/USD) among the venues that support xStocks.
- **Decentralized:** Trades on Solana DEXs (e.g., Orca) and other chain-native pools; Solana is the deepest venue.
- **Liquidity profile:** Thin relative to the underlying equity. 24h volume (~$5.7M) is small versus TSLA's multi-billion-dollar equity turnover, so on-chain spreads and depth are the main practical constraint. Liquidity concentrates during US trading hours when arbitrageurs are active.

---

## Narrative, Category & Catalysts

TSLAX sits in the **tokenized stocks / RWA** narrative — bringing US equities on-chain for non-US users who want 24/7 access, DeFi composability (using tokenized equity as collateral), and fractional, borderless exposure. The xStocks line-up spans 50+ US stocks and ETFs. The thesis is "stocks as composable tokens"; the practical draw is access for users outside US brokerage rails. This was one of the most actively built corners of [[real-world-assets|RWA]] in 2025-2026.

**Catalysts:** broader on-chain-equities adoption, DeFi integrations accepting tokenized stocks as collateral, additional issuer competition on the same names, and regulatory clarity. Price catalysts are simply TSLA's own drivers — deliveries, margins, FSD/robotaxi headlines, and Elon Musk newsflow, all of which make TSLA a high-volatility, high-beta name.

**Macro context (2026-06):** crypto sentiment is risk-off — Fear & Greed at 21 (Extreme Fear), composite market-health 29/100 — though the long-horizon regime model has shifted toward **Bottoming / Accumulation**. TSLAX's price is driven mainly by TSLA, not crypto beta, but muted crypto risk appetite can thin RWA-wrapper liquidity at the margin.

### History / timeline

- TSLAX is published by Backed Finance under the xStocks brand as part of the tokenized-US-equities lineup. The earliest market snapshot for this page in the wiki is the [[coingecko-top-1000-2026-04-09|CoinGecko listing snapshot of 2026-04-09]]; recorded all-time high $496.55 (2025-12-22) and all-time low $292.26 (2025-07-07).

*(Only verified dated events are asserted; additional history should be added via the ingestion workflow.)*

---

## Risks

- **Issuer & custody risk.** Holders rely on Backed Finance and its custodian actually holding the shares and honoring redemptions. This is a centralized counterparty, unlike native crypto, and lacks US investor-protection coverage.
- **Redemption-gating risk.** Only whitelisted APs can mint/redeem; if that channel slows under stress, peg arbitrage weakens and discounts can persist.
- **Peg / tracking risk.** During off-hours or low liquidity, the token can deviate from the true TSLA price; convergence depends on arbitrageurs and open redemption windows.
- **Regulatory / securities-law risk.** Tokenized securities sit in an evolving legal grey zone. US persons are excluded, and regimes could change in the EU or elsewhere.
- **Liquidity risk.** Thin on-chain markets mean slippage on size and potential gaps versus the equity.
- **No shareholder rights.** Token holders get economic exposure, not voting rights or direct legal share ownership.
- **Macro backdrop.** As of 2026-06-21 the broad crypto Fear & Greed index reads in Extreme Fear; risk appetite for newer RWA wrappers is muted, though TSLAX's price is driven mainly by TSLA, not crypto beta.

---

## Trading Playbook (for a crypto trader)

- **Use case:** On-chain dollar exposure to a high-beta US growth/EV name without a US brokerage account; usable as DeFi collateral or as a volatility sleeve in an on-chain book.
- **Character of the underlying:** TSLA is one of the most volatile mega-caps — large gaps around deliveries, earnings, and Musk/robotaxi headlines. Expect equity-grade swings; TSLAX inherits them fully.
- **Mind the basis:** Be cautious with weekend/holiday quotes — TSLAX can carry a premium/discount to the stale TSLA print that reverts at the next US open. Don't take large positions into a long closure unless you intend to hold the basis.
- **Execution:** Prefer US market hours when AP arbitrage is active and spreads are tightest; check the premium/discount to the underlying and size to shallow on-chain depth.
- **Alternatives:** Want leverage? A TSLA CFD/perp may suit better. Want to eliminate wrapper risk and don't mind KYC/US-hours? Hold the real share.

---

## Related

- [[real-world-assets]]
- [[tokenization]]
- [[backed-finance]] — the xStock issuer
- [[tokenized-stocks]]
- [[crypto-markets]]
- [[solana]]
- [[arbitrum]]
- [[ethereum]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Issuer documentation: xStocks (https://xstocks.com/) and Backed Finance (https://docs.backed.fi/).
- General market knowledge; no specific wiki source ingested yet.
