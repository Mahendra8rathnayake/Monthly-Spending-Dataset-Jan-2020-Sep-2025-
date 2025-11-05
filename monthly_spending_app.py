import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
# Page Setup
# --------------------------
st.set_page_config(page_title="Monthly Spending Dashboard", layout="wide")
st.title("💳 Monthly Spending Dashboard (2020–2025)")
st.write("Upload your dataset to explore financial metrics, trends, and category insights.")

# --------------------------
# File Upload
# --------------------------
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Detected Columns")
    st.write(list(df.columns))
    
    # --------------------------
    # Robust Column Detection
    # --------------------------
    # Month column detection
    month_cols = [c for c in df.columns if 'month' in c.lower()]
    if month_cols:
        df['month'] = pd.to_datetime(df[month_cols[0]])
    else:
        st.error("❌ Cannot detect a 'month' column.")
        st.stop()
    
    # Income column detection
    income_cols = [c for c in df.columns if 'income' in c.lower()]
    if income_cols:
        income_col = income_cols[0]
    else:
        st.error("❌ Cannot detect an 'income' column.")
        st.stop()
    
    # Total expenditure column detection
    expenditure_cols = [c for c in df.columns if 'total_expenditure' in c.lower()]
    if expenditure_cols:
        expenditure_col = expenditure_cols[0]
    else:
        st.error("❌ Cannot detect 'total_expenditure' column.")
        st.stop()
    
    # Numeric columns for categories
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    category_cols = [c for c in numeric_cols if c not in [income_col, expenditure_cols[0]]]
    
    # --------------------------
    # Year Column
    # --------------------------
    df['year'] = df['month'].dt.year
    
    st.success("✅ File processed successfully!")
    
    # --------------------------
    # Sidebar Navigation
    # --------------------------
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["EDA", "Financial Metrics", "Category Analysis"])
    
    # --------------------------
    # PAGE 1: EDA
    # --------------------------
    if page == "EDA":
        st.subheader("📊 Exploratory Data Analysis")
        st.dataframe(df.head())
        st.write(df.describe())
        
        # Total expenditure trend
        st.subheader("Total Expenditure Over Time")
        fig = px.line(df, x='month', y=expenditure_cols[0], title="Total Expenditure Trend", markers=True)
        st.plotly_chart(fig, use_container_width=True)
        
        # Income vs Expenditure
        st.subheader("Income vs Total Expenditure")
        fig2 = px.line(df, x='month', y=[income_col, expenditure_cols[0]], title="Income vs Expenditure")
        st.plotly_chart(fig2, use_container_width=True)
    
    # --------------------------
    # PAGE 2: Financial Metrics
    # --------------------------
    elif page == "Financial Metrics":
        st.subheader("📈 Average Income Growth per Year")
        income_growth = df.groupby('year')[income_col].mean().pct_change()
        st.write(income_growth)
        
        fig = px.bar(income_growth, title="Average Income Growth per Year")
        st.plotly_chart(fig, use_container_width=True)
        
        # Savings rate
        if 'savings_' in df.columns:
            st.subheader("Savings Rate Over Time")
            df['savings_rate_'] = (df['savings_'] / df[income_col]) * 100
            fig2 = px.line(df, x='month', y='savings_rate_', title="Savings Rate (%)")
            st.plotly_chart(fig2, use_container_width=True)
    
    # --------------------------
    # PAGE 3: Category Analysis
    # --------------------------
    elif page == "Category Analysis":
        st.subheader("💰 Category Contribution to Total Expenditure")
        
        contribution = (df[category_cols].sum() / df[expenditure_cols[0]].sum()) * 100
        contribution = contribution.sort_values(ascending=False)
        st.write(contribution)
        
        # Bar chart
        fig = px.bar(contribution, orientation='h', title="Category Contribution (%)")
        st.plotly_chart(fig, use_container_width=True)
        
        # Pie chart
        fig2 = px.pie(contribution, values=contribution.values, names=contribution.index, title="Spending Category Distribution")
        st.plotly_chart(fig2, use_container_width=True)
        
else:
    st.info("📂 Please upload the CSV file to begin.")

