# 🏡 Luxury_Housing_Sales_Analysis

This project is based on a luxury housing dataset, where I analyzed booking trends, pricing patterns, and buyer behavior across different micro markets. I also created an interactive dashboard using Power BI to present the insights clearly.

---

## 📂 Project Workflow

```text
Raw CSV Dataset
      ↓
Data Cleaning using Python
      ↓
Feature Engineering
      ↓
PostgreSQL Database
      ↓
SQL Validation Queries
      ↓
Streamlit Dashboard
      ↓
Business Insights
```
---

## 🛠 Tools & Technologies

1. Python
2. Pandas
3. PostgreSQL
4. SQLAlchemy
5. Streamlit
6. Plotly
7. GitHub

---

## 📁 Project Structure

```
Luxury_Housing_Sales_Analysis/
│
├── app.py
├── cleaned_luxury_housing.csv
├── Data_Cleaning_process.ipynb
├── Luxury_Housing_Bangalore.csv
├── README.md
└── Sql.ipynb
```

## Project Steps

1. **Data Cleaning**

   * Handled missing values
   * Standardized column formats
   * Cleaned text fields like micro-market and builder names

2. **Feature Engineering**

   * Created `Booking_Flag`
   * Created `Quarter_Label`
   * Created `Price_per_Sqft`

3. **SQL Integration**

   * Loaded cleaned data into PostgreSQL
   * Performed validation and aggregation queries

4. **Dashboard Development**

   * Built an interactive Streamlit dashboard
   * Created 10 business visualizations

5. **Insight Generation**

   * Analyzed market trends, builder performance, booking conversion, and buyer behavior


## ▶️ How to View the Dashboard

1. Download the `.pbix` file from this repository
2. Open it using Power BI Desktop
3. Explore the dashboard pages and visuals


## Key Insights

* Booking trends change across quarters and micro-markets.
* Prestige, SNN Raj, Brigade, L&T Realty, and Total Environment are among the top revenue-generating builders.
* Configuration demand is almost equally distributed across 3BHK, 4BHK, and 5BHK+.
* Sales channels show nearly balanced booking conversion rates.
* Top builders can be identified clearly through KPI cards and revenue comparison.


## How to Run

```bash
pip install pandas streamlit plotly sqlalchemy psycopg2-binary
streamlit run app.py
```

---

## Conclusion

This project converts raw luxury housing data into a clean and interactive business dashboard.
It shows how Python, SQL, and Streamlit can be used together to generate useful real estate insights.

---

## Author

**KIRUBAKARAN R**

---
