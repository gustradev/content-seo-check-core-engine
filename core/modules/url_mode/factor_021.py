# core/modules/url_mode/factor_021.py
from bs4 import BeautifulSoup

def check(html: str) -> dict:
    """
    Checks if the meta robots tag contains the 'noindex' directive.
    Returns 1 if 'noindex' is found, 0 if it is absent.
    (1 indicates that the page is explicitly blocked from indexing).
    """
    value = 0
    if html:
        try:
            # Parse the HTML content
            soup = BeautifulSoup(html, 'html.parser')
            
            # Find the <meta name="robots"> tag
            meta_robots = soup.find('meta', attrs={'name': 'robots'})
            
            # Check if the tag exists and has a content attribute
            if meta_robots and meta_robots.get('content'):
                # Normalize content to lowercase for robust checking
                content = meta_robots['content'].lower()
                
                # Check for the 'noindex' directive
                if 'noindex' in content:
                    value = 1 # Found 'noindex'
        except Exception:
            # Fail gracefully if parsing encounters an error
            pass

    return {
        "factor": "Meta Robots Noindex (Found)",
        "value": value
    }