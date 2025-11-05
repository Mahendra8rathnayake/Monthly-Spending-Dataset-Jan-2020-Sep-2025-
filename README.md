# 💳 Monthly Spending Dashboard (2020–2025)

An interactive **Streamlit multi-page dashboard** for analyzing personal spending, income trends, financial habits, and category-wise expenditure distribution using the dataset **monthly_spending_dataset_2020_2025.csv**.

This dashboard helps users:
✅ Understand spending patterns  
✅ Track income growth  
✅ Analyze savings & investment behavior  
✅ Identify high-impact expense categories  
✅ Visualize trends across 2020–2025  

---

## 🚀 Features

### ✅ **1. Multi-Page Streamlit App**
- **Homepage** – Upload dataset  
- **EDA Dashboard** – Dataset preview, summary stats, spending trends  
- **Financial Metrics** – Income growth %, spending ratio, savings rate  
- **Category Analysis** – Category contribution %, pie charts, bar charts  

---

## 📂 Project Structure

my_spending_dashboard/
│── streamlit_app.py
│── pages/
│ ├── 1_📊_EDA_Dashboard.py
│ ├── 2_📈_Financial_Metrics.py
│ ├── 3_💰_Category_Analysis.py
│── monthly_spending_dataset_2020_2025.csv
│── README.md

markdown
Copy code

---

## 📊 Dataset Overview

The dataset contains monthly financial records from **2020–2025**, including:

- `income_`
- `total_expenditure_`
- `groceries_`
- `rent_`
- `utilities_`
- `transportation_`
- `dining_&_entertainment_`
- `shopping_&_wants_`
- `investments_`
- `savings_`
- `emi/loans_`
- `gym_`
- `savings_rate_`
- `investment_rate_`
- `spending_ratio_`
- `year`

---

## 🔧 Installation & Setup

### **1. Clone the repository**
```sh
git clone https://github.com/yourusername/monthly-spending-dashboard.git
cd monthly-spending-dashboard