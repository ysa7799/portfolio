# Data Quality Checklist Template

A reusable checklist for validating any new dataset before it goes into analysis or a dashboard. Built from the kind of validation habits required for auditable operational logging — applied to data pipelines.

## Schema
- [ ] Column names match expected schema (no typos, consistent casing)
- [ ] Data types are correct (dates parse as dates, numbers aren't stored as text)
- [ ] Required columns are present; no unexpected columns silently added

## Completeness
- [ ] Row count matches expectation (compare against source system count)
- [ ] Missing-value rate calculated per column — flag any column >5% missing
- [ ] Missing values have a documented handling decision (impute, drop, flag) — never silently ignored

## Duplicates
- [ ] Primary key / unique identifier has no duplicates
- [ ] Full-row duplicates checked and removed if unintentional
- [ ] Fuzzy duplicates checked where relevant (e.g., same customer, slightly different name/email)

## Outliers & Consistency
- [ ] Numeric columns checked for impossible values (negative ages, dates in the future, etc.)
- [ ] Outliers identified (e.g., >99th percentile) and a handling decision documented (cap, remove, keep + flag)
- [ ] Categorical columns checked for inconsistent labels (e.g., "USA" vs "United States" vs "U.S.")
- [ ] Referential integrity checked (foreign keys match a valid parent record)

## Sign-off
- [ ] Validation results documented (this checklist + issue log filled in)
- [ ] Known issues communicated to stakeholders before analysis begins
- [ ] Re-run this checklist after any upstream schema or source-system change

---
See `issue_log_template.csv` for tracking specific issues found during a validation pass.
