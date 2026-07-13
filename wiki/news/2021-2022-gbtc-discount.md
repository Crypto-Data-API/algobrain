---
title: "GBTC Premium-to-Discount Flip — The Trade That Killed 3AC"
type: news
created: 2026-04-24
updated: 2026-07-13
status: good
tags: [news, arbitrage, crypto, etf, bitcoin, history]
event_date: 2022-12-01
markets_affected: [crypto, etf]
impact: high
verified: true
sources_count: 6
related:
  - "[[cryptodataapi]]"
  - "[[gbtc-discount-arbitrage]]"
  - "[[bankruptcy-claim-arbitrage]]"
  - "[[2022-05-terra-luna-depeg-arb]]"
  - "[[bitcoin]]"
---

# GBTC Premium-to-Discount Flip -- The Trade That Killed 3AC

The Grayscale Bitcoin Trust (GBTC) traded at a persistent **+20-40% premium to NAV** through 2020 and early 2021, making it one of the most lucrative structured arbitrage trades in crypto history. In **February 2021** the premium flipped to a discount, deepened to **-49% by December 2022**, and became the catalyst that destroyed Three Arrows Capital, BlockFi, Celsius, Voyager, and Genesis. When the SEC finally approved spot Bitcoin ETFs on **January 11, 2024**, the discount collapsed to par -- rewarding traders who bought GBTC late 2022 with **60%+ returns** in 12-15 months.

## Background -- The Premium Era (2017-2021)

GBTC was the only US-listed Bitcoin product available in tax-advantaged accounts (IRAs, 401ks) for years. Demand from accredited investors and institutions who could not custody [[bitcoin]] directly drove GBTC shares to trade well above the value of the underlying BTC.

The structure created a one-way arbitrage:

- **Accredited investors** could create new GBTC shares by depositing BTC at NAV (creation-in-kind).
- Newly created shares were locked for **6 months** under SEC Rule 144.
- During the lockup, the trader earned the persistent premium plus any BTC appreciation.
- After 6 months, shares unlocked and could be sold on the secondary market at a (then) +20-40% premium.

At its peak in **December 2020**, the premium reached **~40%**. With 6-month lockups, a leveraged position could compound a remarkable spread. Hedge funds including Three Arrows Capital ([[three-arrows-capital]]), BlockFi, and Genesis built massive positions, often financed with [[bitcoin]] borrowed at 4-8% from retail platforms (Celsius, Voyager, BlockFi).

## The Flip -- February 23, 2021

The premium evaporated almost overnight. Catalysts:

- **Purpose Bitcoin ETF** (Canada) launched **February 18, 2021** -- the first North American spot BTC ETF, drawing assets immediately.
- US ETF filings from VanEck, WisdomTree, and others reignited expectations of a US spot ETF.
- The 6-month lockup pipeline meant supply of unlocked shares hitting the market exceeded organic demand.

By **February 23, 2021**, the premium turned negative. The discount widened steadily through 2021 and 2022:

| Date | Discount/Premium | BTC Price | Notes |
|------|-----------------|-----------|-------|
| Dec 2020 | +40% | $29K | Peak premium |
| Feb 23, 2021 | 0% | $48K | Flip date |
| May 2021 | -15% | $37K | China ban, deleveraging |
| Mid-2022 | -25% | $20K | LUNA fallout |
| Jun 2022 | -34% | $19K | 3AC liquidations |
| Nov 2022 | -45% | $16K | FTX collapse |
| **Dec 2022** | **-49%** | **$16.5K** | **Cycle bottom** |
| Aug 2023 | -25% | $26K | Grayscale wins lawsuit vs SEC |
| Jan 11, 2024 | ~0% | $46K | Spot ETF approval, conversion |

## The 3AC Catastrophe

[[three-arrows-capital|Three Arrows Capital]] (3AC) -- managing roughly **$10 billion** at peak -- was the most exposed entity. Founders Su Zhu and Kyle Davies had run the GBTC premium trade aggressively, financed with borrowed BTC. As the discount widened through 2021 and 2022, the trade went from "low risk yield" to a deepening unrealized loss.

When [[2022-05-terra-luna-depeg-arb|Terra/LUNA collapsed in May 2022]], 3AC's $200M LUNA position evaporated. Already capital-impaired, the GBTC discount widening below -30% pushed them into insolvency. By **June 2022** they were unable to meet margin calls; **July 1, 2022** they filed Chapter 15 bankruptcy.

The contagion cascaded:

- **Voyager Digital** had lent 3AC ~$650M unsecured -- bankrupt **July 5, 2022**.
- **Celsius Network** -- frozen withdrawals **June 12, 2022**, bankrupt **July 13, 2022**.
- **BlockFi** -- bailed out by FTX June 2022, bankrupt November 2022 after FTX's own collapse.
- **Genesis Global Capital** ([[dcg|DCG's]] lending arm) -- had lent 3AC ~$2.36B; bankrupt **January 19, 2023**.

## The DCG Feedback Loop

Digital Currency Group (DCG), Grayscale's parent company, owned a substantial GBTC position itself and lent against it through Genesis. As the discount widened:

- Genesis loans collateralized by GBTC became under-secured.
- DCG took on a **$1.1 billion promissory note** to Genesis to cover the 3AC default loss.
- Grayscale collected ~**2% annual management fee** on the trust's BTC -- ~$200M+/year revenue, but the discount blocked redemptions, locking BTC inside the trust permanently (until ETF conversion).

The structural conflict: DCG benefited from the trust staying closed-end (no redemptions = recurring fees); shareholders suffered from the discount. Activist investors including Fir Tree Capital sued Grayscale in 2022 to force redemptions.

## The Resolution -- Spot ETF Approval

**August 29, 2023**: DC Circuit Court ruled in Grayscale's favor against the SEC, calling the SEC's denial of GBTC's ETF conversion "arbitrary and capricious."

**January 10, 2024**: SEC approved 11 spot Bitcoin ETFs, including the GBTC conversion.

**January 11, 2024**: GBTC began trading as a true ETF with creation/redemption -- the discount closed to ~0%.

Traders who bought GBTC at -45% in November 2022 captured roughly:

- ~80% return from the discount closing alone (price moved from ~55% of NAV to ~100%).
- Plus BTC appreciation from $16K to $46K (~190%).
- Combined: **a 4-6x return on capital in 14 months** for those who held through.

## Why the Arbitrage Worked (and Didn't)

The persistent discount demonstrated [[limits-to-arbitrage]] in closed-end fund structures:

- **No redemption mechanism**: Unlike an ETF, GBTC could not redeem shares for BTC. The only way to close the discount was a structural change (ETF conversion).
- **Tax inefficiency**: Selling GBTC and buying BTC directly triggered taxable events for many holders.
- **Forced sellers**: Bankruptcy estates (3AC, Celsius, BlockFi, FTX) all held GBTC and were liquidating it into a thin market, deepening the discount.
- **No clear catalyst date**: Until the August 2023 court ruling, traders had no certainty when (or if) the discount would close. This duration risk kept the discount wide.

## Trading Lessons

- **Closed-end fund discounts can persist for years**: Without a redemption mechanism, the discount is bounded only by patience and forced selling. See [[bankruptcy-claim-arbitrage]] for parallel dynamics.
- **Crowded "arbitrage" can become a death trap**: Every major crypto lender ran the GBTC premium trade. When it flipped, they were all on the same side -- and forced liquidations cascaded.
- **Lockups embed hidden risk**: The 6-month creation lockup was free money on the way up and a liquidity prison on the way down.
- **Structural arb requires a catalyst**: Buying the discount only paid out when the ETF conversion happened. Without the **August 2023** court win, the discount could have persisted indefinitely.
- **Fees vs. fairness conflicts kill closed-end funds**: DCG/Grayscale's 2% fee created a structural reason to keep the trust closed -- against shareholder interests. Activists eventually forced the issue.

The GBTC saga is the canonical example of how a "guaranteed" arbitrage can become an extinction-level event for an industry. See also [[gbtc-discount-arbitrage]] and [[2022-05-terra-luna-depeg-arb]].

## Sources

- Grayscale / YCharts historical GBTC premium-to-NAV data (2020-2024).
- *Grayscale Investments v. SEC*, DC Circuit Court ruling (August 29, 2023).
- SEC order approving 11 spot Bitcoin ETFs, including GBTC conversion (January 10, 2024).
- Three Arrows Capital Chapter 15 filing (July 1, 2022); Voyager, Celsius, Genesis bankruptcy filings (2022-2023).
- DCG / Genesis disclosures of the $1.1B promissory note and $2.36B 3AC exposure (2022-2023).
- Bloomberg / CoinDesk coverage of the GBTC discount and 3AC contagion (2021-2024).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (top coins)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, max pain
- `GET /api/v1/market-intelligence/etf/btc/aum` — BTC ETF total AUM
- `GET /api/v1/market-intelligence/exchange-balance` — exchange BTC balance + flow
- `GET /api/v1/market-intelligence/taker-buy-sell` — taker buy/sell ratio by exchange (4h window)

**Historical data:**
- `GET /api/v1/market-intelligence/etf/{asset}/flows` — BTC/ETH/SOL/XRP ETF flow history
- `GET /api/v1/market-intelligence/coinbase-premium` — Coinbase premium index history
- `GET /api/v1/market-intelligence/btc/cycle-indicators` — all 8 BTC cycle indicators, historical
- `GET /api/v1/backtesting/liquidations` — liquidation records archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]].

## Related

- [[gbtc-discount-arbitrage]]
- [[bankruptcy-claim-arbitrage]]
- [[three-arrows-capital]]
- [[2022-05-terra-luna-depeg-arb]]
- [[limits-to-arbitrage]]
- [[bitcoin]]
