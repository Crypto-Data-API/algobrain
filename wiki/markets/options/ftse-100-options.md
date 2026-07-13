---
title: "FTSE 100 Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, stocks, uk, europe]
aliases: ["FTSE 100 Options", "UKX Options"]
domain: [derivatives, options, equity-indices]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spx-options]]", "[[dax-options]]", "[[nikkei-options]]", "[[ice-futures-europe]]", "[[ftse-100]]", "[[vftse]]", "[[american-vs-european-options]]", "[[cash-vs-physical-settlement]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[options-greeks]]", "[[short-strangle]]", "[[iron-condor]]", "[[currency-hedging]]", "[[option-on-future-vs-option-on-index]]", "[[dispersion-trading]]"]
---

FTSE 100 options are **ICE Futures Europe-listed**, cash-settled, European-style [[index-options]] on the **FTSE 100 Index (UKX)** — the headline UK large-cap index of the 100 largest London-listed companies by full market cap. They carry a **£10 per index point** multiplier, are GBP-denominated, and settle to a special opening-auction value at LIFFE (the historical London International Financial Futures Exchange, now part of ICE). They are distinct from FTSE 100 **option-on-future** contracts also listed at ICE; this page covers the index option product.

## Overview

The FTSE 100 has a structurally different character from US large-caps: it is **dominated by international revenue** (around 70-75% of FTSE 100 aggregate revenue is generated outside the UK), with heavy weights in **resources** (Shell, BP, Glencore, Rio Tinto, Anglo American), **financials** (HSBC, Lloyds, Barclays, NatWest), and **consumer staples** (Unilever, Diageo, AstraZeneca, GSK). The index is therefore a stronger play on global-cyclical and EM-revenue exposure than on UK domestic conditions, and its volatility regime differs accordingly from a domestic-economy-tracking index.

UKX options on ICE Futures Europe are the standard UK equity-index volatility product, used by UK pension funds, insurance general accounts, and global macro books for GBP-denominated equity hedging and vol expression.

## Contract Mechanics

| Spec | Value |
|---|---|
| Underlying | FTSE 100 Index (UKX) |
| Multiplier | **£10 per index point** |
| Exercise style | European |
| Settlement | Cash, in GBP |
| Strike intervals | 50 index points standard; 25 / 10 near-the-money on monthlies and weeklies |
| Tick size | 0.5 index points (= £5) |
| Trading hours | ICE Futures Europe electronic trading: typically 01:00 – 21:00 UK time, with main liquidity 08:00–16:30 UK time aligning with London cash equity hours |
| Symbol | Z (ICE futures-style symbol for FTSE 100 options); commonly referred to as UKX options or FTSE 100 index options |
| Tax treatment | Jurisdiction-specific (no US Section 1256 analog for foreign-listed) |
| Listed | ICE Futures Europe (London) |

At a FTSE 100 level of 8,000, a single contract represents **£80,000 of notional** (8,000 × £10) — comparable to an [[xsp-options|XSP]] contract in US-dollar terms. The smaller per-contract size relative to SPX makes UKX options accessible at smaller institutional sizes without needing a "mini" variant.

## Index Options vs Options-on-Futures

ICE Futures Europe lists **two distinct FTSE 100 derivatives families** that traders sometimes conflate:

1. **FTSE 100 Index Options** — the product covered on this page. Underlying is the **cash FTSE 100 Index (UKX)**; settlement is to the index level via opening auction.
2. **Options on FTSE 100 Future** — options whose underlying is the **FTSE 100 future** (Z futures contract) rather than the cash index. Settlement is to the futures price; exercise produces a position in the underlying future.

The distinction matters for pricing (futures-priced options inherit cost-of-carry through the future itself) and for settlement mechanics. Most institutional UK-equity-vol activity sits in **index options (UKX)**, but futures-options are deeply liquid and used heavily by global macro books that already trade FTSE futures as their base instrument. See [[option-on-future-vs-option-on-index]].

## Settlement

FTSE 100 index options are **cash-settled in GBP** to the **Exchange Delivery Settlement Price (EDSP)**, computed from the FTSE 100 **opening auction at the London Stock Exchange** on the expiration day:

- **Expiration day**: third Friday of the expiration month for monthlies; weekly expirations on Fridays where listed.
- **EDSP calculation**: derived from the FTSE 100 opening-auction (Intraday Auction Price) on expiration Friday morning at the London Stock Exchange — typically the 08:00–08:35 UK opening auction window.
- **Trading on the expiring contract**: ceases prior to the cash-market opening auction on expiration day.

The **opening-auction-based settlement** is structurally similar to US AM-settlement on [[spx-options|SPX]] monthlies: it concentrates expiry-driven flows into the cash-equity opening auction, with the FTSE 100 EDSP published once the auction has resolved. As with SPX AM settlement, **overnight gap risk between Thursday close and Friday EDSP** is a real exposure on these products.

## Liquidity & Spreads

UKX options are liquid in front-month expirations but materially thinner than SPX or DAX:

- **Volume** — typically **20,000-50,000 contracts/day** in UKX options, concentrated in front-month and second-month.
- **Open interest** — concentrated around round-number FTSE 100 strikes (7,500 / 8,000 / 8,500) and key technical levels.
- **Bid/ask** — typically **1-3 index points wide** (£10-£30 per contract) on near-the-money front-month; wider on back-month and far-OTM strikes.
- **Strike density** — 50-point standard intervals; some 25-point and 10-point strikes near-the-money on weeklies.
- **Quote sizes** — 5-25 contracts at the inside in normal markets; meaningful size requires patience.
- **Liquidity windows** — peak during London cash-equity hours (08:00-16:30 UK); thinner during US overlap and Asian sessions.

For traders accustomed to SPX execution, UKX is meaningfully thinner — limit orders and price discovery patience are essential, especially on wings.

## Greeks & Volatility-Surface Behaviour

UKX options price under standard European Black-Scholes mechanics (cash-settled, no early exercise). Surface features specific to the FTSE 100:

- **Downside skew** — negative [[volatility-skew|skew]] (OTM puts richer than calls), driven by structural put-hedging demand from UK pensions and insurers under liability-driven-investment mandates.
- **Resource/financial sensitivity** — because the index is heavily weighted to oil majors (Shell, BP), miners (Glencore, Rio Tinto, Anglo American) and banks (HSBC, Barclays), the surface reacts to **commodity and credit shocks** more than a domestic-economy index would. An oil or metals dislocation can steepen FTSE skew while leaving a tech-heavy index relatively unmoved.
- **GBP cross-correlation** — the international-revenue translation effect (GBP weakness *boosts* FTSE in GBP terms) gives UKX vol a peculiar relationship to sterling vol; in some regimes UKX and GBP/USD are negatively correlated, which feeds into how FX-hedged books experience the vol surface.
- **[[vftse|VFTSE]]** — the FTSE 100 volatility index, the UK analog of the [[vix|VIX]], is the standard read on UKX implied-vol regime.
- **Thinner wings** — relative to SPX, far-OTM strikes are less liquid, so the *quoted* wing vols can be stale and the effective skew harder to trade at size.

### Term Structure

FTSE vol term structure is typically in **contango in calm regimes** and inverts to **backwardation in stress**, mirroring other major indices and reflecting the [[variance-risk-premium]]. UK-specific drivers create localized term-structure features around **Bank of England MPC dates**, UK fiscal events (Budget), and — historically — Brexit-process milestones, which produced unusually large event humps in 2016-2020.

## Common Spread Structures

| Structure | Construction | Typical UKX use |
|---|---|---|
| **Put spread** | Long higher-strike put, short lower-strike put | Cost-reduced downside hedge for GBP pension books |
| **[[short-strangle|Short strangle]]** | Sell OTM put + OTM call | Harvest UK [[variance-risk-premium]] in range-bound markets |
| **[[iron-condor|Iron condor]]** | Short strangle + protective wings | Defined-risk premium selling around monthly EDSP |
| **Covered call / collar** | Short call (and long put) vs long FTSE | The dominant UK pension income/overlay template |
| **Risk reversal** | Long call, short put (or reverse) | Express directional + skew view on UK large-caps |
| **Calendar spread** | Long back-month, short front-month same strike | Trade UKX term structure around BoE / Budget events |
| **Cross-region pair** | UKX vol vs SPX / DAX / SX5E vol | BoE-vs-Fed-vs-ECB divergence; commodity-cycle expression |

## Typical Strategies / Use Cases

### UK-portfolio hedging

The primary UK institutional use case. Long UKX puts hedge GBP-denominated UK equity exposure without FX mismatch. Pension funds and insurance general accounts hold the bulk of long-dated UKX put open interest as part of liability-driven and tail-risk overlay programs.

### Global-cyclical / EM-revenue expression

Because FTSE 100 revenue is heavily international and resource-sector-weighted, UKX options express views on:

- **Global commodity cycle** — Shell, BP, Glencore, Rio Tinto, Anglo American collectively are a large weight; FTSE 100 vol responds to oil and metals shocks more than SPX does.
- **EM credit and FX cycle** — HSBC and Standard Chartered carry significant Asia exposure; FTSE 100 vol responds to EM stress episodes (Asian financial crisis era, periodic China shocks).
- **GBP / sterling moves** — paradoxically, GBP weakness often *boosts* FTSE 100 in GBP terms because of the international-revenue translation effect, creating a peculiar negative correlation between GBP and UKX in some regimes.

### Cross-region pair trades

UKX-vs-SPX, UKX-vs-DAX, or UKX-vs-EURO-STOXX-50 dispersion expresses views on regional economic divergence, Brexit-era political risk, or BoE-vs-Fed-vs-ECB policy divergence. The UK's distinct macro position (independent monetary policy, post-Brexit trade arrangements) makes UKX a useful regional-divergence expression.

### Premium-selling on UK vol

UKX [[short-strangle|strangles]] and [[iron-condor|iron condors]] capture the UK [[variance-risk-premium]]. The structural VRP is comparable to US and European VRP over long windows; UK-specific risk premia can spike during Brexit-style political events.

### Income overlays for UK pension funds

The structural use case underpinning much of the UKX put open interest: covered-call programs on long FTSE 100 portfolios and put-write programs collecting premium income, both engineered to fit UK pension regulatory requirements.

## Risks / Quirks

- **Opening-auction EDSP gap risk** — overnight news between Thursday close and Friday opening auction can move EDSP materially, similar to SPX AM-settle gap.
- **Index option vs option-on-future confusion** — operationally distinct products at the same exchange; verify which underlying you are trading.
- **GBP currency exposure** — for non-GBP investors, UKX option P&L is in GBP; FX moves can offset or amplify P&L. See [[currency-hedging]].
- **Sector concentration in resources and financials** — a single oil shock or banking-sector event can move FTSE 100 disproportionately to broader UK economic conditions.
- **GBP-FTSE inverse correlation** — the international-revenue translation effect creates a sometimes-negative correlation between GBP/USD and UKX, breaking intuition imported from domestic-economy indices.
- **Lower liquidity than US or DAX options** — wider effective spreads, especially on far-OTM wings; market orders are punished.
- **Tax treatment is non-Section-1256** — US-resident traders do not get the 60/40 blend on UKX options; this is a structural after-tax disadvantage vs SPX for short-term-heavy strategies.
- **Brexit-era regime change** — the FTSE 100 traded through a discrete macro regime shift in 2016-2020 (Brexit referendum to formal departure); historical vol data pre-2016 reflects a structurally different setting.
- **Stamp duty and execution cost specifics** — UK transactional cost structures differ from US (no per-contract SEC fee, but other UK-specific costs); careful calibration needed when modeling realistic strategy P&L.

## Tax Treatment

FTSE 100 index options have **no analog to US Section 1256 treatment** for US-resident traders, and UK tax treatment depends on holder type and account structure:

- **UK retail** — capital gains tax with annual CGT exemption; spread-betting wrappers on FTSE 100 (where available via spread-betting firms, not on ICE proper) can be exempt from CGT, a structural UK advantage that drives some retail flow into spread-bet products instead of options.
- **UK institutional** — varies by entity (pension fund, insurer, regulated investment company); often taxed under specific rules favorable to qualifying long-term investors.
- **US holders** — typically taxed as ordinary capital gains/losses on a section-1234-style basis; foreign-listed index options generally do not qualify for §1256 treatment. The absence of 60/40 treatment is a meaningful after-tax disadvantage vs SPX for short-term-heavy US-resident strategies.
- **Other jurisdictions** — varied; consult local tax counsel.

## Comparison to Other Major Index Options

| Feature | **FTSE 100 (ICE)** | [[spx-options\|SPX]] | [[dax-options\|DAX (ODAX)]] | [[nikkei-options\|Nikkei 225]] |
|---|---|---|---|---|
| Index type | Cap-weighted, **price-return** | Cap-weighted, price-return | Cap-weighted, **total-return** | **Price-weighted**, price-return |
| Currency | GBP | USD | EUR | JPY |
| Multiplier | £10 / pt | $100 / pt | €5 / pt | ¥1,000 / pt |
| Exercise | European | European | European | European |
| Settlement | Cash, opening-auction EDSP | Cash, AM/PM SOQ | Cash, midday auction | Cash, SQ |
| Expiry day | 3rd Friday | 3rd Friday (+ weeklies) | 3rd Friday | **2nd Friday** |
| US §1256 60/40 | **No** | **Yes** | No | No |
| Vol index | [[vftse\|VFTSE]] | [[vix\|VIX]] | [[vdax-new\|VDAX-NEW]] | [[vnky\|VNKY]] |
| Distinctive driver | Resources/financials, **70%+ intl revenue**, GBP-inverse | Global benchmark | Autos/industrials, total-return | Yen-carry / BoJ |
| Relative liquidity | Thinner than SPX/DAX | Deepest globally | Deepest in continental Europe | Deepest in Asia |

The defining FTSE feature versus the others is the **international-revenue / GBP-inverse character**: UKX is much less a "UK economy" index than a global-cyclical and EM-revenue play with a sterling-translation overlay, which is why its vol regime can diverge sharply from domestic-economy benchmarks.

## Related

- [[index-options]] — overview of the franchise
- [[options]] — options fundamentals
- [[spx-options]] — US large-cap analog
- [[dax-options]] — German large-cap analog
- [[nikkei-options]] — Japanese large-cap analog
- [[ice-futures-europe]] — the listing exchange
- [[ftse-100]] — the underlying index
- [[vftse]] — UK VIX-equivalent
- [[option-on-future-vs-option-on-index]] — distinguishing UKX options from FTSE 100 future options
- [[american-vs-european-options]]
- [[cash-vs-physical-settlement]]
- [[implied-volatility]], [[volatility-skew]], [[options-greeks]]
- [[short-strangle]], [[iron-condor]]
- [[dispersion-trading]]
- [[currency-hedging]] — relevant for non-GBP investors

## Sources

- ICE Futures Europe FTSE 100 Index Options product specifications (theice.com — FTSE 100 index option contract spec).
- ICE Futures Europe FTSE 100 Future Options product specifications (separate product).
- FTSE Russell — FTSE 100 Index methodology and component weights.
- London Stock Exchange — opening auction methodology underpinning EDSP calculation.
