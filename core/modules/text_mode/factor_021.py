# core/modules/text_mode/factor_021.py
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Extracts the <meta name="description"> content and returns its character length.
    """
    value = 0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            meta_tag = soup.find('meta', attrs={'name': 'description'})
            
            if meta_tag and 'content' in meta_tag.attrs:
                # Strip whitespace and count characters
                value = len(meta_tag['content'].strip()) 
        except Exception:
            pass

    return {
        "factor": "Meta Description Length",
        "value": value
    }