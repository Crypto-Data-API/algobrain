---
title: "Fidelity Digital Interest Token"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenized-treasuries, stocks]
aliases: ["FDIT", "Fidelity Digital Interest Token"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.fidelity.com/"
related: ["[[real-world-assets]]", "[[ousg]]", "[[hashnote-usyc]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# Fidelity Digital Interest Token

**Fidelity Digital Interest Token** (ticker **FDIT**) is a tokenized, yield-bearing [[real-world-assets|real-world asset]] linked to **Fidelity**, one of the largest U.S. asset managers. It is a **tokenized money-market / short-term Treasury-style instrument** issued on [[ethereum|Ethereum]], holding a stable **$1.00 net asset value per token** and accruing yield from the underlying high-quality, short-duration assets. With a flat $1.00 NAV across ATH and ATL, FDIT functions as a **par-NAV** token where return is delivered as yield rather than price appreciation. It belongs to the same on-chain "tokenized cash / tokenized Treasuries" category as [[ousg]] and [[hashnote-usyc]], and represents Fidelity's entry into on-chain regulated cash management.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | FDIT |
| **Issuer** | Fidelity (Fidelity Digital Assets / Fidelity Investments) |
| **Underlying** | Short-term, high-quality cash-equivalent assets (money-market / Treasury-style) |
| **Current price** | $1.00 |
| **Market cap** | $144.20M |
| **Market cap rank** | #213 |
| **24h volume** | $0 (no secondary on-chain volume at snapshot) |
| **24h change** | 0.00% |
| **Circulating supply** | ~144.20M FDIT |
| **Total supply** | ~144.20M FDIT |
| **All-time high** | $1.00 (2025-09-17) |
| **All-time low** | $1.00 (2025-09-17) |
| **Chain** | Ethereum |

> The flat $1.00 price across ATH and ATL is characteristic of a tokenized money-market product: NAV is held at par and return is delivered as yield (typically via rebasing or accrual), not price appreciation. **The price is an administratively-pinned $1.00 NAV, not a market-discovered price** — the relevant disclaimer is NAV/par integrity and redemption access, not crypto-cycle volatility.

---

## How It Works (Architecture Deep Dive)

FDIT represents a tokenized claim on a Fidelity-managed pool of **short-duration, high-quality assets** (the kind found in a government/Treasury money-market fund). The token holds a **constant $1.00 NAV** and passes through yield to holders.

- **Fund structure & manager:** Issued and managed within **Fidelity's** regulated asset-management framework (via Fidelity Digital Assets / Fidelity Investments). The token is a digital fund interest, not a fiat-reserve stablecoin.
- **Underlying assets:** Short-term U.S.-dollar cash equivalents — **Treasury bills, repo, and similar instruments** managed by Fidelity, mirroring a government/Treasury money-market mandate to minimize duration and credit risk.
- **Backing model:** Each token is backed by the underlying fund assets at par; this is a tokenized fund/interest product, not a fiat reserve stablecoin. Market cap ≈ supply at $1.00 NAV.
- **Custody:** Underlying assets are custodied within Fidelity's regulated asset-management structure.
- **Eligible-investor gating:** A **permissioned, institutional / qualified-investor product** offered under securities-law exemptions (e.g., Reg D / Reg S). Transfers are restricted to whitelisted, KYC/AML-screened holders. It is not a freely circulating retail token.
- **Mint / redeem flow & settlement:** Subscriptions and redemptions occur through Fidelity / the issuance platform against the underlying fund, restricted to eligible KYC'd investors; redemption is at the $1.00 par NAV.
- **Yield source & distribution:** Yield reflects prevailing short-term U.S. rates (T-bill / repo income) and is delivered through the token mechanism (rebasing or accrual) rather than price appreciation; exact APY is not asserted here (do not infer a fixed rate).
- **Oracle / NAV feed:** Price is administratively pinned to a $1.00 NAV; there is no continuous on-chain price discovery because there is no meaningful secondary market.
- **Transfer restrictions / whitelist:** Transfers are limited to the permissioned holder set at the contract / transfer-agent level.

See [[tokenized-treasuries]] and [[real-world-assets]] for the broader category; peers include [[ousg]], [[hashnote-usyc]], and BlackRock's [[buidl]].

---

## Comparison vs Peer Tokenized Treasury / MMF Products

| Product | Issuer / Manager | NAV model | Yield delivery | Notable trait |
|---|---|---|---|---|
| **FDIT** | Fidelity | $1.00 par NAV | Yield via token mechanism | Major U.S. asset manager; institutional cash |
| **[[buidl]]** (BUIDL) | BlackRock + Securitize | $1.00 NAV (rebasing) | New tokens (rebase) | Largest tokenized-Treasury fund |
| **[[ousg]]** (OUSG) | Ondo Finance | Price-accruing | NAV price-accretion | Instant USDC mint/redeem |
| **[[hashnote-usyc]]** (USYC) | Hashnote / Circle | Price-accruing | NAV price-accretion | Repo-focused; Circle collateral |
| **[[vaneck-treasury-fund\|VBILL]]** | VanEck + Securitize | $1.00 NAV (rebasing) | New tokens (rebase) | Multi-chain; stablecoin subscriptions |

FDIT's distinguishing trait is the **Fidelity brand** — a top-tier U.S. asset manager entering on-chain money-market issuance, competing most directly with BlackRock's BUIDL for institutional on-chain cash mandates.

---

## How & Where It Trades / Is Used

- **Primary issuance:** Subscriptions and redemptions occur through Fidelity / the issuance platform against the underlying fund, restricted to eligible KYC'd investors.
- **Eligibility:** KYC/AML-cleared institutional / qualified investors whitelisted by the issuer (Reg D / Reg S); not open retail.
- **Secondary trading:** Effectively none on public DEX/CEX venues — CoinGecko reported $0 24h volume. Transfers are limited to the permissioned holder set, so there is no open-market price discovery.
- **DeFi composability:** As a permissioned par-NAV token, FDIT is a candidate for **collateral / cash-management use within institutional or permissioned DeFi**, subject to each venue's whitelist; broad retail DeFi use is constrained by permissioning.
- **Tracking:** Price is administratively pinned to a $1.00 NAV; there is no underlying-equity tracking dynamic (unlike Ondo tokenized stocks). Stability comes from the underlying short-duration assets and daily NAV management.
- **Hours:** On-chain transfer is 24/7 among permitted holders; subscription/redemption follows the fund's operating schedule.

---

## Narrative, Category & Catalysts

FDIT sits in the **tokenized money-market / tokenized cash** segment of the RWA narrative, notable for Fidelity's brand weight. Catalysts:

- **Institutional brand adoption:** Fidelity, like BlackRock with BUIDL, entering on-chain money-market issuance is a strong validation signal for tokenized cash management.
- **Rates regime:** Demand scales with short-term U.S. rates — higher front-end yields make par-NAV tokenized cash more attractive than idle stablecoins.
- **RWA tokenization wave:** Part of the broader move bringing regulated fixed-income on-chain alongside [[buidl]], [[ousg]], [[hashnote-usyc]], and [[vaneck-treasury-fund|VBILL]].
- **On-chain treasury management:** Crypto-native funds, DAOs, and institutions seeking principal-stable, yield-bearing dollar exposure with blockchain settlement.

### History / Timeline

- **2025-09-17:** ATH = ATL = $1.00 recorded (per snapshot data), consistent with a par-NAV launch around this period. (Exact launch date not independently verified here — do not infer one.)
- **2026-06-21:** Market snapshot — ~$144.20M market cap, $1.00 NAV, rank #213.

---

## Risks

- **Issuer / custodial risk:** Holders rely on Fidelity's management and custody of the underlying assets and on its redemption commitment.
- **Redemption-gating / liquidity risk:** With no meaningful secondary market, exit depends on the issuer's redemption process; this is a hold-to-redeem instrument, not a liquid trading token.
- **Interest-rate risk:** Yield falls if short-term U.S. rates decline; the product's appeal is rate-dependent.
- **NAV-gap / "breaking the buck" risk:** The $1.00 par can in principle break if the underlying portfolio takes losses — the same risk faced by traditional money-market funds, though mitigated by the high-quality short-duration mandate.
- **Regulatory / securities-law risk:** Tokenized funds operate under evolving securities rules; permissioning and eligibility terms can change.
- **Smart-contract risk:** As an on-chain token, it carries contract/operational risk despite institutional backing.
- **Note:** This is a tokenized fund holding a par NAV, not an algorithmic or fiat stablecoin; "de-peg" framing applies less than redemption/credit/operational risk.

---

## Macro Backdrop (2026-06-23)

With the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **21 ("Extreme Fear")** and the long-horizon regime model in bottoming/accumulation, capital often rotates toward yield-bearing, principal-stable instruments. Tokenized money-market products such as FDIT, [[ousg]], and [[hashnote-usyc]] tend to attract demand in risk-off conditions because they offer Treasury-like yield with on-chain settlement. **The token's value tracks fund NAV/yield, not the crypto cycle.**

---

## Trading / Usage Playbook

- **Who can hold it:** KYC/AML-cleared institutional / qualified investors whitelisted by Fidelity (Reg D / Reg S). Not for open retail.
- **Primary use case:** On-chain **cash management** — a $1.00-NAV, Treasury-yielding token from a top-tier U.S. manager, suitable for institutional treasuries.
- **Collateral use:** Candidate for high-quality collateral in permissioned/institutional DeFi where whitelisted.
- **Exit discipline:** Redeem at $1.00 par NAV through the issuer; do not rely on secondary liquidity.

---

## See Also

- [[real-world-assets]]
- [[tokenized-treasuries]]
- [[ousg]]
- [[hashnote-usyc]]
- [[buidl]], [[vaneck-treasury-fund]] — peer tokenized cash / Treasury products
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko market snapshot, 2026-06-21
- General market knowledge; no specific wiki source ingested yet.
