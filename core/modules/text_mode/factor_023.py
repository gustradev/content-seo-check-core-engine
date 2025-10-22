# core/modules/text_mode/factor_023.py
from bs4 import BeautifulSoup

# WARNING: In a real system, the KEYWORD should be passed to check() or fetched dynamically.
PLACEHOLDER_KEYWORD = "seo" 

def check(content: str) -> dict:
    """
    Counts the number of H2 or H3 subheadings containing the Primary Keyword.
    """
    value = 0
    if content and PLACEHOLDER_KEYWORD:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            subheadings = soup.find_all(['h2', 'h3'])
            keyword_lower = PLACEHOLDER_KEYWORD.lower()
            
            for tag in subheadings:
                if tag.text and keyword_lower in tag.text.lower():
                    value += 1
        except Exception:
            pass

    return {
        "factor": "Keyword in Subheadings",
        "value": value
    }