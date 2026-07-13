---
title: "Cum-Ex Dividend Stripping (ILLEGAL — Historical Reference Only)"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, history, regulation, tax, fraud, dividend, europe, illegal]
aliases: ["Cum-Ex", "Cum/Ex Trades", "Dividend Stripping", "Dividend Arbitrage (Criminal Variant)"]
strategy_type: hybrid
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: retired
edge_source: [structural]
edge_mechanism: "Exploited a loophole in German (and other European) dividend-tax refund systems so that two or more parties could claim a tax refund on a single dividend payment -- a fraud, not a legitimate edge. Included here solely as a historical case study in structural edge gone criminal."
data_required: [corporate-actions-calendar, tax-treaty-data, repo-financing]
min_capital_usd: 0
capacity_usd: 0
crowding_risk: high
expected_sharpe: 0
expected_max_drawdown: 1.0
breakeven_cost_bps: 0
decay_evidence: "Closed by German Finance Ministry in 2012; criminal prosecutions ongoing through 2020s. BGH (German Federal Court) ruled in 2021 that cum-ex trades were always criminal tax evasion."
related: ["[[arbitrage]]", "[[dividend-capture]]", "[[regulation]]", "[[failure-modes]]", "[[history]]", "[[tax-arbitrage]]", "[[edge-taxonomy]]", "[[ex-dividend-date]]", "[[regulatory-arbitrage]]", "[[limits-to-arbitrage]]"]
---

# Cum-Ex Dividend Stripping

> **WARNING — ILLEGAL AND CRIMINAL.** Cum-ex trades were not legitimate arbitrage. German, Danish, Belgian, Austrian, and other European courts have ruled them to be criminal tax fraud. This page exists solely as a historical case study to illustrate how a structural tax loophole was exploited on an industrial scale, and the regulatory and criminal consequences that followed. **Do not attempt to replicate any element of this strategy.** The Rules and Implementation sections below describe how the scheme operated historically; they are documentation, not actionable guidance. Modern equivalents are prosecuted as aggravated tax evasion, money laundering, and organized crime.

**Cum-ex** (from Latin "with-without") trades were a family of coordinated share-transfer schemes executed around the [[ex-dividend-date]] of European stocks, designed to produce multiple tax-refund certificates for a single dividend payment. In the German system between roughly **2001 and 2012**, the tax-refund administrator could not distinguish between the true economic owner of shares on the dividend record date and a short-seller's buyer who held only a confused settlement claim. Both would receive certificates of dividend tax paid, and both would apply for refunds. The state paid out refunds on dividends it had collected only once. Estimated losses to the German treasury are most commonly cited at around **€31.8 billion** (academic estimate by Christoph Spengel, University of Mannheim; higher Bundestag-cited figures of ~€36 billion also appear), with cross-European losses estimated at **€55.2 billion** in the 2018 *CumEx Files* investigation and revised upward to roughly **€150 billion** in the 2021 update once cum-cum variants were included (Correctiv, Die Zeit, and 19 other European outlets).

### Cum-ex vs cum-cum vs legitimate dividend strategies

Because the terminology is widely confused in the press, the table below classifies the family. Only the bottom rows are legal; the top two are the subject of the criminal prosecutions documented on this page.

| Scheme | Mechanism (in one line) | Legal status | Notes |
|---|---|---|---|
| **Cum-ex** | Multiple refund certificates generated for *one* withholding via short-sale-and-delayed-settlement circles | **Criminal fraud** (BGH 2021) | The subject of this page; refund > tax remitted |
| **Cum-cum** | Temporary transfer of shares to a domestic/treaty-favored holder around ex-date to dodge withholding | **Largely disallowed / abusive** | Refund = tax remitted but obtained by sham ownership; reclassified, billions reclaimed |
| [[dividend-capture]] | Buy cum-dividend, sell shortly after ex-date | **Legal** | Marginal after tax/costs; no duplicate refund |
| [[dividend-arbitrage]] | Option-based dividend strategies respecting one-dividend-one-refund | **Legal** | Prices early-exercise around ex-date |
| [[put-call-parity-arbitrage]] | Locked-box conversions/reversals around dividend weeks | **Legal** | Enforces a no-arbitrage identity, not a tax claim |

The bright line: a legitimate dividend strategy never causes the state to refund tax it did not collect. Cum-ex crossed that line; cum-cum bent it through artificial ownership transfers. See [[regulatory-arbitrage]] for the broader category this masqueraded as, and [[limits-to-arbitrage]] for why a control failure can persist for a decade before detection.

## Edge source

Originally marketed to participants as a **structural** edge exploiting a tax-administration inefficiency — the classic profile of [[regulatory-arbitrage]] (see [[edge-taxonomy]]). In reality there was no edge: the trades only produced returns because the refund process failed to verify that each claimed refund corresponded to tax actually remitted. The Bundesgerichtshof (German Federal Court of Justice) ruled in July 2021 (case **1 StR 519/20**) that the trades **never constituted legitimate tax optimization** and that participants knew or should have known they were claiming refunds on tax that was never paid. The "structural edge" was reclassified retroactively as simple fraud.

## Why this edge exists

The scheme worked because three overlapping structural features of the German system (with analogues in Denmark, Austria, and Belgium) let more than one party document ownership of the same dividend:

1. **Two-day settlement (T+2)** meant a buyer purchasing shares cum-dividend immediately before the ex-date could receive a dividend *replacement payment* via short-sale mechanics rather than the actual dividend — yet still be issued a tax certificate.
2. **Separate tax-refund certificates** were issued by custodian banks (not the issuer) based on dividend receipts. In coordinated circular trades, multiple custodians issued certificates against the same single dividend.
3. **No cross-checking** existed between the Federal Central Tax Office and the issuer's actual withholding-tax remittance until the 2012 patch.

**Who was on the other side, and why they kept losing:** the counterparty was the German taxpayer. Refunds were paid from general revenues, and no automated control reconciled refund claims against tax collected. The "losers" — the tax authority and the public — kept losing precisely because the loss was diffuse, slow to detect, and buried in a high-volume administrative process that nobody audited end-to-end. Participating banks, funds, and individuals charged fees of typically **40-60% of the refund amount**, splitting stolen public money among the circle.

## Null hypothesis

Under an honest interpretation of the tax code, only the single economic owner on the record date receives a refund, and no arbitrage exists. If the refund administration had reconciled every refund claim against tax actually remitted, the entire profit would have vanished. Any "backtest" showing positive returns was measuring the probability that the fraud went undetected — not a market inefficiency. The null hypothesis (no edge) is the *correct* description of the legal world; the scheme's apparent returns were the signature of a control failure, not alpha.

## Rules (historical description — NOT actionable)

The canonical cum-ex circle involved at least three coordinated parties acting around a stock's ex-dividend date:

- **Entry (cum-dividend window):** a short seller (Party A) sold shares *cum-dividend* shortly before the ex-date to a buyer (Party B), with settlement deliberately delayed until after the ex-date. A separate true owner (Party C) held the shares across the record date.
- **The duplication:** Party C received the actual dividend net of 25% withholding tax and an official tax certificate. After the ex-date, Party B received the shares ex-dividend plus a *dividend-replacement payment* from the short seller's custodian — and Party B's custodian **also** issued a tax certificate, because settlement treated the replacement payment as a taxed dividend.
- **Exit (refund claim):** both Party B and Party C filed for refunds of the 25% withholding tax. The treasury paid two refunds against one dividend collected.
- **Position sizing:** participants scaled by borrowing large blocks of high-dividend German blue chips just before the ex-date, sizing positions to the largest refund that could be claimed without triggering manual review. In aggressive variants (and the related **cum-cum** structures), dozens of shell vehicles traded the same shares in coordinated circles across multiple jurisdictions, generating many refund certificates per dividend.
- **The split:** the circle — often coordinated by a single investment bank, pension fund, or family office acting through affiliates — divided the stolen refund per pre-agreed fee schedule.

## Implementation pseudocode

```text
# HISTORICAL DOCUMENTATION ONLY — describes a criminal scheme, do not execute.
for stock in high_dividend_german_bluechips:
    ex_date = stock.ex_dividend_date
    # Coordinated circle of affiliated parties A, B, C
    on (ex_date - 1):
        A.short_sell(stock, qty, settlement=ex_date + 2)   # cum-dividend, delayed settle
        B.buy_cum_dividend(stock, qty, from=A)
        C.hold(stock, qty across ex_date)                  # genuine owner
    on ex_date:
        C.receive(dividend * (1 - 0.25))                   # net dividend
        C.receive(tax_certificate)                         # legitimate certificate
    on (ex_date + 2):                                      # settlement after ex-date
        B.receive(shares_ex_dividend)
        B.receive(dividend_replacement_payment)            # from A's custodian
        B.receive(tax_certificate)                         # DUPLICATE certificate (the fraud)
        A.cover_short(market)
    # Two refund claims, one dividend collected:
    treasury.refund(B, 0.25 * dividend)                    # state pays twice
    treasury.refund(C, 0.25 * dividend)
    profit = 0.25 * dividend                               # stolen from public revenue
    split_among_circle(profit, fee_schedule=0.40..0.60)
```

## Indicators / data used

- **Corporate-actions calendar** — ex-dividend and record dates for high-dividend German blue chips (DAX constituents) to time the cum-dividend window.
- **Tax-treaty and withholding-tax data** — the 25% German withholding rate and refund-eligibility rules that the certificates exploited.
- **Repo / securities-lending financing** — to source the large share blocks borrowed and short-sold around the ex-date.
- **Custodian settlement mechanics** — knowledge of which custodians issued certificates on replacement payments was the operational core. None of these are market signals; they are the plumbing details that made the fraud executable.

## Example trade

A 2011-vintage structure (representative, drawn from prosecution reconstructions): a circle borrows €1 billion of a high-dividend DAX stock paying a €40 million gross dividend just before its ex-date. The 25% withholding is €10 million. Through the coordinated short-sale-and-delayed-settlement structure, two tax certificates are generated against that single €10 million withholding. Both holders file refunds; the treasury pays out **€20 million** while having collected only €10 million. The €10 million of net "profit" is pure stolen public money, split roughly 40-60% to the arranging bank and the remainder to the capital providers. Hundreds of such trades across multiple ex-dates and multiple shell entities scaled the scheme into the billions.

## Performance characteristics

There is no legitimate risk-adjusted return to report — the apparent "Sharpe" was a function of detection probability, not market risk. While undetected, participants experienced near-deterministic cash inflows (which is why frontmatter lists `expected_sharpe: 0` rather than a positive number — the realized risk is the binary, eventually-certain risk of criminal liability, not market variance). Once detection arrived, realized outcomes were catastrophic: full clawback of refunds plus interest, asset forfeiture frequently exceeding the individual's gain, and multi-year prison sentences. On a true risk-adjusted basis — including the (now-realized) tail of criminal prosecution and forfeiture — the strategy's expected value is **deeply negative**, consistent with `expected_max_drawdown: 1.0`. There is no realistic cost overlay that makes the scheme positive-EV; the dominant cost is criminal liability, which is unbounded.

## Capacity limits

Economically the scheme scaled to tens of billions of euros of refund claims before the control failure was closed — but this "capacity" was the capacity of a fraud to remain undetected, not legitimate market capacity. Frontmatter lists `capacity_usd: 0` because there is **no legitimate capacity**: every euro of capacity was a euro of theft from public revenue, and the larger the volume, the faster and more certain the eventual detection and prosecution.

## What kills this strategy

- **Regulatory closure of the loophole** — Germany patched the certificate-issuance process in 2012, after which the mechanism no longer generated duplicate certificates.
- **Cross-checking / reconciliation** — automated matching of refund claims against remitted withholding tax eliminates the edge entirely.
- **Investigative journalism and whistleblowers** — the *CumEx Files* and insider document leaks gave authorities the evidence to prosecute.
- **Judicial reclassification** — the 2021 BGH ruling that cum-ex was *always* criminal removed any "we thought it was legal" defense for the future.
- **The dominant failure mode is regulatory/legal risk** (see [[failure-modes]]): an edge that depends on a control failure dies the moment the control is fixed, and leaves participants exposed to retroactive liability.

## Kill criteria

This is a retired/illegal scheme; the "kill criteria" are the conditions under which it was — and is — terminally non-viable:

- **Loophole closed (binary):** as of the 2012 German patch and equivalent fixes in Denmark, Austria, and Belgium, the mechanism produces zero duplicate certificates. Edge = 0.
- **Statute of limitations still open:** aggravated cases carry up to a **20-year** limitation period; participants from 2006-2012 remained indictable into the 2026 horizon — i.e., the liability tail has not yet expired.
- **Expected value test:** with criminal penalty present and detection probability now effectively 1, expected value is unbounded-negative. Any deployment fails the most basic kill criterion (do not run a strategy whose downside is criminal conviction and forfeiture exceeding gains).

## Advantages

None legitimate. While undetected, the only "advantage" to participants was stolen public money. The sole legitimate benefit — to the state and to the study of market structure — is that exposing and closing the scheme plugged an estimated €5-10 billion/year hole in German public finances and drove reforms to tax-certificate verification across the EU.

## Disadvantages / Why not to do it

- It was always criminal, and unambiguously so after the 2021 BGH ruling.
- Criminal penalties exceed financial gain by orders of magnitude.
- The 20-year statute of limitations means participants from 2006-2012 were still being indicted in 2026.
- Reputational destruction; professional licenses revoked (lawyers, bankers, accountants).
- International extradition makes "offshore" havens unreliable — Sanjay Shah was extradited from the UAE to Denmark.
- Asset forfeiture typically recovers more than the individual earned, including personal assets.

## Cross-jurisdiction footprint

The same control failure — refund certificates issued without reconciliation against tax actually remitted — recurred across several European withholding-tax systems. The scheme migrated as each jurisdiction patched its rules. (Figures are widely cited estimates from the *CumEx Files* consortium and national prosecutors; treat as journalistic/academic estimates, not audited totals.)

| Jurisdiction | Approx. loss cited | Status of crackdown |
|---|---|---|
| Germany | ~€31.8bn (Spengel); higher figures cited | BGH 2021 ruled criminal; convictions and asset recovery ongoing |
| Denmark | ~DKK 12.7bn (the Sanjay Shah case) | Shah extradited from UAE 2023; trial and recovery proceedings |
| Belgium / Austria | Smaller but material | Loopholes closed; investigations followed Germany's lead |
| Cross-Europe (incl. cum-cum) | ~€55.2bn (2018) → ~€150bn (2021 update) | Multi-country investigations; reforms to certificate verification |

The pattern is a textbook regulatory failure mode: a diffuse, slow-to-detect leak in a high-volume administrative process, arbitraged industrially until journalism and whistleblowers forced reconciliation. See [[failure-modes]].

## Regulatory timeline

- **2001-2007:** scheme runs with increasing volume; early participants include Freshfields, Maple Bank, HypoVereinsbank (HVB), and Warburg.
- **2007:** tax lawyer Hanno Berger structures the most aggressive variants; internal warnings (Deutsche Bank "Sommer-Memo") flag the practice as unlawful.
- **2009:** Germany introduces a partial patch; volumes spike as participants rush the final windows.
- **2012:** loophole formally closed by the German Federal Ministry of Finance; later years use disputed cum-cum variants.
- **2016:** Bundestag Parliamentary Inquiry Committee established; Fabio De Masi leads questioning.
- **2018 (18 Oct):** ***CumEx Files*** published by Correctiv and 18 European media partners — exposé naming 130+ banks.
- **2020:** first criminal conviction (Bonn Regional Court) of two UK-based traders; court finds cum-ex was always criminal.
- **2021 (July):** German Federal Court of Justice (BGH) confirms in case 1 StR 519/20 that cum-ex is criminal tax evasion.
- **2022 (December):** Hanno Berger sentenced (Bonn Regional Court) to 8 years for aggravated tax evasion.
- **2023:** Sanjay Shah extradited from the UAE to Denmark on a DKK 12.7 billion fraud case.
- **2024-2026:** Warburg, HypoVereinsbank, and Maple Bank successor trustees continue asset-recovery litigation; an estimated several billion euros recovered to date against tens of billions stolen.

## Legitimate adjacent strategies

For traders interested in **legal** dividend-related strategies, see:

- [[dividend-capture]] — buying shares before ex-div and selling shortly after. Marginal economics after taxes and transaction costs, but legal.
- [[dividend-arbitrage]] — option-based dividend strategies that respect the one-dividend-one-refund principle.
- [[put-call-parity-arbitrage]] — locked-box trades around dividend weeks.
- [[merger-arbitrage]] — unrelated but in the "event-driven" family.

## Sources

- *CumEx Files* (Correctiv, 2018) — https://correctiv.org/top-stories/2018/10/18/the-cumex-files/
- BGH ruling 1 StR 519/20 (July 2021)
- Bundestag 4. Untersuchungsausschuss final report (2017)
- Oliver Schröm, *Die Cum-Ex-Files* (book, 2019)
- Christoph Spengel (University of Mannheim) loss estimates; coverage in *Die Zeit*, *Süddeutsche Zeitung*, *Financial Times*, *The Guardian*, *Deutsche Welle*
- DW, "Cum-ex tax scandal cost European treasuries €55 billion" (2018) — https://www.dw.com/en/cum-ex-tax-scandal-cost-european-treasuries-55-billion/a-45935370
- Verified via Perplexity (sonar), 2026-06-10: German treasury loss commonly cited ~€31.8bn (Spengel), cross-Europe ~€55.2bn (2018); BGH case 1 StR 519/20, July 2021 confirmed.

## Related

- [[arbitrage]] — parent concept (as a warning of how structural edge can cross into fraud)
- [[regulatory-arbitrage]] — the category this scheme masqueraded as
- [[dividend-capture]] — the legal cousin
- [[regulation]] — the force that killed this scheme
- [[tax-arbitrage]] — broader category (most forms of which are legal)
- [[ex-dividend-date]] — the corporate-action timing the scheme abused
- [[limits-to-arbitrage]] — why a control failure can persist for a decade
- [[failure-modes]] — canonical example of regulatory/legal failure mode
- [[history]] — historical context
- [[edge-taxonomy]] — methodology note
