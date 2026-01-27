"""
Analysing to find if a brand should even be using memes at all.

Problems:
1. Campaign_success_probability().
2. Final strategy recommendation per brand.
"""
import csv
from collections import defaultdict

FILENAME = "data/all_data_merged.csv"

def is_success(row, engagement_threshold=60):
    return (
        row["campaign_used"] == "1"
        and int(row["engagement_score"]) > engagement_threshold
        and row["sentiment"].lower() != "negative"
    )

def load_csv(filename):
    rows = []

    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

data = load_csv(FILENAME)

campaign_rows = [row for row in data if row["campaign_used"] == "1"]

total_campaigns = len(campaign_rows)

successful_campaigns = sum(1 for row in campaign_rows if is_success(row))

campaign_success_probability = (
    (successful_campaigns / total_campaigns) * 100
    if total_campaigns > 0 else 0
)

print(f"campaign success probability: {campaign_success_probability:2f}%")

"""
output:

campaign success probability: 17.525773%

insight:

the predicted probability of campaign success is 17.5%, indicating a high-risk, low-confidence meme strategy under current conditions.
"""

