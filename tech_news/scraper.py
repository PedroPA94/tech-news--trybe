import requests
import time
import re
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    timeout = 3

    try:
        content = requests.get(url, headers=headers, timeout=timeout)
        content.raise_for_status()
        time.sleep(1)
        return content.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css('.entry-title a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css('a.next::attr(href)').get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('.entry-title::text').get()
    timestamp = selector.css('.meta-date::text').get()
    writer = selector.css('.author > a::text').get()
    reading_time = selector.css('.meta-reading-time::text').get()
    reading_time = int(re.search(r'\d+', reading_time).group())
    summary = (
        selector
        .css('.entry-content > p:first-of-type')
        .xpath('string()')
        .get()
    )
    category = selector.css('.category-style .label::text').get()

    return {
        'url': url,
        'title': title.strip(),
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': reading_time,
        'summary': summary.strip(),
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
