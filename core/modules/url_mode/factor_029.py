# core/modules/url_mode/factor_029.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Proxies Broken Links Count by counting the total number of unique links (a tags with href) 
    found on the page, as a real check requires external requests for each one.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', href=True)
            
            # Count the number of unique target URLs
            unique_targets = set(link['href'] for link in links)
            value = len(unique_targets)
        except Exception:
            pass

    return {
        "factor": "Link Count (Broken Link Proxy further premiums plus needed)",
        "value": value
    }