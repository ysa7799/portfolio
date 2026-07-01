# Operations KPI Dashboard

Excel/Power-BI-style KPI dashboard built from simulated security-operations incident data — modeled on the kind of daily logs kept in a physical-security/G4S environment.

## What it does
- Generates 12 months of synthetic incident data (~970 records) across 5 categories: Access Control, Alarm Response, Patrol Finding, Equipment Fault, Visitor Incident
- Aggregates monthly incident volume and average response time
- Builds a 4-sheet Excel workbook: **Raw Data**, **KPI Summary** (with bar + line charts), **Category Trends** (stacked bar), **Insights**

## Run it
```bash
pip install pandas numpy openpyxl
python3 generate_dashboard.py
```
Output: `data/operations_kpi_dashboard.xlsx`

## Key insights (auto-generated on last run)
- ~970 incidents logged across the simulated year
- Alarm Response consistently shows the fastest average response time (highest-priority category, dedicated response team)
- Incident volume rises ~30–40% in June–August — recommend adjusting shift staffing for peak months

## Skills demonstrated
PivotTable-equivalent aggregation in pandas, KPI definition, native Excel chart generation (openpyxl), stakeholder-ready insight summarization.
