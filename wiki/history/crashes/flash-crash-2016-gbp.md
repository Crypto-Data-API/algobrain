---
title: "2016 GBP Flash Crash"
type: news
created: 2026-04-13
updated: 2026-06-12
status: good
tags: [history, crashes, forex, market-microstructure]
event_date: 2016-10-07
markets_affected: [forex]
impact: high
aliases: ["GBP Flash Crash", "Sterling Flash Crash", "Pound Flash Crash 2016"]
related: ["[[flash-crashes]]", "[[flash-crash-2010]]", "[[forex]]", "[[algorithmic-trading]]", "[[liquidity]]", "[[high-frequency-trading]]", "[[currency-dynamics]]"]
---

On October 7, 2016, the British pound plunged 6.1% against the US dollar in approximately 2 minutes during early Asian trading, hitting $1.1841 — a 31-year low. It recovered most of the losses within 30 minutes. The crash demonstrated how [[algorithmic-trading]] in thin [[liquidity]] can produce extreme moves even in the world's fourth-most-traded currency.

## What Happened

### Timeline

- **~12:07 AM London time** (7:07 AM Tokyo): GBP/USD begins dropping sharply
- **12:07–12:09 AM**: GBP/USD plunges from ~$1.26 to $1.1841 — a 600+ pip move in roughly 2 minutes
- **12:09–12:40 AM**: Recovery to ~$1.24 within approximately 30 minutes
- By the London open, GBP/USD had stabilised around $1.24, still down significantly from the pre-crash level

### Key Observation

Trading volume during the crash was actually **LOW**. The move was not driven by the presence of massive selling — it was driven by the **absence of buyers**. With no bids in the order book, even moderate sell orders pushed the price through a vacuum.

## Causes

The [[bank-for-international-settlements|BIS]] published a detailed report in January 2017 identifying multiple contributing factors. No single cause was responsible; instead, several elements combined in a perfect storm.

### 1. Thin Liquidity in the Asian Session

[[forex|FX]] markets are often described as "24/7," but liquidity is highly uneven across time zones. At 12:07 AM London time, dealers in London had gone home and Tokyo market-makers were not focused on sterling. The GBP order book was extremely thin — a fraction of normal London-session depth.

### 2. Algorithmic Cascade

Initial selling — possibly triggered by news-parsing algorithms reacting to French President François Hollande's tough comments on [[brexit|Brexit]] negotiations — hit standing stop-loss orders. These triggered further [[algorithmic-trading|algorithmic]] selling in a classic cascade:

1. News algo sells → price drops
2. Stop-losses triggered → more selling
3. Momentum algos detect trend → pile on
4. No bids in the book → price falls through air

### 3. Options Gamma Hedging

Dealers who had sold GBP put options at strike prices near $1.25 were forced to [[delta-hedging|delta-hedge]] by selling GBP as the spot price dropped. This is the [[gamma]] effect: as spot approaches the strike, delta changes rapidly, requiring increasingly large hedging trades. Each hedge added to the selling pressure, pushing the price further toward (and through) the next strike level.

### 4. Fat-Finger Theory (Dismissed)

Early speculation suggested a "fat-finger" error — a trader accidentally entering an order far larger than intended. The BIS investigation found no evidence supporting this explanation.

## Fundamental Backdrop

The crash did not occur in a vacuum. The UK had voted to leave the European Union in the [[brexit|Brexit referendum]] of June 2016, and sterling had already declined from ~$1.50 pre-referendum to ~$1.26 by early October. Markets were increasingly nervous about "hard Brexit" rhetoric from the UK government, and positioning was heavily short GBP. The flash crash was an extreme expression of an existing trend, amplified by structural market factors.

## Aftermath

- The BIS report led to renewed scrutiny of [[algorithmic-trading|algorithmic trading]] in FX markets
- Several brokers reported significant client losses from stop-loss orders filled at extreme prices
- The event highlighted that even "major" currencies can experience flash-crash dynamics during off-peak hours
- Some FX platforms widened their circuit-breaker bands for major pairs

## Lessons

1. **FX liquidity is NOT 24/7** — there are dead zones between sessions where order books are dangerously thin. The Asian session handoff (London close to Tokyo focus) is a well-known gap for European currencies.

2. **Stop-losses without limit prices are extremely dangerous** — market stop-losses in thin liquidity can fill at prices far from the trigger level. A stop at $1.25 might fill at $1.19. See [[stop-hunting-and-liquidity-sweeps]].

3. **Options gamma effects amplify moves** — the forced hedging by options dealers created a feedback loop that accelerated the decline. Understanding [[gamma]] exposure in the market is critical for anticipating potential cascade events.

4. **Absence of buyers matters more than presence of sellers** — the crash was not about massive selling pressure; it was about there being nobody on the other side. [[liquidity|Liquidity]] is not just about volume — it is about the depth and resilience of the order book.

5. **Algorithmic trading creates correlated behavior** — when many algos use similar signals (stop-loss triggers, momentum, news parsing), they can all act in the same direction simultaneously, overwhelming available liquidity.

## Related

- [[flash-crashes]] — overview of flash crash events
- [[flash-crash-2010]] — the original equity flash crash
- [[forex]] — foreign exchange markets
- [[algorithmic-trading]] — role of algorithms in modern markets
- [[liquidity]] — market liquidity concepts
- [[high-frequency-trading]] — HFT and market microstructure
- [[currency-dynamics]] — how currencies move
- [[stop-hunting-and-liquidity-sweeps]] — predatory liquidity dynamics
- [[brexit]] — the fundamental driver behind GBP weakness
- [[flash-crash-2019-yen]] — the analogous Asian-session JPY flash crash (January 2019)

## Sources

- Bank for International Settlements, *The sterling 'flash event' of 7 October 2016* (Markets Committee report, January 2017) — the definitive multi-factor analysis; ruled out a single "fat-finger" cause and identified thin Asian-session liquidity, automated execution, stop-loss and options-hedging flows as compounding factors.
- *Financial Times* and *Reuters* coverage, 7 October 2016 — intraday timeline; GBP/USD low of ~$1.1841, a 31-year low at the time, with recovery within ~30 minutes.
