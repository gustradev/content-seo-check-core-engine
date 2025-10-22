# core/modules/url_mode/factor_013.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Counts the number of detected structured data blocks (LD+JSON, Microdata, or RDFa).
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # Count 1: LD+JSON scripts
            value += len(soup.find_all('script', {'type': 'application/ld+json'}))
            
            # Count 2: Microdata (itemscope attribute)
            value += len(soup.find_all(attrs={'itemscope': True}))
            
            # Count 3: RDFa (typeof attribute)
            value += len(soup.find_all(attrs={'typeof': True}))
            
        except Exception:
            pass

    return {
        "factor": "Structured Data Block Count",
        "value": value
    }