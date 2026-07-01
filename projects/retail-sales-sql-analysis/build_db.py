"""
Builds a small SQLite retail-sales database with realistic seasonality so the
SQL in queries.sql runs against real data. Run this once before running queries.

Run: python3 build_db.py
Output: retail_sales.db
"""
import random
import sqlite3
from datetime import date, timedelta

random.seed(7)

conn = sqlite3.connect("retail_sales.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unit_price REAL
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date TEXT,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

products = [
    (1, "Wireless Earbuds", "Electronics", 24.99),
    (2, "Smart Watch", "Electronics", 59.99),
    (3, "Yoga Mat", "Fitness", 19.99),
    (4, "Dumbbell Set", "Fitness", 39.99),
    (5, "Coffee Maker", "Home", 34.99),
    (6, "Air Fryer", "Home", 69.99),
    (7, "Desk Lamp", "Home", 14.99),
    (8, "Backpack", "Accessories", 29.99),
    (9, "Sunglasses", "Accessories", 12.99),
    (10, "Bluetooth Speaker", "Electronics", 27.99),
]
cur.executemany("INSERT INTO products VALUES (?,?,?,?)", products)

start = date(2025, 1, 1)
for i in range(365):
    d = start + timedelta(days=i)
    seasonal = 1.6 if d.month in (11, 12) else (0.7 if d.month in (1, 2) else 1.0)
    for p in products:
        base = {"Electronics": 4, "Fitness": 2, "Home": 3, "Accessories": 2}[p[2]]
        qty = max(0, int(random.gauss(base, 1.5) * seasonal))
        if qty > 0:
            cur.execute(
                "INSERT INTO sales (sale_date, product_id, quantity) VALUES (?,?,?)",
                (d.isoformat(), p[0], qty),
            )

conn.commit()
n = cur.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
print(f"Built retail_sales.db — {n} sale rows, {len(products)} products")
conn.close()
