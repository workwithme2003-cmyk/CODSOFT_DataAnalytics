import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="Executive Sales & Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load data with caching
@st.cache_data
def load_data():
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "Task_2_EDA", "sales_dataset.csv"),
        os.path.join(os.path.dirname(__file__), "sales_dataset.csv"),
        "sales_dataset.csv"
    ]
    for p in possible_paths:
        if os.path.exists(p):
            df = pd.read_csv(p)
            df['Order_Date'] = pd.to_datetime(df['Order_Date'])
            return df
    st.error("Sales dataset not found!")
    st.stop()

df = load_data()

# Header
st.title("📊 Executive Sales & Analytics Dashboard")
st.markdown("Interactive analytical dashboard built according to official **Streamlit Best Practices** for CodSoft Data Analytics Internship.")

# Sidebar Filters
st.sidebar.header("🎯 Dashboard Filters")
region_filter = st.sidebar.multiselect("Select Region:", options=df['Region'].unique(), default=df['Region'].unique())
category_filter = st.sidebar.multiselect("Select Category:", options=df['Category'].unique(), default=df['Category'].unique())
segment_filter = st.sidebar.multiselect("Select Customer Segment:", options=df['Segment'].unique(), default=df['Segment'].unique())

# Filter dataframe
filtered_df = df[
    (df['Region'].isin(region_filter)) &
    (df['Category'].isin(category_filter)) &
    (df['Segment'].isin(segment_filter))
]

# Calculate sparkline trend series
monthly_trend_sales = filtered_df.set_index('Order_Date').resample('ME')['Sales'].sum().tolist()
monthly_trend_profit = filtered_df.set_index('Order_Date').resample('ME')['Profit'].sum().tolist()

# Top Key Performance Indicators (KPI Row using cards & sparklines)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Total Revenue", 
        value=f"${filtered_df['Sales'].sum():,.2f}",
        border=True,
        chart_data=monthly_trend_sales if len(monthly_trend_sales) > 0 else None,
        chart_type="line"
    )

with col2:
    st.metric(
        label="Total Profit", 
        value=f"${filtered_df['Profit'].sum():,.2f}",
        border=True,
        chart_data=monthly_trend_profit if len(monthly_trend_profit) > 0 else None,
        chart_type="line"
    )

with col3:
    st.metric(
        label="Total Orders", 
        value=f"{len(filtered_df):,}",
        border=True
    )

with col4:
    st.metric(
        label="Avg Order Value", 
        value=f"${filtered_df['Sales'].mean():,.2f}" if len(filtered_df) > 0 else "$0.00",
        border=True
    )

with col5:
    margin = (filtered_df['Profit'].sum() / filtered_df['Sales'].sum() * 100) if filtered_df['Sales'].sum() > 0 else 0
    st.metric(
        label="Profit Margin", 
        value=f"{margin:.2f}%",
        border=True
    )

st.write("") # Spacer

# Charts Section organized in Card Containers
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    with st.container(border=True):
        st.subheader("📈 Monthly Revenue & Profit Trend")
        monthly_df = filtered_df.set_index('Order_Date').resample('ME').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
        fig_line = px.line(
            monthly_df, x='Order_Date', y=['Sales', 'Profit'],
            labels={'value': 'Amount ($)', 'Order_Date': 'Date', 'variable': 'Metric'},
            color_discrete_map={'Sales': '#1f77b4', 'Profit': '#2ca02c'},
            template="plotly_white"
        )
        st.plotly_chart(fig_line, use_container_width=True)

with row1_col2:
    with st.container(border=True):
        st.subheader("📊 Revenue Breakdown by Category & Sub-Category")
        cat_df = filtered_df.groupby(['Category', 'Sub_Category'])['Sales'].sum().reset_index()
        fig_bar = px.bar(
            cat_df, x='Category', y='Sales', color='Sub_Category',
            barmode='group', labels={'Sales': 'Revenue ($)'},
            template="plotly_white"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    with st.container(border=True):
        st.subheader("🍩 Market Share by Segment")
        fig_pie = px.pie(
            filtered_df, names='Segment', values='Sales', hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            template="plotly_white"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

with row2_col2:
    with st.container(border=True):
        st.subheader("🎯 Discount Rate vs. Profitability Scatter")
        fig_scatter = px.scatter(
            filtered_df, x='Discount', y='Profit', color='Category',
            size='Sales', hover_data=['Order_ID', 'Region'],
            color_discrete_sequence=px.colors.qualitative.Bold,
            template="plotly_white"
        )
        fig_scatter.add_hline(y=0, line_dash="dash", line_color="red")
        st.plotly_chart(fig_scatter, use_container_width=True)

# Data Table View Card
with st.container(border=True):
    st.subheader("📋 Filtered Transactions Table")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    # Download CSV Button
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_sales_data.csv",
        mime="text/csv"
    )
