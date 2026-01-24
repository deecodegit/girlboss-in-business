"""
Analysing to find which meme genres actually drive engagement (likes, shares, sentiment).

Problems:
1. Calculate average likes per meme genre.
2. Use weighted score to rank memes.
3. simulate sentiment shifts wehn campaign_used = 1.
"""

import csv
from collections import defaultdict

filename = 'C:\\Users\\Devanshi Sahu\\girlboss in business\\data studies\\python\\cultural analysis of meme-literate brands\\data\\memes.csv'

# 1. Calculating average likes per meme genre.
def group_csv_by_column(filename, group_by_column_name):
    grouped_data = defaultdict(list)

    with open(filename, mode = 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            group_key = row[group_by_column_name]
            grouped_data[group_key].append(row)

    return dict(grouped_data)

genres = group_csv_by_column(filename, 'genre')

for genre, likes in genres.items():
    total_likes = sum(int(like['likes']) for like in likes)
    average_likes = total_likes / len(likes) if likes else 0
    print(f"Genre: {genre}, Average Likes: {average_likes:.2f}")

"""
output:

Genre: political, Average Likes: 23217.23
Genre: shitpost, Average Likes: 25398.81
Genre: wholesome, Average Likes: 23963.31
Genre: brand_parody, Average Likes: 24655.46
Genre: nostalgia, Average Likes: 23088.03

insight:

since shitpost and brand_parody genres show the highest average likes, irreverent, self-aware humor outperforms informational or nostalgic content in raw engagement.
"""

# Using weighted score to rank memes.
memes = group_csv_by_column(filename, 'meme_name')

weighted_scores = []

for meme_name, meme_rows in memes.items():
    for meme in meme_rows:
        likes = int(meme['likes'])
        shares = int(meme['shares'])

        weighted_score = (0.75 * likes) + (0.25 * shares)

        weighted_scores.append((meme_name, weighted_score))

weighted_scores.sort(key=lambda x: x[1], reverse=True)

print("ranking by weighted scores:")
for meme_name, score in weighted_scores:
    print(meme_name, score)

"""
output: (top 5 only)

ranking by weighted scores:
meme_289 41343.25
meme_57 40644.25
meme_111 40480.5
meme_128 40455.5
meme_142 40381.5

insight:

top memes are driven primarily by likes, not shares.
high likes + moderate shares is not cultural currency.
brands want shares, not just likes.
"""

# Simulating sentiment shifts when campaign_used = 1.

file_name = 'C:\\Users\\Devanshi Sahu\\girlboss in business\\data studies\\python\\cultural analysis of meme-literate brands\\data\\engagement.csv'

engagements = group_csv_by_column(file_name, 'campaign_used')

sentiment_map = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

for campaign_used, engagement_rows in engagements.items():
    total_sentiment = sum(sentiment_map[engagement['sentiment'].lower()] for engagement in engagement_rows)
    average_sentiment = total_sentiment / len(engagement_rows) if engagement_rows else 0
    print(f"Campaign Used: {campaign_used}, Average Sentiment Score: {average_sentiment:.4f}")  

"""
output:

Campaign Used: 0, Average Sentiment Score: 0.0194
Campaign Used: 1, Average Sentiment Score: -0.0966

insight:

when brands explicitly attach themselves to memes, average sentiment shifts negative.
"""