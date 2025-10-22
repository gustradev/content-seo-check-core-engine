# core/modules/url_mode/factor_024.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Returns the character length of the Open Graph Description (<meta property="og:description">).
    Returns 0 if the tag is missing.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            og_desc = soup.find('meta', property='og:description')
            
            if og_desc and og_desc.get('content'):
                value = len(og_desc['content'].strip())
        except Exception:
            pass

    return {
        "factor": "Open Graph Description Length",
        "value": value
    }