# core/modules/url_mode/factor_007.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    internal = [a for a in soup.find_all("a", href=True) if a["href"].startswith("/")]
    return {
        "factor": "Internal Link Count",
        "value": len(internal)
    }
