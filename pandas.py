# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015],
    'Revenue': [1500, 1800, 2000, 2200, 2400, 2600],
    'Profit': [500, 600, 650, 700, 750, 800],
    'Expenses': [1000, 1200, 1300, 1400, 1500, 1600]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Line graph: Plot Revenue and Profit over the years
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Revenue'], label='Revenue', marker='o', linestyle='-', color='blue')
plt.plot(df['Year'], df['Profit'], label='Profit', marker='s', linestyle='--', color='green')
plt.title('Revenue and Profit over the Years')
plt.xlabel('Year')
plt.ylabel('Amount in USD')
plt.legend()
plt.grid(True)
plt.show()

# Bar graph: Plot Revenue and Expenses for comparison
plt.figure(figsize=(10, 6))
df[['Revenue', 'Expenses']].plot(kind='bar', x=df['Year'], figsize=(10, 6))
plt.title('Revenue vs Expenses by Year')
plt.xlabel('Year')
plt.ylabel('Amount in USD')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot: Plot Profit vs Revenue
plt.figure(figsize=(10, 6))
plt.scatter(df['Revenue'], df['Profit'], color='red', label='Profit vs Revenue')
plt.title('Scatter Plot: Profit vs Revenue')
plt.xlabel('Revenue (in USD)')
plt.ylabel('Profit (in USD)')
plt.legend()
plt.grid(True)
plt.show()
