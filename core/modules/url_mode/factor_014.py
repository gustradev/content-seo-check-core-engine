# core/modules/url_mode/factor_014.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Checks for the presence of a valid <link rel="canonical"> tag with an href attribute.
    Returns 1 if present and valid, 0 if missing or empty.
    (Cannot check for URL match without the actual page URL).
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            canonical_tag = soup.find('link', rel='canonical')
            
            if canonical_tag and canonical_tag.get('href', '').strip():
                value = 1
        except Exception:
            pass

    return {
        "factor": "Canonical URL Presence",
        "value": value
    }