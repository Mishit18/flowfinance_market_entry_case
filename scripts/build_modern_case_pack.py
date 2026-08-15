from __future__ import annotations

from pathlib import Path

import pandas as pd

from modern_case_layer import assumption_risk_register, gtmscorecard, investor_readiness_gate


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    out = ROOT / "models"
    docs = ROOT / "docs"
    assumptions = pd.DataFrame(
        {
            "assumption": ["MSME willingness to pay", "AA consent completion", "partner distribution", "LLM categorization cost"],
            "impact": [5, 4, 4, 3],
            "uncertainty": [4, 3, 4, 2],
        }
    )
    channels = pd.DataFrame(
        {
            "channel": ["direct founder-led", "CA/accounting partners", "lender partnerships", "paid performance"],
            "cac": [3200, 1800, 2600, 5200],
            "conversion_rate": [0.18, 0.14, 0.10, 0.05],
            "sales_cycle_days": [18, 30, 45, 12],
            "strategic_fit": [5, 5, 4, 2],
        }
    )
    risk = assumption_risk_register(assumptions)
    gtm = gtmscorecard(channels)
    gate = investor_readiness_gate({"cac_payback_months": 2.14, "gross_margin_pct": 82, "anchor_customers": 1, "customers": 10})
    risk.to_csv(out / "assumption_risk_register.csv", index=False)
    gtm.to_csv(out / "gtm_channel_scorecard.csv", index=False)
    pd.DataFrame([{"passed": gate["passed"], "total": gate["total"], "verdict": gate["verdict"]}]).to_csv(out / "investor_readiness_gate.csv", index=False)
    (docs / "modern_case_evidence_pack.md").write_text(
        "\n".join(
            [
                "# Modern Case Evidence Pack",
                "",
                f"- Top GTM channel: {gtm.iloc[0]['channel']}",
                f"- Highest-risk assumption: {risk.iloc[0]['assumption']}",
                f"- Investor readiness verdict: {gate['verdict']}",
                "- Added assumption risk register, GTM channel scorecard, and investor readiness gate.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

