# core/modules/url_mode/factor_005.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    return {
        "factor": "Image Count",
        "value": len(soup.find_all("img"))
    }
