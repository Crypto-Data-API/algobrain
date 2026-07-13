---
title: "Weekend Effect"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, behavioral-finance, sp500, seasonality]
aliases: ["Monday Effect", "Day-of-the-Week Effect", "Blue Monday", "Weekend Anomaly"]
domain: [anomalies, behavioral-finance]
prerequisites: ["[[anomalies-overview]]"]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]", "[[overnight-vs-intraday]]", "[[btc-weekend-effect]]", "[[data-snooping-and-p-hacking]]"]
---

# Weekend Effect

The weekend effect — also known as the Monday effect or Blue Monday — is the historical finding that US equity returns on Mondays were significantly negative on average, while the other four weekdays had positive returns. It is one of the earliest documented calendar anomalies and one of the most heavily decayed. It survives mostly as a historical curiosity and as a cautionary tale about extrapolating in-sample patterns.

## What

In French's (1980) sample (1953-1977), Monday S&P 500 returns averaged roughly −0.17% per day, while Tuesday-Friday averaged +0.04% per day. The Monday return was statistically distinct from zero and from other weekdays by a wide margin. Subsequent researchers confirmed the pattern through roughly the mid-1980s.

## Original Paper

French, K. (1980) "Stock Returns and the Weekend Effect" — *Journal of Financial Economics*. Earlier observation by Cross (1973).

## Mechanism

No single satisfying explanation. Candidates:

- **Weekend news asymmetry** — bad news disproportionately released Friday after the close (to bury it over the weekend), leading to negative Monday-morning repricing
- **Settlement timing** — prior to T+3 settlement reform, Friday purchases had an extra day of free financing, creating a tiny arbitrage window that affected Friday-Monday returns
- **Psychological "Blue Monday"** — investors return to work pessimistic
- **Short-seller behavior** — short interest disproportionately initiated before weekends

The weekend effect has been at the center of debates about whether calendar anomalies reflect real behavior or are data-mining artifacts. Sullivan, Timmermann, White (2001) argue that when you adjust for multiple-testing across the many possible calendar patterns you could have tested, the weekend effect's statistical significance evaporates.

## Edge Category

Historically **behavioral**, but the evidence is weak and the effect has largely vanished.

## Replication Status

Confirmed in pre-1990 data across multiple developed markets. Post-1990 it has weakened substantially and in some samples reversed (positive Monday returns). By the 2000s it is not reliably detectable in US large-caps.

## Decay History

One of the classic decay stories. Pre-1980: ~-17 bps/day on Mondays. Post-1990: ~0 bps. Post-2000: sometimes positive, sometimes negative, no pattern.

## Current Viability

Not tradeable. Treat as a historical artifact or data-snooping cautionary tale. Some international markets (especially emerging markets) retain weak day-of-week effects but they are too small and unstable to trade directly.

## Trading Relevance

The weekend effect's real value today is methodological, not directional. It is the canonical worked example of how a calendar pattern that is genuinely present in one sample can be (a) a multiple-testing artifact and (b) arbitraged away once published — the two failure modes every systematic researcher must guard against (see [[data-snooping-and-p-hacking]]). When a backtest surfaces a "day-of-week edge," the weekend effect is the prior that should make you suspicious: there are only seven days to test, the pattern was famous by 1980, and it has reversed sign in modern data. Practically, the only residue worth attention is that much of the historical Monday weakness was a Friday-close-to-Monday-open *overnight* move rather than an intraday Monday move (see [[overnight-vs-intraday]]), which matters for anyone decomposing returns into overnight vs intraday components. The crypto analog, where 24/7 trading removes the literal weekend close, is treated separately in [[btc-weekend-effect]].

## Related Strategies

- [[calendar-effects-anomalies]] — broader family
- [[overnight-vs-intraday]] — much of the Monday effect reflected Friday-close-to-Monday-open overnight moves

## Sources

- Cross, F. (1973). "The Behavior of Stock Prices on Fridays and Mondays." *Financial Analysts Journal* — precursor observation.
- French, K. (1980). "Stock Returns and the Weekend Effect." *Journal of Financial Economics* 8(1): 55–69 — canonical reference. https://doi.org/10.1016/0304-405X(80)90021-5
- Lakonishok, J. & Smidt, S. (1988). "Are Seasonal Anomalies Real? A Ninety-Year Perspective." *Review of Financial Studies* 1(4): 403–425.
- Sullivan, R., Timmermann, A. & White, H. (2001). "Dangers of Data Mining: The Case of Calendar Effects in Stock Returns." *Journal of Econometrics* 105(1): 249–286 — argues the effect is a multiple-testing artifact once the universe of testable calendar rules is accounted for.

## Related

- [[anomalies-overview]]
- [[calendar-effects-anomalies]]
- [[overnight-vs-intraday]]
- [[data-snooping-and-p-hacking]]
