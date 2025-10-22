# core/modules/url_mode/factor_002.py
from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, "html.parser")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    content = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else ""
    return {
        "factor": "Meta Description Length",
        "value": len(content)
    }
