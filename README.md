# 🏠 Luxury Housing Sales Analysis – Bengaluru

This project analyzes luxury housing sales data from Bengaluru to understand booking trends, builder performance, configuration demand, buyer behavior, sales channel efficiency, and top-performing micro-markets/builders.

The project was completed using Python for data cleaning, PostgreSQL for database storage, and Streamlit for dashboard presentation.

---

## 📌 Project Objective

The main objective of this project is to convert raw luxury housing data into meaningful business insights through data cleaning, SQL integration, and an interactive Streamlit dashboard.

The dashboard helps answer important real estate business questions such as:

- Which micro-markets have stronger booking trends?
- Which builders generate the highest revenue?
- Which configurations are most in demand?
- Which sales channels perform better?
- Which builders are top performers by revenue and booking success?

---

## 🧰 Tools & Technologies Used

- Python
- Pandas
- NumPy
- PostgreSQL
- SQLAlchemy
- Streamlit
- Plotly
- VS Code 
- GitHub

---

## 📂 Project Workflow

1. **Data Collection**
   - Loaded the luxury housing dataset.

2. **Data Cleaning**
   - Handled missing values.
   - Standardized column formats.
   - Cleaned text fields such as micro-market and builder names.
   - Converted numerical columns into proper data types.

3. **Feature Engineering**
   - Created useful columns such as:
     - `Price_per_Sqft`
     - `Quarter_Number`
     - `Quarter_Label`
     - `Booking_Flag`

4. **SQL Integration**
   - Loaded the cleaned dataset into PostgreSQL.
   - Ran validation and aggregation queries.

5. **Dashboard Development**
   - Created an interactive dashboard using Streamlit and Plotly.
   - Added navigation pages for different analysis sections.

6. **Insight Generation**
   - Created visualizations and business insights for all 10 analysis questions.

---

## 📊 Dashboard Sections

### 🏠 Home Page
Introduces the Luxury Housing Sales Analysis Dashboard.

### 📈 Analysis 1: Market Trends & Performance

1. **Market Trends**
   - Shows how bookings changed quarter by quarter across top micro-markets.

2. **Builder Performance**
   - Shows the top builders based on total ticket sales.

3. **Amenity Impact**
   - Shows the relationship between amenity score and booking conversion rate.

4. **Booking Conversion**
   - Shows booked vs not booked percentage by micro-market.

### 💰 Analysis 2: Demand, Sales Channel & Builder Contribution

5. **Configuration Demand**
   - Shows the most in-demand housing configurations using a donut chart.

6. **Sales Channel Efficiency**
   - Compares booking conversion across different sales channels.

7. **Quarterly Builder Contribution**
   - Shows quarter-wise builder contribution using a matrix table.

### 🏙️ Analysis 3: Buyer & Project Insights

8. **Possession Status Analysis**
   - Shows how possession status affects booking decisions by buyer type.

9. **Geographical Insights**
   - Shows project concentration across Bengaluru micro-markets.

10. **Top Performers**
   - Displays the top 5 builders based on revenue and successful bookings.

---

## 📈 Key Insights

- Booking trends vary across micro-markets and quarters.
- Top builders such as Prestige, SNN Raj, Brigade, L&T Realty, and Total Environment contribute strongly to revenue.
- Configuration demand is almost evenly distributed among 3BHK, 4BHK, and 5BHK+.
- Sales channels show nearly balanced booking conversion rates.
- Certain micro-markets show slightly better booking conversion and project concentration.
- Top performers can be identified clearly using KPI cards and detailed tables.

---

## ▶️ How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/your-username/Luxury_Housing_Sales_Analysis.git
```

2. Go to the project folder:

```bash
cd Luxury_Housing_Sales_Analysis
```

3. Install required libraries:

```bash
pip install pandas numpy streamlit plotly sqlalchemy psycopg2-binary
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

or

```bash
python3 -m streamlit run app.py
```

---

## 📁 Project Structure

```text
Luxury_Housing_Sales_Analysis/
│
├── app.py
├── cleaned_luxury_housing.csv
├── Luxury_Housing_Sales_Analysis_Documentation.docx
├── README.md
└── notebooks/
    └── data_cleaning_and_sql.ipynb
```

---

## 📄 Documentation

The full project documentation includes:

- Project overview
- Data cleaning steps
- SQL integration
- Dashboard screenshots
- 10 business questions
- Visualizations and insights
- Conclusion

---

## ✅ Conclusion

This project helped analyze the Bengaluru luxury housing market using a complete data analytics workflow. It covers data cleaning, SQL storage, dashboard creation, and insight generation. The final Streamlit dashboard provides a simple and interactive way to understand luxury housing sales performance, buyer behavior, and builder contribution.

---

## 👨‍💻 Author

**KIRUBAKARAN R**
