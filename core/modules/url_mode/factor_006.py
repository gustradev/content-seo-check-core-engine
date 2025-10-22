# core/modules/url_mode/factor_006.py
from bs4 import BeautifulSoup

def check(html):
    if not html:
        return {"factor": "Total Link Count", "value": 0}

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", href=True) if soup else []

    return {
        "factor": "Total Link Count",
        "value": len(links)
    }
