---
title: "KelpDAO Stablecoin Sympathy Depegs — April 2026"
type: news
created: 2026-04-28
updated: 2026-06-12
status: good
tags: [crypto, stablecoins, depeg, defi, contagion, kelp, layerzero, ai-trading]
aliases: ["KelpDAO Sympathy Depeg", "April 2026 Stable Contagion", "GHO Sympathy Depeg", "crvUSD Apr 2026"]
event_date: 2026-04-18
markets_affected: [crypto]
impact: medium
verified: true
sources_count: 5
related: ["[[2026-04-18-kelp-layerzero-exploit]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[stablecoin-pair-arbitrage]]", "[[stablecoin-depeg-profit-capture]]", "[[cross-chain-contagion-hedge]]", "[[ai-amplified-exploit-arbitrage]]", "[[2026-exploit-target-watchlist]]", "[[ai-vulnerability-discovery]]", "[[ethena-usde]]", "[[stablecoin-depeg-history]]", "[[rpc-poisoning]]", "[[dvn-compromise-patterns]]"]
---

# KelpDAO Stablecoin Sympathy Depegs — April 2026

> **Companion page:** for the exploit mechanics, full timeline, and protocol-level aftermath of the KelpDAO/LayerZero hack itself, see [[2026-04-18-kelp-layerzero-exploit]]. This page focuses specifically on the **synthetic-stablecoin sympathy-depeg trade** that the exploit triggered.

On **April 18, 2026, 17:35 UTC**, the KelpDAO/LayerZero exploit drained $290M via a 1-of-1 DVN compromise. Within hours, **multiple synthetic stablecoins traded weak in sympathy** — GHO, crvUSD, sUSDe, USDe — without direct exposure to KelpDAO. **The sympathy depegs ranged from 30-80bp; reversion took 24-72 hours.** This is the **canonical AI-era contagion case** for the sympathy-depeg variant in [[synthetic-stablecoin-depeg-arbitrage]] and [[cross-chain-contagion-hedge]]. The trade was **buy the basket of sympathy-depegged synthetic stables; capture the cross-mechanism mean reversion as scope clarified.**

## Timeline

| Time (UTC) | Event |
|-----------|-------|
| Apr 18, 17:35 | KelpDAO LayerZero exploit confirmed: 116,500 rsETH (~$290M) released from Ethereum L1 escrow |
| Apr 18, 17:50-18:30 | Multi-source confirmation (PeckShield, BlockSec, Cyvers, ChainAegis, Forta) |
| **Apr 18, 18:00** | Aave Guardian freezes rsETH and wrsETH markets within ~25 minutes |
| Apr 18, 18:30 | Circle freezes attacker's USDC holdings |
| Apr 18, 19:00-23:00 | Cross-DeFi panic: $5B+ TVL outflow over first 6 hours |
| **Apr 18, 19:30** | GHO peg deviates: $1.001 → $0.992 over 90 minutes (Balancer GHO/USDC pool) |
| **Apr 18, 20:00** | crvUSD peg deviates: $1.000 → $0.996 (Curve crvUSD pool) |
| Apr 18, 21:00-22:00 | sUSDe trades $1.018 → $1.005 (compression of yield premium) |
| Apr 19, 00:00-12:00 | $15B TVL drain across DeFi within 48 hours of incident |
| Apr 19, 14:00 | Aave bad-debt projection: $123-230M depending on socialization |
| Apr 19, 18:00 | LayerZero post-mortem: RPC poisoning + DDoS |
| Apr 20, 00:00 | LayerZero announces no-1-of-1-DVN policy going forward |
| **Apr 20, 12:00-18:00** | Synthetic stable sympathy depegs begin reverting as scope clarifies |
| Apr 21, 00:00 | GHO returns to $0.999; crvUSD to $1.000; sUSDe back to ~$1.015 |
| Apr 22-25 | Continued cleanup; AAVE token traded weak through bad-debt resolution discussion |

## The Sympathy Mechanism

None of these synthetic stables had **direct exposure** to KelpDAO/rsETH. Yet all four traded weak. Why?

### GHO (Aave overcollateralized)

**Mechanism**: GHO is minted against Aave deposits. KelpDAO contagion → Aave bad-debt overhang → market questions Aave's broader stability → GHO traders sell defensively despite GHO collateral being unaffected.

**Specific channels**:
- Aave Safety Module potentially bears bad-debt loss → MKR/AAVE governance impact
- PSM utilization spike from arbitrageurs swapping GHO→USDC for safety
- Lending-protocol-wide sentiment

**Deviation**: $1.001 → $0.992 (90bp); reverted in ~36 hours.

### crvUSD (Curve over-collateralized via LLAMMA)

**Mechanism**: crvUSD has zero direct exposure to LayerZero or KelpDAO. But crvUSD is heavily traded against Curve 3pool (USDC/USDT/DAI), and the panic-flow into "safest stables" (USDC, USDT) caused 3pool composition to skew, secondarily affecting crvUSD pools.

**Specific channels**:
- Curve 3pool imbalance during panic flight-to-safety
- Some crvUSD-collateralized vaults using LRTs as collateral (small but present)
- General DeFi-wide risk-off

**Deviation**: $1.000 → $0.996 (40bp); reverted in ~24 hours.

### sUSDe (Ethena delta-neutral)

**Mechanism**: sUSDe is normally above-peg ($1.01-1.05) due to embedded yield. During panic, the yield premium compresses as participants prefer USDC/USDT.

**Specific channels**:
- Ethena reserve fund unaffected (no direct exposure)
- ETH perp funding remained positive (no mechanism stress)
- Pure flight-to-stables/USDC behavior

**Deviation**: $1.018 → $1.005 (yield-premium compression of 130bp); reverted as panic subsided.

### USDe (Ethena base)

**Mechanism**: same Ethena delta-neutral mechanism; held closer to par throughout.

**Deviation**: $1.000 → $0.998 (20bp); reverted within hours.

## Trade: Sympathy-Depeg Basket

### Position structure

The play was a **long basket of sympathy-depegged synthetic stables** during the 4-72 hour window:

| Stable | Entry price | Size (% of basket) | Exit price | Holding period |
|--------|-------------|-------------------|------------|----------------|
| GHO | $0.993 | 35% | $0.999 | ~36h |
| crvUSD | $0.996 | 30% | $1.000 | ~24h |
| sUSDe | $1.008 | 20% | $1.015 | ~48h |
| USDe | $0.999 | 15% | $1.000 | ~12h |

### P&L worked example

- Capital deployed: $5M across the basket
- Allocation per the table above
- Holding period: 24-72h (longest leg)
- Per-leg returns:
  - GHO leg ($1.75M): +0.6% = $10,500
  - crvUSD leg ($1.5M): +0.4% = $6,000
  - sUSDe leg ($1.0M): +0.7% = $7,000 (note: sUSDe yield-premium reversion has different mechanics)
  - USDe leg ($0.75M): +0.1% = $750
- **Total P&L**: ~$24,250 on $5M = ~0.5% over 36-72h (annualized ~30-50%)

Modest absolute return per event but capacity-friendly and Sharpe-attractive (~3.0+ given short duration and bounded downside).

### Risks

- **Misclassification of sympathy vs structural**: if Aave bad debt had been worse than projected (say $500M+), GHO might NOT have reverted — could have traded structurally lower for weeks. Position sizing reflected this risk via cheap-to-carry sizing.
- **Capital lockup**: 24-72h holding period vs always-on alternatives like funding-arb.
- **Multi-mechanism risk**: each leg has independent mechanism risk; basket diversifies but doesn't eliminate.

## Who Traded This Successfully

Limited public attribution but active participants likely included:

- **Cumberland (DRW)** — institutional OTC; deep stablecoin coverage
- **Wintermute** — UK market maker; on-chain DeFi specialist
- **Galaxy Digital** — Mike Novogratz's firm
- **B2C2** — UK market maker
- **Various DeFi-native funds** (Ramp Capital, Polychain, Variant) — known to track LRT contagion patterns

The 24-72h window required:
- Real-time exploit-feed integration (per [[exploit-arb-implementation-guide]])
- Pre-positioned execution wiring on Curve, Balancer, Hyperliquid, Binance
- Mechanism-specific risk models for GHO, crvUSD, sUSDe distinguishing sympathy from structural
- Capital ready to deploy on alert

## Why This Was a "First"

KelpDAO is the **canonical AI-era contagion case** because it demonstrated:

1. **Cross-mechanism contagion at speed**: 4 different stable mechanisms (Aave overcollateralized, Curve LLAMMA, Ethena delta-neutral, Ethena bridged) all reacted within hours of a single incident. Prior crashes (Terra/UST May 2022, USDC/SVB March 2023) had cleaner single-mechanism narratives.

2. **The 50× contagion multiplier**: $290M direct loss → $15B TVL drain → measurable secondary depegs. This ratio is the floor case for [[cross-chain-contagion-hedge]] sizing.

3. **AI-era exploit + market-structure speed**: Aave Guardian froze rsETH within 25 minutes; Circle froze USDC within 60 minutes. The speed of institutional response was unprecedented and itself caused some sympathy-depeg behavior (panic about which assets would freeze next).

4. **Validated the watchlist approach**: protocols on the [[2026-exploit-target-watchlist]] (Aave V3 contagion, Sui DeFi, LayerZero V2) all behaved according to the watchlist's tier rankings. The sympathy depeg trade was directly anticipated by the watchlist's contagion methodology.

## Lessons for Modern Stable Depeg Trading

This case study informs three principles for [[stablecoin-depeg-profit-capture]] and [[synthetic-stablecoin-depeg-arbitrage]]:

1. **Sympathy depegs are real and tradable.** Not all peg deviations require direct exposure. Cross-mechanism panic-flow + lending-protocol contagion produces measurable, mean-reverting deviations on stables not directly affected.

2. **The 30-80bp deviation range is the sweet spot.** Smaller deviations (<30bp) get crowded out by HFT mean-reversion. Larger deviations (>100bp) are usually structural, not sympathy. The 30-80bp band is where retail/mid-tier doesn't notice but the mechanism is solvable.

3. **Multi-source exploit-feed integration is the alpha leg.** Without sub-30-second alerting (per [[exploit-arb-implementation-guide]]), the sympathy-depeg trade is impossible because the price moves before the trader can respond. With it, the trade is genuinely available.

4. **Basket sizing > single-name sizing.** A single-name sympathy-depeg trade has too much idiosyncratic risk (what if THIS stable is structurally compromised?). The basket of 4-6 sympathy-depegged stables diversifies that risk while still capturing the mean-reversion edge.

## Sources

- Galaxy Research: "KelpDAO LayerZero Exploit DeFi" (April 2026)
- LayerZero post-mortem on KelpDAO incident
- Halborn Apr 2026 contagion analysis
- Aave Guardian freeze logs (on-chain)
- Curve, Balancer, Aave dashboards (peg + composition data)
- Multi-source exploit alerts (PeckShield, BlockSec, Cyvers archives)
- DeFiLlama TVL history (Apr 17-25, 2026)

## Related

- [[synthetic-stablecoin-depeg-arbitrage]] — sympathy-depeg variant strategy this validates
- [[stablecoin-pair-arbitrage]] — fiat-backed companion
- [[stablecoin-depeg-profit-capture]] — Method 1 + 5 application
- [[cross-chain-contagion-hedge]] — broader contagion strategy this is the stable-leg of
- [[ai-amplified-exploit-arbitrage]] — hub strategy
- [[2026-exploit-target-watchlist]] — Tier 2 LayerZero V2 was flagged ex-ante
- [[ai-vulnerability-discovery]] — capability frame
- [[ethena-usde]] · [[ethena]] · [[curve-finance]] · [[makerdao]] — entity pages
- [[stablecoin-depeg-history]] — master timeline
