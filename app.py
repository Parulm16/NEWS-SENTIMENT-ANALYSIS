# dashboard/app.py

import pandas as pd
import streamlit as st
import altair as alt
import os

# Load data
@st.cache_data
def load_data():
    file_path = "data/aggregated_sentiment.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path, parse_dates=["time_bucket"])
    else:
        return pd.DataFrame()

df = load_data()

st.title("🧠 Indian Market News Sentiment Dashboard")
st.markdown("Live sentiment classification using FinBERT on NewsAPI headlines.")

# Sidebar filters
with st.sidebar:
    sectors = df["sector"].unique().tolist()
    selected_sectors = st.multiselect("Select Sectors", sectors, default=sectors)

    time_range = st.slider(
        "Select Time Range (in hours)",
        min_value=1,
        max_value=24,
        value=6,
        step=1
    )

# Filter data
if not df.empty:
    latest_time = df["time_bucket"].max()
    start_time = latest_time - pd.Timedelta(hours=time_range)

    filtered_df = df[
        (df["sector"].isin(selected_sectors)) &
        (df["time_bucket"] >= start_time)
    ]

    st.markdown(f"### Sentiment from {start_time.strftime('%H:%M')} to {latest_time.strftime('%H:%M')}")

    # Chart: Average Sentiment per Sector
    bar_chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X("sector:N", sort="-y"),
        y="avg_sentiment:Q",
        color=alt.condition(
            alt.datum.avg_sentiment > 0,
            alt.value("green"),
            alt.value("red")
        ),
        tooltip=["sector", "avg_sentiment", "headline_count"]
    ).properties(height=400, title="Sector-wise Average Sentiment")

    st.altair_chart(bar_chart, use_container_width=True)

    # Chart: Sentiment Over Time (Line Chart)
    st.markdown("### Sentiment Trend Over Time")
    line_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
        x="time_bucket:T",
        y="avg_sentiment:Q",
        color="sector:N",
        tooltip=["sector", "time_bucket", "avg_sentiment"]
    ).properties(height=400)

    st.altair_chart(line_chart, use_container_width=True)

else:
    st.warning("No data available. Please run the pipeline to generate `aggregated_sentiment.csv`.")

