# core/modules/text_mode/factor_020.py
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Extracts the <title> tag text and returns its character length (requires HTML parsing).
    """
    value = 0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.find('title')
            
            if title_tag and title_tag.string:
                # Strip whitespace and count characters
                value = len(title_tag.string.strip()) 
        except Exception:
            # Silently handle parsing errors
            pass

    return {
        "factor": "Meta Title Length",
        "value": value
    }