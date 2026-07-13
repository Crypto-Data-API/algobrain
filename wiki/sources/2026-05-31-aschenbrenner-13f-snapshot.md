---
title: "Situational Awareness LP 13F Snapshot — Late May 2026"
type: source
created: 2026-05-31
updated: 2026-06-12
status: good
tags: [meta, ai-trading]
aliases: ["Aschenbrenner 13F Snapshot", "Situational Awareness LP 13F", "SAW LP Holdings May 2026"]
source_type: data
source_url: "n/a — 13F regulatory filings (compiled summary supplied by user)"
source_author: "Situational Awareness LP via 13F-HR filing"
source_date: 2026-05-31
source_file: "n/a — direct 13F compilation from user message"
confidence: medium
claims_count: 22
related:
  - "[[leopold-aschenbrenner]]"
  - "[[situational-awareness-lp]]"
  - "[[aschenbrenner-bifurcated-ai-thesis]]"
---

#meta

Late May 2026 13F regulatory filing summary for [[situational-awareness-lp|Situational Awareness LP]] managed by [[leopold-aschenbrenner|Leopold Aschenbrenner]]. Compiled summary supplied by user on 2026-05-31 during portfolio research. Underlying source is the fund's mandatory 13F-HR filing with the SEC; this page reproduces the compiled data and tracks confidence assignment per claim.

## Why this was ingested

User asked for an entity page on Leopold Aschenbrenner and requested wiki coverage of his fund's holdings, identifying which were not yet covered. Per the `feedback_always_update_wiki` memory rule, useful 13F data with fund-thesis interpretation should be wired into the wiki by default. The 13F data is unusually high-signal because (a) Aschenbrenner's *Situational Awareness* essay (June 2024) explicitly states the thesis the fund is expressing, and (b) the holdings are highly concentrated, making each individual position a strong data point.

## Claims and confidence flags

### Fund-level

| Claim | Value | Confidence | Notes |
|---|---|---|---|
| Total AUM | **~$13.7B** | HIGH (regulatory filing) | 13F covers long equity + options notional |
| Filing period | Late May 2026 (13F-HR) | HIGH | 13F filings are quarterly with 45-day lag |
| Fund manager | Leopold Aschenbrenner | HIGH | Public filings, fund correspondence |
| Structure | Bifurcated long-physical / short-semis-via-puts | HIGH | Pattern visible in disclosed positions |

### Long positions

| Ticker | Position type | Size | Confidence | Notes |
|---|---|---|---|---|
| NBIS | Equity (5.6% stake) | ~35% of long portfolio | HIGH | Core holding |
| SNDK | Equity + calls | $1.1B combined | HIGH | 1.1M+ shares + call array |
| BE | Equity + calls | $879M equity (6.5M shares) + calls | HIGH | |
| CRWV | Equity + calls | $697M combined | HIGH | Calls selectively trimmed |
| IREN | Equity / options | $401M | HIGH | |
| CORZ | Equity / options | $389M | HIGH | |
| APLD | Equity / options | $320M | HIGH | |
| RIOT | Equity / options | $142M | HIGH | |
| SHAZ | New initiation | Size not disclosed | MEDIUM | Anomalous given pump-pattern profile |
| HIVE | New initiation | Size not disclosed | MEDIUM | |
| TE | New initiation | Size not disclosed | MEDIUM | |

### Short positions (put options)

| Ticker | Put notional | Confidence | Notes |
|---|---|---|---|
| SMH | $2.04B | HIGH | Largest single line item |
| NVDA | $1.57B | HIGH | |
| ORCL | $1.07B | HIGH | |
| AVGO | $1.01B | HIGH | |
| AMD | $969M | HIGH | |
| MU | $584M | HIGH | |
| TSM | $535M | HIGH | |
| ASML | $494M | HIGH | |
| INTC | $159M | HIGH | Reversed prior long position |
| **Total put notional** | **~$7.7–8.5B** | HIGH | Range reflects different disclosure aggregation |

### Recent dispositions

| Ticker | Action | Size | Confidence |
|---|---|---|---|
| LITE (Lumentum) | Full exit | Was $479M | HIGH |
| EQT (EQT Corp) | Full exit | Was $170M combined | HIGH |
| LBRT (Liberty Energy) | Trimmed | n/a | MEDIUM |
| SEI (Solaris Energy) | Trimmed | n/a | MEDIUM |

## Pages this source contributed to

**New pages created (9):**

- [[leopold-aschenbrenner]] — person entity
- [[situational-awareness-lp]] — fund entity with full 13F table
- [[aschenbrenner-bifurcated-ai-thesis]] — narrative page interpreting the structure
- [[applied-digital]] — new entity (APLD)
- [[sandisk]] — new entity (SNDK)
- [[smh-vaneck-semiconductor-etf]] — new market page (SMH)
- [[oracle]] — new entity (ORCL)
- [[hive-digital-technologies]] — new entity (HIVE — disambiguated from crypto Hive)
- [[t1-energy]] — stub entity (TE)

**Existing pages cross-linked:**

- [[nebius-group]], [[coreweave]], [[bloom-energy]], [[iren]], [[core-scientific]], [[riot-platforms]], [[nvidia]], [[broadcom]], [[amd]], [[micron]], [[taiwan-semiconductor-manufacturing]], [[asml-holding]], [[intel]], [[sharon-ai-holdings]]

## Caveats

- **13F data is point-in-time** and lags 45 days behind the reporting period; positions may have shifted materially between filing date and any subsequent date
- **13Fs do not disclose short equity positions, only long stock and long/short options notional** — the put notional figures are reportable, the short-stock side (if any) is not
- **Notional ≠ premium paid** — put notional is the strike price × contract size, NOT the cash at risk. Cash premium is typically 2-10% of notional depending on tenor and moneyness
- **Compiled summary from user message** — original source is SEC 13F filing, but the wiki content was assembled from a summary not direct filing parse. **Verify specific notional figures against EDGAR before any sized position-taking**
- **The fund's actual cash at risk is far lower than $13.7B "AUM" implies** — much of the put exposure is option premium not stock; the long book is approximately the cash at work
- **Not investment advice.** The wiki documents the fund's thesis as a tradeable view; agreeing with the trades is a separate decision

## Confidence assignment

**Overall: MEDIUM-HIGH** — High confidence on the structural pattern and major position categories (13F filings are mandatory and audited); medium confidence on specific dollar figures pending EDGAR verification of the original filing; medium confidence on the interpretation of newly initiated small positions (SHAZ, HIVE, TE) where size is not granularly disclosed.
