from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data"/"superstore_region_performance_practice.csv")
s=df.groupby("Region",as_index=False).agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit","sum"),Order_Count=("Order ID","nunique"),Units_Sold=("Quantity","sum"))
s["Profit_Margin_Pct"]=(s.Total_Profit/s.Total_Sales*100).round(2)
s["Sales_Rank"]=s.Total_Sales.rank(method="dense",ascending=False).astype(int)
s["Profit_Rank"]=s.Total_Profit.rank(method="dense",ascending=False).astype(int)
s=s.sort_values("Total_Sales",ascending=False); out=ROOT/"outputs"; out.mkdir(exist_ok=True); s.to_csv(out/"region_summary.csv",index=False)
for metric,title,file in [("Total_Sales","Total Sales by Region","sales_by_region.png"),("Total_Profit","Total Profit by Region","profit_by_region.png")]:
 plt.figure(figsize=(8,5)); plt.bar(s.Region,s[metric]); plt.title(title); plt.xlabel("Region"); plt.ylabel(metric.replace("_"," ")); plt.tight_layout(); plt.savefig(out/file,dpi=150); plt.close()
print(s.to_string(index=False))
