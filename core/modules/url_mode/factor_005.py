# core/modules/url_mode/factor_005.py
from bs4 import BeautifulSoup

def check(html):
    if not html:
        return {"factor": "Image Count", "value": 0}

    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img") if soup else []

    return {
        "factor": "Image Count",
        "value": len(images)
    }
