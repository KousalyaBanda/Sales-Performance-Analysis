import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Total Revenue
print("Total Sales:", df["Sales"].sum())

# Total Profit
print("Total Profit:", df["Profit"].sum())

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

# Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum()

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

# Plot 1
plt.figure(figsize=(6,4))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Category-wise Sales")
plt.savefig("plots/category_sales.png")
plt.show()

# Plot 2
plt.figure(figsize=(6,4))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Region-wise Sales")
plt.savefig("plots/region_sales.png")
plt.show()

# Plot 3
plt.figure(figsize=(6,4))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.savefig("plots/monthly_sales.png")
plt.show()