---
title: "Derivatives-Native Regime"
type: concept
created: 2026-06-03
updated: 2026-07-13
status: good
tags: [crypto, derivatives, market-regime, market-microstructure, leverage, quantitative]
aliases: ["Derivatives-Native Regime", "Perps Regime", "Funding/OI Regime"]
domain: [market-microstructure, derivatives]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[basis-carry-regime]]", "[[liquidity-depth-regime]]", "[[funding-rate]]", "[[open-interest]]", "[[liquidation]]", "[[liquidation-cascade-modeling]]", "[[liquidation-cascade-fade]]", "[[funding-rate-arbitrage]]", "[[short-squeeze]]", "[[2025-10-crypto-liquidation-cascade]]", "[[hyperliquid]]", "[[hyperliquid-funding-rate-microstructure]]", "[[cryptodataapi]]"]
---

The **Derivatives-Native regime** is basket #4 of the 14-basket crypto regime taxonomy (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). It groups the trading setups that exist *only* in perpetual-futures markets and have no spot-market analogue: funding-rate extremes, open-interest (OI) imbalance, liquidation cascades, and long/short squeezes. These are not directional theses about where price "should" go — they are positioning-fragility states detectable from derivatives plumbing. This basket is the most [[hyperliquid|Hyperliquid]]-relevant of the fourteen, because Hyperliquid combines high leverage with on-chain transparency, exposing per-coin positioning fragility in real time. Setups here play out on a minutes-to-days timescale and fire in both directions. This page is a regime synthesis: it frames the mechanics (explained elsewhere) as detectable *states* with a bias and a trade. See [[crypto-market-regime-taxonomy]] for the full basket map.

## Sub-Regimes

Each sub-regime below is a state, not a mechanic. For *how* the underlying instruments work, follow the links out.

### Funding Rate Extreme (Long) — bias: Fade longs
- **Signal**: [[funding-rate]] sustained above ~0.1% per 8h (a framework heuristic, Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) across one or more venues — longs are paying heavily to stay long. Persistence matters more than a single print.
- **Bias**: Longs overheated; mean-reversion / reversal increasingly likely as the long side becomes crowded and cost-burdened.
- **What to trade**: Fade the long crowd — short into the extreme, or harvest the funding via [[funding-rate-arbitrage]] (short perp / long spot). On Hyperliquid, cross-reference [[hyperliquid-funding-rate-microstructure]] for per-coin funding behaviour. See [[funding-rate]] for mechanics.

### Funding Rate Extreme (Short) — bias: Fade shorts
- **Signal**: Sustained deeply negative [[funding-rate]] — shorts paying to stay short, signalling an overextended short side.
- **Bias**: Shorts crowded and cost-burdened; squeeze risk elevated.
- **What to trade**: Long into the extreme; the asymmetry favours an upside snap as shorts are forced to cover. Pairs naturally with the **Liquidation Cascade Up** state below.

### Liquidation Cascade Down — bias: Short → Long
- **Signal**: A large cluster of long liquidations is hit, [[liquidation]] flow begets more liquidations, and the move accelerates self-referentially. Watch liquidation clustering and OI bleeding off.
- **Bias**: Momentum-down during the flush, then a sharp snap-back once forced selling exhausts.
- **What to trade**: Short the cascade *while it runs*, cover into the flush, then fade the over-shoot reversal ([[liquidation-cascade-fade]]). The October 2025 event ([[2025-10-crypto-liquidation-cascade]]) is the canonical example. See [[liquidation]] for mechanics.

### Liquidation Cascade Up — bias: Long → Short
- **Signal**: A [[short-squeeze]] cascade — short liquidations trigger forced buying, price gaps up, and OI collapses as shorts are flushed out.
- **Bias**: Violent upside during the squeeze, then exhaustion once shorts are cleared and there is no more forced buying.
- **What to trade**: Ride or front-run the squeeze, then short the exhaustion once OI has collapsed and funding flips sharply positive. See [[short-squeeze]] for mechanics.

### OI Divergence — bias: Counter-trend
- **Signal**: Price and [[open-interest]] disagree. Price up while OI falls = a rally on closing positions, a weakening / unconvincing trend. Price down while OI rises = new conviction shorts being added into weakness.
- **Bias**: Counter-trend — the divergence flags that the visible price move is not backed by fresh positioning.
- **What to trade**: Fade rallies that lack OI support; respect (or join) down-moves where OI is building on the short side. See [[open-interest]] for mechanics.

### Funding Rate Arbitrage — bias: Delta-neutral
- **Signal**: Funding is persistently signed enough to pay for the carry.
- **Bias**: Market-neutral; the edge is the funding stream, not direction.
- **What to trade**: Positive funding → short perp + long spot to collect funding; negative funding → long perp + short spot. See [[funding-rate-arbitrage]] for mechanics — and note the ADL caveat in **Pitfalls** below.

### Long/Short Squeeze Setup — bias: Both
- **Signal**: Lopsided OI build-up — one side of the book is crowded relative to the other (read alongside long/short ratio and funding sign).
- **Bias**: Either direction; the crowded side is the fuel for a forced unwind.
- **What to trade**: Position for the *unwind of the crowded side*. This is the pre-condition that, when triggered, becomes a **Liquidation Cascade** state above.

## Detection Signals

The basket is read from four primary derivatives signals:

1. **Funding** — sign, level, and persistence. A momentary spike is noise; multi-period persistence above/below the ~0.1%/8h heuristic (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) is the regime signal. See [[funding-rate]].
2. **Open interest vs price** — whether OI confirms or diverges from the price move (the OI Divergence state). See [[open-interest]].
3. **Liquidation clustering** — density and direction of [[liquidation]] events; clusters mark the trigger zones for cascades.
4. **Long/short ratio** — which side is crowded, feeding the squeeze-setup read.

**Hyperliquid structural edge**: because Hyperliquid is an on-chain perp venue, per-coin OI, funding, and liquidation data are transparent in real time rather than reconstructed from a CEX's partial feeds. For a basket built entirely on reading positioning fragility, that observability is itself the edge. See [[hyperliquid]] and [[hyperliquid-funding-rate-microstructure]].

## Fragility Synthesis

The most dangerous alignment is not any single extreme but the *stack* — this basket's **funding + OI leg** combined with a crowded [[basis-carry-regime|basis]] and OI outrunning [[liquidity-depth-regime|book depth]]. The full mechanism (why the three together, not any one alone, are the pre-cascade fingerprint of the [[2025-10-crypto-liquidation-cascade|October 2025 cascade]]) is stated canonically in [[crypto-market-regime-taxonomy#The Fragility Triad (canonical)|the taxonomy]]. The piece this basket owns: persistent positive [[funding-rate]] + record [[open-interest]] means leverage is building, not bleeding — the loaded gun the other two legs then determine whether to fire.

## Relationship to Other Regimes

This is a **fragility detector, not a directional backdrop**. It does not tell you the macro trend; it tells you when leveraged positioning is primed to break.

- Pairs with [[liquidity-depth-regime]]: depth determines whether an OI imbalance resolves orderly or cascades.
- Pairs with [[basis-carry-regime]]: carry builds the leverage this basket monitors for failure.
- Overrides the backdrop short-term: a liquidation cascade can dominate price action for hours regardless of the [[macro-trend-regime]] direction, then hand control back once positioning resets.

## Pitfalls

- **Fading a funding extreme too early.** Extremes can persist far longer than they "should"; sustained funding is a *condition*, not a timing trigger. Wait for a confirming OI roll-over or liquidation cluster before fading.
- **Confusing healthy OI growth with fragility.** Rising OI alongside spot inflows and adequate [[liquidity-depth-regime|book depth]] is a healthy trend, not a powder keg. Fragility requires OI outrunning depth.
- **Assuming "delta-neutral" is safe.** A [[funding-rate-arbitrage]] book can blow up if auto-deleveraging (ADL) force-closes the perp leg mid-cascade, leaving the spot leg naked at the worst moment. Model ADL and cascade dynamics explicitly — see [[liquidation-cascade-modeling]].

## Sources

- (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) — defines the 14-basket taxonomy and the funding/OI/liquidation heuristics used here.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[crypto-market-regime-taxonomy]] — hub for all 14 baskets
- [[basis-carry-regime]] — overlapping carry basket that builds the leverage
- [[liquidity-depth-regime]] — depth side of the fragility equation
- [[funding-rate]] · [[open-interest]] · [[liquidation]] — underlying mechanics
- [[liquidation-cascade-modeling]] · [[liquidation-cascade-fade]] · [[short-squeeze]] — cascade and squeeze mechanics
- [[funding-rate-arbitrage]] — delta-neutral funding harvest
- [[2025-10-crypto-liquidation-cascade]] — canonical cascade event
- [[hyperliquid]] · [[hyperliquid-funding-rate-microstructure]] — the most relevant venue for this basket
