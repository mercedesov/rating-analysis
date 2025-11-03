
from collections import defaultdict

def average_rating_report(data):
    brand_ratings = defaultdict(list)
    for row in data:
        brand_ratings[row['brand']].append(float(row['rating']))

    averages = []
    for brand, ratings in brand_ratings.items():
        avg = sum(ratings) / len(ratings)
        averages.append((brand, round(avg, 2)))

    averages.sort(key=lambda x: x[1], reverse=True)
    return averages
