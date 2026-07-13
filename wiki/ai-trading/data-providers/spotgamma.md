---
title: "SpotGamma"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, options, stocks]
entity_type: company
website: https://www.spotgamma.com
related:
  - "[[unusual-whales]]"
  - "[[polygon-io]]"
  - "[[options-trading]]"
---

# SpotGamma

## Overview

Options gamma exposure (GEX) analytics platform that reveals how dealer hedging activity influences stock and index prices. SpotGamma's core thesis: options market makers must continuously hedge their positions, and this hedging creates measurable, predictable effects on price action. When dealers are long gamma, they buy dips and sell rips (suppressing volatility). When dealers are short gamma, they chase price in both directions (amplifying moves). SpotGamma quantifies these forces and translates them into actionable levels for intraday and swing trading on the S&P 500, Nasdaq, and individual stocks.

## Pricing

- **Alpha**: ~$200/mo -- daily GEX levels, key strikes, expected move zones, morning note
- **Pro**: ~$500/mo -- intraday GEX updates, real-time gamma model, historical GEX data, API
- No free tier (some educational content and occasional free GEX snapshots on social media)
- Annual subscriptions offer ~20% discount

## What You Get (vs Free)

- Daily gamma exposure levels: gamma flip, put wall, call wall, key support/resistance from options positioning
- Intraday GEX model updates (Pro) showing how dealer positioning shifts throughout the session
- Expected move zones based on options pricing and volatility term structure
- Volatility trigger level -- above this, dealers suppress moves; below, they amplify them
- Morning note with market structure context and key levels for the trading day
- Historical GEX data for [[backtesting]] gamma-based strategies

## Alpha Edge

- **GEX predicts intraday behavior**: when aggregate dealer gamma is positive (long gamma environment), the S&P 500 tends to mean-revert and stay range-bound. When gamma is negative, markets trend aggressively and volatility spikes. Knowing which regime you are in changes everything about how you trade
- **Gamma flip level**: the price level where dealer gamma flips from positive to negative is a critical support/resistance zone. Markets frequently pin to or bounce off this level
- **Put wall as support**: the strike with the largest put open interest often acts as a floor because dealer hedging creates buying pressure at that level
- **OPEX gravity**: as options expiration approaches, gamma effects intensify and prices gravitate toward max pain / highest OI strikes
- **Vol regime identification**: SpotGamma's volatility trigger helps determine whether to trade mean-reversion or momentum strategies

## Key Features

- **HIRO (Hedging Impact Real-time Oscillator)**: measures real-time hedging pressure from options flow
- **GEX Dashboard**: visual breakdown of gamma exposure by strike and expiry
- **Volatility Trigger**: key level determining whether market is in positive or negative gamma regime
- **Morning Note**: daily pre-market analysis with key levels and market structure outlook
- **Equity Hub**: GEX analysis for individual stocks beyond just indices
- **Education**: extensive library explaining gamma mechanics and dealer hedging dynamics

## Who Uses It

- S&P 500 and Nasdaq intraday traders using GEX levels as support/resistance
- Options traders timing entries around gamma regime shifts
- Institutional volatility desks monitoring dealer positioning
- Swing traders using put walls and call walls for directional bias
- Anyone trading [[spy-qqq]] who wants to understand WHY the market pins at certain levels
- Traders who recognize that options market structure drives equity price action more than most realize
