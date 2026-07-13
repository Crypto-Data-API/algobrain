---
title: "Regional Currency Arbitrage (Pre-1870s Bank Note Discounting)"
type: strategy
created: 2026-04-24
updated: 2026-06-10
status: good
tags: [arbitrage, history, forex, market-microstructure, regulation]
aliases: ["Bank Note Arbitrage", "Wildcat Bank Note Discounting", "Broken Bank Note Arbitrage"]
strategy_type: fundamental
timeframe: swing
markets: [forex]
complexity: intermediate
backtest_status: retired
edge_source: [informational, structural]
edge_mechanism: "Professional note brokers maintained rate sheets and redemption networks; country merchants and travelers accepted notes at poorly-informed prices, creating persistent informational asymmetry."
data_required: [bank-note-reporter-listings, redemption-network-cost]
min_capital_usd: 1000
capacity_usd: 500000
crowding_risk: low
expected_sharpe: 1.0
expected_max_drawdown: 0.40
breakeven_cost_bps: 200
decay_evidence: "Extinguished by [[national-banking-act-1863]] and equivalent consolidations in Europe."
---

# Regional Currency Arbitrage (Pre-1870s Bank Note Discounting)

Regional currency arbitrage was the practice, roughly from the 1830s through the 1863 [[national-banking-act-1863]], of buying distant or poorly-capitalized bank notes at a discount in one city and redeeming them at or near par in another — or selling them to a broker whose network could. In the United States this was the defining retail-facing arbitrage of the "wildcat banking" era; analogous trades operated on Scottish notes circulating in England before the Bank Charter Act of 1844 and on the billets of French provincial banks before the Banque de France acquired its monopoly on issuance.

## Edge Source

Primarily **informational**, secondarily **structural**. The core inefficiency was that any given merchant, farmer, or traveler could only reasonably know the standing of a handful of issuing banks, while professional note brokers and bank-note reporters maintained near-exhaustive lists. Structural edges came from physical redemption networks: the [[suffolk-system]] in New England, correspondent banking chains, and specialized express firms (Adams, American, Wells Fargo) that moved paper to the issuing counter for a commission smaller than the discount a country merchant would accept.

## Why This Edge Exists

The United States between the 1836 expiration of the Second Bank of the United States and the 1863 [[national-banking-act-1863]] had roughly 1,500–1,600 state-chartered banks issuing their own paper. Notes were technically redeemable at the issuing bank in specie (gold or silver), but the cost of physically presenting a Georgia bank's note in Savannah if you received it in Cincinnati was a nontrivial fraction of face value. "Wildcat" banks were deliberately sited in remote locations — literally, per the folklore, where only wildcats lived — to make redemption impractical.

This created a two-tier market. Country merchants posted discount lists or simply refused distant notes; professional note brokers published **bank note reporters** — periodical rate sheets — listing every known bank with a current discount (e.g., "Bank of Marietta, Ohio: 2%"; "Cincinnati Trust: 15%"; "closed, worthless") and counterfeit-detection notes. The two canonical publications were **Bicknell's Counterfeit Detector and Bank Note List** (Philadelphia, from c. 1830) and **Thompson's Bank Note Reporter** (New York, from 1842). Brokers took the other side of nearly every retail transaction, making the spread between the country-merchant bid and the broker redemption cost.

The other side of this trade: rural note-holders who had no access to current discount information, immigrants paid in notes and needing specie, and merchants unwilling to lock up capital in a redemption trip. They kept losing because they had no alternative — until the telegraph and the national currency eliminated the edge.

## Null Hypothesis

Under no-edge conditions, any bank note would trade at its face value minus the expected present value of (a) the probability of issuer failure, (b) the redemption cost, and (c) a small broker margin. The empirical observation — that identical notes traded at meaningfully different prices in different cities on the same day, and that broker profits persisted for decades — is what established the inefficiency.

## Rules

### Entry
1. Obtain the current issue of a bank-note reporter (e.g., *Thompson's*), no more than a few days old.
2. Quote the country merchant or traveler a discount **wider** than your redemption cost. Typical structure: reporter quotes 5% discount; broker bids 7–8%; redemption cost through a correspondent is 2–3%.
3. Verify authenticity: cross-check plate design, paper, and serial ranges against the counterfeit-detector section of the reporter.
4. Refuse notes of any bank flagged "closed," "doubtful," or recently downgraded unless discount exceeds likely recovery.

### Exit
1. Route notes to a correspondent bank in the issuing region; pay a fee (often 0.25–1.5% plus freight and insurance).
2. Alternatively, sell in bulk to a larger up-stream broker at a smaller spread (wholesale redemption).
3. In [[suffolk-system]] New England, present directly to the Suffolk Bank in Boston, which redeemed all participating New England notes at par for a modest reserve deposit.

### Position Sizing
Sized by freight-and-insurance economies of scale — notes were bundled into parcels worth several hundred to a few thousand dollars before being shipped for redemption. Exposure concentration to any single issuer was kept small because bank failures were frequent and sudden.

## Implementation Pseudocode

```
for each note presented:
    issuer = identify_bank(note)
    reporter_discount = lookup(issuer, current_reporter)
    if issuer in blacklist or reporter_discount > max_acceptable:
        refuse
    bid = reporter_discount + broker_margin   # ~1.5-3% wider than reporter
    if counterfeit_check(note) fails:
        refuse and report
    accept at (1 - bid) * face_value

batch by region:
    when parcel_value > min_shipment_size:
        ship via correspondent to issuing_region
        redeem at (1 - redemption_fee - freight_insurance) * face_value
        realize spread = bid - redemption_cost
```

## Indicators / Data Used

- **Bank note reporters**: Bicknell's, Thompson's, Van Court's, Hodges' — updated weekly or semi-monthly.
- **Counterfeit detectors**: plate descriptions, vignette details, known alterations.
- **Correspondent network rate cards**: per-region redemption cost.
- **[[suffolk-system]] participation list**: New England notes redeemable at par in Boston.
- **Specie flow telegrams** (from roughly 1846): early warning of bank runs and suspensions.

## Example Trade

A Cincinnati broker in June 1855 is presented with $500 face value in notes of the **Bank of Morgan, Georgia**. *Thompson's Bank Note Reporter* for that week lists Morgan, GA at a 6% discount in New York. The broker bids 8.5% discount (pays $457.50 in Cincinnati-acceptable specie or local notes). She bundles the notes with $2,000 of other Southern issues and ships to a Charleston correspondent, who redeems at the Bank of Morgan counter for a combined 3.25% in fees, freight, and insurance. Net: $500 face redeemed for $483.75; purchase cost $457.50; **gross profit $26.25 (5.25%)** over roughly six weeks of float.

## Performance Characteristics

Broker accounts from the period (Knox's *History of Banking*; Gorton's modern reconstruction in "Reputation Formation in Early Bank Note Markets") suggest net margins of 2–4% per round-trip, with turnover of 6–10 cycles per year, implying gross returns of 15–35% annually on capital — spectacular by modern standards, but achieved in an environment with frequent total losses when issuers suspended specie payments. Realized Sharpe ratios were likely modest once bank failures are counted.

## Capacity Limits

Capacity was bounded by (a) the float of notes in any given region, (b) the availability of correspondent redemption networks, and (c) the size of the specie reserve any single broker could maintain. The largest houses (Drexel, Clark, later Jay Cooke) operated at high six-figure balances in contemporary dollars.

## What Kills This Strategy

- **Regulatory consolidation**: the [[national-banking-act-1863]] and the 1865 10% tax on state bank note issuance extinguished the U.S. version entirely within two years.
- **Information technology**: the telegraph collapsed the information asymmetry that made rural discounts durable.
- **Banking consolidation abroad**: Scottish note circulation was rationalized by the Bank Charter Act 1844; French provincial notes by the Banque de France's expanding monopoly through 1848.
- **Counterfeit flooding**: occasional waves of sophisticated counterfeits imposed large losses on brokers who misidentified notes.

## Kill Criteria

Historically terminal — retired by statute (the [[national-banking-act-1863]] and the 1865 10% tax on state-bank notes, effective 1866). For the historical operator, the working kill criteria would have been numerical: (a) net redemption spread below ~1% per cycle after freight, insurance, and failure losses; (b) single-issuer loss exposure exceeding ~5% of broker capital; (c) telegraph-driven convergence of city and country discount quotes to within broker costs. No modern analogue trades the same instrument, though the structural parallel (regional price discovery in fragmented private issuance) lives on in [[stablecoin-depeg-arbitrage]] and cross-exchange crypto arbitrage.

## Advantages

- **Persistent edge** over decades due to geographic friction
- **Negative-duration** on local bank failure, if hedged via basket diversification
- **Public-good externality**: brokers enforced price discovery on otherwise opaque issuers

## Disadvantages

- **Catastrophic single-issuer risk** — a bank suspension wiped the position
- **Counterfeit exposure** — sophisticated fakes were hard to detect
- **Capital tied up in float** for weeks during redemption trips
- **Total extinction risk** — the strategy died overnight by legislation in 1863–1866

## Sources

- Gary B. Gorton, "Reputation Formation in Early Bank Note Markets" (*Journal of Political Economy*, 1996)
- Bray Hammond, *Banks and Politics in America from the Revolution to the Civil War* (1957)
- Roger H. Hinderliter and Hugh Rockoff, "The Management of Reserves by Antebellum Banks in Eastern Financial Centers"
- Thompson's and Bicknell's bank note reporters (period primary sources)

## Related

- [[specie-flow-arbitrage]]
- [[gold-point-arbitrage]]
- [[bill-broking-arbitrage]]
- [[suffolk-system]]
- [[national-banking-act-1863]]
- [[free-banking-era]]
- [[wildcat-banking]]
- [[rothschild-family]]
- [[baring-brothers]]
- [[historical-cable-arbitrage]]
- [[gold-standard-mechanics]]
