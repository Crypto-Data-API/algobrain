---
title: "Lighter"
type: entity
created: 2026-09-03
updated: 2026-09-03
status: good
tags: [exchange, crypto, derivatives, defi, hyperliquid, perpetual-futures, layer-2]
entity_type: exchange
aliases: ["Lighter Exchange", "LIT"]
founded: 2022
website: "https://lighter.xyz"
related: ["[[hyperliquid]]", "[[edgex]]", "[[dydx-chain]]", "[[cryptodataapi-exchanges]]", "[[perpetual-futures]]", "[[layer-2]]", "[[funding-rate]]"]
---

# Lighter

**Lighter** (token: **LIT**) is a decentralized perpetual-futures exchange built as a custom **zero-knowledge rollup**, pairing a central limit order book with cryptographically verifiable on-chain settlement. Its pitch is CEX-grade matching performance with the auditability of a zk-proof: every order match, funding payment, and liquidation is proven correct before Ethereum accepts it. It competes directly with [[hyperliquid|Hyperliquid]], [[edgex|edgeX]], and [[dydx-chain|dYdX]] in the post-2025 "verifiable/CEX-grade perp DEX" wave — see those pages for how the wiki treats comparable zk/L2 perp-DEX peers.

## Key Facts

| Metric | Value |
|---|---|
| Founded | 2022 (company); private beta launched January 2025 |
| Founder / CEO | Vladimir (Vlad) Novakovski |
| Headquarters | Decentralized (company incorporated; no public physical HQ) |
| Architecture | Custom zero-knowledge rollup (Ethereum L2) |
| Products | Order-book perpetual futures, spot markets |
| Token | LIT — launched ~30 December 2025, 1B fixed total supply |
| KYC | Not required |
| Custody | Self-custody |

CryptoDataAPI's own venue directory (see below) profiles Lighter as `kind: DEX`, `founded: "2024"`, `based: "On-chain (zk-rollup)"` — the "2024" in that field does not match this page's 2022 company-founding date or January 2025 beta launch; treat CryptoDataAPI's `founded` field as a coarse "when we started seeing this venue as live" marker rather than an authoritative incorporation date, and prefer the dates in this Key Facts table for anything precise.

## Technology

Lighter runs a **zk-rollup order book**: trades match off-chain at low latency, and the resulting state transition — every fill, funding payment, and liquidation — is proven correct with a zero-knowledge proof before being accepted on Ethereum. The stated goal is to combine a centralized exchange's matching speed with an on-chain venue's verifiability and MEV resistance, without requiring traders to trust an off-chain operator's honesty. This places Lighter in the same architectural family as other zk/validity-proof-based perp DEXs, distinct from [[hyperliquid]]'s custom-L1 approach and [[dydx-chain|dYdX]]'s Cosmos-appchain CLOB.

## Points Program and Token Launch

Lighter ran a multi-season points program ahead of its token generation event: **Season 1** during the January 2025 private beta, and **Season 2** from roughly October to the end of December 2025. Points accrued from trading, providing liquidity, and referrals. The **LIT** token launched around **30 December 2025** with a fixed **1 billion total supply**, with roughly **25% distributed to Season 1 and Season 2 points holders** at the token generation event — leaving the majority of supply (team, investors, ecosystem, future incentives) still to unlock, a structural dilution overhang comparable to other recent perp-DEX token launches (see [[dydx-chain]]'s peer-comparison table, which records Lighter's post-TGE market cap at roughly $382M with an MC/FDV near 0.25).

## Fee Model

Lighter's headline differentiator is that **standard retail accounts pay zero trading fees** — 0% maker and 0% taker — on its order-book perpetual and spot markets. This is reportedly subsidized in part through a revenue-share arrangement tied to Circle (the USDC issuer) on USDC deposits, plus liquidation fees routed into a liquidity pool and a separate **Premium/HFT account tier** (reported at roughly 0.002–0.004% maker / 0.02–0.028% taker, discountable further by staking LIT) aimed at market makers and high-frequency firms. **This fee model is unverified as a permanent structure** — a zero-fee retail venue subsidized by a single partner's economics is a specific, named sustainability risk: if that arrangement changes, Lighter's fee schedule could change with it. Treat any specific basis-point figure here as a snapshot from third-party trackers, not confirmed against Lighter's own current fee page.

## What Could Not Be Verified

- **Exact current fee schedule for Premium/HFT accounts** — figures vary slightly across third-party sources (exchange-compare.com, lighterpedia.com, dextools.io); no single authoritative current number was confirmed
- **Current leverage caps** — CryptoDataAPI's own exchange directory (below) records `max_leverage: null` for Lighter, i.e. it does not currently carry a max-leverage figure for this venue; do not assume parity with Hyperliquid's 40x or AsterDEX's 1001x without checking Lighter's own docs
- **Precise Circle revenue-share terms** — reported annual revenue figures ($30-40M) for the zero-fee subsidy come from third-party analysis, not confirmed against Lighter's or Circle's own disclosures
- **Current TVL, open interest, and volume** — these move materially for a token that only launched in December 2025; no figure is asserted here beyond the dYdX page's dated snapshot

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/exchanges/lighter` — venue profile: `kind`, `focus[]`, `specs` (instruments, max_leverage, KYC, custody), no API key required (see [[cryptodataapi-exchanges]])
- `GET /api/v1/exchanges?referral_only=true` — filters the venue directory to partner-link venues only (Lighter currently holds no CryptoDataAPI referral link)

```bash
curl "https://cryptodataapi.com/api/v1/exchanges/lighter"
```

Auth: none required for the Exchanges category. Endpoint catalog: [[cryptodataapi-exchanges]]. See also [[cryptodataapi]].

CryptoDataAPI does not yet carry Lighter in its cross-exchange derivatives/funding/OI feeds the way it does [[hyperliquid]] — the exchange directory entry is presently an overview-only profile, not a live market-data feed for this venue.

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] researching or routing to Lighter can:

- **Venue discovery** — `GET /api/v1/exchanges/lighter` to pull current `specs` (custody, KYC, instruments) before recommending the venue, rather than relying on a static write-up
- **Cross-venue comparison** — `GET /api/v1/exchanges` (all venues) to compare Lighter's profile against [[hyperliquid]], [[asterdex]], and other listed DEXes on `kind` and `specs`
- **Regime/liquidity proxy** — since Lighter is not yet in CryptoDataAPI's Hyperliquid-parity market-data feeds, use [[hyperliquid]]'s BTC/ETH perp data (`GET /api/v1/hyperliquid/summary`) as the nearest liquid cross-venue reference when comparing funding or basis
- **LIT token tracking** — LIT is a recently-launched (Dec 2025) token; check CryptoDataAPI's coins/market-data endpoints (see [[cryptodataapi-coins]]) for current listing status before assuming coverage

## Related

- [[hyperliquid]] — the transparent-book perp-DEX category benchmark
- [[edgex]] — comparable CEX-grade orderbook perp DEX, same 2025-2026 competitive wave
- [[dydx-chain]] — comparable app-chain/CLOB perp DEX; its peer-comparison table carries Lighter's post-TGE market data
- [[asterdex]] — the hidden-order/yield-collateral perp DEX; also newly documented via [[cryptodataapi-exchanges]]
- [[cryptodataapi-exchanges]] — the venue-directory API this page's data section cites
- [[layer-2]] — the zk-rollup scaling category Lighter's architecture belongs to
- [[perpetual-futures]], [[funding-rate]] — the underlying instrument and mechanics

## Sources

- https://cryptodataapi.com/api/docs and live `GET /api/v1/exchanges/lighter` response (fetched 2026-09-03)
- [[dydx-chain]] — existing wiki peer-comparison data on Lighter (MC rank #120, ~$382M cap, MC/FDV ~0.25 as of its 2026-06-21 snapshot)
- [[edgex]] — existing wiki context on the "CEX-grade perp DEX" competitive set including Lighter
- Bitget Academy, "What Is Lighter (LIGHT): zk-Rollup Perpetuals With Secure Liquidations" and "What is Lighter (LIT)?"
- DEXTools, "What Is Lighter? The Zero-Fee ZK Perpetual DEX, Explained (2026)"
- AirdropAlert / airdrops.com / CryptoLenz — Lighter points-program and airdrop history, 2026
