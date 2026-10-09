import pandas as pd

# 1. Read the CSV file
df = pd.read_csv("sales.csv")

print("--- INITIAL DATA ---")
print(df)

# 2. Add a new column for total sales (Price x Quantity)
df["total_sales"] = df["price"] * df["quantity"]

print("\n--- AFTER CALCULATING TOTAL SALES ---")
print(df)

# 3. Calculate overall revenue from all products
overall_revenue = df["total_sales"].sum()
print(f"\nOverall revenue: {overall_revenue} €")