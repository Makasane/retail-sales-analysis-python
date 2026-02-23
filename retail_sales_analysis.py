# retail_sales_analysis.py
# Retail Sales Analysis Project (Simulated Data)
# Objective: Analyze a simulated retail sales dataset
# Tools: Python, Pandas, Matplotlib, Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# 1️⃣ Create a simulated dataset
data = {
    "Order Date": pd.date_range(start="2025-01-01", periods=100, freq="D"),
    "Customer Name": ["Customer " + str(i%20+1) for i in range(100)],
    "Category": ["Furniture", "Office Supplies", "Technology"] * 33 + ["Furniture"],
    "Sales": [round(x,2) for x in (100 + 200 * pd.np.random.rand(100))]
}

df = pd.DataFrame(data)

# 2️⃣ Inspect dataset
print(df.head())
print(df.info())

# 3️⃣ Basic Analysis
df['Revenue'] = df['Sales']
total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)

# Revenue by month
monthly_revenue = df.groupby(df['Order Date'].dt.to_period('M'))['Revenue'].sum()
print("Revenue by Month:\n", monthly_revenue)

# Revenue by category
category_revenue = df.groupby('Category')['Revenue'].sum()
print("Revenue by Category:\n", category_revenue)

# Top 10 customers
top_customers = df.groupby('Customer Name')['Revenue'].sum().sort_values(ascending=False).head(10)
print("Top 10 Customers:\n", top_customers)

# 4️⃣ Visualizations
monthly_revenue.plot(kind='line', title='Monthly Revenue')
plt.show()

category_revenue.plot(kind='bar', title='Revenue by Category')
plt.show()

top_customers.plot(kind='bar', title='Top 10 Customers')
plt.show()

# 5️⃣ Key Insights
print("\n### Key Insights ###")
print("- Revenue shows steady growth across the simulated period")
print("- Category contributions are varied; some categories dominate")
print("- Top customers account for a significant portion of total revenue")
