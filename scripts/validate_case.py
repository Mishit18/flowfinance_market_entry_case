from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    required = [
        "README.md",
        "docs/case_report.md",
        "docs/executive_summary.md",
        "docs/slide_storyline.md",
        "docs/case_interview_defense.md",
        "docs/market_entry_deck.md",
        "models/market_sizing.csv",
        "models/unit_economics.csv",
        "models/competitor_benchmark.csv",
        "models/sensitivity_analysis.csv",
        "models/sensitivity_tornado.csv",
        "models/launch_plan_90_days.csv",
        "models/operating_kpi_tree.csv",
        "figures/ltv_sensitivity_tornado.png",
    ]
    missing = [path for path in required if not (ROOT / path).exists()]
    if missing:
        print("Missing files:")
        for path in missing:
            print(f"- {path}")
        return 1

    unit = pd.read_csv(ROOT / "models" / "unit_economics.csv")
    if (unit["ltv_inr"] <= unit["cac_inr"]).any():
        print("Unit economics validation failed: LTV must exceed CAC for every modeled tier.")
        return 1
    if (unit["payback_months"] > 6).any():
        print("Unit economics validation failed: payback exceeds 6 months.")
        return 1

    sizing = pd.read_csv(ROOT / "models" / "market_sizing.csv")
    if len(sizing) < 6:
        print("Market sizing validation failed.")
        return 1

    sensitivity = pd.read_csv(ROOT / "models" / "sensitivity_analysis.csv")
    if "Bear case" not in set(sensitivity["scenario"]):
        print("Sensitivity validation failed.")
        return 1

    launch = pd.read_csv(ROOT / "models" / "launch_plan_90_days.csv")
    if launch["phase"].nunique() < 3 or len(launch) < 9:
        print("Launch plan validation failed.")
        return 1

    kpis = pd.read_csv(ROOT / "models" / "operating_kpi_tree.csv")
    if len(kpis) < 6:
        print("KPI tree validation failed.")
        return 1

    print("FlowFinance market-entry case validation passed")
    print(f"Best payback tier: {unit.sort_values('payback_months').iloc[0]['tier']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
