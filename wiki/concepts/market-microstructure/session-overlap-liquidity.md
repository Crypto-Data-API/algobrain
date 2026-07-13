---
title: "Session Overlap Liquidity (LNY Dominance)"
type: concept
created: 2026-05-16
updated: 2026-06-11
status: good
tags: [crypto, market-microstructure, liquidity, day-trading]
aliases: ["LNY Overlap", "London New York Overlap", "Session Overlap"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[crypto-trading-sessions]]", "[[crypto-weekday-weekend-etf-era]]", "[[bid-ask-spread]]", "[[adverse-selection]]", "[[liquidation]]", "[[session-overlap-momentum]]", "[[kaiko]]", "[[coinglass]]"]
---

# Session Overlap Liquidity (LNY Dominance)

A session overlap is a window of UTC time during which traders in two regional financial centers are both at their desks. In crypto, the most important overlap by a wide margin is **London–New York (LNY), roughly 13:00–16:00 UTC**. This 3-hour window concentrates the day's deepest order books, tightest spreads, and largest share of price-discovery activity, and it is the dominant execution window for any trade that requires meaningful size. See [[crypto-trading-sessions]] for the broader session framework this page sits inside.

## The LNY Overlap

Tick-level Bitcoin studies covering 2017–2021 find that trading volume, volatility, and liquidity all rise sharply during the LNY overlap, and that this window dominates intraday price discovery for BTC/USD and BTC/EUR. The intraday activity curve for these pairs is an inverted U with the peak centered on the LNY window (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

In the ETF era, the LNY overlap has become even more dominant on a flow basis. ETF authorized-participant activity, market-maker hedging via [[cme-bitcoin-futures]], and macro/data-release reactions all concentrate inside it. Roughly half of BTC volume now occurs during US sessions, with the LNY overlap doing a disproportionate share of that work (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## Other Overlaps

The other notable overlap is the **Asia–London handoff, roughly 07:00–09:00 UTC**. European desks come online while Tokyo/Singapore have not fully stepped away. This window is meaningfully thinner than LNY and shorter in duration, but it is still tighter than the late-Asia trough and often marks the day's first decisive break of the overnight range.

Sydney–Tokyo and other intra-Asia handoffs exist but have limited additional impact on liquidity for the major BTC/ETH USD pairs, as the major Asia-hours liquidity sits inside the broader Asia session rather than at its internal boundaries.

## Why Overlaps Concentrate Liquidity

The mechanism is not just "more humans awake at once." A few reinforcing structural reasons:

- **Two regional institutional bases are simultaneously staffed.** Risk officers, traders, and market-makers in both London and New York can quote, hedge, and respond to news in real time. Single-region windows have only one set of risk-takers.
- **Market-makers calibrate quoting to adverse-selection risk.** When more informed participants are live, quotes can be tightened with lower expected loss to information-asymmetric trades (see [[adverse-selection]] and [[bid-ask-spread]]). Counterintuitively, deeper participation lets spreads tighten, not widen.
- **Macro releases and ETF flows land in this window.** US CPI, FOMC decisions, NFP, and most equity-hour-bound ETF creations/redemptions hit during LNY. The window self-selects to attract the day's largest expected information events, which pulls in liquidity providers who want to be there.
- **Cross-venue arbitrage is fastest and cheapest.** Latency-arbitrage firms and cross-exchange market-makers operate at peak coverage during LNY, which tightens spreads on every connected venue.

## Trading Implications

For an intraday trader, the LNY overlap is simultaneously the best window to execute size and the most dangerous window to hold a brittle position:

**Why it is the best execution window for size:**
- Tightest spreads — round-trip cost is lower than at any other time of day
- Deepest L2 books — large clips can be absorbed without walking the book several levels
- Highest probability that a passive limit order gets filled at a reasonable price
- Lowest slippage variance — execution cost is more predictable

**Why it is the most dangerous window for fragile positions:**
- It is where the day's largest moves happen. Stop hunts, breakout traps, and macro-driven gaps cluster here.
- Liquidation cascades have the most fuel here because open interest is at session highs and leverage has had all of Asia/London hours to accumulate (see [[liquidation]]).
- Information events that move price by multiple percent in seconds are concentrated in this window.

The practical takeaway: if you need to put on or take off real size, do it in LNY. If you need to **carry** real size, the question is which thin session your position will survive the worst — and the answer is usually not LNY itself, but the late-Asia/weekend windows that follow.

A direct strategy that exploits the overlap's character is documented at [[session-overlap-momentum]].

## How to Measure

- [[kaiko]] tick and L2 data lets you build intraday spread/depth curves to verify the LNY peak empirically across venues
- [[coinglass]] open-interest and liquidation dashboards visualize how leverage builds through Asia/London and clears (or cascades) through LNY
- Order-book depth feeds (e.g., CoinDesk Data) quantify the size that books can absorb in each session

## Related

- [[crypto-trading-sessions]] — the parent session framework
- [[crypto-weekday-weekend-etf-era]] — how the LNY peak is amplified on weekdays
- [[bid-ask-spread]], [[adverse-selection]] — the microstructure mechanics behind session-varying quotes
- [[liquidation]] — cascade mechanics that interact with overlap timing
- [[session-overlap-momentum]] — strategy implementation
- [[kaiko]], [[coinglass]] — measurement infrastructure

## Sources

- [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]] — Perplexity deep-research synthesis citing intraday Bitcoin studies (2017–2021) and ETF-era Kaiko data on LNY dominance
