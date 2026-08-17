# FlowFinance SMB Embedded Finance Market Entry Case

Consulting-style market-entry and GTM case for [FlowFinance](https://www.flowfinancebusiness.com), an MSME financial-intelligence product. The repository separates observed pilot/product evidence from modeled market-sizing and unit-economics assumptions.

## Verified Public Product Evidence

- The application is publicly accessible at [flowfinancebusiness.com](https://www.flowfinancebusiness.com).
- Deployment used AWS EC2 and RDS within a VPC, with Secrets Manager for application credentials.
- Transaction workflows covered 81,813 mixed anonymized and generated records across 28 categories.
- FlowFinance ran one-month free pilots with 10+ MSMEs; 10+ returned after initial use.
- FlowFinance did not generate revenue during this period; no paid-customer claim is made.

See [`docs/public_product_evidence.md`](docs/public_product_evidence.md) and
[`models/pilot_evidence.csv`](models/pilot_evidence.csv) for the public evidence boundary.

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

Private customer decks and partner documents are maintained outside this public repository. This repo contains the public-facing strategy case, modeled assumptions, aggregate pilot evidence, and validation scripts used to defend the market-entry recommendation.

| Artifact | Location | Purpose |
|---|---|---|
| Market-entry case | `docs/market_entry_deck.md` | Strategy/Ops interview and founder's-office evidence |
| Executive summary | `docs/executive_summary.md` | One-page recommendation |
| Case defense | `docs/case_interview_defense.md` | Interview-ready assumptions, risks, and tradeoffs |
| Public product evidence | `docs/public_product_evidence.md` | Deployment, pilot, and data-provenance boundaries |
| Pilot evidence | `models/pilot_evidence.csv` | Aggregate and non-confidential pilot facts |

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

- Co-founded FlowFinance, an AWS-deployed MSME financial-intelligence product; ran one-month free pilots with 10+ MSMEs, processed 81,813 mixed anonymized/generated records, and built a market-entry case covering TAM/SAM/SOM, pricing, and partner economics.

## Validation

```bash
python scripts/validate_case.py
```
