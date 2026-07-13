---
title: "Stablecoin Depeg History"
type: overview
created: 2026-04-28
updated: 2026-06-21
status: excellent
tags: [crypto, stablecoin, depeg, history, defi, banking, regulation, contagion]
aliases: ["Stable Depeg Timeline", "Historical Stablecoin Depegs", "Depeg Master Timeline"]
related: ["[[stablecoin-pair-arbitrage]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[stablecoin-depeg-profit-capture]]", "[[lst-depeg-arbitrage]]", "[[depeg-risk]]", "[[defi-hacks-and-exploits]]", "[[history-overview]]"]
---

# Stablecoin Depeg History

Master timeline of all major stablecoin depeg events from **2014 to present**, categorized by trigger type. Cross-linked to dedicated case study pages where they exist; remaining events documented inline. Companion to [[defi-hacks-and-exploits]] (master hack timeline) and the strategy pages [[stablecoin-pair-arbitrage]] / [[synthetic-stablecoin-depeg-arbitrage]] / [[stablecoin-depeg-profit-capture]].

**Total documented events: 18 across 6 categories.** Event frequency has averaged 2-5 major events per year since 2018; the rate is roughly stable with composition shifting from banking-driven (2017-2020) toward mechanism-driven and contagion-driven (2022-present).

> **Data caveat.** Depeg "lows" are sensitive to the venue and timeframe measured — a thin-liquidity print on one DEX pool can show a deeper low than the volume-weighted market. Figures below are drawn from the cited per-event case-study pages and aggregated price sources; treat single-venue extremes as indicative. Dates are the widely reported event dates. Where a figure is uncited inline, it is preserved from the existing case-study pages, not newly asserted.

## Why Stablecoins Depeg: Design Taxonomy

A stablecoin's depeg risk is largely determined by **how it keeps its peg**. The four dominant designs map directly onto the trigger categories below:

| Design | Peg mechanism | Primary failure mode | Examples |
|--------|---------------|----------------------|----------|
| **Fiat-backed (custodial)** | 1:1 reserves at banks / in Treasuries; redemption at par | Banking-partner failure; reserve doubt; redemption-channel friction | [[usdc\|USDC]], USDT, BUSD, FDUSD |
| **Crypto-overcollateralized** | Over-collateralized [[smart-contracts\|smart-contract]] vaults + liquidation auctions; often a PSM | Liquidation/auction failure (above-peg); collateral contagion | [[dai\|DAI]]/[[usds\|USDS]] (see [[makerdao]]), GHO, crvUSD |
| **Algorithmic (uncollateralized / reflexive)** | Mint/burn a volatile sister token to defend the peg | Reflexive death spiral — irrecoverable | [[terra-luna\|UST]], TITAN, USDN, USDR |
| **Yield-bearing / synthetic** | Delta-neutral or basis positions, or LST/LRT wrappers | Funding inversion, exit-queue depth, sympathy contagion | sUSDe/USDe, stETH/LRTs, sUSD |

The single most important historical lesson is the line between **collateralized** and **algorithmic**: collateralized stables have recovered from every major stress to date (DAI, USDC), while pure-algorithmic stables that broke (UST, TITAN, USDN, USDR) **never recovered**. This is why the [[depeg-risk]] framework treats backing type as the first-order risk variable.

## Master Timeline

| Date | Stable | Depeg low | Recovery | Trigger | Trade outcome | Page |
|------|--------|-----------|----------|---------|---------------|------|
| 2014-2018 | USDT | varies (5-15% premium episodes) | Multi-month | Banking partner instability | Long arb captured by USD on-ramp desks | [[2017-2020-tether-banking-premium]] |
| **Oct 15, 2018** | USDT | **$0.91** (-9%) | 3 days | Noble Bank insolvency rumors | Buy-the-depeg arb worked | [[2017-2020-tether-banking-premium]] |
| **Mar 12, 2020** | DAI | **$1.10 (ABOVE peg)** | ~3 weeks | Auction mechanism failure (Black Thursday) | Short DAI above peg via Compound borrow | [[2020-03-dai-black-thursday]] |
| Apr 2021 | Fei Protocol | $0.70 (FEI) | Days-weeks | Algorithmic mechanism stress at launch | Some recovery; peg never robustly held | — |
| Jun 2021 | TITAN (Iron Finance) | $0.00 (collapse) | Never | Algorithmic death spiral | NOT an arb — total loss | — |
| Jan 2022 | UST (Terra) | $0.998-1.001 ranges | n/a | Pre-collapse stress | Death spiral incubating | — |
| Apr 2022 | USDN (Waves) | $0.20 | Permanent | Algorithmic death spiral | NOT an arb | — |
| **May 2022** | **UST (Terra)** | **$0.00 (collapse)** | Never | Algorithmic death spiral | NOT an arb — death spiral; -$40B+ ecosystem loss | [[2022-05-terra-luna-depeg-arb]] |
| **Jun 2022** | stETH | **0.9346 ETH** | Weeks | 3AC/Celsius forced selling; Lido withdrawal queue | Long stETH at 0.94 if confident in Lido; recovered to par | [[2022-06-steth-depeg]] |
| Aug 2022 | USDC (briefly) | $0.998-1.002 | Hours | Tornado Cash sanctions; Circle freezes addresses | No tradable depeg; sentiment event only | — |
| **Feb 2023** | BUSD | $0.998 | n/a (no panic) | SEC Wells Notice + NYDFS halt | NO trade — regulatory shutdown without panic | [[2023-02-busd-wind-down]] |
| **Mar 11, 2023** | **USDC** | **$0.8774** (-12%) | 48 hours | SVB banking failure | **Textbook arb: 14-50% across methods** | [[2023-03-usdc-svb-depeg]] |
| Mar 11, 2023 | FRAX | $0.88 | 48 hours (co-move) | Same as USDC (FRAX backed by USDC) | Same as USDC | (covered in USDC page) |
| Mar 11, 2023 | DAI | $0.97 (briefly) | 24 hours | USDC contagion (DAI partially USDC-backed) | Modest sympathy depeg | (covered in USDC page) |
| Oct 11, 2023 | USDR (TangibleDAO) | $0.50 | Permanent | Real-estate collateral redemption failure | NOT an arb — death spiral | — |
| Apr 2025 | sUSD (Synthetix) | $0.83 | Days | SNX collateral stress | Recovered through SIP backstop; arb captured by patient buyers | — |
| Multiple 2024-2025 | Various LRTs | -1 to -5% | Hours-weeks | Specific protocol stress (Pendle, Penpie) | Per-event specific | (covered in [[lst-depeg-arbitrage]]) |
| **Apr 18, 2026** | **GHO, crvUSD, sUSDe, USDe** | -30 to -80bp | 24-72 hours | KelpDAO/LayerZero contagion | **Sympathy-depeg basket trade; ~0.5-2% per event** | [[2026-04-kelp-stable-sympathy-depeg]] |

---

## By Trigger Category

### 1. Banking-Partner Instability

The earliest and most-recurring driver. A stablecoin issuer's banking relationship breaks → redemption channel friction → premium or discount emerges.

**Events**: Tether 2017-2020 (multiple); USDC/SVB March 2023.

**Mechanism**: USD on-ramp scarcity creates persistent or acute premium/discount. Crucially, **reserves are typically not in question** — only the channel is broken.

**Trade pattern**: redemption-channel arb (per [[stablecoin-depeg-profit-capture]] Method 2) is the dominant capture method. Buy discount on-market; redeem via official channel.

**Lessons**:
- Diversified banking partners reduce frequency (Tether post-2020; Circle post-2024)
- Banking schedule (T+1 settlement) creates a structural arb-window
- Single-banking-partner exposure is the main risk metric to monitor

### 2. Mechanism Failure (Above-Peg)

When a stable's mechanism breaks in the protocol's *own* design failures — typically liquidation systems failing under stress.

**Events**: DAI Black Thursday March 2020.

**Mechanism**: Auction failure → debt repayment shortfall → DAI demand exceeds supply → above-peg trading.

**Trade pattern**: short the rich stable via lending-protocol borrow + market sell; cover at peg restoration.

**Lessons**:
- Modern PSM-equipped stables (DAI, GHO, FRAX) are immune to this exact pattern
- Forks of pre-PSM architectures still vulnerable (cited in [[compound-fork-donation-short]])
- Above-peg events are rare but high-Sharpe when they occur

### 3. Algorithmic Death Spiral

Pure-algorithmic stables (no collateral backing) collapse irrecoverably when mechanism enters reflexive feedback.

**Events**: TITAN (Jun 2021); USDN (Apr 2022); UST/Terra (May 2022); USDR (Oct 2023).

**Mechanism**: Demand drops → mechanism issues more tokens to maintain peg → token price drops further → mechanism issues more → reflexive spiral.

**Trade pattern**: **Short, do not buy.** UST collapsed from $1 to $0; TITAN from $65 to $0; USDR from $1 to $0.50. **Long-side participants who tried to "catch the falling knife" lost 100%.**

**Lessons**:
- **Key principle**: pure-algorithmic stables (no collateral) cannot be arbitraged on the long side. Period.
- Hybrid algorithmic + collateral (like FRAX) can be arbed when collateral ratio remains above critical threshold.
- The sign of "death spiral incoming" is mechanism issuance accelerating without price recovery; verify before long entry.

### 4. Regulatory Action

Regulator intervenes; stable's operations are restricted or wound down.

**Events**: BUSD wind-down (Feb 2023); USDC Tornado Cash freeze (Aug 2022).

**Mechanism**: Variable. **Important**: regulatory action ≠ panic depeg. BUSD wound down without panic; USDC after Tornado Cash sanctions saw only sentiment effects, not price.

**Trade pattern**: Often the right move is to **NOT trade**. The "obvious" depeg trade may not materialize. Verify trigger type before sizing.

**Lessons**:
- Regulatory action has many modes; reserves question vs procedural classification produce very different price reactions
- Slow drains from regulatory wind-downs can be tradable via small-spread redemption arb during the multi-month period
- The absence of a panic depeg is itself a signal of issuer stability

### 5. LST/LRT Specific Stress

Liquid staking tokens face their own depeg patterns: validator queue, slashing, exit-queue depth.

**Events**: stETH June 2022 (3AC/Celsius); various LRT depegs 2024-2026.

**Mechanism**: Forced selling (liquidations of leveraged LST positions) + exit-queue capacity → temporary discount to ETH-equivalent value.

**Trade pattern**: Long the discount LST; hold through queue clearance OR convert to ETH via exit queue.

**Coverage**: documented in detail in [[lst-depeg-arbitrage]].

### 6. Contagion-Driven Sympathy

Cross-mechanism deviations from a primary exploit; affected stables are not directly exposed but trade weak in sympathy.

**Events**: KelpDAO sympathy depegs (April 2026) — multiple synthetic stables; Curve July 2023 (CRV-collateral spillover).

**Mechanism**: Major exploit → DeFi-wide risk-off → cross-stable panic → 30-80bp deviations on stables with no direct exposure.

**Trade pattern**: Basket of sympathy-depegged stables; 24-72h reversion as scope clarifies.

**Coverage**: documented in detail in [[2026-04-kelp-stable-sympathy-depeg]] and as variant 5 in [[synthetic-stablecoin-depeg-arbitrage]].

---

## Deep Dives: The Defining Events

The three events below are the canonical reference points for stablecoin risk. They are the reason the categories above exist. Each has a dedicated case-study page; figures here are summarized from those pages.

### UST / Terra — May 2022 (the archetypal death spiral)

The largest stablecoin failure in history and the defining lesson on [[algorithmic-stablecoins|algorithmic]] design. [[terra-luna|UST (TerraUSD)]] held its peg via a mint/burn arbitrage with its sister token LUNA, with much of its demand parked in the **Anchor Protocol** at an unsustainable ~20% yield.

| Aspect | Detail |
|--------|--------|
| **Date** | Depeg began ~May 7-9, 2022; collapse to near-zero within days |
| **Mechanism** | Large UST withdrawals → peg slips → arbitrage mints vast LUNA → LUNA hyperinflates → confidence collapses → reflexive spiral |
| **Outcome** | UST → ~$0; LUNA supply exploded from ~350M to trillions; **-$40B+ ecosystem value destroyed** |
| **Recovery** | None. Terra forked to "Terra 2.0"; original chain renamed Terra Classic |
| **Trade lesson** | **Do not catch the knife.** No long-side arb exists for an uncollateralized death spiral; only shorting (if early) or sitting out |

Contagion from Terra cascaded into 3AC, Celsius, Voyager, and the broader 2022 credit crisis. See [[terra-luna-collapse]] / [[2022-05-terra-luna-depeg-arb]].

### USDC / SVB — March 2023 (the textbook banking depeg)

The cleanest example of a **banking-partner** depeg, and the most profitable arb of the modern era.

| Aspect | Detail |
|--------|--------|
| **Date** | March 10-11, 2023 |
| **Trigger** | Silicon Valley Bank failure; Circle disclosed **$3.3B of USDC reserves** held at SVB |
| **Low** | [[usdc\|USDC]] traded to **~$0.8774** (March 11) on fear reserves were impaired |
| **Contagion** | DAI fell to ~$0.97 and FRAX to ~$0.88 (both partly USDC-backed) — a sympathy depeg |
| **Recovery** | Within ~48 hours, once US authorities backstopped SVB depositors and the $3.3B was confirmed safe |
| **Trade lesson** | Reserves were never actually lost — only the *channel* was in doubt. Buying the discount and/or redeeming at par returned a reported 14-50% across methods |

This event is the canonical proof that "banking-partner" depegs are usually a liquidity/confidence problem, not a solvency one — the highest-conviction depeg buy when the reserve question is answerable. See [[2023-03-usdc-svb-depeg]].

### DAI / Black Thursday — March 12, 2020 (the above-peg mechanism failure)

The rare and instructive case of a stablecoin breaking **above** $1 because its *own* liquidation machinery failed.

| Aspect | Detail |
|--------|--------|
| **Date** | March 12, 2020 (COVID crash) |
| **Trigger** | ETH fell ~43% in a day; Ethereum gas spiked; [[makerdao\|MakerDAO]] collateral auctions malfunctioned, some won with **$0 bids** |
| **Effect** | Protocol left **~$5.4M undercollateralized**; emergency MKR minted/auctioned to cover the gap |
| **Peg** | [[dai\|DAI]] traded **above $1** (to ~$1.10) for weeks as vault owners scrambled to buy DAI to repay debt |
| **Aftermath** | MakerDAO added circuit breakers, redesigned auctions (Liquidations 2.0), and added [[usdc\|USDC]] collateral / the PSM |
| **Trade lesson** | An over-collateralized stable can still break — *upward* — when liquidation infrastructure fails. The trade is to short the rich stable via a lending-protocol borrow and cover at peg restoration |

See [[2020-03-dai-black-thursday]] and the [[makerdao]] entity page.

---

## Recovery vs Permanent Loss

The clearest dividing line in the entire dataset is whether the peg ever came back:

| Outcome | Events | Common factor |
|---------|--------|---------------|
| **Recovered to par** | USDT 2018, DAI 2020 (above-peg), USDC/FRAX/DAI 2023, stETH 2022, sUSD 2025, KelpDAO basket 2026 | Real collateral or solvent reserves; only channel/confidence broke |
| **Never recovered** | UST 2022, TITAN 2021, USDN 2022, USDR 2023 | Uncollateralized or collateral fundamentally impaired |

**Every permanent loss in this table was an uncollateralized/algorithmic mechanism or a collateral-impairment failure.** No fully-reserved or over-collateralized stablecoin has yet suffered a permanent depeg. This is the empirical backbone of the [[depeg-risk]] backing-type heuristic.

---

## Frequency Analysis

Major events per year by category (2018-2026):

| Year | Banking | Mechanism (above-peg) | Algorithmic spiral | Regulatory | LST/LRT | Contagion | Total |
|------|---------|----------------------|-------------------|------------|---------|-----------|-------|
| 2018 | 1 | — | — | — | — | — | 1 |
| 2019 | — | — | — | — | — | — | 0 |
| 2020 | — | 1 | — | — | — | — | 1 |
| 2021 | — | — | 2 | — | — | — | 2 |
| 2022 | — | — | 2 | — | 1 | — | 3 |
| 2023 | 1 | — | 1 | 2 | — | — | 4 |
| 2024 | — | — | — | — | 2-3 | 1 | 3-4 |
| 2025 | — | — | — | — | 2-3 | 1 | 3-4 |
| 2026 (YTD) | — | — | — | — | 1 | 1 | 2 |

**Trend observations**:
- Banking-driven events have become rarer post-2020 (improved infrastructure)
- Algorithmic-spiral events are now historical (post-Terra, no major launches)
- LST/LRT and contagion events have grown rapidly (2024-present)
- Total event frequency is roughly stable at 2-5/year, but composition has shifted toward DeFi-internal triggers

This shift validates the [[ai-amplified-exploit-arbitrage]] thesis: as DeFi composability deepens and AI-driven exploits multiply, the *contagion* and *mechanism* depegs replace banking depegs as the primary trade.

---

## Outcomes by Trigger Type (Trade Performance)

| Trigger | Hit-rate (peg restored) | Median return per event | Best path |
|---------|------------------------|-------------------------|-----------|
| Banking-partner | ~95% (when channel functional) | 8-15% | Redemption arb (Method 2) |
| Mechanism failure (above-peg) | ~90% | 5-10% | Short via lending borrow (Method 4 inverse) |
| Algorithmic death spiral | ~5% | -100% (don't trade long) | DON'T trade long; short if early |
| Regulatory action | ~50% (variable) | 0-5% | Sometimes don't trade at all; small redemption arb if open |
| LST/LRT stress | ~85% | 3-8% | Long discount; convert via exit queue |
| Contagion sympathy | ~90% | 0.5-2.5% | Basket of sympathy-depegged stables |

Key takeaways:
- **Banking-partner events have the highest per-event return** (~10-15%) and the cleanest mechanism. Sweetest events when they occur.
- **Algorithmic death spirals are completely uninvestable on the long side.** The only correct action is to short or sit out.
- **Contagion sympathy depegs have lowest per-event return but highest frequency** (multiple events per major exploit) — cumulative capture is significant for desks running [[cross-chain-contagion-hedge]].
- **Regulatory events are bimodal**: either no depeg (BUSD pattern) or massive depeg (theoretical). Verify trigger type.

---

## Notable Trades and Desks

Over the 2017-2026 period, the desks most consistently profitable on stablecoin depeg events:

- **Cumberland (DRW)** — institutional OTC; primary captures across Tether 2017-2020, USDC/SVB 2023, KelpDAO 2026
- **Wintermute** — UK market maker; on-chain DeFi specialist; KelpDAO sympathy basket
- **Genesis Trading** (pre-2022 collapse) — institutional flow; Tether 2017-2020
- **Galaxy Digital** — Mike Novogratz's firm
- **B2C2** — UK market maker
- **Jane Street, Citadel Securities** — late entrants (2023+); USDC/SVB redemption arb
- **DeFi-native funds** (Polychain, Variant, Ramp Capital) — smaller capital but agile on novel mechanisms

The aggregate value extracted from stablecoin depeg events in 2017-2026 is estimated at **$2-5B+** distributed across these desks. The bulk of that came from infrastructure-enabled redemption arb (Method 2 from [[stablecoin-depeg-profit-capture]]) which retail and most mid-tier participants couldn't access.

---

## Forward Outlook (2026+)

Based on the historical pattern, expect:

1. **Banking-driven events**: rare but not extinct. Single-banking-partner stables (Tether-style) remain at risk; diversified-banking stables (USDC post-2024, FDUSD) lower-risk. Probability ~1-2 events per year.

2. **Mechanism failures**: increasingly rare for major stables (PSM-equipped); persistent for forks and new launches. Probability ~1-2 events per year on long-tail.

3. **Algorithmic death spirals**: very rare for new launches (regulatory environment makes them uneconomic to launch). Existing algorithmic stables with collateral hybrid (FRAX) are unlikely to spiral.

4. **Regulatory events**: increasingly common as MiCA and US frameworks mature. Most will be procedural (BUSD-style) rather than panic-inducing.

5. **LST/LRT stress**: continued; restaking architecture creates new variants. Probability ~3-5 events per year.

6. **Contagion sympathy depegs**: growing. AI-driven exploit frequency (per [[ai-vulnerability-discovery]]) means more triggering events; more contagion. Probability ~5-10 events per year (multiple per major exploit).

**Total expected events 2026-2027**: 10-20 per year, weighted toward LST/LRT and contagion categories.

This is the empirical foundation for the [[stablecoin-depeg-profit-capture]] strategy's claim of 2-5 major events/year being conservative; the broader contagion universe pushes the count meaningfully higher.

---

## Sources

- Per-event sources documented in individual case study pages
- CoinMetrics historical stablecoin price data
- DeFiLlama TVL and stablecoin circulation data
- Curve Finance subgraph (3pool composition history)
- Multiple regulatory body press releases (NYAG, SEC, NYDFS, FinCEN)
- Industry publications (The Block, CoinDesk, Bloomberg Crypto)

## Related

- [[stablecoin-pair-arbitrage]] — fiat-backed stable strategy hub
- [[synthetic-stablecoin-depeg-arbitrage]] — synthetic mechanism strategy hub
- [[stablecoin-depeg-profit-capture]] — tactical playbook (7 capture methods)
- [[lst-depeg-arbitrage]] — adjacent LST/LRT depeg strategy
- [[depeg-risk]] — risk framework
- [[defi-hacks-and-exploits]] — adjacent master timeline (exploits trigger contagion stable depegs)
- [[ai-amplified-exploit-arbitrage]] — broader AI-era trading framework
- [[cross-chain-contagion-hedge]] — captures sympathy-depeg basket leg
- [[makerdao]] — issuer of DAI/USDS (Black Thursday, SVB sympathy)
- [[sky]] / [[usds]] — current Sky-era stablecoin brand
- [[dai]] · [[usdc]] · [[terra-luna]] — the principals in the defining events
- [[stablecoin]] — general concept and design taxonomy
- [[real-world-assets]] — Treasury backing relevant to modern collateralized stables
- Individual case studies: [[2017-2020-tether-banking-premium]] · [[2020-03-dai-black-thursday]] · [[2022-05-terra-luna-depeg-arb]] · [[2022-06-steth-depeg]] · [[2023-02-busd-wind-down]] · [[2023-03-usdc-svb-depeg]] · [[2026-04-kelp-stable-sympathy-depeg]]
