# core/modules/url_mode/factor_009.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    return {
        "factor": "Alt Attribute Coverage",
        "value": sum(1 for img in soup.find_all("img") if img.get("alt"))
    }
