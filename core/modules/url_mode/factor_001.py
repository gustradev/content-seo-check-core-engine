# core/modules/url_mode/factor_001.py
from bs4 import BeautifulSoup

def check(html):
    if not html:
        return {"factor": "Title Tag Length", "value": 0}

    soup = BeautifulSoup(html, "html.parser")

    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()

    return {
        "factor": "Title Tag Length",
        "value": len(title)
    }
