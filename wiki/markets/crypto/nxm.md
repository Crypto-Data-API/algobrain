---
title: "Nexus Mutual"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, risk-management]
aliases: ["NXM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://nexusmutual.io/"
related: ["[[crypto-markets]]", "[[decentralized-finance]]", "[[ethereum]]", "[[risk-management]]"]
---

# Nexus Mutual

**Nexus Mutual** (NXM) is a decentralized insurance ("discretionary mutual") protocol built on [[ethereum|Ethereum]] that lets members pool capital to underwrite cover against crypto-native risks — primarily smart-contract failure, protocol hacks/exploits, and custodian/de-peg events. NXM is a **membership/capital token**: it is bonding-curve-priced against the mutual's capital pool and is restricted to KYC'd members rather than freely traded like an ordinary ERC-20.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | NXM |
| **Chain** | [[ethereum\|Ethereum]] |
| **Current Price** | $46.86 |
| **Market Cap** | $80,812,716 |
| **Market Cap Rank** | #312 |
| **24h Volume** | $0 (membership-gated token; minimal open-market trading) |
| **24h Change** | +1.22% |
| **7d Change** | +2.58% |
| **Fully Diluted Valuation** | $80,812,716 |
| **All-Time High** | $185.97 (2021-11-10) |
| **All-Time Low** | $6.96 (2020-07-22) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Trading context: the market is in **extreme fear (Fear & Greed = 23)** and an **Established Bear Market** as of 2026-06-21. The reported $0 / 24h volume is characteristic of NXM specifically: the token is membership-gated and priced by the mutual's bonding curve, so there is little or no open-market spot turnover. Practical exposure for non-members typically runs through the wrapped **wNXM** wrapper, not NXM directly. NXM held green on both the day (+1.22%) and week (+2.58%) — but for a bonding-curve token those moves reflect changes in the mutual's capital pool / MCR ratio rather than market trading.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.72M NXM |
| **Total Supply** | ~1.72M NXM |
| **Max Supply** | Uncapped (mint/burn via bonding curve) |
| **Market Cap / FDV** | 1.00 |

NXM has no fixed max supply: tokens are **minted when members deposit capital** into the pool and **burned when capital is withdrawn or claims are paid**, with the price set by a bonding curve referencing the **Minimum Capital Requirement (MCR)** — the ratio of the mutual's capital to its outstanding cover liabilities. Because circulating ≈ total supply, MC/FDV = 1.00 (no overhang of unvested tokens). The token's value is therefore directly tied to the health and surplus of the underwriting pool, not to emissions or speculation alone.

---

## How & Where It Trades

### Protocol mechanics (the venue itself)
Nexus Mutual is an underwriting venue, not a swap venue:

- **Cover pools / risk pools** — members stake NXM to back specific protocols or risk buckets. Stakers earn premiums for the cover they underwrite and bear the loss if a claim against that risk pays out. This is the core "sell insurance, earn premium" trade.
- **Buying cover** — users purchase cover (e.g. against a specific DeFi protocol being hacked, a stablecoin de-pegging, or a custodian failing) by paying a premium quoted from staked capacity and assessed risk.
- **Capital pool & MCR** — all premiums and deposits sit in a shared capital pool; the MCR ensures the mutual holds enough capital relative to liabilities. NXM mint/redeem price moves along the bonding curve as the capital-to-MCR ratio changes.
- **Claims assessment** — when a covered event occurs, members vote/assess whether a claim is valid; approved claims are paid from the pool (burning NXM). This **claims process is itself a risk** — discretionary assessment means payout is not guaranteed.

### Spot venues / access
- NXM itself is **not freely listed** — it is restricted to KYC'd members and the bonding curve, hence the ~$0 open-market volume.
- Non-members typically gain exposure through **wNXM** (wrapped NXM), which historically trades on centralized and decentralized venues and can deviate from NXM's bonding-curve "book value."

There is no meaningful derivatives market (perps/OI/funding) for NXM given its membership-gated design.

### Contract address
| Chain | Address |
|---|---|
| Ethereum | `0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b` |

---

## Use Case / Narrative / Category

Nexus Mutual is the flagship of the **DeFi insurance / on-chain risk-transfer** category. Its narrative: as DeFi grows, so does demand to hedge smart-contract and custodian risk, and Nexus offers a decentralized, member-owned alternative to traditional insurers. It expanded over time from pure smart-contract cover to **custody cover** (centralized custodians/lenders such as Celsius, BlockFi, Nexo) and de-peg/yield cover. Note the original smart-contract cover protects against "unintended uses" of contracts — it does **not** cover lost private keys or generic exchange hacks unless a specific custody product applies.

---

## Peer Comparison

| Protocol | Model | Token tradability | Coverage focus | Notes |
|---|---|---|---|---|
| **Nexus Mutual (NXM)** | Discretionary mutual; bonding-curve token, MCR-driven | Membership-gated NXM + open **wNXM** wrapper | Smart-contract, custody, de-peg cover | Flagship; capital pool underwrites; claims by member assessment |
| InsurAce (INSUR) | Parametric + discretionary cover | Freely traded ERC-20 | Multi-chain DeFi cover, stablecoin de-peg | Lower capital base post-2022 |
| Unslashed / Sherlock | Underwriting + audit-linked cover | Freely traded | Protocol exploit cover | Often paired with audits |
| Risk Harbor / others | Parametric, automated payout | Freely traded | Algorithmic claim triggers | No discretionary assessment |
| **Traditional reinsurance** | Regulated, capital-backed | n/a | Broad, off-chain | The off-chain benchmark Nexus competes against on cost/transparency |

Nexus Mutual is by capital and reputation the **dominant on-chain risk-transfer venue**, but its discretionary-claims model and membership-gated token make it structurally different from freely-traded, parametric competitors: holders get tighter alignment between token value and pool health (MC/FDV = 1.00, no emissions), at the cost of liquidity and a non-guaranteed, vote-based payout process. See [[insurance]] and [[risk-management]] for the broader category framing.

---

## Notable History

- Launched 2019 as one of the first decentralized insurance protocols; introduced **custody cover** in December 2020.
- NXM hit its all-time high of **$185.97** on 2021-11-10 at the peak of the last bull cycle; all-time low of **$6.96** on 2020-07-22.
- The mutual paid claims during major DeFi exploits and the 2022 CeFi collapse wave (custody-cover relevance), testing its claims process in real conditions.
- As of 2026-06-21 NXM trades ~75% below its $185.97 ATH (at ~$46.86) amid the broad bear market, though it remains far above its $6.96 ATL.

---

## Risks

- **Claims risk** — payouts depend on discretionary member assessment; a claim can be denied, or cover terms may exclude a loss the buyer expected to be covered. This is the defining risk of buying Nexus cover.
- **Underwriting / capital-pool risk** — stakers (capital providers) can lose principal if claims exceed premiums in their pool; a large correlated exploit could stress the MCR and depress the bonding-curve price.
- **Liquidity / access risk** — NXM is membership-gated with ~$0 open-market volume; entry/exit for non-members runs through wNXM, which can trade at a discount/premium to bonding-curve value.
- **Bonding-curve mechanics** — price is endogenous to capital flows; rapid withdrawals can compress the curve.
- **Smart-contract risk** — ironically, the insurer itself runs on contracts that carry their own bug risk.
- **Regime risk** — DeFi activity and cover demand tend to fall in bear markets, pressuring premium income.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[insurance]]
- [[risk-management]]
- [[decentralized-finance]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-1000): rank #312, $80.81M mcap, $46.86, $0 24h volume (membership-gated).
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
