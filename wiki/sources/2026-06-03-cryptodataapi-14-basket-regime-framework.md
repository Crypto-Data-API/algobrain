---
title: "Crypto Data API — 14-Basket Market Regime Framework"
type: source
created: 2026-06-03
updated: 2026-06-12
status: good
tags: [meta, crypto, derivatives, market-microstructure, data-provider, quantitative]
aliases: ["14-Basket Regime Framework", "Crypto Data API Regimes", "Market Regimes Framework"]
source_type: article
source_url: "https://cryptodataapi.com/regimes"
source_author: "Crypto Data API (VENTURE AI LABS)"
source_date: 2026-06-03
confidence: medium
claims_count: 14
related: ["[[crypto-market-regime-taxonomy]]", "[[regime-matrix]]", "[[market-regime-detection-ml]]", "[[hyperliquid]]"]
---

# Crypto Data API — 14-Basket Market Regime Framework

#meta — source summary for the **Crypto Data API "Market Regimes" framework** (cryptodataapi.com/regimes), a product of **VENTURE AI LABS**. It defines **14 meta-baskets** that "capture every state crypto markets can be in," each implying a distinct set of coins, leverage levels, holding durations, and funding-cost tolerance. The framework is explicitly **designed for systematic perps trading on venues like [[hyperliquid|Hyperliquid]]**. This is the canonical structure the wiki's [[crypto-market-regime-taxonomy|crypto regime taxonomy]] is organised around.


## The 14 Meta-Baskets

| # | Basket | Timescale | Bias | Wiki page |
|---|---|---|---|---|
| 1 | Macro Trend | Months | Long/Short | [[macro-trend-regime]] |
| 2 | BTC Cycle | Weeks–Months | Long/Neutral | [[bitcoin-cycle-regime]] |
| 3 | Meme / Speculative | Hours–Days | Long/Short | [[meme-speculative-regime]] |
| 4 | Derivatives-Native | Minutes–Days | Both | [[derivatives-native-regime]] |
| 5 | Event / Catalyst | Hours–Weeks | Both | [[event-catalyst-regime]] |
| 6 | Macro Correlation | Days–Weeks | Short/Long | [[crypto-macro-correlation-regime]] |
| 7 | On-Chain Intelligence | Days–Weeks | Leading | [[on-chain-regime]] |
| 8 | Carry Trade / Basis | Days–Weeks | Regime health | [[basis-carry-regime]] |
| 9 | Liquidity / Market Depth | Real-time–Days | Size filter | [[liquidity-depth-regime]] |
| 10 | Institutional Flow | Weeks–Months | Structural floor | [[institutional-flow-regime]] |
| 11 | Security / Black Swan | Hours–Days | Short→Long | [[security-black-swan-regime]] |
| 12 | Geopolitical / Policy Shock | Hours–Weeks | Both | [[policy-shock-regime]] |
| 13 | Volatility Regime | Days–Weeks | Risk overlay | [[volatility-regime-classification]] |
| 14 | Technical / Structural | Hours–Days | Universal overlay | [[technical-structural-regime]] |

## Key Claims

- **[MEDIUM]** Regimes should be treated as **distinct strategies gated by detection**; mixing them ("bull-run logic firing during a liquidation cascade, range-fade dying on a breakout") turns one strategy into noise inside another. This is the framework's central thesis and aligns with the wiki's [[regime-adaptive-strategy]].
- **[MEDIUM]** **OI growing faster than order-book depth** was "the single clearest pre-crash warning" in the October 2025 cascade — see [[liquidity-depth-regime]], [[2025-10-crypto-liquidation-cascade]].
- **[MEDIUM]** Persistent **positive funding + record OI = fragility forming**; basis collapse precedes cascades — see [[basis-carry-regime]].
- **[MEDIUM]** **ETF inflows set structural floors** defending cost-basis levels ("$80K BTC was the 2025 ETF floor") — see [[institutional-flow-regime]]. Specific price level is unverified.
- **[MEDIUM]** The **2025 Bybit hack ($1.46B)** created a forensic regime: immediate OI unwind → self-custody withdrawals → institutional reaccumulation — see [[security-black-swan-regime]].
- **[LOW]** Compressed vol (~30% annualized ATR) is "the most dangerous setup" — masks leverage buildup before cascades. Treat thresholds as illustrative.

## Confidence & Caveats

Confidence is **medium**: the framework is a coherent, practitioner-grade taxonomy from a commercial data vendor, not peer-reviewed research. Specific numeric thresholds (funding >0.1%/8h, basis 8%+ APR, DXY >105, $80K ETF floor, $500M/week inflows) are **illustrative heuristics** — they are reproduced on the regime pages as the vendor's stated signals, not as independently verified facts. Several baskets were marked "coming soon" / "live" at capture; the taxonomy itself is complete.

## Related

- [[crypto-market-regime-taxonomy]] — the consolidated wiki hub built from this framework
- [[regime-matrix]] — the wiki's strategy-by-regime matrix (orthogonal, 6-dimension)
- [[market-regime-detection-ml]] — ML detection methods for these regimes
- [[regime-adaptive-strategy]] — regime-gated strategy switching
- [[hyperliquid]] — the venue the framework is designed for
