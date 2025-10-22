# core/modules/url_mode/factor_003.py
from bs4 import BeautifulSoup

def check(html):
    if not html:
        return {"factor": "H1 Tag Count", "value": 0}

    soup = BeautifulSoup(html, "html.parser")
    h1_tags = soup.find_all("h1") if soup else []

    return {
        "factor": "H1 Tag Count",
        "value": len(h1_tags)
    }
