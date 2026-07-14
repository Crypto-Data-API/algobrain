---
title: "Gap Finder: Hyperliquid Low-Timeframe Perp Backtesting"
type: source
created: 2026-06-02
updated: 2026-06-12
status: good
tags: [meta, backtesting, crypto, derivatives, market-microstructure, data-provider]
aliases: ["Hyperliquid LTF Backtesting Gap Finder", "Hyperliquid Perp Backtesting Gap Report"]
source_type: data
source_url: "https://hyperliquid.gitbook.io/hyperliquid-docs"
source_author: "Perplexity (sonar)"
source_date: 2026-06-02
source_file: "raw/articles/2026-04-22-gap-finder-hyperliquid-crypto-perpetual-exchange-lo.md"
confidence: low
claims_count: 5
related: ["[[bar-resolution-selection]]", "[[intrabar-fill-modeling]]", "[[multiple-timeframe-analysis]]", "[[microstructure-noise-low-timeframe]]", "[[overfitting]]", "[[crypto-perp-backtesting-pitfalls]]", "[[hyperliquid]]", "[[dydx]]"]
---

# Gap Finder: Hyperliquid Low-Timeframe Perp Backtesting

#meta — this is a **gap-direction report**, not a factual source. It was produced by a Perplexity gap-analysis run (Perplexity `sonar`) on 2026-06-02 to identify wiki coverage gaps for *Hyperliquid + low-timeframe (1m/3m/5m/15m) perpetuals backtesting*. The deep-research (`sonar-deep-research`) variant failed twice with a dropped connection; the fast `sonar` run succeeded. Use this report to decide **what to write**, not as content to copy — its specific figures are unverified and several "missing" venues it lists (Binance, Bybit, OKX, GMX, dYdX, CCXT, Kaiko, CoinAPI, Glassnode) already have wiki pages, so the report is partly out of date on coverage.

Raw report: `raw/articles/2026-04-22-gap-finder-hyperliquid-crypto-perpetual-exchange-lo.md`

## Claims Extracted

These are the substantive claims the report surfaced. Because the report is a fast-`sonar` gap-direction artifact (deep mode failed) drawing partly on YouTube/analytics explainers, confidence is uniformly low-to-medium and figures are unverified — re-confirm against the cited Hyperliquid docs before quoting in any page.

1. **[MEDIUM]** Hyperliquid contract specifications (tick sizes, margin tiers, funding cadence, maximum leverage per pair) are documented in the official Hyperliquid GitBook and are the authoritative reference for any low-timeframe (1m/3m/5m/15m) backtest of HYPE-listed perps. Source: hyperliquid.gitbook.io contract-specifications.
2. **[LOW]** A HYPE perpetual was the subject of a Coinbase listing breakdown in 2026 per Bitget Academy — venue-expansion context, not a verified backtesting input. Source: Bitget Academy.
3. **[MEDIUM]** Low-timeframe perp backtesting requires explicit treatment of bar-resolution / event-time sampling, microprice, order-book imbalance, queue position, and adverse selection — methodology gaps the wiki did not previously cover. (Actioned into new pages; see below.)
4. **[MEDIUM]** Robust LTF perp research needs walk-forward / purged cross-validation and volatility-regime filters as overfitting controls. (Actioned into [[overfitting]].)
5. **[LOW]** Several venues the report listed as "missing" (Binance, Bybit, OKX, GMX, dYdX, CCXT, Kaiko, CoinAPI, Glassnode) already have wiki pages — the report's coverage map is partly stale, so its "missing venue" claims should not be trusted at face value.

## Gaps It Flagged (and how they were actioned)

- **Bar-resolution / event-time work, microprice, order-book imbalance, queue position, adverse selection** → new pages [[bar-resolution-selection]], [[intrabar-fill-modeling]], [[microstructure-noise-low-timeframe]].
- **Multi-timeframe / top-down structure** → expanded [[multiple-timeframe-analysis]] with a systematic-backtest look-ahead section and a crypto-perp stack.
- **Walk-forward / purged CV, volatility-regime filters (overfitting controls)** → expanded [[overfitting]].
- **dYdX comparator depth** → expanded [[dydx]].
- **Already covered (no action):** Binance/Bybit/OKX/GMX exchange pages, [[ccxt|CCXT]], Kaiko, CoinAPI, Glassnode, [[crypto-perp-backtesting-pitfalls]], ADL/liquidation-cascade pages.

## Citations from the Raw Report

1. Hyperliquid docs — contract specifications: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications
2. Bitget Academy — HYPE perpetual Coinbase listing breakdown (2026)
3-6. Assorted YouTube / analytics explainers (low confidence)

## Related

- [[bar-resolution-selection]]
- [[intrabar-fill-modeling]]
- [[multiple-timeframe-analysis]]
- [[microstructure-noise-low-timeframe]]
- [[overfitting]]
- [[crypto-perp-backtesting-pitfalls]]
- [[hyperliquid]]
- [[dydx]]
