---
title: Crypto Perpetual Futures
type: concept
created: 2026-06-24
updated: 2026-06-24
status: good
tags: [market-microstructure, derivatives, crypto, leverage, funding-rate]
aliases: [crypto-perpetuals, perpetual-swaps, perps, crypto-perps, perpetual-swap]
domain: [market-microstructure]
prerequisites: ["[[perpetual-futures]]", "[[funding-rate]]", "[[leverage]]"]
difficulty: intermediate
related:
  - "[[perpetual-futures]]"
  - "[[funding-rate]]"
  - "[[funding-rate-arbitrage]]"
  - "[[delta-neutral]]"
  - "[[mark-price]]"
  - "[[maintenance-margin]]"
  - "[[cross-margin-vs-isolated-margin]]"
  - "[[liquidation-cascade]]"
  - "[[hyperliquid]]"
  - "[[spot-price]]"
---

# Crypto Perpetual Futures

Crypto perpetual futures (perpetual swaps, or "perps") are leveraged derivative contracts that track an underlying crypto asset but, unlike traditional dated futures, never expire. A periodic [[funding-rate]] payment between longs and shorts keeps the contract price tethered near the [[spot-price]], replacing the convergence-at-expiry mechanism of ordinary futures. They are cash-settled, trade 24/7, and commonly offer high [[leverage]].

## Contrast With TradFi Dated Futures

A traditional futures contract has a fixed expiry date; arbitrage forces its price to converge to spot as expiry approaches, and the holder must roll into a later contract to maintain exposure. A perpetual has no expiry and therefore no scheduled convergence. Instead, the [[funding-rate]] is exchanged periodically (commonly several times per day) so that whenever the perp trades above spot, longs pay shorts (incentivizing the price down) and whenever it trades below, shorts pay longs (incentivizing it up). This continuous, market-driven tether is the defining feature that lets the contract live forever. See the general [[perpetual-futures]] page for the broader concept and its origins.

## Key Characteristics

- **No expiry / no roll** — continuous exposure without rolling contracts.
- **Funding-anchored** — the [[funding-rate]] pulls the contract toward spot; the basis is reflected in the [[mark-price]].
- **Cash-settled** — settled in a quote currency or stablecoin, not by physical delivery of the underlying coin.
- **24/7 markets** — crypto trades continuously, so funding and liquidation engines run around the clock.
- **High leverage** — venues often allow large multiples, which makes [[maintenance-margin]] and [[liquidation]] mechanics central to survival.
- **Margin modes** — positions can run under cross or isolated collateral; see [[cross-margin-vs-isolated-margin]].

## Worked Illustrative Example

Suppose the [[spot-price]] of an asset is 100 and demand for leveraged longs pushes the perp to 100.5 — a premium. Funding is therefore positive, so longs pay shorts a small periodic fee proportional to the premium. That cost nudges longs to trim and shorts to add, pulling the perp back toward 100. A [[delta-neutral]] trader who is long spot and short the perp collects this funding while carrying little price risk — the basis of [[funding-rate-arbitrage]]. (Premium and funding magnitudes are illustrative and vary by venue and market conditions.)

## How Traders Use Them / Why They Matter

- **Leveraged directional bets** — efficient long or short exposure without holding the underlying.
- **Hedging** — shorting a perp against a spot bag to neutralize price risk.
- **Funding capture** — [[funding-rate-arbitrage]] and [[delta-neutral]] carry trades harvest persistent funding.
- **Price discovery** — deep perp order books (on venues such as [[hyperliquid]] and major centralized exchanges) often lead spot, so perp funding and [[open-interest]] are watched as sentiment gauges.

## Risks and Pitfalls

- **Funding drag** — a position held against persistent funding bleeds equity even if price is flat.
- **Liquidation at mark** — high leverage plus the [[mark-price]] trigger means small adverse moves can liquidate; crowded leverage feeds [[liquidation-cascade]] dynamics.
- **Basis blowouts** — in stress, the perp can dislocate sharply from spot, spiking funding and the basis.
- **Venue and oracle risk** — index construction can be attacked ([[oracle-manipulation]]) and venues differ in engine behavior, insurance funds, and auto-deleveraging.

## Related

- [[perpetual-futures]]
- [[funding-rate]]
- [[funding-rate-arbitrage]]
- [[delta-neutral]]
- [[mark-price]]
- [[maintenance-margin]]
- [[cross-margin-vs-isolated-margin]]
- [[liquidation-cascade]]
- [[hyperliquid]]
- [[open-interest]]
- [[spot-price]]
- [[leverage]]

## Sources

General market knowledge; no specific wiki source ingested yet.
