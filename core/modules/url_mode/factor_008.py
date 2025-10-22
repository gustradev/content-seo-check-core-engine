# core/modules/url_mode/factor_008.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    external = [a for a in soup.find_all("a", href=True) if a["href"].startswith("http")]
    return {
        "factor": "External Link Count",
        "value": len(external)
    }
