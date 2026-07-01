-- Retail Sales Analysis — SQL
-- Run against retail_sales.db (build with build_db.py)
-- sqlite3 retail_sales.db < queries.sql

-- 1. Monthly revenue by category (JOIN + aggregation)
SELECT
    strftime('%Y-%m', s.sale_date) AS month,
    p.category,
    ROUND(SUM(s.quantity * p.unit_price), 2) AS revenue
FROM sales s
JOIN products p ON p.product_id = s.product_id
GROUP BY month, p.category
ORDER BY month, revenue DESC;

-- 2. Top 3 products by revenue each month (window function: RANK)
WITH monthly_product_revenue AS (
    SELECT
        strftime('%Y-%m', s.sale_date) AS month,
        p.product_name,
        SUM(s.quantity * p.unit_price) AS revenue
    FROM sales s
    JOIN products p ON p.product_id = s.product_id
    GROUP BY month, p.product_name
),
ranked AS (
    SELECT *,
        RANK() OVER (PARTITION BY month ORDER BY revenue DESC) AS rnk
    FROM monthly_product_revenue
)
SELECT month, product_name, ROUND(revenue, 2) AS revenue, rnk
FROM ranked
WHERE rnk <= 3
ORDER BY month, rnk;

-- 3. Month-over-month revenue change (window function: LAG)
WITH monthly_revenue AS (
    SELECT
        strftime('%Y-%m', s.sale_date) AS month,
        SUM(s.quantity * p.unit_price) AS revenue
    FROM sales s
    JOIN products p ON p.product_id = s.product_id
    GROUP BY month
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(revenue - LAG(revenue) OVER (ORDER BY month), 2) AS mom_change,
    ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month), 1) AS mom_pct_change
FROM monthly_revenue
ORDER BY month;

-- 4. Underperforming products (CTE: below-average revenue)
WITH product_revenue AS (
    SELECT p.product_name, p.category, SUM(s.quantity * p.unit_price) AS revenue
    FROM sales s
    JOIN products p ON p.product_id = s.product_id
    GROUP BY p.product_name, p.category
),
avg_revenue AS (
    SELECT AVG(revenue) AS avg_rev FROM product_revenue
)
SELECT product_name, category, ROUND(revenue, 2) AS revenue
FROM product_revenue, avg_revenue
WHERE revenue < avg_rev
ORDER BY revenue ASC;

-- 5. Seasonality check: Nov-Dec vs Jan-Feb revenue by category
SELECT
    p.category,
    ROUND(SUM(CASE WHEN CAST(strftime('%m', s.sale_date) AS INTEGER) IN (11,12)
        THEN s.quantity * p.unit_price ELSE 0 END), 2) AS holiday_revenue,
    ROUND(SUM(CASE WHEN CAST(strftime('%m', s.sale_date) AS INTEGER) IN (1,2)
        THEN s.quantity * p.unit_price ELSE 0 END), 2) AS post_holiday_revenue
FROM sales s
JOIN products p ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY holiday_revenue DESC;
