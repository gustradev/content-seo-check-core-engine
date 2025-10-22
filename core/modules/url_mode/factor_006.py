# core/modules/url_mode/factor_006.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", href=True)
    return {
        "factor": "Total Link Count",
        "value": len(links)
    }
