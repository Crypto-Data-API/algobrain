---
title: "Bitcoin Dominance & Alt-Season Rotation — Narrative Impact"
type: concept
created: 2026-06-04
updated: 2026-07-13
status: good
tags: [crypto, bitcoin, market-regime, market-microstructure, narrative-impact]
aliases: ["BTC Dominance", "Altcoin Season", "BTC.D"]
related: ["[[crypto-narratives-overview]]", "[[l1-l2-rotation]]", "[[memecoin-mania]]", "[[cryptodataapi]]"]
domain: [market-microstructure, behavioral-finance]
difficulty: intermediate
---

Bitcoin dominance (**BTC.D** = Bitcoin's market cap ÷ total crypto market cap) is the master gauge for how capital rotates *within* crypto. Rising dominance means money is concentrating in Bitcoin — early-bull accumulation, ETF-driven legs, or risk-off flight-to-quality. Falling dominance means capital is rotating down the risk curve into altcoins ("alt-season"), historically a late-cycle, risk-on euphoria signal. For a backtester, dominance is best used as a **regime filter** (which basket to be in), not as a directional bet on total market cap.

## How it moves price

Crypto capital rotates along a risk curve anchored by Bitcoin, the de-facto reserve asset of the asset class:

1. **BTC-led leg.** Early in a bull market and during risk-off, money concentrates in BTC and dominance rises. The 2024–2025 spot-ETF era exaggerated this: ETF inflows were BTC-only, structurally lifting dominance and starving alts.
2. **Mid-cycle large-cap rotation.** Once BTC has run, capital rotates first into ETH and large-cap alts (watch the **ETH/BTC ratio**).
3. **Late-cycle alt/meme blow-off.** Having made multiples on majors, the most speculative capital chases low-quality alts and memecoins — dominance bottoms, the **Altcoin Season Index** spikes >75, and this typically coincides with the cycle top (see [[memecoin-mania]]).
4. **Risk-off reversal.** Alts crater faster than BTC, dominance spikes back up ("flight to crypto quality"), confirming the regime flip.

The signal is the **regime**, not any single coin's level. The people on the other side of a dominance call are traders fighting the prevailing regime — buying alts that bleed vs BTC in a dominant tape, or hiding in BTC during a genuine alt-season.

> **Operational thresholds.** Altcoin Season Index **>75 = alt-season**, **<25 = Bitcoin season** (share of top-50 alts beating BTC over 90 days). BTC.D below ~55% with a falling slope is the classic rotation trigger.

## BTC dominance regime (risk-on/off rotation within crypto)

**Mechanism.** As above — dominance up = BTC concentration / risk-off; dominance down = alt rotation / risk-on.

**Directional bias:** mixed (regime indicator, not a direction on total mcap).
**Typical magnitude:** BTC.D swings 15–35 percentage points across a full cycle; alt baskets out/under-perform BTC by 50–200%+ over a rotation.
**Lag / duration:** regime-scale — weeks-to-months per leg; not an intraday signal.
**Recurrence:** every cycle (BTC-led → ETH/large-cap → alt/meme blow-off → flight back to BTC).
**Affected scope:** BTC.D, ETH/BTC ratio, large-cap alts, TOTAL2 (market cap ex-BTC).

**Leading signals:** BTC.D level + 30-day slope; Altcoin Season Index; ETH/BTC ratio and its 50/200-DMA crosses; TOTAL2/TOTAL ratio; BTC-ETF flows vs alt-fund flows; days since last alt-season.

| Date | Event | Gauge | Reading | Window | Confidence | Source |
|------|-------|-------|---------|--------|-----------|--------|
| 2021-01→05 | 2021 alt-season — DOGE/BNB/alt blow-off | BTC.D | ~73% → ~40% (−33pp) | Jan–May 2021 | medium | [coinmarketcap](https://coinmarketcap.com/charts/bitcoin-dominance/) |
| 2025-07-14 | ETF-era **BTC-led** leg; alts lagged | BTC | ATH $122,838 (Jul 14); $126,210 ATH Oct 6 2025 | 2024–2025 | high | [mexc](https://www.mexc.com/learn/article/what-is-bitcoin-all-time-high-btc-record-prices-explained/1) |
| 2026-06-03 | **Bitcoin Season** (NOT alt-season) | BTC.D / ASI | ~58.7% / ASI ~49; ~249 days since last alt-season | early Jun 2026 | high | [news.bitcoin.com](https://news.bitcoin.com/altcoin-season-index-at-49-traders-need-bitcoin-dominance-below-55-to-trigger-rotation/) |
| 2026-06-01 | Same regime — risk-off drawdown, not a rally | BTC | **−13.6%** ($73,570→$63,563; low $62,115) | Jun 1-4 2026 | high | [coingecko (measured)](https://www.coingecko.com/en/charts) |

> **Data-integrity note.** A widely-circulated June-2026 roundup claimed a "$122,800 ATH," "$118,838 spot," "$4.13T total market cap," and a "June-2026 alt-season." All four are a **stale 2025 snapshot**: the $122,838 print was 2025-07-14, the real ATH ($126,210) was 2025-10-06, and $4.13T mcap corresponds to the Oct-2025 peak. In early June 2026 BTC was actually ~$63.5k and falling, total mcap ~$2.35–2.5T, and it was **Bitcoin Season** (ASI ~49). The catalog records the verified reality.

## Alt-season extreme as a late-cycle top signal

**Mechanism.** Alt-season is the final leg of the risk curve — once majors have run, speculative capital floods low-quality alts/memecoins. The dominance *bottom* (maximum alt euphoria) historically coincides with cycle tops because risk appetite and leverage are maxed with no higher-beta buyer left. The reversal — a sharp dominance spike as alts crater faster than BTC — confirms the risk-off flip.

**Directional bias:** bearish (it marks the top).
**Typical magnitude:** post-peak alt baskets draw down 70–90%+; BTC.D rebounds 15–30pp off the bottom.
**Lag / duration:** coincident-to-leading by days/weeks; the unwind runs the ensuing bear (months-to-a-year).
**Recurrence:** once per cycle at the euphoria peak.
**Affected scope:** altcoins, memecoins, TOTAL2, BTC.D.

**Leading signals:** Altcoin Season Index spiking >75; BTC.D at a multi-month low; memecoin/low-cap volume share at extremes ([[memecoin-mania]]); ETH/BTC and alt/BTC ratios parabolic then rolling over; alt funding/leverage extremes.

| Date | Event | Gauge | Reading | Window | Confidence | Source |
|------|-------|-------|---------|--------|-----------|--------|
| 2018-01-07 | ICO-era alt-mania top | BTC.D | fell to ~33% at the cycle top | Dec 2017–Jan 2018 | medium | [statista](https://www.statista.com/statistics/1269669/bitcoin-dominance-historical-development/) |
| 2021-05-19 | Alt-season bottom → May-19 leverage crash | BTC.D / alts | dominance bottomed ~40%, rebounded; alts −50% to −70%+ | May 2021 | medium | [coinmarketcap](https://coinmarketcap.com/charts/bitcoin-dominance/) |

## Backtest features

- `btc_dominance_level`
- `btc_dominance_30d_change_pp`
- `altcoin_season_index` (>75 alt-season / <25 BTC season)
- `eth_btc_ratio` / `eth_btc_ratio_50dma_cross`
- `total2_total_ratio` (alt share of market cap)
- `days_since_last_altseason`
- `alt_basket_beta_to_btc_30d`
- `memecoin_volume_share`
- `alt_funding_rate_zscore`

**Analog mechanisms:** sector-rotation, sentiment-shock, mean-reversion.

> **Backtester takeaway:** use dominance as a *regime gate*. In a rising-dominance / Bitcoin-Season tape, fade alt strength and favour BTC; only switch to an alt-overweight when ASI confirms (>75) and BTC.D breaks down — and treat a dominance *bottom* with euphoric ASI as a cycle-top warning, not a buy signal.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-health/summary` — dual health scores + sentiment
- `GET /api/v1/market-health/altcoin-breadth` — % of coins above N-day MA (default 200)

**Historical data:**
- `GET /api/v1/market-health/history?days=730` — historical health scores

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-health]].

## Related

- [[crypto-narratives-overview]]
- [[l1-l2-rotation]] — capital rotation between specific L1/L2 platforms
- [[memecoin-mania]] — the highest-beta leg of an alt-season; top signal
- [[spot-etf-flows]] — BTC-only ETF flows that drove the 2024–2025 dominance regime
- [[technical-signals]] — the May-2021 leverage crash and cycle-top markers
- [[bitcoin]]
- [[ethereum]]
- [[altcoins]]

## Sources

- https://coinmarketcap.com/charts/bitcoin-dominance/
- https://www.coingecko.com/en/charts
- https://news.bitcoin.com/altcoin-season-index-at-49-traders-need-bitcoin-dominance-below-55-to-trigger-rotation/
- https://www.tv-hub.org/guide/bitcoin-dominance
- https://www.mexc.com/learn/article/what-is-bitcoin-all-time-high-btc-record-prices-explained/1
- https://carboncredits.com/bitcoin-breaks-records-passing-126k-the-bull-run-thats-redefining-digital-gold-and-climate-debate/
- https://www.statista.com/statistics/1269669/bitcoin-dominance-historical-development/
