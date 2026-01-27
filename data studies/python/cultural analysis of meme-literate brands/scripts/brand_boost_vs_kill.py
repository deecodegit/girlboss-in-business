"""
Analysing to find when brand campaigns boost engagement vs. kill authenticity.

Problems:
1. Join meme + brand + engagement tables.
2. Compare sentiment with campaign_used = 0 vs 1
3. aesthetic dissonance index.
"""

import csv
from collections import defaultdict

# Join meme + brand + engagement tables.
def join_csv_files(file1_path, file2_path, common_column_name, output_path):
    data_file1 = {}
    header_file1 = []

    with open(file1_path, mode='r', encoding='utf-8') as f1:
        reader = csv.DictReader(f1)
        header_file1 = reader.fieldnames
        for row in reader:
            key = row[common_column_name]
            data_file1[key] = row

    joined_data = []
    header_file2 = []

    with open(file2_path, mode='r', encoding='utf-8') as f2:
        reader = csv.DictReader(f2)
        header_file2 = reader.fieldnames
        
        output_header = header_file1 + [col for col in header_file2 if col != common_column_name]

        for row2 in reader:
            key = row2[common_column_name]

            if key in data_file1:
                row1 = data_file1[key]

                combined_row = row1.copy()
                for col, value in row2.items():
                    if col != common_column_name:
                        combined_row[col] = value
                joined_data.append(combined_row)

    with open(output_path, mode='w', encoding='utf-8', newline='') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=output_header)
        writer.writeheader()
        for row in joined_data:
            writer.writerow(row)

join_csv_files('data/meme_engagement_joined.csv', 'data/brands.csv', 'brand_id', 'data/all_data_merged.csv')

# Compare sentiment with campaign_used = 0 vs 1
sentiment_map = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

filename = 'data/all_data_merged.csv'

def group_csv_by_column(filename, group_by_column_name):
    grouped_data = defaultdict(list)

    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            group_key = row[group_by_column_name]
            grouped_data[group_key].append(row)
    
    return dict(grouped_data)

engagements = group_csv_by_column(filename, 'campaign_used')

for campaign_used, engagement_rows in engagements.items():
    total_sentiment = sum(sentiment_map[engagement['sentiment'].lower()] for engagement in engagement_rows)
    print(f"Campaign Used: {campaign_used}, Total Sentiment Score: {total_sentiment:.4f}")

"""
output:

Campaign Used: 0, Total Sentiment Score: 4.0000
Campaign Used: 1, Total Sentiment Score: -20.0000

insight:

Campaigns tend to drive negative sentiment overall.
"""

# Aesthetic dissonance index.
rows = []

with open(filename, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['engagement_score'] = int(row['engagement_score'])
        row['sentiment_score'] = sentiment_map.get(row['sentiment'].lower(), 0)
        rows.append(row)

# step 1: compute expected performance per (genre, tone)
baseline = defaultdict(list)

for row in rows:
    key = (row['genre'], row['tone'])
    combined_score = row['engagement_score'] + row['sentiment_score']
    baseline[key].append(combined_score)

expected_performance = {
    key: sum(values) / len(values)
    for key, values in baseline.items()
}

# step 2: calculate ADI per meme
adi_results = []

for row in rows:
    key = (row['genre'], row['tone'])
    expected = expected_performance.get(key, 0)

    actual = row['engagement_score'] + row['sentiment_score']
    adi = expected - actual

    adi_results.append({
        'meme_id': row['meme_id'],
        'meme_name': row['meme_name'],
        'brand_name': row['brand_name'],
        'genre': row['genre'],
        'tone': row['tone'],
        'campaign_used': row['campaign_used'],
        'adi': round(adi, 3)
    })

# step 3: sort by highest dissonance
adi_results.sort(key=lambda x: x['adi'], reverse=True)

print("\nHighest Aesthetic Dissonance Cases:\n")

for r in adi_results[:10]:
    print(
        f"Brand: {r['brand_name']} | Meme: {r['meme_name']} | "
        f"Genre: {r['genre']} | Tone: {r['tone']} | "
        f"Campaign Used: {r['campaign_used']} | ADI: {r['adi']}"
    )

"""
output:

Highest Aesthetic Dissonance Cases:

Brand: brand_172 | Meme: meme_5 | Genre: wholesome | Tone: minimal | Campaign Used: 1 | ADI: 60.5
Brand: brand_262 | Meme: meme_282 | Genre: political | Tone: ironic | Campaign Used: 0 | ADI: 59.5
Brand: brand_65 | Meme: meme_99 | Genre: brand_parody | Tone: chaotic | Campaign Used: 0 | ADI: 48.9
Brand: brand_25 | Meme: meme_176 | Genre: brand_parody | Tone: serious | Campaign Used: 1 | ADI: 48.273
Brand: brand_184 | Meme: meme_28 | Genre: political | Tone: minimal | Campaign Used: 0 | ADI: 48.0
Brand: brand_113 | Meme: meme_120 | Genre: nostalgia | Tone: chaotic | Campaign Used: 1 | ADI: 46.3
Brand: brand_193 | Meme: meme_280 | Genre: wholesome | Tone: ironic | Campaign Used: 0 | ADI: 46.125
Brand: brand_92 | Meme: meme_77 | Genre: wholesome | Tone: chaotic | Campaign Used: 1 | ADI: 46.091
Brand: brand_86 | Meme: meme_251 | Genre: brand_parody | Tone: chaotic | Campaign Used: 0 | ADI: 44.9
Brand: brand_232 | Meme: meme_84 | Genre: brand_parody | Tone: serious | Campaign Used: 1 | ADI: 44.273

insight:

High ADI cases often involve brand campaigns (campaign_used = 1) that clash with the meme's genre and tone, leading to poor audience reception.
Brands should align meme content with their authentic voice to minimize aesthetic dissonance.
"""

"""
HOW COULD BRANDS USE THIS?
brands should only deploy meme campaigns when tone-genre alignment keeps ADI below a defined risk threshold.
Otherwise, organic participation or silence outperforms forced visibility.
"""