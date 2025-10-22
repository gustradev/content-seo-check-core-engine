# core/modules/text_mode/factor_022.py
from bs4 import BeautifulSoup

# WARNING: In a real system, the KEYWORD should be passed to check() or fetched dynamically.
# For compatibility with your current structure, we use a placeholder keyword.
PLACEHOLDER_KEYWORD = "seo" 

def check(content: str) -> dict:
    """
    Checks if the Primary Keyword is present in the <title> tag.
    Returns 1 if present, 0 if absent.
    """
    value = 0
    if content and PLACEHOLDER_KEYWORD:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.find('title')
            
            if title_tag and title_tag.string:
                title_text = title_tag.string.lower()
                keyword_lower = PLACEHOLDER_KEYWORD.lower()
                
                if keyword_lower in title_text:
                    value = 1 # Found
        except Exception:
            pass

    return {
        "factor": "Keyword in Title",
        "value": value
    }