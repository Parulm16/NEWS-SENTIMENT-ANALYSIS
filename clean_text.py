# pipeline/clean_text.py

import pandas as pd
import re

def clean_headline(text):
    # Lowercase, remove punctuation, numbers, URLs
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)               # remove URLs
    text = re.sub(r"[^a-z\s]", "", text)              # remove punctuation and numbers
    text = re.sub(r"\s+", " ", text).strip()          # remove extra spaces
    return text

def clean_news_file(input_csv="data/raw_news.csv", output_csv="data/clean_news.csv"):
    df = pd.read_csv(input_csv)
    df["clean_title"] = df["title"].apply(clean_headline)
    df["clean_description"] = df["description"].fillna("").apply(clean_headline)
    df.to_csv(output_csv, index=False)
    print(f"Cleaned news saved to {output_csv}")

if __name__ == "__main__":
    clean_news_file()
