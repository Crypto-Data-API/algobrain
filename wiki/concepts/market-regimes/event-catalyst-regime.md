---
title: "Event / Catalyst Regime"
type: concept
created: 2026-06-03
updated: 2026-07-13
status: good
tags: [crypto, market-regime, news, event-driven, market-microstructure]
aliases: ["Event Regime", "Catalyst Regime", "Event-Driven Crypto"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[policy-shock-regime]]", "[[security-black-swan-regime]]", "[[institutional-flow-regime]]", "[[stablecoin-depegs]]", "[[sector-rotation]]", "[[hyperliquid]]", "[[cryptodataapi]]"]
---

The **Event / Catalyst regime** is basket #5 of the fourteen-basket [[crypto-market-regime-taxonomy]] — short, high-conviction windows lasting anywhere from a few hours to a few weeks, triggered by a *discrete* event rather than a slow structural shift. Listings, token unlocks, narrative pumps, regulatory headlines, macro prints, and stablecoin depegs all fall here. Trades run in both directions, and the defining feature is that the event temporarily **overrides the [[macro-trend-regime|backdrop]]**: a strong catalyst can rip an alt 40% higher inside a flat or even bearish macro tape, then mean-revert just as fast once the window closes (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).

Because the catalyst is discrete, this regime is unusually *plannable*. Many of its triggers — unlock schedules, listing announcements, FOMC dates — are knowable in advance, so the edge is less about reaction speed and more about pre-positioning the rumor, defining the fade, and sizing for a two-way volatility spike. On [[hyperliquid]] perps the funding and [[open-interest|OI]] reads around the event give a live tell on how crowded the positioning already is.

## Sub-Regimes

Each catalyst type carries its own signal, directional bias, and posture for coin selection, leverage, holding duration, and funding tolerance (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).

### Exchange Listing (Long pre-listing)
- **Signal:** Listing rumor or confirmed announcement on a major venue; rumor-phase pre-pump building into the announcement.
- **Bias:** Long the rumor, sell the news — the framework flags a fade in the 1–3 days *after* listing.
- **What to trade:** Long the listed token (or its perp where available) on the announcement; small-to-moderate leverage given gap risk; hold only into the listing event, then flip to fade or stand aside. Tolerate elevated funding on the pre-listing long because the window is short; do not carry the position through the post-listing fade.

### Narrative / Sector Pump (Long sector)
- **Signal:** A theme — AI tokens, DePIN, RWA, GameFi — visibly trending with capital rotating in fast; social and volume momentum confirm.
- **Bias:** Long the leading sector basket.
- **What to trade:** Long the strongest 2–4 names in the hot sector rather than chasing the laggards; moderate leverage; hold days to a couple of weeks while momentum persists. High positive funding is tolerable while the narrative is fresh, but rising funding into fading volume is the exit cue.

### Sector Rotation (Long in / Short out)
- **Signal:** Capital visibly flowing between themes (e.g. DeFi → AI → Gaming); the leaving sector tops while the next one bases. See [[sector-rotation]].
- **Bias:** Short the peaked sector, long the next one.
- **What to trade:** Pair construction — short the exhausted leaders, long the emerging basket — to neutralise broad market beta. Moderate leverage on each leg; hold for the rotation leg (days to weeks); the spread funds itself if the short side pays funding.

### Protocol Event (Varies)
- **Signal:** Scheduled protocol milestone — mainnet launch, major upgrade, governance event, or unlock.
- **Bias:** Direction depends on the event: launches and upgrades tend to pump into the date, unlocks tend to dump.
- **What to trade:** Long into mainnet launches and headline upgrades (buy anticipation, often sell the activation); fade into unlock dates. Keep leverage modest around binary outcomes; hold only across the event window and tolerate funding only for the duration of the catalyst.

### Token Unlock / Vesting (Short bias)
- **Signal:** A large scheduled unlock approaching on a high-[[fully-diluted-valuation|FDV]] token, adding known future sell pressure to float.
- **Bias:** Short into the unlock.
- **What to trade:** Short high-FDV, low-float tokens with chunky cliff unlocks; moderate leverage; hold from a few days before the unlock through the absorption period. Watch funding — if the short side is already crowded (deeply negative funding), the unlock may be priced in early and the squeeze risk rises.

### Regulatory News (Both)
- **Signal:** SEC action, ETF approval or rejection, lawsuit, or a country-level ban — a headline that lands without a clean prior direction. See [[policy-shock-regime]].
- **Bias:** Both — expect a sharp two-way volatility spike, not a clean trend.
- **What to trade:** Trade the *reaction*, not the prediction: wait for the headline, fade the initial overshoot or ride the confirmed break. Keep leverage low into the print because the gap can run either way; hold short (hours to a day or two); funding is secondary to gap risk here.

### Macro Print Event (Risk on/off)
- **Signal:** Scheduled macro release — CPI, Fed decision, FOMC, jobs print — landing on the calendar. See [[crypto-macro-correlation-regime]].
- **Bias:** Risk-on / risk-off; in these windows BTC and ETH trade like Nasdaq, correlation to equities spikes.
- **What to trade:** Trade BTC/ETH directionally off the print's risk signal rather than coin-specific stories; reduce leverage going *into* the print (the gap is binary) and add after the direction confirms; hold the post-print momentum leg (hours). Funding tolerance low — these are fast windows.

### Stablecoin Depeg (Short majors)
- **Signal:** USDT, USDC, or an algorithmic stable losing peg; panic selling and a BTC volatility spike follow. See [[stablecoin-depegs]] and [[security-black-swan-regime]].
- **Bias:** Short majors into the panic.
- **What to trade:** Short BTC/ETH into the de-risking cascade; expect violent two-way swings and venue-specific dislocations. Keep size controlled despite high conviction — depeg events whipsaw on every reassurance headline. Hold only through the acute panic; funding can swing wildly, so prioritise gap and liquidation risk over carry.

## Detection Signals

Read these together; the catalyst calendar is the backbone of this basket (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]):

- **Event calendar** — listing announcements, unlock/vesting schedules, mainnet/upgrade dates, and macro print dates. Crucially, **unlocks and listings are knowable in advance** — this basket rewards maintaining a calendar rather than reacting late.
- **Narrative / social momentum** — which theme is trending; volume and social velocity flagging an active narrative pump.
- **Rumor flow** — pre-announcement chatter on listings and partnerships that drives the pre-pump leg.
- **Regulatory headlines** — SEC, ETF, and jurisdiction-level news feeds that trigger two-way spikes.
- **Funding / OI around the event** — crowded positioning into a known catalyst (extreme funding, spiking OI) signals the move may already be priced in.

## Trade Construction

The event regime is built around a binary calendar:

- **Pre-position the rumor.** For listings and narrative pumps, the edge is established *before* the event — accumulate into the anticipation, not after the headline.
- **Define the fade in advance.** Every "buy the rumor" leg needs a pre-defined "sell the news" exit. The 1–3 day post-listing fade and the post-launch activation dump are the canonical examples.
- **Size for a two-way spike.** Around binary events (regulatory, macro prints, depegs) the gap can run either way, so cut leverage going in and add only after direction confirms.
- **Asymmetry on perps.** Many of these events are best expressed with option-like convexity (capped downside, open upside). On [[hyperliquid]] perps that convexity has to be manufactured with tight stops and disciplined sizing — a wide-stop perp position into a binary print is the opposite of the desired payoff.

## Relationship to Other Regimes

The Event basket overlaps several neighbours and is best read as the "discrete trigger" layer of the taxonomy:

- **[[policy-shock-regime]]** — the regulatory and policy-event sub-states are shared; a large enough policy headline graduates from a catalyst window into a full policy-shock regime.
- **[[security-black-swan-regime]]** — depegs, exploits, and bridge hacks live on the boundary; a depeg that cascades into systemic contagion crosses into black-swan territory.
- **[[institutional-flow-regime]]** — ETF approvals and rejections are catalysts here but feed the structural institutional-flow read once flows actually arrive.
- **[[meme-speculative-regime|Narrative pump]]** — the speculative cousin: a narrative pump that detaches entirely from any underlying event becomes pure meme-speculative behaviour.

## Pitfalls

- **Holding through "sell the news."** The most common error — riding a pre-listing or pre-launch long past the event into the scheduled fade.
- **Mis-timing a macro print.** Carrying full leverage into a CPI or FOMC release and getting stopped on the binary gap before direction resolves.
- **Assuming an unlock isn't priced in.** Large unlocks can be discounted weeks early; shorting into already-crowded negative funding invites a squeeze.
- **Treating a regulatory headline as one-directional.** These produce two-way spikes; betting a single direction into the print ignores the reaction-trade nature of the event.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket regime framework defining the Event / Catalyst states, sub-regime biases, and detection signals.

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

- [[crypto-market-regime-taxonomy]]
- [[policy-shock-regime]]
- [[security-black-swan-regime]]
- [[institutional-flow-regime]]
- [[stablecoin-depegs]]
- [[sector-rotation]]
- [[hyperliquid]]
