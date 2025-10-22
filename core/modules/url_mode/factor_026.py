# core/modules/url_mode/factor_026.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Checks for the presence of a properly configured viewport meta tag.
    Returns 1 if found, 0 if missing.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            viewport = soup.find('meta', attrs={'name': 'viewport'})
            
            if viewport and viewport.get('content'):
                content_value = viewport['content'].lower()
                # Check for the key components
                if 'width=device-device' in content_value and 'initial-scale=1' in content_value:
                    value = 1
        except Exception:
            pass

    return {
        "factor": "Viewport Meta Tag (Full Check)",
        "value": value
    }