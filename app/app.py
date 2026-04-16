import sys
import os

# Fix import issue (VERY IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.anomaly import detect_anomaly
from src.forecast import forecast_temperature

# Page config
st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

# Title
st.title("Climate Trend Analyzer Dashboard")

# Load Data
df = load_data("data/raw/climate_data.csv")
df = preprocess(df)
df = detect_anomaly(df)

# Sidebar
st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())

# Filter data
df = df[(df['Date'] >= pd.to_datetime(start_date)) &
        (df['Date'] <= pd.to_datetime(end_date))]

# Top Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Average Temperature", round(df['Temperature'].mean(), 2))
col2.metric("Total Rainfall", round(df['Rainfall'].sum(), 2))
col3.metric("Anomalies", int(df['Anomaly'].sum()))

# Temperature Graph
st.subheader("Temperature Trend")
fig1 = px.line(df, x='Date', y='Temperature', title="Temperature Over Time")
st.plotly_chart(fig1, use_container_width=True)

# Rainfall Graph
st.subheader("Rainfall Trend")
fig2 = px.line(df, x='Date', y='Rainfall', title="Rainfall Over Time")
st.plotly_chart(fig2, use_container_width=True)

# Anomaly Graph
st.subheader("Anomaly Detection")

fig3 = px.scatter(
    df,
    x='Date',
    y='Temperature',
    color='Anomaly',
    title="Temperature Anomalies",
    color_discrete_map={True: 'red', False: 'blue'}
)

st.plotly_chart(fig3, use_container_width=True)

# Forecast Section
st.subheader("Forecast")

if st.button("Generate Forecast"):
    predictions = forecast_temperature(df)
    st.success("Forecast Generated")
    st.write(predictions)

# Show Data (Optional)
if st.checkbox("Show Raw Data"):
    st.subheader("Dataset")
    st.write(df.head())