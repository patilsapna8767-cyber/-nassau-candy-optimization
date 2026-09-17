import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Nassau Candy Distributor", layout="wide")

st.title("🍬 Nassau Candy - Supply Chain Optimization")

# Try to load data, if not found ask user to upload
try:
    df = pd.read_csv("Nassau Candy Distributor - Historical Data (MASTER).csv")
except:
    st.warning("Please upload the Nassau Candy CSV file first, or add it to GitHub")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()

st.subheader("Dataset Overview")
st.dataframe(df.head())

# Simple Analytics
st.subheader("📊 Sales Analysis")
if 'Division' in df.columns and 'Gross Sales' in df.columns:
    fig = px.bar(df.groupby('Division')['Gross Sales'].sum().reset_index(), x='Division', y='Gross Sales')
    st.plotly_chart(fig, use_container_width=True)

if 'Channel' in df.columns:
    fig2 = px.pie(df, names='Channel', values='Gross Sales' if 'Gross Sales' in df.columns else None)
    st.plotly_chart(fig2, use_container_width=True)

st.success("App is working! This will be your Live Link.")
