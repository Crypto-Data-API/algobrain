---
title: "OnRe Tokenized Reinsurance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["ONYC", "ONyc", "Onchain Yield Coin"]
entity_type: protocol
headquarters: "Decentralized (OnRe protocol)"
website: "https://onre.finance"
related: ["[[crypto-markets]]", "[[ethena]]", "[[real-world-assets]]", "[[solana]]", "[[stablecoin]]"]
---

# OnRe Tokenized Reinsurance

**OnRe Tokenized Reinsurance** (ticker **ONYC**, branded "ONyc") is a yield-bearing, multi-collateral token on **[[solana|Solana]]** that channels capital into the real-world **reinsurance** market. It is a [[real-world-assets|real-world asset]] (RWA) / yield-bearing [[stablecoin]] product: holders earn yield sourced from reinsurance premiums (largely uncorrelated to crypto cycles) **plus** the yield on the underlying collateral. OnRe positions ONYC as on-chain, composable access to the ~$750B reinsurance industry — an asset class historically gated behind institutional allocators and insurance-linked-securities (ILS) funds. The token is designed to drift up in value as yield accrues (a "rebasing-in-price" model) rather than trade as a free-floating governance coin, which is why it sits just above its $1 reference.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Ticker** | ONYC |
| **Price** | $1.11 |
| **Market-cap rank** | #181 |
| **Market cap** | ~$192.8M |
| **Fully diluted valuation** | ~$192.8M |
| **24h volume** | ~$904K |
| **24h change** | -0.09% |
| **7d change** | +0.18% |
| **Circulating supply** | ~173.0M ONYC |
| **Total supply** | ~173.0M ONYC |
| **Max supply** | Uncapped (mints on deposit) |
| **All-time high** | $1.12 (2026-06-20), now -0.4% |
| **All-time low** | $1.005 (2025-07-24), now +10.9% |

**Supply / valuation note:** Circulating supply equals total supply, so **MC = FDV** (ratio ~1.00) — there is no hidden token overhang or future unlock dilution. Supply scales with deposits rather than a fixed emission schedule. The price hovering just above $1 is consistent with a yield-bearing, collateral-backed design (value drifts up as yield accrues rather than floating freely).

---

## Architecture / How It Works

ONYC is a **yield-bearing collateral token**, not a free-floating governance coin. The design stacks a crypto-native yield layer underneath a real-world insurance-yield layer, so that a single token captures two independent return streams.

### 1. Collateral layer (crypto-native yield)

ONyc is collateralized by stablecoins; the protocol has used **sUSDe** (staked [[ethena|Ethena]] USDe) as collateral. sUSDe itself is a yield-bearing dollar token whose return comes from [[ethena|Ethena]]'s delta-neutral basis trade (perp [[funding-rate|funding]] plus staked-collateral yield). By holding a productive collateral asset rather than an idle stablecoin, the base of the stack is already earning before any reinsurance return is added. This is the "crypto-native" half of the yield.

### 2. Reinsurance engine (real-world yield)

OnRe describes itself as **licensed to deploy digital assets as insurance collateral**. The pooled collateral is posted to back real-world **reinsurance** contracts and private placements — i.e., it sits behind insurers as risk capital. In exchange, the pool accrues a share of reinsurance **premiums** (and, where structured, returns from insurance-linked private placements). Reinsurance is the business of insuring insurers: the capital absorbs tail losses (catastrophes, large claims) in return for a premium stream. Because catastrophe and underwriting risk is driven by physical events — hurricanes, earthquakes, mortality — rather than financial markets, this return stream is **largely uncorrelated** to crypto and equity cycles. That uncorrelated profile is the core structural pitch.

### 3. Compound yield stack

The two layers combine into a single accrual:

1. **Base reinsurance yield** — the share of premiums earned for bearing insurance risk. The protocol has marketed a base rate **exceeding ~16%** — a *forward target, not a guarantee*.
2. **Collateral yield** — the native yield on the sUSDe (or other stablecoin) collateral underneath.

The token's NAV rises as both layers compound, which is why ONYC prints just above $1 and grinds upward rather than oscillating around a hard peg.

### 4. Mint / redeem (elastic supply)

Tokens are **minted on deposit** and **burned on redemption**, so circulating supply tracks protocol AUM rather than a fixed emission schedule. There is no inflation cliff and no vesting unlock — new ONYC only exists because new collateral was deposited. The mint/redeem path (not the secondary market) is the protocol's intended primary liquidity mechanism; redemption is gated by the collateral being unwound from live reinsurance commitments, which is the key liquidity caveat (see Risks).

See [[real-world-assets]], [[stablecoin]], and [[ethena]] for the broader category and the collateral dependency.

---

## Tokenomics & Supply

- Supply (~173.0M at the 2026-06-21 snapshot) is **fully circulating** — circulating = total, so **MC = FDV** (ratio ~1.00). There is no team/investor unlock cliff and no future-emission dilution overhang, which is structurally cleaner than most low-float RWA listings.
- Supply is **elastic**: it expands one-for-one as users deposit collateral and mint ONyc, and contracts on redemption/burn. The "Max supply: Uncapped (mints on deposit)" field reflects that the cap is AUM-driven, not a fixed schedule — growth in supply is a sign of *inflows*, not of inflationary dilution of existing holders.
- **Value accrual is via yield, not buybacks or fee burns.** The design intends the per-token NAV to appreciate toward and above its $1 reference as reinsurance premiums and collateral yield compound — a price-accretive ("up-only NAV") model rather than a rebasing-balance model.

### Value accrual / governance

- **Holder economics:** value flows to holders purely through NAV appreciation of the token as the two-layer yield stack compounds. There is no staking lock required to earn — holding ONYC is the yield position. This is closer to a tokenized fund share than to a governance token.
- **No prominent on-chain governance token role:** ONYC is a collateral/yield instrument, not a vote-weighting governance coin. Protocol parameters (collateral mix, reinsurance allocations, redemption windows) are controlled by OnRe/the issuer rather than by ONYC-weighted on-chain voting, per available issuer documentation. Treat governance decentralization claims as unverified.

---

## Comparison vs Other RWA / Yield-Bearing Dollar Tokens

ONYC competes for the same allocator dollars as other on-chain yield products, but it is the only one in this peer set whose yield source is **insurance underwriting** rather than T-bills or perp funding. That makes its return profile uncorrelated to the rate cycle and the crypto basis trade — at the cost of catastrophe/underwriting risk the others do not carry.

| Token | Yield source | Backing | Primary chain | Correlation profile |
|---|---|---|---|---|
| **ONYC** (OnRe) | Reinsurance premiums **+** collateral yield | sUSDe / stablecoin collateral posted as insurance capital | [[solana\|Solana]] | Largely **uncorrelated** (insurance/catastrophe risk); inherits sUSDe/[[ethena]] tail via collateral |
| **sUSDe** ([[ethena\|Ethena]]) | Perp [[funding-rate\|funding]] + staked collateral (delta-neutral basis) | Crypto + hedged shorts | [[ethereum\|Ethereum]] (multi-chain) | Tied to funding rates / crypto basis; positive in bull, can compress in bear |
| **USDY** (Ondo) | Short-term US Treasuries + bank deposits | T-bills / cash | Multi-chain (Ethereum, Solana, others) | Tied to the **rate cycle**; low crypto correlation but rate-sensitive |
| **BUIDL** (BlackRock) / **OUSG** (Ondo) | Tokenized US Treasury / money-market fund | T-bills (institutional fund wrapper) | [[ethereum\|Ethereum]] (permissioned) | Pure rate exposure; institutional/KYC-gated, very low crypto correlation |
| **Maple (syrupUSDC)** | Over-collateralized institutional lending | Crypto/institutional loan book | Ethereum / Solana | Credit-cycle exposure; correlated to crypto-credit stress |

Differentiation: ONYC's pitch is **diversification** — an income stream that does not move with rates (USDY/BUIDL/OUSG), with crypto funding ([[ethena|sUSDe]]), or with crypto credit (Maple). The trade-off is that it carries a risk type none of those do: a bad catastrophe-loss year.

## How & Where It Trades

- **Decentralized:** Primarily on Solana DEXs (e.g., **Orca**). On-chain liquidity is the main secondary venue.
- **Mint/redeem is the primary path:** As a deposit-minted instrument, the intended way in and out is the protocol's mint/redeem flow, not the DEX order book. Secondary DEX liquidity exists mainly for marginal entries/exits and price reference.
- **Liquidity profile:** Modest/thin. 24h volume (~$904K at the 2026-06-21 snapshot) is small relative to a ~$192.8M market cap — typical for a yield-bearing, hold-to-earn asset where most supply sits earning rather than trading. Expect shallow secondary depth; exiting size in a stressed market depends on the redemption window, not the DEX.
- **Derivatives:** No major perpetual-futures or options market evident — this is a spot/redeem instrument, not a leverage vehicle.

---

## Narrative & Category

ONYC sits at the intersection of three of the strongest 2025–26 crypto narratives: **[[real-world-assets|RWA]]**, **yield-bearing stablecoins**, and **insurance-linked returns**. The thesis: bring an institutional, market-uncorrelated asset class (reinsurance premiums) on-chain and make it composable as DeFi collateral. It competes for the same allocator attention as other RWA-yield products and yield-bearing dollar tokens, differentiated by its reinsurance source rather than T-bills or perp funding. The **"uncorrelated real-world yield"** pitch is the core marketing hook — and the most genuinely differentiated thing about it.

**Catalysts to watch:**
- AUM growth (visible via circulating-supply expansion, since supply tracks deposits).
- Realized vs. target yield — whether the marketed ~16%+ base actually prints across a full underwriting cycle.
- New collateral types or chains beyond sUSDe/Solana, reducing single-collateral dependency.
- Composability: integrations that let ONYC be used as collateral elsewhere in [[solana|Solana]] DeFi.
- Broader RWA-narrative rotation — in a risk-off tape, "real yield, uncorrelated" stories attract defensive allocators even when speculative tokens bleed.

## History / Timeline

Only dated events corroborated by the on-chain/market record are listed; the protocol's detailed launch history is not independently verified here.

- **2025-07-24** — All-time low of **$1.005** printed (per market data), consistent with the token launching near its $1 reference around mid-2025.
- **2026-06-20** — All-time high of **$1.12** printed — the cumulative effect of NAV grinding upward as yield compounded over roughly a year, rather than a speculative spike.
- **2026-06-21** — Snapshot: $1.11, ~$192.8M market cap, rank #181, MC = FDV (see Market Data).

> The tight ATL→ATH range (≈$1.005 → $1.12 over ~11 months, ~+11%) is itself the most telling fact: this asset behaves like a slow-accreting yield instrument, not a volatile token.

---

## Risks

- **Reinsurance / underwriting (catastrophe) risk.** The defining risk. A large catastrophe-loss year (major hurricanes, earthquakes, pandemic-scale claims) could impair the collateral backing the reinsurance contracts or wipe out a year of premium yield. The "uncorrelated" benefit cuts both ways: it protects against crypto drawdowns but exposes holders to physical-world tail events that have nothing to do with markets.
- **Collateral / Ethena dependency.** Reliance on **sUSDe** ties ONyc to [[ethena|Ethena]]'s peg and funding-rate model. A USDe de-peg, a sustained negative-funding regime, or an sUSDe yield collapse would flow straight through to ONYC's collateral layer. ONYC's risk is therefore *additive*: sUSDe risk **plus** reinsurance risk.
- **Smart-contract & custody risk.** On-chain contract bugs on [[solana|Solana]], plus off-chain dependencies — insurance collateral is held in regulated/custodial structures, so holders are exposed to the issuer's licensing, counterparty, and operational integrity, which are not trustlessly verifiable on-chain.
- **Liquidity / redemption-window risk.** Thin secondary DEX markets mean exits in size depend on the **mint/redeem** path. Because collateral is committed to live reinsurance contracts, redemptions may be gated, delayed, or queued during stress — exactly when holders most want out. Do not assume instant, at-NAV exit.
- **Yield-claim risk.** A "16%+ base" is a marketed **target, not a contractual rate**. Realized yield can vary materially with the underwriting cycle and collateral conditions; treat the headline number as aspirational.
- **Transparency / verification risk.** Reinsurance positions and AUM are largely off-chain and qualitatively disclosed; an allocator cannot fully verify backing on-chain. Treat issuer claims with appropriate skepticism.
- **Macro backdrop.** As of 2026-06-24 crypto Fear & Greed reads **22 (Extreme Fear)** and the long-horizon regime is an **Established Bear Market** (market-health 28/100). Demand for newer RWA-yield tokens is subdued and redemption pressure can rise in risk-off conditions even for a peg-anchored asset.

## Trading Playbook (bear / Extreme-Fear regime)

This is a **hold-to-earn, NAV-accreting instrument**, not a trade. The playbook is closer to allocating to a yield product than to taking a directional position.

- **Why it can appeal in this regime:** In an Established Bear Market with Extreme Fear (F&G 22), a genuinely uncorrelated, peg-anchored real-yield asset is a defensive candidate — it should grind up on yield rather than track BTC/ETH downside. The ~+11% ATL→ATH path over ~11 months reflects that low-volatility profile.
- **Position as a yield sleeve, not a momentum trade:** Upside is the compounding yield (marketed ~16%+ base, unverified), not price appreciation beyond NAV. There is no leverage/perp market — sizing is about how much uncorrelated income exposure you want, not about a stop-loss thesis.
- **Entry:** Near the $1 reference; paying a premium far above NAV makes little sense for a hold-to-earn asset. The DEX is fine for marginal size; mint via the protocol for larger allocations.
- **Exit discipline:** Plan the exit around the **redemption window**, not the order book. Assume secondary liquidity vanishes in stress; size so you can wait out a redemption queue.
- **Disqualifiers / kill signals:** sUSDe/[[ethena]] de-peg or funding stress; a major catastrophe-loss event in the underlying reinsurance book; ONYC trading *below* NAV (signals redemption stress or loss of confidence); evidence that realized yield is far below the marketed target. Any of these breaks the core thesis.
- **Bottom line:** Suitable as a small, diversifying real-yield allocation for a risk-off book — explicitly **not** a vehicle for directional crypto exposure, and not liquid enough for tactical trading.

---

## Related

- [[real-world-assets]]
- [[stablecoin]]
- [[ethena]]
- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Issuer documentation: OnRe (https://onre.finance).
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[solana]]

---
