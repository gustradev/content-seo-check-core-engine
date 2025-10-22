# core/modules/url_mode/factor_019.py
from bs4 import BeautifulSoup

# Common class names or link components for share buttons
SHARE_INDICATORS = [
    'share-button', 'social-icon', 'fa-share', 'twitter-share', 
    'facebook-share', 'linkedin-share', 'pinterest-share', 'sharethis'
]

def check(html: str) -> dict:
    """
    Counts the total number of elements that appear to be social share buttons 
    based on common class names or link patterns.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # Search for elements containing any of the indicator strings in their class
            elements_by_class = soup.find_all(class_=lambda c: c and any(ind in c.lower() for ind in SHARE_INDICATORS))
            value += len(elements_by_class)
            
            # Also check for explicit sharing links (often not covered by class check)
            value += len(soup.find_all('a', href=lambda href: href and ('twitter.com/intent/tweet' in href or 'facebook.com/sharer' in href)))

        except Exception:
            pass

    return {
        "factor": "Social Share Button Count",
        "value": value
    }