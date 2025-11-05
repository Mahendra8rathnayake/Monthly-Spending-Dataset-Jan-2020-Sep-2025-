import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Financial Metrics Dashboard")

# ---------------------------
# File Upload
# ---------------------------
uploaded = st.file_uploader("Upload monthly_spending_dataset_2020_2025.csv", type=['csv'])

if uploaded is not None:
    df = pd.read_csv(uploaded)

    # Ensure date column is datetime
    df['month'] = pd.to_datetime(df['month'])

    # Extract year column
    df['year'] = df['month'].dt.year

    st.success("✅ File uploaded successfully!")

    st.subheader("📌 Dataset Preview")
    st.write(df.head())

    # ================================
    # ✅ Average Income Growth per Year
    # ================================
    st.subheader("📈 Average Income Growth per Year")

    income_growth = df.groupby('year')['income_'].mean().pct_change()

    st.write(income_growth)

    # Line Chart
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(income_growth.index, income_growth.values, marker='o')
    ax1.set_title("Average Income Growth per Year (%)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Growth Rate")
    st.pyplot(fig1)

    # ==========================================
    # ✅ Category Contribution to Total Spending
    # ==========================================
    st.subheader("🥧 Category Contribution to Total Spending (%)")

    numeric_cols = [col for col in df.columns if col.endswith('_')]

    contribution = (df[numeric_cols].sum() / df['total_expenditure_'].sum()) * 100
    contribution = contribution.sort_values(ascending=False)

    st.write(contribution)

    # Pie Chart
    fig2, ax2 = plt.subplots(figsize=(7, 7))
    ax2.pie(contribution.values, labels=contribution.index, autopct="%1.1f%%")
    ax2.set_title("Category Contribution (%)")
    st.pyplot(fig2)

else:
    st.warning("📂 Please upload the dataset to begin.")
