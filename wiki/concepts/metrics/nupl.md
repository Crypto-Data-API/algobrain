---
title: "Net Unrealized Profit/Loss (NUPL)"
type: concept
created: 2026-06-24
updated: 2026-07-13
status: draft
tags: [crypto, bitcoin, indicators, valuation, market-microstructure, behavioral-finance]
aliases: ["NUPL", "Net Unrealized Profit/Loss", "Net Unrealized Profit Loss", "net-unrealized-profit-loss"]
domain: [market-microstructure]
prerequisites: ["[[mvrv]]", "[[realized-price]]"]
difficulty: intermediate
related: ["[[mvrv]]", "[[mvrv-z-score]]", "[[realized-price]]", "[[sopr]]", "[[on-chain-analysis]]", "[[market-capitalization]]", "[[bitcoin]]", "[[market-cycle]]", "[[glassnode]]", "[[cryptoquant]]", "[[behavioral-finance]]", "[[cryptodataapi]]"]
---

**Net Unrealized Profit/Loss (NUPL)** is an [[on-chain-analysis|on-chain]] sentiment-and-valuation metric that expresses the aggregate paper profit or loss held across all holders as a *fraction of* [[market-capitalization|market cap]]. It is closely related to [[mvrv|MVRV]] — both compare market cap to [[realized-price|realized cap]] — but where MVRV is a ratio, NUPL is a normalised percentage that maps neatly onto a set of named psychological "colour bands" describing market mood. It is a popular [[bitcoin]] cycle gauge on [[glassnode]] and [[cryptoquant]].

## How It Is Computed

```
NUPL = (Market Cap − Realized Cap) / Market Cap
```

Equivalently:

```
NUPL = 1 − (Realized Cap / Market Cap) = 1 − (1 / MVRV)
```

- **Market Cap − Realized Cap** is the aggregate *unrealized* profit (positive) or loss (negative) embedded in the supply.
- Dividing by **Market Cap** rescales it to a bounded percentage, so NUPL typically lives roughly between −1 and +1: positive when the supply is in aggregate profit, negative when in aggregate loss, and near zero when the market sits at its [[realized-price|cost basis]].

A common variant separates the supply into long-term and short-term holder cohorts (LTH-NUPL / STH-NUPL), and **entity-adjusted** versions strip internal exchange transfers so the cost basis better reflects genuine ownership changes — conceptually adjacent to the adjustment that aSOPR makes to [[sopr|SOPR]].

## Interpretation / How Traders Use It

NUPL's signature feature is its mapping to named psychological **colour bands**, read as a progression through a [[market-cycle]] driven by [[behavioral-finance|crowd psychology]]:

- **Capitulation** (NUPL negative): the supply is in aggregate loss; sellers exhausting. Historically a late-bear accumulation zone.
- **Hope / Fear** (NUPL slightly positive to near zero): the market is recovering from or sliding into stress; small aggregate profit.
- **Optimism / Anxiety** (low-to-mid positive): a building uptrend with moderate unrealized gains.
- **Belief / Denial** (mid-to-high positive): strong trend with large embedded profit.
- **Euphoria / Greed** (high positive): extreme aggregate unrealized profit; *historically* coincident with overheated, top-risk conditions and heavy distribution potential.

The exact percentage boundaries between bands drift across cycles and should be read qualitatively. Because NUPL is just a monotonic transform of [[mvrv]], it carries the same valuation information; traders favour it for its intuitive sentiment narrative and pair it with [[sopr]] (is profit actually being realised?), [[mvrv-z-score]] (statistical extremes), and flow metrics like [[exchange-netflow]].

## Illustrative Example

If [[bitcoin]]'s market cap is well above its realized cap — say realized cap is roughly half of market cap — NUPL reads about +0.5, placing the market in the upper "belief/euphoria" range: holders collectively sit on large paper gains, and the metric flags rising distribution risk. If price later collapses below the realized price, market cap falls under realized cap, NUPL turns negative, and the metric drops into the "capitulation" band — the kind of reading that has historically marked oversold, bottoming conditions.

## Limitations and Pitfalls

- **Redundant with MVRV**: NUPL contains no information beyond MVRV (it is `1 − 1/MVRV`); its value is interpretive framing, not an independent signal.
- **Lagging at turns**: as a valuation/sentiment gauge it confirms regimes rather than timing exact tops and bottoms; it can sit in a band for an extended period.
- **Lost and dormant supply**: realized cap assumes coins reflect a live cost basis; provably lost, burned, or ancient dormant coins distort the aggregate and bias NUPL.
- **Entity/exchange adjustments**: internal custodial transfers can reset the "last-moved price" without a real ownership change; entity-adjusted variants help, but the label layer is provider-produced and revised over time (see [[on-chain-analysis#Leading vs Lagging, and Data Caveats]]).
- **Band drift across cycles**: the percentage thresholds that named earlier euphoria/capitulation phases have shifted as the asset matured; treat the colour bands qualitatively, not as fixed lines.
- **Best for mature assets**: most reliable for [[bitcoin]]; noisier on thin or newer chains.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — CEX inflow/outflow (1h/6h/24h/7d, per-exchange breakdown)
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — stablecoin dry-powder z-score signal
- `GET /api/v1/on-chain/miners/reserves` — BTC miner pool reserves + flows
- `GET /api/v1/on-chain/miners/hash-ribbon` — Hash Ribbon state (capitulation/recovery/normal)
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + supply-shock zone classification
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100)

**Historical data:**
- `GET /api/v1/on-chain/whale-score/{symbol}` — whale accumulation score timeseries
- `GET /api/v1/market-intelligence/stablecoin-history` — stablecoin market-cap timeseries

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]].

## Related

- [[mvrv]] — NUPL is a direct transform of the MVRV ratio
- [[mvrv-z-score]] — Standardised cycle-extreme companion
- [[realized-price]] — Realized cap underlies the unrealized P/L calculation
- [[sopr]] — Whether the embedded profit/loss is actually being realised
- [[on-chain-analysis]] — Parent mechanics page
- [[market-cycle]] — The cycle the colour bands track
- [[behavioral-finance]] — The crowd psychology the bands describe
- [[glassnode]], [[cryptoquant]] — Providers that popularised the metric

## Sources

General market knowledge; no specific wiki source ingested yet.
