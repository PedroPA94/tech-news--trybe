from tech_news.database import find_news
from collections import Counter


def sort_categories(item):
    return -item[1], item[0]


# Requisito 10
def top_5_categories():
    all_news = find_news()

    categories = [
        news['category']
        for news in all_news
    ]

    categories_counter = Counter(categories).most_common()

    return [
        category_count[0]
        for category_count in sorted(categories_counter, key=sort_categories)
    ][:5]
