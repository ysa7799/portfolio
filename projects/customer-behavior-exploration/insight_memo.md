# Customer Behavior Exploration — Insight Memo

## Data quality
- 20 missing `age` values imputed with median (45).
- 15 missing `monthly_spend` values imputed with median after outlier handling.
- 5 extreme high-spend records capped at the 99th percentile ($166.56) rather than dropped, to avoid losing real high-value customers while preventing them from distorting averages.

## Key findings
- Tenure and monthly spend show a **positive correlation** (r = 0.08) — longer-tenured customers spend modestly more, consistent with typical retention/loyalty patterns.
- Average monthly spend by channel:
  - Online: $56.60
  - Mobile App: $55.78
  - In-Store: $53.01
- Spend distribution is right-skewed even after capping — most customers cluster in a moderate spend band, with a smaller group of high-value customers pulling the mean upward.

## Suggested next-step analyses
- Segment customers into value tiers (e.g., low/medium/high spend) and profile each by channel and tenure.
- Test whether channel differences in spend are statistically significant (t-test/ANOVA) rather than assumed from means alone.
- Bring in a churn/cancellation flag (not present in this synthetic dataset) to study whether spend or tenure predicts churn risk.
