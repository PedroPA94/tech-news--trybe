import requests
import time


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
