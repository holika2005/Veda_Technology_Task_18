# Task 18 — Region Performance

## Objective
Compare sales across regions, compare profit as well as sales, and rank regions.

## Tools
Excel and Power BI. Python helper scripts are included to reproduce summaries and chart images.

## Dataset note
The official Superstore dataset was not attached, so this package includes an 800-row **synthetic Superstore-style practice dataset**, not the official Sample Superstore file. Replace it with the official dataset if exact-source compliance is required.

## Deliverables
- `data/superstore_region_performance_practice.csv` — practice data
- `outputs/Region_Performance_Analysis.xlsx` — Raw Data, Region Summary, Region by Category
- `outputs/region_summary.csv` — totals, margin, and separate sales/profit ranks
- `outputs/sales_by_region.png` and `outputs/profit_by_region.png` — bar charts
- `powerbi/Power_BI_Report_Guide.md` — DAX measures and report build steps
- `scripts/analyze_regions.py` — reproducible analysis

## Run helper
`pip install pandas matplotlib openpyxl` then `python scripts/analyze_regions.py`.

## Interpretation
Higher sales do not automatically mean higher profit. Compare total profit, profit margin and ranks before recommending a region.
