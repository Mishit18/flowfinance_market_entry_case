from __future__ import annotations

import pandas as pd


def assumption_risk_register(assumptions: pd.DataFrame) -> pd.DataFrame:
    required = {"assumption", "impact", "uncertainty"}
    missing = required - set(assumptions.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    out = assumptions.copy()
    out["risk_score"] = out["impact"] * out["uncertainty"]
    out["priority"] = pd.cut(out["risk_score"], bins=[-1, 3, 6, 10], labels=["monitor", "validate", "de-risk"])
    return out.sort_values("risk_score", ascending=False)


def gtmscorecard(channels: pd.DataFrame) -> pd.DataFrame:
    required = {"channel", "cac", "conversion_rate", "sales_cycle_days", "strategic_fit"}
    missing = required - set(channels.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    out = channels.copy()
    out["score"] = (
        out["conversion_rate"].rank(pct=True) * 0.35
        + (1 / out["cac"]).rank(pct=True) * 0.25
        + (1 / out["sales_cycle_days"]).rank(pct=True) * 0.20
        + out["strategic_fit"].rank(pct=True) * 0.20
    )
    return out.sort_values("score", ascending=False)


def investor_readiness_gate(kpis: dict[str, float]) -> dict[str, object]:
    checks = {
        "payback_under_3_months": kpis.get("cac_payback_months", 999) <= 3,
        "gross_margin_above_70": kpis.get("gross_margin_pct", 0) >= 70,
        "anchor_customer_present": kpis.get("anchor_customers", 0) >= 1,
        "customer_count_10_plus": kpis.get("customers", 0) >= 10,
    }
    return {"checks": checks, "passed": int(sum(checks.values())), "total": len(checks), "verdict": "investor_ready_packet" if all(checks.values()) else "needs_validation"}

