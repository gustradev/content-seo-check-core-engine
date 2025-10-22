# core/modules/url_mode/factor_002.py
from bs4 import BeautifulSoup

def check(html):
    if not html:
        return {"factor": "Meta Description Length", "value": 0}

    soup = BeautifulSoup(html, "html.parser")
    meta_desc = soup.find("meta", attrs={"name": "description"})

    content = ""
    if meta_desc and meta_desc.get("content"):
        content = meta_desc["content"].strip()

    return {
        "factor": "Meta Description Length",
        "value": len(content)
    }
