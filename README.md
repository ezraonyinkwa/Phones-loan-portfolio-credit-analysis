# Phone Loan Portfolio Analysis

## What This Project Does

Phone financing companies extend credit to thousands of customers 
daily. Managing that portfolio means answering hard questions: How 
much of our loan book is at risk? Which customers are most likely to 
default? And when customers are unhappy, does that show up in the 
credit numbers?

This project answers those questions using real loan portfolio data 
from a phone financing company. It builds a full analytics pipeline 
— from raw data to cleaned metrics to visualisations — covering 
portfolio health, segment-level risk, and the relationship between 
customer experience and credit outcomes.

---

## How It Works

### Step 1 — Data Loading & Cleaning
Raw datasets covering credit performance, customer demographics, NPS 
(customer satisfaction) scores, and sales details are loaded, 
validated, and prepared for analysis. Missing values, column 
mismatches, and data type issues are resolved before any metric is 
computed.

### Step 2 — Portfolio Health Metrics
Five core credit risk metrics are calculated across the full loan book:

| Metric | What It Measures |
|--------|-----------------|
| **PAR 30 / 60 / 90** | % of outstanding balance held by accounts 30, 60, or 90+ days past due |
| **Impaired Rate** | Share of active loan balance carrying any delinquency |
| **Average Arrears per Impaired Account** | Mean arrears balance in KES across all delinquent accounts |
| **Default Rate** | % of balance in accounts 60+ days past due |
| **NPE Rate** | % of total book classified as non-performing (90+ DPD) |

All metrics are computed both as point-in-time snapshots and as 
monthly trends to show how portfolio quality evolved over time.

### Step 3 — Segment Risk Analysis
The loan book is broken down by customer age group to identify which 
segments carry disproportionate risk. Credit data is merged with 
customer date-of-birth records to compute NPE rates per age band, 
revealing where the portfolio's risk is concentrated.

### Step 4 — Customer Experience × Credit Outcomes
NPS (Net Promoter Score) data is joined to the credit dataset on 
loan ID to test whether customer satisfaction has a measurable 
relationship with repayment behaviour. Three correlations are 
computed:

- **NPS vs Default Rate** (by month)
- **Arrears Status vs NPS Score** (account level)
- **Loan Price vs NPS Score** (to test whether cost drives 
  dissatisfaction)

Monthly PAR rates are then plotted alongside average NPS scores to 
visualise the tension between collections pressure and customer 
experience.

---

## Key Findings

- **NPE rate reached 14.2%** by December 2024, with PAR30 breaching 
  the 10% industry watch threshold
- **The 19–25 age cohort carries 1.8× the portfolio average NPE 
  rate** — 25.1% vs 14.2% — making it the single highest-risk segment
- **–0.91 correlation between NPS and Default Rate**, confirming that 
  customer dissatisfaction and credit deterioration move together — 
  collections friction is not just a CX problem, it's a portfolio risk
- **Zero correlation between loan price and NPS**, suggesting cost 
  alone does not drive dissatisfaction — the issue is operational, 
  not commercial

---

## Tech Stack

- **Python** — end-to-end analytics pipeline
- **Pandas & NumPy** — data manipulation and metric computation
- **Matplotlib & Seaborn** — trend and segment visualisations
- **Jupyter Notebooks** — exploratory analysis

---

## Who This Is For

This project is relevant to anyone in **fintech, device financing, 
or consumer lending** who needs to move beyond spreadsheet-level 
portfolio reporting. It shows how to build a repeatable, 
code-driven credit monitoring workflow that surfaces the right 
signals — before they become write-offs.
