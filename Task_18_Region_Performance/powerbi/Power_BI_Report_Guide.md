# Power BI Report Guide — Region Performance

1. Import `data/superstore_region_performance_practice.csv` via Get Data > Text/CSV.
2. Set Order Date to Date, Sales/Profit to Decimal Number, Quantity to Whole Number.
3. Create measures:
```DAX
Total Sales = SUM(SuperstorePractice[Sales])
Total Profit = SUM(SuperstorePractice[Profit])
Order Count = DISTINCTCOUNT(SuperstorePractice[Order ID])
Units Sold = SUM(SuperstorePractice[Quantity])
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
Sales Rank = RANKX(ALL(SuperstorePractice[Region]), [Total Sales], , DESC, DENSE)
Profit Rank = RANKX(ALL(SuperstorePractice[Region]), [Total Profit], , DESC, DENSE)
```
4. Add clustered bar charts with Region as Axis and Total Sales / Total Profit as Values. Add a table with region totals, margin and ranks. Add Category and Order Date slicers.

A native PBIX is not included; create and save it in Power BI Desktop using these steps.
