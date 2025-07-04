# model/sentiment_model.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import os

# Load FinBERT model and tokenizer
MODEL_NAME = "yiyanghkust/finbert-tone"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

# Define sentiment labels
labels = ["negative", "neutral", "positive"]

def classify_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "neutral"
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    sentiment = labels[torch.argmax(probs)]
    return sentiment

def run_sentiment_on_file(input_csv="data/clean_news.csv", output_csv="data/sentiment_scores.csv"):
    df = pd.read_csv(input_csv)

    # Combine title and description if you want more context
    df["full_text"] = df["clean_title"] + ". " + df["clean_description"]

    print("Scoring headlines with FinBERT...")
    df["sentiment"] = df["full_text"].apply(classify_sentiment)

    df.to_csv(output_csv, index=False)
    print(f"✅ Sentiment scores saved to: {output_csv}")

if __name__ == "__main__":
    run_sentiment_on_file()
