# Yusuf Hakeem — Data Analyst Portfolio

Static single-page portfolio site. No build step, no framework — plain HTML/CSS.

## Structure
- `index.html` — all page content
- `style.css` — all styling
- `assets/` — CV PDF + headshot photo

## Before deploying
1. Replace `assets/headshot-placeholder.svg` reference in `index.html` with a real photo saved as `assets/headshot.jpg`.
2. Create the 4 project repos referenced in the Projects section (or update the links to point wherever the code actually lives):
   - `operations-kpi-dashboard`
   - `retail-sales-sql-analysis`
   - `customer-behavior-exploration`
   - `data-quality-checklist`
3. Add a real phone number / confirm contact details.

## Deploy
- **Vercel**: `vercel --prod` from this directory, or connect the GitHub repo in the Vercel dashboard.
- **Netlify**: `netlify deploy --prod` from this directory, or connect the GitHub repo in the Netlify dashboard.
- **GitHub**: `git remote add origin https://github.com/ysa7799/portfolio.git && git push -u origin main`
