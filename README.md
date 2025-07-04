# 🧠 Real-Time News Sentiment Dashboard for Indian Markets

This project analyzes real-time financial news headlines from Indian sources using **FinBERT**, a finance-specific transformer model, and maps them to sectors such as Finance, IT, Pharma, Auto, and more. It provides an interactive **Streamlit dashboard** to visualize sector-wise sentiment trends — ideal for quantitative research, trading signals, or market monitoring.

---

## 🚀 Features

- 🔄 Fetches real-time Indian financial news via **NewsAPI**
- ✨ Cleans, filters, and deduplicates raw headlines and descriptions
- 🤖 Classifies sentiment (`positive`, `neutral`, `negative`) using **FinBERT**
- 🏷️ Tags each headline with its relevant sector using keyword-based rules
- 📊 Aggregates sentiment over hourly time buckets and computes trend metrics
- 📈 Visualizes everything with a fully interactive **Streamlit dashboard**
- 🧠 Built for **analysts, quants, and data scientists** to demonstrate real-time NLP + dashboard skills

---

## 🧠 Tech Stack

| Component       | Technology       |
|----------------|------------------|
| News Fetching   | `NewsAPI`        |
| NLP Model       | `FinBERT` via HuggingFace Transformers |
| Dashboard       | `Streamlit` + `Altair` |
| Data Processing | `pandas`, `regex`, `datetime` |
| Scheduler       | Python loop or OS-based cron/task scheduler |

---

## 🗂️ Project Structure
news-sentiment-india/
├── pipeline/
│ ├── fetch_news.py # Collects raw headlines from NewsAPI
│ ├── clean_text.py # Text preprocessing and deduplication
│ ├── map_sectors.py # Maps headlines to sectors
│ ├── aggregate.py # Aggregates sector-wise sentiment
├── model/
│ └── sentiment_model.py # FinBERT classification
├── dashboard/
│ └── app.py # Streamlit dashboard code
├── utils/
│ └── config.py # API keys and keyword maps
├── run_pipeline.py # End-to-end pipeline automation script
├── requirements.txt # Python libraries needed
└── README.md
