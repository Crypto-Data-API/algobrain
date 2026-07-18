---
title: "Convex Finance (Protocol)"
type: entity
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [crypto, defi, ethereum]
entity_type: protocol
founded: 2021
website: "https://www.convexfinance.com"
aliases: ["Convex", "Convex Finance", "CVX", "vlCVX", "convex-finance", "cvx"]
related: ["[[curve-finance]]", "[[curve-dao-token]]", "[[defi]]", "[[ethereum]]", "[[yearn]]", "[[yield-farming]]", "[[balancer]]", "[[lido]]", "[[curve-gauge-wars-arbitrage]]"]
---

# Convex Finance

**Convex Finance** (CVX) is a yield-optimization protocol built on top of [[curve-finance|Curve Finance]] that aggregates veCRV voting power. Launched in May 2021, Convex lets CRV holders and Curve LPs earn boosted rewards without personally locking CRV for four years — and in doing so it accumulated the single largest veCRV position, effectively "winning" the **Curve Wars** and making CVX the meta-governance token of the Curve ecosystem.

---

## How It Works

1. Users deposit CRV into Convex and receive **cvxCRV** (liquid, tradeable), while Convex permanently locks the underlying CRV as veCRV.
2. Curve LPs stake their LP tokens through Convex and receive Curve's maximum 2.5x emission boost from Convex's pooled veCRV — without holding any veCRV themselves.
3. **vlCVX** (vote-locked CVX, 16-week lock) holders direct how Convex's massive veCRV stake votes on Curve gauge weights — and collect bribes from protocols (via marketplaces like **Votium**) that want CRV emissions steered to their pools.
4. Convex takes a platform fee on Curve rewards and distributes it to cvxCRV stakers and vlCVX lockers.

The same model was later extended to Frax Finance (cvxFXS / FXS gauges) and Prisma, making Convex a general "governance aggregation" layer.

## Key Facts and Numbers

| Metric | Value |
|---|---|
| **Launched** | May 2021 |
| **Peak TVL** | ~$20B+ (January 2022, height of the Curve Wars) |
| **TVL (March 2025)** | ~$867M, ~97% of it on Ethereum (~$838M) |
| **veCRV share** | ~40-50% of all veCRV historically controlled via Convex — the largest single bloc |
| **CVX max supply** | 100M, minted pro-rata against CRV earned by the platform; ~89.9M circulating / ~99.96M total |
| **CVX price** | ~$1-2 range in 2025-2026 (ATH $60.09 on 2022-01-01, -97% since; ATL $1.36 on 2025-10-10); verify on CoinGecko |
| **Contract (Ethereum)** | `0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b` |
| **Vote-locked float** | >40% of CVX supply remains vote-locked as vlCVX (2026), limiting sellable float to roughly 54M of ~90M circulating tokens — a structurally tight float relative to market cap |

## Status as of 2026

The Curve Wars have cooled dramatically from their 2021-2022 peak: bribe volumes on Votium and overall Convex TVL are an order of magnitude below the highs, tracking the broader decline in CRV price and stablecoin-pool incentive budgets. By late 2025 Convex TVL sat near ~$1.0B as Curve's own TVL stabilized in the ~$2.6–4B range (Curve TVL ~$2.63B for the week ending 2026-01-15, ~$4B as of October 2025). Convex nonetheless remains the dominant veCRV aggregator and the default route for boosted Curve LP yield, and vlCVX bribe income remains one of DeFi's longest-running "real yield" streams. Convex's fortunes are structurally leveraged to [[curve-finance|Curve]]: CRV price, crvUSD adoption, and gauge-incentive demand flow directly through to cvxCRV/vlCVX yields. The main bull case is a Curve revival (a major v2 upgrade or stablecoin/RWA flows); the bear case is continued share loss to newer stablecoin DEXs (e.g., Maverick).

---

## Trading Relevance

- **CVX is leveraged CRV beta**: CVX historically amplifies CRV moves because Convex revenue is a function of CRV emissions and bribe demand.
- **Bribe yield as a signal**: $/vlCVX per voting round on Votium is a measurable "price of liquidity" in DeFi — rising bribe yield signals new stablecoin/LST issuers competing for Curve liquidity (historically 8-25% APY at the peak, far lower in 2025-2026).
- **cvxCRV/CRV peg**: cvxCRV is irreversibly backed (CRV in is locked forever), so cvxCRV trades at a floating discount to CRV; the discount widens in risk-off periods and has been a recurring mean-reversion/carry trade.
- **Governance concentration risk**: a single protocol controlling ~half of veCRV is a standing systemic-governance risk for the whole Curve ecosystem.
- **Float squeeze mechanics**: with >40% of supply locked for 16 weeks at a time, CVX can move violently on modest flows — relevant for both momentum and liquidity-risk sizing.
- **Governance-attack monitoring**: large vlCVX accumulations (e.g., by stablecoin issuers) telegraph future gauge-weight shifts, which in turn predict where Curve liquidity and stable-pool depth will migrate.
- **Bribe-market relative value**: comparing annualized bribe yield to CVX price is a classic DeFi screen — see [[curve-gauge-wars-arbitrage]].

---

## Related

- [[curve-finance]] — the protocol Convex is built on (see "Curve Wars" section)
- [[curve-dao-token]] — CRV token page
- [[curve-gauge-wars-arbitrage]] — strategy page on gauge/bribe dynamics
- [[crv]] — CRV token (redirects to Curve Finance)
- [[yearn]] — competing/complementary yield aggregator and early Curve Wars combatant
- [[balancer]] — analogous veBAL system with Aura Finance as its "Convex"
- [[lido]] — stETH liquidity was a major driver of Curve gauge bribes
- [[yield-farming]] — the broader strategy category
- [[defi]] — ecosystem context

## Sources

- Convex Finance docs — https://docs.convexfinance.com
- CoinMarketCap, "What Is Convex Finance (CVX) And How Does It Work?" — https://coinmarketcap.com/cmc-ai/convex-finance/what-is/
- Switchere, "Convex Finance: How One Protocol Mastered the Curve Wars" — https://switchere.com/guides/cvx-coin (TVL ~$867M as of March 2025; veCRV share 40-50%)
- BestChange, "Convex Finance (CVX) — a protocol for maximizing Curve returns" — https://www.bestchange.com/blog/convex-cvx-protocol
- CoinMarketCap — Convex Finance (CVX) price page: https://coinmarketcap.com/currencies/convex-finance/
- Crypto News Navigator — "Three On-Chain Metrics Explain CVX's 2026 Trajectory": https://www.cryptonewsnavigator.com/academy/article/three-on-chain-metrics-explain-cvxs-2026-trajectory
- OneKey — "CVX Deep Research Report: Token Future and Price Outlook": https://onekey.so/blog/ecosystem/cvx-deep-research-report-token-future-and-price-outlook/
- CoinDesk — "CRV Extends Rally as 'Curve Wars' Intensify" (2022-01-04): https://www.coindesk.com/markets/2022/01/04/crv-extends-rally-as-curve-wars-intensify
- (Source: [[coingecko-top-1000-2026-04-09]]) — market-data snapshot (price, supply, contract, listings)
- Verified via web search and Perplexity, 2026-06-10
