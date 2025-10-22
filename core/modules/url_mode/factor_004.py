# core/modules/url_mode/factor_004.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    return {
        "factor": "H2 Tag Count",
        "value": len(soup.find_all("h2"))
    }
