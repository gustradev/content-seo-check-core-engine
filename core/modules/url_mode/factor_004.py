# core/modules/url_mode/factor_004.py
from bs4 import BeautifulSoup

def check(html):
    if not html:
        return {"factor": "H2 Tag Count", "value": 0}

    soup = BeautifulSoup(html, "html.parser")
    h2_tags = soup.find_all("h2") if soup else []

    return {
        "factor": "H2 Tag Count",
        "value": len(h2_tags)
    }
