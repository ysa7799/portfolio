# Customer Behavior Exploration — Python (pandas)

EDA on a simulated customer transaction dataset (500 customers) with intentionally realistic messiness: missing values and outliers, so the cleaning steps are doing real work.

## Files
- `analysis.py` — full pipeline: generate data → clean → visualize → write insight memo
- `data/customers_raw.csv` — messy synthetic input
- `data/customers_clean.csv` — cleaned output
- `charts/spend_distribution.png`, `charts/tenure_vs_spend.png`
- `insight_memo.md` — findings, generated fresh on each run

## Run it
```bash
pip install pandas numpy matplotlib
python3 analysis.py
```

## Approach
- **Missing values**: `age` and `monthly_spend` imputed with median rather than dropped, to preserve sample size.
- **Outliers**: extreme high-spend values capped at the 99th percentile instead of removed — keeps real high-value customers in the dataset without letting them distort the mean.
- **Visualization**: spend distribution histogram + tenure-vs-spend scatter colored by acquisition channel.

## Sample finding (from actual run)
Tenure and spend show a weak positive correlation (r ≈ 0.08) — tenure alone isn't a strong spend predictor in this dataset, which is itself a useful finding: it argues against assuming "longer customer = bigger spender" without testing it.

## Skills demonstrated
Missing-value strategy (impute vs. drop), outlier handling (cap vs. remove), correlation analysis, channel-level aggregation, translating stats into a plain-English memo for non-technical stakeholders.

## Presentation
`Customer_Behavior_Exploration.pptx` — a 6-slide walkthrough of the dataset, cleaning approach, and key findings.
