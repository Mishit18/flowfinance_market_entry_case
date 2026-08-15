import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from modern_case_layer import assumption_risk_register, gtmscorecard, investor_readiness_gate


def test_modern_case_layer():
    risk = assumption_risk_register(pd.DataFrame({"assumption": ["a", "b"], "impact": [5, 2], "uncertainty": [4, 1]}))
    gtm = gtmscorecard(pd.DataFrame({"channel": ["x", "y"], "cac": [100, 200], "conversion_rate": [0.2, 0.1], "sales_cycle_days": [10, 20], "strategic_fit": [5, 3]}))
    gate = investor_readiness_gate({"cac_payback_months": 2.0, "gross_margin_pct": 80, "anchor_customers": 1, "customers": 10})

    assert risk.iloc[0]["risk_score"] >= risk.iloc[-1]["risk_score"]
    assert gtm.iloc[0]["score"] >= gtm.iloc[-1]["score"]
    assert gate["verdict"] == "investor_ready_packet"
