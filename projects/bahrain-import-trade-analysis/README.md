# Bahrain Import Trade Analysis (2025) — General Assembly Capstone

Data Analytics capstone project (DAP-PT-16, General Assembly). Full-year analysis of Bahrain's 2025 import economy using official government trade data — concentration risk, commodity mix, seasonality, and growth signals.

## Dataset
- **Source**: Bahrain Open Data Portal (data.gov.bh) — official Bahrain Government, Customs Affairs Authority
- **Coverage**: January–December 2025, full calendar year
- **Scale**: 324,818 transactions · 221 source countries · 6,335 commodity types
- **Total value**: $16.45B USD (BD 6.19B) — fixed peg of 1 BD = 2.6596 USD confirmed with zero variance across every transaction
- **Cleaning**: 0 nulls after cleaning, 0 duplicates, 59 Namibia UN codes filled, 1 negative value flagged and handled

## Four analytical questions
1. **Source country concentration** — how dependent is Bahrain on a small number of trading partners?
2. **Commodity basket analysis** — is the import mix diversified or concentrated in a few raw materials?
3. **Seasonal import patterns** — are there predictable monthly peaks and dips?
4. **Growth signals** — which commodity categories grew fastest H1→H2 2025, and what does that reveal about Bahrain's economic direction?

## Key findings

**Country concentration**: China leads at $2.353B (14.3%), followed by Australia ($1.546B, 9.4%) and UAE ($1.430B, 8.7%). The top 3 partners alone account for 32.4% of all imports. Australia's total is almost entirely one commodity (aluminium oxide for ALBA) — a single-product dependency masquerading as a trade relationship.

**Commodity concentration**: Aluminium oxide ($1.483B) and iron ore ($1.459B) together make up 17.9% of all imports — Bahrain's industrial base (aluminium smelting via ALBA) drives extreme concentration in just two raw materials.

**Seasonality**: Imports swing 26% between the April peak ($1.53B, post-Q1/pre-summer restocking) and the June dip ($1.22B, summer slowdown) — a planning-relevant gap for procurement and cash flow.

**Growth signal**: Solar panel imports grew **+1,105%** from H1 to H2 2025 — the clearest early indicator of Bahrain's clean energy transition actually showing up in trade data, ahead of most public commentary on the topic.

## Recommendations delivered
- Diversify aluminium oxide sourcing beyond Australia (Guinea, Brazil, Jamaica)
- Build 90-day strategic reserves for aluminium oxide and iron ore given inelastic industrial demand
- Align procurement calendars to the April peak / June dip seasonal cycle
- Scale customs, port, and logistics infrastructure ahead of continued solar import growth
- Establish a trade intelligence monitoring unit at the Ministry of Industry, Commerce and Tourism (MOICT) for real-time concentration and dependency tracking

## Limitations (stated honestly in the capstone)
- Single year of data — can't separate 2025-specific anomalies from long-term trends
- No export data — full trade balance and re-export activity (notably via UAE) can't be measured
- Only 12 monthly data points — time-series forecast models returned low R² (0.04–0.16); directionally useful, not statistically strong
- No GDP/inflation linkage available to normalize real vs. nominal growth
- Inconsistent units across commodities (NO, KG, L, T, SQM) limit price-per-unit comparability without standardization

## Files
- `Capstone_Presentation.pptx` / `.pdf` — full 13-slide capstone deck as presented

## Skills demonstrated
Large-scale real-world data cleaning (324K+ rows, official government source), concentration/dependency risk analysis, seasonality analysis, growth-rate analysis (H1 vs H2), translating findings into policy-relevant recommendations, and transparent limitation reporting.
