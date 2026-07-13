---
title: "CME Bitcoin Futures Launch (December 2017)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [crypto, history, bitcoin, futures, derivatives, arbitrage]
aliases: ["CME BTC Futures Launch", "December 2017 BTC Top", "Bitcoin Futures Inception"]
event_date: 2017-12-18
markets_affected: [crypto, futures]
impact: high
verified: true
sources_count: 4
related: ["[[crypto-spot-perp-futures-triangle]]", "[[basis-trading]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]"]
---

# CME Bitcoin Futures Launch (December 2017)

The **Chicago Mercantile Exchange (CME)** launched cash-settled Bitcoin futures the evening of **Sunday December 17, 2017** (first trade ~18:00 ET; the official contract listing date is December 18) — one week after CBOE launched its competing XBT product on December 10. The launch coincided with — and is widely credited as the trigger for — the **$19,783 BTC peak on December 17, 2017** and the subsequent 84% drawdown. For arbitrage traders, the futures launch opened the first regulated venue for triangulating BTC spot vs futures vs perpetuals — a structural opportunity that has generated billions in basis-trade profits since.

## Background

Pre-December 2017, BTC derivatives were unregulated:
- **BitMEX perpetual swaps** (launched 2016): up to 100x leverage; offshore.
- **Bitfinex margin swaps**: 3-5x leverage.
- **OKEx / Huobi futures**: dated quarterly contracts; onshore China until late 2017.
- **Genesis Trading OTC**: institutional spot.

CME's December 17 launch added:
- Cash-settled at the **CME CF Bitcoin Reference Rate (BRR)** — a daily-anchored composite price.
- 5 BTC per contract; max 5 BTC initial margin per contract.
- Regulated US venue accessible to institutions previously barred from BitMEX.

CBOE had launched a similar product December 10, 2017 (XBT contracts) but discontinued in 2019.

## The Triangular Arb Setup

CME futures vs spot BTC vs BitMEX perpetuals created a **three-wrapper triangle** (the canonical version of [[crypto-spot-perp-futures-triangle]]):

```
Spot BTC (Coinbase, Kraken, Gemini)
  ↓ ↑
Perpetual swap (BitMEX, Bitfinex)
  ↓ ↑
CME futures (regulated, dated)
```

In an efficient market:
```
spot × (1 + funding × days/365) ≈ perp price
spot × (1 + basis × days/365) = futures price
```

In December 2017, the relationships were dramatically dislocated because:
1. **Different participant bases** — CME drew TradFi shorts; perps drew crypto-native longs; spot drew retail buyers.
2. **Funding rates on BitMEX peaked at 0.375%/8h** (≈ 410% APR) during the bubble peak — implying spot-perp dislocations of similar magnitude.
3. **CME futures traded at 8-15% premium to spot** on launch day — but quickly inverted to discount.

## The Move

| Date | BTC Spot | CME Front Month | Spread |
|------|----------|-----------------|--------|
| Dec 10, 2017 (CBOE launch) | $14,910 | $18,000 (CBOE futures open) | +20.7% |
| Dec 17, 2017 (CME launch eve) | $19,783 (ATH) | $20,650 (CME open) | +4.4% |
| Dec 22, 2017 | $14,200 | $14,750 | +3.9% |
| Jan 17, 2018 | $11,000 | $10,500 | -4.5% (backwardation) |
| Feb 2018 | $7,500 | $7,400 | -1.3% |

Spot BTC peaked at $19,783 on Dec 17 the morning CME futures launched. By Dec 22, BTC had crashed 28%; over the next 13 months it would fall to $3,200 — an 84% drawdown.

The futures launch coinciding with the top is statistically suspicious; the dominant theory is that **CME futures finally allowed institutional shorting**, draining the bubble.

## Triangular Aspects

Three windows of dramatic triangular arbitrage:

**Window 1: Launch-day premium (Dec 17-22, 2017).** CME futures at +4-8% premium to spot, BitMEX perps at +5-15% premium. Triangle:
- Short CME futures.
- Long BTC spot.
- Short BitMEX perp (collect funding).
- Net: 50-200% APR for 1-2 weeks.

**Window 2: Backwardation (January-March 2018).** As BTC fell, CME futures flipped to backwardation (-2 to -8%). Triangle:
- Long CME futures.
- Short BTC spot (via OTC borrow or BitMEX short).
- Net carry-the-decline: 30-100% APR for 6-8 weeks.

**Window 3: Funding rate divergence (continuing 2018-2020).** BitMEX funding rates often diverged from CME basis by 100-500 bp annualized, creating sustained 3-leg basis-trade alpha. This became the foundation strategy of crypto-native quant funds (Alameda, Cumberland, B2C2, Genesis Trading prop).

## Winners

**Alameda Research** — Founded November 2017, just before CME launch. Sam Bankman-Fried's team made the CME-spot-perp basis trade their flagship strategy. Reportedly $20-50M profit in 2018 just on this.

**Cumberland (DRW Trading)** — Established crypto desk; ran institutional basis trades.

**Jump Trading** — Crypto desk basis trading.

**Genesis Trading** — Genesis lent BTC to short-the-spot-side participants; basis trade infrastructure.

**MIT/Yale endowment-style allocators** — Cited as among first institutional CME futures users; some made directional bets on the bubble bursting.

## Losers

**Retail BTC longs Dec 17 - Jan 2019** — 84% drawdown over 12 months. Many lost 50-90% of capital.

**CBOE Bitcoin Futures product** — Discontinued in 2019 due to low volume; CME won the duopoly.

**BitMEX directional retail traders** — 100x leverage during the volatility cascade wiped out the typical retail account.

**Bitcoin "to the moon" narrative** — December 2017 became the cautionary tale; multi-year crypto winter ensued (2018-2020).

## Aftermath

- 2018-2020: Crypto winter; BTC -84% from peak. Basis trade alpha fell as fewer participants.
- 2020-2021: Renewed interest as Tesla, MicroStrategy bought BTC. CME open interest expanded.
- October 2021: ProShares BITO (BTC futures ETF) launched; CME OI spiked to $5B+.
- January 2024: Spot Bitcoin ETF approval (BlackRock IBIT etc.) compressed the futures-spot basis structurally.
- 2024-2026: CME futures basis remains a key indicator and arb venue, now alongside Hyperliquid perp + spot ETFs.

## Lessons for Crypto Traders

1. **First-day futures premia compress fast.** The 4-20% launch-day premium on CME/CBOE was the easiest arb of 2017.
2. **Regulated derivatives change the participant base.** Adding institutional shorts via CME drained the speculative bubble.
3. **Triangulation across regulated + offshore + spot venues is durable** — basis trades have generated 8-30% APR consistently 2018-2024.
4. **Funding rate spikes precede crashes.** BitMEX funding hit 410% APR in late 2017; same pattern in March 2021 (pre-Apr 2021 top), Nov 2021 (the cycle peak), Jan 2024 (pre-March 2024 peak), and Aug 2024 (yen-carry crash).
5. **Cash-settled futures are an arbitrageable mechanism.** CME's reference rate calculation has been gamed at expiration multiple times — the "CME gap" pattern.

## Sources

- CME Group, *Bitcoin Futures Launch Press Release* (December 17, 2017).
- CBOE, *XBT Bitcoin Futures Launch* (December 10, 2017).
- Sam Bankman-Fried, public talks 2018-2021 on Alameda's basis-trade strategy.
- *Bloomberg Crypto*, contemporaneous coverage December 2017 - January 2018.
- Tim Bittl, *Crypto Derivatives Market Structure* (2022).

## Related

[[crypto-spot-perp-futures-triangle]] · [[basis-trading]] · [[funding-rate-arbitrage]] · [[cash-and-carry]] · [[gbtc-discount-arbitrage]] · [[2013-2014-mtgox-premium-arbitrage]] · [[2017-2021-kimchi-premium]]
