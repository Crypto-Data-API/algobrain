---
title: "Tether Banking Premium 2017-2020"
type: news
created: 2026-04-28
updated: 2026-06-12
status: good
tags: [crypto, stablecoin, depeg, history, regulation]
aliases: ["Tether Premium", "USDT Banking Crisis", "Bitfinex Premium", "Tether NYAG"]
event_date: 2018-10-15
markets_affected: [crypto]
impact: high
verified: true
sources_count: 8
related: ["[[stablecoin-pair-arbitrage]]", "[[stablecoin-depeg-profit-capture]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[depeg-risk]]", "[[tether]]", "[[bitfinex]]", "[[2023-03-usdc-svb-depeg]]", "[[stablecoin-depeg-history]]"]
---

# Tether Banking Premium 2017-2020

A multi-year period during which **USDT routinely traded at a 5-15% premium on Bitfinex** while trading at par on most other exchanges. The driver was **banking-partner instability** at Tether and Bitfinex (the two are sister entities under iFinex), which made it difficult for new USD to enter the system but easy for existing USDT to circulate. The **October 15, 2018 episode** saw USDT touch **$0.91 — a 9% depeg**. The arbitrage opportunity was vast and persistent, captured almost entirely by **specialist USD on-ramp desks** with banking infrastructure that could navigate Tether's reserves model.

## Context

Tether was launched in 2014 as a 1:1 USD-backed token. Through 2017-2020 it grew from <$10M to >$10B in circulation, while its banking partners cycled through several disruptions:

| Date | Banking partner | Event |
|------|----------------|-------|
| Late 2017 | Wells Fargo | Wells Fargo terminated correspondent banking with iFinex |
| Early 2018 | Crypto Capital Corp (Panama) | Tether/Bitfinex used Crypto Capital as shadow banking |
| April 2018 | Crypto Capital | $850M of Bitfinex/Tether funds seized in Poland and Portugal |
| 2018-2019 | Various | Multiple smaller banking relationships disrupted |
| April 2019 | NYAG investigation begins | NYAG alleges Bitfinex used Tether reserves to cover Crypto Capital loss |
| February 2021 | NYAG settlement | Tether pays $18.5M; admits commingling reserves; banned from operating in NY |

These banking disruptions did NOT stop USDT from being created or redeemed entirely — but they did create **friction in the USD redemption channel**, particularly for non-institutional users.

## The Premium Mechanism

The premium emerged from a structural asymmetry:

1. **USD into Bitfinex was hard.** Banking restrictions meant that wiring USD to Bitfinex took weeks (or failed entirely) for most participants.
2. **USDT to Bitfinex was easy.** Anyone holding USDT on another exchange could send it to Bitfinex.
3. **Bitfinex offered USD/USDT direct trading.** Users wanting to exit to USD bid up USDT on Bitfinex relative to other venues.
4. **Result: persistent 5-15% premium for USDT on Bitfinex.**

Equivalently: USDT was the only easy way to *get USD off Bitfinex* during banking issues. Holders paid up for that privilege.

## October 15, 2018 — Peak Depeg

The single sharpest episode came on October 15, 2018 when USDT briefly touched **$0.91 on multiple exchanges** including Kraken, Binance, and Huobi (NOT Bitfinex, where it traded at $1.00+).

Catalyst: rumors of a Tether banking partner failure (later confirmed: Noble Bank reported insolvency); plus NYAG investigation rumors; plus broad crypto bear market.

Recovery: USDT recovered to ~$0.96 within 24 hours and to par within 72 hours as Tether issued reassurances and demonstrated continued redemption.

**Trade tape (Oct 15-18, 2018):**
- Buy USDT at $0.93-0.95 on Kraken / Binance
- Send USDT to Bitfinex
- Sell USDT for USD at $1.00-1.02 on Bitfinex
- Wire USD out (slow, but profitable)
- Net: ~5-9% per round trip; multiple round trips per week possible for desks with infrastructure

## Who Made Money

**Specialist USD on-ramp desks** captured the bulk of the premium throughout 2017-2020:

- **Cumberland (DRW)** — institutional OTC; primary USD/USDT on-ramp
- **Genesis Trading** — similar institutional flow
- **Galaxy Digital** — Mike Novogratz's firm
- **B2C2** — UK-based market maker
- **Various Asia-Pacific OTC desks** — Hong Kong / Singapore / Tokyo banking relationships

The aggregate premium captured during 2017-2020 is estimated at **$500M-$1B+** distributed across these desks. Per-event captures during peak premium episodes (Oct 2018, multiple smaller episodes) ran to $10-50M for top desks.

**Retail mostly couldn't capture it.** The trade required:
- Banking relationships that could send USD wires to Bitfinex (rare)
- KYB / institutional accounts at Bitfinex (rare)
- Capacity to handle the multi-day settlement cycle

## Who Lost Money

- **USDT holders who panicked at $0.93** and sold at the lows (sold 5-9% below the eventually-recovered price)
- **Speculators who shorted USDT permanently** assuming Tether would collapse (Tether did not collapse; shorts paid funding for years against zero-percent reversion)
- **Derivative protocols using USDT-priced oracles** that liquidated based on the Bitfinex premium price (mispriced positions)

## NYAG Settlement (February 2021)

The New York Attorney General's investigation concluded with a settlement:

- Bitfinex/Tether paid $18.5M to NYAG
- Tether admitted that reserves had been commingled with Bitfinex's operations
- Tether agreed to publish quarterly reserve breakdowns going forward
- Tether was banned from operating in New York State

This did NOT collapse Tether — USDT continued trading at par after the settlement, and banking infrastructure stabilized through 2021-2024. However, the disclosure that reserves had been commingled validated the long-running skeptical narrative around Tether's backing.

## Why the Premium Disappeared (2020+)

Several structural changes ended the persistent banking premium:

1. **Tether banking diversified.** By 2020, Tether claimed multiple banking partners across Bahamas, Cayman, and other jurisdictions.
2. **Tether shifted to commercial paper backing.** Reserves moved from "USD in bank accounts" to "short-duration USD-equivalent securities" (later USTs), reducing banking partner dependency.
3. **USDC scaled.** Circle's USDC offered a regulated, US-bank-backed alternative; many users migrated, reducing premium pressure on USDT.
4. **Stablecoin redemption infrastructure matured.** Multiple OTC desks now offer USD-USDT redemption with T+1 settlement, removing the on-ramp scarcity.

By Q4 2020, USDT premium episodes had compressed from 5-15% to under 50bp on banking news, and the persistent premium was effectively gone.

## Lessons for Modern Stable Depeg Trading

This case study informs three principles for [[stablecoin-depeg-profit-capture]]:

1. **Redemption channel functionality is everything.** USDT didn't depeg because reserves were inadequate — it depegged because the *channel* was friction-laden. Channel-functional stables in stress are the trade; channel-broken stables are not.
2. **Banking-system structure is the underwriting story.** Diversified banking partners + redemption infrastructure (Tether 2020+) makes premium episodes structurally rare. Single-banking-partner exposure (Tether 2017-2019; USDC/SVB 2023) makes them recurring.
3. **The "obvious" trade is captured by infrastructure-haves.** Retail saw the premium and theorized about the trade; the actual extraction required banking + KYB + desk infrastructure that took 2-5 years to build. The same is true today for redemption-arb on USDC/USDT (per Method 2 in [[stablecoin-depeg-profit-capture]]).

## Sources

- New York Attorney General settlement documents (February 2021): `ag.ny.gov`
- Bloomberg coverage of Crypto Capital seizure (April 2018, multiple articles)
- The Block: Tether banking timeline (2017-2021)
- Bitfinex / iFinex public disclosures
- CoinMarketCap historical price data for USDT
- Various OTC desk public commentary (Cumberland, Genesis)

## Related

- [[stablecoin-pair-arbitrage]] — strategy hub
- [[stablecoin-depeg-profit-capture]] — Method 2 (redemption arb) draws directly on this case
- [[synthetic-stablecoin-depeg-arbitrage]] — modern synthetic equivalent
- [[depeg-risk]] — risk framework
- [[tether]] · [[bitfinex]] — entity pages
- [[2023-03-usdc-svb-depeg]] — modern parallel (banking-partner failure)
- [[stablecoin-depeg-history]] — master timeline
