# core/modules/text_mode/factor_018.py
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Counts the number of H1 tags in the content (requires HTML parsing).
    """
    value = 0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            value = len(soup.find_all('h1'))
        except Exception:
            # Silently handle parsing errors
            pass

    return {
        "factor": "H1 Presence Count",
        "value": value
    }