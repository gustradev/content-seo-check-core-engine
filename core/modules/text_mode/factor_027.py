# core/modules/text_mode/factor_027.py
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# NOTE: This is the inverse logic of is_internal from factor_026
def is_external(href):
    if not href:
        return False
    # Full URLs (http/https/ftp) are usually external
    if href.startswith('http') or href.startswith('ftp'):
        return True
    
    # Check for a network location (domain)
    parsed = urlparse(href)
    # If it has a netloc (and isn't just a relative path), we assume external
    return bool(parsed.netloc)

def check(content: str) -> dict:
    """
    Counts the number of anchors that appear to be external links.
    """
    value = 0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a', href=True)
            
            value = sum(1 for link in links if is_external(link['href']))
        except Exception:
            pass

    return {
        "factor": "External Links Count",
        "value": value
    }