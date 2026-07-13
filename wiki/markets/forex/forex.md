---
title: "Forex Market"
type: market
created: 2026-04-06
updated: 2026-06-17
status: good
tags: [forex, markets, currencies]
aliases: ["Forex", "Foreign Exchange", "FX", "Currency Market", "Currency", "Currencies", "Currency Trading", "FX Trading"]
related: ["[[global-macro]]", "[[interest-rates]]", "[[central-bank]]", "[[leverage]]", "[[george-soros]]", "[[black-wednesday]]", "[[cls-group]]", "[[last-look]]", "[[cross-currency-basis-swap]]", "[[us-dollar]]", "[[carry-trade]]", "[[currency-hedging]]"]
---

# Forex Market

The foreign exchange (forex or FX) market is the largest and most liquid financial market in the world. The BIS [[bank-for-international-settlements|Triennial Central Bank Survey]] put daily OTC FX turnover at roughly **$9.6 trillion in April 2025**, up about 28% from $7.5 trillion in 2022. It is the global marketplace for exchanging national currencies, operating 24 hours a day, five days a week across major financial centers in London, New York, Tokyo, and Sydney. The [[us-dollar|US dollar]] is on one side of roughly **88% of all trades**, making it the dominant vehicle and reserve currency.

## Market Structure

Forex is a decentralized over-the-counter (OTC) market with no central exchange. The interbank market (major banks trading with each other) forms the core, with pricing cascading to institutional clients, brokers, and retail traders. Key participants include [[central-banks]], commercial banks, [[hedge-funds]], corporations hedging international exposure, and retail traders. The 2025 survey data shows a continued rise in the share of trading intermediated by non-bank financial institutions and electronic platforms relative to traditional dealer banks.

Execution mechanics matter as much as price. Most FX trades settle through [[cls-group|CLS]] on a payment-versus-payment basis to neutralize [[settlement-risk|settlement (Herstatt) risk]], and dealer-quoted liquidity is often subject to [[last-look]] — a brief window in which a liquidity provider may reject a trade — whereas exchange-style venues such as [[lmax-exchange]] offer firm, no-last-look execution. The [[cross-currency-basis-swap|cross-currency basis]] embeds the true cost of funding and hedging across currencies.

## Instruments: Spot, Forward, Swap

| Instrument | What it is | Typical use | Share of turnover (2022 BIS) |
|---|---|---|---|
| **Spot** | Immediate exchange, settling [[settlement-risk|T+2]] (T+1 for USD/CAD) | Directional trades, conversions | ~28% |
| **Outright forward** | Exchange at a fixed future date and rate | Hedging future cash flows | ~15% |
| **FX swap** | Spot leg + offsetting forward leg | Rolling positions, funding, liquidity management | ~51% (largest) |
| **Options & other** | Right but not obligation to exchange | Hedging tail risk, expressing vol views | ~6% |

FX swaps — not spot — are the single largest segment, because banks and asset managers use them constantly to fund foreign-currency positions and manage short-term liquidity. Forward and swap pricing is governed by [[covered-interest-rate-parity|covered interest rate parity]].

## Currency Pairs: Majors, Minors, Exotics

| Pair | Nickname | Characteristics |
|------|------|----------------|
| EUR/USD | "Euro" / "Fiber" | Most traded pair, ~22-25% of volume, tightest spreads |
| USD/JPY | "Gopher" / "Ninja" | Safe-haven dynamics, classic [[carry-trade]] vehicle |
| GBP/USD | "Cable" | Volatile, news-sensitive |
| USD/CHF | "Swissy" | Safe-haven currency |
| AUD/USD | "Aussie" | Commodity-linked, risk-on proxy |
| USD/CAD | "Loonie" | Oil-correlated, settles T+1 |

- **Majors** — the seven most liquid pairs, all containing the [[us-dollar|USD]]. They carry the tightest spreads (EUR/USD often <1 pip) and the deepest liquidity.
- **Minors / crosses** — liquid pairs that exclude the USD (EUR/GBP, EUR/JPY, GBP/JPY). Spreads are wider; many are derived by triangulating two USD legs.
- **Exotics** — a major paired with an emerging-market currency (USD/TRY, USD/ZAR, USD/MXN, USD/SGD). Spreads can be 10-50x a major's, liquidity is thin, and many fall outside [[cls-group|CLS]] settlement, raising [[settlement-risk]].

## Pips, Lots, and Leverage

- **Pip** — the smallest standard price increment, the fourth decimal for most pairs (0.0001) and the second decimal for JPY pairs (0.01). Brokers often quote a fifth "fractional pip" (pipette).
- **Lot** — the trade unit. A **standard lot** is 100,000 units of the base currency; a **mini lot** is 10,000; a **micro lot** is 1,000. On EUR/USD a standard lot makes one pip worth ~$10; a micro lot makes it ~$0.10.
- **Leverage** — brokers offer high [[leverage]] (typically 30:1 in the EU/UK under ESMA caps, up to 50:1 in the US, and 200:1-500:1 offshore). 50:1 leverage means a 2% adverse move wipes out the position. The combination of high leverage and 24-hour trading makes [[risk-management]] discipline essential; most retail FX accounts lose money.

## Trading Sessions

The market runs continuously from Sydney's Monday open to New York's Friday close, but liquidity concentrates in regional sessions (times approximate, GMT):

| Session | Hours (GMT) | Character |
|---|---|---|
| **Sydney** | 22:00-07:00 | Thin, AUD/NZD focus |
| **Tokyo** | 00:00-09:00 | JPY pairs, Asian flows |
| **London** | 08:00-17:00 | Highest volume (~35% of global turnover), EUR/GBP focus |
| **New York** | 13:00-22:00 | USD data releases drive volatility |

The **London-New York overlap (13:00-17:00 GMT)** is the most liquid and volatile window of the day, when the two largest centers trade simultaneously.

## Who Trades It and Why

- **Central banks** — manage reserves and occasionally intervene to steer their currency (e.g., the Bank of Japan's 2022-2024 yen interventions).
- **Commercial banks & dealers** — make markets and intermediate client flow.
- **Corporates** — convert revenues and hedge import/export and balance-sheet exposure via [[currency-hedging]].
- **Asset managers & pensions** — hedge the FX risk of foreign equity and bond holdings; their persistent hedging flows are a major driver of the [[cross-currency-basis-swap|cross-currency basis]].
- **Hedge funds & CTAs** — express [[global-macro]] views, run the [[carry-trade]], and trade trend/momentum.
- **Retail traders** — speculate on margin, typically via [[metatrader|MetaTrader]] brokers.

## Key Drivers and the Carry Trade

Forex prices are driven by [[interest-rates]] differentials, [[central-bank]] policy ([[quantitative-easing]], rate decisions), economic data (GDP, employment, inflation), trade balances, and geopolitical events. The **carry trade** — borrowing in a low-yield currency (historically JPY or CHF) to invest in a high-yield one (historically AUD, NZD, or EM currencies) — is a dominant and recurring strategy. It earns the [[interest-rates|rate differential]] as long as the funding currency does not appreciate sharply, which is why carry "works for years, then loses in days" during risk-off unwinds. Its profitability reflects the empirical failure of [[uncovered-interest-rate-parity|uncovered interest rate parity]]. See [[carry-trade]].

## Why It Matters for Traders

Forex is the purest expression of [[global-macro]] trading. Currency moves affect all other asset classes -- [[stock-markets]], [[commodities]], and [[bond-market|bonds]] all respond to currency dynamics. Understanding forex is essential even for traders who never directly trade currencies. The market's history is dotted with macro landmarks such as [[george-soros|George Soros]] breaking the pound on [[black-wednesday]] (1992).

## Related

- [[us-dollar]] — on one side of ~88% of all FX trades
- [[carry-trade]] — the dominant rate-differential strategy
- [[currency-hedging]] — why and how foreign exposure is hedged
- [[covered-interest-rate-parity]] — prices FX forwards and swaps
- [[settlement-risk]] — the largest gross risk in FX
- [[cls-group]] — the PvP settlement utility
- [[global-macro]] — FX as the core macro asset class
- [[metatrader]] — the dominant retail FX platform

## Sources

- General market knowledge; no specific wiki source ingested yet.
