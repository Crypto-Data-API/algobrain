---
title: "Self-Custody Crypto Tax-Evidence Checklist"
type: concept
created: 2026-05-30
updated: 2026-06-21
status: excellent
tags: [australia, tax, crypto, risk-management, education]
aliases: ["Crypto Self-Custody Evidence", "Cold Storage Tax Records", "Crypto Loss Claim Documentation", "Pre-Loss Documentation Crypto"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: intermediate
prerequisites: ["[[cryptocurrency-tax-australia]]", "[[lost-or-stolen-crypto-au-tax]]"]
related:
  - "[[lost-or-stolen-crypto-au-tax]]"
  - "[[cryptocurrency-tax-australia]]"
  - "[[reporting-obligations-australia]]"
  - "[[capital-gains]]"
  - "[[itaa-1997-overview]]"
---

> **Not tax advice.** This is an operational checklist intended to make any future tax position defensible. Confirm specific evidence requirements with a registered tax agent.

A successful lost or stolen crypto tax claim — see [[lost-or-stolen-crypto-au-tax]] — depends almost entirely on **contemporaneous evidence assembled before the loss occurred**. After-the-fact narratives rarely succeed; pre-loss documentation routinely does. This page is the operational checklist: what records to create, how to store them, how to refresh them, and what to do immediately if loss does occur. It is written for Australian self-custody holders but the underlying principles apply broadly.

## Why this matters

The ATO's evidence bar for lost-crypto claims is high and biased toward independent contemporaneous records. The holder must be able to establish, with documentation:

1. **What was acquired** (asset, amount, date, AUD cost)
2. **That the holder controlled the relevant wallet** (chain of custody)
3. **What happened** (mechanism of loss)
4. **That recovery is genuinely impossible** (negative evidence)

A taxpayer who produced these records two years after the loss generally fails. A taxpayer who can point to a folder of receipts, signed declarations, and on-chain confirmations dated to the acquisition and to the loss event will generally succeed. The cost of the discipline is low; the cost of failing the evidence test is the entire loss claim.

## The four document classes

The evidence package is built in four classes, each tied to a different moment in the asset's life. The point of the framework is that the hardest evidence to fake — and the most persuasive to a tax authority — is **contemporaneous**: created at the time of the event, not reconstructed afterward. Build each class *when its trigger occurs*, not in a panic later.

| Class | Trigger | Cadence | Purpose | What it proves |
|---|---|---|---|---|
| **1 — Acquisition** | Every purchase | Per event | Cost base + ownership origin | What was acquired, when, for how much |
| **2 — Cold storage setup** | Wallet creation | Once per wallet | Chain of custody | The holder controls this wallet |
| **3 — Ongoing logs** | Continuous | Quarterly refresh | Position continuity | The asset stayed in custody over time |
| **4 — Loss event** | If loss occurs | Immediately (24–48h) | Mechanism + irrecoverability | What happened and that recovery is impossible |

The four map directly onto the four things the holder must establish (see [Why this matters](#why-this-matters)): Class 1 → *what was acquired*; Class 2 → *control of the wallet*; Class 4 → *what happened*; Classes 3+4 together → *recovery is genuinely impossible*.

### Class 1: Acquisition records (do this on every purchase)

For every crypto acquisition that ever enters self-custody, preserve:

- [ ] **Exchange purchase confirmation** (CSV export, screenshot, email)
- [ ] **AUD value at time of acquisition** (exchange rate, fiat-equivalent — needed for cost base)
- [ ] **Transaction hash for the withdrawal from exchange to self-custody wallet**
- [ ] **Receiving wallet address** (the cold-storage public address)
- [ ] **Date and time** of withdrawal
- [ ] **Exchange KYC tier** at the time (links the withdrawal to your identity)
- [ ] **Network fees paid** (additional cost base element under s 110-25)
- [ ] **Source of funds** if relevant for AML purposes

Store as one file per acquisition, named `YYYY-MM-DD_acquisition_<asset>_<exchange>.pdf` or similar.

### Class 2: Cold storage setup records (do this when wallet is created)

When a hardware wallet, paper wallet, or other cold-storage device is first set up:

- [ ] **Hardware wallet purchase receipt** with date, vendor, model, **serial number**
- [ ] **Photo of unboxing** showing tamper-evident packaging (security-relevant *and* tax-relevant)
- [ ] **Wallet generation date** (firmware logs, hardware wallet info screen photo)
- [ ] **First test transaction** — small amount in, small amount out, both transaction hashes preserved
- [ ] **Derivation path** used (BIP-44, BIP-49, BIP-84 etc. for HD wallets)
- [ ] **xpub or public address list** (NEVER seed phrase) for chain monitoring
- [ ] **Seed backup method documentation** (without recording the seed itself):
  - Type of backup (paper, metal plate, encrypted file, Shamir shares)
  - Physical location(s) of backup(s)
  - Number of copies
  - Backup creation date
  - Witness statement if applicable

The seed phrase itself never goes in any digital record. The *fact* that a backup was created on a given date and stored in a given way does.

### Class 3: Ongoing transaction logs (refresh quarterly)

Maintain a running record of all activity in/out of cold storage:

- [ ] **Transaction journal** — date, hash, direction, amount, counterparty (if known), AUD value
- [ ] **xpub-derived address list** updated as new addresses are used
- [ ] **Blockchain export** — periodic (quarterly) export of full address history from a block explorer
- [ ] **Balance attestations** — annual signed statement of the position
- [ ] **Hardware wallet firmware update logs** with dates
- [ ] **Any security incidents** (suspected compromise, lost backup copy, etc.) even if not loss events

The transaction journal serves a second purpose: it is the basis for the annual capital-gains computation if any disposals occurred.

### Class 4: Loss event records (assemble immediately if loss occurs)

If access is lost or assets are stolen:

- [ ] **Date and time of discovery** of the loss
- [ ] **Written narrative** of how the loss occurred, signed and dated **same day**
- [ ] **Statutory declaration** sworn before an authorised witness (JP, lawyer, pharmacist etc.) **within days**
- [ ] **For theft**: police report with case number, lodged **immediately**
- [ ] **For cybercrime**: ACSC ReportCyber report and Scamwatch report
- [ ] **Hardware wallet manufacturer communication** if device failure (correspondence chain)
- [ ] **Recovery attempt records** — every attempt documented with date and outcome
- [ ] **Independent corroboration** — witness statements from anyone with knowledge of the loss
- [ ] **Final on-chain state** — block explorer snapshot showing wallet balance at last access and at present

The 24–48 hours after loss discovery is the highest-leverage documentation window. Contemporaneous statements made then are dramatically more persuasive than retrospective ones.

## Storage architecture

The records must themselves survive long enough to be produced years later. Recommended:

| Layer | Content | Storage |
|---|---|---|
| **Primary** | Original receipts, photos, transaction logs | Encrypted cloud (Proton Drive, iCloud encrypted, etc.) |
| **Secondary** | Same content | Physical secure storage (home safe, deposit box) |
| **Tertiary** | Key documents only | Trusted family member or legal counsel |
| **Notarised** | Statutory declarations and signed narratives | Lawyer's file or court depository |

The five-year minimum retention rule (see [[reporting-obligations-australia]]) applies to all tax records from the year of lodgement. For potential lost-crypto claims, retention should extend until the claim is fully accepted (potentially years).

## Annual review checklist

Once per year, ideally before EOFY (30 June):

- [ ] Refresh exchange CSV exports for the financial year
- [ ] Compute AUD-at-acquisition for any new positions
- [ ] Reconcile cold-storage balances against the transaction journal
- [ ] Confirm hardware wallet still functional (sign a test transaction)
- [ ] Verify backup integrity (without exposing seed — use a non-destructive recovery test)
- [ ] Update xpub-derived address monitoring
- [ ] Refresh balance attestation
- [ ] Update binding death benefit / inheritance instructions (separate document)
- [ ] Check witness availability for any future statutory declarations

The annual review is also when the evidence package gets backed up to all storage layers.

## Inheritance and succession

A material number of "lost access" cases are actually **succession failures** — the holder died or became incapacitated without leaving recoverable instructions. Tax-wise, this is its own category:

- The crypto becomes part of the estate
- The executor's job is to establish ownership, value, and tax basis
- Without records, the executor faces the same evidence problem as a living holder claiming a loss
- Estate-level capital losses can be claimed where recovery is genuinely impossible

**Documentation for executors should be assembled now**, not deferred:

- Sealed letter of instruction held by lawyer (separate from will)
- Sufficient information for a trusted executor to locate (but not necessarily access) the wallet
- Schedule of holdings with cost bases
- Cross-reference to which documents prove what

This is a security/operational issue first; the tax dimension follows.

## What to do immediately if loss occurs

Within 24 hours of discovering loss:

1. **Write the narrative** — date, time, what happened, signed
2. **Snapshot the chain** — block explorer image of current state
3. **Lodge police report** if theft
4. **Notify hardware wallet manufacturer** if device failure
5. **Begin statutory declaration** process (book the witness)
6. **Notify your tax agent** — they will guide subsequent steps

Within 7 days:

1. **Complete statutory declaration** before authorised witness
2. **Compile evidence package** from Classes 1–3 records (already assembled, just retrieve)
3. **Document recovery attempts** so far
4. **Decide on professional recovery services** if applicable

Within 30 days:

1. **Determine the income year** in which the loss should be reported
2. **Prepare the CGT schedule entry** — see [[lost-or-stolen-crypto-au-tax]]
3. **Consider a private ruling application** for material claims
4. **Maintain the evidence file** for at least 5 years post-lodgement

## Common evidence failures

The pattern from public ATO rulings:

| Failure | Why it kills the claim |
|---|---|
| No acquisition record | Cannot prove cost base or ownership |
| Acquisition record but no transfer to self-custody | Cannot prove the crypto ever left the exchange |
| Self-custody transfer record but no wallet generation evidence | Cannot link the wallet to the holder personally |
| Narrative written years after the alleged loss | ATO discounts retrospective statements |
| Statutory declaration but no contemporaneous corroboration | Single self-serving document is weak |
| On-chain activity inconsistent with the narrative (e.g., post-loss transactions from the "lost" wallet) | Disproves the claim entirely |
| Round-number balance with no acquisition pattern | Suggests fabrication |
| Theft claim with no police report | ATO treats as unsubstantiated |
| Multiple lost-crypto claims from same holder | Pattern raises audit risk |

Each of these is solvable by following the four-class framework before the loss.

## Evidence strength: a qualitative ranking

Not all evidence carries equal weight. As a general principle (indicative, not a rule), independent and contemporaneous records are the strongest; self-serving retrospective statements are the weakest. The practical aim is to assemble several mutually-corroborating items from the top of this ranking rather than relying on any single document.

| Evidence type | Relative strength | Why |
|---|---|---|
| On-chain transaction records (immutable, timestamped) | Strongest | Independent, tamper-evident, dated by the chain itself |
| Independent third-party records (exchange CSV, police report, manufacturer correspondence) | Strong | Created by a party with no stake in the tax outcome |
| Statutory declaration sworn before an authorised witness | Strong (if contemporaneous) | Carries legal weight; perjury exposure |
| Contemporaneous self-authored narrative (signed, dated same day) | Moderate | Self-serving but timely; corroborates other items |
| Photos with verifiable metadata (unboxing, device screens) | Moderate | Supports chain of custody if dated |
| Retrospective narrative written long after the event | Weak | Tax authorities discount after-the-fact accounts |
| Round-number, pattern-free assertions with no supporting trail | Weakest | Reads as reconstruction or fabrication |

The dominant theme across published guidance is that a *cluster* of independent, dated records beats any one document, however formal.

## Timeline-at-a-glance: what to do when

A consolidated view of the action windows from the detailed sections below. The 24–48 hours after discovery is the single highest-leverage documentation window — contemporaneous statements made then are dramatically more persuasive than anything reconstructed later.

| Window | Priority actions | Evidence class |
|---|---|---|
| **On every purchase** | Save acquisition + transfer-to-self-custody records | Class 1 |
| **On wallet creation** | Capture device receipt, generation date, test tx, backup method | Class 2 |
| **Quarterly** | Refresh transaction journal, blockchain export, address list | Class 3 |
| **Annually (pre-EOFY)** | Reconcile balances, verify backups, refresh attestation | Class 3 review |
| **Within 24h of loss** | Signed narrative, chain snapshot, police report (if theft), notify tax agent | Class 4 |
| **Within 7 days** | Complete statutory declaration, compile Class 1–3 package | Class 4 |
| **Within 30 days** | Determine income year, prepare CGT entry, consider private ruling | Class 4 |

## Cost-benefit framing

For a holder with material cold-storage positions (say $10,000+ in crypto), the operational cost of building the evidence framework is:

- 30 minutes per acquisition for Class 1
- 2 hours one-time for Class 2 per wallet
- 30 minutes quarterly for Class 3
- 2 hours annually for the review

Roughly 4–6 hours per year, ongoing. For a $50,000 cold-storage position, that's ~10% effort relative to the potential tax saving on a fully substantiated loss (at top marginal rate, the loss-shield value on $50k of capital gains is up to ~$11.75k). The framework is overwhelmingly cost-effective for material positions.

## Source notes

Synthesised from ATO public guidance on crypto asset investments, ATO record-keeping guidance, the pattern of publicly available ATO private rulings on lost-crypto claims, and general Australian evidence-law practice for statutory declarations. **Not exhaustive — for material positions, consult a registered tax agent and consider a binding private ruling.**

## Related

- [[lost-or-stolen-crypto-au-tax]] — what the loss claim looks like and how to report it
- [[cryptocurrency-tax-australia]] — broader crypto tax framework
- [[reporting-obligations-australia]] — record retention rules
- [[capital-gains]] — general CGT concept
- [[itaa-1997-overview]] — broader ITAA index

> **Reminder — not tax advice.** As stated at the top, this is an operational checklist to make a future position defensible, not legal or tax advice. For material positions, confirm specific evidence requirements with a registered tax agent and consider a binding private ruling.
