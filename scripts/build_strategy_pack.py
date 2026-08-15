from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
DOCS = ROOT / "docs"
FIGURES = ROOT / "figures"


def write_launch_plan() -> None:
    rows = [
        {"phase": "Days 0-30", "workstream": "ICP validation", "owner": "Founder", "deliverable": "25 accountant/MSME interviews", "success_metric": "15+ qualified pain confirmations"},
        {"phase": "Days 0-30", "workstream": "Product wedge", "owner": "Product", "deliverable": "Credit-readiness score prototype", "success_metric": "5 pilot users connect transaction data"},
        {"phase": "Days 0-30", "workstream": "Compliance framing", "owner": "Ops", "deliverable": "Readiness-not-lending policy note", "success_metric": "No loan-decision language in product"},
        {"phase": "Days 31-60", "workstream": "Pilot acquisition", "owner": "Growth", "deliverable": "CA/consultant channel pilot", "success_metric": "50 SMBs onboarded at CAC below Rs 1,400"},
        {"phase": "Days 31-60", "workstream": "Data quality", "owner": "Analytics", "deliverable": "Categorization audit loop", "success_metric": "90%+ category precision on reviewed transactions"},
        {"phase": "Days 31-60", "workstream": "Pricing", "owner": "Founder", "deliverable": "Pro tier paid test", "success_metric": "10 paid users at Rs 799/month"},
        {"phase": "Days 61-90", "workstream": "Partner motion", "owner": "BD", "deliverable": "2 lender/accounting platform LOIs", "success_metric": "One partner pilot scoped"},
        {"phase": "Days 61-90", "workstream": "Retention", "owner": "Product", "deliverable": "Receivables/cashflow alerts", "success_metric": "30-day active usage above 55%"},
        {"phase": "Days 61-90", "workstream": "Investment case", "owner": "Founder", "deliverable": "Investor-ready metrics memo", "success_metric": "CAC, activation, retention, and payback tracked weekly"},
    ]
    pd.DataFrame(rows).to_csv(MODELS / "launch_plan_90_days.csv", index=False)


def write_kpi_model() -> None:
    rows = [
        {"metric": "Activation rate", "definition": "Connected transaction data and completed first health-score review", "target_30d": "35%", "target_90d": "55%", "why_it_matters": "Measures whether onboarding reaches the core use case"},
        {"metric": "Categorization precision", "definition": "Reviewed transactions correctly categorized", "target_30d": "85%", "target_90d": "92%", "why_it_matters": "Trust breaks if financial interpretation is wrong"},
        {"metric": "CAC payback", "definition": "CAC divided by monthly gross profit", "target_30d": "<4 months", "target_90d": "<3 months", "why_it_matters": "Keeps GTM viable for low-ARPA MSMEs"},
        {"metric": "Pro conversion", "definition": "Activated users converting to Rs 799/month Pro tier", "target_30d": "8%", "target_90d": "15%", "why_it_matters": "Validates willingness to pay"},
        {"metric": "Weekly active usage", "definition": "Users viewing dashboard or alerts weekly", "target_30d": "35%", "target_90d": "50%", "why_it_matters": "Proxy for retention before long cohorts mature"},
        {"metric": "Partner qualified leads", "definition": "SMBs sourced by accountant/consultant/lender partners", "target_30d": "20", "target_90d": "200", "why_it_matters": "Tests scalable CAC advantage"},
        {"metric": "Lender-readiness exports", "definition": "Users exporting credit-readiness packet", "target_30d": "5", "target_90d": "50", "why_it_matters": "Measures embedded-finance wedge pull"},
    ]
    pd.DataFrame(rows).to_csv(MODELS / "operating_kpi_tree.csv", index=False)


def write_tornado_chart() -> None:
    sensitivity = pd.read_csv(MODELS / "sensitivity_analysis.csv")
    base = sensitivity.loc[sensitivity["scenario"] == "Base"].iloc[0]
    rows = []
    for _, row in sensitivity.iterrows():
        if row["scenario"] in {"Base", "Bear case", "Bull case"}:
            continue
        rows.append(
            {
                "scenario": row["scenario"],
                "delta_ltv": row["pro_ltv_inr"] - base["pro_ltv_inr"],
                "delta_payback": row["pro_payback_months"] - base["pro_payback_months"],
            }
        )
    tornado = pd.DataFrame(rows).sort_values("delta_ltv")
    tornado.to_csv(MODELS / "sensitivity_tornado.csv", index=False)

    FIGURES.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(9, 4.8))
    colors = ["#dc2626" if x < 0 else "#059669" for x in tornado["delta_ltv"]]
    ax.barh(tornado["scenario"], tornado["delta_ltv"], color=colors)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_title("Pro Tier LTV Sensitivity vs Base Case")
    ax.set_xlabel("Change in LTV, INR")
    fig.tight_layout()
    fig.savefig(FIGURES / "ltv_sensitivity_tornado.png", dpi=180)
    plt.close(fig)


def write_deck() -> None:
    unit = pd.read_csv(MODELS / "unit_economics.csv")
    sizing = pd.read_csv(MODELS / "market_sizing.csv")
    competitor = pd.read_csv(MODELS / "competitor_benchmark.csv")
    base_pro = unit.loc[unit["tier"] == "Pro"].iloc[0]

    deck = f"""# FlowFinance Market Entry Deck

## Slide 1: Recommendation

Enter MSME embedded finance through credit-readiness and cashflow-health analytics, not direct lending. Start with the Pro tier and partner-led distribution through accountants, consultants, and later lenders.

## Slide 2: Market Map

| Layer | Modeled Assumption | Value |
|---|---|---:|
{chr(10).join(f"| {r.segment} | {r.assumption} | {r.value} {r.unit} |" for r in sizing.itertuples())}

## Slide 3: Customer Pain

MSMEs have transaction data but weak interpretation. They need cashflow visibility, expense categorization, receivables discipline, and loan-readiness documentation before they need another generic dashboard.

## Slide 4: Competitive Positioning

| Competitor Type | Strength | Weakness | FlowFinance Position |
|---|---|---|---|
{chr(10).join(f"| {r.competitor_type} | {r.strength} | {r.weakness} | {r.flowfinance_position} |" for r in competitor.itertuples())}

## Slide 5: Unit Economics

| Tier | Price | CAC | LTV | Payback |
|---|---:|---:|---:|---:|
{chr(10).join(f"| {r.tier} | Rs {r.monthly_price_inr}/mo | Rs {r.cac_inr:,.0f} | Rs {r.ltv_inr:,.0f} | {r.payback_months:.2f} mo |" for r in unit.itertuples())}

Pro is the recommended wedge: Rs {base_pro.monthly_price_inr}/month, Rs {base_pro.cac_inr:,.0f} CAC, Rs {base_pro.ltv_inr:,.0f} LTV, and {base_pro.payback_months:.2f}-month payback.

## Slide 6: Sensitivity

Use `figures/ltv_sensitivity_tornado.png`. The bear case still has payback below 4 months, but it requires partner-led CAC discipline.

## Slide 7: 90-Day Launch Plan

Use `models/launch_plan_90_days.csv`. The first 30 days validate pain and data quality; days 31-60 test paid Pro conversion; days 61-90 secure partner pilots.

## Slide 8: Risks and Decision

Proceed with analytics-first market entry. Do not originate loans. Do not position the score as credit approval. Track activation, data quality, CAC payback, Pro conversion, weekly active usage, and lender-readiness exports.
"""
    (DOCS / "market_entry_deck.md").write_text(deck, encoding="utf-8")


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    MODELS.mkdir(parents=True, exist_ok=True)
    write_launch_plan()
    write_kpi_model()
    write_tornado_chart()
    write_deck()
    print("Wrote docs/market_entry_deck.md")
    print("Wrote models/launch_plan_90_days.csv and models/operating_kpi_tree.csv")
    print("Wrote figures/ltv_sensitivity_tornado.png")


if __name__ == "__main__":
    main()
