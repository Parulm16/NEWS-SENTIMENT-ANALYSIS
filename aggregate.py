# pipeline/aggregate.py

import pandas as pd
from datetime import datetime

# Map sentiment label to score
SENTIMENT_SCORE_MAP = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

def aggregate_sentiment(input_csv="data/sector_sentiment.csv", output_csv="data/aggregated_sentiment.csv"):
    df = pd.read_csv(input_csv)

    # Convert timestamp to datetime
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])

    # Optional: create time windows (e.g., hourly or daily)
    df["time_bucket"] = df["publishedAt"].dt.floor("1H")  # hourly grouping

    # Convert sentiment to numeric
    df["sentiment_score"] = df["sentiment"].map(SENTIMENT_SCORE_MAP)

    # Split multi-sector rows (optional but recommended)
    df = df.assign(sector=df["sector"].str.split(", "))
    df = df.explode("sector")

    # Group by sector + time
    agg = df.groupby(["sector", "time_bucket"]).agg(
        headline_count=("sentiment_score", "count"),
        avg_sentiment=("sentiment_score", "mean"),
        pos_count=("sentiment", lambda x: (x == "positive").sum()),
        neg_count=("sentiment", lambda x: (x == "negative").sum())
    ).reset_index()

    agg.to_csv(output_csv, index=False)
    # Fix time bucket
    df["time_bucket"] = df["publishedAt"].dt.floor("1h")
    
    # Fix print message
    print(f"[INFO] Aggregated sentiment saved to: {output_csv}")

if __name__ == "__main__":
    aggregate_sentiment()
