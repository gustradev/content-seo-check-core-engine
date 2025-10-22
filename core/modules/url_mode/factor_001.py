# core/modules/url_mode/factor_001.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    return {
        "factor": "Title Tag Length",
        "value": len(title)
    }
