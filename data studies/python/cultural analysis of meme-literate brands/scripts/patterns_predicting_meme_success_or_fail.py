"""
Analysing to find what patternspredict a meme campaign's success or failure.

Problems:
1. Lambda-based weighted ranking.
2. Simulate 10 meme campaigns
3. Pattern extraction across failure/success.
"""

import csv
from collections import defaultdict

# lambda-based weighted ranking 
input_file = 'data/all_data_merged.csv'
output_file = 'data/all_data_with_reach.csv'

col_1 = "likes"
col_2 = "shares"
new_col = "reach"

rows = []

with open (input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + [new_col]
    
    for row in reader:
        try:
            value_1 = int(row[col_1])
            value_2 = int(row[col_2])
            row[new_col] = value_1 + value_2
        except (ValueError, KeyError):
            row[new_col] = 0

        rows.append(row)

with open (output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

filename = 'data/all_data_with_reach.csv'

with open(filename, 'r', newline = '', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

    rankings = defaultdict(float)
    for row in data:
        weight = float(row['engagement_score']) * 0.7 + float(row['reach']) * 0.3
        rankings[row['meme_id']] += weight
        sorted_rankings = sorted(rankings.items(), key=lambda x: x[1], reverse=True)
    print("Top 10 meme campaigns by weighted ranking:")
    for i, (meme_id, score) in enumerate(sorted_rankings[:10], 1):
        print(f"{i}. Meme ID: {meme_id}, Score: {score}")


"""
output:

Top 10 meme campaigns by weighted ranking:
1. Meme ID: 142, Score: 58829.9
2. Meme ID: 97, Score: 35494.1
3. Meme ID: 242, Score: 34226.100000000006
4. Meme ID: 141, Score: 34142.5
5. Meme ID: 29, Score: 33731.0
6. Meme ID: 16, Score: 33639.399999999994
7. Meme ID: 291, Score: 32409.899999999994
8. Meme ID: 229, Score: 31620.0
9. Meme ID: 208, Score: 31458.1
10. Meme ID: 280, Score: 31238.1
"""

# simulate 10 meme campaigns
import random

campaigns = []

for i in range(1, 11):
    platform = random.choice(['Reddit', 'Instagram', 'Twitter', 'TikTok'])

    if platform == 'Reddit':
        likes = random.randint(1000, 5000)
        shares = random.randint(500, 2000)
    elif platform == 'Instagram':
        likes = random.randint(2000, 8000)
        shares = random.randint(1000, 3000)
    elif platform == 'Twitter':
        likes = random.randint(1500, 6000)
        shares = random.randint(800, 2500)
    else: 
        likes = random.randint(3000, 10000)
        shares = random.randint(1500, 4000)

    comments = int(likes * random.uniform(0.02, 0.08))

    virality_score = round(
        (shares * 0.5) + (comments * 0.3) + (likes * 0.2), 2
    )

    campaigns.append({
        "campaign_id": i,
        "platform": platform,
        "likes": likes,
        "shares": shares,
        "comments": comments,
        "virality_score": virality_score
    })

    with open("meme_campaigns.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "campaign_id",
                "platform",
                "likes",
                "shares",
                "comments",
                "virality_score"
            ]
        )

        writer.writeheader()
        writer.writerows(campaigns)

# pattern extraction across failure/success
FILENAME = "data/all_data_merged.csv"

def is_success(row):
    return (
        row["campaign_used"] == "1"
        and int(row["engagement_score"]) >= 60
        and row["sentiment"].lower() != "negative"
    )

def load_csv(file_name):
    data = []
    with open(file_name, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

data = load_csv(FILENAME)

success_rows = []
failure_rows = []

for row in data:
    if is_success(row):
        success_rows.append(row)
    else:
        failure_rows.append(row)

def count_by_field(rows,field):
        counts = {}
        for row in rows:
            value = row[field]
            counts[value] = counts.get(value, 0) + 1
        return counts

def average(rows, field):
    if not rows:
        return 0
    total = sum(int(row[field]) for row in rows)
    return total / len(rows)

def extract_patterns(success_rows, failure_rows, field):
    success_counts = count_by_field(success_rows, field)
    failure_counts = count_by_field(failure_rows, field)

    patterns = {}
    all_values = set(success_counts) | set(failure_counts)

    for value in all_values:
        s = success_counts.get(value, 0)
        f = failure_counts.get(value, 0)
        patterns[value] = s - f  # dominance score

    return patterns

def extract_combo_patterns(success_rows, failure_rows, field1, field2):
    def combo_counter(rows):
        combos = {}
        for row in rows:
            key = (row[field1], row[field2])
            combos[key] = combos.get(key, 0) + 1
        return combos

    success_combos = combo_counter(success_rows)
    failure_combos = combo_counter(failure_rows)

    patterns = {}
    all_combos = set(success_combos) | set(failure_combos)

    for combo in all_combos:
        s = success_combos.get(combo, 0)
        f = failure_combos.get(combo, 0)
        patterns[combo] = s - f

    return patterns

tone_patterns = extract_patterns(success_rows, failure_rows, "tone")
genre_patterns = extract_patterns(success_rows, failure_rows, "genre")
platform_patterns = extract_patterns(success_rows, failure_rows, "platform")

tone_genre_patterns = extract_combo_patterns(
    success_rows, failure_rows, "tone", "genre"
)

avg_success_engagement = average(success_rows, "engagement_score")
avg_failure_engagement = average(failure_rows, "engagement_score")

print("\n=== average engagement ===")
print("success:", round(avg_success_engagement, 2))
print("failure:", round(avg_failure_engagement, 2))

print("\n=== tone dominance ===")
for tone, score in sorted(tone_patterns.items(), key=lambda x: x[1], reverse=True):
    print(tone, "has", score)

print("\n=== genre dominance ===")
for genre, score in sorted(genre_patterns.items(), key=lambda x: x[1], reverse=True):
    print(genre, "has", score)

print("\n=== tone + genre patterns ===")
for combo, score in sorted(tone_genre_patterns.items(), key=lambda x: x[1], reverse=True):
    print(combo, "has", score)

"""
output:

=== average engagement ===
success: 78.53
failure: 46.29

=== tone dominance ===
ironic has -29
serious has -35
minimal has -37
chaotic has -48

=== genre dominance ===
political has -26
brand_parody has -27
nostalgia has -30
shitpost has -30
wholesome has -36

=== tone + genre patterns ===
('serious', 'political') has -1
('ironic', 'nostalgia') has -3
('serious', 'shitpost') has -3
('minimal', 'brand_parody') has -4
('ironic', 'wholesome') has -6
('ironic', 'political') has -6
('ironic', 'brand_parody') has -6
('minimal', 'political') has -7
('chaotic', 'brand_parody') has -8
('minimal', 'shitpost') has -8
('chaotic', 'nostalgia') has -8
('minimal', 'wholesome') has -8
('ironic', 'shitpost') has -8
('serious', 'nostalgia') has -9
('serious', 'brand_parody') has -9
('chaotic', 'wholesome') has -9
('minimal', 'nostalgia') has -10
('chaotic', 'shitpost') has -11
('chaotic', 'political') has -12
('serious', 'wholesome') has -13

insight:

- campaigns need significantly higher engagement to avoid negative sentiment fallout.
- chaotic branding performs worst when formalized into campaigns.
- irony survives institutionalization better than chaos.
- “wholesome” memes collapse fastest under brand intervention. authenticity erosion is strongest there.
-brands fail hardest when:
    - they inject chaos into serious discourse
    - or sanitize inherently organic meme genres
- platforms don’t just distribute memes - they reshape risk profiles.
"""

"""
HOW COULD BRANDS USE IT?

1. successful meme campaigns share three traits:
    - restrained brand tone (ironic > loud)
    - genre compatibility (parody > wholesome)
    - high engagement intensity (no soft wins)

2. failed campaigns cluster around:
    - tone-genre dissonance
    - low engagement with high visibility
    - brands “trying too hard to belong”
"""