# run_pipeline.py

import subprocess
import time

def run_step(script):
    print(f"▶️ Running {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"⚠️ Error in {script}:\n", result.stderr)

def run_full_pipeline():
    steps = [
        "pipeline/fetch_news.py",
        "pipeline/clean_text.py",
        "model/sentiment_model.py",
        "pipeline/map_sectors.py",
        "pipeline/aggregate.py"
    ]
    for script in steps:
        run_step(script)

if __name__ == "__main__":
    while True:
        print("🔁 Running full sentiment pipeline...\n")
        run_full_pipeline()
        print("✅ Pipeline complete. Sleeping for 60 minutes...\n")
        time.sleep(1 )  # Sleep for 1 hour
