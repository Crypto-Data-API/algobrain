---
title: "Ethena"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi]
aliases: ["ENA", "Ethena Labs"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://www.ethena.fi/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[ethena-usde]]", "[[usdtb]]", "[[stablecoins]]", "[[hyperliquid]]", "[[funding-rates]]", "[[stablecoin-yields]]", "[[sky]]", "[[aave]]", "[[restaking]]", "[[decentralized-exchange]]"]
---

# Ethena

**Ethena** (governance token **ENA**) is the DeFi protocol behind [[ethena-usde|USDe]], the "synthetic dollar" that earns yield by holding crypto collateral and shorting BTC/ETH/SOL perps to harvest funding rates — at peak the largest crypto-native yield product, with USDe supply reaching roughly **$14.5B in late 2025** before correcting to ~$5.9B by March 2026. ENA matters to traders as a leveraged proxy on the perp funding-rate regime: when funding is rich, sUSDe yield and USDe supply expand and ENA rallies; when funding compresses or goes negative, the whole complex deflates. Key 2025 developments were the **fee-switch** push (routing protocol revenue to ENA), the **Converge** blockchain (ENA as staking asset), GENIUS-Act onshoring of sister stablecoin [[usdtb|USDtb]], and the **StablecoinX** Nasdaq treasury vehicle.

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.08843 |
| **Market Cap** | $821.60M |
| **Market Cap Rank** | #78 |
| **24h Volume** | $99.05M |
| **24h Change** | +1.44% |
| **7d Change** | +11.68% |
| **Circulating Supply** | 9.29B ENA (~62% of max) |
| **Total / Max Supply** | 15.00B / 15.00B ENA |
| **Fully Diluted Valuation** | $1.326B |
| **MC / FDV** | 0.62 |
| **All-Time High** | $1.52 (2024-04-11) — now ~-94.2% |
| **All-Time Low** | $0.07049 — now ~+25% above ATL |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

ENA rallied +11.7% on the week — in line with DeFi blue chips like [[aave|AAVE]] (+11.9%) and outperforming the broad tape, which is in **extreme fear** (Fear & Greed = 23, "Established Bear Market"). The bounce is consistent with the funding regime improving off the late-2025 deleveraging lows. The 0.62 MC/FDV flags meaningful dilution overhang: ~38% (~5.7B ENA) is still locked and subject to ongoing unlocks. High volume relative to market cap (~$99M/day vs ~$822M cap) keeps ENA one of the more liquid mid-cap perps and tokens here.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ENA |
| **Rank tier** | #78 (2026-06-20) |
| **Products** | USDe (synthetic dollar, delta-neutral basis trade), sUSDe (staked yield-bearing version), USDtb (treasury-backed stablecoin), iUSDe (planned TradFi wrapper), Converge chain |
| **USDe supply** | Peak ~$14.5B (late 2025); ~$5.9B by March 2026 (approximate) |
| **Supply mechanics** | 15B ENA max; ~9.29B circulating (2026-06-20), MC/FDV 0.62 — ongoing unlocks |
| **Backers** | Dragonfly, YZi Labs (ex-Binance Labs), Delphi, OKX Ventures, World Liberty Financial portfolio |
| **Market data** | $821.60M cap at $0.08843, rank #78 (2026-06-20) |
| **Website** | [https://www.ethena.fi/](https://www.ethena.fi/) |

---

## Overview

Ethena is a DeFi stablecoin-issuer project on [[ethereum|Ethereum]] (with the ENA token bridged across 18+ chains including Arbitrum, Base, Optimism, Avalanche, TON, Mantle, Blast and others). Its core product, USDe, generates yield from the cash-and-carry basis: long spot/staked collateral, short perpetual futures, capturing funding payments. Holders who stake into sUSDe receive this yield; the protocol also captures spread. ENA is the governance token, used for protocol votes, staking (sENA), and — since the Converge roadmap — as the staking token for the Converge Validator Network (CVN).

Ethena's design risk is well-understood by the market: sustained negative funding turns the carry trade unprofitable, which is why reserves can rotate into the treasury-backed [[usdtb|USDtb]] as a hedge, alongside an insurance ("reserve") fund.

---

## Protocol & Technology

Ethena's core is a **delta-neutral "cash-and-carry" basis trade**, productized as a token.

### How USDe is minted and stays delta-neutral

1. An authorized participant deposits crypto collateral (e.g., staked ETH / [[restaking|LST/LRT]], BTC, or stablecoins) and receives **USDe** 1:1 in dollar terms.
2. Ethena simultaneously opens an equal-size **short perpetual futures** position against that collateral on centralized venues.
3. The **long spot + short perp** combination is delta-neutral: if the collateral price moves, the spot gain/loss is offset by the perp loss/gain, so the net dollar value (the peg) is stable.
4. The position **earns funding** — in a positive-funding regime, perp shorts are *paid* by longs; plus any staking yield on the collateral.

### USDe vs sUSDe

| Token | What it is | Yield |
|---|---|---|
| **USDe** | The synthetic dollar; held for stability/payments; *not* yield-bearing by itself | None (peg only) |
| **sUSDe** | Staked USDe; accrues the protocol's carry yield via a vault | Variable; tracks funding + staking yield (double-digit in rich-funding regimes) |

Because not all USDe is staked, the spread between yield generated on the whole pool and yield paid only to sUSDe holders accrues to the protocol — this is the revenue stream the **fee switch** would route to ENA/sENA.

### Risk management and hedges

- **Negative-funding regimes** turn the carry unprofitable; Ethena can rotate reserves into the treasury-backed [[usdtb|USDtb]] (T-bill-style) as a hedge, and draws on an **insurance/reserve fund** to cover shortfalls.
- **Custody & counterparty** — collateral is held with off-exchange custody/settlement (OES) providers to limit direct exchange-failure exposure on the spot leg; the short legs still carry venue counterparty risk.
- **Peg defense** — USDe is *synthetic*, not fiat-redeemable in the GENIUS-Act sense; the peg relies on the hedge holding and on mint/redeem arbitrage. The October 2025 episode showed venue-specific depegs are possible under stress.

### ENA token and Converge

ENA is the governance token (votes, staking as **sENA**) and — per the **Converge** roadmap (with Securitize) — the staking asset securing the **Converge Validator Network (CVN)**, a TradFi/DeFi settlement chain. ENA is bridged across 18+ chains ([[arbitrum|Arbitrum]], Base, Optimism, Avalanche, TON, [[mantle|Mantle]], Blast and others).

---

## Major News & Events

- **April 2024** — ENA launched via Binance Launchpool; ATH $1.52 (2024-04-11).
- **2025 — Fee switch.** Ethena's governance milestones for activating revenue-sharing to ENA holders were tied to USDe scale and institutional adoption; the fee-switch countdown/activation became the dominant ENA-specific catalyst as USDe crossed the $12B TVL milestone in late 2025 (ainvest, CCN).
- **July 2025 — GENIUS Act onshoring.** Anchorage Digital agreed to issue Ethena's ~$1.5B USDtb in the US as the first GENIUS-compliant stablecoin (CoinDesk, 2025-07-24).
- **July 2025 — StablecoinX.** An ENA-accumulating treasury company ("StablecoinX") was announced with a planned Nasdaq listing (proposed ticker "USDE"), giving equity investors direct exposure to the Ethena ecosystem; listing remained pending into 2026.
- **Late 2025 — Converge.** Ethena (with Securitize) advanced Converge, a TradFi/DeFi settlement chain with ENA staking securing the Converge Validator Network.
- **Oct 2025 – Mar 2026 — Deleveraging.** After the October 2025 crypto deleveraging event and a soft funding regime, USDe supply contracted from ~$14.5B peak to ~$5.9B (March 2026); ENA fell to an ATL of $0.0769 (2026-04-05), -94% from ATH.

---

## Trading Relevance

- **ENA = levered funding-rate beta.** USDe supply and sUSDe yield are public, high-frequency fundamentals: expanding supply + double-digit sUSDe yield = bullish carry regime for ENA; supply contraction = direct revenue compression. Watch DefiLlama USDe TVL and the sUSDe yield as the primary dashboard.
- **Crowding indicator for everyone else:** sUSDe yield is effectively the market-wide perp funding composite — useful even if you never touch ENA (see [[funding-rates]], [[stablecoin-yields]]).
- **Venues:** spot on Binance, Kraken, Upbit, Bitget, KuCoin, Crypto.com; **ENA-PERP on [[hyperliquid|Hyperliquid]]** and major perp venues; deep liquidity (~$133M daily volume at the April 2026 snapshot).
- **Catalysts:** fee-switch value accrual to sENA, Converge mainnet adoption, StablecoinX Nasdaq listing, USDe re-expansion in a positive-funding regime, unlock schedule (MC/FDV 0.58).
- **Risks:** sustained negative funding, a USDe depeg/redemption spiral (the October 2025 episode demonstrated venue-specific depegs), exchange counterparty risk on the short legs, and regulatory treatment of yield-bearing synthetic dollars.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 9.29B ENA (~62% of max) |
| **Total Supply** | 15.00B ENA |
| **Max Supply** | 15.00B ENA |
| **Fully Diluted Valuation** | $1.326B |
| **Market Cap / FDV Ratio** | 0.62 |

**Dilution flag (HIGH).** With MC/FDV at 0.62, ~38% (~5.7B ENA) is still locked. ENA launched April 2024 via Binance Launchpool with large allocations to investors, the core team, the foundation, and ecosystem/airdrops, vesting over multi-year schedules — so **ongoing unlocks** are a persistent supply headwind that any ENA thesis must net against. Circulating supply rose from ~8.76B (April 2026) to ~9.29B (June 2026), confirming the live emission. The **fee switch** (routing protocol revenue to ENA/sENA) is the demand-side mechanism meant to offset this dilution.

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.08843 |
| **All-Time High** | $1.52 (2024-04-11) — now ~-94.2% |
| **All-Time Low** | $0.07049 — price ~+25% above ATL |
| **7d Change** | +11.68% (DeFi-basket strength) |
| **24h Volume** | $99.05M |

---

## Ecosystem & Use Cases

- **Synthetic dollar (USDe)** — a crypto-native, scalable dollar that does not depend on a bank issuer; used as collateral, a settlement asset, and a savings instrument across [[defi|DeFi]].
- **Yield (sUSDe)** — the flagship draw: staked USDe pays the carry yield, making sUSDe one of the largest on-chain "real yield" instruments.
- **USDtb** — treasury-backed (T-bill) stablecoin issued in the US under the GENIUS Act via Anchorage; doubles as Ethena's **negative-funding hedge**.
- **Integrations** — USDe/sUSDe are integrated as collateral and yield assets across lending and DEX protocols (including [[aave|Aave]]'s Horizon RWA market and broad [[decentralized-exchange|DEX]] liquidity).
- **Converge** — a TradFi/DeFi settlement chain (with Securitize) using ENA staking for validator security.
- **iUSDe** — a planned TradFi-wrapped version targeting institutional allocators.

---

## Market Structure & Derivatives

- **Spot venues** — [[binance|Binance]] (ENA/USDT), [[kraken|Kraken]], Upbit (KRW), Bitget, KuCoin, Crypto.com; on-chain on Uniswap V3 (ENA/WETH). 24h spot volume ~$99M (2026-06-20) — high turnover for the cap.
- **Perpetuals** — ENA-PERP on [[hyperliquid|Hyperliquid]], Binance Futures, Bybit, OKX; ENA is a liquid, high-beta perp.
- **The meta-trade** — ENA is itself the *governance proxy on the perp funding-rate regime*, while Ethena's protocol is the largest single short-perp participant in crypto. So ENA's price, sUSDe yield, and aggregate market funding are tightly linked.
- **sUSDe yield as a market signal** — sUSDe yield is effectively a **market-wide perp funding composite**, useful even to traders who never touch ENA (see [[funding-rates]], [[stablecoin-yields]]). Rising sUSDe yield = rich funding = bullish carry regime; collapsing/negative = revenue compression and depeg risk.

---

## Valuation Framework

ENA is valuable only insofar as protocol revenue reaches the token (via the fee switch). Lenses (describe, do not invent values):

- **USDe supply / TVL** — the revenue base; track DefiLlama USDe TVL. Supply expansion (toward the ~$14.5B peak) vs contraction (toward the ~$5.9B March-2026 trough) is the single most important driver.
- **sUSDe yield** — the carry the protocol harvests; high yield in rich-funding regimes scales revenue.
- **Protocol revenue & take rate** — yield generated on the whole pool minus yield paid to sUSDe; the residual is protocol revenue. Apply a P/S or P/E lens vs the fee-switch share.
- **Fee-switch status** — whether/when revenue is routed to ENA/sENA is the binary that converts protocol economics into token value.
- **MC/FDV (0.62)** — apply the dilution adjustment; net any revenue/buyback against ongoing unlocks.

---

## Trading Playbook

- **ENA = levered funding-rate beta.** Expanding USDe supply + double-digit sUSDe yield = bullish carry regime for ENA; supply contraction = direct revenue compression. Primary dashboard: DefiLlama USDe TVL and sUSDe yield.
- **Macro context** — in the current **extreme-fear / Established Bear Market** regime, ENA bounces with the DeFi basket when funding firms (the +11.7% week here), but is high-beta to any renewed deleveraging.
- **Catalysts (bull)** — fee-switch value accrual to sENA, Converge mainnet adoption, StablecoinX Nasdaq listing, USDe re-expansion in a positive-funding regime.
- **Catalysts (bear)** — sustained negative funding, USDe depeg/redemption spiral, exchange counterparty failure on the short legs, regulatory action on yield-bearing synthetic dollars, and unlock cliffs (MC/FDV 0.62).
- **Cross-asset use** — even non-holders should watch sUSDe yield as a crowding/funding gauge for the whole market.

---

## History

- **2023** — Ethena Labs founded (Guy Young); raised from Dragonfly, YZi Labs (ex-Binance Labs), Delphi, OKX Ventures.
- **Feb 2024** — USDe mainnet; the "Internet Bond" synthetic dollar.
- **Apr 2024** — ENA launches via Binance Launchpool; ATH $1.52 (Apr 11).
- **2024–25** — USDe scales rapidly on rich funding; multi-chain ENA expansion.
- **Jul 2025** — GENIUS-Act onshoring of [[usdtb|USDtb]] (~$1.5B) via Anchorage; **StablecoinX** Nasdaq treasury vehicle announced.
- **Late 2025** — USDe peaks ~$14.5B; **Converge** chain advanced with Securitize; fee-switch countdown dominates ENA catalysts.
- **Oct 2025 – Mar 2026** — October deleveraging + soft funding contract USDe to ~$5.9B; ENA ATL $0.07049.
- **2026** — recovery attempts tied to the funding regime; +11.7% week into 2026-06-20.

---

## Competitive Positioning

| Issuer | Token / Dollar | Backing model | Differentiator vs Ethena |
|---|---|---|---|
| **Ethena** | ENA / USDe | Delta-neutral basis (long spot + short perp) | Highest native yield; funding-rate dependent; not fiat-redeemable |
| [[sky\|Sky]] (ex-Maker) | SKY / USDS | Crypto + RWA (T-bill) overcollateralized | Overcollateralized & DAO-governed; yield from RWA/stability fees, not funding |
| [[aave\|Aave]] | AAVE / GHO | Overcollateralized crypto-backed | Issued against money-market collateral; protocol-captured stability fee |
| Fiat-backed (USDT/USDC) | — | 1:1 fiat/T-bill reserves | Fully redeemable, no native yield to holders; regulated under GENIUS Act |
| Other synthetic dollars | — | Various delta-neutral / algorithmic | Ethena is the largest and most battle-tested synthetic dollar |

Ethena's edge is **yield and scale**: USDe offers the highest sustainable on-chain dollar yield in rich-funding regimes. Its structural weakness vs overcollateralized ([[sky|USDS]], [[aave|GHO]]) and fiat-backed (USDC/USDT) dollars is that the yield — and ultimately the peg under stress — depends on the perp funding regime holding up.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x57e114b691db790c35207b2e685d4a43181e6061` |
| Mantle | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Metis Andromeda | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Fraxtal | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Kava | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Zircuit | `0x813635891aa06bd55036bbd8f7d1a34ab3de9a0f` |
| Swellchain | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Morph L2 | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Scroll | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Mode | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| zkSync | `0x686b311f82b407f0be842652a98e5619f64cc25f` |
| The Open Network | `EQAPh9RCprgg5kKumtJi8uB7nFKctPBwuRUu82JgTGmzklNV` |
| Base | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Arbitrum One | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Manta Pacific | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Blast | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Optimistic Ethereum | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |
| Avalanche | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | ENA/USDT |
| Kraken | ENA/USD |
| Upbit | ENA/KRW |
| Bitget | ENA/USDT |
| KuCoin | ENA/USDT |
| Crypto.com Exchange | ENA/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ENA-PERP | Perpetual |
| Uniswap V3 (Ethereum) | ENA/WETH | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.ethena.fi/](https://www.ethena.fi/) |
| **Twitter** | [@ethena_labs](https://twitter.com/ethena_labs) |
| **Telegram** | [ethena_labs](https://t.me/ethena_labs) (17,943 members, April 2026) |
| **Docs** | [https://ethena-labs.gitbook.io/](https://ethena-labs.gitbook.io/) |

---

## Risks

- **Funding-rate dependence (HIGH)** — sustained negative funding turns the carry unprofitable, compressing sUSDe yield and shrinking USDe supply (and protocol revenue) directly.
- **Depeg / redemption spiral** — USDe is synthetic, not fiat-redeemable; the October 2025 episode showed venue-specific depegs under stress. A run could force loss-making hedge unwinds.
- **Counterparty / exchange risk** — the short legs sit on centralized perp venues; an exchange failure or forced position closure impairs the hedge despite off-exchange custody.
- **Dilution (HIGH)** — ~38% of ENA still locked; multi-year unlocks are a persistent supply headwind.
- **Regulatory** — yield-bearing synthetic dollars face uncertain treatment; USDtb is GENIUS-compliant but USDe itself is not a fiat-backed regulated stablecoin.
- **Fee-switch execution** — if revenue is never durably routed to ENA, the token may not capture protocol value.
- **Macro beta** — high-beta in an **Established Bear Market** / extreme-fear regime; bounces are sharp but reversible.

---

## Related

- [[ethena-usde]] — the protocol's core product
- [[usdtb]] — Ethena's treasury-backed stablecoin and negative-funding hedge
- [[stablecoins]], [[stablecoin-yields]], [[funding-rates]]
- [[sky]] — overcollateralized stablecoin peer (USDS)
- [[aave]] — overcollateralized stablecoin peer (GHO); Horizon RWA partner
- [[restaking]] — LST/LRT collateral context
- [[decentralized-exchange]] — on-chain venue context
- [[hyperliquid]] — ENA-PERP venue
- [[crypto-markets]], [[ethereum]]

---

## Sources

- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko): price $0.08843, mcap $821.60M, rank #78, vol $99.05M, 24h +1.44%, 7d +11.68%, FDV $1.326B, MC/FDV 0.62.
- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- ainvest (Sep 2025): Ethena's fee switch and USDe's $12B milestone — https://www.ainvest.com/news/ethena-fee-switch-usde-12b-milestone-era-defi-governance-yield-innovation-2509/
- CCN: Ethena network growth, fee-switch countdown — https://www.ccn.com/analysis/crypto/ethena-ena-network-activity-fee-switch-price-impact/
- CoinDesk (2025-07-24): Ethena taps Anchorage to issue $1.5B USDtb under GENIUS Act — https://www.coindesk.com/business/2025/07/24/ethena-taps-anchorage-to-issue-usd1-5b-usdtb-stablecoin-in-u-s-under-genius-act
- BeInCrypto: Ethena USDe stablecoin growth (peak $14.5B, ~$5.92B March 2026) — https://beincrypto.com/ethena-usde-stablecoin-growth/
- DefiLlama USDe dashboard — https://defillama.com/stablecoin/ethena-usde
- Verified via Perplexity sonar + web search, 2026-06-10.
