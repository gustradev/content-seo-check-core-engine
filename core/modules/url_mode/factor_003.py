# core/modules/url_mode/factor_003.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    return {
        "factor": "H1 Tag Count",
        "value": len(soup.find_all("h1"))
    }
