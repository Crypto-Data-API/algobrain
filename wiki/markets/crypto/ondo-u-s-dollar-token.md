---
title: "Ondo U.S. Dollar Token"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, stablecoins, real-world-assets]
aliases: ["USDON"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[bnb-chain]]", "[[stablecoin]]", "[[stablecoins]]", "[[real-world-assets]]", "[[ondo-finance]]", "[[treasuries]]", "[[tokenized-treasuries]]", "[[usdu]]"]
---

# Ondo U.S. Dollar Token

**Ondo U.S. Dollar Token** (ticker **USDON**) is a US-dollar token issued by **[[ondo-finance|Ondo Finance]]**, deployed on [[ethereum|Ethereum]] and [[bnb-chain|BNB Chain]], targeting a 1:1 peg to the US dollar. The real-world asset it represents is a reserve of cash and short-term US [[treasuries|Treasuries]] / Treasury-equivalent instruments. It is Ondo's [[real-world-assets|RWA]]-backed dollar in the same lineage as Ondo's flagship USDY yield product — a tokenized claim designed as a compliant, institution-grade settlement dollar that can carry the underlying short-term-rate yield to eligible holders.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As a Treasury-backed dollar, **price ≈ peg/NAV by design** — the redemption/backing disclaimer matters far more than rank or market cap.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | USDON |
| **Market Cap Rank** | #345 |
| **Current Price** | $1.000 |
| **Market Cap** | $71.8M |
| **24h Volume** | $337.5K |
| **24h Change** | 0.00% |
| **Circulating / Total Supply** | 71.82M / 71.82M USDON |
| **All-Time High** | $1.000 |
| **All-Time Low** | $1.000 |
| **Categories** | Stablecoins, USD Stablecoin, RWA, Ethereum / BNB Chain Ecosystems |
| **Website** | [https://app.ondo.finance/](https://app.ondo.finance/) |

At the snapshot USDON traded at **exactly $1.000**, with a recorded ATH and ATL both at $1.000 — i.e. **no de-peg has ever been observed** in CoinGecko's data. This tight pin to par is consistent with a tightly redemption-managed, Treasury-backed RWA dollar from a well-capitalized issuer, though the flat history also reflects relatively limited price discovery (low secondary volume).

---

## Architecture — How It Works

### Reserve / collateral model
USDON is backed by **cash and short-term US Treasury / Treasury-equivalent instruments** held via Ondo's regulated structure. Ondo's RWA dollars are collateralized by short-duration government-money-market-style assets — high-credit-quality, liquid dollar instruments — rather than crypto collateral or an algorithmic mechanism.

### NAV / peg mechanism
The reserve NAV anchors USDON to $1.00. The peg is enforced primarily by the **issuer-level mint/redeem channel** (par creation and redemption against reserves), with secondary on-chain liquidity allowing free transfer. Because issuance/redemption is permissioned, arbitrage that pins the secondary price to $1 must flow through KYC'd counterparties.

### Yield source & distribution
The yield is the underlying **short-term Treasury yield**; like Ondo's USDY, yield can accrue to **eligible (often non-US / KYC-qualified) holders**. APY is kept qualitative here. The gating of yield to qualified holders is a deliberate regulatory design — passing yield to US retail would more clearly invoke securities treatment.

### Mint / redeem & KYC gating
Issuance and redemption are **permissioned** to verified counterparties at par against reserves; this issuer-level mint/redeem is the primary peg-enforcement mechanism. The token then **transfers freely** on-chain, with secondary liquidity for ordinary holders who do not mint/redeem directly.

### Regulatory wrapper & issuer
Issued by **[[ondo-finance|Ondo Finance]]**, one of the larger RWA issuers, via a compliant structure that gates yield/redemption to qualified participants. Treatment of yield-bearing tokenized dollars (security vs. e-money vs. stablecoin) varies by jurisdiction and remains a live regulatory question.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 71.82M USDON |
| **Total Supply** | 71.82M USDON |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | ~1.00 |

Supply tracks reserve inflows/outflows from mint and redeem; there is no emission schedule or speculative tokenomics. Market cap represents dollars tokenized rather than a valuation.

---

## Comparison vs Peers

| Product | Issuer | Yield to holder | Domicile / gating | Backing |
|---|---|---|---|---|
| **USDON** (Ondo) | Ondo Finance | Yes, to eligible holders | Permissioned / KYC-gated | Cash + short Treasuries |
| **USDY** (Ondo) | Ondo Finance | Yes (accruing NAV, price > $1) | Offshore / non-US | Cash + short Treasuries |
| **USDM** (Mountain Protocol) | Mountain Protocol | Yes (rebasing $1) | Bermuda (BMA) | Short-term Treasuries |
| **USDO** ([[openeden-open-dollar]]) | OpenEden Digital | Yes (rebasing $1) | Bermuda (BMA) | T-bills + reverse repo |
| **USDC** (Circle) | Circle | No | US (regulated) | Cash + short Treasuries |

USDON's nearest sibling is **USDY** — both are Ondo, Treasury-backed, and yield-bearing to eligible holders — but USDON is structured as a flat-$1 settlement dollar (price pinned at par) rather than USDY's accruing-NAV note. Against rebasing dollars (USDM, USDO) it keeps a $1 price without elastic balances; against USDC it adds passthrough yield for qualified holders.

---

## How / Where It Trades

- **Primary venue:** on-chain on [[ethereum|Ethereum]] (`0xace8e719899f6e91831b18ae746c9a965c2119f1`) and [[bnb-chain|BNB Chain]] (`0x1f8955e640cbd9abc3c3bb408c9e2e1f5f20dfe6`); transfers freely, with issuance/redemption through Ondo for verified counterparties.
- **Liquidity caveat:** ~$337K/24h volume against a ~$72M cap is thin on the secondary market — the peg is held mainly by issuer redemption rather than deep DEX/CEX order books. Large secondary trades could move the price off $1 until arbitrageurs (who must be KYC'd to mint/redeem) step in.
- **Composability:** as a flat-$1, multi-chain ERC-20/BEP-20, USDON can serve as a settlement/collateral dollar across Ethereum and BNB Chain DeFi for eligible users.

---

## Narrative / Category & Catalysts

USDON is a play on **tokenized-Treasury / yield-bearing dollars** and Ondo's broader RWA franchise. Drivers:
- **Rates:** the passthrough yield is a function of short-term US rates; higher-for-longer rates make it attractive, cuts erode the draw.
- **Institutional adoption:** growth follows demand for compliant, yield-bearing on-chain dollars among institutions and offshore holders.
- **Ondo ecosystem:** USDON benefits from Ondo's distribution, integrations, and brand among RWA products (USDY, OUSG).
- **Regulatory clarity:** a defined stablecoin/securities framework would shape how widely a yield-bearing dollar can be offered.
- **Regime context:** as of 2026-06-22 the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **21 (Extreme Fear)** in an established bear market; Treasury-backed dollars are defensive, but secondary liquidity tends to thin in such regimes.

---

## History / Timeline

| Date | Event |
|---|---|
| 2026-04-09 | Captured in CoinGecko top-1000 snapshot ([[coingecko-top-1000-2026-04-09]]) as an Ondo RWA dollar |
| 2026-06-21 | Market snapshot: $1.000 (ATH = ATL = $1.000, no recorded de-peg), market cap ~$71.8M (rank #345) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.000 |
| **All-Time Low** | $1.000 |
| **Current Price** | $1.000 (no recorded de-peg) |
| **24h Change** | 0.00% |

---

## Risks

- **Depeg risk:** none observed to date (ATH = ATL = $1.00), but a permissioned, thinly-traded RWA dollar can still deviate on the secondary market under stress before issuer arbitrage restores par.
- **NAV-gap risk:** the token is worth its reserve NAV; any discrepancy between attested and actual reserves threatens par directly.
- **Redemption-gating risk:** mint/redeem at par is permissioned to KYC'd counterparties; ordinary holders depend on secondary liquidity to exit, which is thin.
- **Collateral / custodial counterparty risk:** value depends on Ondo's reserve assets (cash + short Treasuries) and their custodians; a custody freeze or reserve shortfall would impair backing.
- **Issuer risk:** concentration in a single issuer, [[ondo-finance|Ondo Finance]] — its solvency, operations, and willingness to redeem at par are the backstop.
- **Regulatory risk:** RWA / tokenized-Treasury dollars with embedded yield face active securities- and stablecoin-regime scrutiny; yield is typically gated to non-US / qualified holders for this reason.
- **Liquidity risk:** thin secondary liquidity (see above) makes orderly exits at par dependent on the redemption channel.
- **Macro backdrop:** the Extreme-Fear / bear regime tends to thin secondary liquidity even for defensive Treasury-backed dollars.

---

## Trading / Usage Playbook

- **Treat as a yield-bearing cash instrument, not a trade.** USDON is for parking dollars on-chain to earn the Treasury passthrough (if eligible), not for directional exposure.
- **Confirm eligibility first.** Yield and par redemption are gated to KYC'd / qualified holders — non-eligible holders are exposed to thin secondary liquidity.
- **Par exit via the issuer.** The reliable $1 exit is Ondo's redemption channel; secondary buyers should expect slippage on size given low volume.
- **Watch rates.** Expected return is essentially the short-term Treasury yield; rate cuts reduce the appeal versus non-yield dollars.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xace8e719899f6e91831b18ae746c9a965c2119f1` |
| Binance Smart Chain | `0x1f8955e640cbd9abc3c3bb408c9e2e1f5f20dfe6` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.ondo.finance/](https://app.ondo.finance/) |
| **Twitter** | [@ondofinance](https://twitter.com/ondofinance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $337.5K |
| **Market Cap Rank** | #345 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[ondo-finance]] — the issuer
- [[stablecoin]] / [[stablecoins]]
- [[real-world-assets]] / [[treasuries]] / [[tokenized-treasuries]]
- [[usdu]] — peer tokenized-Treasury yield dollar
- [[crypto-markets]]
- [[ethereum]] / [[bnb-chain]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.
