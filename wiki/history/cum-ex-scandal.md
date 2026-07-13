---
title: "Cum-Ex / Cum-Cum Dividend Stripping Scandal"
type: news
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [history, stocks, regulation, arbitrage]
aliases: ["Cum-Ex", "Cum-Cum", "Dividend Stripping Scandal", "Cumex-Files", "Cum-Ex Scandal"]
event_date: 2018-10-18
markets_affected: [stocks]
impact: high
verified: true
sources_count: 6
related: ["[[regulatory-arbitrage]]", "[[tax-arbitrage]]", "[[hanno-berger]]", "[[sanjay-shah]]", "[[warburg-bank]]"]
---

> **This is a criminal tax fraud, not a strategy.** The cum-ex variant has been ruled **criminal tax evasion** by Germany's highest criminal court (BGH, July 2021); architects and operators have received multi-year prison sentences. This page documents the scandal for historical and risk-management context **only**. The mechanics described here are illegal and are presented to explain how the fraud worked and was prosecuted — not as anything to replicate. See [[regulatory-arbitrage]] and [[tax-arbitrage]] for the legitimate (and the illegitimate) boundaries.

The cum-ex / cum-cum scandal is the largest tax fraud in European history, estimated at over **EUR 55 billion** across Germany, Denmark, Belgium, France, Austria, Italy, Switzerland, and the Netherlands between roughly 2001 and 2012 -- with aftershocks still litigated into the 2020s. The scheme exploited a technical gap in European dividend-withholding-tax systems: by coordinating share trades around the dividend ex-date, participants produced two or more tax certificates ("Steuerbescheinigungen") for a single actual dividend, then claimed refunds on tax that had never been paid. The scandal was surfaced publicly in the 2018 "**CumEx-Files**" cross-border journalism project led by German nonprofit [[correctiv]], in partnership with *Die Zeit*, *Le Monde*, *The Guardian*, *Reuters*, and 15+ other outlets.

## Master Timeline

| Date | Event |
|------|-------|
| ~2000-2001 | Cum-cum and cum-ex execution begins at scale in Germany (per German loss estimates) |
| 2007 | German finance ministry first attempts to narrow the loophole (partial, ineffective) |
| 1 Jan 2012 | Germany amends the Income Tax Act (EStG); withholding shifts to the net-dividend payer, closing the cum-ex dual-certificate gap |
| 2012-2015 | [[sanjay-shah]] / [[solo-capital]] export the scheme to Denmark (SKAT) |
| ~2013 | Cologne prosecutor **Anne Brorhilker** establishes the central German cum-ex task force |
| 2016 | [[maple-bank]] fails after a EUR 450M cum-ex tax claim; first cum-cum narrowing in Germany |
| 18 Oct 2018 | [[correctiv]] + 19 outlets publish the **CumEx-Files** (EUR 55.2B EU-wide damage figure) |
| 2019 | [[deutsche-bank]] pays EUR 3.9M settlement |
| Mar 2020 | **Bonn Landgericht** — first criminal convictions; cum-ex ruled criminal tax evasion |
| 2020 | Germany extends statute of limitations for severe tax fraud to 25 years |
| 28 Jul 2021 | **German Federal Court of Justice (BGH), 1 StR 519/20** — upholds Bonn; confirms cum-ex is criminal tax fraud |
| 2021 | "CumEx-Files 2.0" extends investigation to cum-cum; cum-cum loophole narrowed again |
| 2022 | [[hanno-berger]] extradited from Switzerland; convicted in Wiesbaden (May) and Bonn (Dec) — 8 years aggregate |
| 2023 | Shah extradited to Denmark; **Dec 2023 Copenhagen** conviction — 12 years (longest to date) |
| 2024 | Brorhilker resigns citing political interference; Cologne caseload >1,700 suspects, 130 banks |

## Two Variants

### Cum-Ex (the stronger fraud)

"Cum-ex" ("with-without") trades involved short sales executed just before the dividend record date, with delivery settling just after. Because of legacy T+2 settlement mechanics in Germany and reliance on bank-issued tax certificates rather than central-authority records, **the same dividend tax credit could be claimed by multiple counterparties**: the original owner, the short seller's counterparty, and often the short seller themselves. A coordinated ring of long holders, short sellers, securities-lending desks, prime brokers, and custodian banks produced two or three certificates per actual dividend; each was redeemed against the German tax authority (Finanzamt) for a refund of a tax that had been paid only once (or in some cases not at all).

Simplified mechanics (German stock paying EUR 1.00 gross dividend, 26.375% withholding):

```
Day T-2  Party A sells short to Party B (cum-dividend -- "with")
Day T    Ex-dividend date; actual dividend of EUR 0.7363 net paid to record-date holder
Day T+2  Short delivery settles; B receives shares ex-dividend ("without")
         Short seller compensates B with a manufactured dividend
         Bank issues tax certificate to B AND to original record-date holder
Day T+X  B and original holder each claim refund of EUR 0.2638 from Finanzamt
         State has collected EUR 0.2638 once, refunded it twice -> net loss EUR 0.2638
```

Scale came from leverage, repeat execution, and the ability to run the same circular trades across dozens of German blue chips every April-June dividend season.

### Cum-Cum (weaker but far larger)

"Cum-cum" trades were simpler: a foreign holder who could not claim back German withholding tax (because their tax treaty did not provide for a full refund) would temporarily lend or repo the shares to a German institutional counterparty just before the record date. The German counterparty collected the dividend, claimed the refund domestically, and shared the proceeds with the foreigner via an inflated lending fee. The tax was paid once and refunded once -- but to a party not entitled to the refund under the spirit of the tax treaty. German authorities have argued this is tax evasion / aggressive avoidance rather than fraud; the legal boundary remains contested.

Estimated losses by variant:

| Variant | Period | Estimated Loss |
|---------|--------|----------------|
| Cum-ex | 2001-2012 | EUR ~10-12 billion (Germany) |
| Cum-cum | 2000-2015+ | EUR ~28-36 billion (Germany) |
| Cross-border (DK, FR, BE, AT, IT) | 2005-2015 | EUR ~10+ billion |
| **Total EU** | | **EUR 55+ billion** |

Denmark alone lost roughly **DKK 12.7 billion (~EUR 1.7 billion)** in a concentrated 2012-2015 episode largely tied to [[sanjay-shah]]'s [[solo-capital]].

## Key Architects and Participants

### Hanno Berger

German tax lawyer, formerly a senior Hessen tax official who *enforced* such rules before crossing over into private practice. [[hanno-berger]] became the acknowledged intellectual architect of the cum-ex structure as a partner at [[freshfields-bruckhaus-deringer]] and later at his own firm. He issued legal opinions ("Gutachten") to banks and trading firms blessing the scheme, fled to Switzerland when German prosecutors moved in, was extradited in 2022, and was convicted by a Wiesbaden court in May 2022 and a Bonn court in December 2022. Total sentence: **eight years** imprisonment.

### Sanjay Shah and Solo Capital

British hedge-fund principal who ran [[solo-capital|Solo Capital Partners]] in London. Shah exported the cum-ex logic to Denmark (2012-2015), where he and his network allegedly defrauded the Danish tax authority (SKAT) of roughly **EUR 1.7 billion (DKK 12.7 billion)**. Shah moved to Dubai, was arrested there in 2022, extradited to Denmark in 2023, and in December 2023 a Copenhagen court convicted him and sentenced him to **12 years** imprisonment -- the longest single sentence to date in the scandal.

### M.M. Warburg & Co.

Hamburg private bank [[warburg-bank]] was among the most heavily implicated German institutions. Former Warburg managers Christian Olearius and Max Warburg faced criminal investigations; Warburg itself was ordered in multiple civil rulings to repay roughly **EUR 176 million** to the German treasury. The bank's 2016-2017 contacts with then-Hamburg Mayor [[olaf-scholz]] over potential treasury clawbacks became a political scandal during Scholz's 2021-2025 chancellorship ("**Warburg affair**"), investigated by a Hamburg parliamentary committee.

### Global Bank Involvement

Investigations and lawsuits have implicated multiple tier-one banks as counterparties, custodians, or prime brokers in cum-ex chains:

| Institution | Role | Exposure |
|-------------|------|----------|
| [[deutsche-bank]] | Custodian, prime broker, lending | Paid EUR 3.9M settlement 2019; disclosed ongoing reviews |
| [[barclays]] | Prime brokerage in London | Paid ~GBP 0.5B to tax authorities (reported) |
| bank-of-america / Merrill Lynch | Prime brokerage, securities lending | Civil claims pending |
| morgan-stanley | Custody / lending | Civil claims pending |
| [[bnp-paribas]] | French angle (French dividend-stripping variants) | Paris investigation |
| [[maple-bank]] | German mid-tier | Failed 2016 from EUR 450M cum-ex tax claim |
| commerzbank | Counterparty | Provision taken 2017-2019 |
| [[hypovereinsbank]] (UniCredit DE) | Counterparty | Settled EUR 9.8M with German courts |

## Investigations and Trials

### Cologne (Koln) as Epicenter

The Cologne state prosecutor's office built the central German cum-ex task force under prosecutor **Anne Brorhilker** beginning ~2013. Cologne's Landgericht hosted most of the landmark trials, later handed to Bonn for some defendants.

### Landmark Rulings

- **March 2020 -- Bonn Landgericht**: First criminal convictions. Two former UK-based [[hypovereinsbank]] traders received suspended sentences; court ruled definitively that cum-ex was **criminal tax evasion**, not mere aggressive tax planning, closing the primary legal defense.
- **July 2021 -- German Federal Court of Justice (BGH)**: Upheld the Bonn ruling; confirmed cum-ex constitutes tax fraud under German criminal law.
- **2022-2023 -- Hanno Berger convictions**: Wiesbaden and Bonn courts (8 years aggregate).
- **December 2023 -- Copenhagen**: Sanjay Shah convicted, 12 years.
- **Ongoing**: dozens of cases at various stages; Cologne prosecutor's caseload exceeds 1,700 individual suspects and 130 banks as of 2024.

### The 2018 CumEx-Files Disclosure

On 18 October 2018, [[correctiv]] and 19 partner outlets published the "CumEx-Files" after a year-long cross-border investigation, putting the total EU damage figure at **EUR 55.2 billion** -- the first time the public understood the scandal's scale beyond Germany. A 2021 follow-up ("CumEx-Files 2.0") extended the investigation to cum-cum variants and raised the estimate further.

## Why the Gap Existed

- **Private banks issued tax certificates**: German law permitted custodian banks to issue the "Steuerbescheinigung" that the taxpayer presented for a refund. There was no central registry cross-checking that a given dividend's withholding had not already been refunded.
- **T+2 settlement ambiguity**: Legacy short-sale settlement on German equities made it possible for ownership-at-record-date to be disputed among multiple parties.
- **Gap closed 2012 (Germany)**: Bundestag amended the Income Tax Act (EStG) effective 1 January 2012, shifting withholding-tax obligations to the payer of the net dividend and eliminating the dual-certificate possibility for cum-ex. Cum-cum loopholes were narrowed in 2016 and again in 2021.
- **Cross-border coordination failure**: Even after Germany closed its gap, the same playbook worked in Denmark until 2015 and in smaller jurisdictions later.

## Connection to Broader Regulatory-Arbitrage Theme

Cum-ex is the archetypal [[regulatory-arbitrage]] case study: exploiting the seams between two regulatory systems (securities settlement on one hand, tax refund processing on the other) where neither system fully validated the other's output. It also sits at the intersection of [[tax-arbitrage]] and dividend-arbitrage -- mechanically identical to many legitimate dividend-capture strategies, with the single distinguishing feature that no net tax was actually paid.

| Feature | Legitimate dividend-capture / dividend-arbitrage | Cum-ex (illegal) | Cum-cum (contested) |
|---------|----------------------------------------------------------|------------------|---------------------|
| Tax actually paid | Yes, once; refund only if entitled | Once (or zero) | Once |
| Tax refunded | Once, to entitled party | **Two or three times** | Once, to a **non-entitled** party |
| Net effect on treasury | Neutral / legitimate | **Direct theft** of refunds | Avoidance of treaty-limited withholding |
| Legal status (Germany) | Legal | **Criminal tax fraud** (BGH 2021) | Evasion / aggressive avoidance (contested) |
| Distinguishing feature | Genuine economic ownership at record date | Manufactured duplicate certificates | Ownership transferred only to capture refund |

The scandal catalyzed:

- **EU-wide discussion of a withholding-tax one-stop-shop** (2023 "FASTER" directive proposal).
- **Enhanced T+1 settlement** moves in the U.S. (May 2024) and EU (October 2027 plan) partly justified on dividend-timing abuse grounds.
- **Reopening of statute of limitations in Germany** for severe tax fraud cases (2020 law extended limitations to 25 years).

## Notable Figures

| Name | Role | Outcome |
|------|------|---------|
| [[hanno-berger]] | Architect, tax lawyer | 8 years prison (2022) |
| [[sanjay-shah]] | Solo Capital founder | 12 years prison Denmark (2023) |
| Anne Brorhilker | Cologne chief prosecutor | Resigned 2024 citing political interference |
| Christian Olearius | Warburg co-owner | Multiple charges, health-related trial pauses |
| [[olaf-scholz]] | Hamburg mayor, then finance minister, then chancellor | Testified multiple times; parliamentary inquiry ongoing |
| Oliver Schroem / [[correctiv]] | Lead journalist | CumEx-Files publication 2018 |

## Lessons for Traders and Risk Managers

1. **"Legitimate until proven otherwise" is not a defense**: cum-ex participants relied on tax-lawyer opinions (Gutachten) that later proved worthless. Regulators eventually treated the entire structure as criminal regardless of the opinion chain.
2. **Regulatory arbitrage has a half-life**: the gap was obvious to practitioners by 2005 and closed by 2012, but civil and criminal exposure now extends decades past the original trades.
3. **Cross-border coordination is improving**: ESMA, DG TAXUD, and OECD have each set up information-sharing mechanisms specifically modelled on the cum-ex failure.
4. **Prime-broker counterparty screening**: banks that merely facilitated (custody, securities lending) are being held jointly liable in civil recovery suits.
5. **Dividend-capture strategies require enhanced diligence**: legitimate dividend-capture and dividend-arbitrage strategies now face heightened scrutiny across Europe.

## Glossary

| Term | Meaning |
|------|---------|
| **Cum-ex** | "With-without" — trades structured so the dividend is captured "with" then settled "without," generating duplicate tax certificates |
| **Cum-cum** | "With-with" — shares lent to a domestic party "with" the dividend to capture a refund the foreign owner could not claim |
| **Steuerbescheinigung** | German bank-issued tax certificate redeemed for a withholding-tax refund |
| **Finanzamt** | German local tax office that processed (and refunded) withholding tax |
| **SKAT** | Danish tax authority defrauded of ~DKK 12.7B in the Denmark episode |
| **Ex-date / record date** | The dividend cut-off dates the timing trades were built around |
| **Manufactured dividend** | A compensating payment the short seller pays the buyer in lieu of the real dividend |
| **Gutachten** | Legal opinion (here, the tax-lawyer opinions that "blessed" the scheme and later proved worthless) |
| **BGH** | Bundesgerichtshof — Germany's Federal Court of Justice; its 2021 ruling settled cum-ex's criminality |

## Related

- [[regulatory-arbitrage]] -- the general category
- [[tax-arbitrage]] -- parent concept
- [[hanno-berger]] -- architect
- [[sanjay-shah]] -- Denmark ringleader
- [[warburg-bank]] -- implicated institution
- [[correctiv]] -- investigative publisher
- [[olaf-scholz]] -- politically connected figure
- [[ltcm-collapse-1998]] / [[archegos-blowup-2021]] -- companion "lessons in leverage / structure" case studies

## Sources

Primary documents and reporting underpinning this page (not yet ingested as formal source summaries; listed here as the citation base):

- **CumEx-Files (October 18, 2018)** — [[correctiv]] and 19 partner outlets (*Die Zeit*, *Le Monde*, *The Guardian*, *Reuters*, et al.). The cross-border investigation that established the EUR 55.2 billion EU-wide damage figure.
- **CumEx-Files 2.0 (2021)** — follow-up extending the investigation to the cum-cum variant and raising the loss estimate.
- **German Federal Court of Justice (BGH) ruling, 28 July 2021, 1 StR 519/20** — confirmed cum-ex constitutes criminal tax fraud under German law.
- **Bonn Landgericht judgment, March 2020** — first criminal convictions (former HypoVereinsbank traders); ruled cum-ex was criminal tax evasion, not aggressive planning.
- **Copenhagen City Court judgment, December 2023** — convicted Sanjay Shah, 12-year sentence (longest in the scandal to date).
- **Wiesbaden / Bonn Landgericht Hanno Berger judgments, 2022** — eight-year aggregate sentence for the scheme's architect.
