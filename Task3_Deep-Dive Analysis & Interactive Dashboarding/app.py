import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("📊 Sales Performance & Customer Insights Dashboard")

df = pd.read_excel("Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx")

# KPIs
revenue = df["Total_Sales"].sum()
orders = df["Order_ID"].nunique()
customers = df["Customer_ID"].nunique()
quantity = df["Quantity"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Revenue", f"₹{revenue:,.0f}")
c2.metric("Orders", orders)
c3.metric("Customers", customers)
c4.metric("Quantity Sold", quantity)

st.divider()

# Category Analysis
category = df.groupby("Category")["Total_Sales"].sum().reset_index()

fig1 = px.pie(
    category,
    names="Category",
    values="Total_Sales",
    title="Category Contribution"
)

st.plotly_chart(fig1, use_container_width=True)

# Product Analysis
product = df.groupby("Product")["Total_Sales"].sum().reset_index()

product = product.sort_values(
    by="Total_Sales",
    ascending=False
).head(10)

fig2 = px.bar(
    product,
    x="Product",
    y="Total_Sales",
    title="Top Products"
)

st.plotly_chart(fig2, use_container_width=True)

# City Analysis
city = df.groupby("City")["Total_Sales"].sum().reset_index()

fig3 = px.bar(
    city,
    x="City",
    y="Total_Sales",
    title="City Wise Revenue"
)

st.plotly_chart(fig3, use_container_width=True)

# Customer Segmentation
customer = df.groupby(
    ["Customer_ID","Customer_Name"]
)["Total_Sales"].sum().reset_index()

def segment(x):
    if x > 150000:
        return "High Value"
    elif x > 75000:
        return "Medium Value"
    return "Low Value"

customer["Segment"] = customer["Total_Sales"].apply(segment)

fig4 = px.pie(
    customer,
    names="Segment",
    title="Customer Segmentation"
)

st.plotly_chart(fig4, use_container_width=True)
