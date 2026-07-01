"""
Customer Behavior Exploration — pandas EDA
--------------------------------------------
Simulates a customer transaction dataset (with realistic messiness: missing
values, a few outliers) and runs an exploratory analysis: cleaning,
missing-value handling, distribution/outlier visualization, and a written
insight memo.

Run: python3 analysis.py
Outputs:
  data/customers_raw.csv       (messy synthetic input)
  data/customers_clean.csv     (cleaned output)
  charts/spend_distribution.png
  charts/tenure_vs_spend.png
  insight_memo.md
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

np.random.seed(42)
os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

N = 500
customer_id = np.arange(1, N + 1)
age = np.random.randint(18, 70, N).astype(float)
tenure_months = np.random.randint(1, 60, N).astype(float)
monthly_spend = np.random.gamma(shape=3, scale=15, size=N) + tenure_months * 0.3
channel = np.random.choice(["Online", "In-Store", "Mobile App"], N, p=[0.45, 0.25, 0.30])

# Inject messiness: missing values + a few extreme outliers
missing_idx = np.random.choice(N, 35, replace=False)
age[missing_idx[:20]] = np.nan
monthly_spend[missing_idx[20:]] = np.nan
outlier_idx = np.random.choice(N, 5, replace=False)
monthly_spend[outlier_idx] *= 8  # extreme high spenders / data entry errors

df = pd.DataFrame({
    "customer_id": customer_id,
    "age": age,
    "tenure_months": tenure_months,
    "monthly_spend": monthly_spend,
    "channel": channel,
})
df.to_csv("data/customers_raw.csv", index=False)

# --- Cleaning ---
missing_report = df.isna().sum()
df_clean = df.copy()
df_clean["age"] = df_clean["age"].fillna(df_clean["age"].median())

# Outlier handling: cap monthly_spend at 99th percentile rather than dropping
spend_before_na = df_clean["monthly_spend"].dropna()
p99 = spend_before_na.quantile(0.99)
n_outliers = (df_clean["monthly_spend"] > p99).sum()
df_clean["monthly_spend"] = df_clean["monthly_spend"].clip(upper=p99)
df_clean["monthly_spend"] = df_clean["monthly_spend"].fillna(df_clean["monthly_spend"].median())

df_clean.to_csv("data/customers_clean.csv", index=False)

# --- Visualizations ---
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(df_clean["monthly_spend"], bins=30, color="#2e75b6", edgecolor="white")
ax.set_title("Monthly Spend Distribution (post-cleaning)")
ax.set_xlabel("Monthly Spend ($)")
ax.set_ylabel("Customers")
fig.tight_layout()
fig.savefig("charts/spend_distribution.png", dpi=140)
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 4.5))
colors = {"Online": "#2e75b6", "In-Store": "#1f3864", "Mobile App": "#9fb8dd"}
for ch, sub in df_clean.groupby("channel"):
    ax.scatter(sub["tenure_months"], sub["monthly_spend"], alpha=0.5, s=18, label=ch, color=colors[ch])
ax.set_title("Tenure vs. Monthly Spend by Channel")
ax.set_xlabel("Tenure (months)")
ax.set_ylabel("Monthly Spend ($)")
ax.legend()
fig.tight_layout()
fig.savefig("charts/tenure_vs_spend.png", dpi=140)
plt.close(fig)

# --- Insight memo ---
corr = df_clean["tenure_months"].corr(df_clean["monthly_spend"])
channel_avg = df_clean.groupby("channel")["monthly_spend"].mean().sort_values(ascending=False)

memo = f"""# Customer Behavior Exploration — Insight Memo

## Data quality
- {int(missing_report['age'])} missing `age` values imputed with median ({df_clean['age'].median():.0f}).
- {int(missing_report['monthly_spend'])} missing `monthly_spend` values imputed with median after outlier handling.
- {n_outliers} extreme high-spend records capped at the 99th percentile (${p99:.2f}) rather than dropped, to avoid losing real high-value customers while preventing them from distorting averages.

## Key findings
- Tenure and monthly spend show a **{"positive" if corr > 0 else "negative"} correlation** (r = {corr:.2f}) — longer-tenured customers spend modestly more, consistent with typical retention/loyalty patterns.
- Average monthly spend by channel:
{chr(10).join(f"  - {ch}: ${v:.2f}" for ch, v in channel_avg.items())}
- Spend distribution is right-skewed even after capping — most customers cluster in a moderate spend band, with a smaller group of high-value customers pulling the mean upward.

## Suggested next-step analyses
- Segment customers into value tiers (e.g., low/medium/high spend) and profile each by channel and tenure.
- Test whether channel differences in spend are statistically significant (t-test/ANOVA) rather than assumed from means alone.
- Bring in a churn/cancellation flag (not present in this synthetic dataset) to study whether spend or tenure predicts churn risk.
"""
with open("insight_memo.md", "w") as f:
    f.write(memo)

print("Done. See insight_memo.md, data/customers_clean.csv, and charts/*.png")
print(memo)
