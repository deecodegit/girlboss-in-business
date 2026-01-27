"""
Analysing to find how platform context changes meme performance.

Problems:
1. Count memes per platform.
2. Top 5 brands per platform.
3. Average engagement score per platform.
"""

import csv
from collections import defaultdict

# Count memes per platform.
filename = "data/memes.csv"

def group_by_column_csv(filename, group_by_column_name):
    grouped_data = defaultdict(list)

    with open(filename, mode = 'r', newline = '', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            group_key = row[group_by_column_name]
            grouped_data[group_key].append(row)

    return grouped_data

platforms = group_by_column_csv(filename, 'platform')

for platform, memes in platforms.items():
    meme_count = len(memes)
    print(f'Platform: {platform}, Meme Count: {meme_count}')

"""
Output:

Platform: instagram, Meme Count: 82
Platform: twitter, Meme Count: 71
Platform: tiktok, Meme Count: 76
Platform: reddit, Meme Count: 71

Insight:

instagram appears to be the primary meme distribution hub, likely due to:
    - visual-first design
    - algorithmic amplification
    - ease of resharing
"""

# Top 5 brands per platform.
def join_csv_files(file_path1, file_path2, common_column_name, output_path):
    data_file1 = {}
    header_file1 = []

    with open(file_path1, mode='r', newline='', encoding='utf-8') as f1:
        reader = csv.DictReader(f1)
        header_file1 = reader.fieldnames
        for row in reader:
            key = row[common_column_name]
            data_file1[key] = row

    joined_data = []
    header_file2 = []

    with open(file_path2, mode='r', newline='', encoding='utf-8') as f2:
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

    with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=output_header)
        writer.writeheader()
        for row in joined_data:
            writer.writerow(row)

join_csv_files('data/memes.csv', 'data/engagement.csv', 'meme_id', 'data/meme_engagement_joined.csv')

platform_for_brands = group_by_column_csv('data/meme_engagement_joined.csv', 'platform')

for platform, memes in platform_for_brands.items():
    brand_engagement = defaultdict(int)

    for meme in memes:
        brand = meme['brand_id']
        engagement = int(meme['engagement_score'])
        brand_engagement[brand] += engagement

    sorted_brands = sorted(brand_engagement.items(), key=lambda x: x[1], reverse=True)
    top_5_brands = sorted_brands[:5]

    print(f'Top 5 Brands on {platform}:')
    for brand, total_engagement in top_5_brands:
        print(f'Brand: {brand}, Total Engagement: {total_engagement}')
    print()

"""
Output:

Top 5 Brands on twitter:
Brand: 180, Total Engagement: 162
Brand: 32, Total Engagement: 150
Brand: 280, Total Engagement: 126
Brand: 152, Total Engagement: 115
Brand: 275, Total Engagement: 111

Top 5 Brands on instagram:
Brand: 235, Total Engagement: 178
Brand: 94, Total Engagement: 136
Brand: 103, Total Engagement: 127
Brand: 203, Total Engagement: 124
Brand: 89, Total Engagement: 98

Top 5 Brands on tiktok:
Brand: 15, Total Engagement: 145
Brand: 192, Total Engagement: 142
Brand: 44, Total Engagement: 125
Brand: 45, Total Engagement: 113
Brand: 134, Total Engagement: 107

Top 5 Brands on reddit:
Brand: 289, Total Engagement: 185
Brand: 72, Total Engagement: 168
Brand: 199, Total Engagement: 127
Brand: 40, Total Engagement: 113
Brand: 279, Total Engagement: 110

Insight:

brand–platform fit matters more than brand size alone.
this suggests:
    - content strategy must be platform-native
    - cross-posting memes blindly is inefficient
"""

# Average engagement score per platform.

platform_for_engagement = group_by_column_csv('data/meme_engagement_joined.csv', 'platform')

for platform, memes in platform_for_engagement.items():
    total_engagement = 0
    meme_count = len(memes)

    for meme in memes:
        engagement = int(meme['engagement_score'])
        total_engagement += engagement

    average_engagement = total_engagement / meme_count if meme_count > 0 else 0
    print(f'Platform: {platform}, Average Engagement Score: {average_engagement:.2f}')

"""
Output:

Platform: twitter, Average Engagement Score: 52.52
Platform: instagram, Average Engagement Score: 46.18
Platform: tiktok, Average Engagement Score: 55.16
Platform: reddit, Average Engagement Score: 47.76

Insight:

1. tiktok is a high-engagement, low-volume environment:
    - fewer memes
    - stronger per-meme interaction

2. instagram is a high-volume, diluted engagement platform:
    - many memes
    - lower average engagement per meme

this indicates different roles:
    - tiktok for breakout potential 
    - instagram for reach and visibility
    - twitter/reddit for discourse-driven engagement
"""

"""
HOW COULD BRANDS USE THIS?

- high volume platforms is not equal to high engagement platforms
- brands must optimize differently per platform:
    - visibility on instagram
    - interaction on tiktok
    - conversation on twitter/reddit
"""