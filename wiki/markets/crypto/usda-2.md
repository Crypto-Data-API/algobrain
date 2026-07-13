---
title: "USDa"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["USDA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.avalonfinance.xyz/"
related: ["[[stablecoins]]", "[[crypto-markets]]", "[[ethereum]]", "[[bitcoin]]", "[[dai]]"]
---

# USDa

**USDa** (ticker **USDA**) is a Bitcoin-backed, crypto-collateralised [[stablecoins|stablecoin]] issued by **Avalon Labs** through a CDP (Collateralized Debt Position) model on its CeDeFi lending platform. It targets a **1:1 peg to the US dollar** and is deployed on [[ethereum|Ethereum]], Mantle, and BNB Chain. As of the snapshot below it trades at **~$0.983, roughly 1.7% below its dollar peg** — a mild but notable discount that should be treated as a soft de-peg rather than a clean $1 asset.

> **Disambiguation:** This is **Avalon Labs' BTC-backed USDa** (CDP model). It is a *different asset* from the **AP Web3 / Alpha Partner USDA on BNB Chain** documented at [[usda-3]] (a fiat-backed exchange-style token) and from Angle's USDA. Same ticker, unrelated issuers — do not conflate their histories or de-pegs.

## Market data

| Field | Value |
|---|---|
| **Ticker** | USDA |
| **Price** | $0.9831 (≈1.7% below peg) |
| **Market cap** | $216.94M |
| **Market-cap rank** | #169 |
| **24h volume** | $0 (no reported on-snapshot volume) |
| **24h change** | n/a |
| **Circulating supply** | 220.67M USDA |
| **Total supply** | 220.67M USDA |
| **All-time high** | $1.021 (2025-01-13) |
| **All-time low** | $0.690 (2026-05-21) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

## Architecture — peg, backing & yield mechanism

USDa is a **crypto-collateralised CDP stablecoin** — closer in design to [[dai]] than to fiat-backed [[usdt]]/[[usdc]]. Users lock collateral (principally [[bitcoin|BTC]] and BTC-derived assets) in Avalon's lending platform and mint USDa as over-collateralised debt against it.

- **Collateral / reserve model:** the backing is **on-chain crypto collateral, dominated by BTC** (and BTC-derived/wrapped assets) rather than fiat reserves. Each USDa is issued against collateral worth *more* than the debt (over-collateralisation), giving a buffer against collateral price falls. This is a [[dai|Dai]]-style CDP architecture adapted to a Bitcoin-centric collateral base — Avalon's pitch is the **stablecoin layer of an "on-chain financial center for Bitcoin."**
- **Peg / stability mechanism:** the peg is defended by three forces working together — (1) **over-collateralisation** absorbs normal collateral volatility; (2) **liquidations** automatically close positions whose collateral ratio falls below the minimum, protecting solvency; and (3) **mint/redeem arbitrage** — when USDa trades below $1, borrowers are incentivised to buy it back cheaply to repay debt at par; when above $1, minting new USDa is attractive. The soft discount in the snapshot (~$0.983) and the ATL of $0.69 show this arbitrage has **not** held a hard peg under stress.
- **Mint / redeem & gating:** minting requires opening a CDP and posting collateral on Avalon's CeDeFi platform; redemption at par is done by **repaying USDa debt to unlock collateral**, not by a fiat wire. There is no fiat off-ramp — exits are either CDP repayment or selling into (thin) secondary liquidity.
- **Yield source:** USDa itself is the base dollar token (non-rebasing); **yield is earned by depositing/staking it within Avalon's products** (e.g. yield accounts), funded by borrowing demand and platform revenue, rather than a native rebase or pass-through Treasury coupon. This is distinct from RWA dollars (Treasury interest) and from synthetic dollars (funding carry).

Avalon markets USDa alongside BTC-backed lending, yield accounts, and a credit card, positioning it as the dollar unit of a Bitcoin-collateral ecosystem.

### Comparison vs peer crypto-backed & fiat dollars

| Token | Collateral / model | Peg defence | Key risk vs USDa |
|---|---|---|---|
| **USDa (Avalon)** | BTC-dominated CDP, over-collateralised | OC + liquidations + arbitrage | BTC-collateral cascade; thin liquidity; past de-peg to $0.69 |
| **[[dai]] (Maker/Sky)** | Diversified crypto + RWA CDP | OC + liquidations + PSM | More diversified collateral; deeper liquidity |
| **[[ethena-usde\|USDe]]** | Crypto + short perps (delta-neutral) | Funding-neutral hedge | Different engine (funding), not collateral cascade |
| **[[usdt]] / [[usdc]]** | Off-chain fiat + T-bills | Issuer 1:1 redemption | Centralised custody, but far deeper liquidity & tighter peg |

The cleanest peer is **[[dai]]**: same CDP logic, but USDa is far more **BTC-concentrated** and far **less liquid**, which is exactly why its peg has historically broken harder.

## De-peg note

The snapshot price of **$0.983** sits below the $1 target, and the all-time low of **$0.690 (2026-05-21)** shows USDa has experienced a **significant historical de-peg**. Combined with **zero reported 24h volume**, this indicates redemption-dependent / illiquid pricing: with no active two-sided market, the quoted price reflects last/stale prints rather than a tradeable $1. Do not treat USDa as a hard $1 asset at this snapshot.

## How / where it trades

Liquidity is **thin and redemption-dependent**. The snapshot reports **$0 of 24h volume**, and the primary venue noted is a Uniswap V3 (Ethereum) pool pairing USDa against [[usdt]]. With negligible secondary depth, the realistic way to exit at par is via the protocol's CDP redemption path (repaying debt / unwinding collateral), not by selling into a market. Any meaningful spot sale could move price well below the already-discounted quote.

DeFi composability is concentrated inside the **Avalon ecosystem** (lending, yield accounts) across [[ethereum|Ethereum]], Mantle and BNB Chain; USDa is not a widely-integrated collateral asset across third-party DeFi the way [[dai]]/[[usdc]] are, which compounds the liquidity problem.

## Tokenomics & supply

| Metric | Value |
|---|---|
| **Circulating supply** | 220.67M USDA |
| **Total supply** | 220.67M USDA |
| **Circulating / total** | ~1.00 |
| **Market cap** | $216.94M |
| **Market-cap rank** | #169 |

USDa supply is **debt-elastic**: it grows as users open CDPs and mint against BTC collateral, and shrinks as debt is repaid/liquidated. There is no fixed cap or vesting schedule — outstanding USDA equals outstanding over-collateralised debt across the platform. Because market cap reflects par value (~$1) times supply, the ~$217M figure tracks total minted debt, not a market valuation.

## Narrative / category & catalysts

USDa sits at the intersection of two narratives: **BTCfi / Bitcoin-collateral DeFi** (making idle BTC productive) and the **crypto-collateralised stablecoin** category. The pitch is "borrow dollars against your Bitcoin without selling it."

- **Catalysts (upside):** rising BTC prices improve collateral ratios and borrowing capacity; expansion of Avalon's BTCfi product suite (lending, card, yield); new-chain deployments and DeFi integrations that deepen liquidity.
- **Catalysts (downside):** BTC drawdowns (liquidation cascades), the current ~1.7% discount widening, or any failure to restore the peg after the 2026-05 break.

## History / Timeline

| Date | Event |
|---|---|
| **2025-01-13** | All-time **high ~$1.021** — a slight above-peg print consistent with healthy early demand. |
| **2026-05-21** | All-time **low ~$0.690** — a **severe de-peg** (~31% below par), the defining risk event for this asset. |
| **2026-06-21** | Trades ~**$0.983** (≈1.7% below peg) with **$0 reported 24h volume** — a soft, redemption-dependent discount; price is stale/illiquid rather than a tradeable $1. |

> **De-peg flag:** the ATL of ~$0.69 (2026-05-21) is a documented severe break, and the asset is *still* below par at the snapshot. Treat USDa as an **actively-soft-pegged** token, not a hard $1 asset.

## Trading playbook

- **Not a par-stable parking asset.** USDa is currently ~1.7% under peg with a recent collapse to $0.69; do not hold it as if it were [[usdc]]. If holding, do so to access Avalon's BTCfi yield, with eyes open on de-peg risk.
- **Exit is redemption, not the order book.** With ~$0 secondary volume, par exit means **repaying CDP debt to unlock collateral**; a spot sale of any size would print well below the quoted discount.
- **BTC-beta de-peg risk dominates.** The peg's health is a function of BTC collateral. In the current **Extreme Fear** tape (Fear & Greed 21; market-health 29/100; BTC ≈ $64,568, long-horizon regime = bottoming/accumulation), a sharp BTC leg-down is the scenario most likely to trigger liquidation cascades and widen the discount. The peg-restoration trade (buying the discount expecting return to $1) only works if collateral health and arbitrage hold — both have failed once already in 2026.

## Risks

- **De-peg risk (active):** Trading ~1.7% below peg now, with a documented drop to $0.69. Peg restoration depends on collateral health and arbitrage that may not function in stressed BTC markets.
- **Collateral / volatility risk:** BTC collateral is volatile; sharp BTC drawdowns can trigger cascading liquidations and undercollateralisation, especially in the current "Established Bear Market" backdrop (Fear & Greed 23).
- **Liquidity risk:** ~Zero secondary volume — exiting at par may be impossible without protocol redemption.
- **Issuer / smart-contract risk:** CeDeFi model concentrates trust in Avalon Labs' contracts, custody, and operations.
- **Regulatory risk:** Crypto-backed synthetic dollars face uncertain and tightening regulatory treatment.

## Platform & chain

Native chain: [[ethereum|Ethereum]]. Also on Mantle and BNB Chain.

| Chain | Contract |
|---|---|
| Ethereum | `0x8a60e489004ca22d775c5f2c657598278d17d9c2` |
| Mantle | `0x075df695b8e7f4361fa7f8c1426c63f11b06e326` |
| BNB Chain | `0x9356086146be5158e98ad827e21b5cf944699894` |

## See also

- [[stablecoins]] — category overview
- [[dai]] — peer crypto-collateralised CDP stablecoin
- [[ethena-usde]] — synthetic-dollar peer (different engine)
- [[usdt]], [[usdc]] — fiat-backed peers
- [[usda-3]] — *unrelated* AP Web3 USDA on BNB Chain (same ticker, different issuer)
- [[bitcoin]], [[crypto-markets]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.
