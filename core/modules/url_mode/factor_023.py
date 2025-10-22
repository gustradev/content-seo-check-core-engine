# core/modules/url_mode/factor_023.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Returns the character length of the Open Graph Title (<meta property="og:title">).
    Returns 0 if the tag is missing.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            og_title = soup.find('meta', property='og:title')
            
            if og_title and og_title.get('content'):
                value = len(og_title['content'].strip())
        except Exception:
            pass

    return {
        "factor": "Open Graph Title Length",
        "value": value
    }