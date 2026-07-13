---
title: "Re Protocol reUSD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins, real-world-assets]
aliases: ["REUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://re.xyz"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoin]]", "[[stablecoins]]", "[[real-world-assets]]", "[[yield-bearing-stablecoin]]"]
---

# Re Protocol reUSD

**Re Protocol reUSD** (ticker **REUSD**) is a **yield-bearing, value-accruing dollar deposit token** from Re Protocol, a platform that tokenizes exposure to **reinsurance risk** — a [[real-world-assets|real-world asset]]. reUSD is the principal-protected, *fixed-yield* tier (quoted by the protocol as a risk-free reference rate + ~250 bps); its sibling [[re-protocol-reusde|reUSDe]] is the risk-bearing, variable-yield tier (advertised up to ~23% APR). It is deployed across [[ethereum|Ethereum]], Base, Arbitrum, Avalanche, BNB Chain and Ink. Crucially, reUSD is **not a $1-pegged stablecoin** — it is a rebasing/accruing claim whose price rises above $1 as yield compounds.

reUSD is best understood as the **senior tranche** of a two-token capital structure built on reinsurance cash flows: reUSD takes the safe, fixed coupon and is shielded by reUSDe, which absorbs first-loss underwriting risk in exchange for a higher variable yield. This is the same risk-tranching logic as a senior/junior credit structure or a stablecoin's safe/risky pairing, but with the underlying cash flow being **(re)insurance premiums** — an asset class largely uncorrelated to crypto and rates, which is the core appeal of the category.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | REUSD |
| **Market Cap Rank** | #187 |
| **Current Price** | $1.084 |
| **Market Cap** | $181.7M |
| **24h Volume** | $4.33M |
| **24h Change** | +0.01% |
| **Circulating / Total Supply** | 167.54M / 167.54M REUSD |
| **All-Time High** | $1.085 |
| **All-Time Low** | $0.8734 |
| **Categories** | Insurance, RWA, Ethereum / Base / Arbitrum / Avalanche / BNB / Ink Ecosystems |
| **Website** | [https://re.xyz](https://re.xyz) |

**On the "de-peg" question:** reUSD traded at **$1.084** — about 8.4% above $1 — and is at/near its ATH ($1.085). This is **by design, not a de-peg**: as a value-accruing deposit token, reUSD's price climbs above its $1 mint value as fixed yield compounds, similar to how a [[yield-bearing-stablecoin|yield-bearing / rebasing]] dollar trades above par. The ATL of $0.8734 reflects an early period before the accrual ramped and/or a stress drawdown; the asset should be read as a *yield claim*, not a hard $1 peg.

---

## Architecture — How reUSD Works

reUSD is a **value-accruing deposit token over a real-world-asset (reinsurance) cash flow**, structured as the senior, principal-protected tier of Re Protocol's two-token system.

### Collateral / backing model
- **Backing:** claims on **tokenized reinsurance contracts** underwritten through Re Protocol's pools — an insurance/RWA cash-flow stream rather than fiat reserves or crypto collateral. Capital deposited as reUSD is allocated to reinsurance underwriting; the premiums earned (net of claims) are the economic source of the token's yield.
- **Tranching:** reUSD is the **senior / principal-protected** claim. The junior tier ([[re-protocol-reusde|reUSDe]]) sits below it and absorbs underwriting losses first, which is what allows reUSD to be quoted as a fixed, lower-risk yield.

### Value-accrual / "peg" mechanism
- **Target:** **not** a fixed $1 peg. reUSD is a deposit token redeemable for its accrued NAV; its market price is expected to drift above $1 over time as yield accrues. At $1.084 (≈8.4% above mint value), the quote reflects accumulated yield, *not* a de-peg.
- **NAV anchor:** the price is anchored to net asset value rather than a $1 redemption guarantee; the stability mechanism is NAV redemption through the protocol plus secondary-market arbitrage against pool prices, not a hard dollar peg.

### Yield source
- **Yield source:** reinsurance underwriting premiums. The **reUSD** tier is structured as principal-protected fixed yield (risk-free rate + ~250 bps); the **reUSDe** tier takes first-loss underwriting risk for higher variable yield (~23% APR advertised). Figures kept qualitative. The yield is **uncorrelated to crypto funding rates or equity beta** — its driver is catastrophe/insurance-loss experience, which is the diversification pitch.

### Governance / redemption & gating
- **Governance / redemption:** the Cayman-based **Re Foundation** oversees governance and treasury; redemption is at NAV through the protocol, with integrations into [[curve-finance|Curve]], [[pendle|Pendle]] and [[ethena-usde|Ethena]] for secondary liquidity and yield-tokenization. Redemption at NAV can be subject to protocol gating/queueing given the illiquid nature of the underlying reinsurance contracts.

---

## Comparison vs Peer Yield-Bearing / RWA Dollars

| Dimension | **reUSD** (Re, senior) | [[re-protocol-reusde\|reUSDe]] (Re, junior) | sUSDe ([[ethena-usde\|Ethena]]) | [[usdu\|USDU]] (Unitas) |
|---|---|---|---|---|
| **Price model** | Value-accruing (>$1) | Value-accruing (>$1) | Value-accruing (>$1) | $1 peg |
| **Yield source** | Reinsurance premiums (fixed) | Reinsurance premiums (variable, first-loss) | Funding rate + staking | T-bill yield |
| **Risk tier** | Senior / principal-protected | Junior / first-loss | Single-tier synthetic | Reserve-backed |
| **Correlation to crypto** | Low (insurance-linked) | Low (insurance-linked) | High (funding-driven) | Low (rates-driven) |
| **Headline yield** | RFR + ~250 bps | up to ~23% APR | Variable funding | Short-end rate |
| **Chains** | ETH/Base/Arb/Avax/BNB/Ink | ETH (+) | ETH (+) | Solana/BNB |

reUSD's distinguishing feature versus other yield dollars is its **insurance-linked, low-correlation** cash flow and its **senior tranche** position — it trades safety for a capped fixed coupon, whereas reUSDe and sUSDe chase higher, riskier yield.

---

## How & Where It Trades / Is Used

- **Primary venue:** multi-chain DeFi, anchored on [[ethereum|Ethereum]] (`0x5086bf358635b81d8c47c66d1c8b9e567db70c72`) with deployments on Base, Arbitrum, Avalanche, BNB Chain and Ink; secondary liquidity via [[curve-finance|Curve]] and yield-tokenization via [[pendle|Pendle]].
- **DeFi composability:** the Pendle integration is significant — it lets holders split reUSD into principal (PT) and yield (YT) tokens, enabling fixed-rate lock-ins or leveraged yield exposure on the reinsurance cash flow. Curve pools provide the main on-chain swap liquidity, and the Ethena linkage offers additional venues.
- **Liquidity caveat:** ~$4.3M/24h volume against a ~$182M cap is healthier than the other names here, but liquidity is fragmented across six chains. Because reUSD trades *above* $1, buyers are paying for accrued yield — mispricing the accrual or thin pools on a given chain can create entry/exit slippage.

---

## Narrative / Category & Catalysts

reUSD sits in the **insurance-linked / RWA-yield** narrative — bringing reinsurance, a multi-trillion-dollar institutional asset class, on-chain as composable yield. Its pitch is *diversification*: a dollar-denominated yield whose driver (catastrophe-loss experience) is largely uncorrelated to crypto cycles and rate moves. Catalysts:

- **Demand for uncorrelated yield:** in a bottoming/accumulation crypto regime where funding-rate yields (sUSDe-style) compress, an insurance-linked fixed coupon stands out — a relative tailwind.
- **Pendle/Curve composability deepening:** more PT/YT and pool liquidity lowers the entry/exit friction that currently limits the senior tranche's appeal to passive allocators.
- **Reinsurance hard-market cycle:** when reinsurance premiums are rich (a "hard market" after large loss years), the underlying cash flow funding reUSD's coupon improves.
- **Soft-market / cat-loss headwind:** conversely, a benign-premium soft market or a major catastrophe-loss year stresses the cash flow — and in a severe enough event, even the senior tranche's "principal protection" can be tested.

---

## History / Timeline

- **2026-04-09** — Captured in the wiki via the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); page created.
- **2026-06-21** — Market-data refresh: price $1.084 (≈ATH $1.085), cap ~$181.7M, rank #187, ~$4.33M 24h volume; ATL of record $0.8734.
- **2026-06-23** — Page expanded to `excellent`.

> Note: only wiki-verified dates are listed; dated launch, audit, and partnership milestones are not yet ingested from a primary source and are deliberately omitted rather than fabricated.

---

## Risks

- **Underwriting / collateral risk:** the backing is reinsurance underwriting exposure. A catastrophe-loss spike or mis-priced risk pool can impair NAV — especially for the risk-bearing reUSDe tier, but a severe enough event can stress the "principal-protected" reUSD claim too.
- **Not a peg — valuation risk:** because reUSD accrues above $1, holders bear the risk that the quoted yield/NAV is not actually realized; the $0.8734 ATL shows the price can fall well below its accrued value under stress.
- **Issuer / governance risk:** dependence on Re Protocol and the Cayman-based Re Foundation for underwriting discipline, treasury management, and honoring redemptions at NAV.
- **Smart-contract / cross-chain risk:** six chains plus Curve/Pendle/Ethena integrations widen the attack surface (bridge and contract risk).
- **Regulatory risk:** tokenized (re)insurance and yield distribution sit at the intersection of insurance and securities regulation.
- **Macro backdrop:** as of 2026-06-21 the Crypto Fear & Greed Index read **23**; by the 2026-06-23 snapshot it sits at **21 (Extreme Fear)**, market-health 29/100, long-horizon regime **bottoming / accumulation**. Reinsurance cash flows are relatively uncorrelated to crypto, which is a relative strength in this regime, but bear-market liquidity withdrawal can still widen secondary spreads on the value-accruing token.

---

## Trading / Usage Playbook

- **Buy it for fixed, low-correlation yield — not for a $1 peg.** reUSD is the *safe tranche*; its appeal is a reinsurance-linked coupon (RFR + ~250 bps) that does not move with crypto funding. Do not size it as a dollar-par stablecoin.
- **Price > $1 is correct.** When valuing a position, mark to **accrued NAV**, not to $1. The ~8.4%-above-par quote is compounded yield; a fall toward $1 would signal NAV impairment, not a "return to peg."
- **Understand your tranche.** reUSD is shielded by reUSDe's first-loss buffer; a catastrophe-loss event large enough to exhaust that buffer is what threatens the senior coupon (see Risks).
- **Use Pendle to express a view:** lock a fixed rate via PT or take leveraged yield via YT if you want to trade the reinsurance carry rather than simply hold it.
- **Mind cross-chain fragmentation:** check which of the six deployments has the deepest pool before entering/exiting size; slippage differs sharply by chain.

> *Not financial advice. reUSD bears real underwriting and NAV risk; "principal-protected" is a structural claim, not a guarantee.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 167.54M REUSD |
| **Total Supply** | 167.54M REUSD |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | ~1.00 |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x5086bf358635b81d8c47c66d1c8b9e567db70c72` |
| Arbitrum One | `0x76ce01f0ef25aa66cc5f1e546a005e4a63b25609` |
| Base | `0x7d214438d0f27afccc23b3d1e1a53906ace5cfea` |
| Ink | `0x5bcf6b008bf80b9296238546bace1797657b05d6` |
| Binance Smart Chain | `0xba9425ec55ee0e72216d18e0ad8bbba2553bfb60` |
| Avalanche | `0x180af87b47bf272b2df59dccf2d76a6eafa625bf` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://re.xyz](https://re.xyz) |
| **Twitter** | [@re](https://twitter.com/re) |
| **Telegram** | [re_protocol](https://t.me/re_protocol) (53,708 members) |
| **Whitepaper** | [https://docs.re.xyz](https://docs.re.xyz) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.33M |
| **Market Cap Rank** | #187 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[stablecoin]] / [[stablecoins]]
- [[real-world-assets]]
- [[yield-bearing-stablecoin]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.
