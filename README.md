# Yusuf Hakeem — Data Analyst Portfolio

Static single-page portfolio site. No build step, no framework — plain HTML/CSS.

Live: https://yusufhakeem.app

## Structure
- `index.html` — all page content
- `style.css` — all styling
- `script.js` — scroll-reveal animation + mobile nav toggle
- `assets/` — CV (PDF/DOCX), headshot photo, project thumbnail images
- `projects/` — 5 project case studies, each with its own code, data, README, and pptx presentation:
  - `bahrain-import-trade-analysis` — General Assembly capstone (324K+ transactions, 221 countries)
  - `retail-sales-sql-analysis` — SQL (joins, CTEs, window functions)
  - `customer-behavior-exploration` — Python/pandas EDA
  - `operations-kpi-dashboard` — Excel/Power BI-style KPI workbook
  - `data-quality-checklist` — reusable data validation template

## Deploy
- **Vercel**: `vercel --prod` from this directory, or connect the GitHub repo in the Vercel dashboard.
- **Netlify**: `netlify deploy --prod` from this directory, or connect the GitHub repo in the Netlify dashboard.
- **GitHub**: `git remote add origin https://github.com/ysa7799/portfolio.git && git push -u origin main`
