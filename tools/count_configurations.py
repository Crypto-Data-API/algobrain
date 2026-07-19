#!/usr/bin/env python3
"""
Count the distinct strategy configurations derivable from the AlgoBrain wiki.

Formula (deliberately conservative, assumptions printed):
  designs        = sum over matrix rows of (2^k - 1) * COMPOSABILITY  (k = viable overlays)
  single configs = sum over rows of row_designs * applicable_instruments(row)
  pair/basket    = counted only once instrument structures are formalized
                   (.claude/instrument-structures.json written by campaign item C3)

Run:  .venv/Scripts/python.exe tools/count_configurations.py
"""
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "wiki" / "strategies" / "combinations" / "combination-matrix.md"
STRUCTS = ROOT / ".claude" / "instrument-structures.json"

COMPOSABILITY = 0.5   # haircut: not all viable overlays stack pairwise

# Instrument-applicability class per primitive row (matched by row-name substring).
# Universe sizes are counts of enriched Trading-Profile pages by venue capability.
PERP = 380     # Hyperliquid perps + Binance USD-M perp names (profiled)
SPOT = 481     # all profiled tradable assets
OPTIONS = 3    # Deribit liquid options underlyings (BTC, ETH, SOL) — conservative
APPLICABILITY = [
    ("funding carry", PERP), ("basis", PERP), ("momentum", SPOT), ("mean-reversion", SPOT),
    ("liquidation", PERP), ("narrative", SPOT), ("vol selling", OPTIONS),
    ("vol buying", OPTIONS), ("grid", PERP), ("stat-arb", PERP), ("on-chain", SPOT),
    ("sentiment", SPOT),
    # Campaign-2 rows (defaults; refine as rows land)
    ("mev", 50), ("defi-yield", 150), ("options-rv", OPTIONS), ("prediction", 20),
    ("stablecoin", 30), ("whale", PERP),
]

def applicability(row_name: str) -> int:
    n = row_name.lower()
    for key, size in APPLICABILITY:
        if key in n:
            return size
    return 200  # conservative default for unmapped rows

def main() -> None:
    rows = []
    for line in MATRIX.read_text(encoding="utf-8").splitlines():
        if line.startswith("| **"):
            name = re.match(r"\| \*\*([^*]+)\*\*", line).group(1).strip()
            cells = line.split("|")[2:-1]
            k = sum(1 for c in cells if "[[" in c)
            rows.append((name, k))

    total_designs = 0.0
    total_configs = 0.0
    print(f"{'primitive':<28}{'k':>3}{'designs':>10}{'instr':>7}{'configs':>12}")
    for name, k in rows:
        designs = (2 ** k - 1) * COMPOSABILITY
        instr = applicability(name)
        configs = designs * instr
        total_designs += designs
        total_configs += configs
        print(f"{name:<28}{k:>3}{designs:>10,.0f}{instr:>7}{configs:>12,.0f}")

    pair_basket = 0.0
    if STRUCTS.exists():
        s = json.loads(STRUCTS.read_text(encoding="utf-8"))
        pairs = s.get("screened_pairs", 0)
        baskets = s.get("baskets", 0)
        pair_designs = s.get("pair_capable_designs", 0)
        basket_designs = s.get("basket_capable_designs", 0)
        basket_spreads = math.comb(baskets, 2) if baskets >= 2 else 0
        pair_basket = pair_designs * pairs + basket_designs * (baskets + basket_spreads)
        print(f"\npair/basket structures: {pairs:,} pairs x {pair_designs} designs + "
              f"{baskets} baskets ({basket_spreads:,} spreads) x {basket_designs} designs "
              f"= {pair_basket:,.0f}")
    else:
        print("\npair/basket structures: not yet formalized (C3) -> 0")

    grand = total_configs + pair_basket
    print(f"\nASSUMPTIONS: composability haircut {COMPOSABILITY}; perp universe {PERP}; "
          f"spot {SPOT}; options {OPTIONS}. Conservative by design.")
    print(f"DESIGNS (distinct strategy logic): {total_designs:,.0f}")
    print(f"DISTINCT CONFIGURATIONS: {grand:,.0f}")
    print(f"GOAL (1,000,000): {'REACHED' if grand >= 1_000_000 else f'{grand/1_000_000:.1%} of goal'}")

if __name__ == "__main__":
    main()
