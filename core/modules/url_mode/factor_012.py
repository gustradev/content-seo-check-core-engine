# core/modules/url_mode/factor_012.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Measures "Mixed Content" by counting elements that explicitly load resources
    via the insecure 'http://' protocol. Lower count is better.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # Look for all tags that contain an href or src attribute
            insecure_elements = soup.find_all(lambda tag: 
                (tag.get('href') and tag['href'].lower().startswith('http://')) or 
                (tag.get('src') and tag['src'].lower().startswith('http://'))
            )
            
            value = len(insecure_elements)
        except Exception:
            pass

    return {
        "factor": "Insecure Resource Count (Mixed Content)",
        "value": value
    }