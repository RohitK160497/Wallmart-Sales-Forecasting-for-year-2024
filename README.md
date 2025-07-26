# 🛒 Walmart Retail Sales Analysis & Forecasting

## 📌 Project Overview

This project analyzes Walmart's historical retail sales data across multiple stores to extract meaningful patterns and forecast future sales using data visualization and statistical methods. The focus is on understanding **sales trends**, **holiday effects**, and **external factors** such as **temperature**, **fuel price**, **CPI**, and **unemployment**.

---

## 🗃️ Dataset Summary

- **Source:** Walmart Sales Data
- **Frequency:** Weekly
- **Key Fields:**
  - `Store`: Store ID
  - `Date`: Week ending date
  - `Weekly_Sales`: Weekly revenue per store
  - `Holiday_Flag`: Indicates presence of a holiday week
  - `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`: External factors

---

## 🧪 Questions Explored

1. **📈 What is the trend of weekly sales over time?**  
   > We identify seasonal peaks and dips, typically around holidays.

2. **🎉 How do holidays impact sales?**  
   > Sales show a noticeable spike during holiday weeks vs. non-holiday periods.

3. **🌦️ Do external economic and weather factors influence sales?**  
   > Moderate correlation found with CPI and temperature; weaker with fuel price and unemployment.

---

## 📊 Visualizations

### 1️⃣ Weekly Sales Trend Over Time
<img width="1280" height="692" alt="op1" src="https://github.com/user-attachments/assets/805ae4d9-0dfa-42a1-b4c0-a3ec2ffbc897" />


- Displays seasonality and upward trends during holiday periods.

### 2️⃣ Holiday vs Non-Holiday Weekly Sales
<img width="1280" height="692" alt="op2" src="https://github.com/user-attachments/assets/36a7707e-39be-423c-8a11-d1fa0602f6ed" />


- Clear uplift in sales during holiday weeks.

### 3️⃣ Correlation Heatmap with External Factors
<img width="1280" height="692" alt="op3" src="https://github.com/user-attachments/assets/8ddc14b0-2b31-4d2b-bb87-bae0a0d3d35d" />


- Highlights varying influence levels of external factors on weekly sales.

---

## 🧠 Key Insights

- **Seasonality:** Sales spike consistently during holidays (e.g., Thanksgiving, Christmas).
- **Holiday Impact:** Holidays are positively correlated with higher sales.
- **External Influence:** CPI and temperature moderately affect sales, while fuel price and unemployment rate show weaker influence.

---

## 🛠 Tools & Technologies

- **Python:** Data processing and visualization (`pandas`, `matplotlib`, `seaborn`)
- **Excel:** Initial data review
- **PyCharm:** For code execution and debugging

---


