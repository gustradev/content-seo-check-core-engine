# core/modules/url_mode/factor_025.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Checks for the presence of the Twitter Card type tag (<meta name="twitter:card">).
    Returns 1 if found, 0 if missing.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            twitter_card = soup.find('meta', attrs={'name': 'twitter:card'})
            
            if twitter_card and twitter_card.get('content', '').strip():
                value = 1
        except Exception:
            pass

    return {
        "factor": "Twitter Card Presence",
        "value": value
    }