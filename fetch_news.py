# pipeline/fetch_news.py

import sys
import os
import requests                     
import pandas as pd                
from datetime import datetime 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.config import NEWSAPI_KEY


def fetch_headlines():
    url = (
        "https://newsapi.org/v2/everything?"
        "q=india stock market OR sensex OR nifty OR sebi OR fii OR rbi OR economy&"
        "language=en&sortBy=publishedAt&"
        f"apiKey={NEWSAPI_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    records = []
    for item in articles:
        records.append({
            "publishedAt": item["publishedAt"],
            "title": item["title"],
            "description": item.get("description", ""),
            "source": item["source"]["name"],
            "url": item["url"]
        })

    df = pd.DataFrame(records)
    df["fetched_at"] = datetime.utcnow().isoformat()

    df.to_csv("data/raw_news.csv", index=False)
    print(f"Fetched {len(df)} headlines at {df['fetched_at'].iloc[0]}")

if __name__ == "__main__":
    fetch_headlines()
