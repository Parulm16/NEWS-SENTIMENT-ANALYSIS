# pipeline/map_sectors.py

import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.config import SECTOR_KEYWORDS

def map_to_sectors(text):
    text = str(text).lower()
    matched_sectors = []
    for sector, keywords in SECTOR_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            matched_sectors.append(sector)
    return ", ".join(matched_sectors) if matched_sectors else "Uncategorized"

def run_sector_mapping(input_csv="data/sentiment_scores.csv", output_csv="data/sector_sentiment.csv"):
    df = pd.read_csv(input_csv)
    df["sector"] = df["clean_title"].apply(map_to_sectors)
    df.to_csv(output_csv, index=False)
    print(f"✅ Sector sentiment saved to: {output_csv}")

if __name__ == "__main__":
    run_sector_mapping()
