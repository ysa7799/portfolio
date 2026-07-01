# Retail Sales Analysis — SQL

SQL analysis of a simulated 12-month retail dataset (10 products, 4 categories, ~3,100 transactions) covering joins, aggregations, CTEs, and window functions.

## Files
- `build_db.py` — generates `retail_sales.db` (SQLite) with seasonal sales data
- `queries.sql` — 5 analysis queries
- `retail_sales.db` — pre-built database (ready to query as-is)

## Run it
```bash
python3 build_db.py          # regenerate the database (optional, already included)
sqlite3 retail_sales.db < queries.sql
```

## Queries and findings (from actual run)
1. **Monthly revenue by category** — Electronics leads every month ($6.5K–$8.3K), Home a close second.
2. **Top 3 products/month (RANK window function)** — Smart Watch and Air Fryer trade the #1 spot most months.
3. **Month-over-month % change (LAG window function)** — March saw a +78.3% jump vs. February; most other months move ±10%.
4. **Below-average-revenue products (CTE)** — Sunglasses, Yoga Mat, Desk Lamp, Backpack, Dumbbell Set underperform the product average — candidates for promotion or delisting review.
5. **Holiday vs. post-holiday seasonality** — Electronics revenue drops ~64% from Nov–Dec to Jan–Feb ($41.1K → $14.9K); every category shows the same seasonal cliff.

## Skills demonstrated
Multi-table JOINs, GROUP BY aggregation, CTEs, window functions (RANK, LAG), seasonality analysis, translating query output into business recommendations.
