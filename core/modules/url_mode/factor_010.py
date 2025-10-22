# core/modules/url_mode/factor_010.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    canonical = soup.find("link", rel="canonical")
    return {
        "factor": "Canonical Tag Present",
        "value": 1 if canonical else 0
    }
