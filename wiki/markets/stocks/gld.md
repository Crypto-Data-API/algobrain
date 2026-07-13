---
title: "GLD (SPDR Gold Shares)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [stocks, gold, commodities, etf, options, derivatives]
aliases: ["GLD ETF", "SPDR Gold Trust", "SPDR Gold Shares"]
related: ["[[gold]]", "[[spy]]", "[[options-concentration-risk]]", "[[us-dollar]]", "[[tlt]]", "[[commodities]]"]
---

GLD is the SPDR Gold Shares ETF, issued by State Street Global Advisors and sponsored by the World Gold Council. It is the largest physically backed gold ETF in the world, holding allocated gold bullion in vaults (primarily HSBC London) on behalf of shareholders. Each GLD share represents a fractional ownership of approximately 1/10th of an ounce of physical gold (the ratio declines slowly over time due to the expense ratio). GLD is the standard listed instrument for gold exposure and the foundation of the most liquid gold options market.

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | GLD |
| **Underlying** | Physical gold bullion (allocated, vaulted) |
| **Issuer** | State Street (sponsor: World Gold Council) |
| **Structure** | Grantor trust |
| **Inception** | November 18, 2004 |
| **Expense ratio** | 0.40% |
| **AUM** | approximately $80-100B (as of early 2026, near record highs given 2024-2025 gold rally) |
| **Avg daily volume** | approx 8-12M shares/day |
| **Options liquidity** | Deep — most liquid gold options market |
| **Dividend** | None (gold pays no income) |

## How GLD Tracks Gold

GLD is a grantor trust that holds physical gold. Each share represents a specified weight of gold, which is reduced gradually by the expense ratio (gold is sold to cover trust expenses). The share-to-ounce ratio started at 1/10 oz in 2004 and is now approximately 1/11 oz as of early 2026. Tracking error to spot gold is minimal — GLD trades within pennies of NAV during US trading hours.

For traders who want pure gold exposure without futures roll costs, GLD is the cleanest listed vehicle. Alternatives include IAU (iShares, lower expense ratio at 0.25%, less options liquidity), GLDM (SPDR mini, lowest cost, no options), and gold futures (GC).

## What Physically Backs GLD

GLD is a **grantor trust** whose sole asset is **allocated** physical gold bullion — specific, serial-numbered London Good Delivery bars (each ~400 troy oz, ≥99.5% purity) held in the trust's name, not a pooled or unallocated claim. The structure is the critical detail for understanding what shareholders actually own:

- **Allocated vs unallocated.** Allocated means the bars belong to the trust and are segregated; the trust is not an unsecured creditor of a bank's bullion pool. This is what makes GLD a *physical* gold holding rather than a paper claim.
- **Custodian and vaults.** The bullion is vaulted primarily in London (HSBC as custodian per the trust documentation). A bar list is published, and the gold is subject to periodic physical inspection/audit by an independent party.
- **Creation/redemption in kind.** Authorized Participants create and redeem GLD shares in large blocks (baskets) by delivering or receiving physical gold, which is the arbitrage mechanism that keeps GLD pinned to NAV and to spot.
- **Pricing benchmark.** NAV references the [[lbma-gold-price|LBMA Gold Price]] benchmark methodology, the global standard for gold settlement.
- **No income, gradual erosion.** Gold generates no cash flow, so there is no dividend; instead the trust periodically **sells a sliver of gold to pay the 0.40% expense ratio**, which is why the gold-per-share ratio declines slowly over time (the 1/10 → ~1/11 oz drift noted above).
- **Tax note (US).** GLD is taxed as a **collectible** for US investors — long-term gains are taxed at a higher maximum rate than equities — a structural consideration for taxable holders versus, say, gold-miner equities.

## What Drives the Gold Price (and thus GLD)

Gold is a non-yielding, dollar-denominated monetary metal, so its price is driven by the *opportunity cost of holding it* and by *demand for a monetary safe haven*:

| Driver | Mechanism | Direction |
|--------|-----------|-----------|
| **Real interest rates** | Gold pays no yield, so high real (inflation-adjusted) yields raise its opportunity cost | Rising real rates → gold down |
| **US dollar ([[us-dollar\|DXY]])** | Gold is priced in dollars; a strong dollar makes it more expensive for non-USD buyers | Strong dollar → gold down |
| **Inflation / inflation expectations** | Gold is a long-run store of value and inflation hedge | Higher expected inflation → gold up |
| **Central-bank buying** | Reserve diversification (China, India, Russia, Turkey) is structural demand | More buying → gold up |
| **Geopolitical / tail risk** | Safe-haven and crisis-hedge demand | Risk-off shocks → gold up |
| **ETF & investment flows** | GLD creations/redemptions reflect Western investor positioning | Inflows → gold up |

The single most important framework is **gold as the reciprocal of real rates and the dollar**: the long-running negative correlations to DXY and to real yields (detailed in Key Relationships below) are the backbone of most gold trading theses.

## Options on GLD

GLD hosts the deepest gold options market accessible to retail:

- **Monthly and weekly expirations**
- **Strike granularity** — $1 increments near ATM
- **American-style**, physical settlement (delivery of GLD shares)
- **IV regime** — typically 12-18% annualized in calm periods, spiking to 25%+ during macro shocks (March 2020, Oct 2023 Israel-Hamas, 2024 Middle East tensions)
- **Skew** — modest call skew at times, reflecting gold's tendency to rally on tail events

Gold options have a distinct vol surface profile from equities: less consistent put skew (since gold is often a tail-event hedge, calls can be priced rich during stress), and IV that responds to different macro inputs (real rates, dollar, geopolitical risk) than equity IV.

## Trading Uses

- **Inflation hedge** — long GLD when expecting persistent inflation or negative real rates
- **Tail risk hedge** — gold tends to rally during geopolitical shocks and currency crises
- **Anti-dollar** — long GLD / short [[uup|UUP]] expresses a weak-dollar view
- **Anti-equity tail hedge** — long GLD as portfolio insurance against equity drawdowns; correlation to [[spy|SPY]] is roughly zero on average but turns negative during stress
- **Vol overlay** — short GLD strangles or condors during calm regimes harvest a different vol regime than equity options
- **Gold/silver ratio** — long GLD / short SLV (or vice versa) expresses views on the gold-silver ratio

## Peer & Related-Instrument Comparison

### Gold ETFs (physical)

| Vehicle | Issuer | Expense | Options | Notes |
|---------|--------|---------|---------|-------|
| **GLD** | State Street | 0.40% | Deepest | The benchmark; most liquid gold options market |
| **IAU** | iShares | 0.25% | Some | Cheaper to hold; thinner options |
| **GLDM** | State Street | lowest | None | "Mini" buy-and-hold vehicle; no options |
| **GC futures** | CME | roll cost | Deep | Leverage + 24h; incurs contango/backwardation roll |

GLD wins on **options liquidity and tradability**; IAU/GLDM win on **holding cost** for long-term investors. Futures suit leveraged or round-the-clock traders willing to manage roll.

### GLD vs gold miners (GDX/GDXJ)

Gold *miners* are **not** the same trade as gold *bullion*:

- **Operating leverage.** Miner profits are leveraged to the gold price minus a largely fixed cost of production, so [[gdx|GDX]] (senior miners) and GDXJ (juniors) typically have **higher beta** to gold than GLD — they amplify gold moves in both directions.
- **Equity risk overlay.** Miners carry company- and country-specific risk (cost inflation, mine accidents, jurisdiction/political risk, management, dilution) and correlate partly with the broad equity market, so they can *fall with stocks even when gold is firm*.
- **Income.** Some miners pay dividends; bullion (GLD) never does.
- **Use case.** GLD is the clean macro expression of the gold price; GDX is a higher-beta, equity-flavored bet that also lives inside [[xlb|materials]]. The **GDX/GLD ratio** is watched as a risk-appetite-within-gold gauge.

### GLD vs oil/energy commodity funds (USO-style)

Gold and oil are both commodities but trade on **opposite logic**, which is why GLD pairs well against an oil fund for diversification:

- **Structure.** GLD holds *allocated physical metal* with **no roll cost**; [[uso|USO]]-style funds hold *futures* and suffer **contango/roll decay** (and benefit from backwardation), so USO is a poor long-term proxy for spot oil while GLD tracks spot gold tightly.
- **Drivers.** Gold is a *monetary* metal driven by real rates, the dollar, and safe-haven demand; oil is a *consumption* commodity driven by global growth, OPEC supply, and inventories. Gold often rallies in risk-off; oil usually falls.
- **Storage economics.** Gold is cheap and easy to store (hence physical backing works); oil is bulky and costly to store (hence futures-based funds and roll problems).

## Seasonality

Gold has historically shown some mild seasonal tendencies driven by **physical-demand calendars**: a late-year/early-year firmness associated with Indian wedding-season and festival buying (Diwali, Akshaya Tritiya) and Chinese Lunar New Year demand, plus a "January effect" of fresh investment allocations. These patterns are *weak and unreliable* relative to the dominant macro drivers (real rates, dollar, central-bank flows); in any given year a Fed pivot or geopolitical shock will overwhelm any seasonal tilt. Treat gold seasonality as background color, not a tradable edge. See [[seasonality]].

## Concentration Risk Angle

[[options-concentration-risk]] specifically calls out commodity vol as a key diversifier for short premium books concentrated in equity vol. GLD is the most liquid commodity options vehicle and the natural starting point for diversifying outside equity:

- GLD IV is driven by real rates, dollar dynamics, central bank gold buying, and geopolitical risk
- SPY IV is driven by earnings, growth expectations, and risk appetite
- The realized correlation between GLD vol regime and SPY vol regime is modestly positive (both can spike on macro stress) but well below 1

A trader running short premium on SPY, QQQ, and [[xlk]] who adds GLD short premium has genuinely diversified across vol regimes. During the August 2024 yen-carry unwind, equity vol spiked while gold IV barely moved — a classic example of the diversification working as intended.

GLD short premium typically harvests 2-3 vol points of [[volatility-risk-premium|VRP]], smaller than equity index VRP but with much lower correlation to other premium-selling P&L.

## Key Relationships

- **GLD vs DXY (dollar)**: persistent negative correlation (-0.4 to -0.6); a strong dollar pressures gold
- **GLD vs real rates**: persistent negative correlation; rising real yields make gold (which pays no yield) less attractive
- **GLD vs SPY**: roughly zero correlation in normal regimes; turns negative during equity stress (gold as safe-haven)
- **GLD vs TLT**: weakly positive correlation; both benefit from falling real rates
- **GLD vs central bank gold buying**: structurally bullish since 2022 as global central banks (China, India, Russia, Turkey) accumulated record amounts

## Risks

- **Real-rate / dollar reversal** — the biggest macro risk: a regime of high positive real yields and a strong dollar is structurally bearish for non-yielding gold.
- **No income, costly to hold** — gold pays nothing and the 0.40% expense ratio slowly erodes the gold-per-share ratio; the opportunity cost is real if other assets compound.
- **Crowded-positioning unwind** — after a large rally, heavy ETF and speculative long positioning can reverse sharply on a hawkish surprise.
- **Tax treatment (US)** — taxed as a collectible, a higher long-term capital-gains rate than equities for taxable holders.
- **Not a constant equity hedge** — GLD's negative correlation to [[spy|SPY]] only reliably appears in *stress*; in calm regimes correlation hovers near zero, so it is an imperfect, regime-dependent hedge.
- **Structural risks (low probability)** — custodian/counterparty and operational risk at the vault, and the collectible-tax and grantor-trust mechanics, though the allocated-bullion structure mitigates most credit risk.
- **Sentiment-driven swings** — gold can stay detached from fundamentals for long stretches on flow and narrative, both up and down.

## Sources

- State Street SPDR Gold Shares official trust documentation
- World Gold Council market intelligence reports
- LBMA gold price benchmark methodology

## Related

- [[gold]] — underlying asset
- [[us-dollar]] — primary inverse driver of gold
- [[options-concentration-risk]] — GLD as the commodity-vol diversifier
- [[spy]] — equity counterpart; long GLD / short SPY for stress hedging
- [[tlt]] — fellow real-rates-sensitive instrument
- [[uup]] — dollar ETF; structural inverse of GLD
- [[uso]] — oil ETF; alternative commodity vol vehicle; opposite commodity logic
- [[gdx]] — gold-miner ETF; higher-beta, equity-flavored gold play
- [[gold]] — underlying asset and price-driver framework
- [[commodities]] — broader asset class
- [[lbma-gold-price]] — settlement benchmark referenced by NAV
- [[volatility-risk-premium]] — VRP harvested by GLD short premium
- [[xlb]] — materials SPDR; embeds gold miners
- [[seasonality]] — physical-demand calendar context
