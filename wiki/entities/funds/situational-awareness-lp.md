---
title: "Situational Awareness LP"
type: entity
created: 2026-05-31
updated: 2026-06-10
status: good
tags: [ai-trading, company]
entity_type: fund
aliases: ["Situational Awareness LP", "Situational Awareness Fund", "Aschenbrenner Fund"]
founded: 2024
website: "n/a"
related:
  - "[[leopold-aschenbrenner]]"
  - "[[ai-data-center-power-demand]]"
  - "[[iren]]"
  - "[[core-scientific]]"
  - "[[riot-platforms]]"
  - "[[hive-digital-technologies]]"
---

Situational Awareness LP is a US hedge fund founded and managed by [[leopold-aschenbrenner|Leopold Aschenbrenner]], the AI researcher and author of the June 2024 *Situational Awareness* essay. Launched mid-2024 with a thesis directly drawn from that essay — that AI compute scaling will continue through 2027+ and that the *physical infrastructure layer* (power, data centres, storage, HPC) is structurally underpriced while the *semiconductor consensus beneficiaries* are overpriced — the fund had grown to manage approximately $13.7B by late May 2026 based on 13F regulatory disclosures. The fund expresses its view through a distinctive bifurcated structure: large equity and call positions in physical AI infrastructure names paired with significant put option exposure to crowded semiconductor names. See aschenbrenner-bifurcated-ai-thesis for the durable analytical breakdown.

## Fund snapshot (late May 2026)

| Field | Value |
|---|---|
| **Manager** | [[leopold-aschenbrenner|Leopold Aschenbrenner]] |
| **AUM** | ~$13.7B (per 13F disclosures) |
| **Launch** | Mid-2024 |
| **Structure** | Hedge fund LP |
| **Notable distinction** | High-conviction concentration; bifurcated long/short |

(Source: 2026-05-31-aschenbrenner-13f-snapshot)

## Verified regulatory and performance data (June 2026)

Independent verification against public filings and reporting (2026-06-10):

- **Form ADV:** ~$9.3B in discretionary regulatory assets under management as of December 31, 2025 (per ADV data aggregated by Radient Analytics)
- **Q1 2026 13F:** 42 holdings, ~$13.7B total disclosed portfolio value (13f.info, SEC CIK 0002045724) — consistent with the figures in the late-May snapshot above. Put positions in SMH, NVDA, ORCL, and AVGO confirmed in the filing summary
- **Reported 2026 performance:** secondary press reporting (June 2026) stated the fund had gained roughly **+270% after fees in 2026**, lifting AUM above **$20B**; earlier 2026 reporting cited the portfolio up more than 100% year-to-date. These are reported performance figures, not independently verified NAV data — treat as MEDIUM confidence
- Note: 13F portfolio value reflects only disclosed US long-side and option positions, so the "$13.7B 13F value" and "AUM" figures measure different things and will diverge

## Late May 2026 13F summary

### Long positions (equity + calls)

| Ticker | Position size | Notes |
|---|---|---|
| NBIS | ~35% of long portfolio | **Core holding.** Disclosed 5.6% stake in the NVIDIA-backed neocloud |
| SNDK | $1.1B combined (equity + calls) | Storage / HBM thesis — over 1.1M shares + call array |
| BE | $879M equity (6.5M shares) + calls | Distributed power for data centres — the cleanest power play |
| CRWV | $697M combined equity + calls | Selectively trimmed call exposure |
| [[iren\|IREN]] | $401M | Crypto miner pivoting to AI HPC |
| [[core-scientific\|CORZ]] | $389M | Crypto miner with AI HPC pivot |
| APLD | $320M | Data centre / AI compute infrastructure |
| [[riot-platforms\|RIOT]] | $142M | Crypto miner |
| SHAZ | Initiated (size not disclosed) | Notable — see caution at end |
| [[hive-digital-technologies\|HIVE]] | Initiated | Crypto miner / HPC pivot |
| TE | Initiated | Utility / power provider |

### Short positions (put options)

| Ticker | Put notional | Notes |
|---|---|---|
| SMH | **$2.04B** | **Largest single line item** — VanEck Semiconductor ETF basket short |
| [[nvidia\|NVDA]] | $1.57B | Direct chip short via puts |
| ORCL | $1.07B | AI cloud capex / valuation short |
| AVGO | $1.01B | Custom silicon short |
| AMD | $969M | Direct chip short via puts |
| MU | $584M | Memory short via puts |
| TSM | $535M | Foundry short via puts |
| ASML | $494M | Lithography/EUV short via puts |
| INTC | $159M | Reversed prior long; now short via puts |

**Total put notional: ~$7.7B–$8.5B** across the semiconductor / chip complex.

### Recent exits

- **Lumentum (LITE)** — fully exited a $479M long position
- **EQT Corporation** — fully exited a $170M combined position
- **Liberty Energy (LBRT)** — trimmed
- **Solaris Energy Infrastructure (SEI)** — trimmed

## Concentration and structural observations

1. **Top holdings concentration is extreme.** NBIS alone is ~35% of the long portfolio. Combined NBIS + SNDK + BE + CRWV is likely >70% of the long book. This is a high-conviction, low-diversification structure consistent with a thesis-driven fund rather than a quant fund.
2. **Puts are sized to thesis, not as hedges.** The ~$7.7–8.5B in put notional is structural short positioning, not pair-hedging against the longs. If the chip complex falls, the puts pay out independently of what the longs do.
3. **The crypto-miner basket has a pivot thesis.** IREN, CORZ, APLD, RIOT, HIVE are not held *as* crypto miners but as **public companies with installed data centre and power assets pivoting to AI HPC**. Their value is the underlying real estate, power contracts, and rack space — not Bitcoin mining economics.
4. **Power and storage are the cleanest expressions of the thesis.** BE (fuel cells), TE (utility) on the power side; SNDK (storage) on the data layer. These are the bets least exposed to chip-cycle reversal.
5. **The SHAZ inclusion is notable.** SHAZ matches the ai-microcap-pump-pattern checklist; its inclusion in a high-conviction infrastructure fund is unexpected. Possible explanations: (a) small position taken for narrative-momentum exposure, (b) Aschenbrenner has private information about SHAZ not in public filings, or (c) the inclusion is anomalous and the fund treats it as a tail-optionality lottery. **The wiki view on SHAZ does not change based on inclusion in this fund** — see sharon-ai-holdings for the standalone analysis.

## Why a wiki page for a private fund

Most hedge funds don't warrant their own wiki entities because their thinking is hidden and their trades are inferred. Situational Awareness is unusual:

- **Public 13F sizing** with quarterly cadence
- **Public investment thesis** in the founder's essay
- **High-concentration sizing** that makes individual positions high-signal data points
- **Bifurcated thesis structure** that's analytically novel — most funds are either long-only or market-neutral, this one is "long one layer, short another layer"

This makes the fund a useful **reference point for AI infrastructure trading** independent of agreeing with the trades.

## Related

- [[leopold-aschenbrenner]] — the manager
- [[ai-data-center-power-demand]] — power-as-binding-constraint thesis
- All individual position entities are linked in the table above

## Sources

- SEC 13F filings, Situational Awareness LP (CIK 0002045724) — https://13f.info/manager/0002045724-situational-awareness-lp
- Radient Analytics, Form ADV summary for Situational Awareness LP — https://radientanalytics.com/firm/adv/situational-awareness-lp-333011
- Fintel institutional holdings page — https://fintel.io/i/situational-awareness-lp-5020
- Press reporting on 2026 performance (+270%, AUM >$20B), Globe and Mail / wire reprint, June 2026 — https://www.theglobeandmail.com/investing/markets/stocks/TE/pressreleases/2370003/leopold-aschenbrenners-situational-awareness-surpasses-20-billion-as-ai-focused-hedge-fund-gains-270-in-2026/
- Leopold Aschenbrenner, *Situational Awareness: The Decade Ahead* (June 2024) — https://situational-awareness.ai
- Verified via Perplexity (sonar), 2026-06-10
