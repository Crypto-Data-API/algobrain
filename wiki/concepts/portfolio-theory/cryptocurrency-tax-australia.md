---
title: "Cryptocurrency Tax (Australia)"
type: concept
created: 2026-04-07
updated: 2026-06-20
status: excellent
tags: [australia, tax, crypto, defi, nft]
aliases: ["Australian Crypto Tax", "Crypto CGT Australia"]
related: ["[[australian-investor-tax]]", "[[tax-loss-harvesting-australia]]", "[[capital-gains-tax-discount]]", "[[bitcoin]]", "[[ethereum]]", "[[defi]]", "[[nft]]", "[[staking]]", "[[tax-efficient-investing]]", "[[smsf]]", "[[superannuation]]", "[[austrac]]", "[[vasp-regulation]]", "[[australian-crypto-regulation]]", "[[lost-or-stolen-crypto-au-tax]]", "[[self-custody-tax-evidence-checklist]]", "[[itaa-1997-overview]]"]
domain: [portfolio-theory, risk-management]
difficulty: intermediate
prerequisites: ["[[australian-investor-tax]]", "[[capital-gains-tax-discount]]"]
---

The Australian Taxation Office (ATO) treats cryptocurrency as a **CGT asset**, not as currency — meaning every disposal (selling for AUD, swapping crypto-to-crypto, spending crypto on goods/services, or interacting with DeFi protocols) is a capital gains tax event. The same [[capital-gains-tax-discount|50% CGT discount]] available on shares and property applies to crypto held for more than 12 months, and crucially, Australia has **no wash sale rule** for crypto, making it one of the most advantageous jurisdictions globally for crypto [[tax-loss-harvesting-australia|tax-loss harvesting]].

> **Not tax or legal advice.** This page is general educational information about the ATO's treatment of crypto. The rules — especially around DeFi, staking, wrapping, and personal-use thresholds — are evolving, and some are not yet settled by formal rulings. Dollar thresholds (such as the personal-use exemption) and penalty percentages are **indicative** and may change. Confirm your situation with the [ATO](https://www.ato.gov.au) and a registered tax agent experienced in crypto before acting. See [[australian-investor-tax]] for the underlying CGT framework.

## Decision Tree: Is This Transaction Taxable?

A quick mental model for the most common situations:

- **Did ownership change?** Moving crypto between *your own* wallets is **not** a CGT event. Disposing to anyone or anything else is.
- **Did you receive crypto for free/as reward?** Staking, yield, and airdrops are **ordinary income** at market value on receipt — taxed up front, with a fresh cost base for later CGT.
- **Did you swap one crypto for another?** That is a **disposal of the first + acquisition of the second** — two events, even with no AUD involved.
- **Did you spend crypto?** A disposal at market value — taxable unless the narrow personal-use exemption genuinely applies.
- **Did you hold the disposed asset >12 months?** If yes and it was a capital (not income) holding, the [[capital-gains-tax-discount|50% discount]] applies to the gain.

## Overview

The ATO released its initial crypto tax guidance in 2014 and has progressively tightened enforcement since. Cryptocurrency is now a **priority compliance area**, with the ATO actively data-matching exchange records against tax returns. Over 350,000 letters have been sent to Australians identified as holding crypto who may not have reported correctly.

Despite the strict reporting requirements, the underlying rules are relatively straightforward — crypto follows the same CGT framework as shares and property, with a few additional complexities around DeFi, staking, and airdrops.

## What Is a CGT Event?

Every disposal of cryptocurrency triggers a CGT event. The most common CGT events for crypto investors:

| Action | CGT Event? | Treatment |
|--------|-----------|-----------|
| **Buying crypto with AUD** | No | Acquisition — establishes cost base |
| **Selling crypto for AUD** | Yes | Capital gain or loss on the difference |
| **Swapping crypto-to-crypto** (e.g., BTC to ETH) | Yes | Disposal of BTC at market value + acquisition of ETH at market value |
| **Spending crypto on goods/services** | Yes | Disposal at market value at the time of payment |
| **Gifting crypto** | Yes | Deemed disposal at market value |
| **Transferring between your own wallets** | No | No change of ownership — not a CGT event |
| **Providing liquidity to a DeFi pool** | Likely yes | Disposal of tokens, acquisition of LP tokens (see DeFi section) |
| **Receiving staking rewards** | Not a CGT event — but taxable as ordinary income | See Staking section |
| **Receiving an airdrop** | Not a CGT event — but taxable as ordinary income | See Airdrop section |
| **Losing access to crypto** (lost keys, hack)** | Possible CGT loss | Must prove the asset is permanently lost — ATO requires evidence |

### The Crypto-to-Crypto Trap

One of the most common mistakes: investors who swap one cryptocurrency for another (e.g., trading [[bitcoin|BTC]] for [[ethereum|ETH]]) do not realise that **each swap is two CGT events**:

1. **Disposal of BTC** at market value → capital gain or loss relative to BTC cost base
2. **Acquisition of ETH** at market value → establishes ETH cost base

This means an investor who trades frequently between tokens can accumulate dozens or hundreds of CGT events per year, each requiring cost base tracking and gain/loss calculation. The record-keeping burden is enormous and is the primary reason crypto tax software exists.

## CGT Discount for Crypto

The [[capital-gains-tax-discount|50% CGT discount]] applies to crypto held for more than 12 months, just as it does for shares:

| Holding Period | CGT Treatment |
|---------------|---------------|
| **< 12 months** | Full capital gain taxed at marginal rate |
| **> 12 months** | Only 50% of the gain is assessable (individuals/trusts) |

### Practical Implication

*(Illustrative figures using an indicative 37% marginal rate — confirm current rates with the ATO.)* For a long-term [[bitcoin]] holder in the 37% bracket:
- Buy 1 BTC at $40,000
- Sell 1 BTC at $100,000 after 14 months
- Gross capital gain: $60,000
- After 50% discount: $30,000 assessable
- Tax: $30,000 x 37% = **$11,100** (effective rate of 18.5% on the $60,000 gain)

Without the discount (held <12 months): $60,000 x 37% = $22,200. The discount saved $11,100.

This creates a strong incentive to HODL crypto for at least 12 months before selling — the same structural incentive that applies to shares and property.

## Cost Base Methods

The ATO accepts several methods for identifying which crypto parcels are being disposed of:

| Method | Description | Best For |
|--------|-------------|----------|
| **Specific identification** | Identify exactly which parcel you are selling | Maximising tax efficiency — sell the highest-cost-base parcel first to minimise gains |
| **FIFO (First In, First Out)** | Oldest parcels sold first | Simple, consistent, often results in larger gains (oldest parcels bought cheapest) |
| **LIFO (Last In, First Out)** | Newest parcels sold first | May minimise gains if recent purchases were at higher prices |
| **Highest cost base first** | Sell the most expensive parcels first | Minimises immediate gains |

You must be **consistent** with your chosen method across all disposals of a particular cryptocurrency within a financial year. Specific identification is generally the most tax-efficient if you have the records to support it.

## Income vs Capital: The Core Distinction

Almost every crypto tax question reduces to whether an event is **ordinary income** (taxed at full marginal rate on receipt, no discount) or a **CGT event** (gain/loss, with the 50% discount available if held >12 months). The table summarises common cases:

| Event | Income or Capital? | Discount available? | Notes |
|-------|--------------------|--------------------|-------|
| Sell crypto for AUD | Capital | Yes if >12 months | Standard CGT disposal |
| Swap crypto-to-crypto | Capital (×2) | Yes if each leg >12 months | Disposal + acquisition |
| Spend crypto on goods | Capital | Yes if >12 months | Disposal at market value |
| Staking / validation rewards | Income on receipt | No (on receipt) | New cost base = market value; later sale is CGT |
| Yield farming rewards | Income on receipt | No (on receipt) | Same pattern as staking |
| Airdrop (with market value) | Income on receipt | No (on receipt) | $0 cost base if no value at receipt |
| Receiving an NFT as reward | Income on receipt | No (on receipt) | Then CGT on later disposal |
| Mining (hobby) | Generally capital on disposal | Yes if >12 months | Treatment differs if a business |
| Mining / minting as a business | Income (trading stock) | No | Business deductions instead |

The recurring pattern: **rewards are taxed twice over their life** — once as income when received, then again as a capital gain/loss measured from that income-inclusion value when disposed of.

## DeFi-Specific Tax Treatment

DeFi introduces complex tax scenarios that the ATO has not fully addressed with specific rulings, creating areas of uncertainty.

### Staking Rewards

- Staking rewards (proof-of-stake validation rewards) are treated as **ordinary income** at the market value of the tokens when they are received/earned
- This means they are taxed at your full marginal rate — no CGT discount
- When you subsequently dispose of the staked tokens, the disposal is a separate **CGT event** with a cost base equal to the market value at the time you received them
- Example: Receive 0.5 ETH staking reward when ETH = $3,000 → $1,500 ordinary income. Later sell the 0.5 ETH when ETH = $5,000 → $1,000 capital gain (with potential 50% discount if held >12 months)

### Liquidity Pool Entry and Exit

Providing tokens to a liquidity pool (e.g., Uniswap, SushiSwap) likely involves:

1. **Entry**: Disposing of Token A and Token B (two CGT events) and receiving LP tokens (acquisition)
2. **While in pool**: Trading fees received may be ordinary income or additional CGT events
3. **Exit**: Disposing of LP tokens (CGT event) and receiving Token A and Token B (acquisitions)

The net effect is that entering and exiting a liquidity pool can create multiple taxable events, even if your net position is unchanged.

### Impermanent Loss

When you exit a liquidity pool and receive a different ratio of tokens than you deposited (impermanent loss), the loss is effectively crystallised through the CGT events on entry and exit. The loss reduces your net capital gain — but only if you actually exit the pool. Unrealised impermanent loss is not a tax event.

### Yield Farming

- Yield farming rewards (additional tokens earned from providing liquidity or participating in protocols) are treated as **ordinary income** at market value when received
- Similar to staking rewards — subsequent disposal is a separate CGT event

### Wrapping and Unwrapping Tokens

- The ATO has **not definitively ruled** on whether wrapping tokens (e.g., ETH to WETH) constitutes a CGT event
- Conservative position: treat it as a disposal of ETH and acquisition of WETH (both at market value, so the gain/loss is near zero)
- Aggressive position: no change in economic substance, not a CGT event
- Until the ATO provides clarity, many tax professionals recommend treating wrapping as a CGT event with a near-zero gain/loss to be safe

## NFT Tax Treatment

NFTs are CGT assets under the same framework as other crypto:

- **Purchasing an NFT with crypto**: Two CGT events — disposing of the crypto (gain/loss on the crypto) and acquiring the NFT (cost base = market value of crypto at time of purchase)
- **Selling an NFT for crypto**: Disposing of the NFT (gain/loss relative to NFT cost base) and acquiring crypto (new cost base)
- **Selling an NFT for AUD**: Single CGT event — disposing of the NFT
- **Minting and selling NFTs as a business**: May be treated as trading stock/business income rather than CGT — no [[capital-gains-tax-discount|CGT discount]] but potentially more deductions

The [[capital-gains-tax-discount|50% discount]] applies to NFTs held >12 months (same as any other CGT asset).

## Airdrops

Airdrops create a taxable event:

- **Established tokens from known projects**: Ordinary income at market value when you gain dominion and control (i.e., when they appear in your wallet and you can access them)
- **Worthless/spam airdrops**: If the airdrop has no market value when received, no income to declare. If you later sell for value, the CGT cost base is $0
- **Unsolicited airdrops**: Even if you didn't ask for them, they are taxable income if they have market value
- **Fork tokens**: Similar to airdrops — new tokens received from a chain fork may be ordinary income or may have a $0 cost base (ATO position is evolving)

## No Wash Sale Rule — The Australian Crypto Tax Advantage

This is the single biggest structural advantage Australian crypto investors have over US counterparts:

- In the US, starting 2026, the wash sale rule will apply to crypto — preventing immediate repurchase after selling at a loss
- In Australia, **no such rule exists** for crypto (or for shares)
- You can sell [[bitcoin]] at a loss on 29 June, crystallise the capital loss for tax purposes, and buy back on 30 June (or even the same day)
- The ATO's Part IVA anti-avoidance provision could theoretically apply, but has never been successfully used against straightforward crypto tax-loss harvesting
- This makes [[tax-loss-harvesting-australia|EOFY tax-loss harvesting]] for crypto extremely powerful — especially given crypto's volatility, which creates large unrealised losses frequently

### Example: Crypto Tax-Loss Harvesting

*(Illustrative figures and an indicative marginal rate — confirm current rates with the ATO. Tax-loss harvesting only has value if you have realised gains to offset, or expect to.)*

- Hold 2 BTC purchased at $80,000 each ($160,000 total cost base)
- BTC drops to $50,000 — unrealised loss of $60,000
- Before 30 June: sell both BTC for $100,000 — crystallise $60,000 capital loss
- 1 July: repurchase 2 BTC at ~$50,000 each — new cost base of $100,000
- The $60,000 loss offsets gains elsewhere in the financial year
- At 37% marginal rate on short-term gains, this saves **$22,200 in tax**
- If applied against long-term gains: saves $11,100 (because the gain is already 50% discounted)

## Personal Use Exemption

The ATO provides a narrow exemption for crypto used as currency for **personal purchases under $10,000**:

- The crypto must have been acquired for **personal use** (not as an investment)
- The purchase must be for **personal goods or services** (not another investment)
- The ATO interprets this very narrowly — holding crypto as a speculative investment and occasionally spending small amounts does NOT qualify
- The exemption is essentially limited to people who acquire crypto specifically to buy goods/services and spend it quickly
- **Most investors should assume this exemption does not apply to them**

## ATO Enforcement

The ATO has made crypto a priority compliance area:

- **Data matching**: The ATO receives data from all major Australian exchanges (CoinSpot, Swyftx, Independent Reserve, BTC Markets, Coinbase, Binance AU, etc.)
- **350,000+ letters** sent to Australians identified as potentially non-compliant on crypto reporting
- **Penalties**: Failure to report can result in penalties of 25% (careless) to 75% (intentional disregard) of the tax shortfall, plus interest
- **Voluntary disclosure**: If you haven't reported previous years, making a voluntary disclosure before ATO audit can significantly reduce penalties

## Record Keeping Requirements

The ATO requires comprehensive records:

- Date and time of every transaction
- Value in AUD at the time of every transaction
- Purpose of the transaction (what you received/gave)
- Transaction ID (hash)
- Exchange records and wallet addresses
- Records of any crypto received as gifts, airdrops, staking rewards, or payments for goods/services

### Crypto Tax Software

Given the complexity of tracking hundreds or thousands of transactions, crypto tax software is essential:

| Software | Founded | Key Features |
|----------|---------|-------------|
| **Koinly** | Australian-founded | Auto-import from 700+ exchanges, ATO-specific reports, cost base methods |
| **CryptoTaxCalculator** | Australian-founded | ATO compliance, DeFi support, NFT tracking, multi-chain |
| **CoinTracker** | US-based | Australian tax support, portfolio tracking |
| **Syla** | Australian-founded | ATO-specific, automatic exchange sync |

Both Koinly and CryptoTaxCalculator are Australian-founded companies — a reflection of the complexity of Australia's crypto tax regime and the large Australian crypto investor base.

## Crypto Tax Checklist

A practical routine for staying compliant and tax-efficient:

- [ ] **Export full transaction history** from every exchange and wallet each financial year (trades, transfers, rewards, fees).
- [ ] **Tag wallet-to-wallet transfers** as non-disposals so they are not mistaken for sales.
- [ ] **Record AUD market value** at the time of every disposal, swap, spend, and reward receipt.
- [ ] **Separate income events** (staking, airdrops, yield) from capital events — they are reported differently.
- [ ] **Choose and apply a consistent cost-base method** per asset within the year (specific ID is usually most efficient if records support it).
- [ ] **Review unrealised losses before 30 June** for [[tax-loss-harvesting-australia|harvesting]] (no wash sale rule applies).
- [ ] **Reconcile against the ATO** — exchanges report under data-matching, so your figures should match.
- [ ] **Keep records for the required period** (generally 5 years after the relevant CGT event).
- [ ] **Document lost/stolen crypto** thoroughly if claiming a capital loss — see [[lost-or-stolen-crypto-au-tax]] and [[self-custody-tax-evidence-checklist]].

## Common Crypto Tax Mistakes

1. **Forgetting that crypto-to-crypto swaps are taxable** — the single most common error; each swap is two CGT events even with no AUD.
2. **Not declaring staking/airdrop income** — these are taxed as income on receipt, separately from later disposal.
3. **Assuming the personal-use exemption applies** — it is interpreted very narrowly and rarely covers investors.
4. **Treating transfers between own wallets as disposals** — they are not CGT events; over-reporting them inflates tax.
5. **Losing cost-base records** after an exchange shuts down — export early and often.
6. **Ignoring DeFi/LP entry and exit events** — providing and withdrawing liquidity can create multiple taxable events.
7. **Not harvesting losses** despite the absence of a wash sale rule — leaving the jurisdiction's biggest structural advantage on the table.
8. **Under-estimating ATO data-matching** — non-reporting is actively detected and penalised (see [[austrac]] and the enforcement section above).

## Crypto in SMSFs

[[smsf|SMSFs]] can hold cryptocurrency, subject to:

- The investment strategy must explicitly allow cryptocurrency
- Crypto must be held in the fund's name (not a personal wallet)
- Use a compliant exchange that supports SMSF-specific accounts
- 15% tax on gains in accumulation (10% with [[capital-gains-tax-discount|CGT discount]])
- 0% tax on gains in pension phase
- Record keeping is the same — the SMSF auditor will review crypto holdings

## Related

- [[australian-investor-tax]]
- [[tax-loss-harvesting-australia]]
- [[capital-gains-tax-discount]]
- [[bitcoin]]
- [[ethereum]]
- [[defi]]
- [[nft]]
- [[staking]]
- [[tax-efficient-investing]]
- [[smsf]]
- [[superannuation]]
- [[austrac]]
- [[vasp-regulation]]
- [[australian-crypto-regulation]]
- [[lost-or-stolen-crypto-au-tax]]
- [[self-custody-tax-evidence-checklist]]
- [[itaa-1997-overview]]

## Sources

- ATO — Transacting with cryptocurrency
- ATO — Tax treatment of crypto assets
- ATO — Data matching program — cryptocurrency
- ATO — Record keeping for crypto
