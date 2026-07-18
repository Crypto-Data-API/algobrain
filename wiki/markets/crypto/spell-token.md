---
title: "Spell (Abracadabra.money)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, lending, stablecoins]
aliases: ["Abracadabra.money", "MIM", "SPELL", "Spell Token"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://abracadabra.money/"
related: ["[[arbitrum]]", "[[avalanche]]", "[[binance]]", "[[collateralized-debt-position]]", "[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[lending]]", "[[liquity]]", "[[makerdao]]", "[[stablecoin]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-yield]]"]
---

# Spell (Abracadabra.money)

**Spell** (SPELL) is the governance and incentive token of **Abracadabra.money**, a multi-chain DeFi [[lending|lending]] protocol that lets users deposit interest-bearing and other collateral to **mint MIM (Magic Internet Money)**, a USD-pegged [[stablecoin|stablecoin]]. MIM is created via isolated [[collateralized-debt-position|collateralized debt positions]] (called "cauldrons"). As of 2026-06-22 SPELL trades at **$0.00011811**, ranking **#823** by market capitalization with a market cap of roughly **$20.24M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* SPELL: $0.00011811, rank #823, market cap $20,244,959, 24h -2.27%, 7d -8.22%. Market backdrop: Fear & Greed Index at 21 (Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SPELL |
| **Market Cap Rank** | #823 |
| **Market Cap** | $20,244,959 |
| **Current Price** | $0.00011811 |
| **24h Change** | -2.27% |
| **7d Change** | -8.22% |
| **Protocol** | Abracadabra.money |
| **Stablecoin** | MIM (Magic Internet Money), USD-pegged |
| **Collateral model** | Isolated CDP "cauldrons", interest-bearing collateral |
| **Categories** | DeFi, Yield Farming, Stablecoin Issuer, multi-chain (Ethereum, Avalanche, Fantom, Arbitrum) |
| **Website** | [https://abracadabra.money/](https://abracadabra.money/) |

> In the 2026-06-22 [[crypto-market-regime|bear regime]] (Fear & Greed 21, Extreme Fear), SPELL was down -2.27% on the day and -8.22% on the week — weak, low-conviction trading typical of a damaged-narrative DeFi token.

---

## Overview

Abracadabra.money launched in 2021 and rose to prominence by accepting **yield-bearing / interest-bearing assets** as collateral (for example wrapped staked tokens and Yearn vault shares), allowing users to unlock liquidity against productive collateral by minting the **MIM** stablecoin. Each market is an isolated **"cauldron"** with its own collateral type, loan-to-value, interest rate, and liquidation parameters — an isolated-risk [[collateralized-debt-position|CDP]] design that limits contagion between markets.

There are two tokens in the system:
- **MIM** — the USD-pegged stablecoin minted against collateral (debt instrument).
- **SPELL** — the **governance and incentive token**. SPELL can be staked as **sSPELL** to earn a share of protocol fees and to participate in governance; it is also used to incentivize MIM liquidity. SPELL holders govern protocol parameters and risk settings.

The protocol was strongly associated with the broader 2021 DeFi "degen" wave and with figures including the pseudonymous "Daniele Sestagalli" ecosystem (also linked to Wonderland/TIME), which later became a source of governance controversy.

---

## Mechanism & Architecture (cauldrons in depth)

Abracadabra's lending engine is built on **isolated "cauldron" markets**, each a self-contained [[collateralized-debt-position|CDP]] vault with its own parameters. The key design choices:

- **Isolated collateral, shared debt token** — every cauldron accepts exactly one collateral type and mints the same protocol-wide stablecoin, MIM. Because cauldrons are isolated, a bad-debt event in one (e.g., an exotic LP token cauldron) does not directly cascade into the collateral of another. This is the same isolation philosophy used by [[liquity|Liquity]] troves but with heterogeneous collateral like [[makerdao|MakerDAO]].
- **Per-cauldron risk parameters** — each market sets its own **maximum collateralization ratio (LTV / "MCR")**, **liquidation threshold**, **borrow fee**, **interest rate**, and **liquidation penalty**. Aggressive cauldrons (high LTV on volatile collateral) carry more bad-debt risk; conservative cauldrons resemble a standard money market.
- **Interest-bearing collateral as the original edge** — Abracadabra's differentiator was accepting **productive collateral** (yvUSDC, stETH-style wrappers, GLP, Yearn vault shares, Curve LP tokens). A user could keep earning yield on the deposited asset *and* borrow MIM against it, effectively levering a yield position. This is more capital-efficient than CDPs that only accept idle collateral.
- **Liquidations** — when a position breaches its liquidation threshold, liquidators repay the MIM debt and seize collateral at a discount (the liquidation penalty), restoring solvency. As with all CDP systems, liquidation reliability depends on accurate oracles and liquid collateral.
- **DegenBox / BentoBox** — Abracadabra reuses Sushi's BentoBox vault primitive (rebranded "DegenBox") so deposited assets can be put to secondary use and flash-loaned, increasing capital efficiency but also surface area for bugs.

### The MIM peg mechanism

MIM is **over-collateralized soft-pegged** to $1. The peg is maintained by (1) arbitrage against the cauldron mint/redeem mechanics, (2) deep MIM liquidity on [[curve-finance|Curve]] (the MIM-3CRV pool historically), and (3) the protocol's ability to adjust cauldron parameters and incentivize liquidity. Unlike a fully redeemable fiat-backed [[stablecoin]], MIM has no centralized 1:1 redemption guarantee — its stability rests entirely on collateral quality and market liquidity, which is precisely why it has depegged under stress.

---

## Notable History (told honestly)

Abracadabra/MIM has a materially mixed track record that is central to understanding the token:

- **2022 stress and depeg episodes:** During the 2022 crypto deleveraging — including the Terra/UST collapse and the subsequent credit crunch — MIM came under pressure and **briefly lost its $1 peg**. A significant portion of MIM was backed by exposure to assets and venues that became distressed, and the protocol had to wind down risky positions. Bad debt concerns and reliance on certain collateral types damaged confidence. The Wonderland (TIME) governance scandal involving an associated team member further hurt the ecosystem's reputation.
- **2024 exploit:** In **2024, Abracadabra suffered a smart-contract exploit affecting its cauldrons, with losses on the order of several million dollars (reported around ~$6.5M)**. The attack exploited a flaw in the cauldron lending/borrowing logic, allowing the attacker to borrow MIM without sufficient backing, which pressured the MIM peg and required protocol response. This reinforced the perception of elevated smart-contract and design risk.

These events are recorded here rather than omitted because they are the dominant risk facts for both MIM and SPELL.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~171.51B SPELL |
| **Total Supply** | ~196.01B SPELL |
| **Max Supply** | 210.00B SPELL |
| **Fully Diluted Valuation** | ~$25M (scales with price) |
| **Market Cap / FDV Ratio** | ~0.84 |

SPELL has a very large supply (max 210 billion), which is why each token is priced in fractions of a cent. Most supply is already circulating. SPELL's value is tied to protocol fee generation (which flows to sSPELL stakers) and to the health and adoption of the MIM stablecoin.

### Value accrual & governance (sSPELL / mSPELL)

- **sSPELL (staked SPELL)** — staking SPELL mints sSPELL, which accrues a share of protocol revenue. Historically the protocol directed **borrow-fee and interest income** (a cut of the fees paid by MIM borrowers) into buying SPELL on the open market and distributing it to sSPELL stakers, creating a buyback-and-distribute loop. The yield is therefore directly proportional to MIM borrowing demand: high utilization → high fees → high sSPELL yield, and vice versa.
- **mSPELL** — a separate staking module used at various points for fee distribution / governance participation, distinct from the auto-compounding sSPELL.
- **Governance scope** — SPELL holders vote (typically via forum signaling and on-chain execution) on which cauldrons to launch, their risk parameters, interest rates, treasury use, and incentive emissions. Governance is the lever that determines how aggressive the protocol's collateral acceptance is — the central risk decision in a CDP system.
- **Reflexivity** — SPELL's value is **reflexive** with MIM health: a healthy, widely-used MIM generates fees that support sSPELL yield and SPELL demand; a depeg or bad-debt event simultaneously kills fee income *and* token sentiment, which is why SPELL has been so deeply de-rated.

---

## Worked Example (illustrative)

A user holds $10,000 of a yield-bearing collateral asset accepted by a cauldron with a **75% maximum LTV** and a **liquidation threshold of ~80%**:

1. Deposit $10,000 of collateral into the cauldron. The asset keeps earning its native yield.
2. Borrow up to **$7,500 MIM** (75% LTV). A more conservative borrow of, say, **$5,000 MIM (50% LTV)** leaves a larger safety buffer.
3. Pay the cauldron's one-time **borrow fee** plus ongoing **interest** on the MIM debt.
4. Deploy the MIM (e.g., swap to stablecoins, provide liquidity, or buy more of the collateral asset to lever the yield).
5. **Liquidation trigger:** if collateral value falls such that debt/collateral exceeds the liquidation threshold (~80%), a liquidator repays the MIM and seizes collateral at a discount, plus a penalty. With the conservative 50% LTV position, collateral could fall ~37% before liquidation; the aggressive 75% position has almost no buffer.

This illustrates both the appeal (borrow against productive collateral without selling it) and the danger (thin liquidation buffers on volatile collateral, the failure mode behind Abracadabra's bad-debt episodes). *Figures are illustrative, not live protocol parameters.*

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0351 (2021-11-02) |
| **Current vs ATH** | ~-99.7% |
| **24h Change** | -2.27% |
| **7d Change** | -8.22% |

SPELL trades more than 99% below its November 2021 ATH. The cumulative impact of the 2022 depeg stress, the Wonderland governance scandal, and the 2024 cauldron exploit has kept the token deeply de-rated, with little sign of a sustained recovery into 2026-06-22.

---

## Competitive Position

Abracadabra/MIM competes in the **decentralized stablecoin / CDP** category against [[makerdao|MakerDAO/Sky (DAI/USDS)]], [[liquity|Liquity (LUSD)]], crvUSD, and others. Its historical niche — accepting yield-bearing collateral to mint a stablecoin — was genuinely innovative, but its peg incidents and exploit history left it well behind the category leaders in trust and TVL. MIM persists as a niche stablecoin rather than a major one.

### Comparison vs CDP stablecoin peers

| Protocol | Stablecoin | Collateral model | Governance token | Differentiator | Peg / risk track record |
|---|---|---|---|---|---|
| **Abracadabra** | MIM | Isolated cauldrons, **yield-bearing collateral** | SPELL | Borrow against productive/exotic collateral | Depegged 2022; ~$6.5M cauldron exploit 2024 |
| [[makerdao\|MakerDAO/Sky]] | DAI / USDS | Multi-collateral vaults + RWA + PSM | MKR / SKY | Largest decentralized stablecoin; deep RWA & PSM | Strongest track record; held peg through 2022 |
| [[liquity\|Liquity]] | LUSD / BOLD | ETH-only (v1), immutable, no governance | LQTY | Minimal-governance, redemption-enforced peg | Robust, conservative; ETH-only constraint |
| crvUSD ([[curve-finance\|Curve]]) | crvUSD | LLAMMA soft-liquidation AMM | CRV | Gradual "soft" liquidations via AMM | Newer; resilient soft-liquidation design |

Abracadabra is the most aggressive of the group on collateral acceptance, which historically gave it the highest capital efficiency and the worst tail-risk outcomes.

---

## Risks

- **Stablecoin peg risk:** MIM has depegged under stress before; the peg depends on collateral quality, redemption mechanics, and confidence — all of which can fail quickly.
- **Smart-contract risk:** Demonstrated by the 2024 cauldron exploit; complex CDP logic is a recurring attack surface.
- **Collateral / bad-debt risk:** Accepting exotic yield-bearing collateral raises the chance of under-collateralization in a crash.
- **Reputational / governance risk:** Past scandals (Wonderland) weigh on trust and adoption.
- **Value-accrual dependence:** SPELL only accrues value if MIM borrowing demand and fees recover; in a low-demand environment, sSPELL yields and SPELL's value are weak.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x090185f2135308bad17527004364ebcc2d37e5f6` |
| Fantom | `0x468003b688943977e6130f4f68f23aad939a1040` |
| Arbitrum One | `0x3e6648c5a70a150a88bce65f4ad4d506fe15d2af` |
| Avalanche | `0xce1bffbd5374dac86a2893119683f4911a2f7814` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SPELL/USDT | N/A |
| Kraken | SPELL/USD | N/A |
| Bitget | SPELL/USDT | N/A |
| Crypto.com Exchange | SPELL/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Sushiswap | 0X090185F2135308BAD17527004364EBCC2D37E5F6/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://abracadabra.money/](https://abracadabra.money/) |
| **Twitter** | [@MIM_Spell](https://twitter.com/MIM_Spell) |
| **Telegram** | [abracadabramoney](https://t.me/abracadabramoney) (2,105 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.42M |
| **Market Cap Rank** | #792 |
| **24h Range** | $0.00015777 — $0.00016332 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

SPELL trades on [[binance]] (SPELL/USDT) and other centralized venues, with the SushiSwap SPELL/WETH pool as the main on-chain market. Note that SPELL is the **governance/incentive token**, not the stablecoin — the USD-pegged asset in this system is **MIM**, and SPELL's price is *reflexively* driven by MIM peg health, borrowing demand, and sSPELL fee flows. Practically, the peg / cash-management angle applies to the underlying MIM instrument (peg stability, backing/reserves, depeg risk, and yield/arbitrage), while SPELL itself is a thinly-liquid, deeply de-rated directional proxy on that peg's fortunes. Very low unit price (fractions of a cent) and modest 24h volume mean wide relative spreads and high slippage on size; spot venue availability, not on-chain leverage, is what caps realistic position sizing here. Because SPELL is small-cap and lightly supported, execution should assume liquidity can thin out fast during MIM stress events.

### Applicable strategies

The following peg/stablecoin strategies apply primarily to the **MIM** stablecoin that Abracadabra issues (and thus indirectly to SPELL as a reflexive governance claim on that peg):

- [[stablecoin-depeg-profit-capture]] — MIM has depegged under stress (2022, and post-2024 exploit pressure); accumulating MIM below $1 into a credible re-peg is the classic play, with SPELL as a higher-beta directional expression.
- [[synthetic-stablecoin-depeg-arbitrage]] — MIM is an over-collateralized *synthetic* stablecoin with no fiat 1:1 redemption, so depeg arbitrage keys off collateral quality and Curve liquidity rather than a bank redemption.
- [[mint-parity-arbitrage]] — the cauldron mint/repay mechanics let arbitrageurs mint or repay MIM to nudge it back toward $1, the core mechanism holding the peg.
- [[stablecoin-pair-arbitrage]] — MIM-vs-USDC/USDT/DAI spreads (historically via the MIM-3CRV Curve pool) offer basis capture when MIM drifts off peg against fiat-backed stables.
- [[stablecoin-yield]] — MIM/sSPELL yields track MIM borrowing demand; SPELL's value accrual is tied to that fee stream, making yield a driver of the token itself.
- [[carry-trade]] — borrowing MIM against yield-bearing cauldron collateral is a levered carry on productive assets, the protocol's original edge and its dominant failure mode.

### Volatility & regime character

Two distinct regimes: the **MIM peg** is normally tight around $1 but has broken under system stress (2022 deleveraging, and pressure around the ~$6.5M 2024 cauldron exploit), because backing is over-collateralized CDP debt on exotic/yield-bearing collateral with no centralized redemption. **SPELL** itself is highly volatile and directional — down more than 99% from its 2021 ATH — with price reflexively amplifying any MIM peg wobble, fee-income change, or governance/reputational shock. Redemption mechanics for MIM are indirect (repay debt in cauldrons, arbitrage on Curve) rather than an on-demand fiat window, so peg recovery depends on market liquidity and confidence, not a hard backstop.

### Risk flags

- **Depeg risk:** MIM's peg rests on collateral quality and Curve liquidity, not a redemption guarantee — it has broken before and can break again quickly.
- **Reserve / backing transparency:** backing is a shifting mix of CDP collateral across cauldrons (including exotic yield-bearing assets), so effective reserve quality is harder to assess than a fiat-backed stablecoin.
- **Redemption gating:** no direct 1:1 redemption; exiting depends on cauldron repayment and secondary-market liquidity, which can gate under stress.
- **Smart-contract & reputational risk:** the 2024 cauldron exploit and the Wonderland governance scandal both pressured the peg and sentiment — recurring tail risks for anyone holding MIM or SPELL.
- **Regulatory:** decentralized stablecoin issuance faces evolving regulatory scrutiny that could affect MIM demand and SPELL fee accrual.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SPELLUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=SPELLUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SPELLUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=SPELLUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[stablecoin]]
- [[collateralized-debt-position]]
- [[lending]]
- [[makerdao]]
- [[liquity]]
- [[curve-finance]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
