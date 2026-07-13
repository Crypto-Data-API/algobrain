---
title: "Fastest Profitable Trades in History — Pattern Extraction"
type: overview
created: 2026-04-28
updated: 2026-06-20
status: excellent
tags: [history, behavioral-finance, risk-management, derivatives, options]
aliases: ["Fastest Trades", "Greatest Single Trades", "Asymmetric Trade Pattern Library", "Convex Trade Hall of Fame"]
related: ["[[2020-03-ackman-pandemic-cds-trade]]", "[[2007-2008-burry-subprime-cds-trade]]", "[[2006-09-amaranth-natural-gas-blowup]]", "[[2008-10-vw-porsche-short-squeeze]]", "[[1815-rothschild-waterloo-info-arbitrage]]", "[[1992-black-wednesday-erm-crisis]]", "[[1987-andy-krieger-nzd-short]]", "[[counterparty-stress-arbitrage]]", "[[convex-tail-hedge-arbitrage]]", "[[crisis-alpha]]", "[[information-arbitrage]]", "[[history-overview]]", "[[risk-management]]"]
---

This page extracts the **structural patterns** common to the fastest large profits in modern trading history — Krieger 1987, Soros 1992, Druckenmiller, Burry 2005-08, Arnold 2006, Ackman 2020, and historical antecedents going back to the Rothschilds. The headline P&Ls are eye-catching ($1B+ in days, 100× on premium) but more useful is the **architecture** — what these trades share, what's repeatable, and what's not. Each represents a documented case where a trader extracted enormous value in a short window. The synthesis identifies four reusable patterns and the conditions required to find them in current markets.

## The hall of fame

| Year | Trader | Trade | Premium / Capital at Risk | Realized P&L | Multiple | Days |
|------|--------|-------|---------------------------|--------------|----------|------|
| **1815** | Nathan Rothschild | British Consols (Waterloo info-arb) | Bank's working capital | ~£200K-£1M (disputed) | unknowable from public records | ~3 days |
| **1987** | [[1987-andy-krieger-nzd-short|Andy Krieger]] | NZD short at Bankers Trust | $700M position | ~$300M | ~0.4× | ~24 hours |
| **1992** | [[1992-black-wednesday-erm-crisis|George Soros + Druckenmiller]] | GBP short (ERM break) | $10B notional | ~$1B+ | 0.1× | ~2 days |
| **1995** | Druckenmiller | Yen short (Soros fund) | substantial | ~$1B (multi-year) | — | months |
| **2005-08** | [[2007-2008-burry-subprime-cds-trade|Michael Burry]] | Subprime tranche CDS | ~$30M annual carry | ~$700M (fund); ~$100M personal | ~25× per fund | 24-36 months |
| **2006** | [[2006-09-amaranth-natural-gas-blowup|John Arnold]] | Natural-gas calendar spreads vs Amaranth | ~$200-400M of capital | ~$1B | ~3-5× | ~weeks |
| **2007-08** | John Paulson | Subprime CDS (parallel to Burry) | ~$150M premium | ~$15B for the fund; ~$4B personal | ~100× | 12-18 months |
| **2008** | VW long-side traders | VW short-squeeze longs | varies | 5-10× on positions | 5-10× | 2 days |
| **2020** | [[2020-03-ackman-pandemic-cds-trade|Bill Ackman]] | CDX IG/HY pandemic CDS | ~$27M premium | ~$2.6B | ~100× | ~30 days |

## The four common patterns

Most of these trades fit one of four patterns. Some combine two.

### Pattern 1: Convex tail hedge in cheap-vol environments

**Examples:** Ackman 2020, Paulson 2007-08, Burry 2005-08

**Structure:**
- Find a market pricing extreme complacency (cheap implied vol, tight spreads, low VIX/MOVE).
- Buy bounded-cost protection against a defined adverse outcome (CDS, puts, structured insurance).
- Hold through the carry phase (months to years of paying premium).
- Exit when the catalyst arrives at multi-bagger gains.

**Why it works:** Markets cyclically underprice tail probability. Insurance is cheap when it shouldn't be. A small allocation per quarter, rolled persistently, captures these tail events on average even if individual periods are losses.

**Repeatable strategy:** [[convex-tail-hedge-arbitrage]]

**Required conditions:**
- Implied vol / spreads at multi-year tights
- A reasonable distribution of tail outcomes that re-rates to historical norms
- Capital structure that survives multi-year carry
- Bounded downside instrument access

### Pattern 2: Counterparty stress / forced-liquidation arbitrage

**Examples:** Arnold 2006 (vs Amaranth), Soros 1992 (vs Bank of England), the LRT depeg cascades of 2026 (vs Aave bad-debt holders)

**Structure:**
- Identify a counterparty whose position size exceeds market-clearing liquidity.
- Identify the specific capital-structure pressure that will force them to act.
- Position to receive the price impact of the forced unwind.

**Why it works:** Forced sellers have a non-fundamental marginal price. Their unwind path is predictable from position structure, capital pressure, and exchange/protocol mechanics. Trading the unwind is structurally more tractable than predicting fundamentals.

**Repeatable strategy:** [[counterparty-stress-arbitrage]]

**Required conditions:**
- Visible position-size data (large-trader reports, COT, on-chain analytics, prime-broker disclosures)
- Capital-structure pressure points (margin, redemption gates, regulatory limits, liquidation thresholds)
- Predictable unwind path (which assets sell first, by how much)
- Independent fundamental view to size the persistence of the post-unwind price

### Pattern 3: Information speed advantage

**Examples:** Rothschild 1815 (Waterloo couriers), HFT firms 2010s (microwave links Chicago-NY), modern alt-data hedge funds, on-chain whale-tracking traders

**Structure:**
- Invest in infrastructure that delivers information faster than the market consensus.
- Hold positions sized to the information lead time and the size of the eventual public re-rating.
- Exit on or shortly after public news.

**Why it works:** Markets re-rate when new information becomes public. Being early to information is being early to the re-rating. This is not "secret information" — it is "public-eventually information, faster."

**Repeatable strategy:** [[information-arbitrage]] (concept page; specific implementations include [[block-trade-flipping-arbitrage]], MEV strategies, alt-data hedge fund equity strategies)

**Required conditions:**
- Information that will become public and will move markets
- Infrastructure capable of receiving it earlier (and that competitors haven't built)
- Legal jurisdiction in which trading on the information is permissible (most insider-trading information is illegal; alt-data is legal)
- Sufficient market liquidity to deploy capital in the information window

### Pattern 4: Float-constraint short squeeze

**Examples:** VW 2008, GameStop 2021, copycat squeezes 2021-2022, low-float crypto squeezes

**Structure:**
- Identify a stock or token where reported float overstates true tradable supply.
- Confirm short interest exceeds true float.
- Identify the catalyst that will reveal the float constraint (regulatory disclosure, holder reveal, redemption event).
- Position long before the catalyst at modest size.

**Why it works:** When more shares are sold short than truly available to borrow/buy, mathematics force the squeeze. Forced cover-buying meets inelastic supply, producing exponential price moves.

**Repeatable strategy:** No dedicated wiki strategy page yet; closely related to [[counterparty-stress-arbitrage]] and discussed in [[gamestop-short-squeeze]].

**Required conditions:**
- Float overstated by hidden synthetic ownership (cash-settled options, sponsor blocks, derivative-hedged shares treated as float)
- Short interest > true float
- A catalyst event that reveals the constraint
- Legal ability to take long positions ahead of the catalyst (most jurisdictions allow this; some insider-trading restrictions apply if catalyst is corporate-disclosure-driven)

## Pattern summary map

The four patterns, their repeatable strategy pages, edge source, and the scarce resource that makes each work:

| Pattern | Repeatable Strategy | Edge Source | Scarce Resource | Canonical Cases |
|---------|--------------------|-------------|-----------------|-----------------|
| 1. Convex tail hedge | [[convex-tail-hedge-arbitrage]] | Structural + analytical + behavioral | Capital that survives multi-year carry | Ackman 2020, Paulson, Burry |
| 2. Counterparty stress | [[counterparty-stress-arbitrage]] | Structural + informational | Visibility into a forced seller's position | Arnold vs Amaranth, Soros 1992 |
| 3. Information speed | [[information-arbitrage]] | Informational + latency | Infrastructure competitors haven't built | Rothschild 1815, HFT, alt-data |
| 4. Float-constraint squeeze | (see [[counterparty-stress-arbitrage]], [[gamestop-short-squeeze]]) | Structural | Knowledge that float < short interest | VW 2008, GameStop 2021 |

See [[edge-taxonomy]] for how these edge sources map to the broader framework.

## Cross-cutting features (all four patterns)

Every trade in the hall of fame shares some subset of these:

### A. Asymmetric instrument

The trade was constructed in an instrument where downside was bounded and upside was uncapped. Examples:

- **CDS** (premium = max loss; payoff in default = par notional)
- **Put options** (premium = max loss; payoff = strike - underlying)
- **Currency forwards at extreme strikes** (limited carry cost; large payoff in regime break)
- **Long shares with embedded squeeze convexity** (downside is mark-to-market; upside is unbounded by short-cover dynamics)

Linear instruments (spot exposure, futures, simple shorts) rarely produce 25-100× returns even on correct theses. **The instrument is the trade.**

### B. Convergence forced by structure

The catalyst that converted thesis-correctness into mark-to-market profit was structural, not narrative:

- **Teaser-rate resets** (Burry's subprime — reset waterfall scheduled into 2007 contracts)
- **Margin calls** (Arnold vs Amaranth — Amaranth's prime brokers had defined risk thresholds)
- **Float reveal** (VW — Porsche's regulatory disclosure was a one-day event)
- **Currency band breaks** (Soros 1992 — Bank of England had a defined defense capacity)
- **Pandemic-driven credit defaults** (Ackman 2020 — once shutdowns began, corporate-bond defaults followed mechanically)

Structural catalysts are predictable in mechanism even when unpredictable in timing. Narrative catalysts ("the market will realize this is overvalued") are not.

### C. Multi-year preparation, multi-day payoff

Every hall-of-fame trade was set up over months to years before the payoff window:

- **Burry**: 2003 research → 2005 entry → 2007 catalyst (4 years)
- **Arnold**: 2002-2006 building Centaurus + 2006 reading Amaranth's positions (multiple years)
- **Ackman**: continuous Pershing Square activity since 2004 + late-2019 awareness of cheap CDX (years of context)
- **Krieger**: 18-month research on currency-market structural inefficiencies before 1987
- **Soros/Druckenmiller**: Quantum Fund had been studying ERM stress since 1990; trade executed 1992
- **Rothschild**: courier network built over decades

The payoff window — when most of the P&L is realized — is days to weeks. **The work is in the preparation; the payoff is in the execution.**

### D. Capital structure that survived

Each winner had capital that didn't get pulled at the worst moment:

- **Burry**: invoked contractual lockup
- **Ackman**: closed-end vehicle, no daily redemption
- **Soros/Druckenmiller**: Quantum Fund permanent capital base
- **Arnold**: Centaurus principal capital + sticky LP base
- **Rothschild**: family partnership; no external LPs

Many traders had similar theses but couldn't survive the carry. **Capital structure is the moat.**

### E. Discipline at the exit

Several of these traders left money on the table by exiting too early — but none let the position fully reverse before exiting:

- **Ackman** closed CDX before peak spread widening (could have made more if held longer).
- **Burry** began exiting at large profits in 2007, missing some of the 2008 peak default cascade.
- **Krieger** was held back by Bankers Trust's risk committee; a fully unconstrained position could have made multiples more.
- **Arnold** sold into the Amaranth unwind rather than holding for full mean reversion.

The pattern: **lock in convex profits while convexity is still working**, rather than holding for the mathematical maximum. Marginal-tail-of-tail upside is rarely worth the reversal risk.

## What's NOT a pattern

Several common narratives about these trades are either wrong or non-replicable:

- **"Predicting the future."** None of these traders predicted timing precisely. They positioned for asymmetric outcomes and let the catalyst find them.
- **"Insider information."** Only Rothschild had information advantage in the 1815 sense; modern winners worked from public/semi-public data others didn't bother to read.
- **"Lucky one-off bets."** Each trader had a documented framework that produced multiple successful trades over a career. The one trade each is famous for is the largest of a long sequence.
- **"Genius IQ."** Most of these traders describe their edge as discipline, work ethic, and instrument knowledge — not raw IQ.
- **"Macro forecasting."** Soros 1992 is sometimes framed as a macro forecast; in practice, Druckenmiller's analysis was that the ERM band was structurally too narrow for UK macroeconomics, and the Bank of England's defense capacity was finite. This is structural analysis, not forecasting.

## The other side: who lost

Every legendary winner had a counterparty taking the opposite, losing side. The cautionary record is as instructive as the hall of fame — these are the structural positions that *generated* the convex payoffs above:

| Loser | Position | Pattern they were on the wrong side of | Outcome |
|-------|----------|----------------------------------------|---------|
| CDS / structured-credit writers (2007-08) | Short subprime tail | Pattern 1 (Burry, Paulson long) | Catastrophic; AIG required a federal backstop |
| [[2006-09-amaranth-natural-gas-blowup\|Amaranth Advisors]] (2006) | Oversized nat-gas calendar spreads | Pattern 2 (Arnold on the other side) | ~$6.6B loss; fund collapsed in ~weeks |
| Bank of England (1992) | Defending the ERM band | Pattern 2 (Soros short GBP) | Forced out of the ERM ("Black Wednesday") |
| Porsche short sellers (2008) | Short VW into a hidden float | Pattern 4 (squeeze longs) | Forced cover at extreme prices |
| CDX HY/IG sellers (early 2020) | Short credit tail at multi-year tights | Pattern 1 (Ackman long) | Spreads blew out on the pandemic shock |

The lesson for sizing: the winners' bounded-downside instruments are precisely the losers' unbounded-downside instruments. Selling tail protection (writing CDS, shorting vol, being short a constrained float) collects steady carry until it doesn't — see [[convex-tail-hedge-arbitrage]] for the structural reason vol-sellers persistently underprice the tail, and [[risk-management]] for why position-size limits matter most exactly when the carry looks free.

## How to find the next one

For a trader looking to repeat one of these patterns in current markets:

### Scan for cheap convexity

Look at:
- **CDX IG / HY at multi-year tights** (currently elevated post-2022; not the setup)
- **VIX < 13 for sustained periods**
- **MOVE index at multi-year tights**
- **Crypto implied vol (DVOL, BVIV) below 50 for sustained periods**
- **EM sovereign 5y CDS at multi-year tights for stressed sovereigns**
- **Long-dated calls/puts on indices at flat skew** (no premium for tail)

When you see this setup, the [[convex-tail-hedge-arbitrage]] framework applies.

### Scan for counterparty stress

Look at:
- **Hedge funds approaching peak drawdown with redemption gates near** (13F filings, Form ADV, public commentary)
- **Crypto whales with on-chain leverage (Aave, Compound, Euler positions visible on-chain)**
- **Stablecoin issuers with public reserve attestations showing stress**
- **Validator-node operators with public staking yields and visible exit queues**
- **Token-unlock events approaching with no public hedging**

When you see this setup, [[counterparty-stress-arbitrage]] applies.

### Scan for information asymmetries

Look at:
- **Alt-data sources you've built that competitors haven't** (satellite imagery, foot-traffic, on-chain analytics)
- **Markets where information lag is structural** (illiquid commodities, pre-IPO secondaries)
- **Regulatory or legal events with predictable timing but uncertain outcomes** (FOMC, ECB, court rulings)
- **DeFi exploit feeds** that you've integrated faster than the market

When you have a verified speed advantage, [[information-arbitrage]] applies.

### Scan for float constraints

Look at:
- **Stocks with high short interest as % of float** (S3 Partners, FINRA data)
- **Stocks with sponsor blocks, family ownership, or known holders not captured in float calculations**
- **Stocks with pending regulatory disclosures that may reveal hidden ownership**
- **Crypto tokens with high vesting cliff risk**
- **NFT collections with synthetic-float dynamics from leverage protocols**

When you see this setup, the float-constraint short squeeze framework applies.

## Why this page is more useful than biographies

Most coverage of legendary trades focuses on the trader (genius narrative) or the macro context (era-specific narrative). For a working trader, the structural patterns are what's repeatable. The trader's personality is not.

This page should be read alongside:

- The individual case studies linked above for trade-specific detail.
- [[convex-tail-hedge-arbitrage]] and [[counterparty-stress-arbitrage]] for the strategy-level generalizations.
- [[edge-taxonomy]] for where these fit in the broader edge framework.
- [[crisis-alpha]] for adjacent concepts.
- [[risk-management]] for sizing frameworks.

The patterns are 200+ years old. The instruments change; the structures don't.

## Related

- [[2020-03-ackman-pandemic-cds-trade]]
- [[2007-2008-burry-subprime-cds-trade]]
- [[2006-09-amaranth-natural-gas-blowup]]
- [[2008-10-vw-porsche-short-squeeze]]
- [[1815-rothschild-waterloo-info-arbitrage]]
- [[1992-black-wednesday-erm-crisis]]
- [[1987-andy-krieger-nzd-short]]
- [[counterparty-stress-arbitrage]]
- [[convex-tail-hedge-arbitrage]]
- [[crisis-alpha]]
- [[edge-taxonomy]]
- [[risk-management]]
- [[history-overview]]

## Sources

- Individual case studies linked above
- Sebastian Mallaby, *More Money Than God* (2010)
- Michael Lewis, *The Big Short* (2010)
- Greg Zuckerman, *The Greatest Trade Ever* (2009)
- Niall Ferguson, *The House of Rothschild* (1998-99)
- Sebastian Mallaby, *The Man Who Knew* (Greenspan biography, indirect context)
