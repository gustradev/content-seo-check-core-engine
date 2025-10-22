# core/modules/text_mode/factor_026.py
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# NOTE: Since the engine runs on 'content' (which may be a full HTML page), 
# determining 'internal' vs 'external' is hard without knowing the page's domain.
# We will use a simple heuristic: links starting with '#' or '/' are internal.
def is_internal(href):
    if not href:
        return False
    # Relative paths or hash links
    if href.startswith('/') or href.startswith('#'):
        return True
    
    # Check if the URL has no netloc (e.g., just 'page.html')
    parsed = urlparse(href)
    return not parsed.netloc

def check(content: str) -> dict:
    """
    Counts the number of anchors that appear to be internal links.
    """
    value = 0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a', href=True)
            
            value = sum(1 for link in links if is_internal(link['href']))
        except Exception:
            pass

    return {
        "factor": "Internal Links Count",
        "value": value
    }