from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {
        "title": {
            "$regex": title,
            "$options": "i"
        }
    }

    matches = search_news(query)

    return [
        (news["title"], news["url"])
        for news in matches
    ]


# Requisito 8
def search_by_date(date):
    try:
        date_ISO = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Data inválida")

    date_str = date_ISO.strftime('%d/%m/%Y')
    matches = search_news({"timestamp": {"$eq": date_str}})

    return [
        (news["title"], news["url"])
        for news in matches
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
