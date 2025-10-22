# core/modules/url_mode/factor_022.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Checks if the meta robots tag contains the 'nofollow' directive.
    Returns 1 if 'nofollow' is found, 0 if it is absent.
    (1 indicates that all links on the page are marked as not passing authority).
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            meta_robots = soup.find('meta', attrs={'name': 'robots'})
            
            if meta_robots and meta_robots.get('content'):
                content = meta_robots['content'].lower()
                if 'nofollow' in content:
                    value = 1
        except Exception:
            pass

    return {
        "factor": "Meta Robots Nofollow (Found)",
        "value": value
    }