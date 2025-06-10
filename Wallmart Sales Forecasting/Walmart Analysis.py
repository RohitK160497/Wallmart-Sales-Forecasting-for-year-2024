import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:\\Users\\khila\\PycharmProjects\\Wallmart Analysis\\Wallmart sales\\Walmart_sales.csv'
data = pd.read_csv(file_path)


# Convert 'Date' column to datetime with the correct format ('DD-MM-YYYY')
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Exploratory Data Analysis (EDA)

# Plot total weekly sales over time
total_weekly_sales = data.groupby('Date')['Weekly_Sales'].sum()

plt.figure(figsize=(12, 6))
total_weekly_sales.plot()
plt.title('Total Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Weekly Sales')
plt.grid(True)
plt.show()

# Analyze average weekly sales during holidays vs. non-holidays
holiday_sales = data.groupby('Holiday_Flag')['Weekly_Sales'].mean()

plt.figure(figsize=(8, 5))
holiday_sales.plot(kind='bar', color=['skyblue', 'orange'])
plt.title('Average Weekly Sales: Holiday vs Non-Holiday Weeks')
plt.xlabel('Holiday Flag (0: Non-Holiday, 1: Holiday)')
plt.ylabel('Average Weekly Sales')
plt.xticks(ticks=[0, 1], labels=['Non-Holiday', 'Holiday'], rotation=0)
plt.grid(axis='y')
plt.show()

# Correlation analysis
correlation_matrix = data[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix: Weekly Sales and External Factors')
plt.show()
