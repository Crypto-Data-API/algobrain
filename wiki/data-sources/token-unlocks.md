---
title: "Token Unlock Trackers"
type: source
created: 2026-05-16
updated: 2026-09-02
status: good
tags: [data-provider, crypto, altcoins, event-driven]
aliases: ["TokenUnlocks", "Token Unlock Calendar", "Vesting Calendar", "Token Unlock Trackers"]
source_type: data
source_url: "https://token.unlocks.app"
related: ["[[token-unlock-arbitrage]]", "[[token-unlocks-narrative]]", "[[crypto-trading-sessions]]", "[[session-overlap-liquidity]]", "[[crypto-weekday-weekend-etf-era]]", "[[whale-alert]]", "[[arkham-intelligence]]", "[[crypto-data-sources]]", "[[cryptodataapi]]", "[[cryptodataapi-supply]]"]
---

Token unlock trackers — most prominently **TokenUnlocks** (token.unlocks.app), plus unlock-calendar features on **CryptoRank**, **DefiLlama**, **Tokenomist**, and similar platforms — aggregate and visualize token unlock and vesting schedules across crypto projects. They surface upcoming supply events — cliffs, linear vests, ecosystem unlocks — that intraday and swing traders use to position around predictable supply pressure (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]). This page covers the unlock-calendar data category; for the broader directional/narrative impact of unlocks on price see [[token-unlocks|Token Unlocks & Vesting Cliffs (narrative)]]. Note that [[token-terminal|Token Terminal]] is a protocol-fundamentals platform, not an unlock tracker, and is covered separately.

## What It Tracks

A typical token-unlock platform aggregates project-level vesting data from public token allocation documentation, on-chain vesting contracts, and project disclosures. Key data points:

- **Cliff dates** — the moment a vesting period ends and a tranche becomes claimable (typically large, discrete supply events)
- **Linear unlock schedules** — daily/monthly drip of tokens to recipients over a vesting period
- **Recipient categories** — team, investor (seed/strategic/private), advisor, ecosystem/treasury, public sale, mining/staking emissions
- **USD-value sizing** — unlock amount multiplied by current price for a market-impact estimate
- **Calendar view** — upcoming unlocks ranked by size, date, and percentage-of-circulating-supply
- **Historical unlock impact** — some platforms add price-history overlays around past unlock events

## Why It Matters Intraday

Token unlocks are one of the few truly scheduled supply events in crypto, and their timing matters intraday:

- Many vesting contracts release at a specific UTC time, often **00:00 UTC** or aligned to a project epoch (e.g., genesis-block anniversary)
- That timing typically falls in late-Asia / early-London hours when order books are at their thinnest outside of weekend lows
- A large unlock hitting a thin book can produce outsized intraday price impact, even if the recipient does not immediately sell — because anticipatory hedging and front-running by other traders front-loads the move

The structural overlap between scheduled unlocks and thin-session timing is exactly why session-aware traders treat the unlock calendar as part of their daily prep. The same dollar-value unlock that would be absorbed inside the [[session-overlap-liquidity|LNY overlap]] can dislocate price for hours if it lands in late Asia (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## How Traders Use It

The two primary use cases:

1. **Pre-positioning around discrete unlocks** — short the token (perp or spot-borrow) ahead of a known large cliff unlock, then cover after the supply lands and gets absorbed. See [[token-unlock-arbitrage]] for the full strategy treatment
2. **Multi-week supply overhang** — read the linear unlock schedule as a tape of expected supply pressure over weeks/months; this is a structural bear bias on heavily-emitting projects independent of any single unlock event

Secondary uses:

- **Funding-rate setup** — large upcoming unlocks often coincide with rising negative funding as smart money builds shorts; can confirm a directional bias
- **OI build watch** — open interest building on a token in the days before a large unlock is a tell that the trade is becoming crowded
- **Recipient flow watching** — pair the unlock calendar with [[whale-alert]] and [[arkham-intelligence]] to see whether unlocked tokens actually hit exchange hot wallets (active selling) or move to long-term storage (held)

## Limitations

- **Schedule != actual supply** — unlocked tokens are not always sold; teams and investors may hold or stake them. The price impact often comes from the *expectation* of selling rather than the selling itself
- **Already priced in** — large, well-known unlocks (e.g., scheduled at TGE for years) may be fully discounted by the time they hit. The edge is in tokens where the unlock is under-followed or unexpectedly large relative to circulating float
- **Disclosure quality varies** — smaller or older projects may have incomplete or contradictory vesting documentation; data quality is best for major recent launches
- **OTC sales hidden** — large unlock recipients sometimes pre-sell OTC; the on-chain unlock then doesn't move price because the supply is already with new holders

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/supply/unlocks` — the dedicated cliff-calendar view: forward token-unlock cliffs sized in tokens, USD, and `pct_of_float`/`pct_of_market_cap` (free: next 7 days; Pro/Pro Plus: full 35-day horizon). This is a **cliff calendar only** — continuous emission (mining inflation, linear vesting, runs of identical daily releases) is deliberately excluded, and coverage is bounded by what DefiLlama tracks, so absence is not evidence of no unlock
- `GET /api/v1/supply/float` — circulating float and dilution overhang per coin (`float_pct`, `dilution_overhang`, `next_unlock`, `unlock_coverage`), ranked by ascending float, for sizing how exposed a token is to its own unlock schedule
- `GET /api/v1/event/calendar` — the broader forward catalyst calendar up to 30d out (filter by `type=unlock`/`macro_print`/`depeg`/`mint`, `symbol`, `bias`). `/supply/unlocks` is now the first-class view of the same unlock data that `/event/calendar?type=unlock` has always carried alongside macro prints, depegs, and stablecoin mint/burn events — not a fork, just a dedicated surface
- `GET /api/v1/event/regime/score` — event-risk composite (0-100)
- `GET /api/v1/event/regime/{symbol}` — per-symbol pending catalysts

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time snapshots for event backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/supply/unlocks?window_days=35"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]], [[cryptodataapi-supply]].

## Related

- [[cryptodataapi-supply]] — the dedicated Supply category page for `/supply/float` and `/supply/unlocks`
- [[token-unlock-arbitrage]] — full strategy treatment of trading around unlocks
- [[token-unlocks|Token Unlocks & Vesting Cliffs (narrative)]] — directional/narrative impact of unlock supply on price
- [[token-terminal]] — protocol-fundamentals platform (distinct from unlock trackers)
- [[crypto-trading-sessions]] — Asia/London/NY hub; explains why unlock timing matters
- [[session-overlap-liquidity]] — LNY overlap absorbs unlocks much better than thin sessions
- [[crypto-weekday-weekend-etf-era]] — weekend unlocks land in even thinner books
- [[whale-alert]] — real-time confirmation that unlocked tokens are moving to exchanges
- [[arkham-intelligence]] — recipient wallet attribution and behavior
- [[crypto-data-sources]] — catalog of crypto data providers

## Sources

- [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]
