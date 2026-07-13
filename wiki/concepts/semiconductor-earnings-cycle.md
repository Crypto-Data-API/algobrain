---
title: "Semiconductor Earnings Cycle"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [stocks, earnings, technology, options, correlation, risk-management]
aliases: ["Semis Earnings Cluster", "Semiconductor Earnings Window", "Semis Print Cycle"]
related: ["[[options-concentration-risk]]", "[[nvidia]]", "[[broadcom]]", "[[implied-volatility]]", "[[correlation]]", "[[dispersion-trading]]", "[[itpm-trade-construction-playbook]]", "[[earnings-volatility]]", "[[term-structure]]"]
domain: [risk-management, market-microstructure, behavioral-finance]
prerequisites: ["[[implied-volatility]]", "[[correlation]]", "[[options-greeks]]"]
difficulty: advanced
---

The semiconductor earnings cycle is the recurring 5-7 week window each quarter during which the largest global semiconductor companies report results in a tightly choreographed sequence — TSMC first, then ASML, then Intel and AMD, then NVIDIA, Broadcom, and Marvell late in the cycle. Because each print conditions read-through into the next, the entire complex's [[implied-volatility]] and pairwise [[correlation]] structure repeatedly resets within a single calendar window. This makes the semis cycle the canonical real-world case for [[options-concentration-risk]]: a book of "diversified" short premium across NVDA, AVGO, AMD, TSM, MU, ASML, ARM, and MRVL is, during the cluster, effectively one position on "the AI capex narrative survived the quarter."

## The Earnings Cluster Window

Semiconductor earnings cluster predictably each quarter because most large semis run on a calendar fiscal year (or close to it) and report 3-7 weeks after quarter end. The actual sequence has been stable for several years and currently runs in roughly the following order:

| Week (post quarter-end) | Reporter | Why it leads or lags |
|------|----------|----------------------|
| Week 2-3 | [[tsmc|TSMC]] (TSM) | Reports earliest because Taiwan-listed; foundry results give first read on global silicon demand |
| Week 3 | [[asml]] (ASML) | Litho equipment; reads on capex commitments by foundries |
| Week 3-4 | [[texas-instruments]] (TXN) | Analog; reads on industrial / auto demand |
| Week 4-5 | [[intel]] (INTC) | x86 server + client CPUs; reads on traditional data center |
| Week 4-5 | [[amd]] (AMD) | Data center GPU + CPU; first major AI-capex print |
| Week 4-5 | [[qualcomm]] (QCOM) | Mobile / handset; reads on smartphone unit demand |
| Week 5-6 | [[micron]] (MU) | DRAM / HBM memory; reads on AI memory pricing |
| Week 6-7 | [[nvidia\|NVIDIA]] (NVDA) | The AI bellwether; reports last among the mega-caps because of late January fiscal year-end |
| Week 6-7 | [[broadcom\|Broadcom]] (AVGO) | Custom silicon (XPU), networking; reads on hyperscaler ASIC commitments |
| Week 6-7 | [[marvell]] (MRVL) | Custom silicon, optical; reads on networking + Amazon/Google ASIC ramps |

Concretely for the Q1 2026 cycle, prints ran from TSMC on April 17 through NVIDIA on May 28 and AVGO/MRVL in early June — roughly six weeks of staggered events, every one of which moves the entire complex.

## Sequential Read-Through

The reason the cycle is *one event* rather than ten is that each company's print contains forward-looking information that updates priors on every subsequent reporter. The chain has become more tightly linked since 2023 as the AI capex theme concentrated demand among a small set of hyperscaler buyers.

The conditioning chain typically runs:

1. **TSMC capex and HPC commentary** — TSMC's quarterly capex guide and HPC (high-performance computing) revenue mix is the first read on whether AI silicon orders are accelerating, holding, or rolling over. A capex raise pulls ASML and the entire semicap complex up; a cut crushes them.
2. **ASML order book** — ASML's net bookings (especially EUV system orders) confirm or contradict TSMC's capex signal. A weak ASML order book after a strong TSMC capex raise is a contradiction the market has to reprice.
3. **AMD / Intel data center segment** — AMD's MI300/MI350 data center GPU run-rate is the cleanest single-stock read on the *non-NVIDIA* slice of AI accelerator demand. Intel's Gaudi commentary plus DCAI segment growth fills out the picture.
4. **NVIDIA + AVGO hyperscaler demand** — NVIDIA's data center revenue and forward guide is the dominant single print of the cycle. AVGO's AI revenue (custom XPU + networking) and forward AI revenue guide is now the second-most-watched. A divergence between strong AVGO custom-silicon demand and softer NVDA forward guide is read as hyperscalers shifting from merchant GPUs to in-house ASICs.
5. **MRVL custom silicon** — Reports late and confirms or contradicts the AVGO read on custom-silicon ramps at Amazon, Google, Microsoft.

Each link in this chain shifts the [[implied-volatility]] surface of the next reporter. A hot TSMC + ASML pair pulls down [[nvidia|NVDA]] and [[broadcom|AVGO]] IV (the market is now more confident demand is intact); a soft TSMC capex guide *raises* the IV of every subsequent reporter as uncertainty about the AI capex thesis widens.

## Correlation Behavior During the Window

Pairwise realized correlation among the largest US semis runs ~0.45-0.55 during normal regimes (calm tape, no major sector catalysts). During the earnings cluster window, that correlation typically rises to **0.70-0.90** for several reasons:

- **Common factor exposure** — every name is being repriced on the same AI capex narrative
- **Systematic ETF flows** — [[soxx|SOXX]] and [[smh|SMH]] flows mechanically move all components together; ETF rebalancing concentrates on event days
- **Read-through trading** — discretionary traders explicitly trade the read-through (e.g., long AVGO calls into NVDA's print)
- **Index hedging** — book-level vol overlays use SOXX/SMH options which tighten effective single-name correlations

The implication for an options book: a covariance matrix calibrated on calm-tape data will *materially under-state* portfolio variance during the cluster window. A book modeled assuming 0.5 correlations between NVDA, AVGO, AMD, MRVL will see actual stress-window variance roughly 1.6-2.0x baseline, because portfolio variance is dominated by off-diagonal terms.

This is a deterministic correlation regime shift, not a random one. The window opens with TSMC and closes with AVGO/MRVL, every quarter.

## Implied Volatility Behavior

The complex's IV behavior during the cycle has several characteristic features:

- **Term structure inversion before each leading print** — In the days before TSMC and again before ASML, front-week IV spikes well above back-month IV across the entire complex (not just the reporter), creating a steeply inverted term structure. The inversion partially compresses on the print itself (the "earnings IV crush") and re-inverts before the next reporter.
- **Whole-complex IV moves on TSMC and ASML** — Because these two are read as the leading indicators, a surprise in either direction shifts NVDA, AVGO, AMD, MRVL IV by several points within minutes, even though those names have not yet reported.
- **Skew steepening into NVDA** — Put skew on NVDA and AVGO typically steepens into the late-cycle prints as event-hedging demand concentrates. Crash skew on the entire complex via SOXX and SMH puts also steepens.
- **Calendar spread compression then expansion** — Front-week vs back-month calendar spreads compress (expensive front-week) before each print, then re-expand after the IV crush. The pattern repeats roughly six times in the cycle.
- **Dispersion behavior** — Implied correlation (priced via SPX/SOXX index vol vs single-name vol) typically *falls* into early-cycle prints (idiosyncratic risk dominates) and *rises* into late-cycle prints (read-through dominates). See [[dispersion-trading]] and [[implied-correlation]].

## Single-Stock vs Sector Cascades

A single hot or cold print late in the cycle creates a cascading repricing across the complex because positions have built up around the read-through. Two characteristic patterns:

**Hot AVGO into NVDA** — When AVGO prints strong AI guidance ahead of NVDA, traders bid NVDA into the print expecting a confirming read. NVDA IV stays elevated. If NVDA then beats and guides up, the entire complex (including names that already reported) re-rates higher. If NVDA *meets but does not beat* the now-elevated bar, the sector sells off despite an objectively fine print.

**Weak TSMC guide cascading** — A soft TSMC capex guide early in the cycle pulls every subsequent reporter's IV up and pre-prices a weaker guide from each. Sector ETFs (SOXX, SMH) gap down. Short-premium books that were sized assuming "one hot, one cold, average is fine" find every subsequent print is being graded against a now-lower bar, and any miss along the way produces an outsized down move because the cluster keeps revising the priors.

## Position-Sizing Implications for Options Books

The semis earnings cycle is the textbook case where position-level sizing rules fail and book-level rules are required. ITPM-style guidance (see [[itpm-trade-construction-playbook]] and [[options-concentration-risk]]):

- **Cap earnings-cluster vega** — no more than ~25% of book vega should sit on positions with earnings inside any single calendar week, and no more than ~40% of book vega across the entire 5-7 week cluster.
- **Treat the complex as one underlying for sizing** — when sizing a new short premium trade on a semi during the cluster, count it against an aggregate "semis bucket" with a hard cap (e.g., 20% of portfolio risk).
- **Stress with cluster correlations, not normal correlations** — re-run portfolio variance with ρ=0.85 between every pair of semis. The "stress / baseline variance" ratio above 2.0 means hidden cluster concentration.
- **Avoid stacking same-direction views** — short call spreads on NVDA, AVGO, AMD, and MRVL is *one* short-AI-capex-momentum bet. Sizing rules should treat it that way.
- **Beware late-cycle position growth** — books tend to accumulate positions through the cycle as IV stays elevated; the late-cycle book is usually the most concentrated of the year.
- **Pre-cluster scrub** — before TSMC reports each quarter, audit the book against the cluster window and trim or hedge before the first print, not after.

## Historical Case Studies

**AVGO September 2024 strong → NVDA cycle setup** — AVGO reported in early September 2024 with a strong AI revenue guide that traders read as confirming hyperscaler ASIC ramps. The semis complex rallied into the late-November NVDA print on extrapolated read-through. NVDA delivered a strong print but with a forward guide that merely met the elevated bar; SOXX and SMH sold off in the days following despite NVDA earnings being objectively fine. Books that had stacked short put spreads across NVDA, AVGO, MU, and AMD into the cycle saw correlated losses.

**Weak TSMC guide cascading** — In multiple cycles where TSMC trimmed full-year capex or HPC growth guidance early in the cluster, the entire complex's IV ratcheted higher across every subsequent reporter, and ASML's order book confirmed the soft signal a week later, producing a sector-wide drawdown. Short premium books that had not yet trimmed exposure ahead of TSMC took correlated losses across every name in the bucket.

**August 5, 2024 yen carry unwind** — Not a semis-earnings event per se, but illustrative: a sudden vol regime shift drove the complex's pairwise correlation toward 0.85+ for several sessions, demonstrating that the same correlation-spike behavior the cluster window exhibits also appears on macro tail events. Books built on calm-regime correlations gave back months of premium in days. See [[vix-august-2024-spike]].

## Hedging the Cluster

Several structures address cluster concentration directly:

- **SOXX / SMH puts or put spreads** — the cleanest single hedge for a semis-heavy book. A cluster-window put spread on [[soxx|SOXX]] or [[smh|SMH]] (e.g., 30-delta to 15-delta, 30-45 DTE) provides correlated downside protection at lower cost than buying single-name puts on every position. Sized as a percentage of the short-premium credit collected during the cluster.
- **Index dispersion structures** — long single-name straddles on the messiest 1-2 names (typically NVDA + AVGO during AI cycles) financed by short SOXX or SMH straddles. Profitable when single-name realized vol exceeds index realized vol, which is typical *into* the cluster but reverses *during* the cluster as correlations rise. See [[dispersion-trading]].
- **Calendar spread structures** — long back-month / short front-week calendars on the late-cycle reporters (NVDA, AVGO, MRVL). The front-week IV ramp into the print is sold; the back-month vol stays bid through the entire cluster. Profitable on cluster-window vol persistence even when the directional outcome is uncertain.
- **Cross-asset hedge** — long [[vix-call-spreads]] or long [[move-index|MOVE]]-driven structures during the cluster window, sized as catastrophic protection rather than directional vol expression.
- **Skip the cycle entirely** — for many discretionary books the cleanest hedge is simply to not be short premium on the complex during the cluster. The same names trade for 10 more months of the year with normal correlations.

The choice between explicit hedges and exposure reduction depends on the book's mandate. A vol-selling program *can* sit out the cluster; a delta-hedged dispersion book *must* be on during the window because that's where its edge concentrates.

## Related

- [[options-concentration-risk]] — the parent risk concept; the semis cluster is the canonical worked example
- [[nvidia]] — late-cycle bellwether; dominates the back half of the window
- [[broadcom]] — late-cycle custom-silicon read-through
- [[implied-volatility]] — the term structure and skew dynamics described above
- [[correlation]] — foundational concept; cluster window is a deterministic correlation regime shift
- [[correlation-breakdown]] — the same phenomenon seen in macro tail events
- [[dispersion-trading]] — explicit trade structure that exploits cluster correlation behavior
- [[implied-correlation]] — index vs single-name vol relationship during the cycle
- [[itpm-trade-construction-playbook]] — book construction and earnings-cluster sizing rules
- [[options-portfolio-construction]] — broader book-level construction
- [[options-position-sizing]] — single-position sizing; insufficient on its own during cluster
- [[options-stress-testing]] — running cluster-correlation scenarios
- [[earnings-volatility]] — single-name event-driven IV behavior
- [[term-structure]] — the inversion behavior described above
- [[vega-budgeting]] — allocating vega across the cluster
- [[soxx]] — semis sector ETF used for hedging
- [[smh]] — alternative semis sector ETF
- [[tsmc]] — first reporter in the cluster
- [[asml]] — second reporter; capex confirmer
- [[amd]] — mid-cycle AI accelerator read
- [[intel]] — mid-cycle traditional data center read
- [[micron]] — memory / HBM read
- [[marvell]] — late-cycle custom silicon read

## Sources

- [[options-concentration-risk]] — wiki page that introduces the cluster as the canonical concentration example
- [[itpm-trade-construction-playbook]] — book construction methodology including earnings-cluster caps
- [[vix-august-2024-spike]] — case study of correlated sell-off behavior
