# core/modules/url_mode/factor_027.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Detects the presence of a favicon link tag with a non-empty href.
    Returns 1 if found, 0 if missing.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            # Look for common rel values
            favicon = soup.find('link', rel=lambda r: r and ('icon' in r or 'shortcut icon' in r))
            
            if favicon and favicon.get('href', '').strip():
                value = 1
        except Exception:
            pass

    return {
        "factor": "Favicon Presence",
        "value": value
    }