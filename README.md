# FlowFinance SMB Embedded Finance Market Entry Case

Consulting-style market-entry and GTM case for FlowFinance, a full venture/product built from scratch for MSME financial intelligence. The case supports the broader venture story: product codebase, customer acquisition, user/customer deck, partnership materials, pricing, TAM/SAM/SOM, unit economics, and investor-ready fundraising narrative.

## What This Demonstrates

- Structured market-entry problem solving
- TAM / SAM / SOM sizing
- Customer segmentation and wedge selection
- Competitor benchmarking
- Pricing tiers and unit economics
- CAC / LTV / payback analysis
- 12-month GTM roadmap
- Risk register and operating KPIs
- Executive recommendation

## Headline Recommendation

Enter through a **credit-readiness and cashflow-health analytics wedge**, not through direct lending. FlowFinance should sell workflow analytics to accountants, fintech aggregators, and MSME advisors first, then partner with lenders once enough consented transaction history and model governance exists.

## Venture Collateral

Private customer decks and partner documents are maintained outside this public repository. This repo contains the public-facing strategy case, model assumptions, evidence pack, and validation scripts used to defend the market-entry recommendation.

| Artifact | Location | Purpose |
|---|---|---|
| Market-entry case | `docs/market_entry_deck.md` | Strategy/Ops interview and founder's-office evidence |
| Executive summary | `docs/executive_summary.md` | One-page recommendation |
| Case defense | `docs/case_interview_defense.md` | Interview-ready assumptions, risks, and tradeoffs |

## Key Outputs

| File | Purpose |
|---|---|
| `docs/case_report.md` | Full consulting-style case write-up |
| `docs/executive_summary.md` | One-page recommendation |
| `docs/slide_storyline.md` | 8-slide deck outline |
| `docs/market_entry_deck.md` | Consulting-style slide content with recommendation, sizing, economics, sensitivity, and risks |
| `models/unit_economics.csv` | Pricing, CAC, margin, LTV, payback assumptions |
| `models/market_sizing.csv` | TAM/SAM/SOM sizing assumptions |
| `models/competitor_benchmark.csv` | Competitor and positioning map |
| `models/launch_plan_90_days.csv` | 90-day founder/operator launch plan |
| `models/operating_kpi_tree.csv` | Activation, data quality, CAC payback, conversion, and partner KPI tree |
| `figures/ltv_sensitivity_tornado.png` | Sensitivity tornado chart for Pro-tier LTV |
| `scripts/validate_case.py` | Checks model sanity |

## Resume Bullet

- Built consulting-style FlowFinance market-entry case for MSME embedded-finance analytics: sized TAM/SAM/SOM, benchmarked competitors, modeled three-tier pricing and CAC/LTV economics, and recommended a credit-readiness analytics wedge before lender partnerships.

## Validation

```bash
python scripts/validate_case.py
```
