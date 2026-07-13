---
title: "AM vs PM Settlement"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [options, derivatives, market-microstructure]
aliases: ["AM Settlement", "PM Settlement", "AM/PM Settlement", "SOQ Settlement"]
domain: [derivatives, options, market-microstructure]
difficulty: intermediate
related: ["[[spx-options]]", "[[xsp-options]]", "[[vix]]", "[[weekly-options]]", "[[0dte-trading]]", "[[cash-vs-physical-settlement]]", "[[pin-risk]]", "[[options-portfolio-construction]]"]
---

**AM and PM settlement** describe the two methods by which the final value of a cash-settled index option is determined at expiration. **AM-settled** options reference a **Special Opening Quotation (SOQ)** computed from the opening prices of the underlying index components on expiration day. **PM-settled** options reference the **closing print** of the underlying index at the end of expiration day (typically 4:00pm ET for US indices). The distinction sounds technical but creates real overnight gap risk for any position that straddles both styles — most notably calendar and diagonal spreads on SPX, which is AM-settled for monthlies and PM-settled for weeklies.

## Overview

Cash-settled index options must specify *what value* the contract settles to. There are two industry-standard approaches:

| Style | When fixed | What it references |
|---|---|---|
| **AM settlement** | Expiration day morning open | SOQ — calculated from opening prints of index components |
| **PM settlement** | Expiration day 4:00pm ET close | Official closing index value |

For [[spx-options|SPX]] specifically:

- **Traditional monthly SPX (3rd Friday)** → **AM-settled**.
- **SPXW weeklies (Mon/Tue/Wed/Thu/Fri including 0DTE)** → **PM-settled**.
- **[[xsp-options|XSP]] (all expirations)** → **PM-settled**.
- **[[vix|VIX]] options** → **AM-settled** (Wednesday expirations).

Most US equity options (including [[spy-options|SPY]]) use a different mechanism entirely — physical settlement based on the closing price — so AM/PM settlement is primarily an index-options concept.

## AM Settlement Mechanics (SOQ Calculation)

The Special Opening Quotation is the value used for AM-settled options. Mechanics:

1. **Final trading session** — for monthly SPX, regular trading in the option ends Thursday afternoon (the day before expiration Friday). The contract is dead from the close Thursday until the SOQ prints Friday morning.
2. **Component openings** — Friday morning, each of the 500 underlying S&P 500 stocks opens at its primary listing exchange (mostly NYSE and Nasdaq). Opens are staggered: large caps usually open within minutes of 9:30am, but smaller-cap components can take longer, especially on volatile days.
3. **SOQ computation** — once all 500 components have an opening print (or pre-determined fallback for any that fail to open), the SOQ is calculated using the official S&P 500 index methodology applied to those opening prices. The SOQ is published shortly after all opens are received.
4. **Settlement** — every AM-settled SPX contract is then cash-settled to the SOQ value.

Because the SOQ depends on hundreds of separately-staggered opens, **it can differ materially from Thursday's closing index print**, particularly during:

- Overnight news events (Fed surprises, geopolitical shocks).
- Single-stock gaps on large-weight components.
- Trading halts or LULD (limit up / limit down) bands on individual components delaying their open.

This is the core source of "phantom" gap risk in AM-settled positions.

## PM Settlement Mechanics

For PM-settled options:

1. **Final trading occurs on expiration day** — SPXW weeklies trade until 4:00pm ET on their expiration date.
2. **Settlement value = official closing index print** — the regular published index level at 4:00pm ET, computed from each component's official close.
3. **No overnight risk** — the contract is fully resolved by the end of the trading day; no surprise SOQ to wait for.

PM settlement is operationally simpler and has displaced AM settlement as the modern default for most new products. Only legacy monthly index options on SPX and a handful of others still use AM.

## Why the Difference Matters

For most positions held to expiration, AM vs PM is just a settlement-time convention. The risk concentrates in a few specific scenarios:

**1. Calendar / diagonal spreads that mix AM and PM legs.** Example: a trader sells the 3rd-Friday monthly SPX (AM-settled) and buys the SPXW weekly the same Friday (PM-settled). The two legs settle to different reference values 6.5 hours apart, exposing the position to whatever the index does between Thursday close and Friday SOQ, plus everything between SOQ and 4:00pm.

**2. Holding an AM-settled position into Thursday's close.** Once Thursday's close passes, a trader has no further opportunity to adjust before the SOQ prints. Overnight moves are uncontrollable.

**3. Stress events around AM expiration.** Historical incidents (most notably various VIX-related controversies) have highlighted that the SOQ can be moved by aggressive trading at the open in component stocks, particularly for smaller-cap or thinly-traded components that disproportionately affect calculated values.

## Settlement Risk (Case Studies)

**VIX SOQ controversy (2018 onward).** Academic research and trading-firm analyses (e.g., the 2017 paper by Griffin & Shams "Manipulation in the VIX?") documented unusual volume in SPX options at the open on VIX-expiration mornings, consistent with attempts to influence the SOQ used in VIX option settlement. The episode prompted SEC review and ongoing scrutiny of AM-settle mechanics. Whether the activity was manipulation or legitimate hedging remains contested, but the structural vulnerability — that a small number of trades at the open can move a settlement value used by millions of contracts — is real.

**SPX AM-settle gap (multiple instances).** During major overnight news events (e.g., Brexit, US election surprises, Fed announcements), the SOQ has printed several percent away from Thursday's close, causing AM-settled monthly SPX positions to settle at very different values from where the trader had last marked them.

**Industry response.** The shift toward PM-settled SPXW for weeklies and 0DTE was, in part, a deliberate choice to remove this risk for the products that have grown the most in the post-2010 period.

## Choosing Between Them

In practice, traders rarely "choose" — the product and expiration determine the settlement style. But the implications shape strategy:

- **Avoid mixing AM and PM legs** in a single spread unless the gap risk is the explicit trade.
- **Plan rolls around AM expiration** — close or roll AM-settled positions Thursday afternoon if you want to control the exit price; once the bell rings, you are at the SOQ's mercy.
- **Use SPXW (PM-settled) for tactical work** — same-day or very short-dated trades benefit from PM settlement's predictability.
- **Treat VIX and other AM-settled products with extra caution** — accept that the settlement value is a derived calculation, not a market-traded print.

## Related

- [[spx-options]] — both AM (monthly) and PM (SPXW) variants
- [[xsp-options]] — PM-settled
- [[vix]] — AM-settled
- [[weekly-options]] — generally PM-settled
- [[0dte-trading]] — always PM-settled on SPX
- [[cash-vs-physical-settlement]] — broader settlement-type comparison
- [[pin-risk]] — related expiration risk
- [[options-portfolio-construction]]

## Sources

- Cboe Special Opening Quotation methodology documentation
- Griffin, J. & Shams, A. (2017), "Manipulation in the VIX?" Review of Financial Studies
- SEC and Cboe statements on VIX settlement procedures
- OCC settlement rules
