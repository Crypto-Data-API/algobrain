---
title: "Lost or Stolen Crypto — Australian Tax Treatment"
type: concept
created: 2026-05-30
updated: 2026-06-21
status: excellent
tags: [australia, tax, crypto, regulation, risk-management]
aliases: ["Lost Crypto ATO", "Stolen Crypto Tax", "Inaccessible Wallet Tax", "Lost Private Key Tax", "Crypto Loss of Access Tax"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: intermediate
prerequisites: ["[[cryptocurrency-tax-australia]]", "[[australian-investor-tax]]"]
related:
  - "[[cryptocurrency-tax-australia]]"
  - "[[reporting-obligations-australia]]"
  - "[[self-custody-tax-evidence-checklist]]"
  - "[[tax-loss-harvesting-australia]]"
  - "[[capital-gains]]"
  - "[[itaa-1997-overview]]"
  - "[[australian-investor-tax]]"
---

> **Not tax advice.** Lost-crypto claims are factually fragile and heavily evidence-driven. The ATO has approved some claims and denied many. Confirm with a registered tax agent before lodging.

When a holder loses access to crypto held in self-custody — typically cold storage — the question is whether the loss can be claimed as a **capital loss** in the Australian tax return. The ATO's position is that **lost cryptocurrency can give rise to a CGT event** under s 104-20 (CGT event C1 — loss or destruction) if the asset is genuinely irrecoverable and the loss can be substantiated. The bar is high; the evidence requirements are specific; and the line between "lost" and "stolen" matters because different CGT events apply. This page covers the law, the ATO's published position, the evidence standard, and how the claim is reported.

> **Not tax or legal advice.** Thresholds, amendment periods and CGT-event mechanics described below are indicative of the published ATO position and may change. Confirm the current position with the ATO or a registered tax agent before lodging.

## The legal framework

Under [[itaa-1997-overview|ITAA 1997]]:

- **Crypto is a CGT asset** — confirmed in TD 2014/26 and reinforced in ATO web guidance. Each disposal triggers a CGT event with the gain or loss computed on cost-base mechanics.
- **CGT event C1** (s 104-20) — happens when a CGT asset you own is **lost or destroyed**. Time of event: when you first received compensation or, if no compensation, when the loss/destruction occurred. Capital loss = reduced cost base − any capital proceeds (often zero for lost crypto).
- **CGT event C2** (s 104-25) — happens when ownership of an intangible CGT asset ends (cancellation, abandonment, release, surrender). The ATO has generally applied **C2** rather than C1 to **stolen crypto** in published guidance, on the basis that ownership of the rights ends rather than the underlying asset being physically destroyed.
- **Personal use asset exemption** (s 108-20) — discussed below; effectively **does not apply** to investment cold-storage holdings.

### CGT event C1 vs C2 — mechanics side by side

| Dimension | CGT event C1 (s 104-20) | CGT event C2 (s 104-25) |
|---|---|---|
| Trigger | Asset **lost or destroyed** | Ownership of an intangible asset **ends** (cancellation, abandonment, surrender, release) |
| Typical crypto fact pattern | Lost/forgotten seed phrase, dead hardware wallet | Stolen funds drained on-chain, account takeover |
| Time of the event | When compensation first received, else when loss/destruction occurred | When the contract/act ending ownership happens, else when ownership otherwise ends |
| Capital proceeds | Usually nil (any insurance/recovery counts) | Usually nil (any recovery counts) |
| Capital loss | Reduced cost base − capital proceeds | Reduced cost base − capital proceeds |
| Why it matters | C1 hinges on proving the asset is *gone*; C2 hinges on proving *ownership/control* ended | Same loss quantum, different evidentiary narrative |

The dollar outcome (a capital loss equal to cost base less any recovery) is usually identical between C1 and C2 — the distinction matters for **which narrative and evidence the ATO expects**, not the size of the loss.

Capital losses computed this way:
- Offset against current-year capital gains first
- Excess carried forward indefinitely against future capital gains
- Cannot offset salary, dividends, or other ordinary income

## The "lost vs stolen" distinction

The ATO treats these slightly differently in practice, though both can result in a capital loss claim:

| Scenario | CGT event | Typical evidence focus | Notes |
|---|---|---|---|
| Lost seed phrase, no backup | C1 (s 104-20) | Proof of original control + irrecoverability | Hardest to prove — must show you can't simply remember the phrase |
| Damaged hardware wallet, seed never backed up | C1 | Device receipts + irrecoverability of seed | Some cases successful with strong evidence |
| Forgotten password to encrypted backup | C1 | Proof of attempts + technical irrecoverability | Burden of proof on holder |
| Stolen hardware wallet with seed | C2 typically | Police report + chain trail showing drain | Treated as loss of rights when assets moved out |
| Wallet drained by phishing/malware | C2 typically | Police / cybercrime report + on-chain forensics | Common; ATO has approved these with evidence |
| Sent to wrong address (irretrievable) | C1 or C2 (case-by-case) | Transaction ID + proof recipient is unrecoverable | Hard if the recipient address simply hasn't moved |
| Exchange insolvency (FTX, Mt. Gox, etc.) | Different framework — bankruptcy claim CGT | Claim value, distributions | See [[bankruptcy-claim-arbitrage]] for general pattern |

The key practical difference: **stolen crypto is generally easier to evidence** because the theft is a discrete documented event with police involvement, while **"I lost my seed phrase" is one of the hardest claims to substantiate** because it relies on negative evidence (you can't prove the seed isn't somewhere recoverable).

## ATO evidence requirements

The ATO's published web guidance on lost or stolen crypto lists the evidence the Commissioner expects. The holder must establish ownership at the time of loss and the irrecoverability of the asset. Minimum documentary set:

### Establishing ownership and cost base
- **Date you acquired the private key / wallet** — wallet generation timestamp, exchange withdrawal confirmation, hardware wallet first-use date
- **The wallet address(es)** — public addresses, xpub for HD wallets
- **Cost incurred to acquire the crypto** — original AUD purchase value, exchange records, on-ramp receipts
- **Amount of crypto** in the wallet at the time of loss
- **Hardware wallet purchase records** — receipt with serial number, blockchain trail of first transactions to the device
- **Transactions linked to your identity** — exchange-to-wallet withdrawal records, KYC-tied transactions

### Establishing irrecoverability
- **Statement of how the loss occurred** — written narrative
- **Statutory declaration** — sworn statement of facts
- **Date you lost the private key** or otherwise lost control
- **Evidence of recovery attempts** — communications with hardware wallet manufacturer, password-recovery service receipts, professional forensic recovery attempts
- **Independent corroboration where available** — witness statements, photographs, repair records

### Additional for stolen crypto
- **Police report** with case number — lodged contemporaneously
- **Cybercrime report** if applicable (ACSC ReportCyber, Scamwatch)
- **On-chain forensic trace** showing the assets moved from your wallet to addresses you do not control
- **Exchange communications** if the theft involved an account takeover

### What the ATO regards as weak evidence
- Self-prepared statements with no corroboration
- Claims made years after the alleged loss with no contemporaneous record
- Lost-access claims for wallets with no documented prior history
- Claims where the on-chain record is inconsistent with the narrative
- Round-number losses without supporting acquisition records

## The personal use asset trap (s 108-20)

A common misconception: that small crypto holdings might qualify for the **personal use asset exemption** under s 108-20, which would exempt them from CGT entirely.

The exemption applies to assets used or kept **mainly for personal use or enjoyment** and acquired for **less than $10,000**. ATO guidance is explicit that:

- Crypto held as an **investment** is NOT a personal use asset, regardless of value
- Crypto in cold storage is essentially always investment, not personal use
- Even crypto used to purchase consumer goods is only a personal use asset if acquired and held for that immediate purpose
- The exemption is rarely available in practice

**Practical implication**: do not attempt to claim cold-storage losses as personal-use exempt. They are CGT assets; the loss (if substantiated) is a capital loss claimable under C1 or C2.

## How to report the claim

The capital loss is reported in the **CGT schedule** of the individual or entity tax return:

### Individuals (myTax / paper return)
1. In the CGT section, declare the CGT event (C1 or C2) for the relevant income year
2. Cost base: original AUD cost of the crypto (purchase price + on-ramp fees + any inclusions per s 110-25)
3. Capital proceeds: zero in most lost-crypto cases (or any insurance/exchange recovery if applicable)
4. Capital loss: cost base − capital proceeds
5. Offset against other capital gains in the year; carry forward excess

### Trusts, companies, SMSFs
Same mechanical treatment, with entity-specific overlays:
- [[smsf|SMSFs]]: capital loss offsets fund capital gains; carried forward at fund level. See [[smsf-trading-tax-treatment]].
- Companies: no CGT discount; loss carry-forward subject to continuity-of-ownership / same-business tests under Div 165
- Trusts: trust loss rules in Div 266 may quarantine the loss

### Year of the CGT event
The loss is claimed in the year the CGT event happened — typically the year you became aware the asset was irrecoverable. Late-discovered losses can be amended into earlier years subject to amendment-period limits (indicatively 2 years for most individuals, 4 years for more complex affairs — confirm the period that applies to you).

## Worked example (illustrative figures only)

> Numbers below are **illustrative**, not advice. They show the mechanics, not a real ruling outcome.

A holder buys 1 BTC for **A$30,000** (including on-ramp fees) in a self-custody hardware wallet, documents the acquisition, then loses the seed phrase after a house move two years later. They engage a recovery service (unsuccessful), lodge a statutory declaration, and retain the on-chain history showing no movement since the wallet was funded.

| Line | Amount (A$) | Note |
|---|---|---|
| Reduced cost base | 30,000 | Purchase price + on-ramp fees (s 110-25 inclusions) |
| Capital proceeds | 0 | No recovery, no insurance |
| **Capital loss (CGT event C1)** | **30,000** | Carried forward if no current-year gains |

If the same holder had instead been **drained by phishing** and filed a contemporaneous police/ReportCyber case with an on-chain trace to addresses they do not control, the analysis is materially the same quantum but framed as **CGT event C2** with theft evidence. The capital loss only offsets capital gains — never salary, dividends or other ordinary income (see [[australian-investor-tax]]).

## Substantiation decision flow

1. **Can you establish prior ownership and cost base?** If not, the claim almost always fails — stop and reconstruct records (exchange CSVs, KYC withdrawals, hardware wallet receipts). See [[self-custody-tax-evidence-checklist]].
2. **Is the asset genuinely irrecoverable?** Document recovery attempts; an asset you could plausibly still access is not "lost".
3. **Lost or stolen?** Lost → C1 narrative (irrecoverability). Stolen → C2 narrative (police/ReportCyber + on-chain forensics).
4. **Is the on-chain record consistent with the narrative?** Any post-loss movement undermines the claim.
5. **Within amendment period?** Claim in the year of the CGT event; amend earlier years only within the applicable amendment window.

## Realistic outcomes — what gets approved, what gets refused

Based on the pattern of ATO private rulings and edited advice:

### Likely approved (with strong evidence)
- Stolen crypto with contemporaneous police report and on-chain trace
- Hardware wallet failure with manufacturer correspondence + clear acquisition history
- Documented exchange hack where the holder's allocation is verifiable
- Drained-by-phishing cases with cybercrime report + forensic chain analysis

### Often refused
- "I lost my seed phrase" claims without contemporaneous documentation
- Lost-access claims for wallets with no transaction history establishing prior ownership
- Round-number write-offs with no acquisition records
- Stale claims (3+ years after the alleged loss) without contemporaneous records
- Claims where on-chain activity post-dates the alleged loss (suggesting the holder did retain access)

The pattern: **the more contemporaneous and independent the evidence, the higher the approval probability**. Self-prepared narratives years after the fact rarely succeed.

## Strategic implications

1. **Document acquisition aggressively at the time of purchase.** The hardest evidence to produce after a loss is the acquisition record. See [[self-custody-tax-evidence-checklist]].
2. **Treat security and tax evidence as the same workflow.** Hardware wallet receipts, address derivation records, and on-chain history are *both* security-relevant *and* tax-evidence.
3. **Report theft immediately.** A police report dated within days of the theft is far more persuasive than one filed weeks later.
4. **Consider insurance for material holdings.** Some specialist crypto custodians and DeFi insurance protocols offer cover. Insurance recovery affects the capital proceeds in the CGT calculation.
5. **Don't conflate "lost" with "want to write off."** The ATO is alert to taxpayers using "lost crypto" claims to crystallise paper losses on holdings they still control. Misrepresentation has fraud consequences.

## Interaction with other crypto-tax events

- **Loss claim does not offset ordinary income.** Even if the holder is a [[trader-vs-investor-classification-au|trader]] on revenue account for some activity, a lost-crypto capital loss is on capital account
- **Cannot use lost crypto to satisfy [[non-commercial-losses-div-35|Div 35]] exception tests.** Lost crypto is not "assessable income from the activity"
- **5-year record retention** still applies to all supporting documents (see [[reporting-obligations-australia]])
- **Wash sale rules** are not directly relevant since lost crypto is genuinely disposed of (cannot be re-acquired identically), but the ATO is alert to schemes where "loss" claims coincide with re-purchase of equivalent crypto in a related account

## Common mistakes and ATO red flags

| Mistake | Why it fails | Fix |
|---|---|---|
| Claiming a "lost" wallet you still control | On-chain movement post-loss is visible to the ATO; constitutes misrepresentation | Only claim genuinely irrecoverable assets |
| No acquisition record | Cannot establish cost base; loss is unquantifiable | Reconstruct from exchange/KYC records before lodging |
| Round-number write-off | Pattern-matches to fabricated claims | Tie the figure to actual acquisition documents |
| Stale claim filed years later | No contemporaneous evidence; low approval rate | Document and report at the time of loss |
| Treating it as a personal-use asset | Investment cold storage is not personal-use under s 108-20 | Claim as a capital loss under C1/C2 |
| Offsetting against salary | Capital losses cannot offset ordinary income | Offset against capital gains; carry forward excess |

## Source notes

Written from public ATO guidance on crypto asset investments (published web pages), TD 2014/26, ITAA 1997 s 104-20 / s 104-25 / s 108-20, and the pattern of publicly available ATO private rulings on lost and stolen crypto. Specific Perplexity research saved at `raw/articles/2026-04-22-gap-finder-losing-access-to-a-cold-storage-crypto-h.md`. **This is not tax or legal advice. Confirm the current ATO position and seek professional advice from a registered tax agent before lodging any lost-crypto loss claim.**

## Related

- [[self-custody-tax-evidence-checklist]] — pre-loss documentation guide
- [[cryptocurrency-tax-australia]] — broader crypto tax framework
- [[reporting-obligations-australia]] — general reporting and record retention
- [[tax-loss-harvesting-australia]] — for liquid disposals (different scenario)
- [[capital-gains]] — general CGT concept
- [[itaa-1997-overview]] — broader ITAA index
- [[australian-investor-tax]] — broader investor tax framework
- [[smsf-trading-tax-treatment]] — SMSF-specific loss handling
