"""
Analysing to find which brand tones work with which meme genres.

Problems:
1. Identify best-performing brand tone per meme genre.
2. Brand class + campaign_sucess_probability().
3. Cultural mismatch detection.
"""

import csv
from collections import defaultdict

# Identify best-performing brand tone per meme genre.
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

def group_by_column_csv(file_path, column_name):
    grouped_data = defaultdict(list)

    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            group_key = row[column_name]
            grouped_data[group_key].append(row)

    return grouped_data

group_by_column_csv('data/all_data_merged.csv', 'genre')
for genre, memes in group_by_column_csv('data/all_data_merged.csv', 'genre').items():
    tone_engagement = defaultdict(int)

    for meme in memes:
        tone = meme['tone']
        engagement = int(meme['engagement_score'])
        tone_engagement[tone] += engagement

    if tone_engagement:
        best_tone = max(tone_engagement.items(), key=lambda x: x[1])
        print(f'Best Brand Tone for Meme Genre "{genre}": {best_tone[0]} with Total Engagement: {best_tone[1]}')
    else:
        print(f'No data available for Meme Genre "{genre}"')

"""
output:

Best Brand Tone for Meme Genre "wholesome": minimal with Total Engagement: 609
Best Brand Tone for Meme Genre "political": chaotic with Total Engagement: 518
Best Brand Tone for Meme Genre "nostalgia": ironic with Total Engagement: 585
Best Brand Tone for Meme Genre "brand_parody": serious with Total Engagement: 606
Best Brand Tone for Meme Genre "shitpost": chaotic with Total Engagement: 710

Insight:

meme genres carry implicit emotional contracts. tones that violate these contracts dilute engagement, while aligned tones amplify it.
    - wholesome memes: perform best with minimal tone
    - political memes: reward chaotic tone
    - nostalgia memes: respond best to ironic tone
    - brand parody: surprisingly favors serious tone
    - shitposts: overwhelmingly favor chaotic tone
"""

# Brand class + campaign_sucess_probability().
group_by_column_csv('data/all_data_merged.csv', 'industry')
for industry, memes in group_by_column_csv('data/all_data_merged.csv', 'industry').items():
    total_memes = len(memes)
    successful_memes = sum(1 for meme in memes if meme['campaign_used'] == '1' and int(meme['engagement_score']) > 60)

    success_probability = (successful_memes / total_memes) * 100 if total_memes > 0 else 0
    print(f'Industry: {industry}, Campaign Success Probability: {success_probability:.2f}%')

"""
output:

Industry: fintech, Campaign Success Probability: 15.56%
Industry: fashion, Campaign Success Probability: 27.27%
Industry: tech, Campaign Success Probability: 21.21%
Industry: food, Campaign Success Probability: 16.67%
Industry: media, Campaign Success Probability: 5.88%

Insight:

industries closer to lifestyle and identity benefit more from meme-based communication. regulated or credibility-heavy sectors face structural resistance.
    - fashion (27%): highest meme leverage
    - tech (21%): moderate, execution-sensitive
    - fintech (15%): high risk, low tolerance
    - food (16%): inconsistent returns
    - media (6%): meme fatigue or audience saturation
"""

# Cultural mismatch detection.
SENTIMENT_SCORE = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

group_by_column_csv('data/all_data_merged.csv', 'platform')

for platform, memes in group_by_column_csv('data/all_data_merged.csv', 'platform').items():
    print(f"\nPlatform: {platform}")
    
    for meme in memes:
        engagement = int(meme['engagement_score'])
        followers = int(meme['followers'])
        sentiment = SENTIMENT_SCORE.get(meme['sentiment'].lower(), 0)
        campaign_used = meme['campaign_used'] == '1'

        mismatch_reasons = []

        # rule 1: large audience, weak response
        if followers > 10000 and engagement < 40:
            mismatch_reasons.append("high reach, low engagement")

        # rule 2: campaign spend but no payoff
        if campaign_used and engagement < 50:
            mismatch_reasons.append("campaign used but poor performance")

        # rule 3: attention without approval
        if engagement >= 60 and sentiment <= 0:
            mismatch_reasons.append("engagement without positive sentiment")

        if mismatch_reasons:
            print(f"""
CULTURAL MISMATCH DETECTED
meme: {meme['meme_name']}
brand: {meme['brand_name']}
genre: {meme['genre']}
tone: {meme['tone']}
engagement_score: {engagement}
sentiment: {meme['sentiment']}
reasons: {', '.join(mismatch_reasons)}
""")

"""
output: (1 each platform displayed)

Platform: twitter

CULTURAL MISMATCH DETECTED
meme: meme_176
brand: brand_25
genre: brand_parody
tone: serious
engagement_score: 6
sentiment: positive
reasons: high reach, low engagement, campaign used but poor performance

Platform: reddit

CULTURAL MISMATCH DETECTED
meme: meme_279
brand: brand_10
genre: wholesome
tone: minimal
engagement_score: 49
sentiment: negative
reasons: campaign used but poor performance

Platform: instagram

CULTURAL MISMATCH DETECTED
meme: meme_162
brand: brand_9
genre: wholesome
tone: serious
engagement_score: 27
sentiment: negative
reasons: high reach, low engagement

Platform: tiktok

CULTURAL MISMATCH DETECTED
meme: meme_229
brand: brand_6
genre: nostalgia
tone: chaotic
engagement_score: 34
sentiment: positive
reasons: high reach, low engagement

Insight:

high visibility does not guarantee cultural acceptance. several campaigns achieved reach but triggered disengagement or negative sentiment.
"""

"""
HOW COULD BRANDS USE THIS?

- brands should pre-filter meme genres based on tone before campaign ideation
- tone-genre mismatch is a predictable failure, not bad luck
- meme marketing should be industry-gated
- memes favor lifestyle and identity brands more.
- fintech/media brands need stricter go/no-go thresholds before running meme campaigns
- introduce a cultural mismatch checkpoint before campaigns
- flag campaigns for review when:
    - followers increase but engagement decreases
    - sentiment ≤ 0 despite engagement
    - paid campaigns underperform organic benchmarks
"""